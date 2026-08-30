# SQ-058 — Rybbit Suspect-Metric Adjudication

**Date:** 2026-08-29  ·  **Site:** utilityexplained.com (`d5b63e065e9d`)  ·  **Source:** Rybbit live pathname metric + archived snapshots

## Verdict

| Page | Verdict | Confidence |
|---|---|---|
| why-did-my-water-bill | TRACKING ARTIFACT (regression) | high |
| how-to-read-a-water-meter | TRACKING ARTIFACT (regression) | high |

Both were healthy (nonzero top_s) in every prior window and regressed to ~0 only in the current LIVE pull. This refutes the page-level hypothesis (link-dense / FAQ schema = permanent tracking bug). The current-window 0 is a recent regression in the tracking pipeline (pageview fires, session-duration does not), not real user behavior.

## (a) Was top_s ever nonzero?

Yes, both. Every archived window shows nonzero top_s (seconds):

| Page | Aug-10 baseline | 07-28→08-27 last30 | 08-13→08-20 prior7 | 08-20→08-27 last7 | LIVE 07-30→08-29 last30 |
|---|---|---|---|---|---|
| why-did-my-water-bill | entry=1 | 7.71s | 9.41s | 8.82s | 0.0s |
| how-to-read-a-water-meter | entry=2 | 6.75s | 9.00s | 10.0s | 0.53s |

## (b) Consistent 0-time gap, or recent change to 0?

Recent change to 0 = regression. Trend: healthy in all windows ending ≤ Aug 27 → ~0 in the LIVE window ending Aug 29.

Two reinforcing signatures:
- pv == count on both suspects in LIVE: why=24/24; meter=19/19. Healthy pages show pv > count (e.g. `how-to-read-electric-meter` 20/21). pv==count means the pageview tracker fired but the session-duration tracker did not record time — classic tracking-gap signature.
- Count rose while time hit 0 (why 19→24, meter 14→19) — more visits, no dwell recorded — a tracker failure, not real instant-bounce behavior.

## (c) Control siblings

Mixed, but the closest analog is healthy. Same-count-band (18–24) control rows in the LIVE last30 pull:

| Page | count | top_s (s) | bounce % | verdict |
|---|---|---|---|---|
| `how-to-read-electric-meter/` | 20 | 21.1 | 90.0 | healthy |
| `how-to-read-your-electric-bill/` | 19 | 69.2 | 78.9 | healthy |
| `how-do-smart-meters-work/` | 25 | 19.9 | 92 | healthy |
| `49-demand-charges-electricity-bill-explained/` | 23 | 21.2 | 82.6 | healthy |
| `08-time-of-use-electricity/` | 20 | 40.6 | 85 | healthy |
| `27-utility-connection-fee-explained/` | 22 | 9.4 | 81.8 | healthy |
| `21-past-due-balance-utility-bill-explained/` | 18 | 29.6 | 88.9 | healthy |
| `18-fuel-adjustment-charge-on-utility-bill-explained/` | 24 | 0.0 | 95.8 | also ~0 |
| `utility-bills-costs-explained/` | 21 | 0.19 | 71.4 | also ~0 |
| `why-did-my-water-bill-suddenly-increase/` | 24 | 0.0 | 91.7 | suspect |
| `how-to-read-a-water-meter/` | 19 | 0.53 | 78.9 | suspect |

The breakage is not unique to the two suspects — two other low-volume pages (`fuel-adjustment-charge`, `utility-bills-costs`) are also ~0 in the same pull, while several same-count pages are healthy. This points to a site-wide tracking regression in the current window rather than an isolated per-page bug. The page-specific FAQ/link-density hypothesis is not supported.

## (d) Daily time-series — limitation

The requested per-day `pathname` series could NOT be pulled: the daily-parameter schema on the live API returns HTTP 500 for every candidate name tried, and the `group_by` variant still returns pathname (not date) groups. The `events` endpoint could not reconstruct a daily curve either — its cursor returns identical pages (100% overlap, never advances), so pagination loops. As a result, this report is built from multi-window aggregates (a strong proxy) rather than a literal day-by-day trace.

## Residual INCONCLUSIVE

- Daily per-day regression curve not obtainable. Regression timing inferred as ~Aug 27→29 (last healthy window ending 08-27 vs. current zero window).
- Mechanism (site-wide tracker regression vs. page-specific) is probable (control is mixed), not proven — the daily series that would cleanly separate "only these pages broke" from "whole site broke" was unavailable.

## Recommendation

Do NOT treat these as page-quality defects (FAQ schema, link density, copy). If the 0 is real for the site, the fix is in the tracking pipeline (session-duration capture) for the current window, not the content. Re-pull once the daily-parameter schema is fixed and confirm whether the ~0 cohort (which includes `fuel-adjustment-charge`, `utility-bills-costs`) is site-wide or localized.

## Evidence

- Live `pathname` metric pull: `.rybbit-t11320-2026-08-29/snapshot.json` (LIVE last30 rows).
- Archived windows: `.rybbit-snapshot-2026-08-27/snapshot.json` (last7/prior7/last30 pages data).
- Aug-10 entry counts: `RYBBIT_BASELINE_2026-08-10.json` (entry_pages).
- Aug-10 events burst: `.rybbit-baseline/events_raw.json` (how-to-read-a-water-meter 118 pageviews in a single session on 08-10).
- API shape: live `sessions`/`events` list endpoints return 200; `metric`+`pathname` returns the top_s table.
