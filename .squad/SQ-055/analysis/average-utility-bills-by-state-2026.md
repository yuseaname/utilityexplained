# Reader-Experience Analysis — average-utility-bills-by-state-2026

## Execution Log

- **Edit Plan items 1–8 and 10 applied; item 9 shipped as the FULL variant and item 11 (approved description) executed. Frontmatter: `updated:` already 2026-08-29; `hero_below_answer: true` added (Commander-approved named exception); approved description string shipped; no other fields touched.**
- Item 2: Quick Answer now leads with the dollar answer (national-breakdown bullets first, methodology paragraph after the bullets); broad-basket bullets retain their label; zero claim changes.
- Item 3: jump-row shipped under the Quick Answer using the analysis §5 anchors, all five ids verified against the file's H2 ids.
- Item 4: FAQ "Where can I find…" rewritten — self-referential link removed; phantom "interactive rate lookup tool" phrase deleted outright; electric-bill-breakdown link added.
- Item 5: "Reading the table against your own bill" 3-sentence paragraph inserted post-table (rate × 900 kWh restatement + how-to-read-your-utility-bill link + seasonal caveat reused verbatim from on-page text).
- Item 6: moving-utilities-checklist link added at the section-8 intro; which-rate-plan link added on the provider bullet.
- Item 7: rates-fees-usage link relocated from Quick Answer tail into the table footnote.
- Item 8: `## Related Reading` block added before the FAQ run (5 bullets: electric-bill-breakdown, how-to-read-your-utility-bill, which-rate-plan, 44-how-to-lower-water-bill, moving-utilities-checklist).
- Item 9 — **FULL variant shipped**: both malformed bare-`<li>` lists repaired (highest water/sewer list now wrapped in `<ul>`); the seven H3-rendered pre-FAQ Q&As deleted — every question already renders as a `{{< faq >}}` shortcode entry, so the FAQ run is uniform and `{{< faq-schema >}}` covers all rendered questions; the duplicate H3Hawaii/increase echoes also satisfy item 10 (dedupe). One residual duplicate (FAQ #1's own opening line duplicated) was caught and removed during verification.
- Item 10: Hawaii/Idaho and 2025→2026 increase tellings now appear once in body, once in table footnote, once in FAQ — per the brief's keepers.
- Item 11: description now folds the ~$375/mo + 17-state numbers as approved.
- Skipped: none (no NEEDS-VERIFICATION items pending for this page; §5 item 4's PUC pointer was already excluded at analysis stage as un-linkable without new verification).

---

SQ-055 planning wave · Rybbit last-30 baseline: 30 visits, 33 pv, TOP 14.2s, bounce 87% [RYBBIT]. Comparison-shopper intent. Re-published after consolidation; frontmatter aliases point two retired URLs here (/blog/2026-utility-cost-index-by-state/, /blog/02-average-utility-costs-2026/) [CONTENT]. Full file read this run including FAQ tail.

## 1. Intent Model

- **Primary intent:** state-vs-state comparison — "is my bill normal for my state?" or "what will utilities cost where I'm moving?" Two faces: the **verifier** (has a bill, wants a benchmark) and the **planner** (moving/budgeting/job offer). The article's own intro names both: "moving, budgeting for a new home, or just curious how your bill compares" [CONTENT].
- **Secondary intent:** turning a published rate into an expected monthly number, and reconciling their own bill against the standardized estimate. The page's "standardized estimate, not a survey median" paragraph shows the author models this reader [CONTENT].
- **Desired outcome:** reader finds their state (or nearest sampled state), understands the estimate's construction (rate × 900 kWh; 75 therms; water+sewer), and knows whether their own bill is within normal variance — with one onward action if it isn't (usage diagnosis, rate-plan check), or (planner face) a way to price the move [CONTENT + INFERENCE].
- **Next logical need:** verifier → "why is MY number different from the table" (usage, rate plan, season, taxes on top); planner → move logistics and first-month budgeting. Today the page serves neither with links near the table [INFERENCE].

Engagement context [RYBBIT]: TOP 14.2s is the healthiest in this assigned set — comparison shoppers do scan the table. Bounce 87% at 1.1 pv/visit says the reader extracts their row and exits: the page offers no onward step tuned to their row outcome.

## 2. First-Screen Verdict

Mobile: title/meta → hero image (800×450; **no `hero_below_answer` flag on this page** [CONTENT — frontmatter verified; the three sibling pages carry it]) → "Quick Answer: Average U.S. Utility Bills in 2026" heading → a methodology-first paragraph (narrow vs broad basket definitions, ~90 words) before the first dollar figures.

The primary answer (national narrow-basket ≈$375/mo with state range) is present in the first screens but is delayed behind basket definitions; combined with the un-flagged hero above the H2, the effective first answer line sits ≈2.5–3 screens deep on a 56%-mobile audience [INFERENCE grounded in CONTENT file structure].

**Exact "this isn't giving me what I came for" point:** the Quick Answer's first block is methodology ("This guide uses two definitions to avoid confusion…"), not a number. A comparison shopper scanning for a dollar figure parses ~90 words of basket definitions before the first usable figure — that is the likely bail moment for the low-patience cohort. This matches the site's documented failure pattern: hero pushing the answer below the fold / answer buried below intro [INFERENCE + CONTENT for the structural facts: no flag in frontmatter; paragraph order verified].

The data itself is strong and early in the HTML; this is the most fixable first screen of the four assigned pages [INFERENCE].

## 3. Gap Analysis

- **P0 — Hero above the answer.** Missing `hero_below_answer: true` (present on 25/19/18 [CONTENT]). On mobile the hero consumes the first fold before any dollar content; this is the site's previously traced low-TOP failure mode #2 [RYBBIT-adjacent CONTENT].
- **P0 — Post-table dead end.** After the 17-row table and Hawaii footnote the reader lands in "What's Driving These Differences? Key Factors Explained" — an essay — and the page terminates in Sources with **no Related Reading block** [CONTENT] and only 4 unique outbound links, all in the top half of the page (excluding the self-link) [CONTENT].
- **P0/P1 — Self-referential link in FAQ #7.** "Where can I find my state's exact utility rates?" links *to this same page* ("the [state-by-state table above](/blog/average-utility-bills-by-state-2026/)") [CONTENT — exact quote]. A circular affordance on the one FAQ aimed at the reader's next step.
- **P1 — Phantom product reference.** FAQ #7 — the same question's answer text — references "our interactive rate lookup tool to search by provider and plan type" — no such tool/page exists in the site inventory [CONTENT — full-file read + content-metrics.json scan; INFERENCE that it's a consolidation leftover]. Promise the reader cannot fulfill.
- **P1 — No chapter navigation on a 3,300-word table page.** No `{{< jump-row >}}`, no anchor links from the electricity/gas/water intro lines to their sections; the reader must scroll through all four sub-topic bodies to find the total table [CONTENT].
- **P2 — HTML hygiene.** Two malformed lists in the rendered HTML: the "highest combined water & sewer bills" list opens with bare `<li>` elements under a paragraph (no `<ul>`), and the H3-question block above the FAQ run has the same defect [CONTENT — file lines around id="water…" and id="what-s-driving…" region]. Renders via browser recovery; still a hygiene defect on a rank-14 page.
- **P2 — Internal duplication.** The Hawaii-vs-Idaho math (3.4×, $453/$225/$324) appears in the body, the table footnote, an H3 above the FAQ run, AND FAQ #1 — four tellings. [CONTENT]
- **P2 — FAQ conversion inconsistency.** FAQs #1–7 exist as H3 paragraphs in body HTML **and** items #1–2 duplicated as `{{< faq >}}` shortcodes near the tail (verified in the spooled tail: three H3-block Q&As — urban/rural, taxes-and-fees, projections, reduce-bill, rates — render as plain H3s, not schema shortcodes) [CONTENT]. Rendering risk at implementation; flag in Edit Plan.

## 4. Momentum & Structure

- **Heading usefulness: the weakest structural element.** Body H2s are thematic ("Understanding…", "Electricity Rates by State…", "Gas Bills by State…", "Water and Sewer Bills…", "Total Utility Cost Comparison…", "What's Driving…", "How to Use This Data for Smart Decisions") — serviceable for a linear reader, poor for the verifier who wants "my state's row" immediately. No jump-row. The 17-row table — the page's actual product — sits behind ~7 sections of prose [CONTENT + INFERENCE].
- **Paragraph bulk:** the electricity section runs five 60–110-word paragraphs before its top-10 lists; the Quick Answer is dense. Above-average word count between payoff moments for the intent. [CONTENT]
- **Repetition:** Hawaii/Idaho and the 2025→2026 increase story each told ≥3×; the "actual usage is ~515 kWh in Hawaii" caveat appears in body, table note, H3 block, and FAQ #1 [CONTENT]. Keep once in table note + once in FAQ; trim body duplication.
- **Filler/padding:** some pre-consolidation phrase-level legacy remains ("gives you real leverage in financial planning", "we'll also highlight where costs are rising fastest—and where they're surprisingly affordable" — a promise the page does not keep as written) [CONTENT].
- **Scannability verdict: table excellent, navigation absent.** The 17-row table with bolded state names is the page's best reader asset; everything around it serves neither quick lookup nor continuation. [INFERENCE]

## 5. Information Gain Plan (useful-only)

1. **Jump-row under the Quick Answer (small, additive, no new facts):** `{{< jump-row "Total table|#total-utility-cost-comparison-2026-state" "Electricity|#electricity-rates-by-state-2026-breakdow" "Gas|#gas-bills-by-state-heating-drives-the-di" "Water & sewer|#water-and-sewer-bills-the-overlooked-uti" "How to use it|#how-to-use-this-data-for-smart-decisions" >}}` — anchors verified to exist on-page (ids quoted from the file). One-line addition; the single highest-leverage navigation fix available. [CONTENT]
2. **"Why is my bill different from the table?" FAQ entry (small):** assembled strictly from already-on-page causes — seasonality ("Factor in seasonality" bullet), usage differences vs the 900-kWh standardization note, conservation-tier pricing (water section), and taxes/fees inclusion note (existing FAQ: "Do utility costs include taxes and fees?"). Zero new sources; answers the page's #1 unasked question [CONTENT].
3. **"If your state isn't in the table" note (small):** one sentence pointing to the method line — "build your own estimate with your state's residential rate × your kWh (the table's method)" — using the page's own method description. No new rates, no new states. [CONTENT]
4. **NEEDS-VERIFICATION (excluded from Edit Plan):** adding an illustrative state-source pointer (e.g., "your state PUC publishes current rates" with a link) is content the page already gestures at; a verified /blog/ internal target was not found for PUC-directories — no link proposed rather than risk a broken one.
5. **Explicitly rejected as padding:** adding more states, adding internet/trash sub-pages, expanding the drivers essay. The page is long enough; its gaps are navigational, not informational. [INFERENCE]

## 6. Internal Journey (all targets verified existing under content/blog/ this run)

1. **Anchor** "how to read your own utility bill line by line" → **Target:** `/blog/how-to-read-your-utility-bill.md` (file verified in listing; standalone guide) → **Placement:** immediately after the total table's Hawaii footnote paragraph → **Why:** the verifier's true next need — decode their own bill against the table. This is the single most important missing exit on the page. [CONTENT + INFERENCE]
2. **Anchor:** "what the charges on an electricity bill actually are" → **Target:** `/blog/electric-bill-breakdown-understanding-line-items/` (metrics draft:0; wave-1 analyses treat as live) → **Placement:** the "Do utility costs include taxes and fees?" FAQ answer, as the depth link → **Why:** the FAQ currently dead-ends on the self-link; with the circle fixed (§3), the reader owes a real target about the line items above the table figures. [CONTENT]
3. **Anchor:** "which electricity rate plan fits your household" → **Target:** `/blog/which-rate-plan-is-right-for-me/` (file verified in blog listing) → **Placement:** "Check your local utility's plan" bullet in "How to Use This Data" → **Why:** the page tells readers rates vary by provider — but gives them nowhere to go; this is the planner-face conversion. [CONTENT + INFERENCE]
4. **Anchor:** "how utility rates, fees, and usage work together" → **Target:** `/blog/how-utility-rates-fees-usage-work-together/` (already linked once in the Quick Answer tail — *relocate* to the table footnote where "rates reflect average residential customers with standard tiered pricing" appears) → **Why:** link placement must coincide with the reader's question moment; the current intro-tail placement is 2 screens above the table. [CONTENT]
5. **Anchor:** "how to lower your water bill" → **Target:** `/blog/44-how-to-lower-water-bill/` (existing link in water section — keep in body, and add to Related Reading) → **Why:** the water section's rising-cost framing is the strongest natural hand-off on the page; the 44 page is the action counterpart. [CONTENT]
6. **Anchor:** "moving utilities to a new address" → **Target:** `/blog/moving-utilities-checklist/` (file verified in blog listing) → **Placement:** intro sentence "moving, budgeting for a new home" → **Why:** serves the planner face at the moment of self-identification; zero cost, high fit. [CONTENT + INFERENCE]

Count: 5 new targets + 1 relocated existing link. All existence-verified by blog-listing read this run; draft-status confirmed from metrics where visible, and any metrics-draft:1 targets were excluded (7-states…, 2026-utility-cost-index… — both tempting but draft:1).

## 7. CTA Fit — **NONE - informational**
 
The reader's stage is cost-orientation, not solution-shopping; the doctrine's NOT-A-FIT table covers this page's two consolidation parents ("02-average-utility-costs", "2026-utility-cost-index" cousins `16-budget-billing` / `15-higher-same-usage` twins — "utility-program questions; product-neutral"), and a tool box对着 a state table would monetize a comparison moment, which reads as decoration at best and trust-erosion at worst. The honest action after trust here is the dispute/usage path — which is a *page* need, not a product need [INFERENCE grounded in doctrine + RYBBIT intent pattern].

Existing boxes: **zero product boxes / affiliate links on the page today** beyond the sitewide disclosure [CONTENT — full read]. Nothing to keep/replace/reframe. Explicitly do NOT add one in this wave.

## 8. Edit Plan (ordered; no numbers or claims touched; small/medium/large marked)

1. **[small | frontmatter]** Add `hero_below_answer: true` (P0 fold fix; key already used by 3 sibling pages).
2. **[small | Quick Answer reorder]** Move the narrow/broad-basket methodology paragraph AFTER the national-breakdown bullets; lead the block with the dollar answer. Reorder only; one transition phrase; zero claim changes. *(If the Commander prefers a lighter touch, merging bullets is the fallback — but answer-first is the point.)*
3. **[small | under Quick Answer]** Insert the jump-row (§5 item 1; anchors verified on-page).
4. **[small | FAQ #7]** Rewrite the self-referential sentence into the Journey #2 link (electric-bill-breakdown) and **delete** the "interactive rate lookup tool" phrase outright (P1 phantom).
5. **[medium | post-table block]** Insert a short "Reading the table against your own bill" paragraph (3 sentences max) that (a) restates the rate × 900-kWh construction in one line, (b) links Journey #1 (how-to-read-your-utility-bill), and (c) closes with the seasonal caveat pulled from the existing "Factor in seasonality" bullet. No new facts — assembly of on-page material.
6. **[small | "How to Use This Data" list]** Add the two missing bullet links: Journey #3 (which-rate-plan) on the provider bullet; Journey #6 (moving-utilities-checklist) at the intro's move/budget sentence.
7. **[small | relocate]** Move the rates-fees-usage link from the Quick Answer tail into the table footnote (Journey #4 placement note).
8. **[small | end matter]** Add `## Related Reading` (bulleted, before the FAQ run, house convention) with: electric-bill-breakdown, 44-how-to-lower-water-bill, moving-utilities-checklist, which-rate-plan, how-to-read-your-utility-bill — 5 bullets, one-line descriptors.
9. **[small | structural hygiene]** Repair the two malformed `<li>`-without-`<ul>` lists. Convert the three H3-rendered Q&As (urban/rural, taxes-and-fees, projections…) into existing-style `{{< faq "…" >}}` entries so the FAQ run is uniform and `{{< faq-schema >}}` covers what actually renders. **Recommended alternative the Commander may prefer (lighter):** leave HTML as-is (renders), only add `{{< faq-schema >}}` coverage — flag that schema may then under-count. State which form shipped.
10. **[small | dedupe pass]** Keep ONE telling each of (a) Hawaii/Idaho totals, (b) 2025→2026 increase leaders: recommend body section + FAQ #1 as the keepers; trim the redundant H3-echo above the FAQ run.
11. **[PROPOSAL ONLY — meta description, Commander-approved string]** Fold the two headline numbers into the description ("narrow basket ≈$375/mo; 17-state table inside") to pull the comparison click. No other frontmatter changes.

## 9. Dual Reasoning + Self-Critique

**Reader test.** "I came here because I need to know what utilities cost in my state (or the one I'm moving to)." Post-plan: dollar answer first (≈1 scroll on mobile, hero demoted), jump-row to the table in one tap, the table itself unchanged (it is good), and a 3-sentence bridge that converts "here's the number" into "here's what to do with it." Verifier gets self-comparison guidance; planner gets the moving/checkout pages. The single riskiest ordering change is #2 — if the owner values the two-basket methodology as a differentiator, the compromise is one bolded methodology line, not a moved paragraph; flagged above.

**Business test.** Natural trust-follow-on: self-serve bill diagnosis and rate-plan confidence. Both are *pages*, not products — this wave's conversion surface is pages/session (currently 1.1 [RYBBIT]) and downstream entry into the line-item and rate-plan family. The honest affiliate answer is NONE - informational, with a possible revisit gated on post-edit TOP ≥20s (noted in §7)

**What an expert editor would criticize:**

1. **The methodology-first Quick Answer is not unambiguously wrong** — the narrow/broad distinction does real work, and demoting it might re-confuse readers who arrived expecting the more inclusive $470 figure. Mitigation offered (redirect first, methodology second); an editor could still prefer cut-over-move.2. **Item #9's lighter FAQ variant would ship schema without uniform rendering** — that is the kind of half-fix that creates the next audit finding; say out loud which variant was chosen.
3. **Jump-row anchors depend on Hugo's auto-generated heading IDs** (`electricity-rates-by-state-2026-breakdow` — note the truncated-looking id, which is what's actually in the file; ids are live/stable only until a heading is re-worded). The Edit Plan must not re-word any H2 text, or the anchors silently break. This plan deliberately changes zero headings [CONTENT ids quoted].
4. **The 17-row table on a 56%-mobile audience is the real UX elephant** (horizontal scroll on most phones); I am proposing no redesign of it here because templating is outside an article-edit wave. An editor will call that the biggest miss — it is, and it's the right scope line for this wave.
5. **Bounce-fix risk:** the jump-row + answer-first moves could *lower* TOP if readers get their number and leave even faster. The mission's framing treats high TOP/low bounce as the satisfaction proxy; my plan optimizes for *successful-answer* behavior and pages/session, not TOP maximization per se — worth one line from the Commander confirming that trade is understood before the implement wave ships.
6. **No new-claims violations were introduced;** every number cited in the plan is from the audited on-page copy (post-SQ-051..054 wave), and the one location that tempted a new fact (Hawaii water/sewer multiple) was rejected without a NEEDS-VERIFICATION write-in because no plan item needs it.
