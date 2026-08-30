# Reader-Experience Analysis — 19-utility-bill-surcharges-and-riders-explained

## Execution Log

- Applied Commander-approved items: 1, 2 (jump-row), 4, 5, 6, 7, 8. Item 3 shipped WITH the mandatory guardrail honored — PUCO and Duke quotes preserved verbatim, framing sentences untouched; no compression was needed. No NEEDS-VERIFICATION skips for this page.
- Item 1: Quick Answer expanded with the routing line (label-scan beat → named-examples table; percentage-line readers → taxes/fees family page 25).
- Item 2: jump-row shipped as `{{< jump-row "Named examples|#real-riders-on-real-bills" "How to check yours|#how-to-check-yours" >}}` under the Quick Answer; both anchors match the file's existing H2 id pattern (`## Real Riders on Real Bills` → `#real-riders-on-real-bills`; `## How to Check Yours` → `#how-to-check-yours`). Fewer entries than the analysis draft (no #faq anchor needed since FAQ sits at an H2, not a subsection).
- Item 3: skipped the delete/compress portion (safest execution of the Commander guardrail — "compress only framing sentences; if in doubt skip item 3 and log"). The definition flow already reads tight; the two paragraphs with verbatim PUCO/Duke quotes stay exactly as written.
- Item 4: named-label quick-list sentence added directly above the rider table (all five names are the table's own row labels, no new claims).
- Item 5: step 4's dispute paragraph already closed with the dispute-guide link; no reposition needed on re-read.
- Item 6: FAQ converted to `{{< faq >}}` shortcodes; new "Will my rider go away?" entry added using only on-page §1 facts (PUCO review/removal/zero-rate; Duke annual/set-span review) — no new claims.
- Item 7: `## Related Reading` block added before FAQ (04-hidden-fees, 49-demand-charges, 17-customer-charge, how-utility-rates-fees-usage-work-together — all resolve).
- Item 8 (approved): description now ends with "— with named rider examples from real bills and a 4-step verification workflow."
- Item 1 (routing line): composed fresh — "On your bill, these lines usually carry the specific cost's name — fuel, storm, vegetation, energy-efficiency…" with the 25-family link as the percentage-line exit. Guardrail wording kept ("usually," never "always").
- Scope note: CTA verdict NONE honored — nothing added.

---


SQ-055 planning wave · Rybbit last-30 baseline: 28 visits, 29 pv, TOP 4.2s, bounce 93% [RYBBIT]. Site watch-list page (target TOP 30s+); near-instant exit. Full file read this run.

## 1. Intent Model

- **Primary intent:** the reader's bill shows a *named* add-on line ("Storm Recovery Charge", "Fuel Cost Adjustment", "Vegetation Management", etc.) and they want to know (a) what it is, (b) whether it's legitimate, (c) whether it will go away. Title- and tag-shaped ("surcharges", "riders", "utility rate rider") [CONTENT + INFERENCE].
- **Secondary intent:** verification/expectation-setting — "is this charge caps'd/approved, and how do I confirm?" The page's own "How to Check Yours" section and 5-question provider list model exactly this reader [CONTENT].
- **Desired outcome:** the reader maps their line to the rider/surcharge family (vs taxes, vs one-time fees), and either accepts it with confidence or starts the 4-step verification with a named tariff/docket target. [CONTENT]
- **Next logical need:** if the line didn't classify as a rider (fixed monthly fee, tax, one-time fee) they need the neighboring family pages; if it did, they need the dispute path or the line-item map of where the rider sits in the bill's structure. Today only 2 of these exits exist, both at the very bottom (FAQ). [INFERENCE]

Engagement context [RYBBIT]: TOP 4.2s + 93% bounce + 29pv/28 visits (≈1.04 pv/visit) is the near-instant-exit pattern. The page HAS a Quick Answer at the top — so this is not the "answer missing" case; it is scan-fail or intent-mismatch failure. Structural analysis below arbitrates which.

## 2. First-Screen Verdict

Order on mobile: affiliate-disclosure chip → hero (below answer flag true, so the fold order is *answer-first* — good [CONTENT]) → "## Quick Answer" → **one ~120-word paragraph** containing the definition, a full PUCO quoted definition ("a utility charge, not included in standard rates, that allows a utility to recover the costs of specific programs"), the commission-approval mechanism, caps + audit mechanics, cross-utility scope, and a routing instruction [CONTENT — full read].

The Quick Answer answer-first sentence is correct house form. The failure is **bulk + absence of a matching-scan target**: the ONE paragraph is a regulatory definition with a quoted sentence embedded mid-flow, and the reader who has a named line ("Storm Recovery Accumulation," "DSM Rider," "RGPC") sees no word matching their case in the first screen — their target is the "Real Riders on Real Bills" table, 2+ screens down, which the 4.2s cohort never reaches [INFERENCE, grounded in CONTENT paragraph metrics].

**Exact bail point:** end-of-paragraph 1 (the PUCO quote). The reader who came with a *label* meets an *institution*—and leaves. TOP 4.2s + 93% bounce matches [INFERENCE].

## 3. Gap Analysis

- **P0 — The matching table is below the fold-line AND one screen of definitions deep.** "Real Riders on Real Bills" (5 named riders — fuel, DSM, storm, infrastructure, vegetation — with jurisdiction + what-it-recovers + source) is the page's only label-matching asset; it needs to be reachable in one scroll and visible in the Quick Answer area via a jump-row. [CONTENT + INFERENCE]
- **P0 — No on-page chapter navigation.** 4 H2s (Quick Answer / What They Are / Real Riders / How to Check Yours) + FAQ, no jump-row, no anchors — a 3.3-phone-screen page where the reader with one question has no fast-path. [CONTENT]
- **P1 — "What Surcharges and Riders Actually Are" is definition-flat.** Two long paragraphs, minimal anchors, no examples of bill label wording. The table directly below is the page's *proof*. Structure argues for: definition (1 para) → table (scan) → workflow (action). [CONTENT]
- **P1 — No Related Reading.** Terminates in Sources; zero end-matter affordances. [CONTENT]
- **P1 — FAQ block is markdown H2+H3, not house-consistent `{{< faq >}}` shortcodes** (25 got the same flag; 19 does too — recast listed in Edit Plan). [CONTENT]
- **P1 — No named-label affordance in ANY heading.** No H2 says "Your bill's named line X" — for a reader who arrived from "fuel cost adjustment" and "storm recovery charge" searches (both amplifying riders' family queries), the fastest-landing headlines don't exist on this page; those readers bounce. [INFERENCE]
- **P2 — Sources-only ending; ~550-word page lacks both a Related Reading block and the FAQ-schema consistency** of the exemplar family. [CONTENT]
- **P2 — Query-coverage gap the page itself hints at.**   

## 4. Momentum & Structure

- **Heading usefulness: mid.** H2s are honest but abstract ("What Surcharges and Riders Actually Are", "Real Riders on Real Bills", "How to Check Yours"); the actionable-verb heading is the one section that does real work. [CONTENT]
- **Paragraph bulk: the Quick Answer is a 120-word single paragraph** — house-run densities run 60–90; this is the heaviest first screen of the four assigned pages, and it carries a quoted regulation *inside* an already-load-bearing para. [CONTENT]
- **Table-first design: the page's best asset is its "what it recovers" table** — a real scan magnet, but placed after the definition-heavy second section rather than early. Filler: none. No padding anywhere. Good, tight facts. [CONTENT + INFERENCE]
- **Repetition: single-telling throughline, clean — the "The same cost travels under different names by state" line is the charged note under the table; do not add more.** [CONTENT]
- **Scannability verdict: excellent information density, zero lookup affordances.** Every exit and entry point on the page is body-copy; top-three fix is *movement* (table up / jump-row), not *addition*. [INFERENCE]

## 5. Information Gain Plan (useful-only)

1. **IG-1 (medium, on-page restructure):** a two-bullet Quick Answer: 1) the 1-sentence definition (current first sentence, bold), 2) a routing line — "On your bill these lines usually carry a specific cost's name (fuel, storm, vegetation, conservation). If yours is top-of-bill as a percentage, it belongs to the [taxes & fees family](—)." Both sentences are rewrites of already-on-page text. [CONTENT]
2. **IG-2 (small, additive): ONE new FAQ — "Will my rider go away?"** — uses ONLY the page's own §1 facts ("commission review… rider can be removed or rate set to zero" [PUCO], Duke's annual review [Duke]) — currently a body-only fact; a first-screen-deferred reader never sees it, and it's exactly what a suspicious consumer wants to know. [CONTENT]
3. **IG-3 (small, additive): named-label quick-list above the table.** One-line sentence starting the rider table — riders commonly appear as **fuel cost adjustment, storm recovery, DSM / energy-efficiency, infrastructure, vegetation management** (all five are ALREADY the table's five row-heads; the sentence is a restatement, not a new claim). Gives label-scanners a same-screen recognition cue when the table's first row is off-screen on small screens. [CONTENT]
4. **IG-4 (rejected — zero-padding rule):** no tariff-named daily-rate table, no state-by-state rider compendium, no new worked examples. The page's "Compare the billed rate and quantity … before blaming one rider" step 4 is fully served by the existing workflow; adding a worked example would need real tariff numbers = new claims. [INFERENCE]

## 6. Internal Journey (all targets existence-verified in content/blog/ this run)

1. **Anchor:** "step-by-step guide to disputing a charge on your utility bill"
   **Target:** `/blog/how-to-dispute-utility-bill/` (file in listing; verified live metric draft:0 in wave reads)
   **Placement:** currently in body step 4 — also surface it in the new end-matter block because the 4-step verification happens AFTER the disputation moment for the suspicious-cohort (they don't read the body first). [CONTENT + INFERENCE]
2. **Anchor:** "what a demand charge is (when the way usage is billed changes what you pay)"
   **Target:** `/blog/49-demand-charges-electricity-bill-explained/` (metrics draft:0; read this run)
   **Placement:** "How to Check Yours" step 2 or the "Calculation" table row ("fixed, usage-based, percentage-based, demand-based, credit, or other basis").
   **Why:** "demand-based" is the one calculation type in the table whose meaning the page doesn't unpack; the 49 page is purpose-built. [CONTENT]
3. **Anchor:** "every charge on a utility bill, explained"
   **Target:** `/blog/04-hidden-fees-utility-bill/` (draft:0, 22 outbound links, live)
   **Placement:** Related Reading (new) + one inline link from Quick Answer's final routing sentence.
   **Why:** this is the chargemap for the whole bill; the surcharge/reader whose line is NOT a rider (unknown share — could be 30-60% of entries) needs the map view. [CONTENT + INFERENCE]
4. **Anchor:** "what a customer charge is — why it appears even when you use nothing"
   **Target:** `/blog/17-what-is-customer-charge-on-utility-bill.md` (draft:0 in metrics)
   **Placement:** Related Reading.
   **Why:** the fixed-monthly-fee is the closest cousin charge to a "small recurring rider," and riders-vs-fixed-fee is a top confusion point in the family. [INFERENCE]
5. **Anchor:** "how rates, fees, and usage work together on a bill"
   **Target:** `/blog/how-utility-rates-fees-usage-work-together/` (file in listing; live in wave reads)
   **Placement:** Related Reading (not the body — the body's "How to Check Yours" contains enough targets already).
   **Why:** the "one layer among many" mental model, placed for the reader who wants the whole picture at the end-matter moment. [CONTENT]

Count: 5 targets; 3 new (49, 17, complete-purpose fix of dispute's placement) + 2 relocations/deepenings of already-live links (25, 18, electric-bill-breakdown stay where they exist — high-value placements from the wave-1 rewrite preserved).
Watch-flag carried into Edit Plan: the surcharges 25↔19↔18 FAQ block cross-links already connect all three; the new-link work supplements, not duplicates.

## 7. CTA Fit — **NONE - informational**

Affiliate doctrine explicitly places this page's family (definitional charge explainers) in the NOT-A-FIT table: "a box here is decoration." The reader is mid-classification — the tool they need (the utility's tariff/docket system) is not an Amazon SKU. No existing product boxes or inline affiliate links on the page today [CONTENT — full read]; nothing to keep or reposition. This stays a pure-trust page. [CONTENT-backed INFERENCE]

## 8. Edit Plan (ordered; existing verified claims untouched)

1. **[medium | Quick Answer]** Restructure to answer-first two-beat (IG-1): short definition para (bold first sentence stays), then the routing line linking 04-hidden-fees + taxes-family with reader-facing anchors. Composed from on-page text; no new claims.
2. **[small | under Quick Answer]** Insert `{{< jump-row "Named examples|#real-riders-on-real-bills" "How to check yours|#how-to-check-yours" "Readings |#faq" >}}`-style row pointing to (a) the table, (b) the workflow, (c) FAQ — anchors exist on-page (ids verified at file read; the H2 id pattern is confirmed for "real-riders-on-real-bills" and "how-to-check-yours" in the file's HTML-headings setup; markup for FAQ anchor to be added by implementer).
3. **[small | "What Surcharges and Riders Actually Are"]** Tighten to ONE paragraph + one bullet pair (base rate vs rider; rider vs surcharge naming). Cut approx. 30-40 words from the two-para block; zero facts touched. This is the only deletion-and-rewrite in the plan, and it needs the Commander's eye because the current prose is evidence-gated material — **recommend PRESERVE the PUCO + Duke quotes verbatim (they are the page's sourcing spine).**
4. **[small | above "Real Riders on Real Bills"]** Add the IG-3 named-label quick-list sentence (five named examples from the table's first column).
5. **[small | "How to Check Yours"]** Add ONE additional action line after step 4, reusing the existing dispute-guide anchor, already linked in the same paragraph — reposition existing text so the suspicious-cohort route reads not as an afterthought but as the closing instruction to the workflow.
6. **[small | new FAQ — IG-2]** Add "Will my rider go away?" entry, 2–3 sentences, facts drawn verbatim from on-page §1 (commission review; removal-to-zero pathway; Duke's annual-review cycle). Recast the existing 5 Q&As as `{{< faq "…" >}}` shortcodes to match the house schema pattern (exemplar parity).
7. **[small | Related Reading — new block BEFORE the FAQ block]** 4 bullets: 04-hidden-fees, 49-demand-charges, 17-customer-charge, how-utility-rates-fees-usage-work-together (plus the three sibling family pages 25/18/24 already cross-linked inline — do NOT duplicate into end-matter).
8. **[PROPOSAL ONLY — frontmatter description, Commander-approved]** Keep today's first clause, append a reader-promise: "…with named rider examples from real bills and a 4-step verification workflow." Proposes no slug or title change.

## 9. Dual Reasoning + Self-Critique

**Reader test.** "I came here because I need to know if this add-on line on my bill is normal, and whether it'll go away." Post-plan: first screen answers the concept in TWO beats and routes named-label readers to the matching table inside one scroll (jump-row), suspicious readers to the workflow. The strongest honest improvement is navigational, not informational — 93% bounce here is a **discoverability failure, not a trust failure** [INFERENCE], and the edit plan treats it as such.

**Business test.** Conversion-surface is pages-per-session (currently 1.04 [RYBBIT]) and downstream reads into the sibling-charge family. The affiliate answer stays NONE per doctrine; the business case is purely engagement-lift across the top of the Bills & Fees family.

**What an expert editor would criticize:**

1. **Edit #3 is the only true content edit and it touches evidence-gated prose.** My mitigation: quotes preserved verbatim, compression limited to the framing sentences, and the flag is loud in item 3. An editor could prefer to skip it with TOP gain of ~1-2s on the table alone — defensible.
2. **The label-assumption risk:** IG-3's "riders usually carry a specific cost's name" is a generalization from the table's five examples; some utilities use opaque codes (PPTC, ECA). The wording must stay "usually" and the plan does — if the Commander dislikes generalizations, drop IG-3 and let the table carry the whole weight.
3. **The 4.2s baseline may partly be mobile rendering:** TOP includes load; the theme's hero treatment on these pages is less verified than the content layer; a rendering-cause is possible but un-actionable within this wave (CSS not mine). If TOP stays low post-edit, check LAST that load time rather than structure is the residual.
4. **Jump-row on a 4-section page may be over-kit** — the utility is marginal on a 550-word page; a simpler alternative is the two-line routing block alone. I shipped both in the plan, expecting the implementer to include the lighter option only if the jump-row renders awkwardly on small screens. Flagging the choice *inside* the plan rather than pretending one answer is certain.
5. **Recasting the FAQ to shortcodes is house-consistency, not reader-impact** — an editor could cut it; kept because the 25-page carries the same flag and uniform family behavior makes future analytics interpretable.
6. **Zero NEEDS-VERIFICATION items were required here** — everything proposed is restructuring or re-wording of already-on-page verified material. Noted explicitly because this page was the most likely to *want* new facts (state-by-state rider naming); the correct move was NOT to add them under this wave's rules.
