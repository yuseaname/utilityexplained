# SQ-068 Audit Rubric (binding — distilled from the client audit prompt, 2026-08-29)

Site: utilityexplained.com — Hugo static site, repo root = this directory.
110 content pages: ~88 blog posts (content/blog/), 5 author pages (content/author/),
~17 site pages (about, contact, methodology, editorial-policy, editorial-team, corrections,
affiliate-disclosure, disclaimer, terms, privacy-policy, search, utilities-glossary),
5 hub pages (electricity/gas/water/heating-cooling/utility-bills-costs-explained), homepage content/_index.md.
Rendered site: public/ (fresh 2026-08-29). Monetization: affiliate (see AFFILIATE-PLACEMENTS-2026-08-28.md).

## The seven audit dimensions
1. **Purpose & search intent** — informational / commercial / transactional / navigational / local per page. Flag intent mismatch (e.g., buying guide targeting an informational query, or a post whose title asks a question the body fails to answer). Does the page give a reason to read, trust, share, return, or buy?
2. **Thin & low-value content** — too short for its topic, no original info, vague claims, unanswered user questions; ALSO long pages padded with filler/repetition/generic conclusions. Duplicates, near-duplicates, templated/doorway-style, outdated, placeholder, no standalone purpose.
3. **AI-slop / generic writing** — mass-produced feel, repetitive sentence patterns, formulaic headings, vague filler, buzzwords, unsupported claims, keyword repetition, empty conclusions; missing firsthand experience, concrete examples, original data, named sources. QUOTE representative passages. Confidence: low/medium/high. NEVER label content AI solely because it is polished or stylistically neutral — report observable quality problems.
4. **Originality, expertise, trust (E-E-A-T)** — meaningfully better than competing pages? Trust signals: business identity, contact, author/reviewer details, qualifications, editorial standards, citations, dates, accurate claims, disclosures. Flag unsupported statistics, outdated recommendations, broken links, expired offers. EXTRA scrutiny for money/finance/safety (YMYL): rates, shut-off rules, assistance programs.
5. **Readability & UX** — intro quality, heading hierarchy, paragraph length, walls of text, buried answers (is the main answer visible fast?), scannability, tables/lists, CTAs, tone consistency.
6. **Visual/multimedia** — recommend visuals ONLY where they improve understanding, credibility, accessibility, or decisions (diagrams, charts, comparison tables, calculators, annotated examples). NO decorative stock. Flag missing/inaccurate alt text, weak captions.
7. **On-page SEO & structure** — titles, meta descriptions, URLs, H1s, subheadings, keyword targeting, schema, internal links, orphans, dead ends, weak anchors, cannibalization, indexation risk.

## Action vocabulary (use EXACTLY these labels)
`improve-and-retain` | `rewrite` | `expand` | `consolidate` | `redirect` | `remove-or-noindex` | `retain`

Never recommend adding words merely to increase length — additions must improve usefulness, originality, clarity, trust, or decision-making.

## Scoring
Per page audited in depth: **quality 1–10** and **search-readiness 1–10**. Judge by intent satisfaction, not word count.

## Ground rules
- Repo path contains a space — ALWAYS quote paths in shell commands.
- Prior audits in repo root (AGENCY-AUDIT-2026-08-27.md, CONTENT-AUDIT-2026-08-28.md, SEO-CONTENT-AUDIT-FACTCHECK-2026-08-29.md, VISUAL-CONTENT-AUDIT-2026-08-29.md, VISUAL-MAKEOVER-2026-08-29.md) are PRIOR CLAIMS — re-verify anything you rely on; never copy their conclusions as evidence.
- Evidence over confidence: every important judgment needs page-specific evidence (path, quote, or command output).
- Do not invoke scripts/squad.py or any provider endpoint (recursion guard). Web tools allowed where granted.
