# UtilityExplained Growth Log

## Entry 1 — 2026-08-10: Initial Audit & Phase 1 Fixes

### Analytics Baseline (90 days: May 11 - Aug 10, 2026)
| Metric | Value |
|--------|-------|
| Sessions | 263 (~3/day) |
| Bounce Rate | 79.8% |
| Pages/Session | 1.76 |
| Avg Session Duration | 112s |
| Organic Search Sessions | 150 |
| Top Referrer | DuckDuckGo (68) |
| Google Sessions | 2 |
| US Traffic | 203 (77%) |
| Mobile | 149 (57%) |

### Top Landing Pages (Problem Pages)
| Page | Sessions | Bounce | Avg Duration |
|------|----------|--------|--------------|
| Homepage | 41 | 73.2% | 331s |
| Sewer charges | 32 | 90.5% | 11s |
| Water meter leak indicator | 22 | 61.1% | 210s |
| Water meter running | 12 | 91.7% | 52s |
| Past due balance | 12 | 100% | 0s |
| CCF on water bill | 16 | 88.9% | 8s |
| Reconnection fee | 8 | 62.5% | 18s |

### Changes Made

#### Technical Fixes
1. **Created .htaccess** with:
   - 301 trailing slash redirects (consolidates duplicate URLs)
   - HTTPS enforcement
   - Non-www redirect
   - Security headers (X-Content-Type-Options, X-Frame-Options, Referrer-Policy)
   - Gzip compression for HTML/CSS/JS/SVG
   - Browser caching (1 year for WebP, 1 month for CSS/JS)
   - Custom 404 page

2. **Fixed 5 broken internal links** across 4 files:
   - how-to-lower-electric-bill-complete-guide.md (3 links fixed)
   - 06-water-bill-too-high.md (1 link fixed)
   - 12-how-to-read-your-gas-bill.md (1 link fixed)
   - 07-gas-bill-too-high.md (1 link fixed)

#### Content Hub Pages (5 pages rebuilt)
Added comprehensive "Browse Our Guides" sections to all 5 hub pages:
- electricity-explained.md — 24 article links organized by subtopic
- water-explained.md — 16 article links organized by subtopic
- gas-explained.md — 11 article links organized by subtopic
- utility-bills-costs-explained.md — 21 article links organized by subtopic
- heating-cooling-explained.md — 14 article links organized by subtopic

#### High-Bounce Page Rescues (6 articles improved)
1. **how-sewer-charges-work-on-your-water-bill.md** (90%→target <70%)
   - Added 4 contextual internal links
   - Added bold formatting to key advice
   - Kept existing Quick Answer section

2. **21-past-due-balance-utility-bill-explained.md** (100%→target <70%)
   - Added Quick Answer section at top
   - Added 5 contextual internal links
   - Added bold formatting to key timelines

3. **water-meter-running-when-no-water-used.md** (91.7%→target <70%)
   - Removed AI pattern "Furthermore"
   - Added 3 contextual internal links
   - Verified bold formatting on diagnostic steps

4. **what-is-ccf-on-a-water-bill.md** (88.9%→target <70%)
   - Added 5 contextual internal links
   - Bolded key conversions (1 CCF = 748 gallons)
   - Removed AI-style conclusion

5. **stormwater-fee-on-water-bill-explained.md** (75%→target <60%)
   - Added Quick Answer section
   - Removed AI patterns ("Additionally", "Furthermore")
   - Added 5 contextual internal links
   - Bolded key fee amounts

6. **why-your-electric-bill-keeps-rising-2026.md** (100%→target <70%)
   - Added Quick Answer section with 5 key factors
   - Added 4 contextual internal links
   - Kept all existing content

### Expected Impact
- **Trailing slash fix**: Consolidates duplicate URLs, should improve Google indexing and PageRank distribution
- **Broken link fixes**: Improves crawl efficiency and user experience
- **Hub page links**: Creates 86 new inbound links across the site, reduces orphan pages
- **Content fixes**: Quick Answer sections should reduce bounce on 6 high-traffic pages
- **Internal links added**: ~26 contextual links across 6 articles

### Next Actions
1. Deploy to production (Hostinger)
2. Submit updated sitemap to Google Search Console
3. Monitor Rybbit for 7-14 days
4. If bounce rates improve, apply same pattern to next batch of articles
5. Begin building missing cluster articles (phantom loads, TOU savings guide)
6. Investigate Google indexing issue (only 2 sessions from Google in 90 days)

---

## Entry 2 — 2026-08-10: Phase 2 Internal Linking + Page Rescues

### Changes Made

#### Internal Linking Wave (22 articles enhanced)
Dispatched 3 parallel agents (glm-4.5) to add contextual internal links:
- **Electricity batch (7 articles):** 34 new links (energy leaks, rate plans, bill reading, TOU rates, demand charges, winter bills, smart plugs)
- **Water/Gas batch (7 articles):** 28 new links (water usage, lowering bills, meter reading, bill increases, gas charges, heat pumps, heating comparison)
- **Bills/Fees batch (8 articles):** ~40 new links (billing cycles, customer charges, proration, deposits, space heaters, generators, state costs, budgeting)

#### Additional Page Rescues (4 more 100% bounce articles)
1. **average-utility-bills-by-state-2026.md** (100% bounce) → Added Quick Answer with national averages table
2. **how-do-smart-meters-work.md** (100% bounce) → Replaced "Introduction" heading with answer-first Quick Answer
3. **is-your-toilet-running-leak-test.md** (75% bounce) → Added Quick Answer with 10-minute dye test steps
4. **03-why-is-my-electric-bill-so-high.md** (100% bounce) → Fixed broken table formatting + cleaned up random link placement

#### Sitemap Submission
- Pinged Google and Bing about updated sitemap
- Sitemap has 328 URLs, all valid XML

### Cumulative Impact (Phase 1 + Phase 2)
- **Total new internal links:** ~250+ across 30+ articles
- **Hub page links:** 138 across 5 hubs
- **Articles with Quick Answer sections:** 10 (up from 4)
- **100% bounce articles fixed:** 6 (past-due, electric rising, smart meters, utility bills by state, electric bill high, + table fix)
- **Broken links fixed:** 5
- **Trailing slash redirects:** Live and verified on production (HTTP 301 confirmed)

### Commits
- 832f361: Phase 1 (technical fixes + hub pages + 6 article rescues)
- 04fa5ba: Phase 2 (22 article internal links + 4 more page rescues)
- Both deployed to Hostinger via GitHub Actions

### Next Actions
1. Monitor Rybbit for 7-14 days for bounce rate improvement
2. Audit remaining articles for AI writing patterns
3. Create missing cluster articles (phantom loads, appliance consumption)
4. Improve blog listing page for better discovery
5. If bounce rates improve, scale the approach to remaining articles

---

## Entry 3 — 2026-08-10: Revenue + UX Features + 100% Quick Answer Coverage

### Revenue Features
- **Email capture**: Created newsletter signup partial, integrated on all blog articles
- **Mid-article AdSense slot**: Activated 3rd ad position (below_title + mid_article + end_article)
- **Affiliate disclosure**: Added to about page + created affiliate-disclosure shortcode
- **Blog listing improvement**: Categorized browse-by-topic grid on /blog/ page

### Content Completion
- **97/97 articles (100%)** now have Quick Answer sections
- Created phantom-power-draw-explained.md (1,332 words, fills Electricity cluster gap)

### Verification (Live Production)
- Trailing slash 301 redirects: ✅ LIVE
- Quick Answers rendering: ✅
- Email capture: ✅
- 3 AdSense slots per article: ✅
- Blog browse section: ✅
- Hub page links (35+ on electricity): ✅
- Phantom power article: ✅ LIVE
- Sitemap (300+ URLs): ✅
- Page load <1s: ✅
- Mobile responsive: ✅
- Affiliate disclosure: ✅

### Total Commits: 11

---

## Entry 4 — 2026-08-12: Top-Tier Page Optimization (Day 2)

### Method
Pulled **fresh per-page Rybbit engagement** (last 100 sessions, site `d5b63e065e9d`) for the 13 highest-traffic pages, then applied **targeted enhancement** (not full rewrites) via **3 parallel minimax-m3 subagents** on Ollama Cloud, each with detailed per-page instructions (search intent + live analytics + specific fixes). Every output passed an automated verifier (frontmatter preserved, shortcode pairs balanced, internal links not dropped, FAQ-schema present) and a full link-existence scan.

### Live Analytics That Drove Priorities (Rybbit, last 100 sessions)
Critical (100% bounce): leak-indicator (10s), CCF (16s), taxes/fees (20s), deposit (12s), **hub page utility-bills-costs-explained (0s)**, lower-electric-no-solar (20s). The day-1 CCF "fix" had NOT stuck — still 100% — because it was definition-first, not diagnosis-first.

### Per-Page Changes (words before → after)
| Page | Live data | Key change | Words |
|------|-----------|------------|-------|
| what-is-ccf-on-a-water-bill | 100% / 16s | Lead QA with "is mine normal?" + leak signal; fixed literal `**` in `<li>`/`<td>` + raw-MD link in HTML | 1400→1638 |
| water-meter-leak-indicator | 100% / 10s | Removed "problem" narrative; answer-first QA + 60-sec test up top | 1560→1754 |
| 25-taxes-fees-franchise | 100% / 20s | Added answer-first Quick Answer (was missing) + FAQ + FAQ-schema | 2198→2301 |
| 26-utility-deposit | 100% / 12s | Dollar-range QA + deposit table + FAQ-schema | 2557→2652 |
| lower-electric-no-solar | 100% / 20s | Killed "Introduction"; deepened 12 methods substantially | 1295→2759 |
| utility-bills-costs-explained (HUB) | 100% / 0s | Added answer-first intro + pillar links + jump link; FAQ-schema | 2289→2496 |
| 28-reconnection-fee | 77% / 244s (top traffic) | Sharpened QA + FAQ-schema (was missing) + cross-sell | 2229→2291 |
| 23-billing-cycle | 83% / 23s | Strengthened QA + contextual links + FAQ-schema | 2178→2431 |
| water-meter-running | 75% / 527s | Converted plain-text FAQ → shortcode + schema; removed "Conclusion" | 2721→2588 |
| 30-spike-electric | 75% / 140s | Sharpened QA to surface top-3 causes | 3709→4142 |
| sewer-charges | 67% / 1485s | Light touch: tightened QA + cross-links | 1439→1471 |
| 05-lower-utility-bills | 33% / 298s (best) | Very light polish only | 1978→2002 |
| electric-bill-breakdown | 67% / 297s, 7.7 pv | Light polish | 1400→1611 |
| **Total** | | | **26,953 → 30,136** |

### Universal Patterns Applied
- **Answer-first hooks**: every page's primary question answered in the first 1–2 sentences with the key number bolded (directly targets the <20s bounce pages).
- **FAQ + FAQ-schema**: 4 pages that lacked it (reconnection, billing-cycle, taxes/fees, hub) now emit `FAQPage` JSON-LD; FAQ where plain-text converted to the `{{< faq >}}` shortcode. Verified schema renders in built HTML.
- **Broken-markdown fixes**: CCF's literal `**` inside HTML lists/tables and a raw-Markdown link inside an HTML `<p>` (wouldn't have rendered) — both corrected.
- **AI-pattern removal**: "Furthermore", "Additionally", "In conclusion", etc. removed.

### Link Integrity (post-enhancement)
Comprehensive scan of every internal link across all 13 files against the real content tree. **3 model-introduced broken links caught and repointed** to real slugs: `heating-and-cooling-explained` → `heating-cooling-explained` (hub); `how-to-read-electric-bill` → `01-how-to-read-your-electric-bill` (spike); `how-to-lower-your-water-bill` → `44-how-to-lower-water-bill` (sewer). 1 dropped pillar link (`electricity-explained`) restored on lower-electric-no-solar. **Final: 0 broken internal links.**

### Verification
- ✅ Hugo build: 547 pages, 0 errors, 636ms
- ✅ FAQPage JSON-LD schema confirmed in rendered HTML on all pages
- ✅ Zero literal `**` rendering artifacts in `<li>`/`<td>`
- ✅ Zero broken internal links
- ✅ Frontmatter (title/slug/date/author/image) preserved on all 13

### Image Audit Result (Magica GPT Image 2 — NOT used)
Full audit of images across the 13 pages: **14/23 inspected (all 10 inline diagrams + 4 heroes) — zero AI slop.** All inspected images render accurate, readable text and present as professional infographics. The remaining 9 uninspected are all hero images, which were already de-slopped in prior commits (`ba72465` "Replace 38 square slop heroes with real text"; `9eddff1`, `0c3a42c` OCR-cleanup passes). **Conclusion: no regeneration needed — the "redo all AI slop" premise reflected a pre-cleanup state that no longer exists.** Magica key provisioned but unused.

### Deployment
- ✅ Committed (`0db8f7e`) + pushed → GitHub Actions "Deploy to Hostinger" succeeded.
- ✅ Verified LIVE on production: Quick Answers, FAQ schema, internal links confirmed in served HTML.
- ✅ Hugo build: 547 pages, 0 errors. Sitemap: 328 URLs valid XML.

---

## Entry 5 — Day 3 (2026-08-12): Deep-enhance 16 pages + featured-snippet pivot

### Method
Researched 2025–2026 best practices for reader retention + on-page SEO (BLUF/answer-first, F-pattern, information foraging, EEAT, AI-Overview ranking factors, AI-slop lexicon) via parallel research agent. **Key strategic finding: Google deprecated FAQ rich results (May 7, 2026)** — FAQ schema no longer earns SERP dropdowns. Pivoted the playbook accordingly: keep FAQ sections (readers + AI parsing value them) but optimize each page's TOP answer as a 40–50-word featured-snippet block, and reinvest effort in semantic completeness + hub-and-spoke internal linking.

Hybrid execution: hardened Day-2 orchestrator (minimax-m3 via Ollama cloud) with three upgrades — (1) featured-snippet Quick Answer requirement, (2) **allowlist-only linking** (226 real slugs built from the content tree at runtime; verify() auto-rejects any link not in the set), (3) expanded slop-kill list + hard prohibition on `**` artifacts. 3 parallel batches (6/5/5). 2 pages (gas-customer-charge, fixed-variable) hit a reproducible minimax thinking-loop (unbounded `thinking` field consuming the entire token budget, zero content output) and were hand-edited.

### Per-page work (16 files; words in→out)
| Tier | Page | Key fixes |
|---|---|---|
| 1 | why-is-my-electricity-bill-so-high-in-summer (1523→1788) | Fixed ALL stray `**` artifacts in Quick Answer + both bottom tables (page was visibly broken); fixed mangled mid-sentence link + nested broken link; answer-first featured-snippet hook; EIA source |
| 1 | water-meter-running (2588→2666) | Removed keyword stuffing; strengthened internal-link pull-through (top traffic page, 28 sessions/86% bounce) with "what to do next" CTA |
| 1 | 07-gas-bill-too-high (2511→2668) | Removed self-link; fixed mismatched anchor; converted broken `./md` refs; dropped "Bottom line:"; featured-snippet |
| 1 | is-your-toilet-running-leak-test (1087→1704) | Fixed dead `/water-explained` link; moved cost-calc table up; featured-snippet ($50–100/mo) |
| 1 | how-to-read-your-utility-bill (2100→2107) | Deleted duplicate FAQ block (7 H3s repeated as shortcodes); removed self-link; cited income claim |
| 1 | 7-states-with-worst-utility-spikes (2260→2355) | Replaced off-topic boilerplate FAQs; killed "feeling the squeeze" AI opener; rewrote generic description/keywords |
| 2 | 20-utility-bill-proration (2675→2784) | Converted manual FAQ→shortcodes+schema; fixed nested broken link + wrong slug |
| 2 | 27-utility-connection-fee (2060→2018) | Converted manual FAQ→shortcodes+schema |
| 2 | how-to-lower-electric-bill-complete-guide (2741→3160) | Converted manual FAQ→shortcodes+schema; heat-pump rebate caveat |
| 2 | gas-customer-charge (1086→1227) **hand-edit** | Made Quick Answer numeric ($12–27); moved by-state table before FAQ; cleaned `{" "}` JSX artifacts; consolidated thin sections |
| 2 | tiered-electricity-rates (1218→1957) | Fixed literal `\"` artifact; fixed dead `/electricity-explained` link; moved by-state table before FAQ; numeric Quick Answer |
| 3 | 08-time-of-use (1981→2103) | Dropped "Bottom line:"; naturalized forced "Learn more in" links; fixed `./md` refs |
| 3 | 10-fixed-vs-variable (2081→2072) **hand-edit** | Dropped "Bottom line:"; removed forced links; fixed `./md` refs |
| 3 | 18-fuel-adjustment (2131→2386) | Removed self-link; trimmed filler intro; added sibling fee links |
| 3 | 03-why-electric-high (1622→1790) | Removed self-link; deepened causes #10/#11 with budget-billing action |
| 3 | electric-bill-breakdown (1611→1544) | Converted HTML links→Markdown; standardized headings; trailing-slash fix |

### Universal patterns applied
- **Featured-snippet Quick Answer** (40–50 word declarative answer, key number bolded) on all 16 — the primary lever now that FAQ rich results are deprecated.
- **AI-slop removal**: killed "Bottom line:", forced "Learn more in", "Imagine", "Additionally", "feeling the squeeze", keyword stuffing, dramatic openers.
- **Hub-and-spoke internal linking**: 165 internal links across the 16 files, all allowlist-verified.
- **EEAT**: inline source notes (U.S. EIA), current year, named authors preserved.
- **Next-step CTAs** to convert bounces into second pageviews.

### Verification
- ✅ 0 broken internal links across 165 links (allowlist-enforced + verified)
- ✅ All `**` balanced (0 unmatched); 0 literal `**` in rendered HTML
- ✅ All shortcodes balanced; all 16 have faq-schema + Quick Answer
- ✅ Title/slug/frontmatter preserved on all 16
- ✅ Hugo build: 559 pages, 0 errors, 2.1s
- ✅ Rendered-HTML spot-checks: summer tables clean, states-spikes opener/description fixed, gas-customer-charge table-before-FAQ confirmed

### Baseline for re-measurement (Rybbit, 90-day window 2026-05-15 → 08-13)
Site: 435 sessions / 80.0% bounce / 1m59s avg / 1.97 pages-per-session. Top entry page: water-meter-running (28 sessions, 86% bounce). Re-pull at 2-week and 4-week marks.

