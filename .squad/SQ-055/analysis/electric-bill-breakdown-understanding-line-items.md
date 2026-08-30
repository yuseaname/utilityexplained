# APEX Reader-Experience Analysis — electric-bill-breakdown-understanding-line-items

## Execution Log (implemented by lieutenant, wave 2, 2026-08-29)

- Applied item 1 (P0, shipped first): dead `/blog/fixed-vs-variable-rate-electricity-plan/` in TOU section → `/blog/10-fixed-vs-variable-utility-rate/`, anchor "how to compare fixed and variable rate offers".
- Applied item 2: QA citation de-clutter — kept the two residential figures (17.30¢ 2025, 18.34¢ June 2026) in the answer; moved the 13.63¢ all-customer figure and the Electric Power Monthly / verify-the-release meta into a one-line source note under the Tip. All figures and attribution wording carried verbatim; no sourcing bracket touched.
- Applied item 3: five-line category→explainer map added below the Charge Categories table (24, 17, 18, 19, 49); table rows untouched.
- Applied items 4–6: dispute-guide escalation sentence at the end of Questions to Ask; 17 link at the end of Fixed customer charges; 23 link on the billing-period-days bullet in Start here.
- Applied item 7: Related Reading block (6 entries) and item 8 (two follow-up FAQs inside the existing faq block; faq-schema untouched).
- Skipped: none of items 1–8; item 9 not executed (IG-5 meta proposal is Commander-level only). One self-critique fix: removed a first-pass duplicate of the 17 link in the Fixed-customer-charges paragraph (kept the §6.3 end-of-section placement).
- Frontmatter: no change needed (`updated: 2026-08-29` was already set). Existing links 03/01/49/04/kwh/meter retained unmodified; all eight plan targets were draft:0 files verified before linking.

**File:** content/blog/electric-bill-breakdown-understanding-line-items.md · 1,958 words · 11 H2 / 1 H3 · 3 tables · 7 FAQs + faq-schema · 0 product boxes · updated 2026-08-23
**Internal-link count note:** .squad/content-metrics.json reports internal_links: 2, but the full read shows ~13 rendered anchors (intro blockquote ×4, Next step ×2, body ×~7) — the metrics counter evidently misses HTML a-tags; the full read governs. [CONTENT + metrics discrepancy resolved by full read]
**Traffic (Rybbit baseline 2026-07-30 → 08-29, pre-change):** 52 visits · 64 pv · TOP 57.7s · bounce 73% — best performer of the tier [RYBBIT]
**Analyst:** lieutenant, planning wave SQ-055. Analysis only — an implementation wave executes Edit Plans after Commander review. Stance per packet: **protect what works, extend the journey.**

---

## 1. Intent Model

**Primary intent [CONTENT][RYBBIT]:** decode-the-statement — the reader is staring at an electric bill with unfamiliar lines (supply, delivery, customer charge, taxes, riders) and wants each one explained and checked against their own rate plan. Evidence: title and description promise a charge-by-charge decode; the four-part Start-here model; the intro blockquote hooks readers whose one line looks wrong. Tier-best bounce (73%) says the page satisfies the widest slice of arrivals.

**Secondary intent [CONTENT]:** surprise triage — why is the total up? Served by Why bills jump and the estimated-readings/true-ups section; the Quick Answer Tip (compare the energy charge month-over-month against kWh used) is the pivot from decoding to diagnosing.

**Desired outcome [CONTENT]:** the reader can map every line on their statement to a category, verify it against their rate schedule, and know which lines are worth questioning.

**Next logical need [INFERENCE]:** depth on the specific line that worried them (delivery vs supply, the fixed monthly fee, fuel adjustments, riders, demand charges), the rate-plan tradeoffs behind the lines, and — if a line looks wrong — the dispute path. Maps to the 24, 17, 18, 19, 49, which-rate-plan, and dispute pages.

**Journey note [RYBBIT]:** 73% bounce is the tier’s best — protect it; the extension opportunity sits at the engagement peak (FAQ + category table), which today holds zero onward links (§3 P1-1).

## 2. First-Screen Verdict

Mobile sees: hero, title, Quick Answer, Tip, Next step, four-link blockquote router. [CONTENT]

- **Verdict: PASS — the right first screen; do not restructure it.** Sentence one names the four-part anatomy; the Tip gives an immediate self-check; the blockquote routes by symptom. [CONTENT]
- **Friction [CONTENT]:** the answer’s second sentence is a ~50-word parenthetical stacking three EIA figures from three vintages (13.63¢ 2025 all-customer retail, 17.30¢ residential annual, 18.34¢ June 2026) plus reader-facing meta (verify the current release at eia.gov). Citation hedging momentarily buries the four-part model inside the reader’s answer. The facts themselves are fresh-squared (SQ-051..054) — this is placement, not accuracy.
- **No this-isn’t-for-me moment identified [INFERENCE on CONTENT + RYBBIT]:** the blockquote router answers the four likeliest sub-intents one tap from the top.

## 3. Gap Analysis

### P0 — kills satisfaction
- **P0-1 · A live click on the tier’s best page routes to an unpublished draft [CONTENT + verified metrics].** The TOU/tiered section links /blog/fixed-vs-variable-rate-electricity-plan/ — the file exists under content/blog/ but is draft:1 in .squad/content-metrics.json (its live twin, 10-fixed-vs-variable-utility-rate.md, is draft:0, verified this run). On the production site this is a 404-class journey break on the page with the most to lose. First edit to ship.

### P1 — degrades satisfaction
- **P1-1 · The engagement peak is link-dead [CONTENT].** After Why bills jump, the page’s most-read zone — 7 FAQs, the Charge Categories table (its signature asset), Questions to Ask About a Line Item — holds **zero** onward links. The last rendered exit is the meter link in Estimated readings; everything after is a cul-de-sac.
- **P1-2 · Quick Answer citation clutter [CONTENT].** Three EIA vintages plus verify-the-release meta inside the answer sentence (§2). Tighten by placement, not by touching verified facts.
- **P1-3 · The category map withholds its own depth [CONTENT].** Charge Categories You May See lists seven rows; five have dedicated live pages (customer charge → 17; fuel/purchased-power adjustment → 18; riders/program charges → 19; delivery-vs-supply split → 24; demand charge → 49) — none linked from the table zone. The page teaches categories, then withholds the explainers it has.
- **P1-4 · No Related Reading block [CONTENT].** House convention places a curated bulleted Related Reading before the FAQ (exemplar: what-is-ccf-on-a-water-bill.md); this page has none.

### P2 — polish
- **P2-1 [CONTENT]** Start here’s billing-period-days bullet is unlinked although 23-utility-billing-cycle-explained covers exactly it.
- **P2-2 [CONTENT]** FAQ answers cite sources but never exit onward — the Q&A closes the reader’s path as written.
- **P2-3 [CONTENT]** Start here spends a long sentence on the 2022 state spread (Hawaii 6,178 / Louisiana 14,774 kWh) right after the national figure — low decode-value detail; candidate for a one-line tighten (rephrase only, figures untouched). Not executed in this plan (see §9, point 5).

## 4. Momentum & Structure

- **Heading usefulness: strong [CONTENT].** The H2 spine (Start here → supply → delivery → fixed → taxes → TOU → estimated → spikes) mirrors the actual order of curiosity; the tail table + questions give declarative scannability.
- **Paragraph bulk: controlled [CONTENT].** Two heavy sentences: the Quick Answer EIA parenthetical and the Con Ed delivery description; both compressible by reflow without fact changes.
- **Repetition: low [CONTENT].** The Why-bills-jump list and FAQ answer 4 overlap slightly — acceptable cross-reinforcement for scanners.
- **Filler: low [CONTENT].** The citation meta inside the answer (§2) is the only bloat-flavored patch.
- **Scannability: 8/10.** Blockquote router, bolded leads, 7 FAQs, category table. Docked for the dead back half (P1-1) and answer-sentence density.

## 5. Information Gain Plan

Useful-only; reuse of verified in-page or verified sibling content. **Zero new factual claims; no padding; the page must stay ≈2,000 words.**

- **IG-1 · Category→explainer mini-map (medium).** Below the Charge Categories table, five one-line exits, one line each, no descriptions: delivery vs supply in depth → 24; the fixed monthly fee → 17; fuel/purchased-power adjustments → 18; riders and program charges → 19; the surprise demand charge → 49. Converts the signature table from a map into a dispatch — the page’s single biggest engagement upgrade.
- **IG-2 · Two follow-up FAQ entries (small),** answerable from on-page verified material: (a) Why does my neighbor pay a different delivery rate? — the rate-schedule/tariff framing already on page + link 24. (b) How do I get a line item formally reviewed? — the page’s own questions-to-ask list + link the dispute guide.
- **IG-3 · Related Reading block (small).** House-convention placement before the FAQ; 4–6 curated entries with one-line descriptions, drawn from §6 (03, 04, 24, 49, which-rate-plan, 23).
- **IG-4 · Escalation pointer (small).** One sentence at the end of Questions to Ask About a Line Item → how-to-dispute-utility-bill (verified). Completes the decode → check → escalate arc.
- **IG-5 · Meta-description proposal (Commander-level only; frontmatter out of scope).** Optional tighten to lead with the four-part decode + the one-line self-check. PROPOSE, do not execute.

## 6. Internal Journey

All targets verified present under content/blog/ and draft:0 in .squad/content-metrics.json (verified this run). Draft:1 pages are excluded everywhere (supply-vs-delivery-charges-electricity, why-electric-bill-changes-month-to-month, how-to-read-your-utility-bill, stormwater, 02/15/41, the 2026 index pages). [CONTENT, verified]

1. **PLACEMENT SWAP (P0-1):** replace the dead /blog/fixed-vs-variable-rate-electricity-plan/ link in the TOU/tiered section with **content/blog/10-fixed-vs-variable-utility-rate.md** (live, draft:0, same topic). Anchor: how to compare fixed and variable rate offers. [CONTENT]
2. **the two big halves of your bill, side by side** → content/blog/24-delivery-charge-vs-supply-charge-utility-bill.md — IG-1 map row (anchor: delivery vs supply, compared line by line). [CONTENT]
3. **why you pay a fixed fee even in an empty house** → content/blog/17-what-is-customer-charge-on-utility-bill.md — end of the Fixed customer charges section. [CONTENT]
4. **what a fuel or purchased-power adjustment is** → content/blog/18-fuel-adjustment-charge-on-utility-bill-explained.md — IG-1 map row (anchor: the pass-through line that moves with fuel costs). [CONTENT]
5. **riders, surcharges, and program lines** → content/blog/19-utility-bill-surcharges-and-riders-explained.md — end of Taxes and other charges. [CONTENT]
6. **when a demand charge appears on a residential bill** → content/blog/49-demand-charges-electricity-bill-explained.md — IG-1 map row (anchor: the demand line). Already linked in the intro blockquote — that stays; this is the deeper placement at the engagement peak. [CONTENT]
7. **how two months with the same usage can bill differently** → content/blog/23-utility-billing-cycle-explained.md — Start here, on the billing-period-days bullet (P2-1). Cross-hub link; ships together with 23’s plan for symmetry. [CONTENT]
8. **how to formally question a charge** → content/blog/how-to-dispute-utility-bill.md — IG-4 closing sentence at Questions to Ask About a Line Item. [CONTENT]

**Alternates considered and parked (do not add in this pass):** 46-what-time-is-electricity-cheapest at the TOU section (08-time-of-use-electricity also fits; one exit is enough — item 1 already repairs TOU routing); 11-understanding-kwh-usage at Start here (the two what-is-a-kilowatt-hour links already serve unit basics). Retained as-is: all existing live links (03, 01, 49, 04, what-is-a-kilowatt-hour, how-to-read-electric-meter). [INFERENCE on verification]

## 7. CTA Fit

**Verdict: NONE — informational.**

- Zero product boxes today; none warranted. [CONTENT + DOCTRINE]
- AFFILIATE-PLACEMENTS-2026-08-28.md places product surfaces on the diagnosis/action pages (03, 06, water pages, 05) and deliberately none on definitional statement-anatomy pages; this page is the definitional hub for electricity. A Kill-A-Watt box here (the temptation) would answer a measurement question the reader has not asked yet; 03 — this page’s onward diagnosis exit — already carries the measurement box in doctrine Tier 1.
- The page’s business job is to send: decode-trust converts into a click into 03 or 04, where product surfaces live and convert honestly. A reader who maps their bill here and then hits the what-drives-the-total diagnostic is the highest-quality arrival 03 will ever get. Protect that flow; do not tax it with chrome.

## 8. Edit Plan

Ordered, section-level, targeted. Sizes: small = ≤1 paragraph or swap; medium = one-zone addition. No wholesale changes; frontmatter and slug untouched (IG-5 is a proposal, not an edit).

1. **[small | TOU/tiered section — P0, SHIP FIRST]** Swap the dead link to content/blog/10-fixed-vs-variable-utility-rate.md (§6 item 1). One-line diff.
2. **[small | Quick Answer — P1-2]** De-clutter the citation sentence: keep the residential annual average and the June 2026 figure in the answer; move the all-customer 13.63¢ figure and the verify-the-release meta into a one-line source note directly under the Tip. No fact added or removed. If the implementer cannot do this without touching sourcing brackets, defer to the Commander — this page’s sourcing was just squared and must not drift.
3. **[medium | after Charge Categories table — P1-1 + P1-3]** Add the IG-1 five-line category→explainer map (24, 17, 18, 19, 49). One line each, no descriptions; the table itself is not reflowed.
4. **[small | Questions to Ask About a Line Item]** Add the IG-4 escalation sentence → how-to-dispute-utility-bill.
5. **[small | Fixed customer charges section]** Add the 17 link.
6. **[small | Start here]** Link the billing-period-days bullet → 23 (P2-1).
7. **[medium | before FAQ — P1-4]** Add the Related Reading block (IG-3; house convention; 4–6 entries, one-line descriptions, exemplar style).
8. **[small | FAQ]** Append the two IG-2 follow-up Q&As inside the existing faq block (no schema restructure).
9. **[Commander-level proposal only]** Meta-description tightening per IG-5 — not part of the implementation diff.

**Sequencing:** 1 immediately (production break), 2 next (first screen), 3–8 gently in one release. Net delta ≈ +120 words — the page holds ≈2,080 words, no bloat. Coordinate the release with 23-billing-cycle so the cross-hub links land together.

## 9. Dual Reasoning + Self-Critique

**Reader test** — *I came here because I need every line on my electric bill explained and checked.* Today: four-part answer in sentence one (excellent), symptom router one tap below (excellent), then a mid-page dead link (P0-1) and a content-rich back half with no roads out (P1-1). After the plan: the broken exit is repaired, the citation wall is lifted off the answer, and every category row — plus the questions list and the FAQs — hands the reader the next page their line item deserves. Protect-then-extend, in that order. [INFERENCE on CONTENT + RYBBIT]

**Business test** — decode-trust converts into a click into the diagnosis page (03), the every-charge map (04), or a line-specific deep-dive (17/18/19/24/49) — where the site’s honest product surfaces already live [DOCTRINE]. The page stays unmonetized: no product answers how-do-I-read-my-bill. NONE — informational, journey-deferral business model.

**What an expert editor would criticize about this plan:**
1. The Quick Answer citation de-clutter (item 2) touches a freshly fact-squared sentence — the highest-risk edit on this page; moving figures verbatim (not merging) must be the implementer’s default.
2. The Charge Categories table is the signature asset; the IG-1 map must sit below it untouched — any temptation to bolt link columns onto the table is refused.
3. Eight journey links on an already-routed page risks exit fatigue; the one-line rule for map rows is load-bearing.
4. FAQ additions take the block to 9 entries; both must be follow-ups, not restatements — item 8 is the first cut if the owner balks.
5. The plan flags the Start-here state-spread sentence (P2-3) but does not touch it — an editor will call that inconsistent; the defense is the no-touch-sourcing posture on a 73%-bounce page: cosmetic provenance trims outside the answer sentence are not worth the diff risk.

**Verification trail (this run):** full single-pass read of the article (file ends at Sources); P0-1 status check — fixed-vs-variable-rate-electricity-plan draft:1, 10-fixed-vs-variable-utility-rate draft:0, both under content/blog/; every §6 target verified via directory listing + metrics draft:0; Rybbit figures are packet-supplied baseline values, not re-derived [RYBBIT].