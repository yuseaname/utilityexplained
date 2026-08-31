# SQ-065 Evidence Brief — Wave 1 (source of truth for wave 2)

Compiled by the Commander 2026-08-30 from wave-1 result envelopes + artifacts.
Per-page entry tables live in .squad/SQ-065/wave1/*.md — READ THEM for the page-by-page section; this brief carries the cross-cutting findings only.

## Site facts (verified)

- utilityexplained.com — Hugo static site, 114 markdown pages (89 blog + 25 core), deployed via GitHub Actions (hugo --minify --gc) + rsync
- Production sitemap VERIFIED HEALTHY: 121 URLs (89 posts + 6 author + 7 category + 18 core + home); the "1 URL" reading was a grep line-count artifact on single-line XML (lieutenant#2 confirmed by fetching live sitemap)
- Analytics (Rybbit 2026-08-29): 867 sessions/7d, 1.14 pv/session, 91% bounce, ~65s sessions, Bing-heavy, Google ~0
- Monetization: Amazon Associates; product boxes via shortcodes; rel=sponsored nofollow on all audited money links (lieutenant, grep-verified)

## Seat verdicts (status + headline)

| Seat | Status | Artifact |
|---|---|---|
| lieutenant (12 money+flagship) | complete, 0 warnings | wave1/lieutenant-pages.md (38.5K, 12 entries) |
| prospector (22 fees cluster) | complete | wave1/prospector-pages.md (30.5K, 22 entries + 13-pair overlap map) |
| tracer (14 journey pages) | complete, 0 warnings, 343K ctx | wave1/tracer-journey.md (27.6K, 14 entries + pathway map) |
| twin_q (12-page judgment sample) | complete | wave1/twinq-verdict.md (11.2K) |
| lieutenant#2 rescue (25 core + cluster map) | complete, 0 warnings | wave1/cartographer-core.md (37.3K, 25 core entries + C0–C6 cluster map) |
| cartographer (original, 2h marathon, token-limit truncation warning) | complete — core compact entries (Part A) + FULL water/rates 22 entries (Part B1–B22) + cluster map (Part C) | wave1/cartographer-map.md (25.7K) |
| verifier (claims/freshness/rendered) | PARTIAL — generation collapse at 289 steps (3.1h); SALVAGED: live sitemap ✓ (121 URLs), metrics rerun byte-identical ✓, line-level staleY sweep (workspace); web claim re-derivation LOST → twin_q reduced rescue in flight | — |
| prospector#2 rescue (19 HVAC) | artifact landed (20.7K, 19 entries); envelope in flight | wave1/mason-pages.md |
| prospector#3 rescue (22 water/rates) | DEAD — protocol failure; REDUNDANT (cartographer Part B covers the slice fully) | — |
| mason (original HVAC) | DEAD — protocol failure, zero output; slice rescued on prospector#2 | — |

## Coverage census (114 pages)

- 12 money+flagship: lieutenant ✓ | 22 fees: prospector ✓ | 14 journey: tracer ✓
- 19 HVAC: prospector#2 (in flight) | 22 water/rates: cartographer Part B ✓ | 25 core: lieutenant#2 ✓ + cartographer Part A (double-covered)

## Cross-cutting findings (ranked by severity)

### Credibility / correctness
1. REVENUE-CORE PAGE BROKEN FRONTMATTER: duplicate `sources:` key (lines 8 + 19) in how-to-lower-electric-bill-complete-guide.md — silently drops one block (lieutenant, grep-verified)
2. STACKED-SAVINGS ARITHMETIC on same page: section banners sum to $200–$450/month savings vs the page's own $164.88 national-average bill — impossible promise (lieutenant)
3. 07-gas-bill-too-high internal contradictions: title "10 Causes" vs 11 in body; heating share 40-50% vs 60-70% both cited to one source; furnace payback 5-8y vs 3-8y vs ~23y worked example; two mislabeled sources (lieutenant)
4. CROSS-PAGE CLAIM DRIFT: water-heater blanket savings ~25% (05) vs 5-10% (07) vs 4-7% (guide); EPA leak-waste 9,400 gal (06) vs 10,000+/9,300 (point-sensor); 03's anchor misdescribes 42's thesis (lieutenant)
5. 28-utility-reconnection-fee: fee table claims "verified via state PUC dockets 2024–2026" with no checkable URL; moratorium claims conflict with 21's verified MN rules (prospector)

### AI-slop / writing patterns (twin_q)
- Pattern A "Phantom Philosophy" intros (External/Internal/Philosophical tripartite) — old cohort fingerprint (aux-heat, afue); CRITICAL severity; new cohort largely clean
- Pattern B "Echo-Bloop" template: Quick Answer bullets → prose rephrasing same bullets → FAQ repeat = answer 3×; sitewide; hurts scannability + triggers repetitive-content classification
- Pattern C link-stuffing: 4 internal links in single sentences (afue)
- Batch-generation fingerprint: many articles share date: 2025-12-25; bulk updated: 2026-08-21 stamps — "zombie content revived" risk
- Factual hallucination rated LOW (twin_q) — facts are solid; structure is the slop

### Structure / journey (tracer + lieutenant#2)
- 2 ABSOLUTE DEAD ENDS: net-metering-explained (0 ilinks), ev-charging-impact-electric-bill (0 ilinks, 0 outbound) — rg-confirmed
- 7 named missing edges (tracer artifact: complete-guide→dispute, 03→dispute/shutoff/rate-plan, which-rate-plan→ev-charging, etc.)
- 1 wrong-target link: two pages link /blog/why-electric-bill-changes-month-to-month/ (alias of 03, resolves but wrong-target)
- Orphans (grep-verified inbound): do-thermal-curtains (1), 09-apartment (2), ev-charging (2), gadgets (2), single-stage (2), net-metering, water-service-charge (0)... (full list in cartographer-core.md)
- CLUSTERS: 5 trunked (Electricity, Gas, Water&Sewer, HVAC, Bills&Fees) + 1 HEADLESS high-value cluster (Savings & Efficiency — the site's BEST pages 42-space-heater + do-home-energy-monitors have NO hub) + semi-hub glossary
- Cannibalization: lower-electric-bill trio (complete-guide vs how-to-lower-electric-bill-complete-guide vs 05); 11-understanding-kwh vs what-is-a-kilowatt-hour (~50% overlap); 09-apartment state table duplicates average-utility-bills-by-state
- Fees cluster: 13 overlap pairs adjudicated (prospector); TOP MERGE: gas-delivery-charge-vs-supply-charge → 12-how-to-read-your-gas-bill (~70% duplication, 301)

### Trust / E-E-A-T (lieutenant#2 + twin_q)
- Authors: 5 personas NOT real people — but site NOW discloses ("editorial bylines ... not claims of independently credentialed individuals"; "Guides may use AI assistance"). Residual fabrication signals remain (bios still carry credentials-style framing)
- Corrections page logs REAL corrections with figures + retrieval dates — genuine trust asset
- Policies "largely credible, not theater"
- Missing safety/financial disclaimers on risk pages (electrical-panel advice in 47, capacitor testing in 13, variable-rate advice in which-rate-plan) — twin_q Gap 2
- Monetization integrity: HOLDING (disclosures visible; monitor page declines unverifiable links; abrupt free→paid transitions flagged on water-suddenly-increase)

### Ratings snapshot (per-seat, details in artifacts)
- Below 6/10: 50-best-smart-plugs (SEO 5, slug/intent mismatch), 05-how-to-lower-utility-bills (SEO 5), how-utility-rates-fees-usage (5/5, structural), net-metering (SEO 4), ev-charging (SEO 4), which-rate-plan (thin 702w) — full list per artifact
- Strongest: 42-space-heater 9/10, do-home-energy-monitors 9/10, point-sensor 8/10, do-thermal-curtains 8/10 — the new money cohort
- Old cohort legacy pages (0 h2/h3): ac-running, afue, aux-heat, mcf-vs-ccf, average-by-state, gas-vs-electric, heat-pump-running — rebuild candidates (mason slice, in flight)

## Tooling + render corrections (material to the report)

1. METRICS TOOL ARTIFACT: .squad/content-metrics.md counts ONLY markdown `##`/`###` headings and `](/...)` links — pages using HTML `<h2>/<h3>` or `<a href>` markup are FALSELY flagged "0 h2 / 0 ilinks" (prospector#2 found ac-running-but-not-cooling rated "0/0" while actually having 14 H2 sections + 6 internal links). Commander re-verified with grep across formats: the DEAD-END finding is REAL for net-metering-explained, ev-charging-impact-electric-bill, water-service-charge-explained (0 links in ALL formats) — but any "0 ilinks/0 h2" flags on other pages must be re-checked before citing them in the report.
2. RENDER BUGS in source (prospector#2): aux-heat-vs-emergency-heat-meaning.md has truncated `<h2 id="the-problem">The problem: \` and `<h2 id="emergency-heat">...when it` — broken/truncated heading markup that renders wrong.
3. staleY nuance (verifier raw sweep): most "stale-year" flags are LEGITIMATE dated primary citations (NIPSCO IURC order Apr 2025 with in.gov PDF; CPSC 2023/2024; San Antonio 2024 stage rules) WITH retrieval dates and/or current-year counterpoints — the sweep's line-level detail is in /tmp/squad-workspaces/20260830-140430-verifier/staleY-sweep.txt. True staleness ≠ old citation; judge each.

## HVAC slice headlines (prospector#2, from mason-pages.md)

- 13-ac-short-cycling 8/10 (original Record-Pattern method) but no FAQ block
- ac-running-but-not-cooling 9/10 quality (metrics FALSE-negative page)
- aux-heat 6/10 — render bugs + generic framing
- Legacy rebuild list + full 19 entries in the artifact

## In-flight / final status

- twin_q claims rescue: COMPLETE — .squad/SQ-065/wave1/claims-verification.md (10 verdicts: 4 CONFIRMED, 2 REFUTED, 4 UNVERIFIED)
  - REFUTED #1: water-heater blanket ~25% (05-how-to-lower-utility-bills) — DOE/Energy Star cap blanket savings at 4–9%; 25% only for pre-1980s uninsulated tanks → FIX
  - REFUTED #2: heating share 60–70% (07-gas-bill) — EIA RECS: space heating ~40–45% of residential gas; 60–70% conflates/aggregates wrongly → FIX the 40-50 vs 60-70 contradiction on 07
  - CONFIRMED: EIA 899 kWh/mo; $164.88 internal consistency (18.34¢×899); EPA leak figures all defensible; CPSC ~100 generator deaths/yr ~40% CO share; DOE 1%/degree/8h setback
  - UNVERIFIED: EIA 18.34¢ cell value (XLSX truncation — arithmetic consistent though); 28-reconnection PUC table (plausible, uncheckable, no URLs); NIPSCO docket PDF (403 via fetch)
  - Rendered-vs-source sanity: do-home-energy-monitors + which-rate-plan render clean (title/byline/date/prices) ✓
- prospector#2 HVAC: artifact COMPLETE (mason-pages.md, 19 entries); envelope pending (formality)
