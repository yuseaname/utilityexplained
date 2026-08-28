# UtilityExplained — Full-Site Content Audit (SQ-045)

**Date:** 2026-08-28 · **Method:** Commander deterministic metrics + 7-seat fleet (prospector full read, tracer journeys, cartographer clusters, verifier mechanical re-derivation, mason claim-level sourcing map, analyst/challenger benchmarks + prioritization) + Commander spot-checks
**Scope:** all 97 blog articles + sitewide quality systems
**Machine data:** `.squad/content-metrics.{md,json}` · `.squad/SQ-045/artifacts/` (per-page tables)

---

## 1. Executive Summary

The corpus splits into a **strong diagnostic core** and a **long thin tail**, with one acute problem that outranks everything: **a sitewide data-credibility crisis**. Two pages contradict each other on the national average utility bill ($262 vs $430–500/mo), a headline state figure fails arithmetic (Hawaii $0.34/kWh × 900 kWh = $306, page claims $450/mo), and the site's #1 revenue page carries **249 dollar figures with zero sources**. For a site whose brand promise is "exact savings," this is the highest-leverage repair available — and the gate on Google re-trust.

**Verdict distribution (prospector, all 97 pages):** 12 retain (12%) · **41 improve (42%)** · 20 consolidate (21%) · 6 replace (6%) · **18 remove (19%)** — page count shrinks ~30% before any new content.

**Systemic findings (all Commander-verified or multi-seat corroborated):**

| # | Finding | Scale | Severity |
|---|---|---|---|
| S1 | Contradictory national averages between pages | 2 pages | CRITICAL |
| S2 | Hawaii math error (and unverifiable state table) | 1 page, 484 figures | CRITICAL |
| S3 | Zero-source pages incl. flagship + top troubleshooters | 19 pages (20%) | HIGH |
| S4 | Intent-slug mismatches (title ≠ slug ≠ reader need) | 3 confirmed (05, 44, + others) | HIGH |
| S5 | Journey gaps: no "lower gas/water bill" bridge, no water-bill-reading page, fee hub too thin, no rate-plan hub | 12 gaps | HIGH |
| S6 | Stale-year data without current counterpoint | 8 pages | MEDIUM |
| S7 | Markdown/HTML heading inconsistency | ~6 pages | LOW (style only — verified NOT an SEO issue) |
| S8 | 90+ pages lack diagrams/tables where topic begs for one | sitewide | MEDIUM (benchmark gap) |

---

## 2. The Credibility Crisis (fix FIRST)

1. **Reconcile the national average.** `average-utility-bills-by-state-2026` says $430–500/mo; the site elsewhere says $262. One is wrong (likely both partially). Prescription: pull EIA RECS + Electric Power Monthly, define the basket (electricity+gas+water+sewer+trash?), state the definition ONCE in a data-methodology block, and make every page use it.
2. **Fix the state cost table math** (`2026-utility-cost-index-by-state`, currently draft — keep it draft): every row = rate × usage must reconcile; cite EIA Table 5.6.A per row or label as estimate with methodology.
3. **Source the flagship** (`how-to-lower-electric-bill-complete-guide`: 15.7% of pageviews, 0 sources, 249 dollar figures): the 3–6%/degree thermostat claim → DOE Energy Saver; the 40–50% HVAC share → EIA RECS; per-fix savings ranges → DOE/ENERGY STAR. **This is challenger's #1 first-40-hours item and I concur.**

## 3. Page-Classification Plan

**Remove/redirect candidates (18, worst 10):** the zero-traffic alias twins and duplicate-intent pages — `why-my-utility-bill-is-higher-with-same-usage` (896w duplicate of 15), `15-why-utility-bill-higher-same-usage` (334w, absorbed by 03), `41-how-to-read-electricity-bill` (duplicate of 01), `supply-vs-delivery-charges-electricity` + `gas-delivery-charge-vs-supply-charge` + `24-delivery-charge-vs-supply-charge` (triple-play → one canonical), `fixed-vs-variable-rate-electricity-plan` (canonical already exists), `46-what-time-is-electricity-cheapest` (fold into 08 ToU), plus the 6 already-aliased drafts (stay dead). Full list: prospector artifact.

**Consolidation designs (cartographer, ranked):**
1. **CLUSTER-FEES → new master "Every Fee on Your Utility Bill Explained"** absorbing ~10 fee pages (each keeps a definitional stub or 301-alias) — biggest index-quality win
2. **CLUSTER-READ-ELEC → 01-how-to-read-your-electric-bill** (best aligned, 7 sources) absorbing breakdown/workflow content
3. **CLUSTER-SAVE → flagship** absorbing phantom-power + smart-plugs as subsections (post-sourcing)
4. **CLUSTER-HIGH-ELEC → 03** absorbing sudden-spike's "no usage change" section
5. **CLUSTER-SERVICE → can-utility-shut-off-service** (2774w) absorbing deposit/connection/reconnection/past-due as lifecycle chapters
6. CLUSTER-HIGH-WATER → 06 (needs expansion first); CLUSTER-HVAC → new merged efficiency comparison

**Thin verdicts:** 56 pages <800 words — **16 thin-incomplete** (need depth: 13-ac-short-cycling at 400w, 04-hidden-fees at 327w, 16-budget-billing at 311w…) vs ~40 **thin-but-tight** (concise by design — leave alone; polishing them is the trap challenger warned about).

## 4. Journey Gaps → New-Page Needs (in priority order)

1. **"How to Lower Your Water Bill"** — real page, not the mislabeled 44 (fix 44's title/slug to match its investigate-intent)
2. **"How to Lower Your Gas Bill"** — 07 embeds fixes; extract a dedicated action page, cross-link
3. **"How to Read Your Water Bill"** — only exists as 1/3 of a 598w universal guide
4. **Rate-plan hub** ("Which rate plan is right for me") coordinating the 8 rate pages
5. **Fee hub expansion** — 04-hidden-fees becomes the launching pad (or the master fee page IS this)
6. HVAC: "furnace not turning on", "heat pump not heating" — later, with HVAC cluster merge

## 5. The Benchmark Bar (analyst + Commander, verified fetches 2026-08-27)

Authority pages that own these queries (EIA Electricity-use, ConEd bill-reading, EPA WaterSense, energy.gov Home Upgrades) share: **specific dollar/percent data with named sources, a calculator or checklist tool, dated updates, hub-and-spoke internal structure**. Our pages match on structure, trail on: sourced data, tools (zero interactive elements sitewide), and freshness signals. Complete-treatment checklists per topic live in the analyst envelope + this audit's research notes.

## 6. Remediation Queue (machine-readable update follows)

**P0 — credibility (this week):** S1 reconcile averages · S2 state-table math · S3a source the flagship · S3b source 07-gas + 30-spike (both monetized, both 0-source)
**P1 — intent repair (2 weeks):** fix 44/05 title-slug mismatches · build 3 bridge pages (lower water/gas, read water bill) · depth-pass the 16 thin-incomplete · expand fee hub
**P2 — consolidation (30 days):** execute cluster merges 1–5 · remove/alias the 18 · stale-year refresh (8 pages) · rate-plan hub
**P3 — differentiation:** first interactive tool (bill anatomy calculator or CCF calculator) per benchmark gap

**Measurement:** bounce on fixed pages (target <75% → <70%), Google referrer share (2.6% → 5%+ in 30d post-P0), indexation count, then CTR on newly-sourced money pages.

*Evidence tiers: S1/S2/S4 Commander-verified on disk; cluster designs multi-seat corroborated; per-page verdicts prospector+metrics reconciliation (word counts THIS time deterministic). Known corrections: prospector's "6 zero-heading pages invisible to SEO" refuted (HTML h2s render fine — consistency issue only).*
