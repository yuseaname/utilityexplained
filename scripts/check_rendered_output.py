#!/usr/bin/env python3
"""Fail the build if rendered HTML contains leaked shortcode markup.

SQ-064 lesson (2026-08-30): single-brace `{< ... >}` shortcodes in article
markdown render as literal text on the live site while every content-side
gate (image-path check, content audit) still passes — the files exist and
the text parses. The only reliable detection point is the RENDERED output.
This script greps public/ for the escaped and raw leak signatures and
exits 1 if any are found.

Usage: python3 scripts/check_rendered_output.py [root=public]
"""
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "public")

# Escaped form (Hugo/minify renders `{<` as `{&lt;`) and raw fallback.
PATTERNS = [
    re.compile(r"\{&lt;\s*/?\s*(visual|product-box|faq|amazon|affiliate-disclosure|image)"),
    re.compile(r"\{<\s*(visual|product-box)"),
]

# 2026-10-28 attribution gate: every amazon.com URL anywhere in rendered HTML
# (hrefs, JSON-LD citation schema, inline text) must carry tag= — untagged
# ones earn under Associates "Other" with zero per-site attribution.
# Char class includes backslash so JSON-escaped URLs (\u0026tag=...) match fully.
AMZ_URL = re.compile(r"https?://(?:www\.)?amazon\.com/[^\s\"'<>)]*")

def main() -> int:
    if not root.is_dir():
        print(f"FAIL — rendered root not found: {root}")
        return 1
    bad = []
    for page in root.rglob("*.html"):
        text = page.read_text(errors="ignore")
        for pat in PATTERNS:
            for m in pat.finditer(text):
                bad.append(f"{page.relative_to(root)}: ...{m.group(0)[:50]}...")
        for m in AMZ_URL.finditer(text):
            if "tag=" not in m.group(0):
                bad.append(f"{page.relative_to(root)}: untagged amazon URL: {m.group(0)[:90]}")
    if bad:
        print(f"FAIL — leaked markup / untagged Amazon URLs at {len(bad)} location(s):")
        for line in bad[:20]:
            print(" ", line)
        return 1
    print("OK — no leaked shortcode markup in rendered HTML.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
