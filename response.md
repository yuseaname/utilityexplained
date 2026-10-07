# Hub Rewrite — Water Hub (`content/water-explained.md`)

Seat: ds-or-1 · Assignment: hub-water · File edited: `content/water-explained.md` (single file only)

## Summary

Rewrote the Water hub from a teaching pillar into a decision/navigation page. Added a Quick Answer + a 6-row intent router, cut the textbook prose sections to one-sentence handoffs linking the owning article, removed the dead-weight "Related guides" list and "Final thoughts", and condensed the misconceptions and leak sections. The bill-anatomy figure, FAQ, and the `## Browse Our Water Bill Guides` directory were kept. No affiliate surfaces existed in this file before or after (zero delta).

## Line counts

| | Lines |
|---|---|
| Before | 288 |
| After | 163 |
| Reduction | **43.4%** (≥40% required) |

## Sections CUT (replaced with one-sentence handoff)

- **How water service works** → links `/blog/06-water-bill-too-high/` + `/utilities-glossary/` (verdict table noted the ideal target `/blog/what-is-ccf-on-a-water-bill/` is not in the allowed slug list, so used the fallback targets)
- **How water is measured: gallons, cubic feet, and CCF** → links `/utilities-glossary/#ccf-water`
- **Understanding your water bill** → links `/blog/06-water-bill-too-high/` (bill-anatomy figure KEPT)
- **Tiered water pricing and conservation rates** → links `/blog/tiered-water-rates-explained/`
- **What uses the most water in a typical home?** → links `/blog/average-water-usage-per-person/`
- **Seasonal changes and why water bills vary** → links `/blog/why-is-my-water-bill-higher-in-summer/` + `/blog/why-is-my-water-bill-higher-in-winter/`
- **How to read your water meter** → links `/utilities-glossary/#meter-reading`
- **How to reduce water usage without major changes** → links `/blog/44-how-to-lower-water-bill/`
- **Related guides to deepen your understanding** (plain-text list, no links) → replaced with one sentence pointing at the `#water-guides` directory anchor
- **Final thoughts** → removed entirely

## Sections KEPT (condensed)

- **Quick Answer** — ADDED (3 sentences: service charge + per-CCF usage + sewer; CCF→gallons conversion)
- **How to detect leaks and reduce waste** — KEPT condensed (leak detection is a money topic); toilet test + meter test folded into one paragraph, common-leak-source list retained
- **Common misconceptions about water service** — KEPT, condensed to 2–3 lines each (3 misconceptions)
- **Estimated readings and bill corrections** — KEPT, condensed, links `/blog/14-estimated-utility-bill-explained/`
- **Frequently asked questions** — KEPT (5 Q&A)
- **`## Browse Our Water Bill Guides` directory** — KEPT untouched (all real links)
- **bill-anatomy figure** — KEPT untouched

## Router rows added (6, under Quick Answer)

1. My water bill is too high → `/blog/06-water-bill-too-high/`
2. I want to understand tiered water rates → `/blog/tiered-water-rates-explained/`
3. How much water does a person use? → `/blog/average-water-usage-per-person/`
4. My bill is higher in summer or winter → `/blog/why-is-my-water-bill-higher-in-summer/` · `/blog/why-is-my-water-bill-higher-in-winter/`
5. I want to lower my water bill → `/blog/44-how-to-lower-water-bill/`
6. My bill was estimated → `/blog/14-estimated-utility-bill-explained/`

All router slugs are from the allowed list. No invented slugs.

## Verification outputs

**1. Hugo build (temp destination)**
```
$ hugo --destination "$TMPDIR/ue-hub-water" --quiet
HUGO_EXIT=0
```

**2. Every href resolves in built tree** — all hrefs in the built hub page checked against the built tree; every one resolves (0 MISS). Includes the two new glossary anchors `#ccf-water` and `#meter-reading`, both confirmed present in the built `/utilities-glossary/index.html`.

**3. Affiliate surfaces unchanged (zero delta)**
| Marker | Before | After |
|---|---|---|
| `amazon.com` | 0 | 0 |
| `tag=utexplained-20` | 0 | 0 |
| `product-box` | 0 | 0 |
| `data-rybbit` | 3 | 3 |
| `rel=` | 12 | 12 |

Hub had zero affiliate surfaces before; stays zero. No `{{< product-box >}}`, Amazon link, disclosure, or `data-rybbit` attribute was touched.

**4. Line count** — 288 → 163 = 43.4% reduction.

**5. QA gate**
```
$ python3 scripts/qa_content.py --report --built "$TMPDIR/ue-hub-water"
OK: no blocking violations
QA_EXIT=0
```
No R1–R7 blocking violations for `water-explained.md` (R7 broken-internal-url checked against the built tree).

**6. Router** — 6 intent rows present, all allowed slugs.

**7. Safety content** — the water hub contains no gas/CO safety section (that lives on the gas hub); nothing safety-related was cut here. No safety content existed to preserve.

**8. No fabricated sources/stats/dates** — no new citations, retrieval dates, or numbers introduced. The only figures retained are the pre-existing illustrative bill-anatomy example (in the untouched figure) and the pre-existing FAQ ranges (40–80 gal/day, 10–20 gal/day drip), which carried no fabricated sources. No `{{< stat >}}` shortcodes or "Data through" freshness lines existed in this file before or after.

## Unresolved blockers

None. All acceptance criteria pass.
