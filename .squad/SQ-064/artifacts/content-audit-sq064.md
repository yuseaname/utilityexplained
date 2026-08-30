# SQ-064 — Full-Scale Content Audit: The Five SQ-063 Campaign Pages

**Site:** utilityexplained.com · **Audit date:** 2026-08-30 · **Auditor:** ZCode (Commander), THE SQUAD v4.2.1
**Scope (operator order):** ONLY the five campaign pages shipped 2026-08-29. No other page received an audit entry; other pages appear solely as link targets and cluster context.

| # | Page | Live URL |
|---|---|---|
| A1 | Do Home Energy Monitors Save Money? | /blog/do-home-energy-monitors-save-money/ |
| A2 | Do Thermal Curtains Really Work? | /blog/do-thermal-curtains-really-work/ |
| A3 | What MERV Rating Do I Need? | /blog/what-merv-rating-do-i-need/ |
| A4 | Point Sensor or Whole-Home Shutoff? | /blog/point-sensor-vs-whole-home-water-leak-when-to-upgrade/ |
| A5 | How to Find and Seal Drafts in Your Home | /blog/how-to-find-and-seal-drafts-in-your-home/ |

**Method.** Nine squad seats audited by angle (Lieutenant GLM editorial · prospector/tracer/cartographer/verifier/mason dsv4 wing · twin_q qwen cold verdict · executor local mechanical · scout local recon), over a Commander-extracted mechanical ground-truth layer (titles, metas, headings, image bytes/dims, link graphs, schema — machine-parsed from the Hugo render). Two seats failed (prospector, mason — protocol deaths) and their angles were absorbed and re-verified Commander-side; scout landed partial with its gaps closed mechanically. Every number below traces to the ground-truth sheets (`/tmp/sq64/sheets/`), a quoted grep, or worker evidence the Commander disk-checked. All prices/availability in the articles were verified against live Amazon pages on 2026-08-30 during SQ-063.

**What would make this audit more complete:** Search Console (impressions/CTR/position per URL), Rybbit analytics (the site's own affiliate_click and scroll events), Amazon Associates reports (EPC per ASIN), and 4+ weeks of post-publish rank data. None existed at audit time; all findings below are on-page and corpus-derivable.

---

## 1. Executive Summary

**Strongest assets.** The five pages are, editorially, the strongest cohort on the site. Both uncorrelated auditor brains (GLM lieutenant, cold qwen) scored content quality 7.0–9.0 with zero classic AI-slop and a unanimous "people-first" verdict: every page states mechanism before product, every page tells the reader when NOT to spend, and several refuse to invent savings percentages competitors fabricate. The fact-check seat re-derived ~35 load-bearing claims against the articles' own Sources lists and found **zero refutations**; citation integrity ([n] ↔ Sources, both directions) passes on all five pages; bylines, author pages, dates, disclosure placement, and retrieval dates are present on all five.

**Biggest risk — and it is not editorial.** A wiring-pass artifact left **26 malformed single-brace `{< ... >}` shortcodes** across the five source files (9 product-boxes + 17 visuals). Hugo renders them as literal raw text on the live site. Consequences, all mechanically verified: **17 in-body images do not display** (every page shows only its hero plus related-card thumbnails), **9 of 14 affiliate product boxes are dead** (A1, A2, A5 render ZERO boxes — three monetized pages with no functioning purchase module; A3/A4 render boxes but also leak broken duplicates — three on A4 — as visible markup garbage), and raw `{< product-box ... >}` text is printed to readers in the middle of buying decisions. The defect was independently discovered by the Commander's ground-truth extraction AND by the cold twin_q seat (which was given no hint) — the finding is doubly confirmed.

**Likely search-visibility blockers.** (1) The rendering defect itself — pages that print template seams don't earn trust signals, and the images' alt text (a planned search-entry surface) never enters the rendered DOM. (2) Title-tag overruns: 92c (A4), 88c (A3), 75c (A5) truncate their differentiators in SERPs; og:titles mirror the excess. (3) Editorial inbound links are far thinner than they appear: raw inbound counts of 5–11 are mostly automatic Keep-Reading cards; genuine in-body editorial inbounds are 1–3 per page, A4 and A1 receive zero links from their campaign siblings. (4) Two live Sources entries print internal operations language ("SQ-063 product dossier…") on consumer trust surfaces.

**The 3–5 improvements most likely to create meaningful results:**
1. Repair the shortcodes (21 conversions + delete 5 duplicate box blocks), add a rendered-HTML lint to the build gate, redeploy (≈1 hour, reverses the single largest trust/conversion leak).
2. Rewrite the three over-length titles (A4/A3/A5) and trim all metas to ≤150c.
3. Execute the editorial inbound wave: 8 specific one-line links identified in §7 (including two water-cluster pages that share A4's exact ASIN and source but never link it).
4. Run the A3 line-edit pass (the campaign's only genuine prose-slop cluster) and the A4 de-tic pass.
5. Scrub the two ops-language Sources entries and restate the nine externally-living figures inside their source annotations.

**Ratings (Commander-adjudicated from both auditor scores + mechanical state).** SEO scores reflect the live broken state; the same pages post-fix would rate 1.5–2.5 points higher.

| Page | Quality /10 | SEO-readiness /10 | Action |
|---|---|---|---|
| A1 energy monitors | 8.5 | 6.0 | Improve and keep indexed |
| A2 thermal curtains | 8.0 | 6.5 | Improve and keep indexed |
| A3 MERV rating | 7.0 | 5.5 | Improve and keep indexed (deepest line edit) |
| A4 leak ladder | 7.5 | 5.0 | Improve and keep indexed (weakest search-readiness) |
| A5 draft sealing | 8.0 | 6.0 | Improve and keep indexed |

No page merits noindex, merge, redirect, or rewrite-from-scratch. All five are improve-and-keep.

---

## 2. Critical Issues (severity-ordered)

**C1 — P0 — Malformed shortcodes render as raw text on production (all 5 pages).**
26 single-brace `{< visual … >}` / `{< product-box … >}` leaks (A1×6, A2×4, A3×5, A4×6, A5×5 — grep-verified in rendered HTML; 9 boxes + 17 visuals). 17 in-body images dead; 9 of 14 boxes dead; 5 duplicated box blocks on A3/A4 print escaped markup mid-article. Reader-impact: the A3 page shows both product boxes rendered, then the same two boxes again as `{&lt; product-box asin=…` text (A4 does it three times); the A5 how-to — the most image-dependent format on the site — is, in tracer's verdict, "functionally blind." The build gate is blind to it: `npm run verify` exits 0 because the images exist and the text parses. **Fix: `{<` → `{{<` (21 instances), delete the 5 duplicated box blocks (A3 lines 103/105, A4 lines 44/102/104 — the doubled Govee/Flume/Moen boxes), add a post-build lint `grep -r '{&lt;' public/` that fails CI, rebuild, redeploy.**

**C2 — P0 — Monetization is dead on 3 of 5 pages.**
A1 (0 of 2 boxes render), A2 (0 of 1), A5 (0 of 1) have no functioning purchase module; their only live Amazon touchpoints are plain text links. A4 — the page built around a $60-vs-$560 decision — carries its dollar comparison only inside boxes and one table, and the tracer flagged that the decision moment "depends entirely on the render-fragile product boxes." This is the campaign's revenue engine running at ~36% (5 of 14 boxes) with visible damage on the rest.

**C3 — P1 — Internal operations language on live trust surfaces (A1, A5).**
A1 Source 7 prints "SQ-063 product dossier, section E1. Retrieved August 30, 2026." A5 Source 4 prints "SQ-063 product dossier — tracer-confirmed live price bands…" (verified in rendered HTML). Internal ticket vocabulary in the citation block — the most scrutinized real estate on a YMYL-adjacent page — reads as process leakage, not transparency. Rephrase as retailer-checked price bands (the underlying data is sound; the verifier confirmed every band traces).

**C4 — P1 — Title-tag and og:title overruns (A4, A3, A5).**
A4 92c ("…| Utility Explained" tail consumes the space; "Leak Protection" differentiator truncates), A3 88c (the dirty-filter hook — its second keyword — is invisible in SERP), A5 75c with "(Room-by-Room)". og:titles mirror at 72c/68c. Metas sit at 151–156c across the set (mobile truncates ~120c; the free-app/DOE-AERC hooks cut mid-thought). A1 55c and A2 52c are the models to match.

**C5 — P1 — Editorial inbound links are 1–3 per page, not 5–11.**
Raw inbound counts (5–11) are dominated by automatic Keep-Reading cards. True in-body editorial inbounds: A1×3 (03, 05, 11), A2×1 (07), A3×2 (13, ac-running), A4×2 (06, 44), A5×2 (05, 47). No campaign sibling links A1 or A4 at all. The cluster's strongest decision pages are its weakest-linked.

**C6 — P2 — A5 title/content mismatch.**
"(Room-by-Room)" promises a room-keyed structure; the page is organized by gap type (attic hatch → rim joist → outlets…). Either add a short room-index or drop the parenthetical (also fixes the length).

**C7 — P2 — A3 citation hygiene.**
Sources 1 and 2 are the same EPA URL twice (definition vs. guidance framing); A2's Source 3 is a non-link stub ("no primary study identified") that looks unresolved rather than scrupulous.

**C8 — P2 — Prose-discipline patterns (full list §5).**
A3 carries the campaign's only genuine sentence-slop cluster; A4 repeats its bottom line three times and narrates its own SEO ("The search says 'Flume vs. Moen Flo'…"); A5 echoes price bands 3–4×; A2 runs 8+ aphorisms in 2,566 words.

**C9 — P3 — Two orphan images = two unwired planned visuals.**
A2 `treatment-comparison-strip.webp` (1693×929, 69KB) and A5 `renter-toolkit-flatlay.webp` (1536×1024, 78KB) exist on disk, referenced nowhere. They were the planned visuals for exactly the two sections tracer/Lt flagged as under-supported (A2 alternatives comparison, A5 renter toolkit). Wire or delete.

**C10 — P3 — Build-gate blind spot (systemic).**
`content_quality_audit.py` and `check_image_paths.py` both pass on text that leaks shortcodes. The rendered-output layer is untested. One grep in CI closes it permanently (see C1).

---

## 3. Page-by-Page Content Audit

### A1 — /blog/do-home-energy-monitors-save-money/ (2,362 source words · Electricity · David Chen)
- **Purpose / intent:** "Do home energy monitors save money" — commercial-investigational with a skepticism edge. **Fit: strong.** Quick Answer returns the honest verdict in one line ("No monitor lowers a bill by itself — it finds the changes that do") and the page handles the free-utility-app competitor, the renter path, and a 4-item skip list. "Emporia Vue vs Sense" intent is served by the comparison table (which does render) with an explicit no-link Sense row.
- **Quality 8.5 · SEO 6.0.** Best single idea of the campaign; held under 9 by two maxim-styled stretches that trade specificity for polish, and by a live page whose two CTAs and four mechanism diagrams are invisible.
- **Weaknesses:** both product boxes + 4 visuals dead; "SQ-063…section E1" in Sources; 156c meta truncates the free-app hook; "Comparing the Monitors" runs ~430 words of prose around its table with no winner/price summary sentence for a buyer who scrolls; CT-clamp jargon unglossed at first use for a bill-payer.
- **AI-slop signals: none.** Nearest miss — the four Behavior Bridge items share a two-beat "The data shows… / What you change:" skeleton; deliberate anaphora doing real work, not slop.
- **Visual gaps:** ct-clamp-anatomy is the must-render (the mechanism is spatial); renter-vs-owner-paths high; the other two supportive. Alt on ct-clamp over-specifies ("125.4 amps" reads like a generation prompt detail) — trim.
- **Action:** improve and keep indexed. Next 3: repair 6 shortcodes; rephrase Source 7; trim meta ≤150c keeping the free-app hook.

### A2 — /blog/do-thermal-curtains-really-work/ (2,042 words · Heating & Cooling · Margaret Harrington)
- **Purpose / intent:** "Do thermal curtains really work" — yes/no with savings expectation. **Fit: strong.** The three-tier evidence ladder (DOE ~15% of HVAC energy → AERC certified 5–16% → marketing "25–40% of window heat loss" downgraded to "up to 40% of what the glass loses, under a hang you may not have") answers the "really" literally.
- **Quality 8.0 · SEO 6.5.** Best sourcing discipline on the site; title 52c is the set's cleanest. Docked for maxim density (8+ one-liners per 2,566 rendered words reads performed), one filler forward-reference ("The film-kit row is its own future article"), and a buy-intent page whose only box never renders.
- **Weaknesses:** 0 boxes render (the single NICETOWN CTA is raw text); the three diagrams that carry the geometry argument (dead-air cross-section, right/wrong hang, seasonal clock) don't display — the prose leans on them; Source 3 stub; savings figures the searcher came for are buried in ~380 words of prose with no comparison table; "convection loop" unglossed.
- **AI-slop signals: none** (no templating, no stuffing — "thermal curtains" ×9 in 2,042 words is natural).
- **Visual gaps:** dead-air + fit-overlap are must-renders (the physics and the fit rules ARE visual); the orphaned treatment-comparison-strip belongs in the alternatives section. The savings-numbers section wants its DOE/AERC/marketing tiers as a small table or strip.
- **Action:** improve and keep indexed. Next 3: repair 4 shortcodes; format Source 3 properly; cut 2–3 quips and surface the three evidence tiers as a table.

### A3 — /blog/what-merv-rating-do-i-need/ (~2,100 words · Heating & Cooling · Roberto Mendoza)
- **Purpose / intent:** "What MERV rating do I need" + "does a clogged furnace filter increase electric bill." **Fit: strongest literal Q→A of the five** — the tier verdict lands in the first sentence and the second keyword owns an H2 and an FAQ.
- **Quality 7.0 · SEO 5.5.** The sizing section ("nominal is a rounded label, not a dimension") is genuinely expert, and refusing a dirty-filter percentage is a credibility win. But this page commits the campaign's only real text slop, and 88c title + 68c og:title hide its differentiator.
- **Weaknesses (beyond C1/C4):** sentence twin two paragraphs apart ("A filter decision is a breathing decision before a shopping decision" / "Your filter is a breathing problem before it's a shopping problem" — the locked DNA line got double-planted); "the manual is the ceiling" ×4 (including inside product-box copy); process voice in an FAQ ("not by a number we'll fabricate here"); uncited authority gesture ("independent review coverage, which frames flagship MERV-13-class picks…"); EPA URL duplicated as Sources 1+2; the sizing section — the article's own declared top priority — lost its tape-measure diagram to the defect.
- **AI-slop signals: YES — the set's only cluster** (items above, all quoted by the Lt and confirmed in source).
- **Visual gaps:** filter-size-measure must render (the page's own thesis); particle ladder + trade scale high. MERV ×66 in 2,100 words is topic-inherent (it IS the scale), not stuffing.
- **Action:** improve and keep indexed; this page needs the deepest line edit, not a rewrite. Next 3: delete 2 duplicate box blocks + repair 3 visuals; the de-slop pass (§5-A3); title ≤65c with the dirty-filter hook moved to meta.

### A4 — /blog/point-sensor-vs-whole-home-water-leak-when-to-upgrade/ (2,457 words · Water · David Chen)
- **Purpose / intent:** point-sensor vs whole-home / when-to-upgrade — comparison + decision. **Fit: strong** ("Point sensors tell you a leak started. A whole-home system sees the ones point sensors can't — and a shutoff valve acts when you can't"); the Flume-vs-Flo table serves the head-to-head keyword directly and honestly widens "vs" into "which rung does your house need."
- **Quality 7.5 · SEO 5.0 — weakest search-readiness of the set.** The risk-priced ladder ("retires the found-it-in-minutes risk; does nothing for walls, slabs, or the meter") is the campaign's most original commerce framing, and the renter section hands the reader a real script. Held back by: 92c title; only 2 editorial inbounds + zero campaign siblings; the stay-at-tier-1 verdict stated three times; on-page SEO meta-commentary ("The search says 'Flume vs. Moen Flo'; the honest comparison is 'watch versus act'" — a content-brief sentence in front of readers); three duplicated boxes printing as markup garbage beneath the table; all three decision visuals (spot-map, upgrade flowchart, priced-ladder tiers) dead.
- **AI-slop signals: patterns, not filler** — antithesis-template overuse ("a ladder, not a face-off" / "coverage, not gadget quality" / "visibility, not action"), verdict redundancy, the meta-commentary sentence.
- **Trust highlights (verifier-confirmed):** EPA leak arithmetic, both Amazon prices, the 95%-compatibility manufacturer-claim label, and Moen flow/pressure/temperature capabilities all trace to their Sources exactly.
- **Action:** improve and keep indexed. Next 3: delete 3 duplicated box blocks + restore 3 visuals; title ≤65c (e.g., "Point Sensor or Whole-Home Shutoff? When to Upgrade" — 52c); one de-tic pass, then the inbound wave of §7 (this page benefits most).

### A5 — /blog/how-to-find-and-seal-drafts-in-your-home/ (2,394 words · Heating & Cooling · Margaret Harrington)
- **Purpose / intent:** how-to with a parts-buying sub-intent. **Fit: strong** — detection kit → 10-stop tour → gap-to-product table → renter kit → never-seal → free list → two priced baskets is a complete do-it-this-weekend path, and the never-seal section answers the safety question competitors skip ("Anything the appliance manual says feeds combustion air never goes on the sealing list — not with foam, not with a rag, not 'just for the winter.'").
- **Quality 8.0 · SEO 6.0.** The most useful page in the set for a reader holding a caulk gun; the Detect/Seal/Renter-ok triplets are scannable and honest about failure modes. Docked for price-band echo across four sections, a Renter-ok clause delivered ~15×, the "(Room-by-Room)" over-promise, and — decisive here — a how-to that lost ALL four of its procedure diagrams plus its only box.
- **AI-slop signals: over-reinforcement, not filler** — bands recur verbatim ("$8–15 / $15–25" at stop 5, the table, and the basket; "breaker off, screws kept" twice); no buzzwords, no templated headings.
- **Visual gaps:** ten-spot-house-map and never-seal-these-map are must-renders (the tour is the spine; the hazard map backs a safety warning); detection-methods-trio high (procedures are visual); the orphaned renter-toolkit-flatlay belongs in the toolkit section. A small room-index strip would reconcile the title promise.
- **Action:** improve and keep indexed. Next 3: repair 5 shortcodes; scrub Source 4's ops language; reconcile title (room-index or drop the parenthetical) + one band-dedup pass.

---

## 4. Thin Content and AI-Slop Findings

**Thin content: none.** All five pages run 2,042–2,457 source words with original framing, verified facts, and decision infrastructure (tables, ladders, tours, skip-lists). A1/A4 exceed the 1,400–2,100 house band by ~10–15% — mild overage from duplication pressure (which the de-tic passes trim), the opposite problem of thinness. No doorway behavior, no near-duplicates (titles/metas unique — grep-verified), no placeholder text.

**AI-slop: one genuine cluster (A3), three pattern-level flags, otherwise clean.** Both uncorrelated brains concur no page "reads written-to-rank"; the Lt's verdict: "Every page states its mechanism before its product, every page tells the reader when NOT to spend."

| Page | Finding | Evidence (quoted) | Treatment |
|---|---|---|---|
| A3 | Sentence twin, 2 paragraphs apart | "a breathing decision before a shopping decision" ↔ "a breathing problem before it's a shopping problem" | Delete one (keep the locked DNA line in QA) |
| A3 | Motif ×4 | "the manual is the ceiling" (incl. inside box copy) | Keep 1–2 |
| A3 | Process voice in FAQ | "not by a number we'll fabricate here" | Rewrite straight |
| A3 | Uncited authority gesture | "independent review coverage, which frames flagship MERV-13-class picks…" | Cite or cut |
| A3 | Citation padding | Sources 1+2 = same EPA URL | Merge to one entry |
| A4 | Antithesis template overuse | "a ladder, not a face-off" / "coverage, not gadget quality" / "visibility, not action" | One per section max |
| A4 | Verdict ×3 | "permission slip to stay at tier 1" ↔ "not a compromise — it is the correct final answer" | Keep the permission-slip line |
| A4 | SEO meta-commentary | "The search says 'Flume vs. Moen Flo'…" | Delete |
| A5 | Band echo ×3–4 | "$8–15… $15–25" at stop 5 / table / basket | Bands live in the table only |
| A5 | Micro-phrase echo | "breaker off, screws kept" ×2 | Keep once |
| A2 | Maxim density | 8+ aphorisms per page ("Spend the money on the tape measure, not the tag") | Cut 2–3 |
| A1 | Deliberate anaphora (not slop) | Behavior Bridge "The data shows… / What you change:" ×4 | Keep — it works |

One chassis-level note: all five front matters carry the same 4-keyword array shape led by the exact primary question — invisible to readers, but worth varying as the site scales.

---

## 5. Visual Content Opportunities

**Tier 1 — restore the 17 dead images (fix, don't regenerate — files verified on disk, all webp, 60–80KB):**

| Rank | Must-render (page loses the concept without it) | Why |
|---|---|---|
| 1 | A5 ten-spot-house-map | The "10-Spot Tour" is the article's spine; without it the how-to is blind |
| 2 | A5 never-seal-these-map | Backs a safety warning (combustion air / weep holes) |
| 3 | A2 dead-air-cross-section | The entire physics argument is spatial |
| 4 | A2 fit-overlap-right-wrong | The fit rules ARE visual (wrong vs right hang) |
| 5 | A5 detection-methods-trio | Hand/smoke/flashlight are procedural techniques |
| 6 | A1 ct-clamp-anatomy | "What is a CT clamp" is unteachable in prose alone |
| 7 | A3 filter-size-measure | The page's own thesis: sizing beats rating debate |
| 8 | A4 coverage-ladder-tiers | The priced decision core ($60/$200/$560 in risk terms) |
| 9 | A2 seasonal-operation-clock | The 4-season operating matrix |
| 10 | A3 capture-vs-airflow-balance | The signature trade |
| 11 | A3 merv-particle-ladder | The tier concept (8/11/13 as ascending steps) |
| 12 | A1 renter-vs-owner-paths | The two-lane distinction |
| 13 | A4 upgrade-decision-flowchart | The 5-signal gate |
| 14 | A4 point-coverage-spot-map | Placement-coverage concept |
| 15 | A5 gap-to-seal-matching | Gap types → product classes (backs the matching table) |
| 16 | A1 bill-anomaly-flowchart | Supportive (3 bill shapes) |
| 17 | A1 behavior-bridge-loop | Supportive (restates the text list) |

**Tier 2 — wire the 2 orphans (zero new generation needed):** A2 treatment-comparison-strip → Alternatives section; A5 renter-toolkit-flatlay → Renter's Toolkit section. Both files exist, correctly sized, referenced nowhere.

**Tier 3 — new visuals, only where they earn their place:**
- **A2 savings-numbers table/strip** — the DOE/AERC/marketing tiers as a small comparison graphic in "What the Savings Numbers Actually Measured" (the exact numbers a searcher came for, currently prose-buried). Placement: after the third paragraph. Alt direction: "Three evidence tiers for thermal-curtain savings, from DOE factsheet to certified ratings to marketing claims."
- **A4 priced-ladder graphic** — three rungs with $60/$200/$560 and what each retires; placement: beside "The Coverage Ladder, Priced." Alt: "Three-tier leak-protection ladder priced at sixty, two hundred, and five hundred sixty dollars."
- **A5 room-index strip** — which of the 10 spots occur in which room; reconciles the title promise. Alt: "Home cutaway indexing the ten leak spots by room."
- **A1:** needs no new visual — its comparison table renders; trim the ct-clamp alt ("…reading of 125.4 amps" → drop the fake-precision number).

**Image hygiene:** in-body webp at 1536×1024/60–80KB is excellent; heroes eager + cards lazy is correct; empty-alt related-card thumbnails are decorative and acceptable (site-wide widget pattern); product images all correctly prefixed "Illustrative" — keep that honesty convention.

---

## 6. Internal Linking and Topic-Cluster Opportunities

**Cluster map (cartographer, corpus-grounded):** Heating & Cooling is the one genuine interlinked cluster — A2↔A3↔A5 all cross-link — but it rides on automatic cards; its editorial stitching is 1–2 links per page. Electricity (A1) and Water (A4) are single-page spokes: no campaign sibling links either, and neither links a sibling. The connective tissue the cluster lacks is `do-programmable-thermostats-cut-heating-bills` — all three H&C pages auto-link to it while it editorially links none of them.

**Missed editorial inbounds (highest-value first):**
1. `water-meter-running-when-no-water-used` → **A4** — it sells the SAME Govee ASIN (B0DQLFC3Q6, in its own product box) and never links the upgrade-decision page. Anchor: "point sensors vs. whole-home shutoff." Link both directions.
2. `water-meter-leak-indicator-explained` → **A4** — shares the EPA WaterSense leak-device source; the meter-indicator page is the natural "found waste, now what" predecessor. Anchor: "when to upgrade from a point sensor to whole-home protection."
3. **A2 → A5** editorial in-body (currently card-only) — the window-insulation sibling should hand the reader to the draft tour. Anchor: "seal the drafts the curtains can't."
4. **A3 → A5** already links 47-audit; add A5 as the fix-path companion. Anchor: "find and seal the gaps around a leaky house."
5. Campaign spokes: **A5 → A1** (measurement complements sealing — "measure what the fixes saved") and **A5 or A1 → A4** (water-side ladder for the reader who seals then monitors).

**Reciprocity gaps (one-line return links):** A1 → 03-spike and 05-lower-bills (both link in editorially; A1 returns neither); A4 → 06-water-bill-too-high; A2 → 42-space-heater, ductless-mini-split, furnace-cold-air.

**Cannibalization: clean.** Emporia's ASIN appears in 7 files, but the intent division is real (monitor-question vs spike-diagnosis vs complete-guide) — judged low-risk, no rewrite. A3's filter ASINs appear nowhere else. The only self-competition is A3/A4's duplicated box blocks (fixed by C1).

**Indexation surface (scout recon + Commander greps):** all 5 in sitemap.xml with self-referencing canonicals; robots.txt clean, no disallows; no noindex/nofollow; homepage, all three hub pages, dedicated tag pages (thermal-curtains, merv-rating, leak-detector, smart-shutoff, air-sealing, drafts, winter-prep…), categories, and pagination all carry the five. Article + FAQPage + BreadcrumbList JSON-LD on every page; twitter:card present. Structurally, these pages are fully surfaced — the visibility ceiling is on-page, not indexation.

---

## 7. Priority Action Plan

### Fix Immediately (today — one commit, ~1 hour, redeploy)
| # | Action | Impact | Effort |
|---|---|---|---|
| 1 | Repair 21 `{<` → `{{<` + delete 5 duplicate box blocks (A3 103/105, A4 44/102/104) | Restores 17 images, 4 boxes; removes visible markup garbage from every page | 20 min |
| 2 | Add rendered-HTML lint to CI: fail on `{&lt;` in public/ | Defect class can never ship again | 10 min |
| 3 | Scrub ops language from A1 Source 7 + A5 Source 4 | Removes internal vocabulary from trust surfaces | 10 min |
| 4 | Titles: A4 ≤65c, A3 ≤65c (hook to meta), A5 drop "(Room-by-Room)"; metas ≤150c | Recovers SERP differentiators on 3 pages | 20 min |

### Improve Next (this week)
| # | Action | Impact | Effort |
|---|---|---|---|
| 5 | Editorial inbound wave: the 5 missed inbounds + 6 reciprocity links of §6 | Lifts the two weakest-authority pages; converts card-stitching into editorial links | 45 min |
| 6 | A3 de-slop pass (5 items of §4) + merge duplicate EPA source | Removes the set's only real slop cluster | 30 min |
| 7 | A4 de-tic pass (antitheses, verdict ×3, delete "The search says…") | Tightens the longest page; removes on-page SEO narration | 20 min |
| 8 | Wire the 2 orphan images into their planned sections | Two sections get their intended visuals for free | 10 min |
| 9 | A5 band-dedup + A2 quip-trim + A2 Source-3 formatting | Voice polish where density flagged | 30 min |
| 10 | Restate the 9 externally-living figures inside their Sources annotations (verifier list §8-notes) | Makes every load-bearing number auditable on-page | 20 min |

### Build Over Time (next 30–60 days)
- **Bridge the thermostat page**: pitch 2–3 editorial links from `do-programmable-thermostats-cut-heating-bills` into the H&C trio — it is the cluster's missing hub link.
- **A2 film-kit follow-up article** (already teased) to complete the window-treatment sub-cluster.
- **Instrument the loop**: wire Rybbit's affiliate_click and scroll-depth per URL into a weekly glance; after 4 weeks, re-check GSC CTR on the rewritten titles.
- **Quarterly price re-verification cadence** for the 10 campaign ASINs (Sources carry retrieval dates — update them with each pass; winter articles get a November re-check before peak season).
- **A5 room-index strip + A4 priced-ladder graphic** (Tier-3 visuals) — only after Tier 1/2 ship and settle.
- **Diversify front-matter keyword-array shapes** as the site scales (chassis note, §4).

---

## 8. Rewrite Briefs

With only five pages audited and every one judged improve-and-keep, full rewrite briefs would be template-filling — the honest deliverable is two **improvement briefs** for the pages carrying real weaknesses, plus the mechanical fix spec that covers the rest.

**Brief W1 — A3 what-merv-rating-do-i-need (prose-discipline rebuild, no structural change).**
- *Audience:* homeowner replacing a furnace filter this week; allergy households considering MERV 13.
- *Intent:* keep the literal tier verdict as the opening answer; the dirty-filter question keeps its H2/FAQ.
- *Missing value:* none structural — the failure is repetition and process voice eroding an otherwise expert page.
- *Structure:* unchanged.
- *Edits:* delete the QA sentence twin (keep the locked "breathing problem" line in paragraph 3, kill the paragraph-2 variant); cut "manual is the ceiling" to one body + one box mention; rewrite "we'll fabricate" FAQ answer straight ("Yes — through runtime. This page gives the mechanism and a cadence, not an invented percent."); cite or delete the "independent review coverage" gesture; merge Sources 1+2.
- *Evidence to restate in Sources:* EPA 0.3–10 µm definition; FilterBuy actual dims; Filtrete MPR 1900.
- *Visuals:* restore filter-size-measure, particle ladder, trade scale.
- *Internal links:* keep 13-ac, ac-running, 47-audit; add A5 as fix-path companion.
- *Outcome:* a page whose prose discipline matches its expertise; quality 7.0 → ~8.5.

**Brief W2 — A4 point-sensor-vs-whole-home (authority + metadata rebuild).**
- *Audience:* homeowner who owns point sensors or is choosing between a $60 kit and a ~$560 shutoff; includes the empty-rental owner.
- *Intent:* comparison/upgrade-decision — unchanged, already the best structure-to-intent match in the set.
- *Missing value:* search-readiness, not content — title, tics, duplicated markup, and link authority.
- *Edits:* title → "Point Sensor or Whole-Home Shutoff? When to Upgrade" (52c); delete "The search says…" sentence; compress the stay-at-tier-1 verdict to its best statement ("permission slip"); thin antitheses to one per section; remove the two duplicate box blocks; restore both decision visuals.
- *Evidence:* all current claims verifier-confirmed — no factual changes.
- *Internal links:* add 06-water-bill return link; receive links from water-meter-running (shared ASIN) and water-meter-leak-indicator; one campaign-sibling link in.
- *Outcome:* the water cluster's decision page stops being its weakest-linked page; SEO 5.0 → ~7.5 post-fix and inbound wave.

**Mechanical fix spec (A1, A2, A5):** shortcode repair + Sources scrub per C1/C3; A1 meta trim + ct-clamp alt trim; A2 Source-3 formatting + evidence-tier table; A5 title reconciliation + band dedup. No prose rebuilds warranted.

---

## 9. Final Prioritized Checklist (do in this order)

1. ☐ Convert 21 single-brace shortcodes to `{{<` across the 5 files
2. ☐ Delete the 5 duplicated product-box blocks (A3:103,105 · A4:44,102,104)
3. ☐ Add `grep -r '{&lt;' public/` CI lint; run `npm run verify` + the new lint
4. ☐ Scrub "SQ-063" ops language from A1 Source 7 + A5 Source 4
5. ☐ Ship titles (A4/A3/A5 ≤65c) + metas ≤150c
6. ☐ Commit + deploy + production-verify: boxes count, images count, zero `{&lt;` in curl output
7. ☐ Wire 2 orphan images (A2 alternatives strip, A5 renter flatlay)
8. ☐ Editorial inbound wave (5 missed + 6 reciprocity links, §6)
9. ☐ A3 de-slop + A4 de-tic + A5 band-dedup + A2 quip-trim
10. ☐ Restate the 9 externally-living figures in Sources annotations
11. ☐ Set 4-week GSC/Rybbit review; November price re-verification for the winter pair

---

### Appendix — Mission record
- Formation: 9 packets dispatched (lt + 5 wing + twin_q + executor + scout), read-only, flash-only cost policy honored (~pennies). Wall time ≈ 52 min.
- Outcomes: 6 complete · 1 partial (scout; gaps closed mechanically) · 2 protocol deaths (prospector, mason — angles absorbed and re-verified Commander-side).
- Wave 2: an independent verifier seat re-derived this compiled report against ground truth. All claim groups CONFIRMED (counts, fix-spec lines, titles, ops-language, inbounds, orphans, cannibalization) except one REFUTED item — the Commander's initial tally undercounted A4's broken duplicates (2 → 3). All tallies above are the post-correction, wave-2-verified numbers: 26 malformed (9 boxes + 17 visuals), 17 dead images, 9-of-14 dead boxes, 5 duplicate deletions + 21 conversions.
- Ground truth: `/tmp/sq64/sheets/ground-truth-sheet.md` + per-page sheets; executor asset table `/tmp/squad-workspaces/20260830-115039-executor/sq64-assets.md`; raw envelopes `/tmp/sq64/results/` and `/tmp/sq64/results-w2/`.
- Validation highlights: shortcode defect independently found by Commander extraction AND cold twin_q; Lt claims disk-checked (title lengths, ops-language leaks, stub source — all confirmed); tracer's "no table on A1" rejected (table renders — grep `<table` = 1); wave-1 verifier re-derived ~35 article claims with zero refutations; cartographer's editorial-vs-card inbound split grep-verified.
- Blackboard: SQ-064 (the-squad mission registry).
