#!/usr/bin/env python3
"""SQ-056 wave-2 validation: master-table coverage vs disk inventory."""
import os
import re

ROOT = "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained"
txt = open(os.path.join(ROOT, "FULL-CONTENT-SEO-AUDIT-2026-08-30.md")).read()
sec = txt.split("## 3. Page-by-Page")[1].split("## 4.")[0]
rows = [l for l in sec.splitlines() if l.startswith("| /") or l.startswith("| /")]
print("page rows:", len(rows))

slugs = set()
for l in rows:
    path = l.split("|")[1].strip().strip("`")
    slugs.add(path)

disk = set()
for root, _, files in os.walk(os.path.join(ROOT, "content")):
    for f in files:
        if f.endswith(".md"):
            rel = os.path.relpath(os.path.join(root, f), os.path.join(ROOT, "content"))[:-3]
            disk.add(rel)

# normalize: table uses URL paths (/blog/slug/, /slug/)
norm = set()
for s in slugs:
    s = s.strip("/").removeprefix("blog/") if s.startswith("/blog/") else s.strip("/")
    norm.add(s)

disk_norm = {d.replace("/_index", "").replace("_index", "INDEX") for d in disk}
disk_norm = {d[:-1] if d.endswith("/_index") else d for d in disk_norm}

missing = {d for d in disk_norm if d != "INDEX" and d not in norm and d.replace("_index", "") not in norm}
print("unique table paths:", len(norm), "| disk md (excl indexes):", len([d for d in disk_norm if d != "INDEX"]))
if missing:
    print("MISSING FROM REPORT:", sorted(missing))
else:
    print("coverage: COMPLETE (all disk pages present)")
