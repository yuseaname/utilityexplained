# Mason Sourcing Debt Map — Full-Site Extraction

**Date:** 2026-08-27
**Extractor:** Mason (swarm builder)
**Scope:** All 97 blog articles — claim-level inventory of unsourced claims, stale sources, zero-source prescriptions, and price-density risk.

---

## 1. UNSOURCED CLAIMS BY FILE (Worst 25 Pages by Claim Density)

### 1.1 Zero-Source Pages (19 total) — Full Claim Inventory

#### 07-gas-bill-too-high.md (3606 words, src=0, 28 $ranges, 44 %)

| Claim | Text excerpt | Impact | Recommended source |
|-------|------------|--------|-------------------|
| Space heating share | "Space heating accounts for about 40–50% of household gas use" | Core fact — drives article premise | EIA Residential Energy Consumption Survey (RECS) 2020 data table HC1.1 |
| Winter bill multiplier | "driving winter bills 2–3× higher than summer" | Reader trust | EIA Short-Term Energy Outlook or utility-specific winter/summer comparison |
| Thermostat savings rate | "Every degree above 68°F increases heating energy use by roughly 3–5%" | Central savings claim | U.S. DOE Energy Saver Guide (energy.gov/energysaver/thermostats) |
| Thermostat savings $ | "Lowering thermostat 1–2°F saves $15–$40/month" | Savings math | U.S. DOE estimate or utility-specific rate calculator |
| Furnace efficiency degradation | "Furnace rated at 92% AFUE may drop to 80–85% after 10–15 years without proper maintenance" | Equipment purchase driver | ACCA (Air Conditioning Contractors of America) manual or DOE furnace maintenance guide |
| Pre-2000 furnace AFUE | "Pre-2000 furnaces commonly sit at 70–80% AFUE" | Age comparison | DOE minimum efficiency standards historical table |
| New furnace AFUE | "A new high-efficiency condensing furnace reaches 95% AFUE" | Product claim | ENERGY STAR Most Efficient criteria (energystar.gov) |
| Water heating share | "Water heating is typically the second-largest gas expense (15–25% of gas usage)" | Core fact | EIA RECS 2020 — water heating energy consumption |
| Water heater temp savings | "Lowering to 120°F saves 4–22% on water heating costs" | Savings claim | U.S. DOE energy.gov/energysaver/water-heating — actual range is 4-9% per 10°F |
| Tank heater efficiency | "Standard tank water heaters are 58–65% efficient" | Product comparison | ENERGY STAR water heater specs or DOE Appliance Standards |
| Tankless efficiency | "A tankless condensing model can be 95–98% efficient" | Product comparison | ENERGY STAR tankless water heater criteria |
| Rate increase claim | "In late 2025 and into 2026, many U.S. utilities have increased rates 15–30% year-over-year (U.S. EIA, 2026)" | Topical claim | EIA Natural Gas Monthly or state PUC rate case filings — **not found at EIA URL** |
| Heating share 60-70% | "Heating accounts for 60–70% of natural gas usage" | Contradicts 40-50% earlier | EIA RECS 2020 — reconcile internally |
| Cold weather impact | "A month that's 5°F colder on average can increase gas usage by 15–25%" | Weather correlation | NOAA HDD data + utility case study |
| Cost/savings table | All 8 rows of $ savings table | Core savings claims | ENERGY STAR savings calculator or DOE data |
| Average bill range | "The average US household gas bill ranges from $40–$80/month in summer to $100–$250/month in winter" | National benchmark | EIA 2023/2024 Residential Energy Consumption data |
| Pool heater cost | "Gas pool heater adds $50–$150/month" | Specific cost | Pool industry association or utility rate calculator |

#### 30-sudden-spike-in-electricity-bill-no-usage.md (3543 words, src=0, 11 $ranges, 24 %)

| Claim | Impact | Recommended source |
|-------|--------|-------------------|
| Dirty filter increases HVAC work 15-30% | Diagnostic guide | U.S. DOE filter maintenance page |
| Refrigerant leak increases consumption 30-50% | Diagnostic guide | ACCA refrigerant guide |
| Duct leak loses 20-30% of conditioned air | Diagnostic guide | ENERGY STAR duct sealing |
| Emergency heat increases costs 200-300% | Cost warning | Heat pump manufacturer specs or DOE |
| Second fridge 100-200 kWh/month | Appliance cost | ENERGY STAR fridge calculator |
| Water heater failure 300-500 kWh/month extra | Diagnostic guide | Water heater manufacturer specs |
| Pool pump 24/7 wastes 300-500 kWh/month | Appliance cost | DOE pump efficiency standards |
| EV charging 250-500 kWh/month | Appliance cost | DOE EV charger calculator |

#### 2026-utility-cost-index-by-state.md (2946 words, src=0, 484 $ singles, 86 %)

**ALL 50 state rankings, electric/gas/water costs, YoY changes, and utility burden stats are ORIGINAL RESEARCH with no verifiable source citations.** The methodology section lists data sources ("EIA State Energy Data System 2025, state utility commission rate filings 2025–2026, AWWA water rate surveys 2025, EPA WaterSense data 2025") but no individual figures are linked or footnoted.

**TOP 3 MOST LOAD-BEARING UNSOURCED CLAIMS:**
1. "Hawaii has the highest electricity costs at $0.34/kWh (avg. $450/month)" — This is the article's headline claim. Source: EIA Electric Power Monthly Table 5.6.A (latest available) or state PUC rate filings. **The $450/month figure is also mathematically inconsistent with 900 kWh × $0.34/kWh = $306, not $450.**
2. "The national average electricity rate is $0.16/kWh" — Source: EIA Electric Power Monthly.
3. "National average: $262/month" — Source: EIA RECS or calculated from EIA data. Inconsistent with the $430-500 claim on average-utility-bills-by-state-2026.md.

#### average-utility-bills-by-state-2026.md (3085 words, src=0, 13 $ranges, 25 %)

**TOP 3 MOST LOAD-BEARING UNSOURCED CLAIMS:**
1. "The average U.S. household pays $430–$500 per month for all utilities combined" — **Directly contradicts** the $262/month figure from the 2026-utility-cost-index. One of these is wrong by 64-91%. This is a sitewide credibility risk.
2. National average electricity rate 14.3¢/kWh, up from 13.2¢ in 2025 — Source: EIA Electric Power Monthly (needs specific table reference).
3. "Pennsylvania (+8.2% total utility cost), Florida (+7.6%), and Texas (+6.9%) had the largest year-over-year increases" — Source: state PUC rate case decisions or EIA data.

#### can-utility-shut-off-service.md (2774 words, src=0, 2 tables)

**TOP 3 MOST LOAD-BEARING UNSOURCED CLAIMS:**
1. "Most states require a written notice (commonly 10–15 days)" — Source: National Consumer Law Center utility shutoff survey or state-specific PUC rules. Legal claim needs citation.
2. "Many states restrict electric and gas shutoffs during winter months" — Source: NCLC winter shutoff protections map. Legal claim needs citation.
3. "Medical certification pauses disconnection for 30 days" — Source: State PUC medical certification rules. Legal claim needs citation.

#### ac-running-but-not-cooling.md (2452 words, src=0)
- Clogged filter 15-30% harder — DOE source
- Refrigerant leak 30-50% — ACCA source
- Duct leaks 20-30% — ENERGY STAR source

#### aux-heat-vs-emergency-heat-meaning.md (1504 words, src=0)
- Backup heat cost comparison — DOE heat pump vs resistance heat cost table
- Emergency heat 200-300% increase — Manufacturer specs or DOE

#### stormwater-fee-on-water-bill-explained.md (3189 words, src=0)
- "Average stormwater fee $12 billed quarterly" — cites Rainplan but no URL
- Raleigh $8.22/SFEU — City of Raleigh stormwater utility page
- Fort Worth $3.4M revenue — City of Fort Worth FY26 budget
- All city-specific fee data — needs municipal source per city

#### water-service-charge-explained.md (1443 words, src=0)
- All water service charge averages — AWWA Rate Survey 2025 or EPA WaterSense

#### tiered-water-rates-explained.md (3335 words, src=0)
- All tiered rate examples — AWWA survey or city-specific rate sheets

#### mcf-vs-ccf-vs-therms-on-gas-bill.md (3152 words, src=0)
- Gas pricing examples — EIA Natural Gas Monthly

#### gas-delivery-charge-vs-supply-charge.md (3244 words, src=0)
- All cost breakdowns — utility tariff sheets or EIA data

#### heat-pump-running-all-day-in-winter.md (924 words, src=0)
- "Normal below 30°F" — heat pump manufacturer specs

#### how-to-read-gas-meter.md (3579 words, src=0)
- Conversion factors — acceptable as general knowledge
- Pricing examples — EIA data

#### moving-utilities-checklist.md (2177 words, src=0)
- Deposit amounts, timing — utility tariff sheets

#### why-is-my-water-bill-higher-in-summer.md (1230 words, src=0)
- All usage increase percentages — EPA WaterSense or AWWA data

#### why-your-electric-bill-keeps-rising-2026.md (2766 words, src=0, 10 cents/kWh, 31 %)
- "Electric rates rose 15-30% across many states" — claims EIA but no hyperlink
- All state-by-state increase data — EIA Electric Power Monthly
- "Grid infrastructure $5-15/month" — utility commission rate case filings

#### how-to-lower-electric-bill-complete-guide.md (3122 words, src=0, 66 $ranges, 58 %)
- "Heating/cooling 40-50%" — EIA RECS (alt text claims EIA but no link)
- "Every degree saves 3-6%" — DOE
- "886-908 kWh/month, $115-180/month" — EIA (no link)
- "Phantom loads 5-10%" — EIA (no link)
- All savings math — unsourced
- All product box claims — unsourced

### 1.2 Remaining Pages — Significant Unsourced Claims (Skim)

#### how-utility-rates-fees-usage-work-together.md (785 words, src=1)
- Single source, most rate/usage claims unsourced

#### supply-vs-delivery-charges-electricity.md (755 words, src=2)
- Two sources, but delivery vs supply breakdown ratios are unsourced

#### why-electric-bill-changes-month-to-month.md (726 words, src=1)
- Single source, most seasonal patterns unsourced

#### why-is-my-water-bill-higher-in-winter.md (805 words, src=2)
- Two sources, but increase percentages unsourced

---

## 2. STALE SOURCES (Older than 2024, No Current-Year Counterpoint)

### Pages with staleY>0 and currentY=0 (8 pages — need source refresh)

| Page | staleY | CurrentY | Stale Reference | Suggested Refresh |
|------|--------|----------|----------------|-------------------|
| 01-how-to-read-your-electric-bill.md | 1 | 0 | EIA 2022 data: 10,791 kWh annual avg | EIA 2024/2025 data (Table 5.6.A) |
| 03-why-is-my-electric-bill-so-high.md | 2 | 0 | Pre-2023 rate/usage data | EIA 2024/2025 or state PUC rate filings |
| 11-understanding-kwh-usage.md | 2 | 0 | Pre-2023 kWh benchmarks | EIA RECS 2024 or latest available |
| 12-how-to-read-your-gas-bill.md | 1 | 0 | Pre-2024 gas pricing | EIA Natural Gas Monthly 2025/2026 |
| 18-fuel-adjustment-charge.md | 1 | 0 | Pre-2024 fuel adjustment data | State PUC fuel adjustment tariff sheets |
| 43-understand-natural-gas-bill-charges.md | 1 | 0 | Pre-2024 gas charge data | EIA Natural Gas Monthly 2025/2026 |
| gas-customer-charge-explained.md | 1 | 0 | Pre-2024 customer charge average | State PUC tariff sheets |
| is-your-toilet-running-leak-test.md | 1 | 0 | Pre-2024 water leak cost data | EPA WaterSense 2025 data |

### Pages with staleY>0 but currentY>0 (2 pages — partially refreshed)

| Page | staleY | CurrentY | Status |
|------|--------|----------|--------|
| electric-bill-breakdown-understanding-line-items.md | 3 | 3 | Balanced — 3 stale refs, 3 current |
| why-your-electric-bill-keeps-rising-2026.md | 1 | 53 | Balanced — 53 current refs outweigh 1 stale |

---

## 3. ZERO-SOURCE PAGE PRESCRIPTIONS (19 pages)

For each of the 19 zero-source pages, the 3 most load-bearing claims and the authoritative source that would cover it.

| Page | Claim #1 & Source | Claim #2 & Source | Claim #3 & Source |
|------|-------------------|-------------------|-------------------|
| **07-gas-bill-too-high.md** | "Space heating 40-50%" → **EIA RECS 2020 Table HC1.1** (space heating energy consumption) | "Every degree saves 3-5%" → **U.S. DOE Energy Saver Guide** (thermostat savings) | "Rate increase 15-30% YoY" → **EIA Natural Gas Monthly** or **state PUC rate case filings** |
| **30-sudden-spike.md** | "Dirty filter 15-30% harder" → **U.S. DOE filter maintenance** | "Duct leak 20-30%" → **ENERGY STAR duct sealing** | "Emergency heat 200-300% increase" → **DOE heat pump vs resistance heat** |
| **2026-utility-cost-index.md** | "Hawaii $0.34/kWh" → **EIA Electric Power Monthly Table 5.6.A** | "National avg $0.16/kWh" → **EIA Electric Power Monthly** | "$262/month national avg" → **EIA RECS 2024 or calculated from EIA data** |
| **avg-utility-bills-by-state.md** | "$430-500/month total" → **EIA RECS 2024** (conflicts with other page) | "14.3¢/kWh" → **EIA Electric Power Monthly** | "PA +8.2%, FL +7.6%, TX +6.9%" → **State PUC rate case decisions** |
| **can-utility-shut-off.md** | "10-15 day notice" → **NCLC Utility Shutoff Survey** | "Winter moratoria" → **NCLC winter protection map** | "Medical 30-day pause" → **State PUC medical certification rules** |
| **ac-running-but-not-cooling.md** | "Filter 15-30% harder" → **DOE** | "Refrigerant 30-50%" → **ACCA** | "Duct 20-30%" → **ENERGY STAR** |
| **aux-heat-vs-emergency.md** | "Backup heat cost" → **DOE heat pump comparison** | "Emergency heat 200-300%" → **DOE** | |
| **stormwater-fee.md** | "$12 avg quarterly" → **Rainplan national survey** (need URL) | "Raleigh $8.22" → **City of Raleigh stormwater utility page** | "Fort Worth $3.4M" → **City of Fort Worth FY26 budget** |
| **water-service-charge.md** | All water charges → **AWWA 2025 Rate Survey** | | |
| **tiered-water-rates.md** | All tier examples → **AWWA Rate Survey 2025** | | |
| **mcf-vs-ccf-vs-therms.md** | Gas pricing → **EIA Natural Gas Monthly** | | |
| **gas-delivery-vs-supply.md** | Cost breakdowns → **Utility tariff sheets** or **EIA** | | |
| **heat-pump-running-all-day.md** | "Normal below 30°F" → **Heat pump manufacturer specs** | | |
| **how-to-read-gas-meter.md** | Pricing → **EIA** | | |
| **moving-utilities-checklist.md** | Deposits → **Utility tariff sheets** | | |
| **why-water-bill-higher-summer.md** | Usage % → **EPA WaterSense** | | |
| **why-electric-bill-keeps-rising.md** | "Rates rose 15-30%" → **EIA Electric Power Monthly** | "Grid costs $5-15" → **State PUC rate cases** | |
| **how-to-lower-electric-bill-complete-guide.md** | "HVAC 40-50%" → **EIA RECS 2024** | "Every degree 3-6%" → **DOE** | "886-908 kWh" → **EIA** |

---

## 4. DOLLAR-FIGURE INVENTORY

### Price Density by Page (dollar-range counts, descending)

| Page | $ Ranges | $ Singles | Cents/kWh | %s | Stale-Price Risk |
|------|----------|-----------|-----------|-----|------------------|
| how-to-lower-electric-bill-complete-guide.md | 66 | 183 | 3 | 58 | **HIGH** — all savings claims unsourced; rates change with utility costs |
| 02-average-utility-costs-2026.md | 48 | 299 | 1 | 15 | **HIGH** — all cost data unsourced; 2026 figures stale by 2027 |
| 07-gas-bill-too-high.md | 28 | 76 | 0 | 44 | **HIGH** — savings math, cost ranges, rate claims all unsourced |
| average-utility-bills-by-state-2026.md | 13 | 126 | 1 | 25 | **HIGH** — all state costs unsourced; conflicts with index page |
| 30-sudden-spike-in-electricity-bill-no-usage.md | 11 | 27 | 2 | 24 | **MODERATE** — waste estimates, some arithmetic acceptable |
| 2026-utility-cost-index-by-state.md | 5 | 484 | 12 | 86 | **HIGH** — 484 single dollar figures, all unsourced original research |
| 7-states-with-worst-utility-spikes-2026.md | 4 | 31 | 8 | 72 | **MODERATE** — has 3 sources but many rate claims unsourced |
| why-your-electric-bill-keeps-rising-2026.md | 4 | 20 | 10 | 31 | **HIGH** — zero-source page with many rate claims |
| gas-vs-electric-heating-cost-comparison.md | 1 | 6 | 0 | 2 | LOW |
| how-to-budget-for-utilities-first-apartment.md | 1 | 2 | 0 | 0 | LOW |

### Top 10 Most Price-Dense Pages (Total $ figures)
| Page | Total $ mentions | Source status | Risk |
|------|-----------------|---------------|------|
| 2026-utility-cost-index-by-state.md | 489 | 0 sources | CRITICAL — all figures unverifiable |
| 02-average-utility-costs-2026.md | 347 | 1 source | HIGH — single source inadequate |
| how-to-lower-electric-bill-complete-guide.md | 249 | 0 sources | HIGH — all savings claims unverifiable |
| average-utility-bills-by-state-2026.md | 139 | 0 sources | HIGH — 13 range + 126 single figures |
| 07-gas-bill-too-high.md | 104 | 0 sources | HIGH — 28 range + 76 single figures |
| 7-states-with-worst-utility-spikes-2026.md | 35 | 3 sources | MODERATE |
| 30-sudden-spike-in-electricity-bill-no-usage.md | 38 | 0 sources | MODERATE |
| why-your-electric-bill-keeps-rising-2026.md | 24 | 0 sources | HIGH |

---

## 5. ENVELOPE: TOP 10 MOST-UNSOURCED LOAD-BEARING CLAIMS SITEWIDE

Ranked by credibility risk if the claim is wrong:

| # | Claim | Page | Why Load-Bearing | Recommended Fix |
|---|-------|------|-----------------|-----------------|
| 1 | "The average U.S. household pays $430–$500 per month for all utilities combined" | average-utility-bills-by-state-2026.md | Contradicts site's own $262 figure from index page; 64-91% discrepancy destroys credibility | Reconcile with EIA RECS 2024; cite EIA table; update both pages |
| 2 | "Hawaii has the highest electricity costs at $0.34/kWh (avg. $450/month)" | 2026-utility-cost-index-by-state.md | Headline claim; $450 not consistent with 900 kWh × $0.34 = $306; math error erodes trust | Verify: 900 × $0.34 = $306, not $450. Fix numbers, cite EIA Electric Power Monthly Table 5.6.A |
| 3 | "In late 2025 and into 2026, many U.S. utilities have increased rates 15–30% year-over-year (U.S. EIA, 2026)" | 07-gas-bill-too-high.md | Claims EIA but no hyperlink; 15-30% is a precise range that demands verification | Cite EIA Natural Gas Monthly specific table or state PUC annual rate case filings |
| 4 | "Every degree you adjust your thermostat saves 3–6% on heating/cooling costs" | how-to-lower-electric-bill-complete-guide.md | Appears on multiple pages; central savings claim for the site's core advice | Cite U.S. DOE Energy Saver Guide (energy.gov/energysaver/thermostats) |
| 5 | "Heating and cooling drive 40–50% of home energy costs" | how-to-lower-electric-bill-complete-guide.md | Appears on 5+ pages; foundational claim | Cite EIA RECS 2020 Table HC1.1 |
| 6 | "National average electricity rate is $0.16/kWh" | 2026-utility-cost-index-by-state.md | Baseline for all state comparisons | Cite EIA Electric Power Monthly Table 5.6.A (latest available month) |
| 7 | "14.3¢ per kWh, up from 13.2¢ in 2025" | average-utility-bills-by-state-2026.md | National benchmark; 8.3% increase claim | Cite EIA Electric Power Monthly; verify 2025 baseline |
| 8 | "Most states require a written notice (commonly 10–15 days)" before shutoff | can-utility-shut-off-service.md | Legal claim; if wrong, readers could miss deadlines | Cite NCLC Utility Shutoff Survey or state-specific PUC rules |
| 9 | "Electric rates rose 15-30% across many states in 2025-2026" | why-your-electric-bill-keeps-rising-2026.md | Topical claim driving article premise | Cite EIA or state PUC rate case filings with specific state examples |
| 10 | ALL 50 state rankings in the utility cost index | 2026-utility-cost-index-by-state.md | 484 unsourced dollar figures; central data product for the site | Add footnoted citations per row or table; mark as "estimated based on methodology" |

---

## 6. SITE-LEVEL FINDINGS

1. **Data consistency failure:** Two pages (2026-utility-cost-index-by-state and average-utility-bills-by-state-2026) give contradictory national averages ($262 vs $430-500). This is a sitewide credibility crisis. One or both are wrong.

2. **19 of 97 pages (20%) have zero outbound sources.** These account for the majority of unsourced factual claims. The 6 worst (by claim density × page length) are: 07-gas-bill-too-high, 30-sudden-spike, 2026-utility-cost-index, average-utility-bills-by-state, can-utility-shut-off, and how-to-lower-electric-bill-complete-guide.

3. **8 pages have stale references with no current-year counterpoint.** These are concentrated in the bill-reading series (01, 11, 12, 18, 43, gas-customer-charge) — the very pages where accurate rate data is most critical.

4. **The 2026-utility-cost-index-by-state page is marked as draft:true** — it should not be published until sources are added and the Hawaii $450 discrepancy is fixed.

5. **The how-to-lower-electric-bill-complete-guide page has 66 dollar ranges and 183 single dollar figures with zero sources.** This is the most price-dense page on the site and the most vulnerable to stale-price claims.

6. **Existing remediation queue** (data/content-remediation-queue.json) has 6 P2 'missing_sources' items — all should be escalated to P1 given the scope of the problem.

---
*Mason, 2026-08-27. Artifact: SQ-045/mason-sourcing-debt-map.md*
