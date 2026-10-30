#!/usr/bin/env python3
"""gen_llms_txt.py — generate static/llms.txt from content front matter.

Why: llms.txt is the AI-engine entry point (ChatGPT/Claude/Grok/Perplexity
fetchers). The old file was a flat, description-less link list of blog
articles only. This generator emits the llmstxt.org shape:
  - H1 + blockquote site summary
  - curated "Key pages" (hubs, glossary, calculator, data page, trust pages)
    with one-line descriptions an LLM can use to decide what to fetch
  - all blog articles grouped by category, each with its front-matter
    description (trimmed to one sentence)
  - About footer block

Run from repo root:  python3 scripts/gen_llms_txt.py
Idempotent; diff static/llms.txt after running.
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOG = ROOT / "content" / "blog"
OUT = ROOT / "static" / "llms.txt"
BASE = "https://utilityexplained.com"

HEADER = """# Utility Explained

> Utility bills decoded: electric, gas, water, and sewer charges explained with worked math, decision frameworks, and verified sources (EIA, EPA, DOE, published tariffs).

Base URL: https://utilityexplained.com

This site publishes original, source-cited guides. Every article carries a Quick Answer, worked cost math, and dated primary-source citations.

"""

# Curated non-article surfaces, ordered by citation value.
KEY_PAGES = [
    ("/blog/average-utility-bills-by-state-2026/",
     "Average electric, gas, and water bills by state (2026) — EIA-sourced national and state-level data with stated vintage."),
    ("/electricity-explained/",
     "Electricity hub: kWh, supply vs delivery charges, demand fees, time-of-use rates — every line on an electric bill."),
    ("/gas-explained/",
     "Natural gas hub: therms, CCF, customer charges, winter rate spikes — every line on a gas bill."),
    ("/water-explained/",
     "Water hub: CCF, sewer charges, stormwater fees, meter reading — every line on a water bill."),
    ("/heating-cooling-explained/",
     "Heating & cooling hub: HVAC costs, thermostat settings, furnace and heat-pump troubleshooting with bill math."),
    ("/utility-bills-costs-explained/",
     "Bill basics: the four parts of any utility bill (usage, delivery, fixed charges, taxes/riders) explained."),
    ("/lower-your-bills/",
     "Savings hub: every way to lower electric, gas, and water bills, organized by cost and effort."),
    ("/utilities-glossary/",
     "Glossary: every utility term defined — CCF, therm, kW vs kWh, riders, franchise fees, LIHEAP and more."),
    ("/calculators/electricity-cost/",
     "Electricity cost calculator: appliance wattage × hours × your rate, with worked examples."),
    ("/methodology/",
     "How this site sources and verifies numbers (EIA/DOE/EPA primary sources, worked math, corrections log)."),
    ("/about/",
     "Who publishes this site, how it is produced, and how it is funded."),
    ("/editorial-policy/",
     "Editorial standards: sourcing rules, review process, and disclosure practices."),
    ("/corrections/",
     "Public corrections log — every material error found and fixed, with dates."),
]

FOOTER = """
## About

Utility Explained articles are produced by an independent editorial desk and cite primary sources (government data, manufacturer specifications, and published tariffs). Data-heavy pages carry dated source links; corrections are public. See https://utilityexplained.com/about/ for editorial information.
"""


def parse_front_matter(text: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_]+)\s*:\s*(.*)$", line)
        if mm:
            val = mm.group(2).strip().strip('"').strip("'")
            fm[mm.group(1)] = val
        # categories list line: categories: ["X", "Y"]
        mc = re.match(r'^categories\s*:\s*\["?([^\]]*)"?\]?\s*$', line)
        if mc:
            first = re.findall(r'"([^"]+)"', line)
            if first:
                fm["category_first"] = first[0]
    return fm


def first_sentence(s: str, cap: int = 140) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    m = re.match(r"^(.{20,}?[.!?])(\s|$)", s)
    out = m.group(1) if m else s
    if len(out) > cap:
        out = out[:cap].rsplit(" ", 1)[0] + "…"
    return out


def main() -> int:
    lines = [HEADER, "## Key pages\n\n"]
    for path, desc in KEY_PAGES:
        name = path.rstrip("/").split("/")[-1]
        lines.append(f"- [{name}]({BASE}{path}) {desc}\n")
    lines.append("\n")

    articles = []
    for f in sorted(BLOG.glob("*.md")):
        if f.name == "_index.md":
            continue
        fm = parse_front_matter(f.read_text(encoding="utf-8", errors="replace"))
        slug = fm.get("slug", f.stem)
        title = fm.get("title", slug)
        desc = first_sentence(fm.get("description", title))
        cat = fm.get("category_first") or fm.get("category", "Guides")
        date = fm.get("date", "")
        articles.append((cat, date, slug, title, desc))

    # group by category, newest first inside each group
    cats = {}
    for a in articles:
        cats.setdefault(a[0], []).append(a)

    for cat in sorted(cats):
        lines.append(f"## {cat}\n\n")
        for _, _, slug, _, desc in sorted(cats[cat], key=lambda a: a[1], reverse=True):
            lines.append(f"- [{slug}]({BASE}/blog/{slug}/) {desc}\n")
        lines.append("\n")

    lines.append(FOOTER)
    OUT.write_text("".join(lines), encoding="utf-8")
    n = len(articles) + len(KEY_PAGES)
    print(f"wrote {OUT} — {len(articles)} articles + {len(KEY_PAGES)} key pages = {n} entries, {len(cats)} categories: {', '.join(sorted(cats))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
