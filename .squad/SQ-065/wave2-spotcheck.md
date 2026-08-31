# SQ-065 Wave 2 — Independent Spot-Check of FULL-CONTENT-SEO-AUDIT-2026-08-30.md
**Checker:** twin_q (uncorrelated re-derivation; read-only; no wave-1 conclusions taken on faith)
**Date:** 2026-08-30 · **Method:** 10 sampled claims re-derived against `content/` grep, `wave1/*.md`, `evidence-brief.md`, `claims-verification.md`. Every verdict includes the evidence line.

## Verdict counts
**9 CONFIRMED · 1 REFUTED** among the 10 samples; plus 3 faithfulness extras: 2 REFUTED-as-stated, 1 partial-REFUTED. Overall: **FIX** (see end).

## Sampled verdicts

### S1 — C1 blanket claim — CONFIRMED
Report: 05 claims water-heater blankets cut standby loss "~25% per DOE"; DOE caps at 4–9%; three figures across three money pages.
- [OBSERVED] `content/blog/05-how-to-lower-utility-bills.md:89` — `| Water heater insulation wrap (electric) | $20–$40 | $3–$7/mo | <1 year | Reduces standby heat loss ~25% per DOE |`
- [OBSERVED] 07:119 — "cuts standby heat loss by 5–10%.[4]"; guide:438 — "Savings: 4–7% on water heating" → the 3-figure contradiction holds (note: 05 says "wrap," which is why a naive grep for "blanket" misses it — the report's wording is accurate).
- [OBSERVED] claims-verification.md #5 — REFUTED against energy.gov blanket page: "DOE & Energy Star officially cap blanket savings at 4–9%."
- Faithful to artifact AND to claims-verification. No embellishment found.

### S2 — C2 heating-share contradiction on 07 — CONFIRMED
- [OBSERVED] 07:26 (Quick Answer) — "space heating accounts for about 40–50% of household gas use**[1]"; 07:56 (Cause 1) — "Heating accounts for **60–70% of natural gas usage** in a typical home.[1]" — same footnote [1] for both.
- [OBSERVED] claims-verification.md #7 — REFUTED: "EIA RECS consistently splits residential natural gas into space heating (~40–45%)…The 60–70% figure conflates heating sectors."
- Report represents the refutation and the same-source defect exactly.

### S3 — C3 duplicate `sources:` key — CONFIRMED
- [OBSERVED] `grep -n '^sources:' content/blog/how-to-lower-electric-bill-complete-guide.md` → `8:sources:` and `19:sources:`; the two blocks differ (3 bare-URL entries vs 5 quoted EIA/DOE entries) — exactly the non-determinism the report describes.
- Matches lieutenant artifact line 161 ("duplicate sources: key at lines 8 and 19… grep-verified").

### S4 — C4 stacked-savings arithmetic + phantom tables — CONFIRMED
- [OBSERVED] guide checklist totals: :518 "$50–$150/month", :532 "$50–$100/month", :542 "$100–$200/month" → sums to **$200–$450/month**.
- [OBSERVED] guide:66 — same page prices the average bill at "**$164.88/month** — 899 × $0.1834". The 2–3×-bill overpromise is real. (Intro at :46 promises "$50, $100, even $150", making the internal contradiction worse, as the artifact noted.)
- [OBSERVED] console: :129 "| Game console | 15–20 W | $22–$30 |" vs :566 (FAQ) "A game console can save $15–$25/year". Totals: :134 "**$75–$220/year**" vs :467 "**Total phantom load elimination:** $50–$100/year".
- Every number in C4 re-derived from the file. Faithful.

### S5 — C5 unverifiable "verified" table on 28 — CONFIRMED
- [OBSERVED] `28-utility-reconnection-fee-explained.md:65` — "PECO tariff Rule 14, PSE&G tariff sheet 63… (each **verified via state PUC dockets 2024–2026**)" — no URLs or docket numbers attached to the fee table (the page has only 3 unrelated external links).
- [OBSERVED] claims-verification.md #8 — UNVERIFIED ("Without the site's original citation URLs…impossible"). Report reports it as UNVERIFIED, not invented-confidence. Faithful.

### S6 — C6 three dead ends + inbound counts — CONFIRMED
- [OBSERVED] net-metering-explained, ev-charging-impact-electric-bill, water-service-charge-explained: `grep -c '](/'`, `<a href`, `ref ` each = **0 / 0 / 0** per page — zero outbound internal links in any format.
- [OBSERVED] net-metering inbound = **3** (how-utility-rates-fees:35 HTML; which-rate-plan:52 and :63) — report says "3 inbound". ev inbound = **2** (08-time-of-use:57; 03:102) — report says "2 inbound incl. from 03".
- Matches Commander grep-verified finding in evidence-brief.md:50,72.

### S7 — C7 render breakage — CONFIRMED
- [OBSERVED] aux-heat:68 — `<h2 id="the-problem">The problem: \</h2>` (truncated mid-sentence); :145 — `<h2 id="emergency-heat">What Emergency Heat means (and when it</h2>`. Both render broken headings.
- [OBSERVED] gas-vs-electric-heating-cost-comparison.md:21 — `[For more detail, see our guide to [heat pump savings](/blog/48-heat-pump-vs-gas-furnace-savings/).]` — the malformed nested link, exactly as described.

### S8 — C8 07 count/payback contradictions — CONFIRMED
- [OBSERVED] title (07:1): "Why Is My Gas Bill So High? **10** Causes and Fixes"; body headings: `### 1.` (07:54) through `### 11.` (07:173) — 11 numbered causes.
- [OBSERVED] payback trio: 07:99 "payback in 5–8 years"; 07:263 "| New 96% AFUE furnace… | 3–8 years |"; 07:270 "payback: ~23 years (gas-only savings)".
- [OBSERVED] uncited claim: 07:125 "many U.S. utilities have increased rates 15–30% year-over-year (U.S. EIA, 2026)" — no matching sources entry; matches artifact defect (4).
- Master-table row (6·7, "3,892w, 29 ilinks, 10 FAQs") matches lieutenant-pages.md:114–116 (Quality 6/10, SEO 7/10; "3,892 words; 29 internal links; 10 FAQs"). [GAP] — raw-word method differs from artifact method (my `wc -w` = 4,254 incl. frontmatter/links); artifact method accepted as the convention; not a defect.

### S9 — 3E master-table row for mcf-vs-ccf-vs-therms — **REFUTED** (stale metrics flag; prescribed fix already done)
Report row: "mcf-vs-ccf-vs-therms-on-gas-bill | Gas unit explainer (3,060w) | 8·4 | **ORPHAN**: link from gas hub + 12 + what-is-ccf (unit bridge)".
- [OBSERVED] word count and 8·4 rating match artifact B22 — those parts are fine.
- [OBSERVED] **Repo ground truth: 7 inbound link instances from 5 files** — gas-explained.md:232 (the gas hub itself), 12-how-to-read-your-gas-bill.md:140, 07-gas-bill-too-high.md:28 and :295 (markdown), utilities-glossary.md:96 and :100, how-to-read-gas-meter.md:153 (HTML).
- [OBSERVED] Two of the three recommended link sources **already link it**: artifact B22's action — "link from /gas-explained/, /blog/12-how-to-read-your-gas-bill/, /blog/what-is-ccf-on-a-water-bill/" — and the report's "gas hub + 12" are existing edges. Only the what-is-ccf cross-link is genuinely missing.
- [OBSERVED] Defect chain: artifact B22 said "ORPHAN (metrics: 0 il)… only 4 raw"; artifact Part C Cluster 4 tags mcf "(O, 4)" under its own rule "**O** = orphan concern (≤2 inbound)" — the artifact violated its own ≤2 rule, and the report laundered the stale flag into an ORPHAN row without re-checking, **in direct violation of the report's own §0 caveat**: "any other '0 ilinks/0 h2' flag must be re-checked before citing."
- Verdict: REFUTED as stated. The SEO-4 context and the bridge-link suggestion partly survive; the ORPHAN label and the "link from gas hub + 12" action are wrong against the repo.

### S10 — Checklist item #13 (§7 line 294) — REFUTED-as-stated (component defect)
Item: "Rebuild legacy cohort: afue (matrix + sources, **drop 4-link sentences**), aux-heat, heat-pump-running."
- [OBSERVED] afue components CONFIRMED: mason artifact lines 79–85 (single DOE source, no tables, 1/0-h2 flag FALSE due to HTML) → "matrix + sources" is sound; aux-heat render-bug component CONFIRMED (see S7).
- [OBSERVED] **"4-link sentences" / "Pattern C — up to 4 internal links in a single sentence (afue)" is false against the page.** afue's internal content anchors: :117 (aux-heat), :136 (duct leaks), :147+:149 ("these guides help: [winter] and [summer]." = 2 links in that sentence), :156 (gas-vs-electric) — across three separate `<p>` blocks. Densest single sentence = **2** links, not 4. The four links twinq named (duct/winter/summer/gas-vs-electric, twinq-verdict.md:29) span ≥2 subsections, not one sentence. The report hardened twinq's [OBSERVED]/[INFERENCE] mix into a quantified sitewide "Pattern" without the re-check §0 promises.
- Verdict: the declutter intent survives (6 body links across 2 sections is still link-dense), but the stated observable is wrong. REFUTED as quantified.

## Master-row bonus checks (mission asked for 3 rows — S9 above plus these two)
- **49-demand-charges row (7·7; "fix duplicate source line") — CONFIRMED.** [OBSERVED] sources block lines 14–17 contain the identical energy.gov/cmei/femp/evaluating-your-utility-rate-options URL twice; prospector artifact :216–220 rates 7/7 and flags "the same DOE URL twice".
- **afue row (7·6; comparison page, zero tables, rebuild matrix + 2+ sources) — CONFIRMED.** [OBSERVED] matches mason artifact :79–85 ("7/10 | 6/10… no tables despite being a comparison page… only a single DOE source").

## Rewrite-brief fidelity check (8.1 — 07)
**CONFIRMED faithful.** Every element of the brief re-derives: refuted 60–70% (07:56 ✓), 10-vs-11 (title vs ### 11 ✓), payback trio 5–8/3–8/~23y (07:99/263/270 ✓), "two mislabeled and two duplicated sources" ≈ artifact (5) (entry-3 label wrong; 2/4 duplicated ✓), uncited EIA claim (:125 ✓), WNA-paragraph duplication (artifact ai_slop bullet ✓), 29-link web (artifact ✓), source-[3] relabel + dedupe 2/4 (artifact ✓). [OBSERVED] 8.1's "route therm/CCF readers to mcf-vs-ccf (its orphan sibling)" repeats the S9 stale-orphan framing — same cure: drop "orphan", keep the link.

## C10 pre-condition check (twinq Gap-2 laundering) — PARTIALLY REFUTED
Report C10: "Missing safety/financial disclaimers on pages advising panel-opening (47), capacitor testing (13), and variable-rate commitments (which-rate-plan)."
- [OBSERVED] **47 does not mention "panel" at all** (grep count = 0); it recommends a non-contact thermal-camera look at "a hot spot on a breaker" (:67), and already carries DIY-limit warnings (:27 "not a substitute for safe electrical…work"; :81 "Do not…work on energized electrical components"). "Advising panel-opening" has no repo support — this is twinq Gap 2's [OBSERVED] tag laundered through, and twinq's own tag was [INFERENCE]-adjacent.
- [OBSERVED] **13 advises AGAINST capacitor testing**: :67 "None — capacitors hold a charge and high-voltage testing is not a homeowner task"; :82 "Do not add refrigerant, work on wiring or capacitors…"; :50 assigns the test to "technician with meter". "Add a capacitor-testing disclaimer" prescribes what the page already does.
- [OBSERVED] The which-rate-plan third is CONFIRMED: zero disclaimer/safety wording (grep = 0) plus "gamble on **variable**" (:23) — that part of C10 stands.

## Faithfulness judgment (report vs wave-1 evidence)
- **Where it matters, the report is faithful.** All 8 load-bearing critical-issue samples re-derive exactly against the repo and claims-verification (C1–C8: quotes, line-level defects, arithmetic, link counts, inbound counts all match). Claims verdicts (#5, #7 REFUTED; #8 UNVERIFIED; #1/#9 OPEN-as-unverifiable) are carried at the right strength — the report does not inflate the UNVERIFIED items. Master-table rows checked match their per-seat artifacts, including provenance notes (twin_q 4th-weakest → average-utility-bills-by-state, twinq:81 ✓; 05's air-sealing mis-cite, 05:85 ✓; batch fingerprint: exactly 14 posts carry date: 2025-12-25 ✓; byline concentration 43 of 89 posts ✓ (90th blog file is `_index.md`); terms' missing place-of-business, terms.md:80–83 ✓; apex hub links no act pages ✓; electricity hub links neither net-metering nor ev-charging ✓).
- **Where it fails its own standard, it fails in a specific way: inheritance without re-check.** Three defects share one root cause — claims originated in twinq/prospector artifacts (some tagged [INFERENCE] there) and entered the final report as flat facts: (1) mcf ORPHAN row + no-op fix (S9); (2) Pattern C "4 links in a single sentence" (S10); (3) C10's "panel-opening (47) / capacitor testing (13)" premises. The report's §0 explicitly sets a re-check rule for exactly this class of stale metrics/secondhand flags, then violates it three times. None of the three is load-bearing for the audit's headline verdicts; all three misdirect fix-work (two prescribe edits that are already done).
- [INFERENCE] The two real REFUTEDs are concentration-bound: every defect traces to the twin_q artifact (Pattern C, Gap 2) or the metrics tool (0-ilinks flags), not to the lieutenant/prospector/mason/cartographer seams. The lieutenant→C1–C4 chain is the cleanest part of the report.
- [GAP] Per-page stat conventions (word/ilink counting) vary between artifact method and raw wc/grep; I accepted artifact numbers where the report cites them. A one-line methods note in §0 would close this.

## Overall verdict: **FIX**
The report's load-bearing spine (C1–C8, refuted-claims adjudication, priority ordering, the 8.1 brief) survived full independent re-derivation — 9 of 10 samples CONFIRMED with line-level evidence. But it ships three citable defects of the exact class its own §0 forbids (stale ORPHAN row with a partially no-op fix; a quantified Pattern that a body read of the page disproves; a C10 restate of twinq's Gap 2 whose 47/13 premises are false against the pages, while the which-rate-plan premise is true), plus one stale "orphan sibling" clause inside 8.1 and the same-orphan clause for water-service-charge's "link from water hub" (hub already links it, water-explained.md:259 — though water-service's dead-end core stands, per Commander grep). Patch pass required — smaller than a §4 rewrite: (1) correct the mcf row and water-service-charge "orphan" clauses to name the genuinely-missing edges only (mcf←what-is-ccf remains real); (2) re-quantify Pattern C ("6 links across 2 subsections") or drop the quantifier; (3) re-premise C10 to which-rate-plan + generalized missing-disclaimer check; (4) drop "orphan" wording from 8.1. Not APPROVE (it violates its own verification discipline in citable rows the operator will act on); not REJECT (the deliverable's evidence spine is real and precisely traceable).

— twin_q, wave-2 spot-check, 2026-08-30. All greps run on `content/` and `.squad/SQ-065/wave1/` this run; no files under judgment were modified.
