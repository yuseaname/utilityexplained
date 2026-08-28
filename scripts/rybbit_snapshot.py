#!/usr/bin/env python3
"""Rybbit snapshot fetcher — pulls a fresh analytics baseline for utilityexplained.

Auth: Bearer key from ~/.config/rybbit/api_key (never printed).
API: https://app.rybbit.io/api/sites/{site_id}/...  (docs: rybbit.com/docs/api)

Usage: python3 scripts/rybbit_snapshot.py [outdir]   (default: .rybbit-snapshot-<today>)
"""
import json
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


def fetch(key, path, params):
    qs = urllib.parse.urlencode(params)
    url = f"{BASE}/{SITE}/{path}?{qs}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {key}",
        "User-Agent": "rybbit-snapshot/1.0",  # WAF blocks default Python-urllib UA
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


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

    # Compact digest for humans
    for name in windows:
        ov = snapshot["windows"][name]["overview"].get("data", {})
        print(f"\n=== {name} ===")
        print(json.dumps(ov, indent=1)[:800])
    print(f"\nsaved -> {outdir}/snapshot.json")


if __name__ == "__main__":
    main()
