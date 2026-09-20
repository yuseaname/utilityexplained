#!/usr/bin/env python3
"""Convert raw <h2 id="...">Text</h2> / <h3 id="...">Text</h3> headings to markdown
'## Text {#id}' form so Hugo's .TableOfContents and heading-aware tooling see them.

Preserves: anchor id, heading text verbatim, level. Skips headings inside shortcode
blocks. Anchor refs elsewhere (href="#id") are untouched and keep resolving because
markdown heading attrs render the same id.
"""
import re, pathlib

BASE = pathlib.Path("/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content")

H = re.compile(r'<h([23]) id="([^"]+)">([^<]+)</h\1>')

converted_files = 0
converted_total = 0
for f in sorted(BASE.rglob("*.md")):
    t = f.read_text(errors="ignore")
    m = H.findall(t)
    if not m:
        continue
    def repl(m):
        lvl, hid, txt = m.group(1), m.group(2), m.group(3).strip()
        return f"\n{'#' * int(lvl)} {txt} {{#{hid}}}\n"
    new = H.sub(repl, t)
    # collapse any triple+ newlines created at conversion seams
    new = re.sub(r"\n{4,}", "\n\n\n", new)
    f.write_text(new)
    converted_files += 1
    converted_total += len(m)
    print(f"{len(m):>3} headings: {f.relative_to(BASE)}")

print(f"\ndone: {converted_total} headings in {converted_files} files")
