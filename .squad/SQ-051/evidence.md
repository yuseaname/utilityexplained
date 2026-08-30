# SQ-051 Evidence Brief — Selection + Engagement Data (2026-08-29)
Selection method: GSC data unavailable in this environment → top 30 by Rybbit Analytics 30-day pageviews (site_id d5b63e065e9d, API pull 2026-08-29), trailing-slash variants merged, /blog pagination excluded. Bounce (br) and time-on-page (TOP) are session-weighted. Traffic is Bing-ecosystem heavy (Google share ~5%).

| # | slug (content/blog/<slug>.md) | pv30d | br% | TOP s |
|---|---|---|---|---|
| 1 | how-to-lower-electric-bill-complete-guide | 222 | 87.8 | 55 |
| 2 | 30-sudden-spike-in-electricity-bill-no-usage | 131 | 86.8 | 36 |
| 3 | how-sewer-charges-work-on-your-water-bill | 130 | 80.2 | 80 |
| 4 | water-meter-running-when-no-water-used | 123 | 81.9 | 60 |
| 5 | what-is-ccf-on-a-water-bill | 113 | 84.1 | 47 |
| 6 | 28-utility-reconnection-fee-explained | 98 | 81.5 | 76 |
| 7 | water-meter-leak-indicator-explained | 98 | 67.0 | 86 |
| 8 | 06-water-bill-too-high | 85 | 93.8 | 42 |
| 9 | 05-how-to-lower-utility-bills | 68 | 73.4 | 86 |
| 10 | 23-utility-billing-cycle-explained | 65 | 83.1 | 57 |
| 11 | electric-bill-breakdown-understanding-line-items | 65 | 71.7 | 56 |
| 12 | 03-why-is-my-electric-bill-so-high | 64 | 85.2 | 31 |
| 13 | 07-gas-bill-too-high | 64 | 84.2 | 90 |
| 14 | 25-utility-bill-taxes-fees-franchise-charges-explained | 45 | 82.1 | 6 |
| 15 | stormwater-fee-on-water-bill-explained | 39 | 86.1 | 12 |
| 16 | average-utility-bills-by-state-2026 | 33 | 86.7 | 14 |
| 17 | average-water-usage-per-person | 32 | 82.1 | 33 |
| 18 | how-do-smart-meters-work | 31 | 89.7 | 17 |
| 19 | 19-utility-bill-surcharges-and-riders-explained | 29 | 92.9 | 8 |
| 20 | mcf-vs-ccf-vs-therms-on-gas-bill | 28 | 88.9 | 37 |
| 21 | why-your-electric-bill-keeps-rising-2026 | 28 | 96.3 | 0 |
| 22 | 49-demand-charges-electricity-bill-explained | 28 | 82.6 | 81 |
| 23 | why-did-my-water-bill-suddenly-increase | 27 | 77.8 | 10 |
| 24 | is-your-toilet-running-leak-test | 25 | 36.0 | 3 |
| 25 | 18-fuel-adjustment-charge-on-utility-bill-explained | 25 | 95.8 | 27 |
| 26 | 27-utility-connection-fee-explained | 25 | 81.8 | 9 |
| 27 | how-to-read-electric-meter | 23 | 86.4 | 19 |
| 28 | how-to-read-a-water-meter | 23 | 65.2 | 72 |
| 29 | 08-time-of-use-electricity | 22 | 84.2 | 42 |
| 30 | tiered-electricity-rates-explained | 22 | 83.3 | 18 |

Known engagement anomalies: #21 (96.3% br, 0s TOP = instant exits), #14 (6s TOP), #19 (8s), #8 (93.8% br on 85pv) — defect-exit suspects. #24 toilet test = positive outlier (36% br) — identify why it works. #7 leak-indicator had trailing-slash split (68/27) — check canonical/redirect handling.
