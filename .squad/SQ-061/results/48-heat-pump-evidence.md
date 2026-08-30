# SQ-061 Evidence Packet — Heat Pump vs Gas Furnace (post 48)

Research date: 2026-08-29. Every number below carries its source URL. Items that could not be confirmed are marked **UNVERIFIED**.

---

## 1. Efficiency ratings (verified)

### Heat pumps: SEER2 / HSPF2, 2023 DOE minimums (nationwide, heat pumps are not regionally split)
- Split-system heat pump minimums since Jan 1, 2023: **14.3 SEER2** (≈15 SEER) and **7.5 HSPF2** (≈8.8 HSPF). Single-package: 13.4 SEER2 / 6.7 HSPF2. Source: AHRI, https://www.ahrinet.org/2023-energy-efficiency-standards
- Context on the metric change (SEER/HSPF → SEER2/HSPF2 test procedure, 2023): same AHRI page.
- DOE background on heat pumps (how they move heat; types): https://www.energy.gov/heat-pumps (already cited on page).

### Furnaces: AFUE
- Federal minimum for gas furnaces: **80% AFUE**. Source: DOE FEMP, https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-furnaces
- ENERGY STAR certified gas furnaces: **≥95% AFUE in the U.S. South, ≥97% AFUE in the U.S. North** (verified directly on the criteria page): https://www.energystar.gov/products/furnaces/key_product_criteria
- Market tiers for the page: 80% (minimum, non-condensing) / 90-96% (condensing; Trane's pricing guide prices an 80% and a 96% tier — see §5) / 97-98% (premium; exact max AFUE of current top models **UNVERIFIED** this session — do not print a specific "98.7%" figure without a manufacturer spec sheet).

## 2. Cold-climate heat pumps (verified)

- **NEEP cold-climate ASHP specification + product list exists** (ccASHP list; covers IECC climate zone 4 and colder): https://neep.org/heating-electrification/ccashp-specification-product-list
- NEEP ccASHP spec requirements: AHRI-matched system, ENERGY STAR certified, **COP ≥ 1.75 at 5°F at max capacity**. Source: NEEP spec PDF, https://neep.org/sites/default/files/resources/NEEP%2520cold%2520climate%2520Air-Source%2520Heat%2520Pump%2520Specification.pdf
- Capacity retention at 5°F: listed units commonly retain ~70-100% of nominal capacity (list reports 5°F capacity/COP per model). The "≥70% at 5°F" criterion figure appears in secondary summaries (e.g., BetterBuiltNW, https://betterbuiltnw.com/resources/neep-cold-climate-air-source-heat-pump-list); treat 70% as a common benchmark, and use the NEEP list itself as the per-model source.
- Low-temp operation, manufacturer source: Mitsubishi Comfort (official) states the Deluxe H2i plus system "provides unparalleled performance at **100 percent capacity in outdoor temperatures as low as -5°F**": https://www.mitsubishicomfort.com/articles/introducing-deluxe-wall-mounted-h2i-plus-system
- Mitsubishi Electric Canada (official) states H2i/Zuba operates at 100% heating capacity at -15°C (5°F), FS model at -20°C (-4°F), FX at -23°C (-9.4°F): https://www.mitsubishielectric.ca/hvac/home-owners/zuba
- **UNVERIFIED:** "-13°F guaranteed operation" (widely repeated for Mitsubishi H2i but not confirmed on a manufacturer page this session) and any "-22°F rated" unit (no manufacturer source found). Do not print either without a spec-sheet citation.

## 3. Operating-cost method: ¢/kWh vs $/therm (core of the page)

### Formula (unit math, derivable and checkable)
Useful heat cost per MMBtu:
- Heat pump: **$ = 293.08 × (¢/kWh ÷ 100) ÷ COP**
- Furnace: **$ = 10 × ($/therm) ÷ AFUE**

Breakeven — heat pump is cheaper when:

  **(¢/kWh) ÷ ($/therm) < 3.41 × COP ÷ AFUE**

Conversion notes: 1 MMBtu = 293.08 kWh; 1 MMBtu = 10 therms; EIA residential gas is quoted $/Mcf — 1 Mcf ≈ 10.3-10.4 therms (≈1.036 MMBtu at ~1,036 Btu/cf). COP 2.5-3.5 seasonal is an illustrative assumption band: HSPF2 7.5 minimum ≈ seasonal COP ~2.2; strong cold-climate units land ~2.5-3+ (label as assumption, not an EIA/DOE fact).

### Current EIA inputs (exact, with months)
- **Electricity: US residential average 18.34 ¢/kWh, June 2026** (latest month; table released 8/26/2026). Recent: Jan 17.45 / Feb 17.65 / Mar 18.56 / Apr 18.83 / May 18.44 / Jun 18.34. Source: EIA Electric Power Monthly Table 5.3, https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_03
- **Natural gas: US residential average $19.83/Mcf, May 2026** (release 7/31/2026) ≈ **$1.92/therm** at 10.34 therms/Mcf. Winter months: Dec 2025 $14.09 (~$1.36/th), Jan 2026 $13.96 (~$1.35/th), Feb 2026 $15.06 (~$1.46/th). Source: EIA, https://www.eia.gov/dnav/ng/ng_pri_sum_a_EPG0_PRS_DMcf_m.htm — note residential $/Mcf runs HIGHER in the off-season (fixed costs over low volumes), so use winter-month data for heating math.

### Worked example — heating-season prices (Jan 2026: 17.45 ¢/kWh, ~$1.35/therm; ratio = 12.9)
- vs **96% AFUE** furnace: HP needs seasonal COP > 3.6 to win → **furnace wins clearly** at national-average prices (useful heat ≈ $14.1/MMBtu furnace vs $17.0 at COP 3).
- vs **80% AFUE** furnace: HP needs COP > 3.0 → near tie; a strong cold-climate unit roughly matches an 80% furnace.

### Worked example — May 2026 prices (18.34 ¢/kWh, ~$1.92/therm; ratio = 9.6)
- vs 95% AFUE: HP wins if COP > 2.67 → typical mid/high-efficiency HP (COP 2.7-3.0) **wins**; COP 2.5 loses.
- vs 80% AFUE: HP wins if COP > 2.24 → **HP wins** for nearly everything modern.

### When each wins (honest framing)
- Cheap-gas regions (Midwest/South, ratio typically >12): gas furnace wins on fuel cost vs 95%+ AFUE — consistent with AGA's claim that the least-efficient gas furnace beats the most-efficient HP in 36 states (advocacy source; attribute: https://www.aga.org/natural-gas-or-a-heat-pump-where-you-live-matters/).
- HP wins where electricity is cheap relative to gas (Pacific Northwest, some Southeast co-ops), and vs propane, oil, or electric resistance (always).
- The decision is the local ratio, not the equipment — that's the page's core message and it survives.

## 4. EIA Winter Fuels Outlook (latest full edition: published Oct 15, 2025, winter 2025-26)

Source: https://www.eia.gov/outlooks/steo/report/winterfuels.php (next edition due Oct 2026)
- Forecast winter heating expenditures (US avg): **natural gas $642 (-1% vs prior winter), electricity $1,133 (+4%), heating oil $1,390 (-8%), propane $1,210 (-9%)**.
- **Natural gas is the main heating fuel in 46% of US homes.**
- Electricity (incl. heat pumps) was the only fuel forecast MORE expensive; rising electricity prices offset HP efficiency gains.
- Regional: NE electric-heat homes forecast to spend the most ($1,520); Midwest electric-heat $1,280; Midwest gas-heat ~$610 (+2%).
- Winter 2025-26 US avg residential electricity ~24 ¢/kWh in the Northeast case; winter US avg residential gas ~$13.50/Mcf (both from same page).
- Later update noting colder weather raised estimates: https://www.eia.gov/todayinenergy/detail.php?id=66864

## 5. Installed cost ranges (manufacturer-official)

Trane official pricing guide (national averages, equipment + labor, pre-incentive): https://www.trane.com/residential/en/pricing/pricing-guide/
- Heat pump (standard, ducted tiers): **$7,369-$15,608**
- **Cold-climate heat pump: $7,983-$17,012**
- Gas furnace **80% AFUE: $5,093-$6,386**; **96% AFUE: $6,630-$8,390**
- Dual-fuel: Trane confirms the configuration (HP + gas furnace) but publishes **no dollar range** — present dual-fuel as "roughly heat-pump tier + furnace tier minus the AC you no longer need" reasoning, not a fake single range.

Carrier official 2026 guide: heat pump installed **$6,000-$25,000** (geothermal/high-efficiency at top): https://www.carrier.com/us/en/residential/hvac-resources/heat-pumps/how-much-does-a-heat-pump-cost/

## 6. Incentives — 25C status (CRITICAL CORRECTION)

- **The 25C Energy Efficient Home Improvement Credit is DEAD for 2026 installations.** Under the One Big Beautiful Bill Act (Public Law 119-21, July 4, 2025), the credit is **not allowed for property placed in service after December 31, 2025**. Official: IRS FAQ on modification of 25C/25D/etc., https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb
- What it was (for historical accuracy): 30% of cost, up to **$2,000/yr for heat pumps** ($1,200 cap for most other items), no lifetime limit, 2023-2025. Source: IRS, https://www.irs.gov/credits-deductions/energy-efficient-home-improvement-credit
- 25D (solar/geothermal, incl. HP-config relevance) also terminated after Dec 31, 2025 (same IRS FAQ).
- Still alive in 2026: **state HEAR/Home Energy Rebates where still state-administered (up to $8,000 heat pump rebate, income-capped)** — https://www.energy.gov/save/home-upgrades (program availability varies by state; some states returned funds — treat any specific state claim as needing its own verification) — plus **utility rebates** (name generically; e.g., Efficiency Maine's comparator exists: https://www.efficiencymaine.com/at-home/heating-cost-comparison/).

**Page correction required:** the current post cites the ENERGY STAR tax-credit definitions page in a way that could read as current; the expansion must state plainly that the federal 25C credit ended 12/31/2025 and only utility/state programs remain.

## 7. Product fit verdict

- **Nest Learning Thermostat 4th gen (B0D5BBYRJM) — HONEST FIT.** Official compatibility: works with most 24V systems including gas forced air and heat pumps; 4th gen supports heat pump systems with aux/backup heat and up to 2 cool / 3 heat stages; dual-fuel supported (pro wiring). Sources: https://support.google.com/googlehome/answer/9246656?hl=en and https://support.google.com/googlehome/answer/9230098?hl=en — ASIN already verified in site inventory (AFFILIATE-PLACEMENTS-2026-08-28.md). Placement angle: it's the one box that controls BOTH systems and the dual-fuel switchover — directly serves the page's "set your balance point" logic. Also pairs with the site's smart-thermostat content.
- **Emporia Vue 3 (B0C7B1LKDW) — PARTIAL FIT; frame narrowly or omit.** It is an electrical-panel monitor (16 circuit CTs): it can verify a heat pump's kWh and aux-heat stripping on the electric side, but it **cannot see gas consumption** — the furnace side of the comparison is invisible to it. Honest copy: "use it after installing a heat pump to watch what the compressor actually draws," never "compare your gas vs electric heating costs." If the page stays decision-focused (math + contractor scope), NO box is the more honest choice; if it adds a "verify after install" section, the Nest is the primary box and the Vue 3 a conditional secondary.
- No alternative ASIN proposed — the existing pair covers the honest angles; a different product would add fabrication risk, not value.

## 8. Competitor scan

Query "heat pump vs gas furnace savings" — top organic themes:
1. **Reddit r/heatpumps threads** (rank heavily): real-user bill comparisons; consensus "depends on your rates; gas often cheaper in cold/cheap-gas states" — no structured method. https://www.reddit.com/r/heatpumps/comments/12t8w47/
2. **AGA "where you live matters"** (gas industry): least-efficient furnace beats most-efficient HP in 36 states — advocacy framing, no DIY math. https://www.aga.org/natural-gas-or-a-heat-pump-where-you-live-matters/
3. **Rewiring America HP savings page**: ~$370/yr average US household savings claim (electrification-advocacy model), no breakeven formula. https://homes.rewiringamerica.org/articles/heating-and-cooling/heat-pump-savings
Also common: AC Direct's 2026 comparison (~$8,500/10-yr moderate-climate claim, cites dead 25C credit as if live — freshness gap we can beat).

Query "heat pump vs furnace cost calculator":
1. **UniColorado switchover calculator**: dual-fuel outdoor-temperature crossover tool ($/therm, ¢/kWh inputs; example at $1.10/th, $0.140/kWh). https://unicolorado.com/tools/switchover-calculator/
2. **Efficiency Maine heating-cost comparator** (state program, trusted, Maine-specific prices). https://www.efficiencymaine.com/at-home/heating-cost-comparison/
3. **EPRI Residential Space Heating Cost Comparison Calculator** (research-grade lifecycle + emissions). https://apps.epri.com/ResidentialSpaceHeatingCalculator/

Gap to exploit: no top result combines (a) the breakeven ratio formula, (b) current-month EIA numbers, (c) post-OBBBA incentive truth, (d) NEEP cold-climate context. All four verified here.

## 9. UNVERIFIED / do-not-print list

- "-22°F rated" heat pumps (no manufacturer source found).
- Mitsubishi "-13°F guaranteed operation" (secondary sources only; use the official -5°F @100% claim instead).
- Exact max AFUE of current furnaces ("98.7%").
- Any specific state's HEAR rebate availability in Aug 2026.
- "≥70% capacity at 5°F" as a NEEP criterion number (verify against the current spec PDF revision before stating as a threshold; the verified hard threshold is COP ≥ 1.75 @ 5°F).
