# UtilityExplained — KPI Tracking Dashboard

## Completion Contract — OFFICIAL FINISH LINE (confirmed 2026-08-30)

The site is an ongoing publication, not a finite build. "Complete" means the traffic-quality milestones below are **all met and sustained for 14+ consecutive days**, measured in Rybbit:

- [ ] **AC-1:** Sessions ≥ 150/day sustained 14+ days (baseline Aug 21: ~191/day, Bing-driven)
- [ ] **AC-2:** Bounce rate < 70% (baseline: 84.7%)
- [ ] **AC-3:** Pages/session ≥ 2.0 (baseline: 1.52)
- [ ] **AC-4:** Google-referral sessions ≥ 50/day (baseline: ~22/week)
- [ ] **AC-5:** US visitor share ≥ 80% (baseline: 78%; CN bot traffic excluded)

**Acceptance evidence:** Rybbit screenshots/exports attached to a GROWTH_LOG entry showing the 14-day window with all five criteria green.
**Acceptance authority:** site owner.
**Out of scope as completion gates:** AdSense approval, affiliate revenue (tracked, but they are monetization outcomes, not the finish line).

## Current Baseline (August 21, 2026 — 7-day window)
Source: Rybbit Analytics. **Traffic spiked ~Aug 14–16 via Bing-ecosystem indexation** (DDG 42%, Bing 35%, Yahoo 12%; Google 4.8% — not yet following).

## Current Baseline (September 4, 2026 — latest snapshot) — CONTRACT STATUS: ALL 5 ACs UNMET

Source: `.rybbit-snapshot-2026-09-04/snapshot.json` (7d window Aug 28–Sep 4). Trend since the Aug-21 baseline is documented in GROWTH_LOG Entry 24: engagement moved AWAY from contract targets (bounce 84.7→88.1%, pages/session 1.52→1.20) while traffic settled at ~121/day. Root-cause diagnosis: GROWTH_LOG Entry 25 (SQ-068) — Rybbit bounce is largely a metric artifact (GA4 shows 29–50% on the same pages); real defects ranked there.

| Metric | Aug 21 (7d) | Aug 24–31 | **Sep 4 (7d)** | Contract target | Status |
|--------|--------------|-----------|----------------|-----------------|--------|
| Sessions/day | ~191 (spike-inflated) | 135 | **121** | ≥150 (AC-1) | ❌ unmet |
| Bounce Rate | 84.7% | 90.6% | **88.1%** | <70% (AC-2) | ❌ unmet (see Entry 25 artifact note) |
| Pages/Session | 1.52 | 1.15 | **1.20** | ≥2.0 (AC-3) | ❌ unmet |
| Google Traffic | 22/7d | 30/7d | **37/7d (~5/day)** | ≥50/day (AC-4) | ❌ unmet — **GSC sitemap submitted 2026-09-07**; impressions should begin |
| US Visitors | 78% | 77.7% | **75.9%** (CN 12.2% = bots) | ≥80% (AC-5) | ❌ unmet (ex-CN ≈ 86%) |
| Duration | 80s | 63s | **71s** | — | — |

Channels (7d): Organic Search 65%, Direct 32%. Referrers: DDG 242, Bing 177, Yahoo 73, Google 37 — Bing ecosystem ≈ 90% of search referrals.

## Monetization & tracking state (2026-09-07)

- **Affiliate surface:** 179 tagged placements across 53 monetized pages (was 157/44 pre-Sep-12 — Entry 28 added 10 Prime-filtered articles + 22 placements). All promoted picks buy-box-verified 2026-09-11 (sold-by-Amazon or FBA; non-Prime bests rejected or replaced per the owner's hard filter). **Vue 3 band fixed 2026-09-12** ($150–180 → ~$100–200 across 3 articles, 7 occurrences). Watch: Frost King SP57 thin stock on common size; Rinnai RX130iN unverified → tankless article intentionally unmonetized.
- **Ads/affiliate separation:** Auto Ads loader now skips all 44 money pages (`head.html` conditional on placements or `no_ads` front-matter); informational pages keep ads. Rationale + research cites: GROWTH_LOG Entry 27.
- **Event tracking live:** `affiliate_click` (Rybbit native + GA4 mirror, with asin/format props) and `email_capture` (home + article_footer). **Owner action: mark `affiliate_click` as GA4 key event** (Admin → Events). Zero events recorded yet — first CTR data expected within 1–2 weeks of traffic.
- **CTR pass shipped:** early-link + closing-CTA pattern on 6 top-traffic pages and 4 buyer-intent articles (HouseFresh-pattern, cited in Entry 27).

## AdSense status — SETUP RESTORED, READY FOR RE-REVIEW (2026-08-31; scope narrowed 2026-09-07)
History: blocked Aug 23 ("Low value content") → ads.txt + loader were removed in the affiliate pivot (commit 6d4390c8). The editorial gate work (audit SQ-065/066 remediation, desk bylines, production disclosure, 96-guide corpus) is complete and verified. AdSense machinery restored 2026-08-31: ads.txt (pub-5566942094411042, DIRECT, f08c47fec0942fa0) at site root + adsbygoogle.js loader (consent-mode ordered, single swap-point `adsense_client` in hugo.toml) — **now informational pages only** (2026-09-07: money pages excluded so display ads never compete with affiliate CTAs or contaminate the CTR baseline). **Next action (owner): request re-review in the AdSense console.** Loader alone serves Auto ads only if enabled in the account; manual slots (below_title/mid_article/end_article) can be re-added after approval on informational pages — commit 6d4390c8 documents exactly where they lived.

### Historical baseline table (Aug 10 / Aug 21 — superseded by Sep-4 section above)

| Metric | Aug 10 (90d) | **Aug 21 (7d)** | Target (30 days) | How to Measure |
|--------|--------------|-----------------|-------------------|----------------|
| Sessions | ~3/day | **~191/day** | sustain 150+/day | Rybbit > Overview |
| Bounce Rate | 79.8% | **84.7%** | <70% | Rybbit > Overview |
| Pages/Session | 1.76 | **1.52** | >1.9 | Rybbit > Overview |
| Avg Duration | 112s | **80s** | >120s | Rybbit > Overview |
| Google Traffic | 2/90d | **22/7d (4.8%)** | 50+/day | Rybbit > Referrers |
| US Visitors | 77% | **78%** (CN 13.5% @99% bounce = bots) | >80% | Rybbit > Countries |

**Watch (post 2026-08-21 batch):** bounce + time-on-page on the 4 defect-exit pages (taxes-fees, complete-guide, water-meter, spike-electric); hub-page entrances after title shortening; IndexNow-submitted URL pickup in Bing.

**Watch (post 2026-08-22 SQ-016 Phase A — measurement window open):** bounce on long articles after funnel reorder + answer-first hero (target <70%); pages/session after related-posts promotion (target >1.9); hub entrance → article CTR on the 5 new hub directories; AdSense mid-article slot (7429084400) viewability + RPM vs 1-ad baseline at +14 days; retired-category 301 traffic loss (should be ~0 via /blog/category/bills-fees/ etc.).

## Milestones (from original plan)
1. **100 visitors/day sustained** for 14+ days
2. **150-200 pageviews/day**
3. **Bounce rate below 60%**
4. **Bounce rate below 50%** while preserving traffic
5. **2.0+ pages/session**
6. **250-300+ pageviews/day**

## What Each Change Should Affect (current wave — Sep 2026)

| Change | Expected Impact | Metric to Watch |
|--------|----------------|-----------------|
| GSC sitemap submitted (2026-09-07) | Google indexing begins; AC-4 unfreezes | GSC Pages indexed + impressions; Google referrals in Rybbit |
| Post-Sense article cluster (5 articles, 2026-09-06) | Google/Bing pickup on vacated SERPs | GSC impressions per new URL; entrances on pillar |
| Early-link CTR pass (14 links, 10 pages, 2026-09-07) | Outbound CTR rises on existing traffic | `affiliate_click` events (Rybbit Events tab + GA4) |
| Ads/affiliate separation (44 money pages, 2026-09-07) | No ad-contaminated CTR baseline; cleaner money-page UX | affiliate_click CTR trend; AdSense coverage on info pages |
| Water-ladder completion (3 pages) | Higher-AOV rungs reachable | affiliate_click by asin (Flume/Flo vs Govee) |
| email_capture event | Lead visibility | Rybbit/GA4 `email_capture` count vs Mailchimp signups |
| Winter refresh (pending) | Seasonal Sep–Feb traffic | Entrances on winter cluster |
| Next-10 wave (2026-09-12, Entry 28) | 10 new money-cluster entries on weak/forum SERPs; IndexNow-submitted | IndexNow/Bing pickup of 10 new URLs; entrances + affiliate_click on new pages |

## Monitoring Schedule (revised 2026-09-07)
- **Weekly:** Full Rybbit review vs Sep-4 baseline (sessions/day, Google referrals) + **GSC**: indexing status, impressions by page, top queries — the sitemap is submitted; this is now the primary discovery signal
- **Weekly (15 min):** affiliate_click events by page/asin/format + email_capture; dead-ASIN spot check on any page being edited (dossier guardrail: re-verify ASINs on publish day)
- **Bi-weekly:** Vue 3 price-band drift check (prose says $150–180; live was $99.99 on 2026-09-07); P4456 stock level (was low)
- **Monthly:** Comprehensive comparison — update this dashboard with a new snapshot (scripts/rybbit_snapshot.py)

## Growth Log Location
All changes documented in: GROWTH_LOG.md
Baseline data saved in: RYBBIT_BASELINE_2026-08-10.json
Full mission report: MISSION_REPORT_2026-08-10.md