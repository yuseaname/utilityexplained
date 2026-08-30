# 18-fuel-adjustment-charge-on-utility-bill-explained — Visual Audit & Image Plan

## Hero
- File: `static/images/articles/18-fuel-adjustment-charge-on-utility-bill-explained/18-fuel-adjustment-charge-on-utility-bill-explained_hero_v2.webp` | Viewed: A painted domestic scene — a surprised woman at a kitchen counter studying a statement that features a teal-highlighted block with a lightning-bolt roundel; round thermostat reading 72 on the wall, steaming mug, phone, plants, warm morning light.
- Verdict: **SUITABLE-WITH-NOTES (demote candidate)** — on-topic (reader reviewing a bill line, per the audit's own description) and competently executed, but it frontally violates the style bible's human-figure rule: a large, expressive, decorative person smiling-adjacent at a bill is exactly what the bible bans, and the palette runs warm-yellow rather than ink/cream/teal/amber. This is the weakest hero of the four against the bible. Recommendation: demote to replace-first in the generation batch — a heroless interim is not required since the current asset is relevant and harmless, but any SQ-056 image batch should regenerate this one before touching anything cosmetic elsewhere. Its replacement is the distinct hero brief in row 1: a symbolic two-part calculation, no faces.

## Current state
- Visual count now (hero + in-body): **1** (hero only; zero in-body visuals in the .md after the SQ-055 refresh)
- In-body visuals: none.
- Unreferenced file in the article's asset folder, viewed this run, **do not wire as-is**: `custom_inline.webp` — photoreal desk stock photo of a statement with garbled line-name text (Electrokets Usage and similar letter-scramble) and fabricated dollar figures ($39.20 total and rows of invented numbers); same off-bible class as the other three pages' orphans. The page's own hard rule — never invent a national price range, use the account's tariff — makes fabricated-amount imagery doubly wrong here.

## Recommended plan
- Recommended total (3-7): **3** — ~750 words with two verify-tables, one symbolic example, and 3 FAQs; anchor 3 (smallest page of the set; figures must earn their room).

| # | Placement/section (exact heading) | Concept (style-bible-aligned) | Purpose | Format/orientation | Type | Affiliate-wired | Proposed filename |
|---|---|---|---|---|---|---|---|
| 1 | Header hero (frontmatter `image:`, keep `hero_below_answer: true`) | **REPLACE hero:** flat symbolic two-part calculation, no faces: tariff fuel rate (with effective-date calendar chip) × the bill's usage basis (meter chip) = the fuel-adjustment line. Cream ledger surface, grid-teal scaffolding, mono labels; amber on the resulting line only; no dollar amounts. | topic-set + clarify | 3:2 webp | illustrative | N | `18-fuel-adjustment-charge-on-utility-bill-explained_hero_v3.webp` |
| 2 | **Identify the Exact Charge** — directly after the symbolic-check paragraph | Generic tariff-excerpt card: a neutral tariff header, the account's charge-label field, unit/rate-basis field, and effective-date field, with an arrow to the matching bill-line placeholder. The fields are labels and blank rules only — no real utility name, rate, or dollar amount. | demonstrate-concept (shows where the line comes from without inventing a tariff) | 16:9 (wide=) | screenshot-style | N | `fuel-line-tariff-excerpt.webp` |
| 3 | In **Compare Bills Before Drawing a Conclusion** | Two-bill comparison spread: current vs prior statement as two flat ledger cards with six shared rows (billing days, metered usage, estimated status, rate-plan version, line-item rates, credits/one-time items); teal row-pairing rules connecting the columns, amber on the one row that differs, mono row labels; generic, no utility names, no amounts | break-up-dense (a six-bullet list becomes a scan) | 3:2 | screenshot-style | N | two-bill-compare-spread.webp |

- Completion note (2026-08-29): row 1's replacement hero and rows 2–3's in-body figures are generated and wired. No pre-existing visual was retained for this page.
- Screenshot-style guardrail: this page publishably contains zero verified dollar figures by design, so the comparison spread must use structure-only mock bills (row labels, no amounts) — the strictest reading of the amounts-must-match-on-page rule.
- No product images: this page carries no product box or amazon link.
- Orphan note: `custom_inline.webp` stays unwired (fabricated amounts contradict the page's own no-invented-numbers doctrine).

## Cohesion note
Page 18 is the worked micro-case of the family: 19 gives the rider mechanism, 25 the government lines, and 18 shows the discipline applied to one line. Its two in-body figures therefore reuse the family grammar at the smallest scale — a tariff-to-bill excerpt whose fields can be matched without invented amounts, and a comparison spread whose amber marks the one changed row — with mono labels and teal scaffolding throughout. Its planned hero regen (row 1) makes the page the family's only all-diagram cover: the same two-part calculation appears at a subject-setting scale, while the inline tariff card resolves the next question, "where do I find it?" This keeps the page's editorial stance—no national numbers, only the account's tariff—visible in the visual system itself.
