# APEX Reader-Experience Analysis — average-water-usage-per-person

**Squad:** SQ-055 planning wave · **Author:** lieutenant · **Date:** 2026-08-29
**Baseline (Rybbit 2026-07-30 → 08-29):** 25 visits / 27 pv · TOP 13.4s · bounce 88% [RYBBIT]
**File:** `content/blog/average-water-usage-per-person.md` — read in full this run. THIN page: mission baseline 527 words; metrics index says 447 (post-audit updates since). No FAQ, no table, no product boxes. [CONTENT]

---

## Execution Log (implemented 2026-08-29 by lieutenant)

- W1+W2 applied: duplicate pre-calc paragraphs merged into one "Before you calculate" line; QA rebuilt to lead with the two-division calculation, snapshot caveat and EPA citation sequenced after (hedges kept, reordered).
- W3 applied: worked example added under the 5-step list (12÷30÷3 arithmetic, only on-page figures); ccf-calculator link appended.
- W4 applied per Commander ruling: ~2–4 CCF/person/month stated WITH attribution to the CCF explainer + link (attribution form); no standalone claim.
- W5 applied: journey links placed — why-is-my-water-bill-higher-in-summer (Calculate), water-meter-leak-indicator + is-your-toilet-running-leak-test (Baseline Changes), 44-how-to-lower-water-bill (closing off-ramp); one duplicated "don't infer a leak" caution structure kept intact (single sentence).
- W6 applied: Related Reading (5 bullets) + 3-question FAQ with faq-schema added before Sources; CCF link also anchored at calc step 1 per §6 consolidation.
- W7: affiliate disclosure not added — page carries no affiliate links; template governs.
- W8 applied as Commander exception: `hero_below_answer: true` added; `updated: 2026-08-29`; meta description untouched.
- Skipped: none from the approved plan. IG-5 (gallons-per-activity block, [NEEDS-VERIFICATION]) NOT executed — no verified per-activity figures on disk; packet approves only the 2–4 CCF benchmark attribution. W7 template check also skipped (no run_command in this wave; no affiliate links to disclose).
- Self-check: all internal links resolve to verified slugs (ccf-calculator, what-is-ccf-on-a-water-bill, water-meter-leak-indicator-explained, is-your-toilet-running-leak-test, 44-how-to-lower-water-bill, why-is-my-water-bill-higher-in-summer); no product box added (NONE verdict); no new facts, ASINs, or numbers beyond the attributed benchmark; Sources remains the final section after FAQ.

## 1. Intent Model

- **Primary intent:** benchmark check — "is my household's water usage normal?" The reader has a number (from their bill) or is about to get one, and wants a reference point. [RYBBIT — the slug itself ranks for 'average water usage per person']
- **Secondary intent:** anxiety triage — "if it's NOT normal, what's wrong?" The page's own tags (`water bill`, `leak detection`) and the sibling page that links here with anchor "a practical range" both confirm this is the expected second beat. [CONTENT]
- **Desired outcome:** a yes/no/maybe against a trusted band, plus the first step of the next action if the answer is 'maybe high'. [INFERENCE]
- **Next logical need:** leak check (toilet-running test, leak indicator), conservation playbook (44-how-to-lower-water-bill), and seasonal context (summer/winter bill shifts). [CONTENT — the site owns all of these]
- **Metric read:** TOP 13.4s / 88% bounce = the reader confirms there is no benchmark here and leaves. Shortest dwell of the assigned three on a page whose entire promise is comparison data. [RYBBIT]

## 2. First-Screen Verdict

- **Layout:** page does NOT set `hero_below_answer` (verified against the site's flag list) — mobile first screen = title + hero, QA pushed below the fold. Known instant-exit defect. [CONTENT]
- **QA content:** first bolded sentence is a hedge: "A per-person water-use figure is useful only as a snapshot for that billing period, not as a universal target or leak diagnosis." The reader has scrolled past a hero to be told their question is malformed. [CONTENT]
- **The "this isn't giving me what I came for" point:** the QA never supplies any normal-range value or even promises one — for a page whose slug and inbound anchor text both promise "average / practical range", the first screen contains zero reference numbers. The reader's verdict on the page is formed by sentence two: 'no benchmark here.'
- **Answer reachable in 2 sentences + one scroll: NO** — the literal intent (a comparison reference) is unreachable on the entire page, not just the first screen.

## 3. Gap Analysis

**P0 — kills satisfaction**
- **P0-1 · The page never answers its own keyword.** Slug = `average-water-usage-per-person`; the article contains no average, no range, no benchmark of any kind — by design, after the AEP-08-29 evidence audit stripped unverifiable figures. The sibling `what-is-ccf-on-a-water-bill.md` links here with "average water usage per person for a practical range" — that anchor promise is unfulfilled on arrival: double loss, this page's readers AND the sibling's referral credibility. [CONTENT — sibling anchor verified in its 'Is your CCF normal?' section]
- **P0-2 · Duplicate editorial scaffolding in the opening.** Two consecutive pre-calculation paragraphs both exist: the '**Next step:**' paragraph and the '**Before calculating...**' paragraph — BOTH link `what-is-ccf-on-a-water-bill`, and the second redundantly re-lists the leak pages the first already sent you to. Reads like two draft intros stapled together, front and center of a 527-word page. [CONTENT]

**P1 — degrades satisfaction**
- **P1-1 · All caution, no procedure payoff.** The five numbered calc steps tell the reader to divide usage by days and by people, but never show the arithmetic once — no worked example anywhere. For a benchmark-checker, the fastest satisfaction would be one example line; it costs three sentences. [CONTENT]
- **P1-2 · Dead end after 'not normal'.** No on-page path TO the fix: the page says 'compare similar periods', 'conduct a safe no-use meter observation', 'contact the utility' — but never reaches the site's toilet-leak test, leak-indicator, or lower-your-water-bill plays. [CONTENT]
- **P1-3 · No FAQ block.** House convention (end-of-article `{{< faq >}}` + `{{< faq-schema >}}`) missing on a page whose question breeds obvious follow-ups ('how many gallons is normal per shower?', 'does a family of 5 use twice as much?'). [CONTENT]

**P2 — polish**
- No 'Related Reading' section (house convention: bulleted, before FAQ). [CONTENT]
- Title ('How to Calculate Water Use Per Person From Your Bill') vs slug intent ('average...') mismatch is a positioning issue; frontmatter is out of scope, so the fix must come from on-page content supplying the benchmark context, plus a meta-description proposal (§8).
- 'Sources' renders as the final section with nothing after it — page ends on a citation list; house pattern ends with FAQ + Related Reading. [CONTENT]

## 4. Momentum & Structure

- **Headings:** four H2s (Quick Answer / Calculate Your Household Baseline / Separate Indoor, Outdoor, and Shared Use / When the Baseline Changes) — an accurate skeleton for the snapshot method, but every section ENDS in a caution rather than a next step; the reader is never released into action. [CONTENT]
- **Paragraph bulk:** fine; short paragraphs, two bullet lists, one numbered list. For 447 words there is no bloat to cut — the problem is absence, not bulk. [CONTENT]
- **Repetition:** the 'Next step' / 'Before calculating' pair (P0-2), plus two consecutive passages in 'When the Baseline Changes' that both say 'don't infer a leak from a national number'. [CONTENT]
- **Scannability verdict:** structurally scannable but every section terminates in a disclaimer; feels like a disclaimer with article-shaped packaging.

## 5. Information Gain Plan

Useful-only; the page is thin so additions are proportionate — target roughly 750–900 words, not 2,000.

- **IG-1 · Worked baseline example** (arithmetic only, no external facts): 'Example: your bill shows 12 CCF over a 30-day period for a household of 3. 12 / 30 = 0.4 CCF/day; 0.4 / 3 = 0.13 CCF per person per day (about 4 CCF/person/month).' Pure division; zero new facts. Sits directly under the 5-step list. [CONTENT]
- **IG-2 · Benchmark context line, reusing the site's existing on-disk figure [NEEDS-VERIFICATION]:** the sibling CCF page already states 'a typical household uses about 2-4 CCF per person per month' (its leak-indicator image caption) and survived today's evidence audit. One sentence here — 'For a rough per-person range, see the 2-4 CCF per person per month benchmark on our CCF explainer' — delivers the promised reference WITHOUT creating a new claim; flag it at insertion so the implementation wave confirms the range's sourcing memo covers prose reuse. [CONTENT + NEEDS-VERIFICATION]
- **IG-3 · 'What pushes a normal number up' checklist** (3-4 bullets, existing content only): irrigation/pool, guests, season, fixture changes — each one line, each expandable via the journey links. Restructures bullets already in 'When the Baseline Changes'. [CONTENT]
- **IG-4 · 3-question FAQ** (+ faq-schema): (1) 'How do I convert my CCF figure to gallons per person?' — route to the `ccf-calculator` tool (link, not new math); (2) 'Is laundry included in normal usage?' — answer with the shared/indoor/outdoor split the page already teaches; (3) 'When does a high number mean a leak?' — the no-use meter observation + link to the toilet-leak test. No new facts. [CONTENT]
- **IG-5 · OPTIONAL [NEEDS-VERIFICATION]:** a small gallons-per-activity context block (shower, load of laundry) would directly satisfy the benchmark intent with figures EPA WaterSense publishes — but NO verified figures exist on disk; implementation wave must source and verify or skip. Listed because it is the single highest-value gap for this reader.

## 6. Internal Journey

All targets verified on disk this run (file under `content/blog/` + slug frontmatter). Six journey links:

1. **'What CCF means on your water bill'** → `content/blog/what-is-ccf-on-a-water-bill.md` — keep, but CONSOLIDATE: merge the two duplicate early references into ONE anchor placed at step 1 of the calculation ('find the total water use and the unit shown on the bill'). [target verified]
2. **'The CCF-to-gallons (and dollars) calculator'** → `content/blog/ccf-calculator.md` — placement: end of the worked example (IG-1). *Why:* benchmark-checkers instantly want their number in gallons/dollars; the site owns a purpose-built tool page. [target verified]
3. **'Is your toilet running? A 10-minute leak test'** → `content/blog/is-your-toilet-running-leak-test.md` — placement: 'When the Baseline Changes' (visible leaks bullet). *Why:* toilets are the classic hidden cause of a high per-person number. [target verified]
4. **'Your water meter's leak indicator'** → `content/blog/water-meter-leak-indicator-explained.md` — placement: keep ONE of the two current mentions (dedupe per P0-2), anchored at the no-use meter observation sentence. [target verified]
5. **'How to lower your water bill'** → `content/blog/44-how-to-lower-water-bill.md` — placement: closing line of 'When the Baseline Changes' ('if your number genuinely is high, here is the fix-it playbook'). *Why:* the organic next act for every 'I'm above range' reader. [target verified]
6. **'Why your water bill is higher in summer'** → `content/blog/why-is-my-water-bill-higher-in-summer.md` — placement: 'compare it with a similar season' sentence in the 'Calculate' section. *Why:* seasonal drift is the most common innocent explanation for a baseline jump. [target verified]

## 7. CTA Fit

- **Reader's intent stage:** benchmark check — pre-diagnosis, pre-purchase. Nothing in AFFILIATE-PLACEMENTS maps a product to 'is my usage normal' (a monitor/sensor answers 'is something LEAKING' — one step later, and covered by other pages).
- **Existing placements:** zero. [CONTENT]
- **Doctrine check:** the plan's water-cluster rule ('avoid double-monetizing near-identical water pages before consolidation') plus the NOT-A-FIT principle for number-look-up pages both point the same way. The Govee sensor box would duplicate `06-water-bill-too-high`'s placement and burn trust at the reader's most neutral moment.
- **Verdict: NONE - informational.** Re-evaluate ONLY if the water cluster consolidates and the Tier-1 sensor placements ship; then a single sensor box at the leak-check moment could earn its place.

## 8. Edit Plan

Ordered, section-level, targeted. The page is thin; additions are proportionate — no padding, stop at ~900 words.

| # | Change | Section | Size |
|---|---|---|---|
| W1 | Merge the duplicated pre-calc paragraphs (P0-2): one paragraph 'Next step' that names the unit explainer + leak-indicator links once; delete the second paragraph's duplicate CCF link and leak list. | Quick Answer tail | small |
| W2 | Rebuild Quick Answer to LEAD with the calculation promise and release the caution second: bolded 'You can calculate your own per-person water use in two divisions: daily usage / people in the home' — then the existing snapshot caveat as sentence two. [No new claims; reorders verified on-page statements.] | Quick Answer | small |
| W3 | Insert IG-1 worked example under the 5-step list; append journey link #2 (ccf-calculator). | Calculate Your Household Baseline | small |
| W4 | Insert IG-2 benchmark context [NEEDS-VERIFICATION] sentence + link: 'For a rough range, see the 2-4 CCF per person per month benchmark on our CCF explainer.' | Calculate section | small |
| W5 | Convert 'Separate Indoor, Outdoor, and Shared Use' + 'When the Baseline Changes' endings from dead ends into action: add links #3, #4, #5, #6 at the sentences named in §6; cut one duplicated 'don't infer a leak' sentence. | sections 2-3 | small |
| W6 | Add house end-matter: '## Related Reading' bullets (CCF explainer, 44, toilet test, leak indicator) + 3-question `{{< faq >}}` block with `{{< faq-schema >}}` (IG-4) — placed BEFORE the Sources section per house convention. | end matter | medium |
| W7 | Verify whether `{{< affiliate-disclosure >}}` is injected sitewide by the template before considering it on this page — no CTA here, so only add if house convention requires it on standalone pages; omit if template handles it. (Optional; verify at implementation.) | template check | trivial |
| W8 | Frontmatter, proposal only: add `hero_below_answer: true`. Meta description PROPOSAL (out of scope, proposal only): current description undersells the benchmark intent; suggest 'Work out your own household's water use per person from your bill — and compare it to typical per-person ranges for US homes.' | frontmatter | small |

Net word delta: +250-350 (thin page); 8 edits, all targeted.

## 9. Dual Reasoning + Self-Critique

**Reader test — 'I came here because I need to know if my water usage is normal.'** Post-plan: the first screen states the two-division calculation and shows one worked example; the rough range is one click away via the site's own benchmark sentence; every 'something's off' instinct now has a named next page (leak test, leak indicator, seasonal explainer, fix-it playbook). The 13.4s reader now has a reason to reach 30s+. [RYBBIT + CONTENT]

**Business test — what natural action follows trust?** None that Amazon sells at this step — and pretending otherwise is what the doctrine's NOT-A-FIT table exists to prevent. The business win is JOURNEY breadth: this page becomes the hub that feeds the leak cluster and `44`, which are where the site's money pages live. The business outcome here is measured in pages/session (site average 1.235), not clicks. [INFERENCE + doctrine]

**What an expert editor would criticize about this plan:**
1. **IG-2 leans on a benchmark the site itself may not want repeated.** The 2-4 CCF/person/month line survived the audit as an image caption; promoting it into prose (here or anywhere) re-opens a sourcing question the audit closed. The NEEDS-VERIFICATION flag is the honest handling, but the Commander may prefer a hard skip over a flag-and-check.
2. **W2's QA rewrite reorders existing statements but changes the page's tone from 'guardrail' to 'tool'.** That is the right reader-experience call [INFERENCE], but it partially unwinds the deliberate post-audit posture; the implementation wave should keep every existing hedge sentence present, just sequenced after the calculation.
3. **The plan adds the most possible value and the least possible length at the same time — the real risk is under-delivery.** If IG-5's verified benchmark block can be sourced, the page should take it (it is the actual answer to the search); I prioritized no-new-claims over completeness. Flagged for a possible follow-up mission with fact-checking support.
4. **No metric isolates scroll depth on this page** — 'reader bounces at the QA' is inferred from TOP + bounce + content shape, not from a heatmap. An uncorrelated seat should recheck the sibling-anchor claim ('practical range' on the CCF page) and the worked-example arithmetic before ship.
