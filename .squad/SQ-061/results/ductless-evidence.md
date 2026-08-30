# Evidence Packet: Ductless Mini-Split vs Central Air (SQ-061)

Target: `content/blog/ductless-mini-split-vs-central-air.md` (expansion 571 → 1,200–1,600 words)
Date: 2026-08-29. All items verified against live sources unless marked UNVERIFIED.

## 1. Efficiency — SEER2 ranges (federal minimums, ENERGY STAR, product data)

**2023 DOE minimums — VERIFIED (eCFR, 10 CFR 430.32(c)):**
https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-C/section-430.32
- Central AC split systems, manufactured on/after Jan 1, 2023: **SEER2 ≥ 13.4** nationwide (manufacture standard).
- Southeast/Southwest **installation** standards: split AC <45,000 Btu/h **SEER2 ≥ 14.3**; Southwest also **EER2 ≥ 11.7** (<45k) / **9.8** (≥45k). Southeast ≥45k Btu/h: SEER2 ≥ 13.8.
- Split-system heat pumps (incl. mini-split heat pumps): **SEER2 ≥ 14.3 / HSPF2 ≥ 7.5** nationwide.
- IMPORTANT CORRECTION: "15.2 SEER2" is NOT a DOE minimum. 15.2 is the ENERGY STAR level (below). The DOE minimum for central AC in the North is 13.4 SEER2. Regional definitions: Southeast = AL, AR, DE, FL, GA, KY, LA, MD, MS, NC, OK, SC, TN, TX, VA, DC; Southwest = AZ, CA, NV, NM.

**ENERGY STAR criteria — VERIFIED (ENERGY STAR Key Product Criteria):**
https://www.energystar.gov/products/air_source_heat_pumps/key-product-criteria
- Split-system heat pumps (all): **≥ 15.2 SEER2 / ≥ 7.8 HSPF2 / ≥ 11.0 EER2**.
- Cold-climate tier, non-ducted (mini-split) split: **≥ 8.5 HSPF2 / ≥ 15.2 SEER2**; ducted split: ≥ 8.1 HSPF2 / ≥ 15.2 SEER2.
- Cold-climate low-ambient: **COP at 5°F ≥ 1.75** and **≥ 70% of heating capacity at 5°F vs 47°F** (per Appendix M1/H42), plus controls verification procedure.
- NEEP ccASHP spec mirrors these (COP@5°F > 1.75, 70% capacity retention; product list sortable by SEER2/COP): https://neep.org/heating-electrification/ccashp-specification-product-list

**Actual product ceiling — VERIFIED (ENERGY STAR certified-product dataset, data.energystar.gov):**
https://data.energystar.gov/resource/w7cv-9xjt.json (queried 2026-08-29)
- Max certified SEER2, ductless ("HP - Mini or Multi Split"): **35.1** (Carrier 37M/45M, Bryant 37M/615, Midea/Payne D5M, MDV MSEP all 35.1; Mitsubishi M-Series 35.0).
- Max certified SEER2, ducted split heat pumps ("HP - Split System"): **25.0**.
- Same-dataset, apples-to-apples: the certified ductless ceiling is ~10 SEER2 points above the ducted split ceiling. Central AC-only claim "top out around 26 SEER2" is a Carrier (manufacturer) statement: https://www.carrier.com/us/en/residential/hvac-resources/ductless-mini-splits/mini-split-vs-central-air/ — label as manufacturer claim if used.

**Where the real-world gap comes from — VERIFIED (ENERGY STAR Duct Sealing):**
https://www.energystar.gov/saveathome/heating-cooling/duct-sealing
- Exact quote: "In a typical house, however, about **20 to 30 percent** of the air that moves through the duct system is lost due to leaks, holes, and poorly connected ducts." Result: "higher utility bills" and rooms hard to keep comfortable.
- Benefits page: "Leaky ducts can reduce heating and cooling system efficiency by as much as **20 percent**." https://www.energystar.gov/saveathome/heating-cooling/duct-sealing/benefits
- Framing for the page: SEER2 is equipment-only; ductless delivers rated efficiency at the head, ducted systems lose 20–30% of moved air before it reaches rooms, so field efficiency < nameplate.

## 2. Duct leakage cost implication

- ENERGY STAR Ductless page: typical household energy bill ≈ **$1,900/yr, nearly half for heating and cooling** (~$950): https://www.energystar.gov/products/ductless_heating_cooling
- Chain (defensible, no fabrication): ~half of $1,900 is HVAC; duct leakage of 20–30% of airflow can cut system efficiency up to 20% → order-of-magnitude $100–$200+/yr waste in a typical home. Present as arithmetic on ENERGY STAR figures, not as an ENERGY STAR dollar quote.
- EIA context — VERIFIED: **88% of U.S. households used AC in 2020** (RECS 2020): https://www.eia.gov/todayinenergy/detail.php?id=52558 ; AC ≈ **19% of residential electricity (254 billion kWh, 2020)**: https://www.eia.gov/tools/faqs/faq.php?id=1174&t=1 (headline from EIA FAQ; treat % as EIA-sourced).

## 3. Zoning and part-load

- VERIFIED (Mass Save blog, utility program): ductless mini-splits enable "cooling only occupied rooms," with programmable timers, sleep modes, and **variable-speed compressors**; central AC "depends on well-sealed ducts" and loses energy through leaks: https://www.masssave.com/blog/residential/mini-splits-vs-central-ac-which-cooling-system-is-right-for-your-home
- VERIFIED (ENERGY STAR ductless page): certified mini-splits use **up to 60% less energy than standard home electric radiators**; sizing must use a **Manual J** load calc; both over- and under-sized systems underperform: https://www.energystar.gov/products/ductless_heating_cooling
- VERIFIED (energy.gov article): modern air-source heat pumps "can reduce your electricity use by 50%" (vs electric-resistance heating): https://www.energy.gov/articles/pump-your-savings-heat-pumps
- Mechanism for the page: inverter-driven mini-splits ramp compressor speed to match load (capacity modulation), vs single-stage central systems that cycle full-on/full-off; zoning saves when heads serve rooms used on different schedules — savings are NOT automatic when the whole house is conditioned all day. (Mechanism framing consistent with Mass Save/ENERGY STAR language above; avoid inventing % savings.)

## 4. Installed costs (label each; government/utility preferred)

| Item | Figure | Source & status |
|---|---|---|
| Whole-home ASHP (multi-zone, MA program data) | **$22,000 avg installed** (2022 program data); $2,650/ton rebate up to $8,500; income-qualified up to $16,000/no-cost; net ~$13,500 std, ~$6,000 enhanced | VERIFIED: https://www.masssave.com/residential/rebates-offers-services/heating-and-cooling/heat-pumps/air-source-heat-pumps |
| ASHP equipment + install range "$4,000–$12,000" (NYSERDA) | **UNVERIFIED** — appears only in a NYSERDA social post snippet; current program page states no range: https://www.nyserda.ny.gov/All-Programs/Heat-Pump-Program | Do not use without finding the live NYSERDA page. |
| Adding ductwork to a ductless home | "up to **$18,000**" on top of AC price | Manufacturer claim (Carrier), same URL as above — label as such. |
| Central AC install | **$3,900–$7,900** (attributed to Angi) | This Old House citing Angi: https://www.thisoldhouse.com/heating-cooling/how-to-choose-an-air-conditioner — marketplace data, not .gov. |
| Single-zone mini-split installed | ~$2,000–$5,500; multi-zone stacks ~$4,000+/zone | Industry/marketplace aggregators (FilterBuy, Budget Heating) — **UNVERIFIED by .gov/utility**; if used, attribute to national marketplace data or omit. |
| Federal incentive | **30% up to $2,000 tax credit**, ENERGY STAR-certified ASHP installed 2023–2032 | VERIFIED: https://www.energystar.gov/products/ductless_heating_cooling (and /about/federal-tax-credits/air-source-heat-pumps) |

Recommended pattern for the page: keep the draft's "no universal price" stance, cite Mass Save's $22k average as the one hard program-data number, use $2,000 credit, and present per-zone stacking qualitatively.

## 5. Decision framework (sourced)

- Existing ducts in good condition → central replacement usually cheaper; no ducts → mini-split avoids the duct premium (Carrier decision guide + Mass Save, both outlined below).
- Additions/garage conversions, historic homes, uneven rooms → mini-split heads avoid duct redesign or unit upsizing (Carrier dealer guidance).
- Rentals/sparse occupancy → per-room zoning + cooling only occupied rooms (Mass Save).
- Cold-climate heating displacement: mini-split as PRIMARY heat is defensible only with ENERGY STAR cold-climate / NEEP-listed equipment (COP@5°F ≥ 1.75, ≥70% capacity at 5°F — verified above). AC-only comparison is the wrong frame in heating climates.
- Mass Save tools: heating comparison calculator + no-cost Home Energy Assessment before deciding; HEAT Loan 0% financing; note Mass Save gives **no central-AC-replacement rebate** (mini-split HPs only) — a real programmatic nudge worth mirroring generically ("many utilities rebate heat pumps, not AC swaps").

## 6. Maintenance / honest downsides

- Filter cadence — VERIFIED (NB Power, utility): check/clean indoor-head filters **monthly** (rinse, dry fully): https://www.nbpower.com/en/save-energy/tips/heating-and-cooling/heat-pump-maintenance/ ; cleaning how-to: https://www.efficiencyvermont.com/blog/how-to/how-to-clean-and-maintain-your-ductless-heat-pump-system
- Outdoor unit: keep clear of snow/leaves/debris; ~2 ft clearance is industry guidance (FilterBuy) — **UNVERIFIED as .gov**, phrase as "keep clearance per manufacturer."
- Refrigerant line aesthetics + 3-in wall penetration: Carrier page (manufacturer, verified outline).
- Max line lengths vary by manufacturer and are a column in the NEEP ccASHP product list (cite the list; don't quote a universal number). Specific per-brand lengths (e.g., Mitsubishi) — UNVERIFIED here.
- Per-room head cost stacking + weaker whole-home filtration: Carrier (manufacturer) cons list.

## 7. Amazon product-fit verdict

**Verdict: NO new product box. Keep the two already-wired products, with thermostat placement care.**
- This is a $4k–$22k system-purchase decision researched over weeks; no accessory converts. A mini-split filter pack or cover would be off-intent (brand/model-specific, wrong affiliate context at decision stage).
- Existing smart thermostat (B0D5BBYRJM) is central-systems-relevant only — if used, caption it explicitly as "for the central-air path" so it doesn't mislead mini-split readers (mini-split heads have own controls; thermostat integration is brand-dependent).
- Energy monitor (B0C7B1LKDW) is the only honest add: it lets readers measure HVAC circuit draw before/after — directly supports the "verify your own duct losses / nameplate vs field efficiency" story at circuit level. One contextual mention max; no new box.

## 8. Competitor scan — "ductless mini split vs central air cost"

1. **Carrier — "Mini Split vs Central Air"** (manufacturer): defines both, pros/cons lists, decision guide with dealer quotes; numbers: ductless up to 35 SEER2 vs central ~26 SEER2, ductwork "up to $18,000," 3-inch line hole. Weakness: sells both but tilts editorial to ductless premium tiers; no duct-loss % or program data.
2. **Mass Save blog — "Mini-Splits vs. Central AC"** (utility): comparison table (efficiency/install/cost/maintenance), decision factors, rebates/HEAT Loan, calculator + assessment CTA. No dollar figures; strong trust signals. This is the closest model to our evidence-gated stance.
3. **This Old House — "How to Choose an Air Conditioner"**: not head-to-head; BTU/sq-ft sizing rules (20 BTU/sq ft; 1 ton per 500–600 sq ft), oversizing warning, central AC $3,900–$7,900 (Angi), monthly filter checks. Gap we can own: nobody pairs the verified 13.4/14.3 minimums + 20–30% duct loss + same-dataset 35.1-vs-25.0 ceiling contrast with a "verify at the circuit" tool.

## 9. Corrections for the current draft

- Draft's "no defensible universal installed-price figure" stance can stand but should now cite Mass Save's $22,000 program average and the $2,000 tax credit rather than refusing all numbers.
- Add the missing hard facts: 20–30% ENERGY STAR duct-loss figure; 13.4/14.3 SEER2 DOE minimums; ENERGY STAR cold-climate COP@5°F ≥ 1.75; 35.1 vs 25.0 certified SEER2 ceiling contrast.
- Do NOT use 15.2 SEER2 as a "DOE minimum" (common error — it's ENERGY STAR). Do NOT use NYSERDA $4k–$12k (unverified on live page). Do NOT claim universal max line length.
