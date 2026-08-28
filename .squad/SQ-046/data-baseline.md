# SQ-046 Canonical Data Baseline — Commander-verified 2026-08-28

Every number below was fetched from its named source this session. Seats cite THESE;
corrections go through the Commander. Never silently estimate.

## Electricity (national, residential)

| Figure | Value | Source (retrieved 2026-08-27/28) |
|---|---|---|
| Avg monthly bill | **$159.14** (mid-2026 report); $142.26 (FY2024) | EIA Electricity Monthly Update — https://www.eia.gov/electricity/monthly/update/end-use.php |
| Avg price | **18.34–18.44¢/kWh** (mid-2026); 17.30¢ (FY2025) | same + EIA Electric Power Monthly Table (avg price by end-use sector) |
| Avg monthly usage | **~899 kWh/mo** (10,791 kWh/yr basis) | EIA FAQ — https://www.eia.gov/tools/faqs/faq.php?id=97&t=3 |

## Energy shares & savings (DOE / energy.gov, verified via Home Upgrades page)

| Figure | Value | Source |
|---|---|---|
| Thermostat setback | 7–10°F for 8h/day → **up to 10%** savings | https://www.energy.gov/save/home-upgrades |
| Heating share | **~30% of utility bills** (energy.gov framing) | same |
| Water heating | ~20% of utility bills | same |
| Duct losses | 20–30% | same |
| Windows | 25–30% of heating/cooling energy | same |

⚠️ The site currently says "heating and cooling 40–50%" (EIA RECS site-energy basis).
METRIC CONFLICT — do not mix: either cite RECS "share of home energy USE (~40-50%)" or
energy.gov "share of utility BILLS (~30% heating)". Pick one, label the metric.
Verify RECS figure at https://www.eia.gov/consumption/residential/ if used.

## Products (manufacturer-published; already live on site)

- Nest Learning 4th gen (B0D5BBYRJM): Google-published ~12% heating / ~15% cooling savings.
- Kill A Watt P4400 (B00009MDBU): 0.2% accuracy, 120V/15A, UL (P3 spec).
- GoveeLife Upgraded Smart Water Leak Detector 1s, 5-pack + gateway (B0DQLFC3Q6): SMS/app/email alerts, 105 dB, IP67, 5-yr battery (Amazon listing, retrieved 2026-08-28).
- Moen Flo 900-001 (B00C03D01Q): flow/pressure/temperature monitoring, drops-per-minute detection, automatic shutoff (Moen spec).
- Emporia L2 EV Charger 48A J1772 (B09ZNN3JB7): 240V, up to 46 mi/hr, WiFi scheduling (Emporia spec).
- ecobee Smart Thermostat Premium (B09XXS48P8): smart sensors, air quality monitoring — VERIFY multi-stage/heat-pump compatibility claims against ecobee's current spec before citing.

## Hawaii (for the draft state-page fix)

Hawaii has the nation's HIGHEST rates but LOWEST household usage (~500–550 kWh/mo,
no space heating) — monthly bills land ~$200–240, NOT $450. Verify current figures
via EIA Electric Sales, Revenue & Average Price Table 5a (https://www.eia.gov/electricity/sales_revenue_price/)
before writing; cite the table. rate × usage MUST reconcile on every row.
