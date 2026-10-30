# utilityexplained.com — Four-Lens Master Audit (SEO / AI-GEO / Amazon Associates / User Intent)

**Date:** 2026-10-30 · **Data:** Rybbit API live pull (Oct 1–30, site 4987), live-site curls, repo inspection, full-page visual audit (Clawbrowser desktop), SERP sampling, Amazon outbound events.

---

## 0. Baseline (all verified today)

| Metric | Value | Source |
|---|---|---|
| Sessions / 30d | 4,105 (4,286 pv, 3,455 users) | Rybbit overview |
| Bounce / duration | 84.1% / ~185s | Rybbit overview |
| Search referrals | DDG 2,754 · Bing 2,051 · Yahoo ~798 · **Google 654** · Ecosia 185 | Rybbit referrers |
| Google MoM | 120/30d (Sep 20 read) → **654/30d (Oct)** = +445% | Entry 30 vs today |
| AI channel | 29 sessions (Copilot 9, ChatGPT 6, Gemini 3, Claude 2, Perplexity 1) | Rybbit referrers |
| AI crawlers | 732 requests/30d (crawl access confirmed working) | Rybbit bots |
| Geo | US 73.5% · CN 10.5% (noise) · GB 2.3% · CA 2.1% | Rybbit countries |
| Bot share | 30.5% of events | Rybbit bots |
| Articles | 140 · median 1,888 words · 1 thin (blog index only) · 0 orphans | repo scan |
| Schema | Article 100% · FAQPage 90/140 (64%, auto-emitted via head.schema) · Breadcrumb 508 pages · WebSite/Org home · HowTo 0 · Speakable 0 | live HTML verify |
| Monetization | 78/140 pages carry boxes/links · 235 ASIN deep links, 0 search links, 100% tagged · build gate live | built-tree grep |
| Affiliate clicks / 30d | 126 (Kill A Watt 33 + Emporia Vue 3 23 + Vue3 cart 11 = 53% of all clicks on 3 ASINs) | Rybbit outbound |
| Earnings | ~$10.26/mo · 6 orders, all off-site relay · on-site tagged funnel 0/78 (PM investigation 10/28) | PORTFOLIO-PM |

---

## 1. SEO lens — grade B+ (mechanics done; now a growth-stage problem)

**Working.** 169-URL sitemap with honest lastmods (10-29 waves present). Taxonomy pages correctly not built (no thin tag pages). Aliases are canonical-correct meta-refresh stubs. 0 orphan articles, min 19 inbound links/article (Entry 30), interlink hardening shipped 10-29. GSC verified, sitemap submitted 9/7. Quick Answers on 139/140 articles. Title/meta hygiene good. Performance healthy (63KB CSS, 4KB JS, WebP heroes, fetchpriority).

**Gaps found (ranked):**

1. **Google is arriving — don't misread it.** 654 referrals vs Bing-ecosystem ~5,600. The Sep diagnosis ("ranking suppression, 9-month-old domain") is aging out. The metric to watch weekly is Google-referral trend; the levers now are freshness on winners + more brand/searcher-behavior signals, not more mechanical work.
2. **FAQ coverage at 64%.** 90/140 articles have FAQ sections with auto-emitted FAQPage JSON-LD (verified live; `faq-schema` shortcode is a no-op — schema comes from head.schema reading the page store). 50 articles have no FAQ section at all (content fix, prioritize by traffic). FAQ blocks are simultaneously snippet bait and AI-answer bait.
3. **Head-term reality check.** "average electric bill by state" is an EIA-data arms race (askento, statecalc, bill.ninja, energyfactbook, electricityplans — all 50-state tables, monthly refresh, some with calculators). "why is my electric bill so high" is owned by utilities + Consumer Reports + retail suppliers. **The open flank is state × utility-type long tail**: every competitor is electric-only. "average water bill in [state]", "gas bill [state] winter" — nobody owns these systematically. UE has the EIA pipeline (data/stats.yaml) to build 50×2 pages honestly.
4. **The state article itself is prose-heavy** where competitors ship machine-quotable tables. Restructure into per-state anchored table blocks (also the AI play — see lens 2).
5. **Publishing cadence gaps** (Feb/Apr/Jun/Jul = zero). Consistency beats bursts for a young domain.
6. **Alias stubs are meta-refresh, not 301** — canonical is right, but a .htaccess 301 layer would pass users instantly (Rybbit shows 127 pv landing on one stub with 5.4s dwell — that's friction, not a redirect).
7. Calculators (1) invisible on homepage and underused in SERP capture vs competitor tool suites.

---

## 2. AI / GEO lens — grade C+ (access solved; citation assets under-built)

**Working.** robots.txt allows everything (no AI-bot blocks). llms.txt exists (151 lines) and is updated per wave. AI crawlers hit 732 req/30d. About/editorial-team/methodology/corrections pages are honest and complete — exactly the transparency AI trust systems score. Organization-author schema consistent.

**Gaps found (ranked):**

1. **llms.txt is a bare link list.** (a) Zero descriptions — the spec's most valuable field for an LLM deciding what to fetch; (b) blog-articles-only — hubs, glossary, calculator, lower-your-bills, methodology are all missing; the glossary and definitional pages (CCF, therms) are precisely what AI engines cite. (c) No llms-full.txt equivalent for full-corpus ingestion.
2. **The state-data page is UE's single biggest citation asset, and it's not built like one.** AI engines quote clean tables with stated vintage + methodology. energyfactbook/statecalc are built exactly that way. UE has the same EIA pipeline + the all-utilities differentiator — restructure into quotable tables with "data vintage: [month], source: EIA [table]" labels.
3. **FAQ coverage 64%** (50 articles lack FAQ entirely — content gap, not schema gap; schema emission is automatic).
4. **No Speakable / no marked answer blocks.** Quick Answers are plain `<h2 id=quick-answer>` paragraphs. A boxed, semantically-marked Quick Answer is more liftable by both scrapers and LLMs.
5. **AI traffic is 0.3% (29 sessions)** — measurement baseline exists; target 150/30d by end of January. Growth path: citation-shaped assets (tables, glossary, FAQs) + llms.txt v2 + being present where AI engines retrieve (the off-site Amazon-URL relay already proves AI engines are re-serving UE's schema URLs — same mechanism serves citation).
6. Entity presence beyond the site (Wikidata, Reddit threads, YouTube) = 0. Reddit is owner-gated (his accounts only); a weekly "answer a utility question" draft queue for the owner is the legal, compounding play.

---

## 3. Amazon Associates lens — grade B− (funnel built; buyer intent inverted)

**Working.** 235 ASIN deep links, zero search links, 100% tagged with a build gate that fails on any untagged Amazon URL (including JSON-LD). Per-box FTC disclosures + rel=sponsored. Cart-add strategy deployed on winter wave (4 live boxes, 11 clicks/30d already on the Vue 3 cart link). Product bench research (dossier) with availability re-checks. The litwd-20 stray-tag leak (6 clicks) is gone from source — legacy of pre-10/28 pages; monitor Amazon "Other" next cycle.

**Gaps found (ranked):**

1. **62/140 articles carry zero product placements** — including real-traffic pages: how-sewer-charges-work (230 pv), complete-guide-understanding-utility-bill (163 pv), 01-how-to-read-your-electric-bill (140 pv), plus most winter-cluster HVAC pages. Free upside on existing traffic; the traffic mix shifted after the last fix wave, so the gap MOVED.
2. **The 0/78 on-site vs 14.6% off-site conversion inversion** (PM 10/28) needs a hypothesis test, not more density: on-site clickers are mid-diagnosis (browse), relayed visitors arrive pre-sold. Fixes that match the diagnosis: decision-stage content + cart boxes on the pages where the diagnosis ENDS (spike → cause found → "here's the fix"), price anchoring on CTAs, and a post-cause-#1 module on the water page (highest anxiety → solution moment).
3. **CTAs have no price anchoring.** "Check current price on Amazon" ×N identical, no numbers. Honest bands ("~$30 · ~$170") lift click intent; the no-on-page-prices rule predates the traffic — revisit with banded (not exact) prices, which stay honest vs. volatility.
4. **Click concentration risk:** 53% of clicks on 3 ASINs, all measurement gear at 3% / ~$0.50–$5 commission. The water ladder (Govee $60 → Flume 2 $199–269 → Moen Flo $550+ = $6–20/order) is UE's highest-AOV path and its strongest cluster — ladder depth is under-placed beyond the entry rung.
5. Winter wave is the right shape (thermostats $130–250). Extend cart=true beyond the 4 boxes to decision-stage boxes on top-10 traffic pages.
6. Track EPC per placement format (sidebar restyle 10/04 vs boxed cards) — the Rybbit format props already exist; read out at 30d.

---

## 4. User intent & UX lens — grade B (excellent architecture; above-fold friction)

**Working.** Answer-first structure, honest stacking caveats, verified math (vision audit re-checked the arithmetic on the flagship page — correct), decision-routing ("Pick your route", spike-triage), dated reviews, "2 sources cited" transparency, breadcrumbs, fast pages. Content genuinely outclasses the utility/brand pages that own the head terms.

**Gaps found (ranked):**

1. **Above-fold friction stack on both flagships:** cookie banner + affiliate-disclosure box + in-column TOC accordion push the Quick Answer below the fold. Desktop shows TWO TOCs (sidebar rail + in-column accordion). The answer should win the first viewport.
2. **Quick Answer is typographically invisible** — same style as body copy. Box it: snippet bait, skimmer bait, AI-lift bait, one change.
3. **Glyph defect on the flagship water infographic:** water-leak-priority-quadrant.webp reads "00+/MO" (missing "$1") on the running-toilet panel — the page's #1 stat is broken. Fix now.
4. **Cookie consent parity:** filled "Accept all" vs ghost "Decline" (asymmetric dark-ish pattern), banner overlays content. Equalize weights (also a compliance-hygiene item the portfolio credibility audit standard checks).
5. Meta row (byline/date/sources) is low-contrast on the sage hero — WCAG borderline on the two flagship pages.
6. Homepage: no email capture, calculators invisible, hero right half empty, "Start with your bill →" is ambiguous (promises a tool, delivers articles). Missing: state/ZIP entry point that feeds the state-data page.
7. Copy nit: dek says "17 proven steps" vs body "20+ proven ways"; unlabeled filter pills on the electric guide; sidebar rail goes thousands of px dead below the pick (a sticky element — email capture or next-guide — belongs there).

**Artifacts dismissed after verification (do NOT re-fix):** "blank product images" = lazy-load capture artifact (all product images 200 OK live; 17 loading=lazy attrs); "zero ads" = consent-gated render (12 ad markers in HTML); sidebar "under-styled" pick = deliberate NN/g-informed restyle (10/04) with tracking — judge on the 30-day CTR readout, not on style opinion.

---

## 5. Prioritized roadmap

**P0 — mechanical, ship now (this session):**
1. llms.txt v2: descriptions per entry + add hubs, glossary, calculators, lower-your-bills, methodology, disclaimer (generator script so future waves auto-update).
2. Fix water-infographic glyph ($1 missing).
3. Cookie consent button parity + banner overlay fix.
(FAQ schema NOT a P0 — auto-emission verified; true FAQ gap is the 50 no-FAQ articles → P2.)

**P1 — this week (existing-traffic upside):**
5. Product placements on unmonetized traffic pages (sewer-charges, complete-guide, 01-read-bill first).
6. Box the Quick Answer sitewide (theme partial).
7. Price bands on product-box CTAs.
8. Restructure average-utility-bills-by-state into quotable, vintage-labeled tables + per-state anchors.
9. Cart boxes on decision-stage spots of top-10 pages.
10. Desktop TOC dedupe (sidebar only; accordion mobile-only).

**P2 — this month (compounding):**
11. State × water/gas long-tail page system (the electric-only competitor flank) — pilot 5 states.
12. FAQ sections for the 50 no-FAQ articles, top-traffic first.
13. .htaccess 301 layer for alias stubs.
14. Homepage: email capture, calculator surfacing, state/ZIP entry.
15. Winter wave 3 (Jan bill-shock cluster: "why is my heating bill so high in January" already exists — extend to furnace/heat-pump decision pages).

**P3 — quarter:**
16. Google authority: the 654 referral trend is the KPI; brand-query + freshness cadence + owner Reddit draft queue.
17. AI citation KPI: 29 → 150 sessions/30d by end of January; llms.txt v2 + tables + FAQ as the levers.
18. Water ladder depth (Flume/Flo decision content), EPC-by-format readout, second calculator (water bill).

**KPIs:** Google referrals (654 → 1,500), AI sessions (29 → 150), affiliate clicks (126 → 300), cart-add clicks (11 → 40), FAQPage coverage (52% → 90%), on-site tagged first order (0 → 1).

---

## 6. Source artifacts

- Rybbit pulls: ~/.hermes/cache/scratch/ue-audit/ry_*.json
- Screenshots: ~/.hermes/cache/scratch/ue-audit/shot-*.png (+ crops)
- Visual audits: vision analyses of home, electric top/mid, water top
- SERP samples: "average electric bill by state 2026", "why is my electric bill so high all of a sudden"
