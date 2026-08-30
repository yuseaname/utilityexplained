#!/usr/bin/env python3
"""Rybbit snapshot fetcher — pulls a fresh analytics baseline for utilityexplained.

Auth: Bearer key from ~/.config/rybbit/api_key (never printed).
API: https://app.rybbit.io/api/sites/{site_id}/...  (docs: rybbit.com/docs/api)

Usage: python3 scripts/rybbit_snapshot.py [outdir]   (default: .rybbit-snapshot-<today>)
"""
import json
import time
import os
import sys
import urllib.request
import urllib.parse
from datetime import date, timedelta
from pathlib import Path

BASE = "https://app.rybbit.io/api/sites"
SITE = "d5b63e065e9d"
TZ = "America/New_York"


def get_key():
    for candidate in (os.path.expanduser("~/.config/rybbit/api_key"), os.environ.get("RYBBIT_API_KEY", "")):
        if candidate and Path(candidate).is_file():
            return Path(candidate).read_text().strip()
        if candidate:
            return candidate.strip()
    raise SystemExit("no rybbit api key found")


def fetch(key, path, params, retries=4):
    qs = urllib.parse.urlencode(params)
    url = f"{BASE}/{SITE}/{path}?{qs}"
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {key}",
            "User-Agent": "rybbit-snapshot/1.0",  # WAF blocks default Python-urllib UA
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                time.sleep(20 * (attempt + 1))  # rate limit: back off hard
                continue
            raise
    return {}


def fetch_events(key, max_pages=40):
    """Pull raw events with stuck-cursor protection + dedupe.

    Rybbit API quirk (observed 2026-08): the events cursor can return
    identical pages forever (100% overlap). Three guards:
      1. stop when a page's payload signature repeats,
      2. dedupe every event by (session_id, timestamp, pathname),
      3. hard page cap.
    Without these, one real pageview can be counted ~60x and poison KPIs
    (SQ-060: 2,950 raw events -> 49 unique pageviews).
    """
    out, seen, prev_sig = [], set(), None
    cursor = ""
    for _ in range(max_pages):
        params = {"limit": 100, "time_zone": TZ}
        if cursor:
            params["cursor"] = cursor
        d = fetch(key, "events", params)
        data = d.get("data") or []
        sig = tuple(sorted((e.get("session_id",""), e.get("timestamp",""), e.get("pathname","")) for e in data))
        if not data or sig == prev_sig:
            break
        prev_sig = sig
        fresh = 0
        for e in data:
            k = (e.get("session_id"), e.get("timestamp"), e.get("pathname"))
            if k not in seen:
                seen.add(k); out.append(e); fresh += 1
        if fresh == 0:
            break
        cur = d.get("cursor") or {}
        if not cur.get("hasMore"):
            break
        cursor = cur.get("oldestTimestamp") or cursor
    return out


def main():
    today = date.today()
    outdir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(f".rybbit-snapshot-{today}")
    outdir.mkdir(exist_ok=True)
    key = get_key()

    windows = {
        "last7": (today - timedelta(days=7), today),
        "prior7": (today - timedelta(days=14), today - timedelta(days=7)),
        "last30": (today - timedelta(days=30), today),
    }

    snapshot = {"date": str(today), "site_id": SITE, "windows": {}}

    for name, (start, end) in windows.items():
        w = {"start": str(start), "end": str(end)}
        w["overview"] = fetch(key, "overview", {"start_date": str(start), "end_date": str(end), "time_zone": TZ})
        for label, param, limit in (
            ("pages", "pathname", 150),
            ("referrers", "referrer", 40),
            ("channels", "channel", 15),
            ("countries", "country", 25),
        ):
            w[label] = fetch(key, "metric", {
                "parameter": param, "start_date": str(start), "end_date": str(end),
                "time_zone": TZ, "limit": limit,
            })
        snapshot["windows"][name] = w
        print(f"[ok] {name} ({start} -> {end})")

    (outdir / "snapshot.json").write_text(json.dumps(snapshot, indent=1))

    # Raw events with dedupe (see fetch_events docstring — SQ-060)
    events = fetch_events(key)
    (outdir / "events_deduped.json").write_text(json.dumps(
        {"fetched": str(today), "unique_events": len(events), "events": events}, indent=1))
    sessions = {e.get("session_id") for e in events}
    print(f"[ok] events: {len(events)} unique, {len(sessions)} sessions "
          f"(deduped; guard active for stuck cursor)")

    # Compact digest for humans
    for name in windows:
        ov = snapshot["windows"][name]["overview"].get("data", {})
        print(f"\n=== {name} ===")
        print(json.dumps(ov, indent=1)[:800])
    print(f"\nsaved -> {outdir}/snapshot.json")


if __name__ == "__main__":
    main()
