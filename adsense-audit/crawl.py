#!/usr/bin/env python3
"""AdSense low-value-content audit — crawl every sitemap URL and extract quality signals.

Writes data/crawl-results.json keyed by URL path. Rerunnable; state lives in
data/inventory.json (per-page status). Usage: python3 crawl.py [--only PENDING]
"""
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from html import unescape

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUD = os.path.dirname(os.path.abspath(__file__))
INV = os.path.join(AUD, "data", "inventory.json")
OUT = os.path.join(AUD, "data", "crawl-results.json")
DOMAIN = "https://utilityexplained.com"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"


class PageParser(HTMLParser):
    """Extract signals from rendered HTML. Tracks a stack of section contexts to
    isolate <main>/<article> text from nav/footer boilerplate."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.in_main = 0
        self.text_parts = []
        self.title = []
        self.in_title = 0
        self.meta = {}
        self.links = []
        self.imgs = []
        self.h1 = []; self.h2 = 0; self.h3 = 0
        self.cur_h1 = None
        self.jsonld = []
        self._buf = None
        self.tables = 0
        self.iframe = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.stack.append(tag)
        if tag in ("main", "article"):
            self.in_main += 1
        if tag == "title": self.in_title += 1
        if tag == "meta":
            name = (a.get("name") or a.get("property") or "").lower()
            if name: self.meta[name] = (a.get("content") or "").strip()
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img":
            self.imgs.append({"src": a.get("src") or a.get("data-src") or "", "alt": a.get("alt", "")})
        if tag in ("h1",):
            self.cur_h1 = []
        if tag == "h2": self.h2 += 1
        if tag == "h3": self.h3 += 1
        if tag == "table": self.tables += 1
        if tag == "iframe": self.iframe += 1
        if tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self._buf = []

    def handle_endtag(self, tag):
        if tag in ("main", "article") and self.in_main: self.in_main -= 1
        if tag == "title": self.in_title = 0
        if tag == "h1" and self.cur_h1 is not None:
            self.h1.append(" ".join("".join(self.cur_h1).split()))
            self.cur_h1 = None
        if tag == "script" and self._buf is not None:
            self.jsonld.append("".join(self._buf)); self._buf = None
        if self.stack and self.stack[-1] == tag: self.stack.pop()

    def handle_data(self, data):
        if self._buf is not None: self._buf.append(data)
        if self.in_title: self.title.append(data)
        if self.cur_h1 is not None: self.cur_h1.append(data)
        if self.in_main or (self.stack and self.stack[-1] == "td"):
            self.text_parts.append(data)


def fetch(url):
    r = subprocess.run(["curl", "-s", "-L", "-A", UA, "-w", "\n__HTTP__%{http_code}__URL__%{url_effective}",
                        "--max-time", "45", url], capture_output=True, text=True, timeout=60)
    body = r.stdout
    m = re.search(r"\n__HTTP__(\d+)__URL__(.*)$", body)
    code = int(m.group(1)) if m else 0
    final = m.group(2) if m else url
    if m: body = body[:m.start()]
    return code, final, body


def analyze(path):
    url = DOMAIN + (path if path != "/" else "/")
    try:
        code, final, body = fetch(url)
    except Exception as e:
        return path, {"http": 0, "error": str(e)}
    p = PageParser()
    try:
        p.feed(body)
    except Exception as e:
        return path, {"http": code, "parse_error": str(e)}

    text = unescape(" ".join(" ".join(p.text_parts).split()))
    words = len(text.split())

    # links
    internal, external, amazon = set(), set(), 0
    for href in p.links:
        h = href.strip()
        if not h or h.startswith(("#", "mailto:", "tel:", "javascript:")): continue
        if h.startswith("/") or "utilityexplained.com" in h:
            internal.add(h.split("#")[0].split("?")[0])
        else:
            external.add(h.split("#")[0])
            if "amazon.com" in h: amazon += 1

    # schema
    schema_types = []
    for js in p.jsonld:
        try:
            d = json.loads(js)
            for obj in (d if isinstance(d, list) else [d]):
                t = obj.get("@type")
                if isinstance(t, list): schema_types.extend(t)
                elif t: schema_types.append(t)
        except Exception:
            schema_types.append("__INVALID_JSON__")

    lowtext = text.lower()
    sig = {
        "http": code,
        "redirect": final.rstrip("/") != url.rstrip("/"),
        "final_url": final,
        "title": unescape("".join(p.title).strip()),
        "title_len": len(unescape("".join(p.title).strip())),
        "desc": p.meta.get("description", ""),
        "desc_len": len(p.meta.get("description", "")),
        "canonical": p.meta.get("canonical", "") if False else None,  # canonical is link tag, below
        "h1_count": len(p.h1), "h1": p.h1[0] if p.h1 else None,
        "h2_count": p.h2, "h3_count": p.h3,
        "words_main": words,
        "imgs": len(p.imgs),
        "imgs_no_alt": sum(1 for i in p.imgs if not (i["alt"] or "").strip()),
        "internal_links": len(internal),
        "external_links": len(external),
        "ext_domains": sorted({re.sub(r"^www\\.", "", (u.split("/")[2] if "://" in u else u)) for u in external})[:12],
        "amazon_links": amazon,
        "schema": sorted(set(schema_types)),
        "tables": p.tables,
        "iframes": p.iframe,
        "og_image": bool(p.meta.get("og:image")),
        "date_published": p.meta.get("article:published_time", ""),
        "date_modified": p.meta.get("article:modified_time", ""),
        "has_faq_schema": "FAQPage" in schema_types,
        "has_affiliate_disclosure": ("affiliate" in lowtext),
        "adsense": ("adsbygoogle" in body or "pagead2" in body),
        "word_repeat_top": None,  # filled by analysis pass
        "html_bytes": len(body),
    }
    # canonical via link tag
    mcan = re.search(r'<link[^>]+rel=["\']?canonical["\']?[^>]+href=["\']?([^"\' >]+)', body)
    sig["canonical"] = mcan.group(1) if mcan else None
    return path, sig


def main():
    only_pending = "--only-pending" in sys.argv
    inv = json.load(open(INV))
    prev = {}
    if os.path.exists(OUT):
        prev = json.load(open(OUT))
    targets = [i["path"] for i in inv if not (only_pending and i.get("status") not in (None, "PENDING"))]
    targets = [t for t in targets if t not in prev] if "--new" in sys.argv else targets
    print(f"crawling {len(targets)} pages...")
    results = {}
    with ThreadPoolExecutor(max_workers=10) as ex:
        futs = {ex.submit(analyze, t): t for t in targets}
        done = 0
        for f in as_completed(futs):
            path, sig = f.result()
            results[path] = sig
            done += 1
            if done % 25 == 0: print(f"  {done}/{len(targets)}")
    merged = {**prev, **results}
    json.dump(merged, open(OUT, "w"), indent=1)
    bad = [p for p, s in merged.items() if s.get("http") != 200]
    print(f"done: {len(merged)} pages in crawl-results.json; non-200: {len(bad)}")
    for p in bad: print("  NON200:", p, merged[p].get("http"))


if __name__ == "__main__":
    main()
