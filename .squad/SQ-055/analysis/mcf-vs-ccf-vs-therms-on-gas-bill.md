# APEX Reader-Experience Analysis — mcf-vs-ccf-vs-therms-on-gas-bill

**Squad:** SQ-055 planning wave · **Author:** lieutenant · **Date:** 2026-08-29
**Baseline (Rybbit 2026-07-30 → 08-29):** 27 visits / 28 pv · TOP 37.1s · bounce 89% [RYBBIT]
**File:** `content/blog/mcf-vs-ccf-vs-therms-on-gas-bill.md` — read in full this run. Metrics index undercounts this page (raw-HTML body: reports 0 internal links / 0 tables / 0 quick-answer); file read is authoritative.

---

## Execution Log (implemented 2026-08-29 by lieutenant)

- E1 applied: Quick Answer rebuilt (raw-HTML idiom kept), stray `<p># MCF vs CCF...</p>` title-echo deleted, stuffed fragments gone, Next step journey line added (→ /blog/12-how-to-read-your-gas-bill/).
- E2 applied: Scenario C rebuilt as clean 15 MCF × $10.50 = $157.50 → 155.55 therms → $1.01/therm; false start (0.15 MCF/$1.65) and all Note:/Corrected debris removed; retitled "(High-Usage Home)"; MCF-scope clause kept.
- E3 applied: all three keyword-stuffed exact-match fragments removed.
- E4 applied per Commander ruling: "(1,000 CCF)" error fixed (CCF/MCF display-convention clause); "divides the rate by 10" clause cut.
- E5+E6 applied: 4 new journey links (12, 18, 07, how-to-read-gas-meter) + 2 benchmark links retargeted to canonical /blog/average-utility-bills-by-state-2026/; Related Reading added before FAQ.
- E7+E8 applied: duplicate 1.037 walkthrough compressed to one worked example; IG-1 statement checklist added post-table; IG-2 inverse-conversion FAQ added; IG-3 Dth/MMBtu connective sentence added.
- E9 applied as Commander exception: `hero_below_answer: true` added; `updated: 2026-08-29`.
- Skipped: none from the approved plan (IG-4 was not in the approved plan — no NEEDS-VERIFICATION items executed).
- Self-check: all internal links resolve to verified slugs; arithmetic 15 × 1.037 = 155.55 and 157.50 / 155.55 = $1.01 recomputed and correct; no new facts or ASINs.

## 1. Intent Model

- **Primary intent:** decode the units on a gas bill — "what is CCF / MCF / a therm, and which one am I being billed in?" The 37.1s TOP is the highest of this assignment's three pages and sits in the site's engaged decode-class (the 40s-class threshold used in prior squad audits), so readers who land here stay to work through definitions and conversions. [RYBBIT]
- **Secondary intent:** rate sanity — "is my $/CCF or $/therm reasonable?" Served by "Calculating Your Cost Per Therm" and "Real-World Bill Scenarios." [CONTENT]
- **Desired outcome:** reader converts their own bill's unit to therms and can judge whether their rate is normal — every ingredient for this already exists on-page. [CONTENT]
- **Next logical need:** (a) locate these units on their own statement, (b) diagnose an abnormal result (why-is-gas-high path), (c) understand the BTU/fuel adjustment line item the article itself introduces. [INFERENCE, anchored to existing sibling pages]

## 2. First-Screen Verdict

- **Layout:** this page does NOT set `hero_below_answer` (frontmatter verified; the flag list confirmed for 13 other pages does not include it). The hero image renders before the body: mobile first screen = title + hero, answer pushed one scroll down. This is the site's documented instant-exit layout defect. [CONTENT]
- **The Quick Answer block is visibly broken.** It opens with a raw-HTML artifact — a paragraph containing a literal markdown title line: `<p># MCF vs CCF vs Therms on Your Gas Bill: What the Units Actually Mean</p>` — i.e., the page title repeats as stray plain text directly under the "Quick Answer" heading. At the most trust-loaded moment of the page, it reads as a template glitch. [CONTENT — exact quote from file]
- The first *sentence* of the QA is actually good (therms = energy; CCF/MCF = volume) and would satisfy the "2 sentences + one scroll" test — **but** it is followed immediately by keyword stuffing: "Understanding MCF vs CCF vs therms on gas bill is essential for spotting billing errors, comparing utility rates…" — the ungrammatical exact-match phrase, three times in the body. [CONTENT]
- **The "this isn't giving me what I came for" point:** the stray repeated-title paragraph (looks like a rendering error), immediately compounded by the stuffed second half of the same paragraph. A skimmer decides the page is low-quality before reaching the true answer.

## 3. Gap Analysis

**P0 — kills satisfaction**
- **P0-1 · Trust collapse in the centerpiece section.** "Real-World Bill Scenarios → Scenario C: The MCF Bill" contains the author visibly correcting themselves mid-example: "$1.65 (Note: This rate seems low, MCF rates are often quoted differently for small users)" → "Corrected Commercial Rate: Let's assume $10.50 per MCF" → "$1.575 (This is clearly a residential example using MCF notation)" → "Realistic MCF Example: 15 MCF Usage at $10.50 per MCF = $157.50." Two half-computations collide with editorial notes left in. This section is the article's payoff — proof that conversion changes the answer — and it reads as unfinished. [CONTENT]
- **P0-2 · Broken-looking first screen.** The stray `<p># MCF vs CCF vs Therms…</p>` title-echo inside Quick Answer (quoted in §2). [CONTENT]

**P1 — degrades satisfaction**
- **P1-1 · Keyword stuffing reads machine-written.** "understanding MCF vs CCF vs therms on gas bill is essential…" (QA ¶1), "The most important distinction in understanding MCF vs CCF vs therms on gas bill is…" ("The Critical Difference" ¶1), "If you are trying to understand MCF vs CCF vs therms on gas bill regarding price…" ("Calculating Your True Cost Per Unit → The Rate vs. The Bill"). The third example is not grammatical English. [CONTENT]
- **P1-2 · Internal inconsistency a unit-decoder will catch.** "Commercial vs. Residential": "To reach 1 MCF (1,000 CCF), a home would need to be exceptionally large" — the article's own MCF section and conversion table say 1 MCF = 1,000 cubic feet = ~10 CCF. On a page whose entire job is unit precision, this is self-undermining. [CONTENT]
- **P1-3 · No journey off-ramps.** Only 4 internal links across ~3.1k words, two of which point at the same benchmark page. Nothing serves the immediate next needs: read your gas bill, why is gas high, where the number comes from (meter), what the BTU adjustment line item is. [CONTENT]

**P2 — polish**
- No "Related Reading" section (house convention: bulleted, before the FAQ). [CONTENT]
- Both benchmark links route via the alias `/blog/02-average-utility-costs-2026/` (verified live: alias of `average-utility-bills-by-state-2026.md`) — resolve fine today, but canonical hrefs are sturdier. [CONTENT]
- Missing `hero_below_answer: true` (frontmatter; proposal only per mission scope). [CONTENT]

## 4. Momentum & Structure

- **Heading skeleton is genuinely good:** defined units → volume-vs-energy → conversion math → why utilities differ → per-unit cost → scenarios → budget → reduction → FAQ → bottom line. A bill-decoder reads this trail naturally; no restructure needed. [CONTENT]
- **Repetition:** "How to Convert Units for Comparison" and "Calculating Your True Cost Per Unit" teach overlapping math (the 1.037 factor appears with a full worked example in both — $50 → 51.85 therms, then the subtract-fixed-fees walkthrough). "The Rate vs. The Bill" H3 is one thin paragraph that mostly restates Commodity vs Delivery already covered. [CONTENT]
- **Paragraph bulk:** scenario sections are bullet walls (`<li><strong>Usage:</strong>…</li>` chains) — dense on mobile; otherwise paragraphing is reasonable.
- **Scannability verdict:** sound spine, three localized momentum breaks — garbled QA, Scenario C's self-correction, duplicated cost math. Fix all three without touching the skeleton.

## 5. Information Gain Plan

Useful-only; article is already complete — additions stay small.

- **IG-1 · "Where to find these on your own bill" mini-checklist** after the conversion table (3 lines: Usage row, rate row, BTU/BTU-adjustment factor row). Structural guidance only; zero new facts. The article explains units abstractly and never anchors them to the physical statement — the one comprehension gap a worked-example-heavy page still leaves. [CONTENT]
- **IG-2 · Inverse-conversion FAQ** (on-page math only): "How do I convert therms back to CCF to match my bill?" (divide by 1.037). Mirrors an existing FAQ's arithmetic in the other direction. [CONTENT]
- **IG-3 · Decatherm/MMBtu footnote sentence** under the conversion table ("Dth and MMBtu both equal 10 therms — you'll meet them on commercial quotes"): already stated on-page in the table; only adds the connective sentence. [CONTENT]
- **IG-4 · OPTIONAL, [NEEDS-VERIFICATION]:** a "typical residential monthly usage in CCF" context line would answer "is my 150 CCF normal?" — no such verified figure exists on disk; flag for the implementation wave to source and verify or skip.

## 6. Internal Journey

All targets verified to exist under `content/blog/` this run (by file + slug frontmatter). Draft-flagged pages excluded.

1. **"How to read your gas bill, line by line"** → `content/blog/12-how-to-read-your-gas-bill.md` — placement: end of "The Three Main Units Defined" intro paragraph. *Why:* once you know the units, the next act is finding them on your own statement. [target verified]
2. **"What the fuel/BTU adjustment on your bill covers"** → `content/blog/18-fuel-adjustment-charge-on-utility-bill-explained.md` — placement: "The Critical Difference" ¶2, anchored on the existing "BTU Adjustment Factor" sentence. *Why:* the article names the factor in passing; the sibling explains the actual line item — a direct curiosity handoff the article currently drops. [target verified]
3. **"Why your gas bill is so high — 10 causes ranked"** → `content/blog/07-gas-bill-too-high.md` — placement: end of "Impact on Your Budget and Average Costs." *Why:* the reader who just compared their rate and found it high needs exactly this. [target verified]
4. **"How to read your gas meter"** → `content/blog/how-to-read-gas-meter.md` — placement: "Calculating Your Cost Per Therm" step 1 ("Find your Usage"). *Why:* the meter is where their number comes from; answers the sub-question before it's asked. [target verified]
5. **Canonical retarget of the two existing benchmark links** → `content/blog/average-utility-bills-by-state-2026.md` (live; currently reached via alias `/blog/02-average-utility-costs-2026/`). Anchor text "average utility bills by state (2026)" / "average gas bill by state." [target verified + alias]

Count: **4 new + 2 retargeted = 6 journey links.** Top of the 3–8 range; justified by a 3.1k-word article with 4 links.

## 7. CTA Fit

- **Reader's intent stage:** definitional decode — the reader wants to understand a unit, not buy anything. The natural "action" after trust is the internal journey (diagnosis path), not a product.
- **Existing placements:** zero product boxes, zero affiliate links on the page. [CONTENT]
- **Doctrine check (AFFILIATE-PLACEMENTS-2026-08-28.md):** the NOT-A-FIT table explicitly lists definitional pages — "no product answers the question; a box here is decoration." The article's "How to Reduce Your Gas Consumption" section is the only conceivable hook (smart thermostat), but the reader is pages away from an equipment decision and the Upgrades section is generic.
- **Verdict: NONE — informational.** Considered and rejected: ecobee/Nest box in the Reduce section (definitional-page rule governs; monetize the diagnosis destination `07-gas-bill-too-high`, which already carries a box).

## 8. Edit Plan

Ordered, section-level, targeted. No rewrite — the skeleton stays.

| # | Change | Section | Size |
|---|---|---|---|
| E1 | Rebuild Quick Answer to house pattern: `## Quick Answer {#quick-answer}` markdown H2; bolded first sentence running the existing volume-vs-energy answer ("**Therms measure the heat energy you were billed for; CCF and MCF measure the volume of gas that passed your meter — and the two are not the same number.**"); **delete** the stray `<p># MCF vs CCF vs Therms…</p>` title-echo paragraph; strip the stuffed second half; append a one-line Next step (→ 12-how-to-read-your-gas-bill). | Quick Answer | medium |
| E2 | Scenario C: keep ONLY the realistic computation already on page (15 MCF × $10.50 = $157.50 → ×10.37 = 155.55 therms → $1.01/therm); delete the 0.15-MCF/$1.65 false start plus all "Note:/Corrected/This is clearly" debris; retitle "Scenario C: The MCF Bill (High-Usage Home)"; add one clause noting MCF mostly appears on commercial accounts (already stated in "Commercial vs. Residential"). No new numbers. | Real-World Bill Scenarios | medium |
| E3 | Remove the three keyword-stuffed fragments (exact strings in §3 P1-1); replace with plain phrasing. | whole body | small |
| E4 | Fix "(1,000 CCF)" → "(10 CCF)" (reconciles with the article's own table); cut the "divides the rate by 10 to make it look like a per-Centum rate" clause [restoring as stated would be NEEDS-VERIFICATION; recommend cut — the remaining sentence stands]. Commander's call: flag-and-keep is the conservative alternative. | Commercial vs. Residential | small |
| E5 | Insert journey links 1–4; retarget 2 benchmark links (§6). | per §6 | small ×6 |
| E6 | Add "Related Reading" bulleted section before the FAQ (house convention): 12-how-to-read-your-gas-bill, 18-fuel-adjustment, 07-gas-bill-too-high, average-utility-bills-by-state-2026. | pre-FAQ | small |
| E7 | De-duplicate cost math: in "Calculating Your True Cost Per Unit," compress the second 1.037 walkthrough to a pointer at the Scenarios section (or trim "The Rate vs. The Bill" H3). Keep one worked example total. | How to Convert / Calculating sections | small–medium |
| E8 | Add IG-1 "find it on your bill" mini-checklist; add IG-2 FAQ inverse-conversion entry; add IG-3 connective sentence. | post-table / FAQ | small |
| E9 | Frontmatter, **proposal only:** add `hero_below_answer: true` (matches the shipped instant-exit fix on 13 pages). Meta description: no change recommended — it already names the units and the comparison promise. | frontmatter | small |

Expected net diff: negative-to-neutral word count (deletions in E2/E7 offset additions).

## 9. Dual Reasoning + Self-Critique

**Reader test — "I came here because I need to know what CCF/MCF/therms mean on MY bill (and whether my rate is sane)."** Post-plan: the answer is sentence one, unbroken by a title echo; the scenario that should demonstrate the payoff demonstrates it cleanly; and the reader's next three questions (find it, compare it, diagnose it) each have a visible door. TOP 37.1s says the content underneath already holds attention — the plan's job is to stop damaging trust, not to rescue content. [RYBBIT + CONTENT]

**Business test — what natural action follows trust?** At unit-decode stage, none monetizable, per doctrine. The conversion happens one hop later on the diagnosis path — this plan builds the exact bridges (`07`, `12`, `18`) the doctrine's "click is a side effect of usefulness" model wants. An honest NONE on a definition page is itself a trust asset.

**What an expert editor would criticize about this plan:**
1. **E2 deletes a teaching moment.** The flailing Scenario C accidentally documents *why* MCF confuses residential readers. The replacement keeps only the clean math — the one-line "MCF on residential bills is rare" salvage must ship with it or the section loses context.
2. **E4's cut of the "divides the rate by 10" claim** removes something a reader may genuinely have seen on a real bill. The more conservative move is flag-and-keep with NEEDS-VERIFICATION; I chose cut because the sentence as written is unverifiable and confusing. Commander's tolerance decides.
3. **The plan deliberately skips full raw-HTML→markdown conversion.** That leaves the page cheap to break (as this file's current state proves) but any full-body conversion is rewrite-class risk under the "targeted edits only" rule. Recommended as a separate follow-up mission, not bundled here.
4. **None of the P0s are metric-proven** — both are inferred from on-page debris, not from scroll/exit data (Rybbit TOP is comparatively healthy here). An uncorrelated reviewer (verifier/twin_q) should confirm the Scenario C rewrite preserves arithmetic correctness before ship; the arithmetic to check: 15 × 10.37 = 155.55; 157.50 / 155.55 = $1.01.
