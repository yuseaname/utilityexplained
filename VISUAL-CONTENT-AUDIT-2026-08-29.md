# Visual Content Audit & Image-Placement Plan — 2026-08-29 (SQ-056)
Scope: the 10 pages optimized in SQ-055 (traffic ranks 11-20). Method: 3 vision-capable analyst seats **viewed every hero and every existing in-body visual** (grounded read_image descriptions, spot-verified by the Commander against 3 heroes and 1 garbled map viewed directly); plans follow the house style bible ("The Independent Bill Auditor" — VISUAL-RECON-2026-08-28.md). Full per-page plans: `.squad/SQ-056/visual-plans/<slug>.md`.

## Executive summary
- **Heroes: 10/10 present on disk, 8/10 judged suitable as-is at audit.** The two P1 regens (mcf-vs-therms and 18-fuel) are now generated and wired; both replace warm person-scenes on pages whose actual subject is decoding numbers/units. One lower-priority P4 hero refinement remains optional (state-avg map: pin amber to the real cost leaders).
- **URGENT — two live images are actively dishonest:** state-avg carries two AI-generated map infographics with garbled pseudo-text ("Wyouning"-class state labels, unreadable legends). A reader extracts zero facts from them on a page whose entire value is trustworthy numbers. **Removed from the page this session** (files remain on disk; replacements are planned — see queue).
- **Count reconciliation:** the live non-affiliate set is **14 placements** (10 heroes + 4 in-body figures); the two affiliate product images are tracked separately. The plan targets **39 non-affiliate placements** (10 heroes + 29 in-body figures), plus the two retained affiliate product images = **41 total rendered placements**. It calls for **25 new in-body figures and two replacement heroes** (27 new image outputs); the four existing in-body figures stay. This separates visual placements from product-card imagery and avoids counting a replacement hero as an added slot.
- **Product imagery: affiliate rule enforced.** The only two product images in scope (Nest B0D5BBYRJM on 07-gas, Emporia Vue 3 B0C7B1LKDW on smart-meters) already render inside affiliate-wired `{{< product-box >}}` shortcodes (tag + Rybbit `affiliate_click` tracking, auto-visual from `data/product_images.yaml`, "Illustrative" alt convention). Both were **viewed and verified accurate to the real products' form factors** (learning thermostat; monitor hub + 4 clamp CTs). No new product images needed; NO bare un-monetized product figure is planned anywhere.
- **Style-system ruling (Commander):** two-tier is the site's coherent system — heroes depict the page's SPECIFIC subject (scene-style where usage-context is the subject: 07-gas, smart-meters; flat ledger style where numbers/units are the subject: water-usage is the gold standard, mcf/18-fuel regens follow it). ALL in-body figures use the flat auditor grammar: cream ledger paper, faint grid-teal scaffolding, mono numerals, amber strictly on the one element that matters, honest data only.

## Page-by-page audit (compact — full plans in .squad/SQ-056/visual-plans/)

| Page | Hero (viewed verdict) | Visuals now → target | New figures (placement → concept) | Types |
|---|---|---|---|---|
| 23-billing-cycle | SUITABLE-WITH-NOTES (statement under magnifier) | 1 → 4 | cycle-lengths section → calendar-bump ledger diagram; worked example → 28-vs-33-day bars with amber daily-average line; estimated-reads section → estimated-then-trued-up bill strip | 3 illustrative |
| 07-gas-too-high | SUITABLE-WITH-NOTES (kitchen/furnace/meter triptych; v3 option logged) | 4 → 6 | thermostat section → 24-h setback schedule (amber on 8-h window, DOE 10% note from page); water-heater section → tank cross-section with sediment + amber standby-loss arrow | 2 illustrative |
| electric-breakdown | KEEP (dollar-allocation hero; both existing figures verified KEEP) | 3 → 4 | charge-categories table → generic mock-bill category map: the verified 899 kWh × 17.30¢ supply line is real; every other amount is blank | 1 screenshot-style |
| 25-taxes | SUITABLE (layered charge breakdown) | 1 → 4 | rates table → generic three-family mock statement; delivery-tax FAQ → gross-receipts math card; 4-step list → verification-path flow strip | 2 illustrative + 1 screenshot-style |
| state-avg-2026 | KEEP-FOR-NOW (map; regen queued — pin amber to actual cost leaders, Hawaii) | 1 live after removal → 5 | **REMOVED 2 garbled maps this session**; replacements: national-vs-state electric bar ledger (Idaho $125 / national / MA $190 from the page's own table); Idaho-vs-Hawaii 9.8¢ vs 33.7¢ rate-gap card (EIA June 2026, from page) | 4 illustrative |
| 19-surcharges | SUITABLE (itemized add-ons statement) | 1 → 3 | under rider table → rider-anatomy diagram (base rate + named rider layer, PUCO cap callout); 4-step list → tariff→docket→reconcile path strip | 2 illustrative |
| mcf-vs-therms | **REPLACE** (cooking scene is generic for a units-decode page; regen: flat meter with legible CCF register + amber therm conversion) | 1 → 5 | hero regen + units-definition strip (CCF/MCF/therm trio); conversion → 1 CCF ≈ 1.037 therms bridge; worked example → cost-per-therm strip; scenarios → three-bill comparison | hero + 4 illustrative |
| smart-meters | SUITABLE-WITH-NOTES (meter + legible kWh + radio arcs; flat-regen optional) | 2 → 4 | AMR/AMI table → meter-evolution strip (analog → AMR drive-by → AMI two-way); verify section → 24-hour meter-check worksheet (amber on daily delta) | 2 illustrative |
| 18-fuel | SUITABLE-WITH-NOTES → **replace-first in batch** (person-at-bill is the bible's banned pattern; regen: symbolic two-part calculation, no faces) | 1 → 3 | hero regen + identify section → generic tariff-excerpt card (blank fields, no real utility name/rate); compare-bills → two-bill diff ledger (page's own checklist dimensions) | hero + 2 screenshot-style/illustrative |
| water-usage | SUITABLE — gold standard (bill→days→household→calculator, flat, amber accents) | 1 → 3 | worked example → 12 CCF ÷ 30 ÷ 3 ledger card (page's own arithmetic); benchmark → 2-4 CCF/person/month band gauge | 2 illustrative |

*State-avg entered the audit with three placements. The two dishonest in-body maps have been removed, leaving its hero as the single live placement until the four planned figures are generated.

## Generation queue (ordered)
**P0 — removals already done this session:** the two garbled state-avg map figures (unwired from the page; files still on disk: `..._section-1_00003_.webp`, `..._section-2_00003_.webp` — delete or archive at next asset sweep). Also flagged: orphan off-style photo `07-gas-bill-too-high/custom_inline.webp` (unreferenced; do not wire).
**P1 — hero regens (2):** mcf-vs-therms (flat meter, legible register, amber therm conversion); 18-fuel (symbolic calculation, no faces).
**P2 — highest-impact in-body (6):** state-avg electric bars + rate-gap card; 07-gas setback schedule + standby-loss cross-section; 23-billing worked-example bars; smart-meters meter-evolution strip.
**P3 — remaining in-body (19):** state-avg gas-range and basket cards ×2; 25-taxes ×3; 19-surcharges ×2; 23-billing ×2; water-usage ×2; mcf-vs-therms ×4; smart-meters worksheet; electric-breakdown category-map mock bill; 18-fuel tariff excerpt and comparison ledger.
**P4 — optional hero polish:** state-avg map regen; 07-gas v3 (schematic still-life); smart-meters flat regen.
Every brief in the plan files carries placement, concept, purpose, format/orientation, type, filename, and affiliate wiring. The P1–P3 scope is **generated and wired**: 27 image outputs in total (P1 2 + P2 6 + P3 19). The style bible is embedded in each brief.

## Generation and wiring completion — 2026-08-29

**P1 through P3 are complete.** All 27 planned outputs were generated in the Independent Bill Auditor visual system, converted to production WebP, and wired to their planned page placement. The two P1 hero replacements now power the affected pages' social/structured-data images and accessible frontmatter alt text.

| Page | Generated and wired output count | Completion |
|---|---:|---|
| 23-billing-cycle | 3 | timeline, daily-average comparison, estimated-to-actual correction |
| 07-gas-too-high | 2 | thermostat setback schedule, water-heater standby-loss cross-section |
| electric-breakdown | 1 | bill-category map |
| 25-taxes | 3 | line-family mock bill, gross-receipts math, verification path |
| state-avg-2026 | 4 | state/national bar ledger, rate gap, gas range, basket comparison |
| 19-surcharges | 2 | rider anatomy, tariff-to-reconciliation path |
| mcf-vs-therms | 5 | replacement hero plus four unit/conversion/cost/scenario figures |
| smart-meters | 2 | meter evolution, 24-hour check worksheet |
| 18-fuel | 3 | replacement hero, tariff excerpt, two-bill comparison |
| water-usage | 2 | household calculation, per-person benchmark band |
| **Total** | **27** | **2 replacement heroes + 25 in-body figures** |

**Verification:** every new source is present at its production path; `npm run verify` completed successfully (Hugo production build, image-path checker, and content audit). Rendered-page inspection at desktop and mobile was used to confirm the article image frame, lazy loading, page gutters, and figure legibility in context. Existing content-audit flags on unrelated source completeness and future-dated claims remain non-blocking and are not image-generation failures.

**Intentional exclusions:** the two removed garbled state-map files and 07-gas `custom_inline.webp` remain on disk for a later asset sweep but are still unwired. P4's state map, 07-gas, and smart-meter hero refinements remain explicitly optional and were not included in this generation scope.

## Affiliate wiring (confirmed)
- Product imagery exists ONLY inside affiliate-wired shortcodes: Nest (07-gas) and Vue 3 (smart-meters) product boxes auto-render `data/product_images.yaml` visuals inside the tagged, tracked link. Both viewed: accurate form factors, "Illustrative" alt labels, no invented branding/specs.
- No planned figure depicts a product outside an affiliate mechanism. Screenshot-style figures use generic mock bills with on-page verified numbers only — no real utility names/logos, no fabricated rates.
