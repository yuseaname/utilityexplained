#!/usr/bin/env python3
"""drop_number_prefixes.py — remove batch-number prefixes from blog slugs (AdSense P1-A).

For every content/blog/*.md whose slug (or filename) starts with NN-, this script:
  1. sets slug front matter to the prefix-free version,
  2. appends the old URL to aliases (Hugo emits a redirect stub),
  3. rewrites every /blog/<old>/ reference across all content/*.md to /blog/<new>/.

Prints the mapping for .htaccess generation. Idempotent: re-running finds nothing.
Run from repo root: python3 scripts/drop_number_prefixes.py
"""
import os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
BLOG = os.path.join(CONTENT, "blog")

def parse_front_matter(txt):
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m: return None, txt, None
    return m.group(1), txt[m.end():], m

def get(yaml_fm, key):
    m = re.search(rf'^{key}:\s*"?([^"\n]*)"?\s*$', yaml_fm, re.M)
    return m.group(1) if m else None

mapping = []  # (old_path, new_path)
changed_files = []

for fname in sorted(os.listdir(BLOG)):
    if not fname.endswith(".md") or fname == "_index.md": continue
    p = os.path.join(BLOG, fname)
    txt = open(p, encoding="utf-8").read()
    fm, body, m = parse_front_matter(txt)
    if fm is None:
        print(f"SKIP (no front matter): {fname}"); continue
    slug = get(fm, "slug") or os.path.splitext(fname)[0]
    mo = re.match(r"^(\d{1,2})-(.+)$", slug)
    if not mo: continue
    new_slug = mo.group(2)
    old_path, new_path = f"/blog/{slug}/", f"/blog/{new_slug}/"

    # 1. slug
    if get(fm, "slug"):
        new_fm = re.sub(rf'^(slug:\s*"?){re.escape(slug)}("?)\s*$', rf"\g<1>{new_slug}\g<2>", fm, flags=re.M)
    else:
        new_fm = fm + f'\nslug: "{new_slug}"'
    # 2. aliases — append old path
    if re.search(r"^aliases:", new_fm, re.M):
        if old_path not in new_fm:
            new_fm = re.sub(r"^(aliases:\s*\[)", rf"\g<1>{old_path}, ", new_fm, flags=re.M)
        else:
            print(f"  alias already present: {fname}")
    else:
        new_fm = new_fm + f'\naliases: ["{old_path}"]'
    open(p, "w", encoding="utf-8").write("---\n" + new_fm + "\n---\n" + body)
    mapping.append((old_path, new_path))
    changed_files.append(fname)

# 3. rewrite references everywhere in content/
link_edits = 0
for dirpath, _, files in os.walk(CONTENT):
    for f in files:
        if not f.endswith(".md"): continue
        fp = os.path.join(dirpath, f)
        t = open(fp, encoding="utf-8").read()
        orig = t
        for old, new in mapping:
            t = t.replace(old, new)
        if t != orig:
            open(fp, "w", encoding="utf-8").write(t)
            link_edits += 1

print(f"renamed slugs: {len(mapping)} | files with link rewrites: {link_edits}")
for old, new in mapping: print(f"  {old} -> {new}")
json.dump(mapping, open(os.path.join(ROOT, "scripts", ".slug-rename-map.json"), "w"), indent=1)
