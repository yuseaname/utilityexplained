# SQ-069 — Audit Remediation Plan & Tracker

**Source:** FULL-CONTENT-SEO-AUDIT-2026-08-29.md (SQ-068) · **Commander:** ZCode
**Started:** 2026-08-30 · **Method:** squad waves (executor/lieutenant/mason/twin_q/verifier) + Commander image generation (Magica `gpt-image-2-text`, quality=medium)
**Rule:** tick a box only after Commander disk-verification. Every phase ends with a git commit.
**Closed:** 2026-08-30 — all 5 phases complete. Final commits: 7c047188 (P2), 001505de (P1), 2902618f (P3), 8af05b4b+6c43449a (P4), 438775ab (P5).

---

## PHASE 1 — Immediate fixes (criticals) — *squad wave 1*
- [x] P1.1 **C1 Image-Prompts leak**: delete `## Image Prompts` section from `content/blog/moving-utilities-checklist.md` (~line 152) — *(executor)*
- [x] P1.2 **C5 drafts**: `git rm` `supply-vs-delivery-charges-electricity.md` + `gas-customer-charge-explained.md`; move `2026-utility-cost-index-by-state.md` out of `content/` to `.squad/archive/` — *(executor)*
- [x] P1.3 **C4 page-46 Con Ed correction**: replace 22.33¢/44.97¢ with live 27.86/17.11/5.22¢ (+delivery 16.402¢, $21 customer charge), fix "50% discount" → ~81%/70%, add retrieval date 2026-08-29 — *(lieutenant)*
- [x] P1.4 **Homepage title tag**: `layouts/partials/head.html:34` — keyword title for `.IsHome` — *(lieutenant)*
- [x] P1.5 **Dead citation**: swap LIHEAP page's dead `acf.hhs.gov/ocs/programs/liheap` URL for a live equivalent, dated — *(executor)*
- [x] P1.6 **C7 eight uncited claims**: source-or-soften in `average-utility-bills-by-state-2026:126` ×2, `07-gas-bill-too-high:160-161` ×2, `44-how-to-lower-water-bill:104-107` ×3, `05-how-to-lower-utility-bills:85` ×1 — *(mason + web)*
- [x] P1.V Commander verification + `hugo` build + **commit `fix: SQ-069 phase 1 — critical fixes`**

## PHASE 2 — Image generation (Magica, gpt-image-2-text @ medium) — *Commander*
Cost discipline: ~13 images × ~0.042 cr ≈ 0.55 cr total. Balance checked first. All 16:9 `2048x1152`, png → webp, saved to `static/images/articles/<slug>/`.
- [x] P2.1 Balance check ≥ 1 credit
- [x] P2.2 moving-timeline-belt (replaces leaked prompt 1) → moving-utilities-checklist
- [x] P2.3 moving-overlap-cost (replaces leaked prompt 2) → moving-utilities-checklist
- [x] P2.4 annotated-sample-bill → shared (04-hidden-fees + flagship)
- [x] P2.5 delivery-vs-supply-split → 24-delivery
- [x] P2.6 tou-24h-price-curve → 08-time-of-use + 46
- [x] P2.7 demand-15min-curve → 49-demand-charges
- [x] P2.8 duct-leak-diagram → duct-leaks
- [x] P2.9 drought-stage-ladder → drought-surcharge
- [x] P2.10 thermostat-auto-vs-fan → furnace-cold-air
- [x] P2.11 meter-leak-indicator → water-meter-leak-indicator
- [x] P2.12 house-leak-cross-section → 47-check-energy-leaks
- [x] P2.13 billing-cycle-timeline → 23-billing-cycle
- [x] P2.V All images downloaded, webp-converted, visually checked by Commander (read_image) + **commit**

## PHASE 3 — Brief rebuilds (5 pages) — *squad wave 2* (embed Phase-2 images)
- [x] P3.1 **Brief 5** `complete-guide-understanding-utility-bill` flagship rebuild (title realign, annotated bill, worked $164.84 example, FAQ schema; fold in `how-to-read-your-utility-bill` draft bones then `git rm` draft) — *(lieutenant)*
- [x] P3.2 **Brief 1** `24-delivery-charge-vs-supply-charge` rebuild (3+-utility verified table, worked split, FAQ) — *(lieutenant #2)*
- [x] P3.3 **Brief 2** `duct-leaks-symptoms` rebuild (symptom list, DIY checklist, runtime math table) — *(mason)*
- [x] P3.4 **Brief 3** `drought-surcharge` rebuild (named-utility drought-rate table, before/after delta) — *(mason)*
- [x] P3.5 **Brief 4** `furnace-cold-air` spine-preserving rebuild (15-min check table, cost bands, 25C-ended note) — *(mason)*
- [x] P3.V Commander verification + build + **commit `feat: SQ-069 phase 3 — five brief-driven rebuilds`**

## PHASE 4 — Bulk & trust layer — *squad wave 3*
- [x] P4.1 **Alt-text template fix**: card-image alt = guide title in layouts (kills all 252) — *(executor)*
- [x] P4.2 **Title trims**: worst ~30 front-matter titles >60 chars — *(mason)*
- [x] P4.3 **Author pages ×5**: one concrete example guide + one real cited source per desk — *(mason)*
- [x] P4.4 **terms.md modernization** (disputes, jurisdiction, commercial terms, date sync) — *(lieutenant)*
- [x] P4.5 **Corrections log**: first two entries (SQ-067 DOE-link fix; page-46 Con Ed correction) on corrections.md — *(lieutenant)*
- [x] P4.6 **Hub byline/updated template line** + electricity-hub duplicate-anchor dedupe — *(executor)*
- [x] P4.7 **Nits**: Hawaii FAQ $453/$324; flagship $144/$165; 07-gas duplicate source entries; glossary linkification; ccf-calculator links — *(mason)*
- [x] P4.8 **Retrieval-date backfill** batch 1 (top 15: YMYL + flagship pages) — *(mason + web)*
- [x] P4.9 **Retrieval-date backfill** batch 2 (next 15) — *(mason + web)*
- [x] P4.10 **Retrieval-date backfill** batch 3 (remaining ~14) + sources for 4 sourceless posts — *(mason + web)*
- [x] P4.V Commander verification + build + **commit**

## PHASE 5 — Verification & close — *squad wave 4 (uncorrelated)*
- [x] P5.1 twin_q verdict on the 5 rebuilt pages (fresh-eyes quality bar)
- [x] P5.2 verifier re-derivation of NEW numeric claims (tariff tables in briefs 1/3, TOU figures, cost bands)
- [x] P5.3 Full `hugo` build + internal-link sweep + sitemap sanity (deletions → aliases resolve)
- [x] P5.4 Image presence + alt audit on touched pages
- [x] P5.5 Tracker closed, mission blackboard closed, **final commit** + user report

---
**Budget log:** (fill as spent) · **Blockers:** (fill if any)

## PHASE 6 — Gap-closure (post-completion review vs audit §2–§9) — *added 2026-08-30*
Review found 11 items the P1-P5 plan missed. Closing them.
- [x] P6.1 how-to-lower-electric-complete: $144/$165 → canonical 18.34¢ × 899 = $164.88 anchor *(Commander)*
- [x] P6.2 water hub → ccf-calculator + what-is-ccf links from units section *(Commander)*
- [x] P6.3 13-ac ⇄ furnace cross-link *(Commander)*
- [x] P6.4 in-links to how-to-lower-electric-complete from 03, 30-spike, phantom-power, smart-plugs *(Commander)*
- [x] P6.5 electricity hub Quick Answer block (audit §3.3) *(Commander)*
- [x] P6.6 disclaimer effective-date reconciliation *(Commander)*
- [x] P6.7 gas hub $1.50/therm anchored to EIA ~$1.91 *(Commander)*
- [x] P6.8 net-metering expand: dollar figures + CA NBT example *(mason, running)*
- [x] P6.9 10-fixed-vs-variable expand: worked comparison *(mason, running)*
- [x] P6.10 dispute-page FAQ schema + 30-spike steps 11-12 compress *(lieutenant, running)*
- [x] P6.V verify + build + commit
**Refuted on review:** homepage 84/85 count drift (no such text in rendered HTML); aria-label duplicates (none); audit's "112 titles >60" (actual: 30 found, 29 trimmed, 1 intentional); Hawaii $453/$324 (intentionally dual-labeled in 3 places); ItemList/calculators/high-bill-block were 'Build Over Time' by design — deferred, listed below.
**Deferred (Build-Over-Time tier, by design):** heat-pump calculator (48), LIHEAP eligibility checker, 'diagnose your high bill' hub block, ItemList schema on hub cards, title-length template enforcement, KPI re-baseline.

## PHASE 7 — Register completion (improve-12 tier) — *added 2026-08-30, post coverage review*
User asked whether coverage was 100%. Finding: mechanical sweeps hit 100% of pages; deep work hit all rewrite/expand/flagged pages; the register's improve-12 tier was ~5/12 done. Closing the rest.
- [x] P7.0 08-time-of-use: tou-24h-price-curve embedded (visual plan said 08+46; worked-example table already existed) *(Commander)*
- [x] P7.1 03 deepen causes + cut filler; 04 tighten 10-15%; 13 decision table *(mason A, running)*
- [x] P7.2 14 actual-vs-estimated table; 27 connection/reconnection comparison + bidirectional links; 05 link-differentiate vs 44/50 *(mason B, running)*
- [x] P7.3 without-solar reduce duplicate blocks; why-did-go-up tighten w/ specific causes *(lieutenant, running)*
- [x] P7.V verify + build + commit + deploy
Already satisfied pre-P7: 49 (worked demand visuals), 27 pairing links, summer/winter water QAs, 05 claims sourcing (P1.6).
