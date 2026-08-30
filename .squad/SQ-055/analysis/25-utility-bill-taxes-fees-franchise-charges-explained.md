# Reader-Experience Analysis — 25-utility-bill-taxes-fees-franchise-charges-explained

SQ-055 planning wave · Rybbit last-30 baseline: 39 visits, 45 pv, TOP 5.6s, bounce 82% [RYBBIT]. Site watch-list page (target TOP 30s+). Aug-10 top-10 member that grew 8x in traffic but engagement regressed. Full file read this run (2026-08-29 state, post-SQ-051..054 evidence remediation).

## Execution Log

- Applied Edit Plan items 1–6 plus the Commander-approved item 7 description rewrite. Frontmatter: only `updated:` (already correct) and the approved `description` touched; hero/title/slug/aliases/sources untouched.
- Item 1 (IG-L1): "Often appears as" pattern column added to the verified-rates table — composed only from the table's own on-page examples, with the "often / labels vary" guardrail (never "always"). Gross-receipts trim kept per Commander ruling.
- Item 2 (IG #2): "Next step:" routing line added directly under the Quick Answer (riders + delivery-vs-supply links, both resolve).
- Item 3 (Journey #3): dispute-guide link added as the closing clause of "How to Read Yours" step 4.
- Item 4 (IG-R1): `## Related Reading` block added before the FAQ — 5 bullets (19-surcharges, 04-hidden-fees map, 24 delivery-vs-supply, how-to-dispute, 26-deposit), one-line house-style descriptors.
- Item 5: verified the FAQ already renders via `{{< faq >}}` shortcodes + single `{{< faq-schema >}}` (page had moved to the house pattern since the analysis read) — no conversion needed, text unchanged.
- Item 6: third retelling of the $100/$11.11 gross-receipts example trimmed from the body (kept the pointer to the FAQ); example retained in FAQ #4 — page net-negative on words.
- Item 7: approved description string shipped verbatim as proposed. Franchise P2 and hero/CTA non-items honored (Section 7 = NONE).
- Skipped: none — no NEEDS-VERIFICATION items in this brief.

## 1. Intent Model

- **Primary intent:** the reader saw one or more mystery lines (a percentage-of-bill tax, a "franchise charge," a named fee) and wants to classify *their* line: what is it, who sets it, is it legitimate. This is identification + legitimacy-check intent, the same family as the surcharges page but with a government-authority flavor. [INFERENCE from query-family keywords "utility bill taxes", "franchise charge utility bill" in frontmatter, and the page's own structure] 
- **Secondary intent:** verification — "the percentage on my bill looks bigger than the printed number" (the page itself anticipates this in its FAQ #4 and the gross-receipts section). [CONTENT]
- **Desired outcome:** reader can (a) classify each non-usage line on their bill into tax / fee / franchise, (b) know which authority sets each, (c) recompute a suspicious line, (d) know they cannot negotiate the rate but can dispute a math error. [CONTENT — this is what the article delivers today]
- **Next logical need:** after classification, either (1) the same workflow for the neighboring charge family — riders/surcharges, fuel adjustment, delivery-vs-supply — or (2) the dispute path when the math doesn't reconcile. The rewritten page links (2) and two of (1), but only deep in the body. [INFERENCE]

Engagement context [RYBBIT]: 39 visits is real traffic for rank ~13, and 82% bounce is below the site's 89% norm, but TOP 5.6s means the median reader classified their line from the Quick Answer and left — or failed to find a matching label and left. Both outcomes are invisible in these numbers; the structure analysis below arbitrates.

## 2. First-Screen Verdict

Mobile (56% of traffic [RYBBIT]) sees, in order: affiliate-disclosure chip → Quick Answer heading → a four-sentence definitional paragraph → (below fold, per `hero_below_answer: true` [CONTENT]) the hero image, then "What Each One Looks Like on a Bill" with the verified-rates table.

The Quick Answer does answer *the taxonomy question* in its first bolded sentence — house pattern satisfied [CONTENT]. **But** the reader's actual first move is label-matching: they scan for *their* word ("PPTC", "Utility Users Tax", "franchise", "gross receipts"). The exact point a reader bails: after sentence 2, when they realize the Quick Answer defines terms but never maps the *labels they see on their own bill* to these categories — that mapping lives in the second section's table, 2+ scrolls down on mobile. A reader whose label isn't "utility tax", "fee", or "franchise" verbatim (most labels are utility-specific PPTC/ECA/RTT-style abbreviations) hits no scan target and exits. TOP 5.6s at 82% bounce matches that step-out point. [INFERENCE, grounded in section structure]

Second risk: sentence 3 of the Quick Answer immediately cross-links to the surcharges page — for a ready-to-leave reader that's a healthy exit; for the still-classifying reader it's a second deferral. [INFERENCE]

## 3. Gap Analysis

- **P0 — No label-matching scan target on the first screen.** "What Each One Looks Like on a Bill" holds the page's unique asset — a table of real bill-line labels paired with who sets each — but it sits below the fold and its five rows are statute-level examples (Pasadena rates, Washington cap, Cheney ballot measure, Florida cap, Minnesota franchise basis), not label-pattern guidance. A reader with "Storm Recovery Accumulation" or "PPTC" in hand cannot reach *their* row in two sentences + one scroll. Section: "What Each One Looks Like on a Bill." [CONTENT]
- **P0 — Watch-list body-link placement.** All five body links (riders ×2, fuel adjustment, connection, reconnection) live in one paragraph at the very end of the reading path, and the two 5.6s-exit cohorts (classified-and-left, unclassified-and-left) statistically never reach it. GROWTH_LOG records the pre-2026-08-29 version of this exact page carried a jump-row and in-QA links to sibling explainers; the evidence-remediation rewrite dropped both — structural regression, not a new finding. Section: end of "How to Read Yours." [CONTENT + INFERENCE]
- **P1 — The four-step "How to Read Yours" reads as procedure, not triage.** It tells the reader what to do but the rollback path — "this classification doesn't fit my line, try the other family pages" — is compressed into a single dense paragraph beneath the steps. Section: "How to Read Yours," closing paragraph. [CONTENT]
- **P1 — No Related Reading block.** The baseline house pattern for this page family (exemplar: what-is-ccf-on-a-water-bill.md) is Related Reading before the FAQ; this rewrite has none, so the deepest-engagement band of the page terminates into Sources. [CONTENT]
- **P1 — Related-page surface is thin: 4 unique outbound targets all inside running prose; no bulleted scannable cluster anywhere.** The pre-rewrite version documented in .rybbit-baseline carried 6-link Related Reading and ~11 total links. [CONTENT + INFERENCE]
- **P2 — FAQ titles are questions but appear as unmarked H3s in an "FAQ" H2; house pattern uses `{{< faq "Q" >}}` shortcodes (schema-consistent rendering). Recast for consistency with the exemplar.** [CONTENT]
- **P2 — Franchise-charge coverage is one table row + one FAQ; the URL keyword promises "franchise charges explained" and a reader landing on that query gets 2 paragraphs. Caveat: do not pad — one plain-paragraph expansion using on-page facts only.** [CONTENT]

## 4. Momentum & Structure

- **Heading usefulness:** H2s are procedural and accurate ("Quick Answer", "What Each One Looks Like on a Bill", "Why a Tax Lands on Your Delivery Charges Too", "How to Read Yours") — good, but no H2 says anything about *reading your own bill's line labels*; the closest is the first-paragraph table. Scannability for label-searchers: weak. [CONTENT]
- **Paragraph bulk:** healthy — short paragraphs, table-first, list-first. No walls of text. Zero filler. [CONTENT]
- **Useful fact density:** high (this is the strongest rewritten template page of the four assigned). Verified-rate table is genuinely additive versus generic competitors. [CONTENT]
- **Repetition:** the gross-receipts point appears in body section 3 AND FAQ #1 AND FAQ #4 — three tellings. For a reader who read linearly that's friction; for a FAQ-jumper it's redundancy-as-feature. Keep body + one FAQ; trim the third telling. [INFERENCE]
- **Scannability verdict:** passable prose, failed lookup design. This page wants to *be* a lookup (label → class → authority), and its current single-table design half-delivers it below the fold. [INFERENCE]

## 5. Information Gain Plan

Useful-only; the site owner rejects length-for-length's-sake. All items below are restructuring or on-page-fact reuse — no new factual claims except where flagged.

1. **Label-pattern mini-table (IG-L1, small, restructure of existing table):** add a first column "Often appears as" to the verified table with *pattern-level* descriptors composed from on-page examples (e.g., tax lines often carry the city/utility name + "tax"; franchise lines often name the municipal right-of-way or franchise agreement). No new rates, no new misconceptions, no new claims beyond restating the page's own verified examples as patterns. [CONTENT]
2. **One-question self-check line placed immediately after the Quick Answer:** "If your line is a percentage of subtotal, start here; if it is a one-time or program add-on, it belongs to the [riders and surcharges family](—)." This is routing, not content — zero padding. [CONTENT]
3. **Related Reading block before FAQ (IG-R1, house convention, ~5 curated uniques, all from the journey targets in §6; all live).** [CONTENT]
4. **No new worked example needed here** — the $100 bill / $11.11 tax line example already on-page is the strongest math anchor in the family; do not duplicate it elsewhere in the page. [CONTENT]

## 6. Internal Journey

All targets verified this run: file present at the listed path under content/blog/, and metrics-rule honored (any entry observed `draft:1` was excluded — none of the six below is).

1. **Anchor:** "riders and surcharges (and other commission-approved add-ons)"
   **Target:** `/blog/19-utility-bill-surcharges-and-riders-explained/`
   **Placement:** Quick Answer sentence 3, replacing today's mid-sentence link-out so the hand-off reads as scope-splitting, not deferral.
   **Why:** the #1 adjacent-family question; the surcharges page is the mirror-explainer and already reciprocates (its FAQ #2 links back to this page). Serves the classifying reader's next step instead of ending the journey. [CONTENT]
2. **Anchor:** "which charges sit in the delivery part of the bill vs the supply part"
   **Target:** `/blog/24-delivery-charge-vs-supply-charge-utility-bill/`
   **Placement:** "Why a Tax Lands on Your Delivery Charges Too," first paragraph after the gross-receipts definition.
   **Why:** the gross-receipts explanation itself presumes the reader already distinguishes delivery from supply; this is exactly the reader who won't. (This target was hit by the wave's read this run: live, draft:0.) [CONTENT]
3. **Anchor:** "step by step: how to dispute a utility bill"
   **Target:** `/blog/how-to-dispute-utility-bill/`
   **Placement:** step 4 "Recompute the line" — immediately after "re-check the authority from step 2 first."
   **Why:** a reader who recomputes and *still* thinks the tax line is wrong has crossed from classify → challenge. Today the page tells them to escalate to the city finance department in a FAQ but never names the dispute guide. [CONTENT]
4. **Anchor:** "every charge on a utility bill, explained"
   **Target:** `/blog/04-hidden-fees-utility-bill.md` → renders as `/blog/04-hidden-fees-utility-bill/`
   **Placement:** Related Reading block (new).
   **Why:** this is the map-view page for the whole taxonomy; a reader classifying one line often wants the whole table of contents next. (Live, draft:0, 1,868 words, 22 outbound internal links.) [CONTENT]
5. **Anchor:** "your utility deposit, explained"
   **Target:** `/blog/26-utility-deposit-explained.md` → `/blog/26-utility-deposit-explained/`
   **Placement:** Related Reading block, as a one-time-charge-family sibling.
   **Why:** readers met with BOTH a tax line and a new-service deposit are often the same reader — new-move-in households getting their first full bill; deposit is the other one-time family member. (Live, draft:0.) [CONTENT + INFERENCE]
6. **Anchor:** "utility bill taxes, fees, and franchise charges — the full guide back you came from" → inverse: pull from the *surcharges* page is already live; propose the reverse only if the commander approves a 2-line addition to 19's FAQ #2. **(Counted in #1; not a new line.)**

Net: 4 new unique outbound targets; 2 additional placements of already-linked targets relocated to higher-value positions. Every target path re-verified by read this run.

## 7. CTA Fit

**NONE - informational.** [CONTENT-backed INFERENCE]

- Intent stage: pure classification + legitimacy-check; the reader is verifying a charge, not shopping for relief.
- Doctrine check: AFFILIATE-PLACEMENTS-2026-08-28.md explicitly lists this page family (definitional charge explainers — "23-billing-cycle, how-sewer-charges-work, what-is-ccf, gas-customer-charge") in the NOT-A-FIT table: "No product answers the question; a box here is decoration."
- The only tools adjacent to the reader's next true need at step-4-verification are the utility's own tariff page (external) and the dispute process — neither is an Amazon SKU, and inserting one would convert a trust page into a commercial page for zero meaningful AOV.
- No existing product boxes or inline affiliate links on the page today beyond the sitewide `{{< affiliate-disclosure >}}` — correct as-is; do not add any.

## 8. Edit Plan

Ordered, targeted, no wholesale rewrite. All diffs are section-level; the existing evidence-gated facts (August remediation) are untouched.

1. **[medium | Quick Answer]** Add the one-question self-check routing line (IG #2) as its own short paragraph below the Quick Answer, linking riders (already-linked target, new anchor wording) and delivery-vs-supply (new).
2. **[small | "What Each One Looks Like on a Bill"]** Add the "Often appears as" pattern column to the verified table (IG #1) using only rewritten phrasings of the table's own examples; do not add rates, caps, statutes, or label spellings not already on-page.
3. **[small | "How to Read Yours," step 4]** Add the dispute-guide link (Journey #3) as the closing clause of step 4, mirroring the sentence shape already used for the rider/fuel-charge cross-links in the paragraph below.
4. **[medium | Related Reading]** Insert a `## Related Reading` block before the FAQ with the four curated bullets from §6 (surcharges, 24, dispute guide, 04 map) plus the deposit page — 5 bullets, one-line descriptors each in house style.
5. **[small | FAQ]** Recast the 5 FAQ Q&As from unmarked `###` blocks to `{{< faq "…" >}}` shortcodes to match the house schema-render pattern (exemplar parity). Text identical; no new claims.
6. **[small | "Why a Tax Lands on Your Delivery Charges Too"]** Trim the third retelling of the gross-receipts math (keep body + FAQ #4). Net word-count negative; improves momentum for the plurality of readers landing mid-page from search.
7. **[PROPOSAL — Commander decision, frontmatter: description tweak]** within the allowed "meta-description improvement" carve-out: current description lists topics but not the *ease* promise; propose "…which authority sets each, how to verify the math, and what you can and can't dispute." — same facts, tighter pull. No other frontmatter changes proposed.

Deliberately NOT in this plan: no hero-image swap (the `hero_below_answer: true` flag already fixes fold order — verified on-page), no new section for franchise depth (P2 — weigh against the no-padding rule; if the owner wants it, franchise expansion is its own mission with fresh sources, not this one), no CTA/monetization additions (Section 7 verdict).

## 9. Dual Reasoning + Self-Critique

**Reader test.** "I came here because I need to know what *this line* on my bill is." Today: they get a taxonomy in 4 sentences (satisfying) but no label-to-line bridge on the first screen (fails fast for the majority who don't use the page's exact nouns [INFERENCE]). Post-plan: the routing line + pattern column put the reader within one scroll of either their answer or the neighboring-family page that has it. Satisfaction improves; TOP target (30s+) only moves if the label-matching table truly lands on screen one, which is a rendering dependency, not a content guarantee.

**Business test.** The natural action after trust here is *verification behavior* — reading the tariff, disputing, and exploring sibling charge pages — not purchasing. Journey links are the conversion surface (deeper sessions, more pages per session), and the affiliate doctrine already writes this page off as a monetization candidate. This plan's business value is entirely in multi-page session lift and watch-list TOP recovery; that is the correct business outcome for a line-classification page.

**What an expert editor would criticize:**

1. The "Often appears as" column flirts with over-promising: real utilities use wildly idiosyncratic labels, and pattern descriptors could set a false expectation that every label matches a pattern. Mitigation baked into the edit plan: descriptors are explicitly composed from the page's *own verified examples*, and the column copy must say "often," never "always." Still — this is the plan's most exposed item; if the editor judges it too fuzzy, cut item 2 and keep the routing line only.
2. Related Reading before FAQ is house convention, but the 5 bullets I picked skew toward *family explainers* rather than *actionable next steps*; an editor could argue the deposit page is the weakest fit on this list (different reader emotion: new-customer vs. bill-auditor). My counter: the move-in household hypothesis. It's an inference, not a measurement — flag for the Commander if the owner dislikes hypothesis-led linking.
3. Adding a 5-bullet Related Reading to a 5-H2, ~1,000-word page nudges end-matter toward a third of the page on small screens. The edit plan is net-positive only if item 6's trim actually ships; if the trim is dropped, drop the deposit bullet too.
4. The plan does nothing for the business metric most site owners watch — the franchise-fee keyword gap (P2). Honest reason: fixing it properly requires new sourced content, which violates this wave's bar; leaving it as a P2 is the right call and I'd defend it, but the editor should know it was left, not missed.
5. Everything above assumes Rybbit's 82% bounce is *classification success* (my read) rather than *satisfaction failure*. If the Commander believes the latter instead, the priority order flips — P0 routing-line first becomes P0 dispute-link first. The [RYBBIT] data cannot separate those two histories; only a post-edit TOP re-measure can.
