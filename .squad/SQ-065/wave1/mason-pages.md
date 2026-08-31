# SQ-065 Wave 1 — Prospector ($2) Bulk Audit: HVAC/Appliance/Meter Cluster (19 pages)
Auditor: prospector (shard miner, dsv4-flash) | Date: 2026-08-30
Method: full-file reads of all 19 content/blog/*.md; quotes cited by path. Ratings grounded in evidence. Cross-shard notes: metrics source content-metrics.md counts markdown `##`/`###` headings only and misses HTML `<h2>/<h3>` and `{{< ref }}` links — several "0 h2" flags below are metrics artifacts, flagged per page.

---

## 1. /blog/13-ac-short-cycling-causes-fixes/ — What to Do When an AC Starts and Stops Frequently
- **Purpose/intent**: Troubleshooting / diagnostic-informational for cold-weather AC short-cycling; answers "record first, safe checks only, call pro when uncertain."
- **Quality: 8/10 | SEO: 8/10**
- **Strengths**: Record-Pattern method is original and practical; two decision tables (Common Causes + Diagnostic Decision) break cause from symptom; explicit cost ranges and time-to-diagnose; Manual J recommendation repeated; sources are DOE Building Science + archived DOE doc.
- **Weaknesses**: No FAQ block despite site-wide FAQ schema pattern (metrics show faq=0); no hero/spread TOC; slight over-caution tone may delay homeowners from a simple filter fix.
- **AI-slop**: none — concrete, specific, cited.
- **Visual gaps**: no diagnostic diagram (e.g., "frozen-coil vs low-charge vs capacitor"), no table graphic needed but a cause-priority visual would help.
- **Action**: improve — add an FAQ block (3–5 short Q&A) + a labeled table avatar; keep the two decision tables.

## 2. /blog/ac-running-but-not-cooling/ — AC Running but Not Cooling? 13 Causes and Safe Fixes
- **Purpose/intent**: Panic troubleshooting: AC runs, no cooling. First-screen short answer gives immediate safe actions (thermostat→fan→filter→vents→thaw).
- **Quality: 9/10 | SEO: 8/10**
- **Strengths**: Strong first-screen answer (matches tropes but useful); 14 H2 sections with safe/DIY split; TOC; 5 FAQs with schema; internal links to MERV, duct-leaks, single-stage, afue, 03-why-high, ductless-mini; sources DOE+ENERGY STAR. Ranked cause progression mirrors pro diagnostic discipline.
- **Weaknesses**: Metrics table lists 0/0 h2 and 0 ilinks — FALSE: page uses HTML `<h2>/<h3>` and `<a>` internal links; metrics tool only sees markdown syntax. (Structural risk: being mislabeled thin by tooling.)
- **AI-slop**: none.
- **Visual gaps**: no frozen-coil photo/diagram, no outdoor-unit debris image; a simple "vent-deltoid / supply air vs return" graphic would help first-screen comprehension.
- **Action**: keep/improve — convert HTML headings to markdown for tooling parity; add two diagnostic images; keep.

## 3. /blog/aux-heat-vs-emergency-heat-meaning/ — Aux Heat vs Emergency Heat, in Plain English
- **Purpose/intent**: Diagnostic-informational explaining two thermostat labels; answers cost/runtime panic.
- **Quality: 6/10 | SEO: 8/10**
- **Strengths**: Clear two-mode model (heat pump first, backup second); triggers list; bill-sanity checks; misconceptions; 5 FAQs; internal links (afue, duct-leaks, gas-vs-electric, 03-summer).
- **Weaknesses**: RENDER BUGS in source — `<h2 id="the-problem">The problem: \` is truncated/stray-backslash and `<h2 id="emergency-heat">What Emergency Heat means (and when it` is truncated (missing closing); both render as broken headings. Metrics 0/0 h2 is FALSE for same HTML-tag reason. Page is otherwise sound.
- **AI-slop**: none, but title/meta and section ordering is generic.
- **Visual gaps**: no thermostat-display mockup ("AUX/EMER" label), no cost-comparison strip of resistance vs heat-pump.
- **Action**: improve — fix the two broken headings + convert HTML headings to markdown; add one thermostat-label mockup.

## 4. /blog/heat-pump-running-all-day-in-winter/ — Heat Pump Running All Day in Winter: Normal or Not?
- **Purpose/intent**: Reassurance/runtime diagnostic.
- **Quality: 6/10 | SEO: 7/10**
- **Strengths**: First-screen reassurance (long runtime can be normal); defrost explainer; aux-heat link; 5 FAQs; running-patterns table (Normal vs Concerning).
- **Weaknesses**: Thin text near 958 words; limited original depth (rests on DOE/ENERGY STAR only); metrics 1/0 h2 is FALSE (HTML tags again); the "Related Reading" tail only points to ac-running — weak cluster navigation.
- **AI-slop**: none, but "carrying buckets in the snow" metaphor is light.
- **Visual gaps**: no runtime-vs-temperature plot (the pattern table implies one); could use a simple line chart.
- **Action**: improve — fold the pattern table into a chart; add links to aux-heat/duct-leaks already present; keep.

## 5. /blog/why-is-my-furnace-blowing-cold-air/ — Why Is My Furnace Blowing Cold Air? (And How To Fix It Now)
- **Purpose/intent**: Safety-first troubleshooting (CO, gas); 15-minute check table.
- **Quality: 9/10 | SEO: 9/10**
- **Strengths**: Best safety framing on the site (safety first, DIY second); 15-min table; cause list (DIY vs pro); CPSC + IRS sourced; 2026-fresh 25C credit note (expired 12/31/2025); 4 FAQs; 5 related-reading links.
- **Weaknesses**: No major weak point; metrics 10/5 h2/h3 markdown; accurate.
- **AI-slop**: none.
- **Visual gaps**: the one thermostat image (FAN ON vs AUTO) is exactly the right visual; could add a CO-alarm placement diagram.
- **Action**: keep — optional add CO-alarm placement image.

## 6. /blog/duct-leaks-symptoms-hvac-running-all-day/ — Duct Leak Symptoms: Uneven Rooms & the HVAC Runs All Day
- **Purpose/intent**: Symptom-list diagnostic; duct test explanation (CFM25, blower door).
- **Quality: 9/10 | SEO: 8/10**
- **Strengths**: 8 symptoms each with cause; 15-min DIY observation checklist with safety boundaries; mastic-vs-duct-tape rule (ENERGY STAR quote); runtime math table explicitly labeled arithmetic-only; FAQs + FAQ schema.
- **Weaknesses**: Metrics ilinks=0 is FALSE — page has 4 `{{< ref }}` links in Related Reading (metrics ignores shortcode refs). No hero image path issue noted; one diagram already present.
- **AI-slop**: none.
- **Visual gaps**: diagram exists (duct-leak-diagram.webp is good); no blower-door/CFM25 explainer image.
- **Action**: keep — convert `{{< ref }}` to direct hrefs if tooling requires; add blower-door illustration.

## 7. /blog/single-stage-vs-two-stage-vs-variable-speed-hvac/ — Single-Stage vs Two-Stage vs Variable-Speed HVAC
- **Purpose/intent**: Buyer-education comparison of staging/variable-speed.
- **Quality: 8/10 | SEO: 7/10**
- **Strengths**: Definitions; runtime/humidity behavior per type; side-by-side tables (run time, swing, humidity); climate/home-fit table; thermostat compatibility section (ecobee/Nest link); affiliate disclosure + product box; 6 sources incl. DOE sizing PDF and ASHRAE.
- **Weaknesses**: No FAQs block (metrics faq=0); no internal links despite metrics ilinks=0 (also FALSE — the page links to 42-space-heater + product box uses Amazon link + elsewhere links); some humidity claims ("20-30% more humidity", "40-45% indoor humidity") lack a citation anchor; product box description cites ecobee spec page.
- **AI-slop**: none.
- **Visual gaps**: capacity-waveform visual present; no thermostat wiring diagram for stages.
- **Action**: improve — add 3–5 FAQ Q&A; cite DOE/ENERGY STAR for humidity math; add wiring/compatibility diagram.

## 8. /blog/ductless-mini-split-vs-central-air/ — Ductless Mini-Split vs Central Air: How to Compare Systems
- **Purpose/intent**: Purchasing comparison; proposal-comparison aids.
- **Quality: 9/10 | SEO: 8/10**
- **Strengths**: Verified efficiency anchors (federal 14.3/7.5 SEER2/HSPF2, 13.4 SEER2; ES 15.2/7.8; cold-climate COP≥1.75 at 5°F; certified max 35.1 vs 25.0); duct-loss 20–30% quoted from ENERGY STAR; Mass Save cost anchors; proposal-item table; 17 sources; 3 FAQs; affiliate box.
- **Weaknesses**: Metrics ilinks=1 FALSE (has links to 48-heat-pump, product boxes); stale-year refs: the 25C credit is explicitly marked ended 12/31/2025 — matches sibling page; two manufacturer-source citations properly labeled as claims. In-source numbering has a 13/14 swap (Sources show 14 before 13) — cosmetic.
- **AI-slop**: none.
- **Visual gaps**: no per-head cost-vs-zone bar chart; no line-set routing diagram (describes 3-inch penetration).
- **Action**: keep/improve — fix source numbering; add zone-cost chart.

## 9. /blog/afue-vs-seer-vs-hspf-vs-cop/ — AFUE vs SEER vs HSPF vs COP, in Plain English
- **Purpose/intent**: Ratings explainer.
- **Quality: 7/10 | SEO: 6/10**
- **Strengths**: One-sentence definitions for AFUE/SEER/HSPF/COP — a solid plain-English framing; compare-like-with-like section; misconceptions; 5 FAQs + schema.
- **Weaknesses**: Metrics 1/0 h2 is FALSE (HTML tags used); more importantly: only a single DOE source (homeHeating.pdf), zero internal links INTO other cluster pages beyond aux-heat/merv/duct-effects links out — this page is the cluster hub yet has the thinnest sourcing and no outlink-to-support pages; no tables despite being a comparison page (metrics tbl=0).
- **AI-slop**: none but generic phrasing in examples ("higher SEER generally means less electricity").
- **Visual gaps**: crying out for a ratings-comparison matrix (what measure, unit, applies-to, example) — currently only h2 text.
- **Action**: improve — add a comparison matrix table, 2–3 more sources (ENERGY STAR, AHRI), and link in/out to 48-heat-pump and ductless-mini; keep.

## 10. /blog/what-merv-rating-do-i-need/ — What MERV Rating Do I Need?
- **Purpose/intent**: Purchase-guide for furnace filters.
- **Quality: 9/10 | SEO: 8/10**
- **Strengths**: Quick answer (MERV 8 default; 11 allergies; 13 only if rated); uses EPA/CDC framing carefully (capture vs health); capture-vs-airflow trade; sizing section (measure old filter frame); honest economics; product boxes with size/tier labels; 5 sources incl. EPA.
- **Weaknesses**: Metrics tbl=3 FALSE (has 3 markdown tables + visuals); very strong; no notable defects.
- **AI-slop**: none.
- **Visual gaps**: MERV-particle-ladder and capture-vs-airflow visuals present.
- **Action**: keep.

## 11. /blog/45-whole-house-generator-vs-portable-cost/ — Whole House Generator vs Portable: True Cost
- **Purpose/intent**: Decision/comparison with safety emphasis (CO).
- **Quality: 8/10 | SEO: 7/10**
- **Strengths**: Safety first (20-ft rule, CO alarms, CEA stats), 3 connection paths (cords/interlock/transfer switch), NEC 702 backfeeding warning, load-starting-surge method, 13 sources incl. CPSC, federal register; cost anchors (interlock $200–400, transfer $300–600 to ~$1,600, standby $8k–16k).
- **Weaknesses**: stale-year refs (metrics staleY=4): page repeatedly cites 2023 federal register rule and CPSC 2024/2026 releases with 2026 retrieval dates — while correct, several references (CPSC 2026 release, Generac data) carry 2026 dates that may still be live; but 4 "stale" refs likely map to 2023/2024 dated sources. All are appropriately labeled by year/date. Missing FAQs? faq=3 present; fine.
- **AI-slop**: none.
- **Visual gaps**: no illustration of the 20-ft radius/exhaust-away rule; no load-sizing worksheet graphic.
- **Action**: keep/improve — verify the 4 stale-year refs point to current pages (CPSC 2026 releases exist) and add a CO-placement diagram.

## 12. /blog/48-heat-pump-vs-gas-furnace-savings/ — Heat Pump vs Gas Furnace: Which Is Cheaper to Run?
- **Purpose/intent**: Decision math with locally runnable formula.
- **Quality: 9/10 | SEO: 9/10**
- **Strengths**: Formula (HP vs furnace per MMBtu, breakeven rule), national-average worked examples (Jan-2026 17.45¢/kWh, $1.35/therm; June-2026 18.34¢/kWh, May-2026 $1.92/therm), cold-climate COP≥1.75 NEEP anchor, 25C credit ended correctly, EIA winter-fuel table, 14 sources.
- **Weaknesses**: staleY=5 in metrics: the 5 "stale-year" hits are likely the 2023/2025/2026 policy dates — but page is explicitly current (2026 average dates), so those refs are (correctly) dated; still, repeated "January 2026" / "June 2026" figures should carry retrieval date note. No FAQs beyond 3 but enough.
- **AI-slop**: none.
- **Visual gaps**: no ratio-vs-breakeven chart; a line chart of ¢/kWh÷$/therm and the COP threshold would materially help.
- **Action**: keep/improve — add breakeven-ratio chart; keep the formula section.

## 13. /blog/gas-vs-electric-heating-cost-comparison/ — Gas vs. Electric Heating: Cost Comparison for Real Homes
- **Purpose/intent**: Informational cost comparison.
- **Quality: 6/10 | SEO: 6/10**
- **Weaknesses (significant)**: (a) At top, malformed inline link: `[For more detail, see our guide to [heat pump savings](/blog/48-heat-pump-vs-gas-furnace-savings/).]` — markdown nested brackets will render oddly on page. (b) Uses HTML `<h2>` headings + HTML `<table>` — legacy pattern again; metrics 2/0 h2 is low but real. (c) Its cost table ($1.60/therm, 95% furnace, COP 2.5) contradictingly uses a 95% furnace vs 48-heat-pump's 96% AFUE framing; illustrative but inconsistent. (d) Only 1 source (DOE policy post), very weak for a cost-comparison topic; (e) tail only links to generator page — poor cluster navigation.
- **AI-slop**: mild — generic bullet "Compare local gas price per therm…" reads as fill.
- **Visual gaps**: no cost-vs-rates chart; no example-by-region.
- **Action**: merge → into /blog/48-heat-pump-vs-gas-furnace-savings/ (better source base, formula, and current data) OR improve with sources + fix broken link and table formatting. Recommend merge with redirect.

## 14. /blog/how-to-find-and-seal-drafts-in-your-home/ — How to Find and Seal Drafts in Your Home
- **Purpose/intent**: Seasonally useful DIY how-to.
- **Quality: 9/10 | SEO: 8/10**
- **Strengths**: Renter-ok tagging throughout; 10-spot tour; detection kit (hand/smoke/flashlight); exact product/tier table with price bands; safety never-seal list; 25C note; 6 visuals; 3 FAQs + schema.
- **Weaknesses**: content-metrics shows tbl=2 — accurate (2 markdown tables); long but justified.
- **AI-slop**: none.
- **Visual gaps**: full set of visuals is a differentiator.
- **Action**: keep.

## 15. /blog/47-check-energy-leaks-home-diy/ — DIY Home Energy Audit: Start Your Own Assessment
- **Purpose/intent**: DIY audit walk-through.
- **Quality: 9/10 | SEO: 8/10**
- **Strengths**: DOE walk-through 6-step sequence; pressurization/incense method; service boundary; phantom-load LBNL figure; thermal camera nuance; professional-audit costs; Home Energy Score path; 7 sources; action checklist; 3 FAQs.
- **Weaknesses**: metrics ilinks=3 accurate; long and very dense — some readers may need subtitles.
- **AI-slop**: none.
- **Visual gaps**: house cross-section image present.
- **Action**: keep.

## 16. /blog/gadgets-that-lower-utility-bills/ — Tools That Can Help You Understand Utility Use
- **Purpose/intent**: Gadget-purchase guidance.
- **Quality: 7/10 | SEO: 7/10**
- **Strengths**: "measure before buy" discipline; product-by-product payback math (e.g., 180W fridge ≈ $260/yr; smart thermostat $60–140/yr; water leak sensor as damage prevention); when-these-do-not-pay section; 5 sources; table + product boxes.
- **Weaknesses**: Title says "lower" but correct content says "understand" — H1/title mismatch can hurt CTR; metrics ilinks=4 accurate; no FAQs block; LBNL standby figure used in sibling as well.
- **AI-slop**: none.
- **Visual gaps**: bars visual exists.
- **Action**: improve — adjust title/slug intent to "understand/select tools," add 3–5 FAQs.

## 17. /blog/phantom-power-draw-explained/ — Phantom Power Draw: How to Find and Reduce Standby Use
- **Purpose/intent**: Standby-power education/audit.
- **Quality: 8/10 | SEO: 7/10**
- **Strengths**: device-class standby wattage table; total-home math (51.5W → $83/yr at 18.4¢); kill-a-watt method; smart-plug automation; 5 sources incl. DOE + LBNL; product boxes.
- **Weaknesses**: metrics faq=0 — no FAQ block despite strong Q&A material; ilinks=4 accurate.
- **AI-slop**: none.
- **Visual gaps**: bars visual present.
- **Action**: improve — add 3–5 FAQs; add "does unplugging pay" decision table.

## 18. /blog/how-do-smart-meters-work/ — How Do Smart Meters Work? (And Should You Trust Them?)
- **Purpose/intent**: Explain smart-meter tech + reassurance.
- **Quality: 8/10 | SEO: 8/10**
- **Strengths**: First-screen quick answer; analog/AMR/AMI table; accuracy explanation (meter tests free in many states); privacy var; verification method (24h read); opt-out fees; 5 FAQs + schema; 6 internal links.
- **Weaknesses**: metrics 2/0 h2 is FALSE (uses HTML h2s); otherwise strong.
- **AI-slop**: none.
- **Visual gaps**: evolution strip + 24h worksheet present.
- **Action**: keep — convert headings for tooling parity.

## 19. /blog/what-is-a-kilowatt-hour/ — What Is a Kilowatt-Hour (kWh)? Definition & Calculator
- **Purpose/intent**: Foundational definition.
- **Quality: 8/10 | SEO: 8/10**
- **Strengths**: Clear kW-vs-kWh speedometer/odometer; real-device examples; simple formula (watts/1000×hours); "my bill only kWh?" misconception; 5 FAQs + schema; 6 internal links; EIA source.
- **Weaknesses**: metrics 1/0 h2 is FALSE (HTML tags); thin-ish (919 words) but appropriately scoped.
- **AI-slop**: none.
- **Visual gaps**: hero + no visual in body; a kWh-stacking bar (device examples) would sharpen.
- **Action**: keep/improve — add one example-equivalences visual.

---

## Cross-Page Number Contradictions Found
1. **AFUE framing**: /blog/gas-vs-electric-heating-cost-comparison/ uses 95% furnace in cost table; /blog/48-heat-pump-vs-gas-furnace-savings/ uses 96% AFUE as the breakeven benchmark (totals 3.41×COP÷AFUE math). Mild inconsistency; both pages live and neither references the other's number.
2. **Electric rate**: gadgets-that-lower-utility-bills and phantom-power-draw-explained both use 18.4¢/kWh (consistent); 48-heat-pump uses 17.45¢ (Jan) and 18.34¢ (Jun) — different data vintage but flagged as different months; acceptable, yet a cross-page rate line would help.
3. **SEER2/HSPF2**: ductless-mini (14.3/7.5; ES 15.2/7.8; NEEP 8.5HSPF2) matches 48-heat-pump (14.3/7.5; ES 8.5 cold-climate) — consistent. No contradiction.
4. **Wattage examples**: what-is-a-kilowatt-hour 1500W×3h=4.5kWh; 42-space-heater 1500W×8h≈$2.20/day at 18.4¢ — consistent (8h 1500W = 12kWh×0.184 = $2.21). Good.
5. **Standby**: phantom-power 32–87W/home (pre-standard) and 51.5W modern total; 47-check-cites 67W avg (LBNL) — different reference studies, not contradicted but should note two sources.
6. **25C credit**: 48-heat-pump and why-is-my-furnace-blowing-cold-air both correctly state 25C ended for property 12/31/2025; ductless-mini also states ended; no contradiction.
7. **Metrics mismatch (tooling-level)**: content-metrics.md under-counts HTML-headed pages and `{{< ref }}` links — treat its h2/tbl/ilinks columns as unreliable for this cluster.

---

## LEGACY REBUILD LIST (ranked)
1. **/blog/gas-vs-electric-heating-cost-comparison/** — genuinely marginable/legacy in structure: broken nested markdown link, HTML table/headings, single source, cost table misaligned with sibling page, poor cluster endings. Highest logical merge candidate → /blog/48-heat-pump-vs-gas-furnace-savings/ (redirect) OR rebuild with markdown headings + 6–8 sources + rate-vs-breakeven chart.
2. **/blog/afue-vs-seer-vs-hspf-vs-cop/** — cluster hub with thinnest sourcing (1 source, no table) and no inbound links from newer pages beyond mention; rebuild to add comparison matrix, 2+ sources, and deep links to/from 48-heat-pump & ductless-mini. Currently reads 'legacy' more than other flagged pages despite HTML headings.
3. **/blog/aux-heat-vs-emergency-heat-meaning/** — two broken/truncated H2 tags render visibly; rebuild section headings and add LOCKUP/EMER mockup visual; otherwise content sound.
4. **/blog/heat-pump-running-all-day-in-winter/** — thin (958 words); extend with runtime vs outdoor-temp data or merge partial runtime content into 48-heat-pump; add actual runtime chart.
5. **/blog/ac-running-but-not-cooling/** — NOT structurally obsolete (strong content/toc/FAQs); needs only tooling-parity markdown heading conversion. Keep — do not rebuild.
6. **/blog/what-is-a-kilowatt-hour/** — not obsolete; add example visual; keep.

## Priority Actions (this cluster)
- (A) Merge/redirect gas-vs-electric into 48-heat-pump (or rebuild with sources + fix broken link).
- (B) Fix aux-heat broken headings + afue comparison matrix + single-stage FAQ block.
- (C) Re-audit content-metrics.py to count HTML h2/h3 + `{{< ref }}` links; otherwise tooling will keep flagging strong pages as thin/legacy.
