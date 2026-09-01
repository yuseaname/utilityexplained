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

## AdSense status — SETUP RESTORED, READY FOR RE-REVIEW (2026-08-31)
History: blocked Aug 23 ("Low value content") → ads.txt + loader were removed in the affiliate pivot (commit 6d4390c8). The editorial gate work (audit SQ-065/066 remediation, desk bylines, production disclosure, 96-guide corpus) is complete and verified. AdSense machinery restored 2026-08-31: ads.txt (pub-5566942094411042, DIRECT, f08c47fec0942fa0) at site root + adsbygoogle.js loader on all pages (consent-mode ordered, single swap-point `adsense_client` in hugo.toml). **Next action (owner): request re-review in the AdSense console.** Loader alone serves Auto ads only if enabled in the account; manual slots (below_title/mid_article/end_article) can be re-added after approval — commit 6d4390c8 documents exactly where they lived.

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

## What Each Change Should Affect

| Change | Expected Impact | Metric to Watch |
|--------|----------------|-----------------|
| .htaccess trailing slash 301s | Google indexing improves | Google sessions in Rybbit |
| Quick Answers on 97 articles | Bounce rate drops | Bounce % on rescued pages |
| 800+ internal links | Pages/session rises | Pages/Session in Overview |
| 5 hub pages + blog grid | Discovery improves | Entrances on hub pages |
| Email capture | Conversions begin | Email signups (check Mailchimp) |
| 3 AdSense slots | Revenue increases | AdSense dashboard |
| Mid-article ad | Higher CTR | AdSense CTR by position |
| Phantom power article | New organic traffic | Entrances on phantom article |

## Monitoring Schedule
- **Daily (first 7 days):** Quick Rybbit check — any traffic spikes? New referrers?
- **Weekly:** Full Rybbit review — compare to baseline, note winners/losers
- **Bi-weekly:** Google Search Console — check indexing status, submit sitemap if needed
- **Monthly:** Comprehensive comparison — update this dashboard with new numbers

## Growth Log Location
All changes documented in: GROWTH_LOG.md
Baseline data saved in: RYBBIT_BASELINE_2026-08-10.json
Full mission report: MISSION_REPORT_2026-08-10.md