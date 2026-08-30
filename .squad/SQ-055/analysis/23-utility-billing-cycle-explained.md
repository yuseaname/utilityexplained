# APEX Reader-Experience Analysis — 23-utility-billing-cycle-explained

## Execution Log (implemented by lieutenant, wave 2, 2026-08-29)

- Applied item 1: merged the duplicate second link paragraph into the single **Next step** paragraph (01, 12, breakdown retained once; unique 03 link folded in).
- Applied item 2: one-sentence routine-shifts reassurance added after the bolded Quick Answer (uses the page's own 1–3 day / 27–35 day figures).
- Applied items 3 + IG-1: proration sentence + link (20) after the worked example. Applied item 5 + IG-4: Compare section reflowed to 4 bullets, minimum-bill link (22), plug-in-your-numbers mini-template under the formula.
- Applied item 4: estimated-reads (14) + estimate-correction-spike (30-sudden-spike) links at the end of the estimated-reads action paragraph.
- Applied item 6: new H2 "Is this normal, or worth a second look?" — 6-row normal/second-look gate built only from figures already on page (27–35, 1–3, 3–6, estimate correction, flat-average, duplicate/credit cases).
- Applied item 7: dispute-guide sentence at the end of Questions for the Provider (also linked in FAQ item d, mirroring the electric page's FAQ-exit pattern).
- Applied item 8: FAQ block (4 Q&As, all follow-ups built from on-page material) + one faq-schema, after content, before Sources. Applied item 9: breakdown charge-map link added at the end of Record the Statement Details.
- Skipped: none — all items 1–9 approved as written and executed. No NEEDS-VERIFICATION items on this page; frontmatter untouched (`updated: 2026-08-29` already set).

**File:** content/blog/23-utility-billing-cycle-explained.md · 1,254 words · 9 H2 / 6 H3 · 8 tables · 8 internal links · 0 FAQ · 0 product boxes · updated 2026-08-29
**Traffic (Rybbit baseline 2026-07-30 → 08-29, pre-change):** 59 visits · 65 pv · TOP 55.7s · bounce 83% [RYBBIT]
**Analyst:** lieutenant, planning wave SQ-055. Analysis only — an implementation wave executes Edit Plans after Commander review.

---

## 1. Intent Model

**Primary intent [CONTENT][RYBBIT]:** the reader noticed their bill covers a date range that does not match the calendar month — or two consecutive bills differ in length or amount — and wants to know why, and whether the bill is wrong. Evidence: title, Quick Answer, and Why Cycle Lengths Vary answer exactly this; sessions are short and question-driven.

**Secondary intent [CONTENT]:** compare two bills fairly — served by the Long-vs-Short-Month Bill Math worked example and Compare Bills Like With Like.

**Desired outcome [CONTENT]:** the reader can locate the service dates and read status on their own statement, compute average daily usage, and conclude confidently that the difference is a period artifact, not a usage change.

**Next logical need [INFERENCE]:** what is actually on the rest of this statement (line-item decoding), and — if something still looks wrong — how to get it reviewed. Maps to the bill-reading, breakdown, estimate, and dispute pages.

**Journey note [RYBBIT]:** 83% bounce with healthy 55.7s TOP = readers get the answer and leave; the page offers no visible road onward (all 8 links sit in the intro; the body has none — see §6).

## 2. First-Screen Verdict

Mobile (56% of traffic [RYBBIT]) sees: hero, title, Quick Answer. [CONTENT]

- **Verdict: PASS, with friction.** The direct answer — the billing period is the service-date range printed on the statement, not necessarily a calendar month — is reachable in two sentences. [CONTENT]
- **Friction:** immediately after, five conditional instructions (dates, day count, read status, unit, tariff version) arrive before any reassurance. [CONTENT]
- **Likely this-isn’t-for-me moment [INFERENCE on CONTENT]:** the Quick Answer’s example is Con Edison; nearly every visitor is not a Con Ed customer and meets a someone-else’s-utility reference before the general explanation arrives in Why Cycle Lengths Vary.
- **Redundancy cost [CONTENT]:** two consecutive link paragraphs under the Quick Answer link the same three targets twice (01, 12, electric-bill-breakdown) — ~60 words of the first screen is duplicate navigation.

## 3. Gap Analysis

### P0 — kills satisfaction
- **P0-1 · Body-link vacuum plus duplicated intro links [CONTENT].** All 8 internal links live in the first two paragraphs; the ~1,000-word body (The Long-vs-Short-Month Bill Math; Estimated-vs-Actual Read Interaction; How to Check Your Cycle Dates; Record the Statement Details; Compare Bills Like With Like; Questions for the Provider) contains **zero** links. The reader’s moment of maximum momentum has no exit — the mechanical explanation of reads-then-leaves [RYBBIT: 83% bounce at 55.7s TOP].
- **P0-2 · No escalation path at the suspicion peak [CONTENT].** The article ends with a five-question script and no link to the bill-review guide; the estimated-read section stops at Con Ed self-read instructions. The reader who leaves *unsure* has nowhere to go.

### P1 — degrades satisfaction
- **P1-1 · No normalization moment [CONTENT].** Reassurance exists only as scattered figures (27–35 days in Meter-Read Schedules; 1–3 day shifts; 3–6 day seasonal drift). No plain statement that this is routine.
- **P1-2 · Procedural tables on mobile [CONTENT].** How to Check Your Cycle Dates and Record the Statement Details are 4–6-row, two-column tables with long cells — walls on 56% mobile; bullets would scan faster (reflow, not new content).
- **P1-3 · FAQ absent [CONTENT].** House pattern (exemplar what-is-ccf-on-a-water-bill.md) closes with faq + faq-schema; this page has none — it forgoes compact follow-ups and the FAQ-rich-result treatment the cluster uses.

### P2 — polish
- **P2-1 [CONTENT]** Con Ed example in Quick Answer; half a sentence generalizes it.
- **P2-2 [CONTENT]** Seasonal Scheduling + Utility-Specific Cycle Days (~90 words) could merge; optional, current length is not a problem.
- **P2-3 [CONTENT]** Formula exists; no plug-in-your-own-numbers mini-skeleton after the worked example.

## 4. Momentum & Structure

- **Heading usefulness: strong [CONTENT].** The 9 H2s trace the reader’s decision tree; navigable by headings alone.
- **Paragraph bulk: fine, two soft spots [CONTENT].** The dense qualification chain in Compare Bills Like With Like; the instruction-sentence in the Quick Answer.
- **Repetition: one real case [CONTENT]** — the duplicated link paragraphs (P0-1). The repeated period-vs-calendar restatement is reinforcement, not filler.
- **Filler: low [CONTENT].** No padded intros; the EIA context sentence does legitimate work.
- **Scannability: 7/10.** Heading skeleton and 8 tables give good grab-points; link-dead body, mobile-unfriendly procedural tables, and doubled first-screen paragraphs drag. Consistent with 55.7s TOP / 83% bounce [RYBBIT]: answer, then gone.

## 5. Information Gain Plan

Useful-only; every item reuses verified in-page or verified sibling-page content. **Zero new factual claims; no padding.**

- **IG-1 · First-bill caveat (small).** One sentence after the worked example: move-in/move-out bills are often partial periods. The mechanics live on the proration page (verified target) — link, do not re-teach.
- **IG-2 · FAQ block (small).** Four Q&As built strictly from in-page verified material: (a) Can my billing date change? — yes; the weekend/holiday and seasonal sections already say so. (b) Why do two bills have different day counts? — the worked-example logic. (c) How do I know if my bill was estimated? — the page’s own wording/asterisk check. (d) What if the math still looks wrong? — the escalation route (IG-5). Plus faq-schema per house pattern.
- **IG-3 · Normal-vs-second-look table (medium).** Reorganize existing on-page statements into one scannable gate. Normal: 27–35 day periods; 1–3 day weekend shifts; 3–6 day seasonal drift; estimated-then-corrected lumps. Second look: totals diverge while the verified daily average is flat; duplicated charge lines; a correction that never lands. Fixes the scattered-reassurance problem (P1-1).
- **IG-4 · Plug-in-your-own-numbers mini-template (small).** Three lines under the existing formula: your kWh ÷ your days = your daily average; repeat for a second bill; compare.
- **IG-5 · Escalation pointer (small).** One sentence after the provider questions, linking the bill-review guide (verified target).

## 6. Internal Journey

All targets verified present under content/blog/ and draft:0 in .squad/content-metrics.json (verified this run). Draft:1 pages (stormwater-fee…, 15-why-utility-bill-higher…, why-electric-bill-changes…, supply-vs-delivery…, how-to-read-your-utility-bill, gas-customer-charge…, 02-average-utility-costs…, 41-…, the 2026 by-state/index pages) are excluded as journey targets. [CONTENT, verified]

1. **estimate correction lands on a later bill** → content/blog/30-sudden-spike-in-electricity-bill-no-usage.md — end of How Estimated Reads Affect Your Bill. Serves the reader whose lumpy bill is a live spike. [CONTENT]
2. **how to request a billing review** → content/blog/how-to-dispute-utility-bill.md — end of Questions for the Provider. Completes the page’s own arc (P0-2). [CONTENT]
3. **how partial periods on first or final bills are prorated** → content/blog/20-utility-bill-proration-explained.md — after the worked example (IG-1). Serves the move-in variant of this exact question. [CONTENT]
4. **why your bill changed when usage looks the same** → content/blog/03-why-is-my-electric-bill-so-high.md — keep, but inside the merged single Next-step paragraph (dedupe). [CONTENT]
5. **how estimated reads and true-ups work** → content/blog/14-estimated-utility-bill-explained.md — Estimated-vs-Actual section, beside #1; the dedicated deep-dive the current section lacks. [CONTENT]
6. **when a minimum charge keeps your bill from dropping** → content/blog/22-minimum-bill-utility-bill-explained.md — Compare Bills Like With Like; the comparison-minded reader’s next question. [CONTENT]
7. **Retained:** 01-how-to-read-your-electric-bill.md, 12-how-to-read-your-gas-bill.md, electric-bill-breakdown-understanding-line-items.md — already linked at top; keep merged, and add the breakdown link at the end of Record the Statement Details so the charge map is reachable from the body, not only the top. [CONTENT]

**Rejected:** what-is-ccf-on-a-water-bill.md (water-unit framing dilutes an electric/gas-example page); all draft:1 candidates above. [INFERENCE on verification]

## 7. CTA Fit

**Verdict: NONE — informational.**

- AFFILIATE-PLACEMENTS-2026-08-28.md lists 23-billing-cycle verbatim under NOT A FIT — deliberately unmonetized: *Definitional. No product answers the question; a box here is decoration.* [DOCTRINE, quoted]
- The page currently carries zero product boxes or affiliate links (full read + metrics agree). [CONTENT]
- The reader is mid-verification of a billing question; no product answers it. The business value is the handoff into the breakdown/troubleshooting pages, where the site’s honest product surfaces live. A box here would trade this page’s whole asset — trust — for decoration: the doctrine’s exact warning.

## 8. Edit Plan

Ordered, section-level, targeted. Sizes: small = ≤1 paragraph; medium = one-section restructure. No wholesale changes; frontmatter/slug untouched (constraint).

1. **[small | Quick Answer]** Delete the duplicated second link paragraph; fold its unique link (03) into the single Next-step paragraph. Fixes P0-1’s duplication; tightens the first screen.
2. **[small | Quick Answer]** Add one reassurance sentence after the bolded answer (weekend/holiday shifts and 27–35-day periods are routine, per Meter-Read Schedules). Mitigates the instruction-wall reaction (§2).
3. **[small | The Long-vs-Short-Month Bill Math]** Add proration link (#3) + the IG-1 sentence after the worked example.
4. **[small | Estimated-vs-Actual Read Interaction]** Add links #1 and #5 at the end of the action paragraph. Serves P0-2’s first half.
5. **[medium | Compare Bills Like With Like]** Break the dense qualification chain into 3–4 bullets (reflow only); add link #6; append the IG-4 mini-template. Fixes P1-2 + P2-3.
6. **[medium | new H2 Is this normal, or worth a second look? — placed before Questions for the Provider]** Add the IG-3 table from existing verified statements. Fixes P1-1. Keep it one screen tall.
7. **[small | Questions for the Provider]** Add link #2 (IG-5). Completes P0-2.
8. **[medium | end of article, before Sources]** Add the IG-2 FAQ block + faq-schema, per house pattern. Fixes P1-3.
9. **[small | Record the Statement Details]** Add the body link to electric-bill-breakdown (#7).

**Sequencing:** 1–2 first screen → 3–7 body → 8 close. Each item independently shippable. Optional Commander-level note (not in this diff): the meta description could later gain a why-is-my-bill-longer-this-month phrasing.

## 9. Dual Reasoning + Self-Critique

**Reader test** — *I came here because I need to know why my bill’s dates look wrong, and whether I’m being billed unfairly.* Today: fast answer (two sentences), then tables, then a stranded ending — good content, dead end [CONTENT]. After the plan: reassurance lands on the first screen, the reader verifies with their own numbers (IG-4), a normal-vs-second-look gate settles the fear (IG-3), and a genuinely unsettled reader gets a scripted escalation (IG-5). Satisfied readers feel satisfied sooner; worried readers land somewhere. [INFERENCE on CONTENT + RYBBIT]

**Business test** — trust here converts into deeper statement understanding, not purchases; the doctrine itself names this page NOT A FIT [DOCTRINE]. The business win is a clean handoff into breakdown/troubleshooting pages where honest product placement exists. NONE — informational is the doctrine-correct verdict, not a hedge.

**What an expert editor would criticize about this plan:**
1. IG-3 risks duplicating Estimated-vs-Actual two scrolls up; it must categorize, not restate — cap at one screen.
2. Seven placements could over-juice section seams; the implementer must not put links inside table rows.
3. IG-2 FAQs must be follow-up questions, not Quick-Answer restatements; the plan says so, the wave must hold the line.
4. Additions total ≈ +250 words; if the owner wants less, cut in this order: item 6 / IG-3, then IG-4.
5. Con Ed-heavy sourcing on generic mechanics was left untouched (out of scope after the SQ-051..054 fact sweep); flagged for any future sourcing-diversification wave.