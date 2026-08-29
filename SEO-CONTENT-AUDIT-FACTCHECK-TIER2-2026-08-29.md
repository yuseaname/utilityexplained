# UtilityExplained — Tier-2 Content Audit & Remediation (SQ-053)

**Date:** 2026-08-29 · Pages: site traffic ranks 31-60 (Rybbit 30d pv, slash-merged, deleted/draft pages excluded — stated per brief; GSC not accessible).
**Method:** 7-seat wave 1 (lieutenant slot re-run on wing after a channel-contamination incident) + GLM wave-2 cross-family verification + 3-seat remediation + Commander disk-checks. Every shipped number traced to a source fetched 2026-08-29.

## Status column: ✅ fixed today · 🔧 rebuilt today · ⏳ open (logged)

| # | Page (slug) | Grade | Key issues found | Factual verdicts (evidence) | Status / what shipped |
|---|---|---|---|---|---|
| 31 | 01-how-to-read-your-electric-bill | **A** | None material — 14 outbound sources, canonical-worthy | Cluster-canonical status CONFIRMED (wave-2) | ⏳ none needed |
| 32 | 21-past-due-balance | **D**→ | 536w "ask the provider", 1 CFPB source, 88.9% br | TX/PUC deposit+notice rules verified | 🔧 rebuilt: CFPB + state notice-period framework |
| 33 | 26-utility-deposit | **D**→ | 501w, no amounts/caps/waivers, 94.7% br | TX cap **verified verbatim** (1/5 annual or 2 months); SCE deposit pages verified | 🔧 rebuilt: TX + CA + MN 216B.098 frameworks |
| 34 | 14-estimated-utility-bill | **C**→ | 444w thin | ConEd FAQ factors verified live | 🔧 rebuilt: EST workflow + PUC rules |
| 35 | how-to-read-gas-meter | **D** | 3,284w but ZERO sources, answer below fold, 87.5% br/5s | — | ✅ hero flag; ⏳ sourcing pass open |
| 36 | water-service-charge-explained | **C−** | Answer buried under 7 headings, 4s TOP | — | ✅ hero flag; ⏳ restructure open |
| 37 | 43-understand-natural-gas-bill-charges | **F** | 442w defensive procedural, 100% br/0s | Content-loss-free redirect confirmed (1 inbound link) | ✅ DELETED → redirects to 12 |
| 38 | 17-what-is-customer-charge | **F**→ | 418w zero examples | SMUD $27.00/mo **verified**; Austin $16.50; PG&E ~$24; Consumers $8 | 🔧 rebuilt: 4 verified utility examples |
| 39 | 11-understanding-kwh-usage | **B** | 2 dead energysaver URLs | 18.34¢ + 899 kWh CONFIRMED (EIA) | ✅ URLs swapped |
| 40 | sewer-averaging-water-bill | **C** | Thin sourcing (1 source) | Broken-link claim vs /water-explained/ **REFUTED by Commander** (page exists) | ⏳ municipal anchors open |
| 41 | complete-guide-understanding-utility-bill | **C−** | 923w thin for "complete guide"; wrong-intent aliases | Alias placement REFUTED 2-of-3 (wave-2) | ✅ data aliases moved to state-average page; ⏳ expansion open |
| 42 | 16-budget-billing-level-pay | **D**→ | Defensive QA, worked example 4 screens deep, **leaked editorial note in prose**, dangling FM sources | All confirmed (wave-2) | 🔧 fixed: mechanism-first QA + reorder + note removed + FM pruned |
| 43 | why-water-higher-in-winter | **C** | 846w thin for 8-cause promise | EPA anchors OK | ⏳ open |
| 44 | 20-utility-bill-proration | **D**→ | 484w, no definition of proration, 1s TOP | SMUD $27÷30×20=$18 math ✓; PG&E $0.19713/day verified | 🔧 rebuilt: definition-first + verified examples |
| 45 | why-water-higher-in-summer | **B** | 1,280w solid but 0 sources | EPA 60%-arid verified | ⏳ sourcing pass open |
| 46 | tiered-water-rates-explained | **B−** | Best engagement in tier (33.3% br); CO HB1090 claim flagged; 0 sources | HB1090 tenant-billing claim UNVERIFIED | ⏳ verify HB1090 + sources |
| 47 | 44-how-to-lower-water-bill | **B** | "30–40% habits" + "$200" attributed to EPA — **REFUTED**; dead fix-leak URL | EPA real language verified: 10% leak savings, ~20% fixtures, $1,300/$500 | ✅ refuted claims replaced + URL fixed |
| 48 | moving-utilities-checklist | **B** | 2,451w, 0 sources | No factual errors found (21 checks) | ⏳ sourcing pass open |
| 49 | why-did-my-utility-bill-go-up-this-month | **C**→ | 0s TOP = 143KB full-bleed hero above QA + narration-first QA (mechanism confirmed in code/CSS/bytes) | Diagnosis CONFIRMED (wave-2) | 🔧 fixed: hero flag + five-things action-first QA |
| 50 | 24-delivery-charge-vs-supply | **B** | 424w thin but accurate; canonical role confirmed | ConEd sourcing verified | ⏳ keep as utility-generic canonical; cross-linked from gas twin |
| 51 | how-to-lower-electric-bill-without-solar | **C** | 587w, non-actionable, 2 dead URLs | — | ✅ URLs swapped; ⏳ rebuild open |
| 52 | 12-how-to-read-your-gas-bill | **B**→ | "80–150 therms winter" **REFUTED as attributed** (RECS = annual only); internal band conflicts vs 07/mcf | RECS 2020 CE5.4 annual splits verified (607/184/41 Ccf ≈ 860 therms, arithmetic Commander-checked) | 🔧 rebuilt: climate-zone framing + absorbs 43 |
| 53 | 50-best-smart-plugs | **C+** | Emporia "outdoor rated" **REFUTED by manufacturer** ("Indoor use only") — safety-relevant | Emporia support docs verified | ✅ corrected + manufacturer source added; ⏳ full claim pass open |
| 54 | gas-delivery-charge-vs-supply-charge | **D**→ | ZERO sources; Columbia Gas $3.25/Mcf example **miscategorized** (it's Ohio SCO supply, not delivery); Localsyr stat wrong domain | Wave-2 flagged; fix-seat re-verified at source | 🔧 rebuilt: SCO re-categorized + full source layer |
| 55 | 22-minimum-bill | **F**→ | 445w, zero tariff examples, 100% br/0s | Avista + PG&E minimum clauses fetched | 🔧 rebuilt: verified tariff examples |
| 56 | can-utility-shut-off-service | **B−** | 3,002w lifecycle hub, 0 sources | — | ⏳ sourcing pass open |
| 57 | 46-what-time-is-electricity-cheapest | **C+** | Overlaps 08-time-of-use (SQ-045 fold design) | — | ⏳ fold decision open |
| 58 | 10-fixed-vs-variable-utility-rate | **C+** | 860w; draft twin exists | — | ⏳ open (scout seat died; triage-lite only) |
| 59 | how-to-dispute-utility-bill | **C** | 603w thin | — | ⏳ open (triage-lite) |
| 60 | 09-apartment-utilities-cost | **C−** | 100% br/0s, 908w | — | ✅ hero flag; ⏳ open (triage-lite) |

## Shipped today (tier 2)
**9 pages rebuilt/fixed by verified evidence** (21, 26, 14, 17, 20, 22, 16, 12, gas-delivery) + **43 consolidated into 12** + surgical fixes on 44, 50-smart-plugs (safety), why-did-my, 11-kwh, without-solar, complete-guide aliases, 02/43 draft deletions, hero flags ×10, dead URLs ×4. Build green: 466 pages, 203 aliases, asset gate OK. Staged in git, uncommitted.

## Open queue — CLOSED 2026-08-29 (SQ-054)

All open-queue items executed same-day, every shipped number verified at source (retrieved 2026-08-29):

- **Sourcing passes DONE (8):** gas-meter (3,284w → 2,877w rebuilt, SoCalGas meter guide + leak-safety + 2 EIA pages, 21 quotes byte-verified); water-service (1,425→1,661w, Louisville 2026 tariff / Philadelphia PWD / Cleveland Water fixed charges — all re-verified from cached PDFs); can-shut-off (3,002→3,379w, MN Statutes 216B.096/.097/.098 + USA.gov, cross-family-verified 5/5 SOUND); tiered-water (CO "HB1090" **REFUTED — no such bill**; real law HB25-1090 is a deceptive-pricing statute with the *opposite* framing, now correctly cited; Austin Water 5-tier table $3.27–$20.40/1,000 gal with recomputed worked examples); moving (USPS $1.25/12-mo/3-business-day facts verified verbatim; unsourced notice windows reframed); summer + winter water (broken table replaced with EPA framework; winter now delivers all 8 promised causes); sewer-averaging (924→1,464w, Austin $11.26 base + $13.40 tier-2 + "whichever is lower" + SAWS Nov 15–Mar 15 window, all verified at source)
- **Rebuilds DONE:** without-solar (587→1,181w actionable: DOE 7–10°F/10%, ENERGY STAR ducts 20–30%, EIA 52%/899 kWh/$144/18.34¢, product-box, 9-source layer); complete-guide → workflow hub (17-charge link table to every line-item explainer; retitle had already shipped); 50-smart-plugs full claim pass (**KP125MP2 is not a real SKU → renamed KP125M** at manufacturer; unverifiable warranty cells deleted; standby-watt heuristics labeled; all 4 SKUs re-verified at tp-link.com)
- **Verified:** CO HB1090 (refuted, corrected); 50-plugs claims (cross-family SOUND)
- **Decisions MADE:** 46 stays standalone (fold design predated its 2026-08-28 verified rebuild; instead fixed 3 numeric defects: fabricated "40–60% typical off-peak discount," invented "8¢ typical off-peak," dishwasher math — now ENERGY STAR $50/yr + ConEd tariff-anchored); 2026-utility-cost-index + how-to-read-your-utility-bill drafts stay parked (50-state table unverified; 700w draft below standard — aliases remain as redirects); 10-fixed draft twin DELETED (wholly redundant; live 10- carries its alias)
- **Triage-lite pages → full treatment:** 10-fixed (EIA 18.44¢ **error → 18.34¢**; 6 unverifiable provider rates deleted → mechanics table + official portals PowerToChoose/PAPowerSwitch/EnergyChoiceOhio; retitled to intent; leaked editorial note removed); dispute (603→2,477w — full escalation ladder utility→written complaint→PUC→escalation, CPUC + PUCT 10-day + disputed-charge rules verified at source, template letter, evidence checklist); apartment (QA now number-bearing via EIA "single-family detached uses nearly 3× the energy of 5+-unit apartments," table relabeled all-home, 4 internal links, unsourced "most apartments include" softened)

**Build:** 470 pages, 205 aliases, asset gate OK. Staged in git, uncommitted.

**Still open (carried forward):** human register (EIA 5.4.a direct fetch, Nest/P3 specs, PG&E tariff currency, author substantiation incl. "Marcia Washington" on 3 pages); 4 Amazon ASINs unverifiable off-Amazon (B08LN3C7WK, B0BYGRLRS1, B0DKGBP38V, B0CLVV7X7Y); Austin averaging-window months (rate sheet doesn't state them — confirm with Austin Water). Tier-3 backlog: 4 files still carry dead energy.gov/energysaver URLs (42-space-heater, gadgets-that-lower-utility-bills, 47-check-energy-leaks, do-programmable-thermostats — live replacements known). Watch in Rybbit (14-day): tiered-water bounce should hold ≤33%; gas-meter (was 87.5% br/5s — QA now above fold); apartment (was 100% br — number-bearing QA); dispute + shut-off engagement; 10-fixed on intent-aligned title.
