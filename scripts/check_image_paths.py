#!/usr/bin/env python3
"""check_image_paths.py — pre-publish image integrity gate.

Fails the build when an image is referenced but missing on disk, which is
exactly how the "3 broken Keep Reading cards" regression shipped: front matter
pointed at files that no longer existed.

Two passes:
  1. Source pass  — every content file's front-matter `image:` (and
     `og_image`/`favicon`-style params) must resolve under static/.
  2. Build pass   — every <img src>, <source srcset>, poster, and CSS url()
     in public/**/*.html must resolve under public/. (Run after `hugo`.)

Usage:
  python3 scripts/check_image_paths.py [SITE_ROOT]

Exit code 0 = all referenced images exist; 1 = missing images (listed).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

IMG_SRC = re.compile(
    r"""(?:<img[^>]+?\bsrc|<source[^>]+?\bsrcset|poster)=["']([^"']+)["']""",
    re.IGNORECASE,
)
CSS_URL = re.compile(r"""url\((["']?)(/[^"')]+)\1\)""", re.IGNORECASE)
SRCSET_ITEM = re.compile(r"^\s*(\S+?)(?:\s+\S+w)?\s*$")
FRONT_MATTER_IMAGE = re.compile(r"^\s*(image|og_image|favicon|hero_image)\s*:\s*[\"']?(/[^\"'\s]+)[\"']?", re.MULTILINE)

EXTERNAL = ("http://", "https://", "//", "data:", "#", "mailto:")


def is_local(ref: str) -> bool:
    return not ref.startswith(EXTERNAL)


def check_source_pass(root: Path) -> list[str]:
    """Front-matter image params in content/ must exist under static/."""
    problems = []
    for md in (root / "content").rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---"):
            continue
        end = text.find("\n---", 3)
        if end == -1:
            continue
        for _field, ref in FRONT_MATTER_IMAGE.findall(text[:end]):
            if not is_local(ref):
                continue
            if not (root / "static" / ref.lstrip("/")).is_file():
                problems.append(f"{md.relative_to(root)}: front-matter image missing -> {ref}")
    return problems


def _expand_srcset(value: str) -> list[str]:
    refs = []
    for part in value.split(","):
        m = SRCSET_ITEM.match(part)
        if m and m.group(1):
            refs.append(m.group(1))
    return refs


def check_build_pass(root: Path) -> list[str]:
    """Local asset refs in built HTML must exist under public/."""
    problems = []
    public = root / "public"
    if not public.is_dir():
        return problems  # build pass skipped when public/ absent
    for html in public.rglob("*.html"):
        text = html.read_text(encoding="utf-8", errors="replace")
        refs = [m for m in IMG_SRC.findall(text)]
        for _q, ref in CSS_URL.findall(text):
            refs.append(ref)
        # srcset attributes may hold multiple candidates
        for attr in re.findall(r"""srcset=["']([^"']+)["']""", text, re.IGNORECASE):
            refs.extend(_expand_srcset(attr))
        for ref in refs:
            ref = ref.split("?")[0].split("#")[0]
            if not ref or not is_local(ref) or not ref.startswith("/"):
                continue
            if not (public / ref.lstrip("/")).is_file():
                problems.append(f"{html.relative_to(root)}: missing asset -> {ref}")
    return problems


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    problems = check_source_pass(root) + check_build_pass(root)
    if problems:
        print(f"FAIL — {len(problems)} missing image reference(s):")
        for p in sorted(set(problems)):
            print(f"  {p}")
        return 1
    print("OK — all referenced images resolve on disk.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
