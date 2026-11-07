#!/usr/bin/env python3
"""health_check.py — weekly site health snapshot for the AdSense restoration project.

Checks: sitemap URL count, sampled redirect integrity (all 35 slug-drop 301s),
key page 200s, literal-leak spot check, Rybbit 7-day sessions.
Writes adsense-audit/data/health/YYYY-MM-DD.json. Run from repo root:
python3 adsense-audit/health_check.py
"""
import json, os, re, subprocess, sys, datetime
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://utilityexplained.com"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124"
RYBBIT_SITE = "4987"

def curl(url, extra=None, timeout=45):
    cmd = ["curl", "-s", "-A", UA, "--max-time", str(timeout)] + (extra or []) + [url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 15)
    return r.stdout

def main():
    today = datetime.date.today().isoformat()
    out = {"date": today, "checks": {}}

    # 1. sitemap
    sm = curl(f"{DOMAIN}/sitemap.xml")
    urls = re.findall(r"<loc>([^<]+)</loc>", sm)
    out["checks"]["sitemap_urls"] = len(urls)
    out["checks"]["numbered_slugs"] = sum(1 for u in urls if re.search(r"/blog/\d{1,2}-", u))

    # 2. redirect integrity (sequential pairs, gentle)
    mapping_file = os.path.join(ROOT, "scripts", ".slug-rename-map.json")
    redirects = {"ok": 0, "bad": []}
    if os.path.exists(mapping_file):
        mapping = json.load(open(mapping_file))
        for old, new in mapping:
            r = curl(f"{DOMAIN}{old}", extra=["-o", "/dev/null", "-w", "%{http_code} %{redirect_url}"])
            parts = r.split(" ", 1)
            if parts[0] == "301" and len(parts) > 1 and parts[1].rstrip("/") == f"{DOMAIN}{new.rstrip('/')}":
                redirects["ok"] += 1
            else:
                redirects["bad"].append({"old": old, "result": r.strip()})
    out["checks"]["redirects"] = redirects

    # 3. key pages 200
    key_pages = ["/", "/blog/", "/electricity-explained/", "/water-explained/",
                 "/blog/average-utility-bills-in-texas/", "/calculators/"]
    def page_ok(p):
        code = curl(f"{DOMAIN}{p}", extra=["-o", "/dev/null", "-w", "%{http_code}"])
        return p, code.strip()
    pages = {}
    with ThreadPoolExecutor(max_workers=3) as ex:
        for p, code in ex.map(page_ok, key_pages):
            pages[p] = code
    out["checks"]["key_pages"] = pages

    # 4. literal-heading leak spot check (3 previously-fixed pages)
    leaks = 0
    for p in ["blog/why-is-my-heating-bill-so-high", "gas-explained", "electricity-explained"]:
        body = curl(f"{DOMAIN}/{p}/")
        leaks += len(re.findall(r">#{1,6} [A-Za-z]", body))
    out["checks"]["literal_heading_leaks"] = leaks

    # 5. Rybbit 7-day sessions (key at ~/.config/rybbit/api_key)
    # NOTE: /overview ignores date params (all-time) — sum overview/time-series daily buckets instead
    try:
        key = open(os.path.expanduser("~/.config/rybbit/api_key")).read().strip()
        import time
        end = datetime.date.today()
        start = end - datetime.timedelta(days=7)
        ts = curl(f"https://app.rybbit.io/api/sites/{RYBBIT_SITE}/overview/time-series?start_date={start.isoformat()}&end_date={end.isoformat()}",
                  extra=["-H", f"Authorization: Bearer {key}"])
        d = json.loads(ts)
        if isinstance(d, dict):
            d = d.get("data", d)
        buckets = d.get("data", d) if isinstance(d, dict) and not isinstance(d, list) else d
        sessions = sum(int(b.get("visitors", b.get("sessions", 0)) or 0) for b in buckets if isinstance(b, dict))
        out["checks"]["rybbit_7d_sessions"] = sessions
        out["checks"]["rybbit_7d_buckets"] = len([b for b in buckets if isinstance(b, dict)])
    except Exception as e:
        out["checks"]["rybbit_7d_sessions"] = f"unavailable: {e}"

    # verdict
    healthy = (out["checks"]["sitemap_urls"] >= 170 and out["checks"]["numbered_slugs"] == 0
               and not redirects["bad"] and all(v == "200" for v in pages.values())
               and leaks == 0)
    out["verdict"] = "HEALTHY" if healthy else "ATTENTION"
    dest = os.path.join(ROOT, "adsense-audit", "data", "health", f"{today}.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    json.dump(out, open(dest, "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "checks"}, indent=1))
    print("checks:", json.dumps(out["checks"], indent=1)[:800])
    print(f"written: {dest}")

if __name__ == "__main__":
    main()
