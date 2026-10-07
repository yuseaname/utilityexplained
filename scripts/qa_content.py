#!/usr/bin/env python3
"""qa_content.py — build-time content QA gate for UtilityExplained.com.

Scans content/ markdown (+frontmatter) and optionally a built tree, failing
the build on violation classes found in the 2026-10-06 deep audit.

Rules:
  R1 dup-href-diff-anchor   ERROR  same href 2+ times in one file with
                                   substantially different anchor texts
                                   (token overlap < 0.5, overlap coefficient
                                   over min token set)
  R2 category-bleed         ERROR  water/gas-category page title/description
                                   using electricity-only vocabulary (kWh,
                                   electricity rate...) and vice versa
  R3 control-chars          ERROR  bytes in [\\x00-\\x08\\x0b\\x0c\\x0e-\\x1f]
  R4 missing-author         ERROR  content/blog/*.md with no author: frontmatter
  R5 missing-sources        ERROR  data-heavy article (EIA|EPA|DOE|ENERGY STAR
                                   in body) missing BOTH updated: AND a
                                   non-empty sources: frontmatter
  R6 duplicate-slug         ERROR  two content files mapping to one URL
  R7 broken-internal-url    ERROR  href="/..." not present under --built dir
                                   (requires --built)
  R8 hardcoded-guide-count  WARN   "\\d{2,3} guides" in _index/hub prose
                                   (ERROR with --strict)
  R9 hardcoded-stats        WARN   STATS literals outside data/stats.yaml
                                   (ERROR with --strict)

Usage:
  qa_content.py [--baseline OUT.json] [--baseline-in IN.json]
                [--built DIR] [--strict] [--report]

Exit codes: 0 ok (warnings allowed unless --strict), 1 violations beyond
baseline, 2 usage error.
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(REPO, "content")

# Literals that must come from data/stats.yaml once R9 is flipped to ERROR.
# Legitimate historical literals are exempt:
#   - Sources/citation lines (numbered "N. [label](url) — ... retrieved ..." rows):
#     a dated retrieval record must keep quoting the value it verified.
#   - image alt= text (describes a baked image; changing it desyncs from the pixels)
#   - worked-example arithmetic ($0.1834 multipliers inside derivations)
STATS = ["18.34", "18.31", "899 kWh", "899 kWh/month"]
CITATION_LINE = re.compile(r"^\s*\d+\.\s*\[.*\]\([^)]*\)\s*[-—]", re.M)
ALT_LINE = re.compile(r"alt=\"[^\"]*\"")
ARITH_LIT = re.compile(r"[×x]\s*\$?0\.18\d|=\s*\$?0\.18\d|\$\s?0\.1834")

def _strip_exempts(body: str) -> str:
    out = []
    for ln in body.split("\n"):
        if CITATION_LINE.search(ln) or ALT_LINE.search(ln):
            continue  # skip whole line (alt/citation lines carry no shortcode-able prose)
        if ARITH_LIT.search(ln):
            ln = ARITH_LIT.sub("", ln)
        out.append(ln)
    return "\n".join(out)

# category -> vocabulary that does NOT belong on that category's pages
ELEC_VOCAB = re.compile(r"\bkWh\b|¢/kWh|cents?/kWh|electric(?:ity)? rate", re.I)
WATER_GAS_VOCAB = re.compile(r"\bCCF\b|\btherms?\b|\bMCF\b|water rate|gas rate", re.I)

# legitimate cross-utility sentences (substring match, case-insensitive)
WHITELIST = [
    "compare water costs to electricity",
    "compare water costs to other utilities",
    "electricity and natural gas",
    "electricity, gas, and water",
    "electricity, gas, or water",
    "electric, gas, and water",
    "other utilities",
    "cross-utility",
]

HUB_FILES = {
    "electricity-explained.md": "Electricity",
    "gas-explained.md": "Gas",
    "water-explained.md": "Water",
    "heating-cooling-explained.md": "HVAC",
    "utility-bills-costs-explained.md": "Bills",
}

FRONT = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
HREF = re.compile(r'href="(/[^"#]*)[#"]')
ANCHOR = re.compile(r'<a\s[^>]*href="([^"#]+)"[^>]*>(.*?)</a>', re.S)
CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
COUNT_RE = re.compile(r"\b\d{2,3}\s+guides?\b")
DATA_HEAVY = re.compile(r"\bEIA\b|\bEPA\b|\bDOE\b|ENERGY STAR")
TAG = re.compile(r"<[^>]+>")
STOP = set("the a an of to for and or in on your you our my is are it its with at from by vs v s".split())


def parse_frontmatter(text):
    m = FRONT.match(text)
    fm = {}
    if not m:
        return fm, text
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "-", "\t")):
            k, _, v = line.partition(":")
            fm.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    return fm, text[m.end():]


def tokens(s):
    s = TAG.sub(" ", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    out = set()
    for t in s.split():
        if t in STOP:
            continue
        if len(t) > 3 and t.endswith("es"):
            t = t[:-2]
        elif len(t) > 2 and t.endswith("s"):
            t = t[:-1]
        out.add(t)
    return out


def overlap(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / min(len(a), len(b))


def category_of(path, fm):
    rel = os.path.relpath(path, CONTENT).replace(os.sep, "/")
    name = os.path.basename(path)
    if name in HUB_FILES:
        return HUB_FILES[name]
    cats = fm.get("categories", "") or fm.get("category", "")
    cats = cats.strip("[]").replace('"', "")
    parts = [c.strip() for c in cats.split(",") if c.strip()]
    if parts:
        return parts[0]
    if rel.startswith("blog/"):
        # fall back: sniff title vocabulary
        t = (fm.get("title", "") + " " + fm.get("description", "")).lower()
        if "water" in t or "sewer" in t:
            return "Water"
        if "gas" in t and "gallon" not in t:
            return "Gas"
    return None


def walk():
    for root, _dirs, files in os.walk(CONTENT):
        if ".agency" in root or "__pycache__" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(root, f)


def scan(built_dir=None):
    v = []
    slug_map = defaultdict(list)

    for path in walk():
        rel = os.path.relpath(path, CONTENT).replace(os.sep, "/")
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError as e:
            v.append((rel, 0, "R3", f"unreadable: {e}"))
            continue
        fm, body = parse_frontmatter(text)

        # R3 control chars
        for m in CONTROL.finditer(text):
            v.append((rel, text[: m.start()].count("\n") + 1, "R3",
                      f"control byte {repr(m.group())}"))
            break  # one report per file is enough to fail

        # R1 dup href with different anchors (directory rows only: anchors
        # inside <li> blocks; inline prose anchors legitimately vary)
        per_href = defaultdict(set)
        for li in re.findall(r"<li\b[^>]*>(.*?)</li>", body, re.S):
            for m in ANCHOR.finditer(li):
                href, label = m.group(1), m.group(2).strip()
                if href.startswith(("http", "mailto:", "#")):
                    continue
                per_href[href].add(" ".join(label.split()))
        for href, labels in per_href.items():
            if len(labels) < 2:
                continue
            labs = sorted(labels)
            for i in range(len(labs)):
                for j in range(i + 1, len(labs)):
                    if overlap(tokens(labs[i]), tokens(labs[j])) < 0.5:
                        v.append((rel, 0, "R1",
                                  f'dup href {href}: "{labs[i]}" vs "{labs[j]}"'))

        # R2 category bleed (title/description only)
        cat = category_of(path, fm)
        tdesc = (fm.get("title", "") or "") + " " + (fm.get("description", "") or "")
        if tdesc.strip() and not any(w.lower() in tdesc.lower() for w in WHITELIST):
            if cat == "Water" or cat == "Gas":
                if ELEC_VOCAB.search(tdesc):
                    v.append((rel, 0, "R2",
                              f'{cat} page title/description uses electricity vocabulary: {tdesc[:90]}'))
            elif cat == "Electricity":
                if WATER_GAS_VOCAB.search(tdesc) and "gas" not in fm.get("title", "").lower():
                    v.append((rel, 0, "R2",
                              f'Electricity page title/description uses water/gas vocabulary: {tdesc[:90]}'))

        # R4 missing author (articles only, not section indexes)
        if rel.startswith("blog/") and os.path.basename(path) != "_index.md" \
                and not fm.get("author"):
            v.append((rel, 0, "R4", "blog article missing author: frontmatter"))

        # R5 missing sources on data-heavy (sources: may be a YAML list, so
        # look for the key anywhere in the frontmatter block)
        if rel.startswith("blog/") and os.path.basename(path) != "_index.md" \
                and DATA_HEAVY.search(body):
            fm_match = FRONT.match(text)
            fm_block = fm_match.group(1) if fm_match else ""
            has_updated = bool(fm.get("updated"))
            has_sources = re.search(r"^sources:", fm_block, re.M) is not None \
                or "## Sources" in body
            if not has_updated and not has_sources:
                v.append((rel, 0, "R5",
                          "data-heavy article (EIA/EPA/DOE/ENERGY STAR) missing BOTH updated: and sources"))

        # R6 duplicate slug
        slug = fm.get("slug") or fm.get("url") or os.path.splitext(rel)[0]
        slug_map[slug].append(rel)

        # R8 hardcoded guide counts (hub/_index prose only)
        if os.path.basename(path) == "_index.md" or os.path.basename(path) in HUB_FILES:
            for m in COUNT_RE.finditer(body):
                v.append((rel, body[: m.start()].count("\n") + 1, "R8",
                          f'hardcoded guide count: "{m.group()}"'))

        # R9 hardcoded stats (citation/alt/arithmetic lines exempt — see _strip_exempts)
        body_x = _strip_exempts(body)
        for lit in STATS:
            for m in re.finditer(re.escape(lit), body_x):
                v.append((rel, body[: m.start()].count("\n") + 1, "R9",
                          f'hardcoded stat literal: "{lit}" (use data/stats.yaml)'))

    for slug, rels in slug_map.items():
        if len(rels) > 1:
            v.append((rels[0], 0, "R6", f"duplicate slug {slug}: {rels}"))

    # R7 broken internal URLs against built tree
    if built_dir:
        existing = set()
        for root, _d, files in os.walk(built_dir):
            for f in files:
                if f == "index.html":
                    p = os.path.relpath(os.path.join(root, f), built_dir)
                    p = "/" + p[: -len("/index.html")]
                    if p != "/index":
                        existing.add(p + "/")
        seen = set()
        for path in walk():
            rel = os.path.relpath(path, CONTENT).replace(os.sep, "/")
            _fm, body = parse_frontmatter(open(path, encoding="utf-8", errors="replace").read())
            for m in HREF.finditer(body):
                href = m.group(1)
                if href in seen or not href.startswith("/"):
                    continue
                seen.add(href)
                if href not in existing:
                    v.append((rel, 0, "R7", f"internal URL not in built tree: {href}"))
    return v


ERRORS = {"R1", "R2", "R3", "R4", "R5", "R6", "R7"}
NAMES = {
    "R1": "dup-href-diff-anchor", "R2": "category-bleed", "R3": "control-chars",
    "R4": "missing-author", "R5": "missing-sources", "R6": "duplicate-slug",
    "R7": "broken-internal-url", "R8": "hardcoded-guide-count",
    "R9": "hardcoded-stats",
}


def key(item):
    return f"{item[2]}|{item[0]}|{item[3]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", help="emit current violations as JSON")
    ap.add_argument("--baseline-in", help="suppress violations listed in this JSON")
    ap.add_argument("--built", help="built tree dir for R7")
    ap.add_argument("--strict", action="store_true", help="warnings are errors")
    ap.add_argument("--report", action="store_true", help="human list")
    args = ap.parse_args()

    violations = scan(args.built)

    if args.baseline:
        payload = {"violations": [
            {"file": f, "line": l, "rule": r, "detail": d} for f, l, r, d in violations]}
        with open(args.baseline, "w") as fh:
            json.dump(payload, fh, indent=1)
        counts = defaultdict(int)
        for _f, _l, r, _d in violations:
            counts[r] += 1
        print(json.dumps({k: counts[k] for k in sorted(counts)}, indent=1))
        print(f"baseline written: {len(violations)} violations -> {args.baseline}")
        return 0

    allowed = set()
    if args.baseline_in:
        with open(args.baseline_in) as fh:
            allowed = {v["rule"] + "|" + v["file"] + "|" + v["detail"]
                       for v in json.load(fh).get("violations", [])}

    fails = []
    for f, l, r, d in violations:
        if key((f, l, r, d)) in allowed:
            continue
        sev = "ERROR" if (r in ERRORS or args.strict) else "WARN"
        line = f"[{sev}] {NAMES[r]:22s} {f}:{l}  {d}"
        print(line)
        if r in ERRORS or args.strict:
            fails.append(line)

    if fails:
        print(f"\nFAIL: {len(fails)} blocking violation(s)", file=sys.stderr)
        return 1
    print("\nOK: no blocking violations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
