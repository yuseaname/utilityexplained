#!/usr/bin/env python3
"""content_quality_metrics.py — deterministic per-page content metrics for utilityexplained.

Body-only word counts (frontmatter stripped), freshness, sources, links, headings,
FAQ/product-box presence, stale-year references, placeholder patterns.
Output: .squad/content-metrics-<date>.md (table) + .json (machine-readable).
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"
TODAY = date.today()

PLACEHOLDER_PATTERNS = [
    r"\bTBD\b", r"\bTODO\b", r"\bFIXME\b", r"lorem ipsum", r"coming soon",
    r"\[insert", r"\[add ", r"\?\?\?", r"\bplaceholder\b", r"XX%", r"\$XX",
    r"to be (added|determined|confirmed)", r"<p>\s*</p>",
]
STALE_YEARS = [2023, 2022, 2021]  # years that indicate aging data references
CURRENT_YEARS = [2026, 2025]


def parse_page(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    fm, body = (m.group(1), m.group(2)) if m else ("", text)

    def fm_get(key):
        mm = re.search(rf'^{key}:\s*"?([^"\n]*)"?', fm, re.MULTILINE)
        return mm.group(1).strip() if mm else ""

    words = len(re.findall(r"[A-Za-z0-9'’\-]+", re.sub(r"\{\{<[^>]*>\}\}", " ", body)))
    # Count markdown AND raw-HTML headings/links (HTML-marked pages are not heading-less)
    h2 = len(re.findall(r"^##\s", body, re.MULTILINE)) + len(re.findall(r"<h2[\s>]", body, re.IGNORECASE))
    h3 = len(re.findall(r"^###\s", body, re.MULTILINE)) + len(re.findall(r"<h3[\s>]", body, re.IGNORECASE))
    internal = (
        len(re.findall(r"\]\(/blog/", body))
        + len(re.findall(r'href="/blog/', body))
        + len(re.findall(r'href="/(?!blog/)[^"]*/"', body))  # hub/core-page links (non-blog)
        + len(re.findall(r'\{\{<\s*ref\s+"[^"]+"', body))    # Hugo ref shortcodes
    )
    src_urls = set(re.findall(r"https?://[^\s\)\]\"']+", fm + "\n" + body))
    sources = len(src_urls)
    faq = len(re.findall(r"\{\{<\s*faq", body))
    boxes = len(re.findall(r"\{\{<\s*product-box", body))
    quick_answer = 1 if re.search(r"^##\s*Quick Answer", body, re.MULTILINE) else 0
    tables = len(re.findall(r"^\|.*\|$", body, re.MULTILINE)) // 3  # rough: rows/3
    placeholders = sum(len(re.findall(p, body, re.IGNORECASE)) for p in PLACEHOLDER_PATTERNS)
    stale_years = sum(len(re.findall(rf"\b{y}\b", body)) for y in STALE_YEARS)
    current_years = sum(len(re.findall(rf"\b{y}\b", body)) for y in CURRENT_YEARS)

    updated = fm_get("updated") or fm_get("date")
    age_days = (TODAY - date.fromisoformat(updated)).days if updated else None
    return {
        "path": str(path.relative_to(REPO)),
        "title": fm_get("title"),
        "words": words,
        "updated": updated,
        "age_days": age_days,
        "h2": h2, "h3": h3, "tables": tables,
        "internal_links": internal,
        "sources": sources,
        "faq": faq,
        "product_boxes": boxes,
        "quick_answer": quick_answer,
        "placeholders": placeholders,
        "stale_year_refs": stale_years,
        "current_year_refs": current_years,
        "draft": 1 if re.search(r"^draft:\s*true", fm, re.MULTILINE) else 0,
    }


def main():
    pages = [parse_page(p) for p in sorted(CONTENT.rglob("*.md"))]
    blog = [p for p in pages if p["path"].startswith("content/blog/") and p["path"].endswith(".md")]
    out_json = REPO / ".squad" / "content-metrics.json"
    out_json.parent.mkdir(exist_ok=True)
    out_json.write_text(json.dumps(pages, indent=1))

    thin = [p for p in blog if p["words"] < 800]
    no_sources = [p for p in blog if p["sources"] == 0]
    stale = [p for p in blog if p["age_days"] and p["age_days"] > 30]
    placeholder_hits = [p for p in pages if p["placeholders"] > 0]
    stale_data = [p for p in blog if p["stale_year_refs"] > 0 and p["current_year_refs"] == 0]

    lines = [
        f"# Content Quality Metrics — {TODAY} (deterministic, body-only)",
        f"\nTotal md files: {len(pages)} | blog articles: {len(blog)}",
        f"\n## Signal summary\n",
        f"- Thin (<800 words body): **{len(thin)}**",
        f"- Zero outbound sources: **{len(no_sources)}**",
        f"- Not updated in 30+ days: **{len(stale)}**",
        f"- Placeholder-pattern hits: **{len(placeholder_hits)}**",
        f"- Stale-year refs w/o current-year counterpoint: **{len(stale_data)}**",
        "\n## Per-page table (blog)\n",
        "| path | words | updated | age | h2/h3 | tbl | ilinks | src | faq | qa | box | ph | staleY |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for p in sorted(blog, key=lambda x: x["words"]):
        lines.append(
            f"| {p['path'].replace('content/blog/', '')} | {p['words']} | {p['updated']} | {p['age_days']} | "
            f"{p['h2']}/{p['h3']} | {p['tables']} | {p['internal_links']} | {p['sources']} | {p['faq']} | "
            f"{p['quick_answer']} | {p['product_boxes']} | {p['placeholders']} | {p['stale_year_refs']} |")
    (REPO / ".squad" / "content-metrics.md").write_text("\n".join(lines))
    print(f"\n".join(lines[:12]))
    print(f"...full table -> .squad/content-metrics.md | json -> {out_json}")


if __name__ == "__main__":
    main()
