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
