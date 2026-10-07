#!/usr/bin/env python3
"""Migrate blog authorship from human personas to the desk model.

Rewrites the `author:` frontmatter line in content/blog/*.md from the five
legacy persona names to their topic-desk equivalents:

    Margaret Harrington -> Bills & Rates Desk
    David Chen          -> Home Energy Desk
    Marcia Washington   -> Affordability & Assistance Desk
    Roberto Mendoza     -> Heating & Cooling Desk
    Tanya Patterson     -> Consumer Rights Desk

Idempotent: running it twice is a no-op (desk values are left untouched).
Reports per-file old -> new counts and a grand total.

Usage:
    python3 scripts/migrate_authors.py [--dry-run]
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

# Exact persona string -> desk string. Match EXACT strings (case-sensitive).
DESK_MAP = {
    "Margaret Harrington": "Bills & Rates Desk",
    "David Chen": "Home Energy Desk",
    "Marcia Washington": "Affordability & Assistance Desk",
    "Roberto Mendoza": "Heating & Cooling Desk",
    "Tanya Patterson": "Consumer Rights Desk",
}

# Matches a frontmatter author line: `author: <value>` (value may be quoted).
AUTHOR_RE = re.compile(r'^(?P<indent>\s*)author:(?P<sp>\s*)(?P<value>.*?)(?P<trail>\s*)$')


def rewrite_value(raw: str) -> tuple[str, str | None]:
    """Return (new_raw, old_persona_or_None) for a raw author value.

    Preserves the original quoting style. Only rewrites when the unquoted
    value exactly equals a known persona name.
    """
    value = raw.strip()
    quote = ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        quote = value[0]
        inner = value[1:-1]
    else:
        inner = value

    if inner in DESK_MAP:
        new_inner = DESK_MAP[inner]
        return f"{quote}{new_inner}{quote}", inner
    return raw, None


def process_file(path: str, dry_run: bool) -> tuple[int, list[tuple[str, str]]]:
    """Rewrite author lines in one file. Returns (change_count, [(old,new),...])."""
    with open(path, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    changes: list[tuple[str, str]] = []
    out_lines = []
    for line in lines:
        m = AUTHOR_RE.match(line)
        if m:
            new_value, old_persona = rewrite_value(m.group("value"))
            if old_persona is not None:
                changes.append((old_persona, DESK_MAP[old_persona]))
                line = (
                    f"{m.group('indent')}author:{m.group('sp')}"
                    f"{new_value}{m.group('trail')}\n"
                )
        out_lines.append(line)

    if changes and not dry_run:
        with open(path, "w", encoding="utf-8") as fh:
            fh.writelines(out_lines)

    return len(changes), changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="report changes without writing files")
    parser.add_argument("--root", default=None,
                        help="repo root (default: parent of this script's dir)")
    args = parser.parse_args()

    root = args.root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pattern = os.path.join(root, "content", "blog", "*.md")
    files = sorted(glob.glob(pattern))

    total = 0
    files_changed = 0
    per_persona: dict[str, int] = {k: 0 for k in DESK_MAP}

    for path in files:
        count, changes = process_file(path, args.dry_run)
        if count:
            files_changed += 1
            total += count
            rel = os.path.relpath(path, root)
            detail = ", ".join(f"{o} -> {n}" for o, n in changes)
            print(f"{rel}: {count} change(s) [{detail}]")
            for old, _ in changes:
                per_persona[old] += 1

    print("-" * 60)
    print(f"files scanned : {len(files)}")
    print(f"files changed : {files_changed}")
    print(f"total changes : {total}")
    for persona, n in per_persona.items():
        print(f"  {persona:20s} -> {DESK_MAP[persona]:32s} : {n}")
    if args.dry_run:
        print("(dry run — no files written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
