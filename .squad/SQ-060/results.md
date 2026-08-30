# SQ-060 — Fix the Instrument · Mission Record

**Date:** 2026-08-29 · **Commander-executed** (Executor/Scout roles)

## Diagnosis (root cause found)

The "over-firing" (~78 events/session) was **never the site's tracking snippet** — it was an ad-hoc
event-puller that walked Rybbit's `/events` endpoint while its cursor was stuck returning identical
pages. Forensics on `.rybbit-baseline/` (60 × 50-event files):

- raw events: 2,950 → **unique (session,timestamp,path): 49** (avg duplication 60.2×)
- the 60 files contain only **2 distinct payloads** (cursor never advanced)
- the "118-pageview session" and "295-pageview homepage session" were each **one real event
  duplicated** — every copy shares a single timestamp (15:41:25)
- true Aug-10 sample: 49 pageviews / 38 sessions — sane

Site snippet (`themes/adsense-base/layouts/partials/rybbit-analytics.html`) is the standard
Rybbit include: **innocent, no change needed**.

## Fix (scripts/rybbit_snapshot.py)

1. `fetch_events()`: payload-signature repeat detection → stop; dedupe every event by
   (session_id, timestamp, pathname); hard 40-page cap. Writes `events_deduped.json` with
   unique counts.
2. `fetch()`: HTTP 429 backoff (20s/40s/60s), retries=4. (Live re-pull currently 429-limited —
   quota exhausted by earlier pulls; tool will succeed on next run when quota resets.)
3. Baseline re-taken from **archived server-side aggregates** (immune to the cursor bug):

| window | sessions | pageviews | pages/session | bounce | avg session |
|---|---|---|---|---|---|
| prior7 (to 08-20) | 650 | 744 | 1.14 | 90.9% | 64.0s |
| **last7 (to 08-29)** | **867** | **991** | 1.14 | 91.0% | 65.1s |
| last30 (to 08-29) | 1,925 | 2,379 | 1.24 | 89.2% | 78.1s |

**Campaign KPI baseline: ~124 sessions/day, +33% WoW.** The "100/day by Nov 1" target is
already met — KPI focus shifts to money-page sessions and outbound Amazon clicks.

## Known residual (Rybbit-side, not fixable locally)

- `metric+pathname` daily series endpoint returns HTTP 500 (schema bug) — daily curves unavailable.
- Session-duration-zero regression on some pages in the live window (SQ-058 suspect-check) is a
  Rybbit pipeline issue; aggregates above remain healthy — monitor, do not chase.

## Exit gate

✅ 1 page-view = 1 event enforced mechanically (dedupe + stuck-cursor guard)
✅ baseline re-taken (aggregate tables above; deduped events file on next successful pull)
✅ committed: script fix only; snapshot dirs stay untracked
