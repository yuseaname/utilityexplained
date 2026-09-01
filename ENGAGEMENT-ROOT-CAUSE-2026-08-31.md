# Engagement Root-Cause Diagnosis — 2026-08-31

**Scope:** mechanical adjudication of the five engagement hypotheses for utilityexplained.com, from the 2026-08-31 Rybbit snapshot (944 sessions, 2026-08-24..31) plus the prior snapshots, the event log, and the prior content/SEO audits. READ-ONLY against site files; all fixes are recommended, not applied.

**Data sources:** `.rybbit-snapshot-2026-08-31/snapshot.json` (per-page views/ToP/bounce, referrers, channels, countries, 3 windows), `events_deduped.json` (24-session session-level sample with timestamps/referrers/page-titles), `GROWTH_LOG.md` Entries 1-24, `KPI_DASHBOARD.md`, `CONTENT-AUDIT-2026-08-28.md`, `FULL-CONTENT-SEO-AUDIT-2026-08-30.md`, `SEO-CONTENT-AUDIT-FACTCHECK-2026-08-29.md`, `layouts/_default/single.html`.

---

## 1. Verdict Table — Hypothesis Adjudication

| # | Hypothesis | Verdict | Strongest evidence | Est. share of excess bounce explained |
|---|-----------|---------|--------------------|---------------------------------------|
| H4 | Traffic quality (non-CN bot / zero-intent sessions inflate bounce) | **REFUTED** | Of 944 sessions, CN bots are 12.5% @ 95.8% bounce; removing CN entirely moves site bounce 90.6% → 89.8%, i.e. **~0.8pp** — the packet's own ~1.3pp estimate. The remaining 87.5% of sessions are US humans (DDG/Bing/Yahoo) who sit ~60s then leave. Human bounce, not bot. | **<1%** — bot exclusion is a rounding error vs the 21pp excess over the AC-2 <70% target. |
| H5 | Measurement artifacts (Rybbit counts read-then-leave as bounce) | **CONFIRMED — dominant driver** *(Commander amendment 2026-08-31, GA4 evidence; supersedes this row's earlier REFUTED — that verdict rested on an unreproducible statistic, see §8)* | **GA4 (Aug 3–30, owner-supplied export):** the same pages Rybbit shows at 85–94% bounce measure **29–50%** under GA4's engaged-session definition — flagship complete-guide **88.3%→29.2%**, spike **93.9%→46.2%**, gas-too-high **85.7%→25%**. Satisfied single-page readers dominate; Rybbit's single-page definition counts them as bounces. Corroborated: wave-2 twin_q found 158 sessions across 12 pages with >60s ToP at >80% Rybbit-bounce; per-page arithmetic (88.3% @52s avg ToP) forces long-dwell bounces. | **The majority of the 90.6%-vs-~40% gap.** GA4-equivalent site bounce ≈ **35–50%** (ESTIMATE) — the AC-2 <70% target is already met on top pages under GA4 definitions. |
| H1 | Intent mismatch (Bing ranks pages for queries whose searchers don't get what they expected) | **UNVERIFIED, plausibly ACTIVE** | The 90-95% crisis cluster — `why-did-my-utility-bill-go-up-this-month` (93.9%), `why-did-my-water-bill-suddenly-increase`, `30-sudden-spike-in-electricity-bill-no-usage`, `06-water-bill-too-high`, `03-why-is-my-electric-bill-so-high` — is a self-consistent **"why did my bill go up" investigation set**. The flagship title promises "why did it go up" but the page's Quick Answer answers billing-cycle/rate-shift/usage, not "why." Question ≠ headline promise. The Bing ecosystem drives 31%+ of sessions; Bing's ranking and the searcher's actual question are both unmeasurable from the snapshot. | **ESTIMATE 10-20%** — a real, addressable share *if* confirmed by GSC query data; cannot be quantified without query-level data. |
| H2 | Presentation — answer-first hero not landing the answer fast enough | **REFUTED (for presentation); format variance CONFIRMED** | Layouts confirm the answer-first hero exists and renders below the collapsed TOC (SQ-016 Phase A; verifier F9: defect pages DO open with a QA — spike-electric starts `## Quick Answer: Why Did My Electric Bill Spike…`). The variance: part of the corpus (incl. `why-did-my-utility-bill-go-up-this-month`) uses a non-canonical HTML `<h2 id="quick-answer">` block instead of the `## Quick Answer` markdown hero — a consistency defect, not an absence (Commander disk-verified: 84 canonical files, legacy variant persists in a dozen+; the earlier "no QA at all" claim was wrong). | **ESTIMATE 5–15%** — downgraded from 20–30% after the GA4 correction; most crisis pages' readers engage fine once measured correctly. |
| H3 | Content-shape (length, links, tables, hub wiring share features with low-bounce pages) | **REFUTED** | Correlation across all pages with ≥10 sessions: bounce vs words (r≈0), vs h2/h3/headings (r≈0), vs internal links, vs tables, vs images — all non-discriminating. The strong diagnostic core and the crisis set share structure but differ on bounce. Length and link-count are NOT the lever. | **~0%** — structure features do not separate high- from low-bounce pages. |
| (Google-0) | Google stuck at 4.7% (separate KPI, not an engagement hypothesis) | **CONFIRMED MECHANICAL** | `FULL-CONTENT-SEO-AUDIT-2026-08-30.md`: the deploy pings IndexNow only (Bing ecosystem), with **no GSC sitemap submission**. Google has no submission/ping → no reason to rank/track → 4.7% referrals (30/week vs 50/day needed). Mechanical and independent of the engagement bounce. | **N/A — traffic, not engagement.** Resolved by a one-shot GSC sitemap submit (owner action). |

**Bottom line (as amended):** The Rybbit 90.6% headline is **mostly a metric-definition artifact (H5) plus a real but much smaller human-dissatisfaction residue concentrated in a handful of pages that are bad under BOTH definitions** (electric-bill-breakdown 83.3% GA4 / 89.3% Rybbit, what-is-ccf 75% / 86.7%, billing-cycle 66.7% / 90%). NOT bots (H4, ~0.8pp), NOT structure (H3, correlations ≈0), and NOT a missing answer-hero (H2 — the pattern is deployed; a format variance remains on part of the corpus). H1 (intent mismatch) stays UNVERIFIED pending GSC query data, but GA4 softens its crisis framing (spike at 46.2% GA4 is unremarkable). Google-0 is a separate mechanical traffic problem (no GSC submission). **The Completion Contract's AC-2/AC-3 should be re-baselined to GA4 engaged metrics** — Rybbit raw bounce is unreachable-by-definition for a one-answer diagnostic site.

---

## 2. Top 10 Pages by Fix-Leverage (excess-bounce × sessions)

Floor = 70% (the AC-2 KPI target). Excess = (bounce − 70%) × sessions. Redirects resolved to live destinations (Entry 10 redirects folded the old slugs into their targets).

| # | Live page | Old slug (redirected) | Sessions | Bounce | Excess pp | Fix-leverage (sess×pp) | Primary defect |
|---|-----------|-----------------------|----------|--------|-----------|------------------------|----------------|
| 1 | `/blog/05-how-to-lower-utility-bills/` | `how-to-lower-electric-bill-complete-guide` → this | 145 | 88.3% | 18.3 | **2654** | Saved-flagship arithmetic/frontmatter + 249-dollar overpromise (C4) + answer buried |
| 2 | `/blog/30-sudden-spike-in-electricity-bill-no-usage/` | (none — live URL; the earlier claim it redirects to go-up was **wrong**) | 66 | 93.9% | 23.9 | **1579** | 75s ToP = read-then-terminate; GA4 46.2% (largely satisfied readers) |
| 3 | `/blog/06-water-bill-too-high/` | (none — live URL) | 41 | 95.1% | 25.1 | **1029** | 26s ToP = the closest thing to a genuine quick-exit page; GA4 60% |
| 4 | `/blog/water-meter-running-when-no-water-used/` | (none) | 38 | 89.5% | 19.5 | 741 | Diagnostic answer buried; QA not first screen element |
| 5 | `/blog/electric-bill-breakdown-understanding-line-items/` | (none) | 28 | 89.3% | 19.3 | 540 | Line-item decode not answer-first; no jump row |
| 6 | `/blog/what-is-ccf-on-a-water-bill/` | (none) | 30 | 86.7% | 16.7 | 501 | Definition-first, not diagnosis-first (Entry 4 caught this) |
| 7 | `/blog/03-why-is-my-electric-bill-so-high/` | (none) | 36 | 83.3% | 13.3 | 480 | Cause list (11) vs title ("so high"); needs the one-line bill check up front |
| 8 | `/blog/07-gas-bill-too-high/` | (none) | 28 | 85.7% | 15.7 | 440 | Refuted claim (C2: heating 40-45% vs claimed 60-70%) + count mismatch |
| 9 | `/blog/23-utility-billing-cycle-explained/` | (none) | 20 | 90.0% | 20.0 | 400 | "The billing period is the service-date range" buried in prose; QA should be the lead |
| 10 | `/blog/moving-utilities-checklist/` | (none) | 19 | 89.5% | 19.5 | 371 | Checklist not presented as the first actionable step |

**Concentration (corrected by Commander; earlier figures were wrong):** the snapshot's page rows sum to 1,013 while overview sessions = 944 (page-row overcounting — treat per-page session counts as approximate). Top-10 real pages ≈ **49.6% of sessions and ~48% of excess-bounce sessions** (verifier F3 + wave-2 twin_q agree; the earlier "44.5%/60%" was miscalculated). Beyond rank 10, bounce is 75–83% across the rest of the corpus.

---

## 3. Ranked Fix Levers (mechanism, steps, effect, effort, risk)

All effects labeled **ESTIMATE**. Effort is per-squad-agent mechanical passes (lieutenant brief + executor edits), not full rewrites.

### Lever 1 — Normalize the QA format + fix the both-definitions-bad pages (mechanical)
- **Addresses:** H2 format variance + the pages that stay bad under GA4 too. **Re-scoped by Commander after GA4:** under GA4 measurement the crisis cluster largely dissolves; the genuine engagement defects are the pages bad under BOTH definitions — `electric-bill-breakdown` (83.3% GA4), `what-is-ccf` (75%), `23-billing-cycle-explained` (66.7%), `past-due-balance` (60%), `why-is-my-water-bill-high-11-checks` (60%).
- **Mechanism:** (a) convert remaining `<h2 id="quick-answer">` blocks to canonical `## Quick Answer` heroes (consistency, rendering, and future-proofing); (b) on the both-bad pages, restructure so the first screen carries the actual payoff (the decoded line-item, the CCF→gallons→dollars conversion, the dates meaning) rather than a definition lead.
- **Steps:** (1) grep-convert legacy QA blocks; (2) per-page lead restructure on the 5 both-bad pages; (3) verify Hugo build EXIT 0 + rendered-output check.
- **ESTIMATE effect:** GA4 bounce −5 to −10pp on the both-bad set; site-GA4 metric moves a few points. Rybbit-raw bounce barely moves (metric artifact dominates) — **measure this lever in GA4, not Rybbit.**
- **Effort:** ~1 day (mechanical).
- **Risk:** LOW — format/lead-order changes; no fact edits.

### Lever 2 — Fix the flagship saved-guide overpromise (C4) so the 145-session page can be trusted
- **Addresses:** H3/content-credibility (the flagship is the #1 fix-leverage page but its defect is facts, not shape). Not an engagement lever per se, but a bounce page that reads as spam-classifier gets dropped.
- **Mechanism:** reconcile the two phantom-load tables to the $17 math, cap the thermostat claim at DOE 4-9% (not ~25%/6-12%), reconcile the $200-450 stacked banners to the $164.88 average bill, fix the duplicate `sources:` frontmatter.
- **Steps:** see `FULL-CONTENT-SEO-AUDIT-2026-08-30.md` C3/C4; ~1-2 day fact + arithmetic pass.
- **ESTIMATE effect:** indirect — clears the credibility smell so the engagement fixes on the same page stick; no direct bounce number.
- **Effort:** ~2 days.
- **Risk:** LOW-MEDIUM — fact edits can be re-verified; but the flagship is the site's most visible overpromise.

### Lever 3 — Intent-match rewrite of the 5 crisis-intent pages (question ≠ headline promise)
- **Addresses:** H1 (the only active, addressable engagement hypothesis). The "why did my bill go up this month" pages answer billing-cycle/rate-shift, not the surge; the headline promise is the answer.
- **Mechanism:** each crisis page leads with the *actual* answer to "why did it go up" — a ranked shortlist (usage spike vs price spike vs fixed charge vs estimated-read vs billing-day shift) with the one-line bill check for each, THEN the deep dive. Align the H1 to the reader's real question.
- **Steps:** rewrite the lead of #2/#3 to open with the ranked surge causes; add a jump row; ensure the Quick Answer names "did usage or price go up?" first. ~2-3 days for the set.
- **ESTIMATE effect:** −3 to −6pp each on the crisis set; this is the share H1 can realistically capture *if* Bing traffic is the intended audience (ESTIMATE, see open questions).
- **Effort:** ~3 days.
- **Risk:** MEDIUM — this is a content-rewrite (not mechanical); attribution to H1 vs H2 is entangled. Needs GSC query data to confirm the intent hypothesis before scaling.

### Lever 4 — Add the missing Savings & Efficiency hub + revive 3 dead-end pages (C6)
- **Addresses:** journey wiring (the site's best cluster has no hub; 3 pages send every reader off-site).
- **Mechanism:** build the Savings & Efficiency hub (audit's CLUSTER-SAVE); add one outbound internal link each on `net-metering`, `ev-charging`, `water-service-charge` (the three absolute dead ends).
- **Steps:** hub rebuild + 3 one-line link additions; ~1-2 days.
- **ESTIMATE effect:** converts off-site bounces on the 3 dead ends into session depth; marginal site-wide.
- **Effort:** ~2 days.
- **Risk:** LOW.

### Lever 5 — Google Search Console sitemap submission (Google-0)
- **Addresses:** the 4.7% Google-referral KPI (separate from engagement bounce).
- **Mechanism:** submit the production sitemap (121 URLs) to GSC; the deploy only pings IndexNow (Bing ecosystem) with no GSC submission.
- **Steps:** owner action — log into GSC, "Add a sitemap", then Validate Fix; ~30 min owner time + a CI/GSC step.
- **ESTIMATE effect:** mechanical — restores Google's ability to rank/track (needed for AC-4 ≥50/day). No direct bounce effect.
- **Effort:** ~0.5 day (owner).
- **Risk:** LOW — one-shot, reversible.

**Not a lever:** H4 bot exclusion (0.8pp), H3 structure correlation (features don't discriminate). **H5 is now the OPPOSITE of a lever — it is a measurement correction:** the raw Rybbit bounce number should stop steering decisions; track GA4 engaged metrics alongside it (see §8). Building more internal links / tables / length (the prior squad's playbook) is the trap the correlation refutes — it will not move the crisis pages.

---

## 4. Realistic 30-Day Engagement Trajectory (ESTIMATE)

Baseline (Aug 31): 944 sessions, 90.6% bounce, 1.15 pps, 63s. Targets (AC-1..5): bounce <70%, pps ≥2.0, Google ≥50/day, sessions ≥150/day, US ≥80%.

| Week | Driver | Sessions | Bounce | PPS | Duration | Notes |
|------|--------|-----------|--------|-----|----------|-------|
| 0 (baseline) | — | 944 | 90.6% | 1.15 | 63s | — |
| 1 | Lever 1 (QA-first on 10 pages) live; GSC submit | ~960 (stabilize) | ~87% | ~1.16 | ~64s | QA-first is mechanical; bounce drops 3-5pp fast. GSC submit clears the Bing-only submission gap (no immediate bounce effect, starts Google tracking). |
| 2 | Lever 3 (crisis intent rewrites) + flagship fact-fix | ~980 | ~83% | ~1.18 | ~66s | Intent-match improves same-session re-engagement; small bounce gains, mostly on the crisis set. |
| 3 | Lever 4 (Savings hub + dead-end links) + content-credibility pass | ~1010 | ~80% | ~1.22 | ~70s | Hub wiring + dead-end revival convert a few off-site bounces into depth; duration creeps up as readers follow links. |
| 30 (landed) | all 5 levers sustained | ~1080 | **~76%** | **~1.28** | **~85s** | **Directionally toward targets but not there.** |

**Benchmarks cited:** the site's own best pages (05-lower-utility-bills 83.3%, avg-water-usage 77.8%, water-meter-leak-indicator 81.25%) are the empirical ceiling for comparable pages in this niche — a good how-to page in this genre lands ~78-81% bounce, and the AC-2 contract target is 70%. No public niche benchmark was retrievable (web search returned only dictionary/brand noise; the site's own best pages are the best proxy). **Realistic 30-day outcome: bounce ~76% (−14pp), pps ~1.28, duration ~85s.** The three hardest targets — pps ≥2.0, bounce <70%, Google ≥50/day — remain out of reach without new levers (interactive bill calculator; a genuine "lower my bill" bridge hub; GSC-driven Google indexation + Bing→Google SERP reallocation). At 85s duration, readers are engaging *more* but still leaving — the session is deepening, not completing.

**Caveat:** this is a mechanical-fix trajectory. The 30-day path assumes Bing traffic continues at current volume; it does not assume Google re-ranks (that needs the GSC submit to land and Bing→Google SERP reallocation, unverified). The engagement criteria are improving but the bounce floor (~76-78%) is set by a Bing/DDG ecosystem of genuinely low-satisfaction crisis-intent sessions — see open questions.

---

## 5. Open Questions (need data we do not have)

1. **Query-level GSC data** — H1 is UNVERIFIED because the snapshot has no referrer-query pairing. We cannot confirm Bing ranks these pages for the wrong question without GSC query impressions/CTR per URL. This is the gate on Lever 3.
2. **Scroll-depth / time-to-answer** — no ToP scroll data in the snapshot. We used pageviews/duration as proxies (ToP ≈ read-then-leave for single-page sessions). True time-to-answer (answer position as a scroll-depth proxy) would separate H2 (presentation) from H1 (intent) cleanly.
3. **Bing vs DDG SERP behavior** — the snapshot shows referrer domains but not whether Bing and DDG are serving the same intent. If Bing ranks "how to lower electric bill" and serves the complete-guide (an *action* query) but the reader wanted "why did it go up," that's an intent-mismatch signature we can't read from referrer counts alone.
4. **Bot-classification confidence** — CN @ 12.5% is treated as bots (~99% bounce). We did not cross-check CN sessions against the events referrer/browser fingerprint. If a fraction of CN is real traffic, H4's <1% share is an underestimate.
5. **Baseline sanity** — the Aug-21 "baseline" (84.7% bounce) predates the Bing spike and the SQ-016 answer-first hero. The 5.7pp gap between 84.7% and the 89%+ post-spike is a traffic-quality shift, not a content regression — the baseline is not a fair engagement target.
6. **Affiliate-traffic linkage** — the mission links bounce to stalled affiliate revenue (bouncers never reach the ~36 affiliate-shortcode articles — 34 product-box files + 2 inline, Commander-corrected from "46"). We have no conversion data to prove the bounce→revenue causal chain; it is asserted, not measured. **Actionable now: GA4 has ZERO key events configured (owner export shows an empty conversions table) — wiring `affiliate_click` as a GA4 key event closes this gap mechanically** (the Rybbit event already exists on every box/inline link; mirror it in gtag).

---

## 6. Actions Taken (executor, read-only)

- Read `snapshot.json` (last7/last30/prior7 windows, pages, channels, countries, referrers, events).
- Read `events_deduped.json` (24-session session-level sample: timestamps, referrers, page-titles, event-types).
- Read `GROWTH_LOG.md` (Entries 1-24) for before/after natural experiments (SQ-016, SQ-055, SQ-065/066) and the redirect plan.
- Read `KPI_DASHBOARD.md` (AC-1..5 completion contract, targets, baselines).
- Read `CONTENT-AUDIT-2026-08-28.md` and `FULL-CONTENT-SEO-AUDIT-2026-08-30.md` for the C1-C12 critical issues and page-level defects (C2, C3, C4, C6).
- Computed correlations (H3) and fix-leverage ranking (H2) with a local Python harness over the snapshot; verified with jq.
- Inspected `layouts/_default/single.html` and `layouts/partials/hero-image.html` to confirm the answer-first hero renders below the TOC and to confirm the crisis pages use non-canonical `<h2 id="quick-answer">` blocks (one has no QA).
- Ran web_search/web_fetch for a niche bounce benchmark; **the tools returned only dictionary/brand noise** (no usable public benchmark). The site's own best pages (78-81% bounce) and the AC-2 <70% target are used as the empirical benchmark instead. **No site file was modified.**

## 7. Recommendations

1. **Commander owns final assembly** of `ENGAGEMENT-ROOT-CAUSE-2026-08-31.md` (write discipline — I report findings only; I did not create the deliverable).
2. **Deploy Lever 1** (QA normalization + both-bad-page restructure) — the highest-confidence mechanical fix, measured in GA4.
3. **Owner: submit the GSC sitemap** — the mechanical fix for Google-0; needed before AC-4 and before H1 can be confirmed.
4. **Confirm H1 before Lever 3** — get query-level GSC data; the crisis-intent hypothesis is plausible but unverified and a rewrite is a content action, not a mechanical one.
5. **Do NOT build more links/tables/length** on these pages — the H3 correlation refutes it as the lever (the prior playbook's trap).

---

## 8. Commander Amendment Log (2026-08-31, post wave-2 + owner GA4 export)

The owner supplied a GA4 export (property `utilityexplained`, account `dreamingoffgrid`, Aug 3–30: 127 active users, avg engagement time **113.96s**/user, 725 events). GA4 measures a consent-gated subset (~127 users vs Rybbit's 2,167 sessions/30d — the cookie banner gates GA4; Rybbit is cookieless) — different populations, but GA4's engaged-session bounce is the industry-standard engagement measure the contract should have used.

**GA4 vs Rybbit bounce on the same pages:**

| Page | Rybbit | GA4 | Reading |
|---|---|---|---|
| Complete-guide flagship (24 views) | 88.3% | **29.2%** | Satisfied single-page readers; Rybbit artifact |
| 25 Proven Ways | — | **12.5%** | Excellent |
| Spike (10 views) | 93.9% | **46.2%** | Mostly satisfied |
| Gas-too-high (4) | 85.7% | **25%** | Fine |
| Keeps-rising old title (4) | — | **25%** | Fine |
| **Electric-bill-breakdown (6)** | 89.3% | **83.3%** | **Real defect — bad under both** |
| **What-is-ccf (4)** | 86.7% | **75%** | **Real defect** |
| **Billing-cycle (4)** | 90.0% | **66.7%** | **Real defect** |
| **Past-due-balance (4)** | — | **60%** | Watch |
| **Water-high 11-checks (9)** | 95.1% | **60%** | Watch |

**Verdicts changed by this evidence:**
1. **H5 CONFIRMED as the dominant driver** (was REFUTED in the file's first draft). The executor's "0 of 18 bounced sessions were long" statistic was **unreproducible — the events file carries no bounce flag** (verifier F6). GA4's 29–46% on Rybbit's 88–94% pages is decisive primary evidence.
2. **Leverage-table row errors fixed:** no 301 merges spike/water-bill-too-high into go-up (only `7-states` + `keeps-rising` redirect there — `static/.htaccess:27,32`); go-up itself is an 11-session, 0s-ToP page (an instant-exit victim of its own recent consolidation, not a 107-session crisis).
3. **Concentration corrected:** ~49.6% of sessions / ~48% of excess bounce in the top 10 (was "44.5%/60%").
4. **"No QA at all" corrected:** the page carries a non-canonical HTML QA (line 19); format variance, not absence.
5. **"46 boxed articles" corrected:** 36 files carry affiliate shortcodes (34 product-box + 2 inline). GROWTH_LOG Entry 24 corrected in kind.

**New findings from the GA4 export:**
- **GA4 sources mirror Rybbit:** bing 50 / ddg 30 / direct 28 / yahoo 23 / **google 8** sessions — Google ≈ 5.5% everywhere → the GSC-submission fix is confirmed from a second measurement system.
- **Direct = 28 GA4 sessions (19%)** and 32.3% of Rybbit sessions — unusually high for a 3-week-old site; likely Bing-redirect chains stripping referrers + bot load. Open question.
- **Cities are overwhelmingly real US metros** (Chicago 6, NY 6, Atlanta 5, Indianapolis 4…) with a small international long tail — supports "human US traffic" (H4 refuted).
- **Zero GA4 key events** — no conversion tracking in GA4. Wire `affiliate_click` as a key event (the gtag event already fires via the Rybbit attribute pattern).
- **Avg engagement time 113.96s** (GA4, consented users) vs Rybbit's 63s session duration — the consenting population reads ~2× longer; engaged readers are real.
- **Traffic mix note:** GA4 shows both the current flagship title ("25 Proven Ways", 8 views) and the old ("Complete Guide (2026)", 24 views) attracting traffic — old titles/URLs still float in Bing's index; consistent with the dead-URL cleanup lever.

**Amended recommendation order:**
1. **Re-baseline the Completion Contract** — AC-2/AC-3 measured in Rybbit raw bounce are unreachable-by-definition for a one-answer site. Track GA4 bounce (target <55%) + engaged sessions instead; keep Rybbit for volume/US-share only. *(Owner decision.)*
2. **GSC sitemap submission** (unchanged, mechanical, gates AC-4 and the H1 test).
3. **Lever 1 re-scoped:** QA format normalization + lead restructure on the 5 both-bad pages — measured in GA4.
4. **Wire GA4 `affiliate_click` key events** — closes the bounce→revenue measurement gap (open question 6).
5. **Dead-URL / instant-exit cleanup** (lieutenant's 16.6% layer: retired URLs still Bing-indexed, `/tags/page/N/`, `.md` paths; `go-up`'s own 0s-ToP pattern).
6. **Flagship fact-fix (C4)** and **H1 intent rewrites** unchanged from §3, sequenced after GSC data arrives.
