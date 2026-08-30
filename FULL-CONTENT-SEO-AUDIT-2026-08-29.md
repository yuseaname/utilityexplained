# UtilityExplained — Full Content, SEO & Quality Audit (SQ-068)

**Date:** 2026-08-29/30 · **Method:** 11-seat squad (9-seat wave 1 + 2 wave-2 follow-ups: lieutenant×2, prospector, tracer, verifier×2, cartographer, twin_q, mason, executor, scout) + Commander disk-verification of every load-bearing claim
**Scope:** all 110 content pages (88 blog — 84 live + 4 draft, 5 author pages, 12 site pages, 5 hubs, homepage), the rendered `public/` build (525 HTML pages), sitemap/robots, analytics baseline (KPI 2026-08-29)
**Artifacts:** `.squad/SQ-068/artifacts/register-thin-generic.md` (110-row register) · `.squad/SQ-068/artifacts/visual-plan-candidates.md` (20-entry visual plan) · `.squad/SQ-068/results*/` (11 seat envelopes)
**Claim discipline:** every worker claim below was either Commander-verified on disk, multi-seat corroborated, or is attributed to its seat. Two worker headline claims were REFUTED by disk-check and excluded (see §2 note).

---

## 1. Executive Summary

**Overall content health: strong and improving fast — the remaining risk is concentrated in a short, specific punch list, not systemic decay.**

In the 24 hours since the SQ-045 audit (2026-08-28), the corpus went from 97 to 88 blog files with the worst duplications alias-absorbed, ~20 fee/guide pages deepened with verified tariff/PUC sources, and a fact-check pass executed. Today's fleet re-derivation confirms the cleanup landed: **zero live orphan pages, zero duplicate titles or meta descriptions among real content pages, canonicals on 100% of 525 rendered pages, FAQ schema on 57 pages, and a house exemplar** (`17-what-is-customer-charge`) that demonstrates exactly what "verified, tariff-first" content looks like.

**Strongest assets:** the five hub pages (quality 8–9/10, real unit math, FAQ schema on the model hub), `how-to-lower-electric-bill-complete-guide` (9/10 — dated EIA/DOE sources, cost-tiered Quick Answer, correctly matched affiliate placements), `07-gas-bill-too-high` (9/10), `can-utility-shut-off-service` and `how-to-dispute-utility-bill` (YMYL-correct: keep-paying guidance, PUC escalation, sample letter), and the FTC-compliant disclosure architecture (every monetized page discloses — the trust chain's strongest link).

**Largest risks (evidence in §2):**
1. **A live authoring-scaffolding leak**: the rendered `moving-utilities-checklist` ships a "Image Prompts" section — three AI image-generation prompts — to users and crawlers (verified in `public/`).
2. **The flagship that anchors the whole bill-reading cluster is underperforming**: `complete-guide-understanding-utility-bill` was retitled "A Practical Workflow…" while its slug, keywords, homepage slot, and absorbed alias still target "complete guide to understanding your utility bill" — the leanest flagship on the site (9KB), zero visuals, no FAQ.
3. **Publish-gated data contradiction**: the unpublished `2026-utility-cost-index-by-state` draft carries a $262/month national figure that contradicts the live $375/month (narrow-basket) figure on `average-utility-bills-by-state-2026`. Publishing without reconciliation recreates the SQ-045 credibility crisis.
4. **Fact drift on a money page**: `46-what-time-is-electricity-cheapest` presents Con Ed TOU rates (22.33¢/44.97¢) that Con Ed's live page no longer shows (27.86/17.11/5.22¢ as of 2026-08-29 fetch).
5. **Execution debt, not content debt**: the #1 query in the niche — "how to read your utility bill" — sits as an unpublished draft while its alias points at the underpowered flagship; three more drafts linger with a URL-collision hazard on one.

**Likely search-visibility blockers** (twin_q verdict + Commander ground truth): title/slug mismatch on the flagship; three draft remnants; hedging-overcorrection on the four sub-520-word diagnostic pages (zero dollar figures, zero named utilities — they read as evasive next to the house exemplar); 112 blog titles over 60 chars; 252 card images without alt text; homepage title tag "Utility Explained" carrying no keyword.

**Top 5 highest-impact improvements:**
1. Delete the Image Prompts section + ship the four brief-driven rebuilds (flagship + 24-delivery + duct-leaks + drought-surcharge) — §8.
2. Resolve the draft cluster: delete 3 dead drafts, archive the state-index draft until the $262/$375 basket is reconciled, and fold the "how to read" query into the rebuilt flagship.
3. Correct page 46's Con Ed figures and backfill retrieval dates on the ~44 posts whose sources list bare URLs (the editorial policy promises "dated source links" — practice is at 48%).
4. Kill the 8 uncited savings claims in buying-decision tables (quoted in §2.6) or source them — they sit exactly where a fabricated number would cost a reader money.
5. Trust-layer upgrades that are cheap: homepage title tag, 252 alt texts, one real corrections-log entry, author pages with one concrete example guide each.

---

## 2. Critical Issues (prioritized)

### C1 — LIVE DEFECT: authoring scaffolding rendered to production (CRITICAL, 2-minute fix)
`content/blog/moving-utilities-checklist.md:152` — an `## Image Prompts` section (3 numbered image-generation prompts) is rendered into `public/blog/moving-utilities-checklist/index.html`, TOC entry included. Users see internal prompts; crawlers index them. The images the prompts describe were never built (the page's visual plan, §5, includes the moving timeline they specify). **Commander-verified in rendered HTML.**

### C2 — Flagship title/slug mismatch + underpowered cluster epicenter (CRITICAL for the site's #1 topic)
`complete-guide-understanding-utility-bill`: H1/title renamed to "A Practical Workflow for Understanding Your Utility Bill" while slug, `keywords:` ("complete guide…understand utility bill"), homepage Essential-guides slot, and absorbed alias `/blog/how-to-read-your-utility-bill/` all still target the head term. Leanest flagship (9,024 bytes vs 17–29KB siblings), zero visuals, no FAQ/schema. (Lieutenant, verified.) The unpublished `how-to-read-your-utility-bill` draft (700w, good bones, 2 tables) is the un-executed consolidation partner. **Fix = rebuild per §8 Brief 5.**

### C3 — Data contradiction staged behind a publish gate (CRITICAL if published, cheap now)
Draft `2026-utility-cost-index-by-state` Quick Answer: **$262/month** national average. Live `average-utility-bills-by-state-2026`: **$375/month** (narrow basket, honestly defined). Hawaii FAQ on the live page also carries a $453-vs-$324 internal inconsistency (lieutenant). Publishing the draft without a single site-wide basket definition recreates SQ-045's #1 credibility crisis.

### C4 — Fact drift on a TOU money page (HIGH, YMYL — **REFUTED, final**)
`46-what-time-is-electricity-cheapest` (lines 37, 46, source[2]) attributes **22.33¢ off-peak / 44.97¢ peak** to Con Edison's residential TOU. Wave-2 verifier re-fetched the cited Con Ed page 2026-08-29: **no such values exist there**. Correct live figures: summer peak (Jun–Sep, 8am–midnight) **27.86¢**, other-months peak **17.11¢**, off-peak **5.22¢**, delivery 16.402¢, customer charge $21.00. The article's hour/period definitions ARE correct (CONFIRMED) — only the prices are wrong. Cascade error: the "roughly 50% off-peak discount" claim (line 56) holds only on the erroneous pair; the real discount is ~81% (vs summer peak) / ~70% (vs winter peak). **Wave-2 also confirmed:** $165/mo national math (900 × 18.34¢), MN cold-weather rule, and the draft state-index's Louisiana row arithmetic (84+65+25=$174, internally consistent — the draft's blocker is C3, not row math). **One dead citation found:** `acf.hhs.gov/ocs/programs/liheap` (LIHEAP page, returns empty).

### C5 — Draft-cluster execution debt (HIGH)
Four `draft: true` files, Commander-verified:
| Draft | Status | Correct action |
|---|---|---|
| `supply-vs-delivery-charges-electricity` | canonical → 24-; **24- also carries its slug as alias — URL collision if ever built with --buildDrafts** | **Delete** |
| `how-to-read-your-utility-bill` | good content; alias consumed by complete-guide | Fold into Brief 5, then delete |
| `gas-customer-charge-explained` | 17- already carries its alias and beats it (11.4KB, verified rates) | **Delete** |
| `2026-utility-cost-index-by-state` | contradicts live page (C3) | Archive outside `content/` until basket reconciled |

### C6 — E-E-A-T gaps on a money-adjacent site (HIGH, systemic but cheap)
- **Identity**: all 5 author pages honestly declare desk bylines + AI assistance (good) but carry **zero credentials and identical boilerplate** across all five (tracer; prospector scored each 5/6). Byline coverage is otherwise total (88/88 posts).
- **Editorial promises vs practice**: policy promises "direct, **dated** source links" — only ~40/84 sourced posts actually carry retrieval dates; **4 posts have no sources at all** (`ac-running-but-not-cooling`, `aux-heat-vs-emergency-heat`, `heat-pump-running-all-day-in-winter`, `mcf-vs-ccf-vs-therms`).
- **Corrections history**: policy promises "we note what changed"; the corpus contains **zero correction entries** — even though real corrections HAVE been made (e.g., SQ-067's DOE-link fix). The history exists in git, not on the site.
- **Recourse**: contact/corrections pages usable (mailto works) — weakest links are the above, not recourse.

### C7 — Uncited savings claims in buying-decision tables (HIGH, 8 quotes)
All in decision tables where readers choose upgrades (tracer, verbatim):
1. `average-utility-bills-by-state-2026.md:126` — "12 states implemented new conservation-tier pricing" (2026 claim, no citation)
2. same line — "drought surcharges of up to 30%"
3. `07-gas-bill-too-high.md:160` — window film "reduces heat loss by 40–70%"
4. `07-gas-bill-too-high.md:161` — thermal curtains claim
5–7. `44-how-to-lower-water-bill.md:104–107` — drip irrigation "30–50% reduction", mulch "20–30%", rain barrel "1,000–5,000 gal/yr"
8. `05-how-to-lower-utility-bills.md:85` — water-heater wrap "25–45% per DOE" (DOE cites ~25% for electric wraps; the 45% bound needs a source)

### C8 — Mechanical SEO debt (MEDIUM, bulk-fixable)
- **252 `<img>` tags without alt** (Commander-verified count) — all related-card tiles, ~3 per post. JSON-LD coverage otherwise strong (321/525 pages; Article×101, FAQPage×57).
- **112 blog titles >60 chars** (worst: 112 chars) — SERP truncation on exactly the long-tail queries the site wins.
- Homepage `<title>Utility Explained</title>` — no keyword (verified).
- `terms.md`: "Effective 2024-12-01" vs updated 2026-08-03; no dispute/jurisdiction/commercial terms on an Amazon-monetized site.
- 18 duplicate titles — all tag/category archives (`X | Utility Explained`), cosmetic.
- 24 alias-stub pages lack meta descriptions — cosmetic (they canonical away).

### Refuted worker claims (kept out of this report)
Wave-1 executor reported "108 blog posts missing from sitemap" and "24 posts with zero H1" — both artifacts of `grep -c` on single-line minified XML/HTML. Commander re-derivation: **sitemap 116 URLs incl. 92/88 live blog posts (all present)**; sampled posts all have exactly 1 H1. Prospector's "ContentImage may not render in Hugo" — refuted: renders as `<figure>` (8/7 figures verified). Mason's register inverted three canonical directions — corrected in §4.

---

## 3. Page-by-Page Audit

Deep-audited pages (prospector read 31 in full; lieutenant reviewed 14 in depth incl. rendered homepage). Scores: **quality / search-readiness** out of 10. Action labels per rubric. AI-slop confidence (low/med/high) shown where a signal was found.

### 3.1 Site & trust pages (12)
| Page | Q/R | Verdict + evidence |
|---|---|---|
| `_index` homepage | 9/8 | Strong rendered UX (single H1, dual CTA, trust strip, a11y). Fix: bare title tag; guide-count register drift (84 shown vs 85 published); aria-label duplicates. **retain** |
| about | 8/8 | Solid funding transparency; generic "how we're different." **retain** |
| contact | 7/8 | mailto works; no form. **retain** |
| corrections | 7/7 | Good policy; **zero demonstrated history** (C6). **improve-and-retain** — publish one worked correction |
| methodology | 7/7 | Formulas good; add dated verification log. **retain** |
| editorial-policy | 8/8 | Strong; practice gap is C6, not the page. **retain** |
| editorial-team | 7/7 | Honest desk framing; no photos/credentials. **improve-and-retain** |
| affiliate-disclosure | 8/8 | FTC-appropriate. **retain** |
| privacy-policy | 8/8 | GA4/Rybbit/Consent-Mode specifics present. **retain** |
| disclaimer | 6/6 | Date contradiction (2024-12-01 vs 2026-08-03). **improve-and-retain** |
| terms | 5/6 | Stale, thin, no dispute/jurisdiction/commercial terms (C8). **improve-and-retain** |
| search | 4/6 | Layout stub, noindexed — fine. **retain** |

### 3.2 Author pages (5)
All: Q5 R6, **improve-and-retain**. Identical templated boilerplate across all five (slop signal: **medium** — same AI-assistance footnote verbatim ×5), honest desk-byline disclosure, zero credentials, zero concrete examples. Fix: one flagship guide + one real cited source per desk; headshots optional but would help.

### 3.3 Hub pages (5)
| Hub | Q/R | Notes |
|---|---|---|
| utility-bills-costs-explained | 9/8 | **The model hub** (Quick Answer H2, component tables, FAQ schema). Add byline; funnel explicitly to the rebuilt complete-guide. |
| electricity-explained | 8/7 | Best worked math; missing Quick Answer block; duplicate links to same slugs under different anchors (01- and 24- ×2, 03- ×3). |
| gas-explained | 8/7 | Therm math solid; $1.50/therm example unanchored vs $1.91 EIA cited elsewhere. |
| water-explained | 8/7 | Excellent unit chain (CCF→gal); ccf-calculator not linked from units section. |
| heating-cooling-explained | 8/7 | Densest hub; repair-vs-replace needs a numeric decision table; missing duct-leaks cross-link. |

All hubs: **improve-and-retain**; systemic gaps — no byline/updated line in body (template fix), no ItemList schema on hub cards.

### 3.4 Flagships & guides (lieutenant deep reviews)
| Page | Q/R | Verdict |
|---|---|---|
| how-to-lower-electric-bill-complete-guide | 9/9 | Model page. Nit: $144 (2024) vs $165 (18.34¢×900) reconciliation. **retain** |
| 07-gas-bill-too-high | 9/8.5 | Duplicate front-matter source entries; 65F/55F line needs labeling. **retain** |
| how-to-dispute-utility-bill | 9/8.5 | YMYL-correct. Add FAQ schema (most question-shaped page has none). **improve-and-retain** |
| average-utility-bills-by-state-2026 | 8.5/8.5 | Best Quick Answer on site; Hawaii FAQ $453-vs-$324 fix; formatting hygiene. **improve-and-retain** |
| 30-sudden-spike | 8.5/8 | FAQ heading but no faq-schema (grep-confirmed); steps 11–12 duplicate dispute page — compress + handoff link. **improve-and-retain** |
| moving-utilities-checklist | 7.5/7.5 | **C1 defect**; sources thin (bare dominionenergy.com). Fix defect, then **retain** |
| complete-guide-understanding-utility-bill | 7.5/7.5 | C2. **rewrite** (Brief 5) |

### 3.5 The weak short tail (prospector full reads + briefs)
| Page | Q/R | Slop signal | Action |
|---|---|---|---|
| 24-delivery-charge-vs-supply-charge | 7/7 | low — "Keep the bill, tariff version, offer terms…" boilerplate | **rewrite** (Brief 1 — it WINS the cluster; both would-be rivals are drafts/canonicalled into it) |
| duct-leaks-symptoms | 6/7 | low — "There is no universal repair, savings percentage, or price for duct leakage." | **rewrite** (Brief 2 — title promises symptoms the body refuses to list; slug promises runtime it doesn't cover) |
| drought-surcharge | 7/8 | **med** — "Do not assume a drought charge is a fine, applies only to outdoor use, uses one national tier…" (negation-list pattern) | **rewrite** (Brief 3) |
| why-is-my-furnace-blowing-cold-air | 8/8 | none — "the shard's best page" on safety spine | **rewrite-lite** (Brief 4: keep spine verbatim, add the 15-min check table + cost bands) |
| net-metering-explained | 7/7 | low — generic Q&A lines | **expand** (zero dollar figures on a YMYL solar topic; add one state credit example) |
| 46-what-time-is-electricity-cheapest | — | — | **expand + correct** (C4 fact drift; thin for high-intent TOU query) |
| 10-fixed-vs-variable-utility-rate | 8/8 | none | **expand** (real comparisons thin at 868w) |

### 3.6 Representative strong tail (verified retain, evidence-based)
`why-is-my-furnace` safety spine; `which-rate-plan-is-right-for-me` Q8 R8 (decision framework, real 18.3¢ EIA + PG&E tariff — **do NOT consolidate with 10-**, intents are distinct); `ccf-calculator` (interactive tool, EPA-sourced); `what-is-a-kilowatt-hour` (worked appliance math); `10-fixed-vs-variable` (TX/PA/OH portals, break-even math). Full 110-row disposition in §4.

### 3.7 AI-slop assessment (sitewide)
**Overall confidence: LOW slop risk.** The corpus reads edited, source-forward, and structurally varied (tables, calculators, Quick Answers, flowcharts). The one systemic pattern — the **de-hallucination overcorrection** (lieutenant): the 2026-08-23 batch of short pages hedge every sentence and carry zero figures/named utilities, reading as evasive rather than careful next to exemplar 17-. The negation-list tic (drought-surcharge quote above) is the visible symptom. Author-page boilerplate ×5 is the other low-grade signal. No unsupported-superlative pattern found in prose (tracer's grep sweeps); the 8 real violations sit in tables (C7).

---

## 4. Thin and Generic Content Register

Full register: `.squad/SQ-068/artifacts/register-thin-generic.md` (110 rows: page | words | cluster | action | reason). **Commander-corrected action distribution** (mason's table with draft-status and canonical-direction fixes applied):

| Action | Count | Pages |
|---|---|---|
| retain | 86 | all site/hub/author pages + well-served posts (incl. all YMYL rule pages, calculators, comparisons) |
| improve-and-retain | 12 | 03, 04, 05, 08, 13, 14, 27, 49, how-to-lower-electric-bill-without-solar, why-did-my-utility-bill-go-up, summer-water, winter-water, dispute (FAQ schema) |
| rewrite | 5 | complete-guide (C2), 24-delivery, duct-leaks, drought-surcharge, furnace (spine-preserving) |
| expand | 3 | net-metering, 46-cheapest (also C4), 10-fixed-vs-variable |
| remove-or-noindex | 4 | the three dead drafts + state-index draft (C5; archive state-index until C3 reconciled) |
| redirect / consolidate | 0 | nothing new — prior consolidations already executed via aliases; directions that mattered are handled in C5/Briefs |

**Near-duplicate groups to watch (differentiate, don't merge):** summer/winter water pair (cross-link + season-specific intent); 05/44/without-solar trio (link-differentiate); read-your-bill set (solved by Brief 5 making complete-guide the definitive epicenter with 01- owning "electric" specifically).

---

## 5. Visual Content Plan

Full 20-entry plan with asset type, placement, confusion-resolved, original/sourced/designed, and alt-text direction: `.squad/SQ-068/artifacts/visual-plan-candidates.md`. Priorities:

1. **Annotated sample bill** (04-hidden-fees; also reusable in Brief-5 flagship) — maps fee labels to bill positions; the single highest-leverage asset on the site.
2. **Delivery-vs-supply comparison table + annotated bill split** (24-delivery, Brief 1).
3. **15-min interval demand curve** (49-demand-charges).
4. **24-hour TOU price curve** (08 + 46 — doubles as the correction vehicle for C4).
5. **Heat-pump vs furnace savings calculator** (48 — local-rate inputs; matches the site's calculator pattern).
6. **YMYL trust pair**: shut-off rules by state table (can-utility-shut-off) + LIHEAP eligibility calculator (utility-assistance-programs).

No decorative stock anywhere in the plan; every entry maps to a purchase, comparison, eligibility, or diagnosis decision the page already asks readers to make. Plus: build the two moving-checklist images whose prompts currently leak (C1) — timeline belt + overlap-cost comparison.

---

## 6. Internal Linking & Topic-Cluster Plan

Ground truth (Commander link-map over all markdown bodies + rendered integrity check): **342 distinct internal hrefs, all resolve; zero live orphans** (the only zero-in-link pages are the three C5 drafts). Sitemap complete for all live posts.

**Cluster map:** 9 clusters — electric-bill (21), bills/fees (24), water (15), HVAC (13), gas (8), meters (5), data/state (2), product guides (4), assistance/YMYL (3) — each anchored by a hub (nav-linked) except data/state and product guides, which lack pillars.

**Prioritized fixes:**
1. **Funnel the flagship**: utility-bills-costs-explained hub → complete-guide (rebuilt) explicit funnel; homepage Essential-guides already slots it. (C2 dependency.)
2. **Under-linked money page**: `how-to-lower-electric-bill-complete-guide` has only 2 contextual in-links (Commander count) — add contextual links from 03, 30-sudden-spike, phantom-power, smart-plugs ("full savings workflow" anchors).
3. **Link the calculators in-context**: ccf-calculator from water-explained units section + tiered-water-rates; ev-charging calculator from 46/08.
4. **Cross-links flagged by wave 1**: heating-cooling hub ⇄ duct-leaks; heat-pump-running-all-day ⇄ duct-leaks (runtime siblings); 13-ac-short-cycling ⇄ furnace-cold-air.
5. **Cannibalization adjudication** (twin_q, Commander-reconciled with draft ground truth): read-your-bill set → complete-guide wins generic, 01- wins electric-specific, `electric-bill-breakdown` differentiates as line-item reference (link, don't merge — it's 2,609w and comprehensive); delivery/supply → resolved by C5 deletions + Brief 1; customer-charge → resolved by C5; state-data pair → resolved by C3 gate (one live page only); high-bill sprawl (23+ pages) → no forced merge, but add a "diagnose your high bill" hub block on utility-bills-costs-explained linking 03/06/07/30/why-did-my…/water-suddenly (twin_q Blocker 5).
6. **Anchor hygiene**: electricity-explained hub links same slugs 2–3× under different anchors — dedupe; glossary "see more" references are plain text — hyperlink them (prospector).

---

## 7. Prioritized Roadmap

### Fix Immediately (≤1 day, ~2–4 hrs total)
| # | Task | Effort | Impact |
|---|---|---|---|
| 1 | Delete `## Image Prompts` from moving-utilities-checklist + rebuild public | 5 min | Removes live professionalism/trust damage (C1) |
| 2 | Correct page-46 Con Ed TOU figures to live tariff (or re-attribute) + date-stamp | 30 min | Kills a wrong money figure (C4) |
| 3 | Delete drafts: supply-vs-delivery, gas-customer-charge; archive state-index draft outside content/ | 15 min | Kills collision hazard + C3 publish-gate (C5) |
| 4 | Homepage `<title>` → "Utility Bill Guides: Electricity, Gas & Water Explained | Utility Explained" | 5 min | SERP CTR on every impression |
| 5 | Source-or-soften the 8 uncited table claims (C7) | 1–2 hrs | YMYL integrity in decision tables |

### Improve Next (1–2 weeks)
1. **Brief 5 flagship rebuild** (title realignment, annotated bill, worked $164.84 example, FAQ schema) — unlocks the cluster.
2. **Briefs 1–4** (24-delivery, duct-leaks, drought-surcharge, furnace) — the weak tail at house-exemplar standard.
3. **Retrieval-date backfill** on ~44 bare-URL posts + sources for the 4 sourceless posts — closes the policy-vs-practice gap (C6).
4. **Alt text on 252 card images** (template fix: card alt = guide title) + title-length trim on the worst ~30 over-60 titles.
5. **Trust layer**: one dated corrections-log entry on corrections.md (seed with the SQ-067 DOE-link fix); author pages get one concrete example guide + one real source each; terms.md modernized; hubs get byline/updated template line.
6. Hawaii FAQ reconciliation ($453/$324) + $144/$165 flagship nit + duplicate source entries on 07.

### Build Over Time (3–6 weeks)
1. Visual plan top-6 (§5) at ~2/week — start with the annotated bill (reused 3×).
2. Heat-pump calculator + LIHEAP eligibility checker (the site's calculator pattern is proven).
3. "Diagnose your high bill" hub block + data/state pillar decision post-C3.
4. Bing→Google bridge: the KPI baseline shows Google ~0% (sandbox) — the fact-fixes + schema here are exactly what lifts it; re-baseline affiliate clicks once Rybbit quota resets.
5. Title systemization (template-enforced 30–60 chars) and ItemList schema on hub cards.

---

## 8. Rewrite Briefs (5, writer-ready)

*Full briefs with section-by-section structure, named fetchable sources with retrieval-date instructions, math to include, visuals, link maps, and measurable done-bars — distilled from wave-2 lieutenant (sources verified against wave-1 fetches where overlapping).*

**Brief 1 — `24-delivery-charge-vs-supply-charge-utility-bill`** (definitive cluster winner). Audience: bill-payers confused by the two buckets + deregulated shoppers. Structure: Quick Answer decision rule → two-bucket table (covers | rate basis | who sets | shoppable?) → **verified 3+-utility split table** (ConEd, National Grid MA, Columbia Gas OH SCO, papowerswitch) → regulated-vs-deregulated → worked 899 kWh × 18.34¢ = $164.84 month split by a named tariff's own numbers → FAQ. Sources: EIA EPM Table 5.6.A (18.34¢, wave-1-verified), utility rate pages, fetch-and-date each. Visual: color-coded annotated bill. Done bar: dated 3+-utility table with where-published column, worked split, FAQ schema, ≥8/10 re-audit.

**Brief 2 — `duct-leaks-symptoms-hvac-running-all-day`** (intent realignment). Deliver the promised 7–9 symptom list (uneven rooms, weak far-register flow, dust streaks at joints, runtime+bill climb at same settings, visible kinks/torn flex, whistling returns), DIY observation checklist, what a pro measures (duct-blaster CFM25, blower door), mastic vs cloth-duct-tape, leakage stats only as ENERGY STAR/DOE published (verify exact wording, else omit). Include labeled-arithmetic runtime table (15%/30% loss → 1.18×/1.43× runtime). Links in from heating-cooling hub + furnace page. Done bar: symptom list matches keywords, ≥1 dated leakage source, FAQ schema, ~900w.

**Brief 3 — `drought-surcharge-on-water-bill-explained`**. Name the 3 forms (fixed % uplift / stage-tier penalties / budget-based excess). **Verified 2–3-utility drought-rate table** (San Jose Water, Marin Water, Austin Water): stage trigger, tiers hit, %/$ uplift, where published. Worked before/after: 6 CCF (4,488 gal — the site's own unit chain) under normal vs drought schedule, compute the delta. Distinguish drought charge vs excess-use fine vs tier creep; leak adjustment ≠ drought relief. Done bar: ≥1 dated named-utility dollar table + computed delta, hedges cut, ~900w.

**Brief 4 — `why-is-my-furnace-blowing-cold-air`** (spine-preserving). Keep the CPSC safety block verbatim. Add: 15-minute check table (HEAT vs FAN-ON, filter inspect, breaker/switch, intake, CO alarm test), causes with DIY-vs-pro column (filter→limit-switch, condensate lockout on 90%+ furnaces, ignition faults), dated cost bands from one fetched source (Angi/HomeGuide; if unfetchable, no dollar bands), AFUE/lifespan from DOE Energy Saver, no rebate promises (25C ended 12/31/2025 — verified). Done bar: ≥3 concrete figures, dated cost table, safety block unchanged, ~1,000w.

**Brief 5 — `complete-guide-understanding-utility-bill`** (flagship rebuild). Retitle back to the "Complete Guide…" family (slug/keywords already there). Keep the 5-step workflow + charge-mapping table. Add: annotated mock bill keyed to the charge map; verified worked bill (electric 899×18.34¢=$164.84 [EIA, verified], gas ~80 therms × EIA residential price, water 6 CCF block-structure anchored on EPA WaterSense — each component labeled verified vs illustrative); 5+ FAQ with schema; national-average context box linking average-utility-bills-by-state-2026. Convert 3 bare DOE PDF URLs to dated convention. Done bar: title/slug/keywords aligned, first-time reader maps every line of their bill without leaving the 5 steps, ≥1 verified-dollar breakdown, ≥2 visuals, FAQ schema, ≥8/10.

---

## 9. Final Checklist (first actions)

- [ ] Delete `## Image Prompts` from `content/blog/moving-utilities-checklist.md` (line ~152) and rebuild/deploy — **5 minutes, live defect**
- [ ] Fix page 46 Con Ed rates to the live tariff (27.86/17.11/5.22¢, fetched 2026-08-29) or re-attribute; add retrieval date
- [ ] `git rm` drafts `supply-vs-delivery-charges-electricity` + `gas-customer-charge-explained`; move `2026-utility-cost-index-by-state` out of `content/` until the $262/$375 basket is reconciled site-wide
- [ ] Homepage title tag rewrite
- [ ] Source or soften the 8 uncited savings claims (§2 C7 list — paths + line numbers ready)
- [ ] Kick off Brief 5 (flagship) — everything else in the bill-reading cluster depends on it
- [ ] Backfill retrieval dates on the ~44 bare-URL posts; add sources to the 4 sourceless posts
- [ ] Card-image alt-text template fix (252 instances)
- [ ] Publish the first corrections-log entry (use the SQ-067 DOE-link fix)
- [ ] Re-run `hugo` + sitemap sanity check after deletions; confirm 3 aliases still resolve

---

## Audit scope & confidence statement

Covered: all 110 content pages (45 read in full by specialist seats; the remainder structurally scanned for the register with boundary spot-reads), full rendered build, sitemap/robots, schema, analytics baseline. Not covered: server logs, Google Search Console (not connected), Bing Webmaster query data, backlink profile, E-E-A-T of competitor head-to-heads beyond sampled comparisons. Two worker headline claims were disk-refuted and excluded; all load-bearing claims in this report carry disk verification or multi-seat corroboration. Wave-2 verifier's 13-item scorecard is folded into §2 (5 CONFIRMED, 1 REFUTED with corrected figures, 6 UNVERIFIED-for-budget, 1 dead link — full envelope in `.squad/SQ-068/results-w2/02-verifier.json`); §6 stands on the Commander-derived link-map (method inline) — cartographer's independent map, if salvaged, lands in `.squad/SQ-068/results/`.
