#!/usr/bin/env python3
"""check_price_bands.py — staleness report for data/product_prices.yaml.

The product-box shortcode renders a band only while fresh (<= 75 days); after
that the band stops rendering silently (by design — a stale price never shows).
This script tells maintainers WHICH bands have gone dark so they can be
re-verified against the live Amazon listing and re-dated.

Run monthly (portfolio rhythm). Exit code 0 always — this is a report, not a gate.
"""
import datetime
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRICES = ROOT / "data" / "product_prices.yaml"
FRESH_DAYS = 75

ENTRY = re.compile(r"^([A-Z0-9]{10}):\s*$")


def main() -> int:
    if not PRICES.exists():
        print("no product_prices.yaml — nothing to check")
        return 0
    current, entries = None, {}
    for line in PRICES.read_text().splitlines():
        m = ENTRY.match(line)
        if m:
            current = m.group(1)
            entries[current] = {}
        elif current:
            km = re.match(r"^\s+(band|checked|source):\s*(.*)$", line)
            if km:
                entries[current][km.group(1)] = km.group(2).strip().strip('"')
    today = datetime.date.today()
    print(f"price-band freshness (threshold {FRESH_DAYS} days) — {today}")
    dark, soon, fresh = [], [], []
    for asin, e in sorted(entries.items()):
        try:
            checked = datetime.date.fromisoformat(e.get("checked", ""))
        except ValueError:
            print(f"  {asin}: UNPARSEABLE checked date {e.get('checked')!r}")
            continue
        age = (today - checked).days
        if age > FRESH_DAYS:
            dark.append((asin, age, e.get("band")))
        elif age > FRESH_DAYS - 15:
            soon.append((asin, age, e.get("band")))
        else:
            fresh.append((asin, age))
    for asin, age, band in dark:
        print(f"  DARK (stopped rendering)  {asin}  {band}  checked {age}d ago — re-verify or drop")
    for asin, age, band in soon:
        print(f"  due within 2 weeks        {asin}  {band}  checked {age}d ago")
    print(f"  fresh: {len(fresh)}  due-soon: {len(soon)}  dark: {len(dark)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
