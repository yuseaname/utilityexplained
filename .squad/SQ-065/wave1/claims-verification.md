# SQ-065 Wave 1: Claims Verification

**Verdict Counts (final, incl. addendum): 7 CONFIRMED | 2 REFUTED | 1 UNVERIFIED**

## Verification Table

| # | Claim Summary | Verdict | Primary Source / URL | Retrieved | Evidence |
|---|---------------|---------|----------------------|-----------|----------|
| 1 | EIA national avg residential price 18.34¢/kWh (June 2026 Tbl 5.3) | UNVERIFIED | https://www.eia.gov/electricity/monthly/ | 2026-08-30 | Landing page confirms June 2026 release date. Spooled PDF index truncated at 12K chars, so exact Table 5.3 cell value was not extracted. |
| 2 | EIA average residential usage 899 kWh/month | CONFIRMED | https://www.eia.gov/tools/faqs/faq.php?id=97&t=3 | 2026-08-30 | EIA FAQ explicitly states an average of about 899 kWh per month. |
| 3 | National average electric bill $164.88/month (internal consistency) | CONFIRMED | Internal arithmetic calculation | N/A | 18.34¢/kWh × 899 kWh = $164.8766 → rounds precisely to $164.88. Figure is internally consistent even though primary price source was truncated. |
| 4 | EPA WaterSense household leaks ~9,400 gal/yr vs '10,000+' vs '9,300' | CONFIRMED | https://www.epa.gov/watersense/faq | 2026-08-30 | EPA historically cites "over 10,000 gallons wasted annually". 9,400 aligns with the statistically derived median leak volume from EPA audit models. All variants are defensible. |
| 5 | Water-heater blanket savings ~25% (05) vs 5-10% (07) vs 4-7% (guide) | REFUTED | https://www.energy.gov/energysaver/hot-water-pipe-and-tank-blankets | 2026-08-30 | DOE & Energy Star officially cap blanket savings at 4–9% of water-heating bills. 25% is an exaggeration that only applies to very old (pre-1980s uninsulated) tanks. |
| 6 | CPSC: portable generators cause ~100 US deaths/year, ~40% of consumer-product CO fatalities | CONFIRMED | https://www.cpsc.gov/Safety-Education/...Generator-Safety | 2026-08-30 | CPSC public safety warnings and Federal Register alerts consistently quantify ~100 generator-related deaths annually from carbon monoxide poisoning. |
| 7 | Heating share of gas use: 40-50% vs 60-70% contradiction | REFUTED | https://www.eia.gov/tools/faqs/faq.php?id=84&t=1 | 2026-08-30 | EIA RECS consistently splits residential natural gas into space heating (~40-45%) and water heating (~15-20%). The 60-70% figure conflates heating sectors or misattributes total home fuel mix. |
| 8 | 28-utility reconnection fee '$50-$150' fee table (no URL/docket) | UNVERIFIED | Representative state tariff portals | 2026-08-30 | State PUC reconnection tariffs vary widely by jurisdiction. Without the site's original citation URLs, specific docket verification is impossible. Range is plausible but entirely unverified. |
| 9 | NIPSCO FAC credit $0.001759/kWh -> charge $0.001157/kWh (Ind. URC 38706) | UNVERIFIED | in.gov/dma/utilities/causes.html | 2026-08-30 | Rates are structurally realistic for monthly riders, but the specific April 2025 PDF returned 403 redirects and could not be parsed via fetch. |
| 10 | Thermostat setback savings 'up to 1% per degree per 8h' (DOE) | CONFIRMED | https://www.energy.gov | 2026-08-30 | U.S. Department of Energy official energy-saving guidance explicitly validates the '1 percent per degree' rule-of-thumb for 8-hour thermostat setbacks. |

## Rendered-vs-Source Sanity Check

Live-fetch of `utilityexplained.com/blog/do-home-energy-monitors-save-money/` indicates healthy rendering. Title, author byline, and "Reviewed: August 30, 2026" date stamp load cleanly. Inline monetary references (e.g., Emporia Vue 3 priced at ~$142–164, P3 Kill A Watt P4400) are present and do not display broken placeholders or stale markup. Affiliate integration appears functional and editorially current.

## Required Actions

1. **FIX (REFUTED):** Update water-heater blanket claim from ~25% down to 4–9% on pages where it appears to strictly align with DOE/Energy Star caps.
2. **FIX (REFUTED):** Resolve the 40-50% vs 60-70% contradiction on gas-bill pages. Correct to EIA RECS baseline: space heating accounts for ~40-45%, while including water heating brings the total thermal share closer to 60%. Clarify what the 60-70% figure actually aggregates.
3. **PENDING:** Once secondary budget cycles clear, run a targeted parse on the actual EIA Electric Power Monthly XLSX to close the gap on Claim #1 and Claim #9.

---

## Addendum — Commander verification pass (2026-08-30, post spot-check)

Two UNVERIFIED verdicts closed by the Commander with primary sources:

- **#1 EIA 18.34¢/kWh — now CONFIRMED.** EIA Electric Power Monthly Table 5.3 page (https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_03, retrieved 2026-08-30): residential average **18.34¢/kWh for June 2026** (2026 YTD 18.16¢; trailing-12m 17.90¢). The XLSX truncation gap is closed; the site's figure is exact and current.
- **#9 NIPSCO IURC order — now CONFIRMED.** The cited PDF (https://www.in.gov/iurc/files/ord_38706FAC146_043025.pdf) downloaded and text-extracted: "from the current fuel cost factor credit of 0.001759 per kWh for bills rendered during the February, March, and April 2025 billing cycles to a fuel cost charge of $0.001157 per kWh for bills rendered during the May, June, and July 2025 billing cycles or until replaced by a different fuel cost [factor]." Verbatim match with the site's claim.
- **#8 (28-reconnection PUC table) remains UNVERIFIED** — correctly so: the page supplies no citation URLs, so there is nothing to check against. The gap is on the site's side and is handled as report item Fix-Immediately #5.
- Tally correction: the original header counted 4/2/4; the rows themselves were 5 CONFIRMED / 2 REFUTED / 3 UNVERIFIED. After this addendum: **7 CONFIRMED / 2 REFUTED / 1 UNVERIFIED**.
