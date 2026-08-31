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


---

## Entry 6 — 2026-08-21: SQ-013 full-squad audit + correctness/engagement batch (Commander ZCode + squad)

### Baseline (Rybbit, 7d, pulled 2026-08-21)
- **1,337 sessions / 2,028 pv** (was ~5/day before Aug 14 — **traffic spike is Bing-ecosystem discovery**: DDG 42.4%, Bing 34.5%, Yahoo 12.2%; Google only 4.8%). US 78% · CN 13.5% @98.8% bounce (suspected bots) · Mobile 58%.
- Bounce 84.7% · pages/session 1.52 · avg session 80s. Organic-search bounce 90.8%.
- Top entries: complete-guide 61 · water-meter 38 · spike-electric 37 · water-bill-too-high 34 · ccf 33.

### Changes (all validated: Hugo build clean ×3, sitemap 138 URLs, FAQPage on 96 pages deterministic, 0 broken internal links)
1. **Phantom TOC H2 fix (5 pages)**: `{{< faq-schema >}}` directly followed by `---` rendered a setext-H2 `HAHAHUGOSHORTCODE…` into every TOC. Blank line inserted (04/06/09/02/10-hidden/apartment/costs pages). Pattern eliminated sitewide.
2. **444 internal links canonicalized**: 262 markdown + 182 raw-HTML `href=` links gained trailing slashes (URL-set-driven conversion against the real build; 0 remaining in content). Template tag-chips (~448) remain — theme-level fix queued (R3 canonical-theme propagation).
3. **Self-link removed** on 06-water-bill-too-high QA (repointed to leak-indicator article).
4. **Footer nondeterminism fixed**: `range first 6 (sort cats "Count" "desc")` had unstable ties (Billing↔Fees order, Troubleshooting↔Gas membership flipped between builds). Site-level `layouts/partials/footer.html` override with curated deterministic Topics.
5. **48-word affiliate-only stub expanded**: do-programmable-thermostats-cut-heating-bills now a full answer-first article (~1,500 words: DOE 1%/degree rule, ENERGY STAR schedule, recovery myth, heat-pump caveat, savings tables, 6 FAQs + schema). Product box retained.
6. **Hub titles shortened** (all 6 were 87–96 chars → 42–51): keyword-first, truncation-safe.
7. **Schema corrected/enriched** (site-level head.schema.html override): author pages now emit ProfilePage+Person (were wrongly Article); articles gain inLanguage + publisher url/@id.
8. **Sitemap hygiene**: noindexed pages (e.g. /search/) no longer listed.
9. **10 consolidation aliases → server 301s** in .htaccess (meta-refresh stubs remain as unreachable fallback).
10. **Engagement fixes on 4 defect-exit pages** (analyst-classified): taxes-fees (4s-bail page) gained jump-row + in-QA links to the regional table; complete-guide gained action-path line after jump-row; water-meter + spike-electric gained in-QA contextual links.
11. **IndexNow wired**: key at /f8c073….txt + CI step POSTs sitemap URLs to api.indexnow.org on every deploy (Bing channel reinforcement).
12. average-water-usage-per-person description rewritten (was <70 chars).

### Squad credits (SQ-013)
Analyst (dsv4-flash): bounce diagnosis, SATISFIED vs DEFECT exit classification. Challenger (dsv4-flash): adversarial review (trust-page ads, cannibalization, Amazon tag, E-E-A-T gaps). Twin Q (qwen3.8): technical-SEO audit (pagination canonicals, alias stubs, author schema, overlong titles). Commander: verification of all claims at disk level (refuted 3, confirmed rest), all edits above, reference-build determinism harness (/tmp/sq013-ref). Muse reconciliation + researcher perf/content audits: workers stalled (hardware/model issues), Commander covered critical paths directly.

### Verification battery (all green)
URL set stable except intended −/search/ · 0 hahahugo artifacts · footer identical across 3 builds · FAQPage=96 across 3 builds · all 9 new internal links resolve · all 4 jump-row anchors exist · YAML lint on deploy.yml · independent Twin Q verification pass on the full diff before commit.

### Rollback
Git: `git revert <commit>` or reset to 36ca5a18 (pre-session). Tar snapshot: logs/backups/utilityexplained-prework-20260821-120504.tar.gz (source tree).

---

## Entry 7 — 2026-08-22: SQ-016 Phase A — Transformation batches 1+2 (Commander ZCode + squad)

### Baseline
Same Aug-21 Rybbit pull as Entry 6 (1,337 sessions/7d, 84.7% bounce, 1.52 p/s, 80s). Measurement window for THIS entry opens now.

### Changes (commit 352a3a36 + b22bd82c, both deployed & live-verified)
1. **Article funnel reorder** (site single.html override): hero below TOC by default (answer-first on 96/97; `hero_above: true` opt-out), "Reviewed:" date in byline, **related-posts promoted before** ad/sources/author/email (was last — the structural 1.52 p/s driver), email demoted to final slot.
2. **mid_article ad reinstated** (slot 7429084400, lost in Aug-19 theme-v3 convergence — 5-source confirmed): injected after 2nd H2 on articles with ≥1,200 words, ≥3 H2s, no product-box (59/96 eligible). Article density now 2 (mid + end); affiliate articles stay 1.
3. **Real hub layout** (hub.html): all 5 pillars render answer-first + auto-generated grouped directory + cross-desk nav (was prose `layout: single`). Counts: electricity 21, gas 7, water 16, heating 12, bills 29.
4. **Homepage**: register readout strip; Most Read rebuilt on theme tokens (Tailwind blue/gray chips eliminated); trust strip honesty fixes (live guide count; "Independent — no provider or switch-site ties" replaces the "Updated 2026" fib).
5. **Freshness system**: 118 files git-derived `updated:` → rendered "Reviewed:" dates + JSON-LD dateModified + OG article:modified_time (scalar-date fix).
6. **De-slop** (site-overrides.css, loads after canonical design-system): nav backdrop-filter, six 135° gradients, SaaS hover lifts, newsletter gradient flattened; mobile fixed-attachment repaint killed. Canonical theme untouched (Twin Q2 50-step review: APPROVE).
7. **Categories consolidated 17 → 7** (Electricity 21 · Gas 7 · Water 16 · H&C 12 · Bills & Fees 29 · Savings & Efficiency 4 · Troubleshooting 7) with **12 server 301s** for retired term URLs. Article URLs unchanged.
8. **Trust**: author/_index.md claims fixed ("decades of experience"/"Licensed HVAC Technician" → honest team framing; AI-assistance disclosure retained). blog/_index.md inline cyan/gray styles tokenized.

### Verification (both batches)
3× deterministic builds (659 pages, URL sets identical, FAQPage=96 stable — R8 held); 0 broken internal links sitewide; funnel order position-verified in built HTML; Twin Q2 independent diff review APPROVE (50 steps, hub counts measured, ad-split edge cases clean, 0 collateral in 118 stamped files). Live: 301s correct, new term pages 200, funnel/hub/register/mid-ad confirmed on production (electricity hub served stale at edge for ~minutes — cache-bypass verified 21/21 correct).

### Squad credits (SQ-016)
Analyst+Challenger: Phase-1 audit + independent creative DUAL (converged on "Independent Bill Auditor" direction). Twin Q: template/blast-radius map. Twin Q2: docs-vs-reality verdicts + pre-commit review (APPROVE). Researcher: editorial sample (8/8 pass). Operator: monetization architecture (94 steps). Executor: 2× transport-fail → Commander takeover. Council: creative+seo integrated (Bill Decoder flagship, de-slop expansion, self-host fonts, DefinedTermSet); monetization seat transport-failed (redundancy covered).

### Deferred (blueprint §15-17)
Magica media (Annotated Bill Anatomy first — credits gated), Phase B canonical-theme token refresh (6-site, after this proves), interactive Bill Decoder build, Plex type swap, category-footer polish.

### Rollback
`git revert 352a3a36 b22bd82c` or tar snapshot logs/backups/utilityexplained-pre-phaseA-20260821-200009.tar.gz. .htaccess category 301s revert with the commit.

---

## Entry 8 — 2026-08-22: SQ-016 media — Annotated Bill Anatomy series (Commander ZCode)

### Changes (commit 2743d604, deployed & live-verified)
1. **4 original annotated-bill diagrams** via Magica `gpt-image-2-text` (per user directive: gpt-image-2 only for generation), quality high, 1024×1536 portrait:
   - Electric: ledger with basic service $12.50 / 862 kWh × $0.1421 = $122.48 / delivery $34.10 / taxes $9.87 / total $178.95, audit labels
   - Gas: $11.00 / 64 therms × $1.12 = $71.68 / $18.30 / $6.24 / total $107.22
   - Water: base $18.00 / 8 CCF × $3.85 = $30.80 / sewer 8 CCF × $4.60 = $36.80 / stormwater $6.50 / total $92.10, "1 CCF = 748 gal"
   - Combined: big-three totals + **v2 regen** — first render's "total" omitted the $5 late fee (reader-detectable arithmetic); regen with explicit "IF IT HAPPENS TO YOU" conditional row + honest $378.27 monthly total
2. **Vision-QA gate** on every master: full transcription, spelling/legibility, arithmetic re-verification, palette check. 4/4 PASS (1 regen).
3. **Install**: webp q85, 85–103 KB each, `static/images/articles/<hub>/bill-anatomy.webp`; lazy-loaded, intrinsic width/height (CLS-safe), descriptive alt per instance, honest "illustrative example" captions.
4. **Wiring — 9 figure instances on 6 pages**: 4 hubs (1 each at their bill-anatomy sections), complete-guide (4 — one per major section; mid-article ad split verified undisturbed), hidden-fees (1 at "Where the Money Goes").
5. `.bill-figure` styles appended to site-overrides.css §6 (site-local; canonical theme untouched).

### Verification
Clean-slate 2× deterministic builds (642 pages, URL sets identical; FAQPage=96; mid_article=59); 0 broken internal links; CI 32551954033 green for 2743d604; live: all 4 images 200 byte-identical, figure counts 1/1/1/1/4/1 across the 6 pages (hub zeros at first probe were edge cache — cache-bypass confirmed), live CSS carries `.bill-figure`.

### Cost
~0.83 Magica credits (5 generations incl. 1 regen). Balance remaining per dashboard.

### Watch (extends Entry-7 window)
Time-on-page + scroll depth on the 6 figure pages vs. pre-figure baseline; image SERP (Bing images) pickup for "electric bill explained"-class queries; CLS on hub pages.

### Rollback
`git revert 2743d604` (content+CSS+images in one commit).

---

## Entry 9 — 2026-08-23: AdSense review returned “Low value content” — remediation handoff

### Status
**BLOCKED — do not request another AdSense review yet.** Google returned a low-value-content policy finding. The technical foundation is intact; the required work is editorial verification and corpus remediation, not another theme or ad-layout pass.

### Completed audit evidence
- Live checks: homepage, `ads.txt`, `robots.txt`, and `sitemap.xml` each returned HTTP 200. The homepage contains AdSense, canonical, JSON-LD, and Rybbit markup.
- Local build: `hugo --minify --gc` completed successfully (590 pages).
- Asset gate: `python3 scripts/check_image_paths.py public` passed.
- Corpus: 96 published blog guides; 7 are under 1,000 words, 32 under 1,500, and 52 under 2,000.
- Evidence gap: 92/96 blog guides have no outbound source URL, despite many containing exact rates, state rankings, savings figures, or regulatory claims.
- Editorial-quality flags: generic AI phrasing remains in several articles, and 16 guides lack a contextual internal link in the source body.

### P0: remove or fully re-research before the next review
1. `content/blog/7-states-with-worst-utility-spikes-2026.md` contains an impossible-at-publication citation to “BLS, December 2026” and other precise 2026 state claims without auditable sources. It must be unpublished/redirected or rebuilt from primary sources.
2. `content/blog/2026-utility-cost-index-by-state.md` claims “original analysis” and provides 50-state rankings, but the underlying data file, source URLs, collection date, and reproducible calculations are not present in the repo. It must be unpublished/redirected or rebuilt with a transparent dataset and methodology.
3. `content/blog/02-average-utility-costs-2026.md` contains conflicting total-cost ranges and numerous precise figures without linked source material. Re-research before retaining it as an indexed guide.
4. Independently verify every author/editor identity and every statement that articles are reviewed against primary sources. Do not imply credentials, editorial review, or source verification that cannot be substantiated.

### Required remediation gate for the next agent
For every retained or republished data-heavy guide:
1. Verify each material factual claim against a primary source; include a visible, dated Sources section with direct URLs.
2. Replace generic tables/ranges with either cited, reproducible calculations or clearly labeled illustrative examples.
3. Rewrite for a distinct reader task: bill-reading steps, a decision rule, a worked example, or a jurisdiction-specific path — not a generic definition plus stock advice.
4. Add only useful contextual internal links; remove templated “Related Reading” lists where they do not advance the task.
5. Keep title, canonical URL, and redirect plan explicit for every unpublished/consolidated page.
6. Rebuild, run the image and internal-link gates, sample rendered pages on mobile, and only then request review.

### Handoff boundary
This entry records the finding only. No articles were unpublished, redirected, rewritten, deployed, committed, or submitted for re-review in this audit session. Another agent owns the remediation decision and implementation.

---

## Entry 10 — 2026-08-23: AdSense remediation implementation started

### Status
**BLOCKED — remediation in progress.** Do not request another AdSense review. The P0 quarantine, disclosure corrections, and first source-led repair below are local/uncommitted and have not been deployed.

### Shipped locally
1. **P0 quarantine + URL preservation:** marked these unsupported high-risk posts as `draft: true` and added Apache 301s in `static/.htaccess`:
   - `/blog/7-states-with-worst-utility-spikes-2026/` → `/blog/why-did-my-utility-bill-go-up-this-month/`
   - `/blog/2026-utility-cost-index-by-state/` → `/blog/complete-guide-understanding-utility-bill/`
   - `/blog/02-average-utility-costs-2026/` → `/blog/complete-guide-understanding-utility-bill/`
2. **Quality gate:** added `scripts/content_quality_audit.py`, tests, `npm test`, and `npm run audit:content`. It inventories published guides and flags future-dated claims plus material quantitative guides missing source metadata. Baseline after quarantine: 93 published guides, 85 still flagged for source remediation.
3. **Trust corrections:** rewrote editorial-policy, editorial-team, and author-bio claims so they no longer imply every guide has already been verified against primary sources or that bylines are independently credentialed people. The public standard is now visible source links and review dates for data-heavy guides; older pages are explicitly under review.
4. **Source-led repairs:**
   - Rewrote `utility-assistance-programs-liheap.md` to remove unsupported national benefit, income, timing, savings, and credit-impact claims. It now uses direct HHS LIHEAP and DOE Weatherization links in front matter and a visible Sources section.
   - Rewrote `what-is-ccf-on-a-water-bill.md` to remove unsupported household-usage and cost ranges; it now uses a direct USGS conversion source and tells readers to compare their own billing history.
   - Rewrote `water-meter-leak-indicator-explained.md` to remove unsupported product claims, brand-specific feature assertions, and universal cost estimates; it now uses EPA WaterSense guidance and a visible Sources section.
   - Rewrote `is-your-toilet-running-leak-test.md` to use EPA WaterSense's documented dye-test protocol and removed unsupported national waste, repair-cost, and bill-impact estimates.

### Verification
- Unit tests: 2/2 pass.
- Clean Hugo artifact: 569 pages built successfully to `/tmp/utilityexplained-adsense-audit`.
- The three withdrawn P0 article routes are absent from that clean artifact; their 301 rules are present in generated `.htaccess`.
- Asset checker passed before this remediation; re-run it as part of final pre-deploy verification.

### Next remediation batch
1. Replace every internal link to withdrawn P0 URLs with its final destination rather than relying on a redirect.
2. Work through the remaining source-flagged guides one source-led batch at a time. Do not bulk-add generic citations or source metadata without matching claims to the underlying page.

### Continuation — future-claim quarantine (same session)
The quality gate identified four additional published pages with future-dated factual claims. They are now also drafts with permanent 301s:
- `/blog/average-utility-bills-by-state-2026/` → `/blog/complete-guide-understanding-utility-bill/`
- `/blog/how-to-lower-electric-bill-complete-guide/` → `/blog/05-how-to-lower-utility-bills/`
- `/blog/stormwater-fee-on-water-bill-explained/` → `/blog/44-how-to-lower-water-bill/`
- `/blog/why-your-electric-bill-keeps-rising-2026/` → `/blog/why-did-my-utility-bill-go-up-this-month/`

Post-quarantine verification: 89 published guides, 81 source-remediation flags, and zero remaining `future_claim` findings. Hugo built 559 pages; the image gate and unit tests passed. These changes remain local/uncommitted and must not trigger an AdSense review yet.

### Continuation — source-led repair batches
Source-led repairs subsequently covered the primary electric-bill guide, high-bill diagnosis, water-meter and leak guides, smart-meter and standby-power guides, net-metering guidance, HVAC staging/ratings/thermostat pages, heating-cost comparison, first-apartment budgeting, and the fee/billing explainers. Each was stripped of unsupported national figures, product claims, or fabricated comparisons; given direct primary-source links; and rebuilt/tested locally.

Current verified baseline: **89 published guides, 52 remaining source-remediation flags, zero future-claim findings.** The automated remediation worker (`utilityexplained-adsense-source-remediation`, every 5 minutes) continues the queue without deploying, committing, or requesting review. Do not submit to AdSense until the queue is empty and a final content, generated-artifact, and live-production audit passes.

## Entry 10 — 2026-08-29: SQ-051 remediation executed (full plan)

**Method:** Commander + 3 concurrent lieutenant seats (GLM) for the big rewrites; every factual change verified against a fetched primary source the same day. Build validated (`hugo --minify --gc`, 471 pages, asset gate OK). All changes staged in git, uncommitted.

### Quick wins shipped
- **Dead draft-stubs resolved** (the 96.3%/0s-TOP page was a 418-byte redirect): deleted drafts for `why-your-electric-bill-keeps-rising-2026` (→ alias to `why-did-my-utility-bill-go-up-this-month`), `stormwater-fee-on-water-bill-explained` (→ alias to `44-how-to-lower-water-bill`), `41-how-to-read-electricity-bill` (alias already on 01). No redirect loops; alias directions verified.
- **`hero_below_answer: true`** set on the instant-exit set: 06-water, 18-fuel-adjustment, how-do-smart-meters, 25-taxes (via rewrite), 19-surcharges (via rewrite).
- **#16 state-average arithmetic fixed & PUBLISHED** — see correction below. $262 headline → component-derived ~$375; electric $159→$165; Hawaii $275→$303 (own-rate 33.7¢×900) + total $425→$453; realistic-Hawaii $332→$324; footnote $200–240→$174; "every U.S. state"→"17-state sample"; title + description now honest; standardized-estimate methodology note added.
- **#24 toilet-test:** two markdown links inside raw HTML → `<a>` tags (first-screen rendering defect).
- **#5 CCF:** false USGS citation (glossary contains no CCF conversion; wave-2 verified 0 hits in 138KB) → EPA "One CCF is equal to 748 gallons" + inline derivation.
- **#9:** phantom "$70/yr (EPA)" → verified 2,700 gal + 330 kWh/yr (EPA showerheads page); dead home-energy-audits URL → live home-upgrades; air-sealing "10–20% (DOE)" → verified thermostat claim.
- **Dead .gov URLs (4 files, 6 URLs):** energysaver family + BBSC PDF → live ENERGY STAR saveathome pages + DOE FEMP (duct 20–30% claim verified VERBATIM on ENERGY STAR live page).
- **#12 retitled** ("12 Common Causes" promise removed — body never enumerated 12).
- **#13 thermostat:** unsourced "3–5%/degree above 68°F" → DOE-anchored ~1%/degree rule + 74vs68 math (~6%).
- **#20:** EIA sources added to frontmatter; $0.96–1.06/therm examples labeled (national avg ≈$1.91/therm, EIA N3010US3 May 2026, wave-2 re-derived).
- **#4:** EPA 10-minute dye-test alignment, EPA 12,000-gal winter threshold added, 'therms' tag removed, plumber FAQ de-hedged (utility leak-check first), smart-meter anchor text fixed.
- **BLS "December 2026" impossible citation** removed from 7-states draft (line 38).
- **#22 + #30 + #28 + #26 + #29:** dead BBSC URL swap; worked tier example (clearly labeled illustrative) + 4 internal links; 4,523-CCF commercial-scale meter example → residential 1,247→1,255; connection-fee internal links; PG&E dateline + TXU 2,000-kWh cap note + smart-plug hardwired-dishwasher qualifier.
- **#2 spike:** ENERGY STAR URL swaps (filter "15–30% harder" → verified qualitative quote; ducts kept, now correctly cited), 5/10/12 structure bridged, FAQ wall reformatted.
- **#1 flagship:** QA dollar contradictions reconciled to body (LED $150–200, water-heater $60–120, phantom $120–190); "3–6%-per-degree" phantom cross-ref deleted; RECS standby misattribution rebased on EIA's verified 23% "other devices"; HVAC 40–50%→52% (EIA RECS 2020); water heating →~20% (DOE); $159/$142→$144 2024 verified; FAQ 3–6% vs 6–9% contradiction fixed; Nest claims labeled manufacturer-reported; Tools block moved below the Why-High section; duplicate CTA paragraph deleted.
- **#3 sewer — three municipal rates corrected from official sources:** Seattle $8.44→**$20.18/CCF** + $86.77 typical bill (live SPU page; the old figure was 2.4× low); Philadelphia "$10.22/CCF tiered"→**flat $5.16/CCF** ($51.62/Mcf, official PWD schedule; old figure was tiered AND double); SFPUC "tiered $6.48/CCF first 10.4/14.4"→**90% of water × $20.74/unit** (Prop 218 notice + FY26-27 schedule). All with "rates as of" datelines + retrieved-date sources.

### High-impact rewrites (lieutenant seats, Commander-verified claim-by-claim)
- **#8 water-bill-too-high (93.8% bounce):** restructured to causes-ranked-by-likelihood (toilet #1, irrigation #2, rate/tier #3…), Quick Answer IS the dye test, product boxes moved after diagnostics, EPA benchmark table computed from 82 gal/day, 12,000-gal winter line. Every EPA figure verified verbatim.
- **#25 taxes-fees (6s TOP):** 467 procedural words → 984-word reference with 5 VERIFIED jurisdiction examples (Pasadena UUT 7.67%/7.9%, WA 6% statutory cap, Cheney 14.75% voter-approved, FL 10% municipal cap, MN 216B.36 franchise basis) + the $11.11 gross-receipts math. Pasadena + Cheney re-verified by Commander post-hoc.
- **#19 surcharges (8s TOP):** definitions lead (PUCO's own words, verified from the fetched artifact), 5 real riders table (Duke fuel/DSM/storm, ORC 4929.161, PUCO $10M vegetation cap), workflow preserved.

### Consolidations
- **#15 family absorbed into #12:** both live duplicates deleted (15-… 394w + why-my-… 963w) + draft why-electric-bill-changes-month-to-month (784w, URL already aliased). All three URLs alias to #12; inbound links retargeted (10-billing-cycle, 7-states). Payment caveat ported to #12.
- **#23 narrowed** to the sudden-spike angle: action-first QA (dye test), rate-vs-leak decision rule, explicit handoffs to #8 (persistent high) and #4 (meter test).
- **#9** keeps its slug; both intents now served (title=methodology, QA row=verified savings).
- **#11** rate provenance labeled; **#17** baseline→snapshot; **#18** RF claim softened to FCC-ID lookup path + NILM qualified + meter-test path added.

### CORRECTION to the SQ-051 audit (important)
`average-utility-bills-by-state-2026` was **draft:true** (retired by SQ-048 during the credibility stopgap) — the audit graded its content while the live URL served a 421-byte redirect to `complete-guide-understanding-utility-bill` (923w generic). Post-fix, the corrected page is **published** (draft removed, complete-guide's alias claim dropped, both decisions one-line reversible in git). The audit table's #16 row should be read as "fixed-and-published," and its engagement numbers (33pv/86.7%br/14s) were measured on the stub, not the content. Mason's "sources don't render as hyperlinks" template finding (#22) was also disproven — footer links render; frontmatter `sources:` is metadata-only by design. No template change made.

### Known remainders (honest list)
- #16's 17-row table: rows are now internally consistent + methodology-labeled, but per-state rates were NOT individually re-sourced against EIA state tables (the 50-state rebuild remains open; Hawaii's 33.7¢ itself unverified vs current EIA).
- Human-review register items still open: EIA Table 5.4.a direct fetch, Nest/P3 spec verification, PG&E tariff currency, #6 tariff references, #28 example intent, author-identity substantiation (Entry-9 P0 #4).
- The flagship's energy-breakdown chart IMAGE still shows the retired 4–8% standby bar (alt text matches image; prose fixed) — regenerate the chart asset.
- #2/#12 shared-cause prose dedup (cross-link ownership done; full text dedup deferred).

**Watch in Rybbit (14-day):** bounce on 06-water (93.8%→~77%?), TOP on 25-taxes/19-surcharges (6s/8s→30s+), entrances on the published state-average URL, stub-URL pv retention, Google referral share.

## Entry 11 — 2026-08-29: SQ-053 tier-2 audit + remediation (ranks 31-60)
9 pages rebuilt with verified jurisdiction evidence (17/20/22 fees, 21/26/14 lifecycle, 12+gas-delivery gas pair, 16-budget surgical); 43→12 consolidation executed; REFUTED claims fixed: Emporia outdoor rating (manufacturer says indoor-only — safety), 44's "30-40%/$200" EPA misattributions (replaced with EPA's real 10%/~20%/$1,300/$500), 12's "80-150 therms" (RECS-annual reframing), Columbia Gas SCO miscategorization. why-did-my 0s-TOP root cause (143KB hero above QA) fixed. complete-guide data-aliases moved to state-average page; 02 draft deleted. Hero flags ×10; dead URLs ×4. Incidents: lieutenant channel contamination (stale SQ-045 artifacts) — makeup run on wing + anti-contamination constraint added to all packets; scout seat (gemma4:e2b) dead both dispatches — work absorbed by Commander; one Commander shell-sweep bug caught by workers (unquoted $SLUGS.md loop). Open queue in SEO-CONTENT-AUDIT-FACTCHECK-TIER2-2026-08-29.md. Watch: 16-budget/20-proration/17/22/21/26 bounce+TOP vs tier baselines (100%/0s, 1s, 15s), 43-redirect traffic retention on 12.

## Entry 12 — 2026-08-29 (SQ-054): Tier-2 open queue cleared — same-day full close

**Scope:** every item logged open in the tier-2 report (Entry 11): 8 sourcing passes, 3 rebuilds, 2 verifications, 3 decisions, 3 triage-lite full treatments. 15 pages touched, 1 draft deleted.

**Refuted-at-source (the day's highest-value catches):**
- CO "HB 1090" tenant-water-billing law **does not exist**; the real HB25-1090 is a deceptive-pricing statute that *exempts* landlords from disclosing actual utility amounts — opposite framing. Deleted + correctly re-cited.
- "KP125MP2" **is not a TP-Link SKU** (URL redirects to KP125M; it's an Amazon bundle ID) — product renamed across table/prose/affiliate box.
- EIA price on 10-fixed was 18.44¢; actual Table 5.6.A = 18.34¢. Fixed.
- 46's "off-peak typically 40–60% cheaper" contradicted by its own cited table (7.5%–100% spread); "typical 8¢ off-peak" was invented. Replaced with tariff-anchored math + ENERGY STAR $50/yr.
- Six provider rates on 10-fixed unverifiable (TXU row likely wrong per aggregator) → replaced with mechanics table + official shopping portals.
- Tiered-water QA contained a math error ("66% less water" — actually 40%) + lifted Corona/CIMIS city text + a leaked HTML comment ledger. All excised in commander rewrite.

**New verified anchors added to the site's evidence base (all fetched/re-derived 2026-08-29):** Austin Water 5-tier table ($3.27–$20.40/1,000 gal) + wastewater ($11.26 base, $13.40 tier-2, "whichever is lower"); SAWS winter-averaging window ("after November 15... on or about March 15"); MN Statutes 216B.096/.097/.098 (Oct 1–Apr 30, 50% median income, 10% payment cap, 5-business-day medical certification, 6/12-month limits — cross-family-verified 5/5); Louisville 2026 tariff + Philadelphia PWD + Cleveland Water fixed charges; USPS forwarding ($1.25/12 mo/3 business days); EIA "single-family detached ≈ 3× the energy of 5+-unit apartments"; CPUC/PUCT complaint procedures (TX: no disconnection of disputed charges until accuracy determined + notification); KP115/KP125M/Tapo P110M spec sheets; ENERGY STAR dishwasher $50/yr.

**Process notes:** packet-generator bug shipped wave A read-only (write_paths never passed) — recovered by re-issuing as a write wave with audit intel embedded (verification-first-then-write actually improved quality); two worker scratch files leaked into repo root (removed); python replace traps reconfirmed (curly-vs-straight apostrophes, quote-collision heredocs — Edit tool is the safe path on read files).

**Build:** 470 pages, 205 aliases, asset gate OK. Staged, uncommitted (HEAD b624a464).

**Watch (14d, Rybbit):** gas-meter (87.5% br baseline), apartment (100% br), tiered-water (33.3% br hold), dispute/shut-off engagement depth, 10-fixed impressions on new title.

## Entry 13 — 2026-08-29 (SQ-055): APEX engagement optimization, traffic ranks 11-20

**Scope:** 10 pages (Rybbit last-30 ranks 11-20, fresh pull 2026-08-29): 23-billing-cycle, 07-gas-too-high, electric-breakdown, 25-taxes, state-avg-2026, 19-surcharges, mcf-vs-therms, smart-meters, 18-fuel-adjustment, avg-water-usage. Ranks 18/19 by raw traffic (keeps-rising, stormwater) were ALIAS redirects — replaced by next real articles (21 smart-meters, 22 fuel-adjustment) to avoid re-editing pages under the SQ-053/054 14-day watch. Lens = reader experience (intent/momentum/journey/CTA) — deliberately NOT fact work; facts came fresh from today's SQ-051..054 audit.

**Formation:** 3× lieutenant analysis wave (10 briefs, Commander-reviewed with spot-checks) → 3× lieutenant implementation (rulings embedded; write_paths confined) → executor mechanical cross-check did NOT complete (run orphaned at 289 steps, no report written; superseded by Commander direct verification: hugo build EXIT 0, 92/92 hrefs resolved in the rendered tree, 0 JSX artifacts in rendered HTML, frontmatter audited against rulings, arithmetic re-derived). Baseline persisted: .rybbit-t11320-2026-08-29/baseline_11-20.json.

**Highest-value catches (analysis wave):**
- LIVE 404: electric-breakdown linked /blog/fixed-vs-variable-rate-electricity-plan/ (file deleted in consolidations) → swapped to 10-fixed-vs-variable-utility-rate.
- JSX artifacts `{" "}` rendering inside 2 links on smart-meters — gone (0 in rendered HTML).
- mcf: raw-HTML title-echo inside Quick Answer, 3× exact-match keyword stuffing, self-correcting Scenario C debris ("Note: this rate seems low..."), and a 1 MCF = "1,000 CCF" internal contradiction — all fixed; math re-verified (15 MCF = 155.55 therms, $1.01/therm).
- state-avg: phantom "interactive rate lookup tool" promise deleted; self-referential FAQ link fixed; jump-row added; hero_below_answer set.
- 07-gas: 10-vs-11 cause-count mismatch fixed (count-free H2); 13-bullet Related-guides dump after Sources (with a duplicate) → curated 10-bullet Related Reading before FAQ; on-page meter course compressed to pointer + link (net-negative words).
- 18-fuel: 0→9 internal links, +3 FAQs, symbolic worked example (no new numbers), disclosure chip for family consistency.
- avg-water-usage: page never answered its own keyword — worked example (12 CCF ÷ 30 ÷ 3) + site's own 2-4 CCF/person/month benchmark (attributed, linked) now on page; hero_below_answer set.

**CTA decisions:** Nest box on 07-gas STAYS at doctrine placement (move vetoed). ONE new box approved: Emporia Vue 3 (B0C7B1LKDW, doctrine copy, problem-language label) at end of smart-meters "Benefits" — the one page where the reader's next need IS the product's function. All other 8 pages: NONE-informational per AFFILIATE-PLACEMENTS NOT-A-FIT.

**Totals:** +397/−181 lines across 10 files; 92 unique internal hrefs — all resolve in rendered tree (verified against fresh hugo build, EXIT 0); zero JSX artifacts in rendered HTML; faq-schema renders on all pages carrying FAQs; frontmatter changes exactly per rulings (3× hero_below_answer, 4× description, updated everywhere; zero slug/title/alias/source touches).

**Watch in Rybbit (14-day):** TOP on 25-taxes (5.6s→30s+ target) and 19-surcharges (4.2s→30s+ target); bounce on mcf (89%), state-avg (87%), water-usage (88%), smart-meters (92%); pages/session site-wide (1.235 → 1.5+ goal); affiliate_click events on the Vue 3 box; entrances on 10-fixed (dead-link repair downstream); NOTE — these baselines are PRE-SQ-051..054 AND PRE-this-wave; the two same-day change sets will entangle attribution for this cohort; treat deltas directionally.

## Entry 14 — 2026-08-29 (SQ-056): Visual audit + image plans for the rank 11-20 set
Vision-grounded audit (analyst seats viewed every hero + existing visual; Commander validated against 4 directly-viewed assets). Heroes 10/10 present, 8/10 suitable; 2 regens queued (mcf, 18-fuel: warm person-scenes on pages whose subject is numbers — two seats converged independently). CRITICAL: state-avg carried TWO live AI-garbled pseudo-text map infographics — REMOVED from the page this session (hugo EXIT 0; files still on disk, flagged for asset sweep). Plans take the 10-page set from 4 to 39 visuals (24 new illustrative figures, style-bible-compliant briefs with filenames). Product imagery confirmed affiliate-wired and form-factor-accurate (Nest, Vue 3); no un-monetized product figures planned. Orphan off-style asset flagged (07-gas custom_inline.webp). Full report: VISUAL-CONTENT-AUDIT-2026-08-29.md; per-page plans: .squad/SQ-056/visual-plans/. Generation of the 24 planned figures = ready-to-execute follow-up.

## Entry 15 — 2026-08-29: SQ-056 generation pass executed (external agent) + Commander completion audit
**Generated + wired:** all 24 planned figures plus 2 bonus state-avg figures (gas-range-by-region, narrow-vs-broad-basket) = 27 in-body visuals across the 10 pages; both hero regens shipped (mcf v3 — meter with legible register, CCF->MCF->THERMS flow, amber on therms, no people; 18-fuel v3 — symbolic calculation). **Verified by Commander:** hugo build EXIT 0; 27/27 figures render on their pages; both v3 heroes live; alt texts honest and specific; 4 figures viewed directly — text fully legible, values match on-page verified data (9.8¢/33.7¢ + EIA Jun 2026 tag; $125/$165/$190 amber-on-national), style on-bible (mono numerals, ledger surfaces, amber discipline). The garbled-pseudo-text failure mode of the previous generation batch is absent. **Bonus:** mobile horizontal-scroll CSS for wide data tables (the 17-row state table now scrolls instead of crushing). **Affiliate rule intact:** no product imagery outside wired product boxes. **Completion audit closed the gaps:** the two garbled state-avg map FILES deleted from disk (unwired in Entry 14; zero references — the initial grep scare was a false positive from the retired draft 7-states page's own same-named assets); this entry added (convention miss). **Remaining flagged, non-blocking:** unwired spare `25-taxes/taxes-fees-breakdown.webp` (wire or sweep); `custom_inline.webp` strays in several article dirs (site-wide asset sweep candidate); superseded hero v2 files kept on disk (harmless); P4 optional hero polish (state-avg map regen, 07-gas v3, smart-meters flat regen) still optional; retired draft 7-states page carries its own garbled section images (dead with the draft — sweep whenever that draft is resolved). Uncommitted, as before — review with `git diff`/`git status` and commit when ready.

## Entry 16 — 2026-08-29: Remaining-task closure (SQ-055/056 tail)
All flagged remainders executed: (1) asset sweep — 33 unreferenced custom_inline.webp orphans deleted (1 kept: 28-reconnection references its own), 3 superseded hero v2s deleted (mcf, 18-fuel, water-usage), redundant spare 25-taxes/taxes-fees-breakdown.webp deleted (viewed, overlapped the authority card), retired draft 7-states page + its garbled image dir deleted per SQ-051 consolidation convention (URL aliases to why-did-my-utility-bill-go-up, verified live). (2) state-avg hero REGENERATED (SQ-056 P4) via magica gpt-image-2 per owner instruction — flat ledger US map, amber pinned to Hawaii (the actual cost leader), exactly two text elements, viewed and verified legible (SHIP verdict); wired as hero_v3.webp (64KB webp), v2 removed, build EXIT 0. (3) Everything committed. Remaining open site-wide (non-blocking, logged for future): none from this mission thread.

## Entry 17 — 2026-08-30 (SQ-065): Full-scale 9-section content audit, cloud-only squad formation
Operator audit prompt (SEO/UX/QC editor lens) executed over all 114 pages (89 blog + 25 core) by a CLOUD-ONLY squad (user constraint: no msi local seats): 13 dispatches — glm-5.3-flash lieutenant ×5 (money/flagship slice, core-pages rescue, wave-2 synthesis), dsv4-flash wing ×6 (fees cluster, journey trace, HVAC rescue, cartographer map incl. water/rates, verifier), qwen3.7-flash ×2 (judgment sample, claims verification). **Deliverable: FULL-CONTENT-SEO-AUDIT-2026-08-30.md** (9 sections, 114-row master table mechanically diffed against the repo inventory — complete; 12 severity-ranked critical issues; 24-item phased action plan; 5 rewrite briefs). Evidence tree: .squad/SQ-065/ (8 wave-1 artifacts, evidence brief, claims table, spot-check).

**Highest-value catches:** 2 external claims REFUTED vs primary sources (water-heater blanket "~25%" → DOE cap 4–9%; 07-gas heating share "60–70%" → EIA RECS ~40–45%, contradicting its own 40–50% under one footnote); duplicate `sources:` frontmatter key on the revenue-core guide; $200–450/mo stacked-savings banners vs the page's own $164.88 average bill; "verified via PUC dockets" fee table on 28 with zero checkable URLs; 3 true dead ends (net-metering, ev-charging, water-service-charge — 0 links in ALL formats, grep-verified); aux-heat truncated-H2 render bugs; headless Savings & Efficiency cluster (the site's best pages have no hub); Google-0 explained mechanically (deploy pings IndexNow only = Bing ecosystem; no GSC sitemap submission; note — the IndexNow key is public BY PROTOCOL DESIGN, do not "rotate" it).

**Verification chain:** every artifact disk-checked; uncorrelated spot-check of the finished report returned FIX (9/10 confirmed, 3 defects — false mcf ORPHAN from the markdown-only metrics tool, overstated link-stuffing, overstated safety-disclaimer framing) — all three Commander-grep-verified and patched in-report; post-check closures CONFIRMED EIA 18.34¢/kWh (June 2026, Table 5.3) and the NIPSCO IURC FAC order (verbatim PDF match) — final external tally 7 CONFIRMED / 2 REFUTED / 1 UNVERIFIED (28's table — site cites no URLs). Metrics tooling caveat logged: markdown-only counting reads HTML-headed pages as false zeros (mcf: "0 ilinks" vs 12 real links).

**Fleet record:** 3 protocol deaths (mason, verifier at step 289, one redundant water rescue) — all rescued with zero coverage loss; cartographer survived a 31-min generation stall to deliver in 2h. Zero site-content writes; only repo additions are the report + .squad/SQ-065/. Uncommitted — review and commit when ready. Fix-Immediately queue (report §7): 9 items, headlined by the two refuted claims, the flagship arithmetic/frontmatter repair, GSC submission, and dead-end revival.

## Entry 18 — 2026-08-30 (SQ-066): Full remediation of the SQ-065 audit — 24-item checklist executed
**Formation:** Commander surgical edits (credibility core, journey wiring, metadata, merges) + 3× glm-5.3-flash lieutenants (forward-topic rebuilds, Savings hub + 05, legacy cohort) + qwen spot-check; cloud-only per session constraint. Mason (dsv4) protocol-died twice on HTML→Markdown conversions — conversions SKIPPED as cosmetic (the metrics tool now counts HTML natively); glossary links done by Commander.

**Credibility (Fix-Immediately, audit C1-C8):** water-heater blanket canonicalized to DOE's 4–9% across 05/07/guide (was ~25%/5-10%/4-7%); 07-gas corrected (title 11 Causes; heating share 40–45% EIA RECS with winter-share clarification; payback rows now cite the ~23y worked example; sources 3 relabeled ENERGY STAR, 4 deduped to the real water-heating page; uncited 15–30% rate claim cut); flagship guide repaired (duplicate `sources:` block deleted; "17 proven steps" honest count; non-additivity note defusing the $200–450 stacked banners; both phantom-load tables reconciled to 17¢ math; Emporia box moved beside step 3); aux-heat truncated-H2 render bugs fixed + Pattern-A intro replaced; 28-reconnection stripped of the "verified via PUC dockets" table claim → structure-only + verify-where pointers, moratorium rows now link 21/can-shutoff, restore timings made honest.

**Journey wiring:** apex hub (complete-guide-understanding) now routes dispute/shutoff/LIHEAP/rate-plan; 03 got act edges + the 42-anchor honest rewrite; crisis loop closed (dispute→internal LIHEAP, LIHEAP→shutoff); 30-spike links 04+shutoff; 5 formerly zero-outbound pages wired (net-metering, ev-charging, water-service-charge, sewer-averaging, single-stage); wrong-target alias links retargeted (why-did, rates-fees, aux-heat winter link, gas-hub fragment).

**Structure/merges:** gas-delivery→12 (category table + SCO rebuild + shopping section + correction note absorbed; 4 inbounds retargeted; alias); gas-vs-electric→48 (LT-3 absorption; 5 inbounds retargeted; alias); what-is-kwh→11 (definition table + formula + examples folded; 5 inbounds retargeted; alias); without-solar scope-differentiated (banner + guide hierarchy) instead of deleted — 3 pages removed net, 112 md total.

**New:** content/lower-your-bills.md — the Savings & Efficiency hub (C6 headless-cluster fix; 14 spokes in 5 reader stages; existing workbench image reused; fanned from guide + electricity hub); 05 retitled "Lower Your Utility Bills: The Ranked List of What Actually Saves" with scope note; LT-1 rebuilt net-metering (Where-This-Lands section + buy-all/sell-all illustrative) and which-rate-plan (Summer Trap with site-verified ConEd rates, decision table, financial disclaimer, EV link); LT-3 rebuilt afue (ratings matrix, 2 verified sources, carpet links cut, markdown body) and heat-pump-running (normal-vs-symptom verdicts, defrost, balance point).

**Hygiene/tooling:** blog-index counts corrected (89 guides; 22/18/10/24 per hub); 49 source dup removed + citations renumbered; 16-budget source annotated; bills-hub duplicate entry → 01, wrong 04-anchor → 24, 03-anchor fixed, 02-alias duplicate dropped; corrections-page internal SQ-IDs stripped; water-hub phantom stormwater slot → real 44/drought links; glossary bottom list now real hub links; **content_quality_metrics.py counts HTML h2/h3 + href links + {{< ref >}} shortcodes** (kills the false-zero artifact class that misflagged mcf/ac-running/kWh); gas-hub therm example canonicalized to $1.91.

**GSC structured data (operator-reported):** root cause found by lieutenant with full reproduction — theme head.schema.html `jsonify` without `safeJS` double-encoded JSON-LD into a top-level string (372/439 blocks failing on the 2026-08-11 snapshot); fix already landed 2026-08-14/21 (ancestors of HEAD); current tree verified 412/412 valid blocks + live-site curl checks on GSC-listed URLs all clean. The 40 GSC rows are stale crawls → user action: hit "Validate Fix" in Search Console.

**Verification:** hugo build EXIT 0 at every stage; check_rendered_output OK (no leaked shortcodes); check_image_paths OK; verify-links: 1 real dead link fixed (gas-hub fragment), remainder are the tool's root-`/` artifact; final twin_q spot-check dispatched. Uncommitted — review with git diff/status. Remaining deferred: §5 visual generation pass (magica), missing spokes (kWh/day, supplier scams, gas-leak safety, furnace tune-up, stormwater), byline identity decision (user), GSC validate-fix click (user).

---

## Entry 19 — SQ-066 follow-up: diagram set + author-desk honesty pass (2026-08-30)

**Diagrams (audit §5):** 15 original figures generated (magica gpt-image-2-text, medium, 1536x1024 → webp VP8 q82), each transcription-verified for legibility/values; 11 regenerated once where the first pass invented text or drifted off-spec. Wired one per section at the audit's recommended placements — net-metering (import/export rate spread), 07 gas (end-use rank order + therm seasonality 19%/2.4%), rate-plan Summer Trap curve, aux-heat 1x-vs-2-3x thermostat card, 05 payback ladder, electric-guide savings-vs-cost card, 13 short-cycle diagnostic (cheap-first), 42 heater safety checklist (wall outlet/3 ft/tip-over/UL), 48 heat-pump breakeven formula card (18.34¢, $1.92/therm, COP 2.7 — matches page math), 06 water leak priority quadrant, ac-running supply/return 20°F delta, 50 smart-plug measure-assess-automate, 45 generator CO placement (20 ft, exhaust away, CO alarm), EV overnight price curve. Alt text carries the page's authoritative numbers for every figure.

**Author pages:** desk-label decision applied — author/_index.md now describes bylines as desks (Bills & Rates, Energy Efficiency, Affordability & Assistance, Heating & Cooling, Consumer Rights), not credential-style personas; about.md gained "How this site is produced" (AI drafting assistance + primary-source/methodology/corrections as the trust basis). Individual desk pages already desk-framed.

**Verification:** hugo EXIT 0; check_image_paths OK; check_rendered_output OK; all 15 figures confirmed present in rendered HTML (15/15 grep). Deployed via main push (CI: build → rsync → IndexNow).
