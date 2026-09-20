#!/usr/bin/env python3
"""Convert legacy <h2 id="quick-answer"> HTML blocks to canonical '## Quick Answer {#quick-answer}' markdown heroes.

Rules (affiliate-site-execution skill, ENGAGEMENT-ROOT-CAUSE Lever 1):
- Preserve each file's own QA heading text (no wording changes).
- Keep the #quick-answer anchor (in-page TOCs link to it).
- Convert the single <p class="lead"> or <p> directly following the heading to markdown
  (strip tags, convert <a href> to [text](url), <strong> to **).
- Leave all other HTML (lists, blockquotes) untouched — markdown-aware conversion only
  where unambiguous. No content changes.
"""
import re, sys, pathlib

FILES = [
    "content/lower-your-bills.md",
    "content/utility-bills-costs-explained.md",
    "content/electricity-explained.md",
    "content/blog/aux-heat-vs-emergency-heat-meaning.md",
    "content/blog/ac-running-but-not-cooling.md",
    "content/blog/why-is-my-water-bill-higher-in-summer.md",
    "content/blog/is-your-toilet-running-leak-test.md",
    "content/blog/mcf-vs-ccf-vs-therms-on-gas-bill.md",
    "content/blog/how-do-smart-meters-work.md",
    "content/blog/average-utility-bills-by-state-2026.md",
    "content/blog/why-is-my-water-bill-higher-in-winter.md",
    "content/blog/why-did-my-utility-bill-go-up-this-month.md",
]

H2 = re.compile(r'<h2 id="quick-answer">([^<]+)</h2>')

def md_inline(s):
    s = re.sub(r'<a href="([^"]+)">([^<]*)</a>', r'[\2](\1)', s)
    s = re.sub(r'<a href=\'([^\']+)\'>([^<]*)</a>', r'[\2](\1)', s)
    s = s.replace("<strong>", "**").replace("</strong>", "**")
    s = s.replace("<em>", "*").replace("</em>", "*")
    s = re.sub(r"</?code>", "`", s)
    s = re.sub(r"<[^>]+>", "", s)
    return s

def convert(text):
    m = H2.search(text)
    if not m:
        return None
    heading_text = m.group(1).strip()
    out = []
    out.append(f"## {heading_text} {{#quick-answer}}")
    tail = text[m.end():]
    # next single-line <p ...>...</p>
    pm = re.match(r"\s*<p( [^>]*)?>(.*?)</p>", tail, re.S)
    converted_para = None
    if pm:
        converted_para = md_inline(pm.group(2).strip())
        out.append("")
        out.append(converted_para)
        tail = tail[pm.end():]
    return "\n".join(out), tail

for fp in FILES:
    p = pathlib.Path(fp)
    orig = p.read_text()
    res = convert(orig)
    if not res:
        print(f"SKIP (no legacy heading): {fp}")
        continue
    head, tail = res
    h2_match = H2.search(orig)
    idx = orig.find(h2_match.group(0))
    prefix = orig[:idx]
    heading_text = h2_match.group(1).strip()
    converted_para = "\n\n" in head and head.split("\n\n", 1)[1] if "\n\n" in head else None
    new = prefix + head + tail
    p.write_text(new)
    print(f"converted: {fp}  (QA text: {heading_text[:40]!r}, para converted: {bool(converted_para)})")
print("done")
