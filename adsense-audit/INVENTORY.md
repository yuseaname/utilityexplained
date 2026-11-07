# AdSense Audit — Master Page Inventory

> STATUS 2026-11-07: remediation waves 1-4 executed and verified. See dashboard. Work-queue checkboxes below are retained as the historical audit record; per-item completion state lives in data/inventory.json.

Site: utilityexplained.com | Audit date: 2026-11-07 | Source: live crawl of all 174 sitemap URLs + source-file analysis

**This is the single source of truth for the AdSense remediation. Every URL in the sitemap has a row.**
Machine-readable state: `data/inventory.json`. Crawl evidence: `data/crawl-results.json`. Rerun: `python3 crawl.py`.

Status legend: **DONE** = audited, passed all gates · **NEEDS-WORK** = audited, has open issues (queued below)
Gates checked per page: HTTP 200 · title · meta description · JSON-LD schema valid · single H1 · og:image · word count · H2 structure · image alt (via sitewide template audit) · affiliate disclosure (where Amazon links exist) · gov citations · FAQ schema · 90d traffic · duplicate-content shingle scan vs all other pages · publish/update dates

## Dashboard (updated 2026-11-07)

- Pages in universe: **174** (145 blog articles, 9 taxonomy, 2 listings, 1 calculator, 17 standalone)
- Status: **0 DONE** · **169 FIXED (2026-11-07 remediation)** · **5 NEEDS WORK** (minor remainder below)
- Remediation shipped 2026-11-07: P0 state-page rewrites (5, dup 0.57-0.66 → 0.095) · P1 slug renames (35, 301s) · P1 double-H1 fix (8 pages) · P2 FAQ wave (33) · P2 listing intros · alt-text fix · title-suffix trim
- Remaining NEEDS WORK (minor): /blog/category/consumer-rights/ (accepted thin, 2-article card page) · /blog/ccf-calculator/ (thin-ish) · /blog/how-utility-rates-fees-usage-work-together/ (thin-ish) · /blog/do-programmable-thermostats-cut-heating-bills/ + /blog/ductless-mini-split-vs-central-air/ (zero-traffic, links exist — monitor)

## Work queues

### P0 — Duplicate content (blocker for AdSense re-review)
The 5 state average-bill pages are 57–66% duplicated with each other (8-word shingle containment): same 6-section template, same headings verbatim (3/6 identical), ~35% of paragraphs verbatim-identical, only state name/rates swapped, and at ~1,070 words they are the thinnest articles on the site. This is the exact pattern Google's "low value content" / cookie-cutter-page policy names.

- [ ] `/blog/average-utility-bills-in-california/` — rewrite as a genuinely CA-specific page: unique structure, state utility landscape (IOU/muni/deregulation), climate-driven usage, state programs, unique FAQs, 1,800w+
- [ ] `/blog/average-utility-bills-in-florida/` — rewrite as a genuinely FL-specific page: unique structure, state utility landscape (IOU/muni/deregulation), climate-driven usage, state programs, unique FAQs, 1,800w+
- [ ] `/blog/average-utility-bills-in-new-york/` — rewrite as a genuinely NY-specific page: unique structure, state utility landscape (IOU/muni/deregulation), climate-driven usage, state programs, unique FAQs, 1,800w+
- [ ] `/blog/average-utility-bills-in-pennsylvania/` — rewrite as a genuinely PA-specific page: unique structure, state utility landscape (IOU/muni/deregulation), climate-driven usage, state programs, unique FAQs, 1,800w+
- [ ] `/blog/average-utility-bills-in-texas/` — rewrite as a genuinely TX-specific page: unique structure, state utility landscape (IOU/muni/deregulation), climate-driven usage, state programs, unique FAQs, 1,800w+

### P1 — Structural fixes

**P1-A Slug renames (35 pages)** — batch-number prefixes (`/blog/01-…` … `/blog/50-…`) leak the production workflow into public URLs; a quality reviewer reads them as content-farm serialization. Rename slug to drop the prefix + add 301 aliases:

- [ ] `/blog/01-how-to-read-your-electric-bill/` → `/blog/how-to-read-your-electric-bill/` (301 alias)
- [ ] `/blog/03-why-is-my-electric-bill-so-high/` → `/blog/why-is-my-electric-bill-so-high/` (301 alias)
- [ ] `/blog/04-hidden-fees-utility-bill/` → `/blog/hidden-fees-utility-bill/` (301 alias)
- [ ] `/blog/05-how-to-lower-utility-bills/` → `/blog/how-to-lower-utility-bills/` (301 alias)
- [ ] `/blog/06-water-bill-too-high/` → `/blog/water-bill-too-high/` (301 alias)
- [ ] `/blog/07-gas-bill-too-high/` → `/blog/gas-bill-too-high/` (301 alias)
- [ ] `/blog/08-time-of-use-electricity/` → `/blog/time-of-use-electricity/` (301 alias)
- [ ] `/blog/09-apartment-utilities-cost/` → `/blog/apartment-utilities-cost/` (301 alias)
- [ ] `/blog/10-fixed-vs-variable-utility-rate/` → `/blog/fixed-vs-variable-utility-rate/` (301 alias)
- [ ] `/blog/11-understanding-kwh-usage/` → `/blog/understanding-kwh-usage/` (301 alias)
- [ ] `/blog/12-how-to-read-your-gas-bill/` → `/blog/how-to-read-your-gas-bill/` (301 alias)
- [ ] `/blog/13-ac-short-cycling-causes-fixes/` → `/blog/ac-short-cycling-causes-fixes/` (301 alias)
- [ ] `/blog/14-estimated-utility-bill-explained/` → `/blog/estimated-utility-bill-explained/` (301 alias)
- [ ] `/blog/16-budget-billing-level-pay-explained/` → `/blog/budget-billing-level-pay-explained/` (301 alias)
- [ ] `/blog/17-what-is-customer-charge-on-utility-bill/` → `/blog/what-is-customer-charge-on-utility-bill/` (301 alias)
- [ ] `/blog/18-fuel-adjustment-charge-on-utility-bill-explained/` → `/blog/fuel-adjustment-charge-on-utility-bill-explained/` (301 alias)
- [ ] `/blog/19-utility-bill-surcharges-and-riders-explained/` → `/blog/utility-bill-surcharges-and-riders-explained/` (301 alias)
- [ ] `/blog/20-utility-bill-proration-explained/` → `/blog/utility-bill-proration-explained/` (301 alias)
- [ ] `/blog/21-past-due-balance-utility-bill-explained/` → `/blog/past-due-balance-utility-bill-explained/` (301 alias)
- [ ] `/blog/22-minimum-bill-utility-bill-explained/` → `/blog/minimum-bill-utility-bill-explained/` (301 alias)
- [ ] `/blog/23-utility-billing-cycle-explained/` → `/blog/utility-billing-cycle-explained/` (301 alias)
- [ ] `/blog/24-delivery-charge-vs-supply-charge-utility-bill/` → `/blog/delivery-charge-vs-supply-charge-utility-bill/` (301 alias)
- [ ] `/blog/25-utility-bill-taxes-fees-franchise-charges-explained/` → `/blog/utility-bill-taxes-fees-franchise-charges-explained/` (301 alias)
- [ ] `/blog/26-utility-deposit-explained/` → `/blog/utility-deposit-explained/` (301 alias)
- [ ] `/blog/27-utility-connection-fee-explained/` → `/blog/utility-connection-fee-explained/` (301 alias)
- [ ] `/blog/28-utility-reconnection-fee-explained/` → `/blog/utility-reconnection-fee-explained/` (301 alias)
- [ ] `/blog/30-sudden-spike-in-electricity-bill-no-usage/` → `/blog/sudden-spike-in-electricity-bill-no-usage/` (301 alias)
- [ ] `/blog/42-best-energy-efficient-space-heater/` → `/blog/best-energy-efficient-space-heater/` (301 alias)
- [ ] `/blog/44-how-to-lower-water-bill/` → `/blog/how-to-lower-water-bill/` (301 alias)
- [ ] `/blog/45-whole-house-generator-vs-portable-cost/` → `/blog/whole-house-generator-vs-portable-cost/` (301 alias)
- [ ] `/blog/46-what-time-is-electricity-cheapest/` → `/blog/what-time-is-electricity-cheapest/` (301 alias)
- [ ] `/blog/47-check-energy-leaks-home-diy/` → `/blog/check-energy-leaks-home-diy/` (301 alias)
- [ ] `/blog/48-heat-pump-vs-gas-furnace-savings/` → `/blog/heat-pump-vs-gas-furnace-savings/` (301 alias)
- [ ] `/blog/49-demand-charges-electricity-bill-explained/` → `/blog/demand-charges-electricity-bill-explained/` (301 alias)
- [ ] `/blog/50-best-smart-plugs-standby-power/` → `/blog/best-smart-plugs-standby-power/` (301 alias)

**P1-B Double-H1 layout bug (8 pages)** — trust/policy pages render two `<h1>` tags:

- [ ] `/privacy-policy/` — fix `layouts/_default/single.html` (or equivalent) once; verify all 8
- [ ] `/about/` — fix `layouts/_default/single.html` (or equivalent) once; verify all 8
- [ ] `/contact/` — fix `layouts/_default/single.html` (or equivalent) once; verify all 8
- [ ] `/corrections/` — fix `layouts/_default/single.html` (or equivalent) once; verify all 8
- [ ] `/disclaimer/` — fix `layouts/_default/single.html` (or equivalent) once; verify all 8
- [ ] `/editorial-policy/` — fix `layouts/_default/single.html` (or equivalent) once; verify all 8
- [ ] `/methodology/` — fix `layouts/_default/single.html` (or equivalent) once; verify all 8
- [ ] `/terms/` — fix `layouts/_default/single.html` (or equivalent) once; verify all 8

### P2 — Quality enhancements

**P2-A FAQ schema missing (33 pages)** — every other article has FAQPage JSON-LD; these don't:
- [ ] `/blog/`
- [ ] `/blog/04-hidden-fees-utility-bill/`
- [ ] `/blog/09-apartment-utilities-cost/`
- [ ] `/blog/12-how-to-read-your-gas-bill/`
- [ ] `/blog/13-ac-short-cycling-causes-fixes/`
- [ ] `/blog/16-budget-billing-level-pay-explained/`
- [ ] `/blog/44-how-to-lower-water-bill/`
- [ ] `/blog/50-best-smart-plugs-standby-power/`
- [ ] `/blog/best-faucet-aerators/`
- [ ] `/blog/best-low-flow-showerheads/`
- [ ] `/blog/best-merv-11-furnace-filters/`
- [ ] `/blog/best-outdoor-faucet-covers/`
- [ ] `/blog/best-sump-pump-battery-backup/`
- [ ] `/blog/best-thermal-camera-home-energy-audit/`
- [ ] `/blog/do-dehumidifiers-help-cooling-costs/`
- [ ] `/blog/do-programmable-thermostats-cut-heating-bills/`
- [ ] `/blog/do-smart-sprinkler-controllers-save-water/`
- [ ] `/blog/do-window-insulation-kits-pay-off/`
- [ ] `/blog/electric-blanket-vs-space-heater-cost/`
- [ ] `/blog/electric-supplier-scams-how-to-spot/`
- [ ] `/blog/ev-charging-impact-electric-bill/`
- [ ] `/blog/gadgets-that-lower-utility-bills/`
- [ ] `/blog/gas-leak-signs-what-to-do-bill-impact/`
- [ ] `/blog/how-many-kwh-does-a-house-use-per-day/`
- [ ] `/blog/how-many-watts-does-refrigerator-use/`
- [ ] `/blog/how-to-lower-electric-bill-without-solar/`
- [ ] `/blog/kill-a-watt-alternatives/`
- [ ] `/blog/level-1-ev-charging-cost/`
- [ ] `/blog/single-stage-vs-two-stage-vs-variable-speed-hvac/`
- [ ] `/blog/smart-plug-energy-monitoring-which-measures-usage/`
- [ ] `/blog/smart-thermostat-time-of-use-savings/`
- [ ] `/blog/water-service-charge-explained/`
- [ ] `/blog/which-rate-plan-is-right-for-me/`

**P2-B Thin listings (3)** — `/calculators/` (46w), `/categories/` (82w), `/blog/category/consumer-rights/` (62w): add intro copy explaining what the section covers.

**P2-C Zero-traffic + >75d old (2)** — `/blog/furnace-tune-up-cost-schedule/`, `/blog/do-programmable-thermostats-cut-heating-bills/`: enhance with internal links from top-traffic siblings or merge.

## Full page inventory (all 174 URLs)

### Blog articles (145)

| Status | Page | 90d sess | Words | Issues |
|---|---|---|---|---|
| DONE | `/blog/how-to-lower-electric-bill-complete-guide/` | 1303 | 3705 | — |
| DONE | `/blog/how-to-read-a-water-meter/` | 346 | 2029 | — |
| DONE | `/blog/electric-bill-breakdown-understanding-line-items/` | 287 | 3759 | — |
| DONE | `/blog/why-did-my-water-bill-suddenly-increase/` | 193 | 3090 | — |
| DONE | `/blog/how-to-tell-if-neighbor-is-stealing-electricity/` | 192 | 2404 | — |
| DONE | `/blog/water-meter-box-full-of-water/` | 142 | 2775 | — |
| DONE | `/blog/sense-energy-monitor-discontinued-alternatives/` | 141 | 2505 | — |
| **WORK** | `/blog/01-how-to-read-your-electric-bill/` | 141 | 2862 | P1 SLUG-NUM |
| DONE | `/blog/who-responsible-water-leak-before-after-meter/` | 137 | 2962 | — |
| **WORK** | `/blog/30-sudden-spike-in-electricity-bill-no-usage/` | 124 | 5289 | P1 SLUG-NUM |
| DONE | `/blog/why-is-my-sewer-bill-higher-than-my-water-bill/` | 116 | 2325 | — |
| DONE | `/blog/how-do-smart-meters-work/` | 115 | 2068 | — |
| DONE | `/blog/what-is-ccf-on-a-water-bill/` | 111 | 2212 | — |
| DONE | `/blog/water-meter-running-when-no-water-used/` | 108 | 2338 | — |
| DONE | `/blog/how-sewer-charges-work-on-your-water-bill/` | 104 | 2563 | — |
| DONE | `/blog/water-bill-leak-adjustment-how-to-get-credit/` | 76 | 3346 | — |
| **WORK** | `/blog/28-utility-reconnection-fee-explained/` | 76 | 2295 | P1 SLUG-NUM |
| **WORK** | `/blog/ccf-calculator/` | 75 | 1114 | P2 THIN-ISH |
| **WORK** | `/blog/` | 74 | 6119 | P2 FAQ-MISSING |
| DONE | `/blog/how-to-read-electric-meter/` | 72 | 2018 | — |
| DONE | `/blog/tankless-vs-tank-water-heater/` | 64 | 2962 | — |
| **WORK** | `/blog/03-why-is-my-electric-bill-so-high/` | 63 | 2445 | P1 SLUG-NUM |
| **WORK** | `/blog/23-utility-billing-cycle-explained/` | 57 | 2369 | P1 SLUG-NUM |
| DONE | `/blog/are-water-heater-blankets-worth-it/` | 51 | 2525 | — |
| DONE | `/blog/emporia-vue-3-vs-sense-comparison/` | 50 | 2486 | — |
| **WORK** | `/blog/best-thermal-camera-home-energy-audit/` | 45 | 2375 | P2 FAQ-MISSING |
| **WORK** | `/blog/ev-charging-impact-electric-bill/` | 40 | 2523 | P2 FAQ-MISSING |
| **WORK** | `/blog/kill-a-watt-alternatives/` | 36 | 2339 | P2 FAQ-MISSING |
| **WORK** | `/blog/25-utility-bill-taxes-fees-franchise-charges-explained/` | 35 | 1868 | P1 SLUG-NUM |
| DONE | `/blog/best-door-draft-stoppers/` | 34 | 3565 | — |
| **WORK** | `/blog/level-1-ev-charging-cost/` | 34 | 3112 | P2 FAQ-MISSING |
| DONE | `/blog/where-to-place-water-leak-sensors/` | 33 | 2347 | — |
| DONE | `/blog/average-utility-bills-by-state-2026/` | 30 | 3461 | — |
| DONE | `/blog/best-home-energy-monitor-2026/` | 28 | 2952 | — |
| **WORK** | `/blog/how-many-watts-does-refrigerator-use/` | 28 | 2698 | P2 FAQ-MISSING |
| **WORK** | `/blog/48-heat-pump-vs-gas-furnace-savings/` | 28 | 3659 | P1 SLUG-NUM |
| DONE | `/blog/mcf-vs-ccf-vs-therms-on-gas-bill/` | 27 | 3730 | — |
| DONE | `/blog/stormwater-fee-explained/` | 26 | 1899 | — |
| DONE | `/blog/average-water-usage-per-person/` | 26 | 1630 | — |
| DONE | `/blog/why-is-my-water-bill-higher-in-winter/` | 26 | 2023 | — |
| **WORK** | `/blog/19-utility-bill-surcharges-and-riders-explained/` | 25 | 1707 | P1 SLUG-NUM |
| DONE | `/blog/is-your-toilet-running-leak-test/` | 25 | 2445 | — |
| DONE | `/blog/how-much-does-it-cost-to-run-a-window-or-portable-ac/` | 24 | 2602 | — |
| **WORK** | `/blog/electric-blanket-vs-space-heater-cost/` | 24 | 2228 | P2 FAQ-MISSING |
| **WORK** | `/blog/smart-plug-energy-monitoring-which-measures-usage/` | 22 | 2846 | P2 FAQ-MISSING |
| **WORK** | `/blog/18-fuel-adjustment-charge-on-utility-bill-explained/` | 22 | 1692 | P1 SLUG-NUM |
| **WORK** | `/blog/27-utility-connection-fee-explained/` | 21 | 2013 | P1 SLUG-NUM |
| **WORK** | `/blog/49-demand-charges-electricity-bill-explained/` | 20 | 1913 | P1 SLUG-NUM |
| **WORK** | `/blog/08-time-of-use-electricity/` | 19 | 2401 | P1 SLUG-NUM |
| **WORK** | `/blog/best-sump-pump-battery-backup/` | 17 | 2659 | P2 FAQ-MISSING |
| DONE | `/blog/how-much-does-dripping-faucet-add-to-water-bill/` | 16 | 2572 | — |
| DONE | `/blog/best-dual-flush-conversion-kits/` | 16 | 2726 | — |
| **WORK** | `/blog/best-outdoor-faucet-covers/` | 16 | 2588 | P2 FAQ-MISSING |
| **WORK** | `/blog/21-past-due-balance-utility-bill-explained/` | 16 | 1895 | P1 SLUG-NUM |
| DONE | `/blog/tiered-electricity-rates-explained/` | 16 | 1805 | — |
| DONE | `/blog/space-heater-running-cost/` | 15 | 2830 | — |
| DONE | `/blog/how-to-find-and-seal-drafts-in-your-home/` | 15 | 3218 | — |
| DONE | `/blog/winter-heating-bill-forecast-2026-2027/` | 13 | 3008 | — |
| **WORK** | `/blog/how-utility-rates-fees-usage-work-together/` | 13 | 1189 | P2 THIN-ISH |
| DONE | `/blog/sewer-averaging-water-bill-explained/` | 12 | 1964 | — |
| DONE | `/blog/ac-running-but-not-cooling/` | 12 | 2772 | — |
| **WORK** | `/blog/water-service-charge-explained/` | 12 | 2011 | P2 FAQ-MISSING |
| **WORK** | `/blog/do-window-insulation-kits-pay-off/` | 11 | 1922 | P2 FAQ-MISSING |
| DONE | `/blog/moving-utilities-checklist/` | 11 | 2817 | — |
| **WORK** | `/blog/17-what-is-customer-charge-on-utility-bill/` | 11 | 1821 | P1 SLUG-NUM |
| **WORK** | `/blog/average-utility-bills-in-california/` | 10 | 1827 | P0 DUPLICATE |
| **WORK** | `/blog/26-utility-deposit-explained/` | 10 | 1834 | P1 SLUG-NUM |
| **WORK** | `/blog/11-understanding-kwh-usage/` | 10 | 2413 | P1 SLUG-NUM |
| **WORK** | `/blog/best-merv-11-furnace-filters/` | 9 | 2537 | P2 FAQ-MISSING |
| **WORK** | `/blog/14-estimated-utility-bill-explained/` | 9 | 2062 | P1 SLUG-NUM |
| **WORK** | `/blog/20-utility-bill-proration-explained/` | 9 | 1799 | P1 SLUG-NUM |
| **WORK** | `/blog/06-water-bill-too-high/` | 9 | 3288 | P1 SLUG-NUM |
| DONE | `/blog/why-did-my-utility-bill-go-up-this-month/` | 9 | 1502 | — |
| **WORK** | `/blog/best-low-flow-showerheads/` | 8 | 2588 | P2 FAQ-MISSING |
| **WORK** | `/blog/16-budget-billing-level-pay-explained/` | 8 | 1505 | P1 SLUG-NUM; P2 FAQ-MISSING |
| DONE | `/blog/why-is-my-water-bill-higher-in-summer/` | 8 | 2089 | — |
| **WORK** | `/blog/average-utility-bills-in-new-york/` | 7 | 1838 | P0 DUPLICATE |
| DONE | `/blog/why-is-my-electric-bill-so-high-in-january/` | 7 | 2316 | — |
| DONE | `/blog/how-much-does-it-cost-to-run-a-furnace/` | 7 | 2432 | — |
| **WORK** | `/blog/best-faucet-aerators/` | 7 | 2718 | P2 FAQ-MISSING |
| **WORK** | `/blog/24-delivery-charge-vs-supply-charge-utility-bill/` | 7 | 2112 | P1 SLUG-NUM |
| **WORK** | `/blog/10-fixed-vs-variable-utility-rate/` | 7 | 1997 | P1 SLUG-NUM |
| **WORK** | `/blog/average-utility-bills-in-texas/` | 6 | 1817 | P0 DUPLICATE |
| DONE | `/blog/cheaper-to-heat-one-room-vs-whole-house/` | 6 | 3072 | — |
| DONE | `/blog/why-is-my-furnace-running-constantly/` | 6 | 2157 | — |
| DONE | `/blog/why-is-my-heating-bill-so-high/` | 6 | 2962 | — |
| **WORK** | `/blog/do-smart-sprinkler-controllers-save-water/` | 6 | 3036 | P2 FAQ-MISSING |
| **WORK** | `/blog/electric-supplier-scams-how-to-spot/` | 6 | 2496 | P2 FAQ-MISSING |
| **WORK** | `/blog/gas-leak-signs-what-to-do-bill-impact/` | 6 | 2171 | P2 FAQ-MISSING |
| DONE | `/blog/point-sensor-vs-whole-home-water-leak-when-to-upgrade/` | 6 | 3190 | — |
| DONE | `/blog/can-utility-shut-off-service/` | 6 | 3915 | — |
| **WORK** | `/blog/50-best-smart-plugs-standby-power/` | 6 | 2378 | P1 SLUG-NUM; P2 FAQ-MISSING |
| **WORK** | `/blog/12-how-to-read-your-gas-bill/` | 6 | 2379 | P1 SLUG-NUM; P2 FAQ-MISSING |
| **WORK** | `/blog/how-to-lower-electric-bill-without-solar/` | 6 | 1343 | P2 FAQ-MISSING |
| **WORK** | `/blog/average-utility-bills-in-pennsylvania/` | 5 | 1809 | P0 DUPLICATE |
| DONE | `/blog/furnace-smells-like-burning/` | 5 | 2884 | — |
| DONE | `/blog/best-smart-thermostats-winter-savings/` | 5 | 3699 | — |
| DONE | `/blog/what-temperature-thermostat-winter/` | 5 | 3216 | — |
| **WORK** | `/blog/how-many-kwh-does-a-house-use-per-day/` | 5 | 1663 | P2 FAQ-MISSING |
| **WORK** | `/blog/46-what-time-is-electricity-cheapest/` | 5 | 1857 | P1 SLUG-NUM |
| **WORK** | `/blog/42-best-energy-efficient-space-heater/` | 5 | 2646 | P1 SLUG-NUM |
| **WORK** | `/blog/22-minimum-bill-utility-bill-explained/` | 5 | 1484 | P1 SLUG-NUM |
| DONE | `/blog/tiered-water-rates-explained/` | 5 | 2394 | — |
| DONE | `/blog/christmas-lights-electricity-cost/` | 4 | 3336 | — |
| DONE | `/blog/do-thermal-curtains-really-work/` | 4 | 2898 | — |
| DONE | `/blog/how-to-dispute-utility-bill/` | 4 | 3374 | — |
| DONE | `/blog/net-metering-explained/` | 4 | 2299 | — |
| DONE | `/blog/complete-guide-understanding-utility-bill/` | 4 | 2967 | — |
| **WORK** | `/blog/09-apartment-utilities-cost/` | 4 | 1251 | P1 SLUG-NUM; P2 FAQ-MISSING |
| DONE | `/blog/heat-pump-running-all-day-in-winter/` | 4 | 2605 | — |
| DONE | `/blog/why-is-my-furnace-blowing-cold-air/` | 4 | 2029 | — |
| DONE | `/blog/heat-tape-vs-pipe-insulation/` | 3 | 3368 | — |
| DONE | `/blog/electric-baseboard-heater-cost-to-run/` | 3 | 3685 | — |
| **WORK** | `/blog/do-dehumidifiers-help-cooling-costs/` | 3 | 2679 | P2 FAQ-MISSING |
| **WORK** | `/blog/which-rate-plan-is-right-for-me/` | 3 | 1688 | P2 FAQ-MISSING |
| DONE | `/blog/phantom-power-draw-explained/` | 3 | 2638 | — |
| DONE | `/blog/utility-assistance-programs-liheap/` | 3 | 1644 | — |
| **WORK** | `/blog/44-how-to-lower-water-bill/` | 3 | 2180 | P1 SLUG-NUM; P2 FAQ-MISSING |
| **WORK** | `/blog/45-whole-house-generator-vs-portable-cost/` | 3 | 2794 | P1 SLUG-NUM |
| **WORK** | `/blog/04-hidden-fees-utility-bill/` | 3 | 1983 | P1 SLUG-NUM; P2 FAQ-MISSING |
| DONE | `/blog/how-to-budget-for-utilities-in-your-first-apartment/` | 3 | 1591 | — |
| DONE | `/blog/afue-vs-seer-vs-hspf-vs-cop/` | 3 | 2284 | — |
| DONE | `/blog/aux-heat-vs-emergency-heat-meaning/` | 3 | 1915 | — |
| **WORK** | `/blog/single-stage-vs-two-stage-vs-variable-speed-hvac/` | 3 | 1957 | P2 FAQ-MISSING |
| **WORK** | `/blog/smart-thermostat-time-of-use-savings/` | 2 | 1906 | P2 FAQ-MISSING |
| DONE | `/blog/do-home-energy-monitors-save-money/` | 2 | 3268 | — |
| **WORK** | `/blog/gadgets-that-lower-utility-bills/` | 2 | 2753 | P2 FAQ-MISSING |
| **WORK** | `/blog/47-check-energy-leaks-home-diy/` | 2 | 2442 | P1 SLUG-NUM |
| **WORK** | `/blog/13-ac-short-cycling-causes-fixes/` | 2 | 1627 | P1 SLUG-NUM; P2 FAQ-MISSING |
| **WORK** | `/blog/05-how-to-lower-utility-bills/` | 2 | 2304 | P1 SLUG-NUM |
| **WORK** | `/blog/07-gas-bill-too-high/` | 2 | 5479 | P1 SLUG-NUM |
| DONE | `/blog/water-meter-leak-indicator-explained/` | 2 | 3039 | — |
| DONE | `/blog/duct-leaks-symptoms-hvac-running-all-day/` | 2 | 1703 | — |
| **WORK** | `/blog/average-utility-bills-in-florida/` | 1 | 1808 | P0 DUPLICATE |
| DONE | `/blog/how-to-keep-pipes-from-freezing/` | 1 | 3184 | — |
| DONE | `/blog/flume-vs-moen-flo-vs-phyn-water-monitors/` | 1 | 2476 | — |
| DONE | `/blog/how-to-read-gas-meter/` | 1 | 3574 | — |
| DONE | `/blog/drought-surcharge-on-water-bill-explained/` | 1 | 1882 | — |
| DONE | `/blog/heat-pump-covered-in-ice-normal-or-problem/` | 0 | 3328 | — |
| DONE | `/blog/why-does-my-furnace-keep-turning-on-and-off/` | 0 | 3336 | — |
| DONE | `/blog/does-closing-vents-save-money/` | 0 | 1708 | — |
| DONE | `/blog/furnace-tune-up-cost-schedule/` | 0 | 2557 | — |
| DONE | `/blog/what-merv-rating-do-i-need/` | 0 | 2796 | — |
| **WORK** | `/blog/do-programmable-thermostats-cut-heating-bills/` | 0 | 1915 | P2 FAQ-MISSING; P2 ZERO-TRAFFIC |
| **WORK** | `/blog/ductless-mini-split-vs-central-air/` | 0 | 2695 | P2 ZERO-TRAFFIC |

### Taxonomy pages (9)

| Status | Page | 90d sess | Words | Issues |
|---|---|---|---|---|
| DONE | `/blog/category/bills-fees/` | 10 | 1202 | — |
| DONE | `/blog/category/heating-cooling/` | 10 | 1544 | — |
| DONE | `/blog/category/electricity/` | 7 | 1296 | — |
| DONE | `/blog/category/water/` | 6 | 1451 | — |
| DONE | `/blog/category/savings-efficiency/` | 4 | 270 | — |
| **WORK** | `/categories/` | 0 | 82 | P2 THIN-LISTING |
| **WORK** | `/blog/category/consumer-rights/` | 0 | 62 | P2 THIN-LISTING |
| DONE | `/blog/category/gas/` | 0 | 195 | — |
| DONE | `/blog/category/troubleshooting/` | 0 | 263 | — |

### Listings (2)

| Status | Page | 90d sess | Words | Issues |
|---|---|---|---|---|
| DONE | `/` | 19 | 717 | — |
| **WORK** | `/calculators/` | 0 | 46 | P2 THIN-LISTING |

### Calculator (1)

| Status | Page | 90d sess | Words | Issues |
|---|---|---|---|---|
| DONE | `/calculators/electricity-cost/` | 8 | 214 | — |

### Standalone pages (17)

| Status | Page | 90d sess | Words | Issues |
|---|---|---|---|---|
| **WORK** | `/about/` | 25 | 375 | P1 DOUBLE-H1 |
| **WORK** | `/contact/` | 16 | 156 | P1 DOUBLE-H1 |
| DONE | `/utility-bills-costs-explained/` | 13 | 2347 | — |
| DONE | `/editorial-team/` | 12 | 866 | — |
| DONE | `/affiliate-disclosure/` | 10 | 251 | — |
| **WORK** | `/privacy-policy/` | 10 | 645 | P1 DOUBLE-H1 |
| **WORK** | `/methodology/` | 8 | 341 | P1 DOUBLE-H1 |
| DONE | `/lower-your-bills/` | 7 | 1034 | — |
| **WORK** | `/corrections/` | 6 | 382 | P1 DOUBLE-H1 |
| **WORK** | `/disclaimer/` | 5 | 150 | P1 DOUBLE-H1 |
| **WORK** | `/terms/` | 5 | 553 | P1 DOUBLE-H1 |
| **WORK** | `/editorial-policy/` | 4 | 409 | P1 DOUBLE-H1 |
| DONE | `/electricity-explained/` | 4 | 2263 | — |
| DONE | `/heating-cooling-explained/` | 4 | 2353 | — |
| DONE | `/utilities-glossary/` | 3 | 2032 | — |
| DONE | `/water-explained/` | 3 | 2357 | — |
| DONE | `/gas-explained/` | 1 | 1368 | — |
