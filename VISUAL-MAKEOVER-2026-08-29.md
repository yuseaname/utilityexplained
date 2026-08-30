# SQ-058 — Visual Makeover Plan & Queue Clearance → CODEX HANDOFF
**Date:** 2026-08-29 · **Site:** utilityexplained.com · **Scope:** the 10 SQ-057 pages (ranks 21-30 tier) · **Base commit:** 276c4363 (plus this mission's queue-clearance edits)
**Execution split:** THIS REPORT is the brief. **Codex generates every NEW image and wires all placements** per the per-page plans + wiring contract. Hero/metadata changes it may make are exactly those named REPLACE in the plans.

## A. Queue clearance — all 3 items DONE (this mission)

### A1. Hub inbound-links — SHIPPED (mason, verified)
The SQ-057 hubs are now linked-in. 13 source pages audited: 4 needed links (tiered-water-rates → why-did-water; supply-vs-delivery → 49-demand; 28-reconnection → 26-deposit; 11-kwh → 01), 9 already carried theirs (grep-verified, skip-logged). All contextual placements, frontmatter `updated:` only.
- **Bonus fix (Commander):** `supply-vs-delivery-charges-electricity.md` carried a live 404 — `/blog/demand-charge-electricity-bill-explained/` (wrong slug) → fixed to `/blog/49-demand-charges-electricity-bill-explained/`. Site-wide grep: 0 wrong-slug occurrences remain.
- Verified: `hugo` EXIT 0; all rendered hrefs on the 13 source pages resolve (mason's anchor links to 08-TOU section IDs confirmed present in rendered HTML); mason's diff facts-frozen (links only).

### A2. Suspect metrics — ADJUDICATED: tracking regression, not reader behavior (executor, data-backed)
Full report: `.squad/SQ-058/rybbit-suspect-check.md`. Verdict per page: **TRACKING ARTIFACT (regression), high confidence.**
- Both suspects were healthy in EVERY prior window (why-did-water: 7.7-9.4s through 08-27; water-meter: 6.8-10.0s) and collapsed to ~0 only in the LIVE 08-29 pull — with pv==count (pageview fired, duration didn't).
- **4 pages affected, not 2:** 18-fuel-adjustment and utility-bills-costs-explained show the same ~0 signature. Same-count-band controls are healthy. This is a Rybbit current-window regression on low-volume pages.
- **Action for the measurement watch:** treat top_s in `baseline_21-30.json` as INVALID for these 4 paths; re-baseline top_s from the next healthy pull (visits/bounce/pageviews remain valid). Do not "fix" the pages for this.

### A3. Affiliate link images — COMPLETE & CLEAN (verifier + executor, vision-verified)
- Coverage: **all 12 wired ASINs** have `data/product_images.yaml` entries AND on-disk files (9 distinct images; 3 smart-plug-class ASINs legitimately share `smart-plug.webp`).
- Quality: **9/9 product images viewed — all match the real product's form factor; zero trust risk** (`.squad/SQ-058/product-image-qa.md`).
- **Codex needs to generate NOTHING here.** The only affiliate-image action in this mission is inside the one new box (below), which auto-renders from existing yaml art.

## B. The visual makeover — 10 per-page plans (AUTHORITATIVE for Codex)

**Read first:** `.squad/SQ-058/wiring-rules.md` (the mechanical contract: canonical shortcode, alt-text voice, file conventions, verification steps) — then each plan in `.squad/SQ-058/visual-plans/<slug>.md` (SQ-056 format: hero verdict, placements table with exact section + concept + retention mechanism + filename, earn-their-place rejects, cohesion note).

### B1. Per-page totals (the 3-7 band, every placement retention-named)

| Page | Total | Composition | Hero | New body figures |
|---|---|---|---|---|
| 01-how-to-read-your-electric-bill | 5 | 1 replace-hero + 3 new + reuses | **REPLACE** (photorealistic → flat ledger) | `statement-anatomy-labeled.webp` (centerpiece), `kwh-explanation-dial.webp` + 1 |
| 08-time-of-use-electricity | 5 | 1 replace-hero + 1 KEEP clock + 3 new | **REPLACE** | `load-shift-dishwasher.webp` + 2 (see plan) |
| why-did-my-water-bill-suddenly-increase | 4 | keep hero + 3 new | keep | `toilet-dye-test.webp` + 2 (reuses diagnosis-strip, leak-indicator-dial) |
| how-to-read-a-water-meter | 4 | keep hero + 1 KEEP dial + 2 new | keep | `water-meter-read-sequence.webp` + 1 (reuses ccf-conversion-chain) |
| tiered-electricity-rates-explained | 4 | 1 replace-hero + 3 new | **REPLACE** (title-card → house style) | `tier-ladder-worked-example.webp` + trio comparison |
| 49-demand-charges | 3 | 1 keep hero + 2 new | keep (best of trio) | `demand-vs-energy-analogy.webp` (kW vs kWh) + trio comparison |
| 21-past-due-balance | 3 | 1 keep hero + 1 WIRE orphan + 1 replace-orphan | keep | `disconnection-notice-to-deadline.webp` (see B3) |
| 26-utility-deposit-explained | 3 | keep hero + 2 new | keep | `deposit-lifecycle-timeline.webp` + 1 |
| how-to-read-electric-meter | 3 | keep hero + 2 new + reuse | keep | dial-procedure figure (see plan) + estimated-read-bars reuse |
| 27-utility-connection-fee | 3 | replace/add hero + 2-3 new | per plan (no hero dir today) | `connection-fee-routing.webp` + per plan |

### B2. Generation list (concept-deduped, smallest honest set)
The cartographer's cross-page rulings (`.squad/SQ-058/concept-dedup.md`) + lieutenant viewings reconcile to ~**12-15 distinct NEW files** (exact authoritative list = the NEW/REPLACE "Proposed filename" fields in the 10 plans):
1. `statement-ledger-hero.webp` (01 hero) · 2. `statement-anatomy-labeled.webp` (01) · 3. `kwh-explanation-dial.webp` (01) · 4. `water-meter-read-sequence.webp` · 5. `toilet-dye-test.webp` · 6. `deposit-lifecycle-timeline.webp` · 7. `connection-fee-routing.webp` · 8. `demand-vs-energy-analogy.webp` · 9. `load-shift-dishwasher.webp` · 10. `tier-ladder-worked-example.webp` · 11. `rate-structure-trio-comparison.webp` (ONE shared, wired on the trio) · 12. `disconnection-notice-to-deadline.webp` (21) — plus the tiered + 08-TOU replacement heroes named in their plans, and any second figure their tables list.
**Reuse — do NOT regenerate:** `time-of-use-clock.webp` (08), `dial-meter-reading.webp` (water-meter), `water-diagnosis-strip.webp` + `toilet-leak-cost.webp` (06), `leak-indicator-dial.webp` (leak-indicator page), `ccf-conversion-chain.webp` (ccf-calculator), `estimated-read-bars.webp` (30-spike), `ebill-4numbers.webp` / `bill-anatomy-category-map.webp` (electric-bill-breakdown — only if the plan's condition holds), `past-due-bill-anatomy.webp` (21's orphan, WIRE as-is).
**Never wire:** `custom_inline.webp` (28-reconnect, photorealistic off-bible), `past-due-disconnection-timeline.webp` in current form (see B3).

### B3. Orphan dispositions (21-past-due)
- `past-due-bill-anatomy.webp` — **WIRE** at `## Step 1: Reconcile the Account First` (viewed: on-bible annotated past-due statement; alt text in plan).
- `past-due-disconnection-timeline.webp` — **DO NOT WIRE; retire** (viewed: red-dominant alarm tone violates the style bible on a crisis page, and its generic 60-day arc contradicts the page's verified state-specific notice rules). Its job is replaced by NEW `disconnection-notice-to-deadline.webp` (notice-card with amber disconnection-date flag + state-rule chips).

### B4. Style (binding — the full bible is in each plan)
"The Independent Bill Auditor": flat ledger surfaces, ink `#0e201c` / cream `#fffcfa` / grid-teal `#3c655c`, amber `#e8a33d` reserved for THE ONE element that matters per figure, mono figures, no gradients/3D/people, annotations hand-entered. Crisis page (21) stays calm-procedural — no red, no alarm.

## C. Engagement & affiliate strategy (how this makes readers stay + click)

**Retention mechanisms (named per image in every plan):** answer-moment figures (first-screen concept becomes glanceable), action-moment demos (the dial sequence, the dye test — show the thing the reader is about to DO), math-made-visual at the dense spots (the $169 tier ladder, the 8-CCF conversion, the kW-vs-kWh split), and pre-exit figures that earn the scroll into Related Reading. Density is deliberately at the band floor for thin/stress pages (27, 49, 21, 26: exactly 3) and up to 5 only where engagement is proven (01, 08).

**Affiliate strategy:** exactly **ONE new product box** in the tier — Govee leak detectors `B0DQLFC3Q6` on why-did-water, placed at the leak-check action moment (publish-ready shortcode + vision-verified image accuracy in its plan; the same ASIN already runs on 3 sibling water pages). 08-TOU keeps its Kasa KP115 box untouched (its product image auto-renders and passed QA). **21-past-due gets NO box ever** (crisis page, binding). Every product image is affiliate-wired by construction (product-box renders from yaml); no bare un-monetized product figures anywhere.

## D. Codex execution order
1. Read `wiring-rules.md` + all 10 plans in `visual-plans/`.
2. Generate the NEW list (B2) in the style bible; sizes/formats per wiring rules.
3. Wire placements in plan order (exact section, before/after the named block); wire reuses with the plan's alt/caption.
4. Hero REPLACEMENTS exactly as the three plans specify (frontmatter `image:` swap; file stays under the slug dir). No other frontmatter changes except `updated:`.
5. Add the one product box (why-did-water plan, verbatim).
6. Retire `past-due-disconnection-timeline.webp` (delete after its replacement is wired).
7. Run the wiring-rules verification checklist (hugo build, per-page 3-7 count, all srcs resolve, alts present, width/height set, sizes under budget).

## E. Verification evidence for this handoff
- All 10 plans authored vision-verified (heroes + every existing asset VIEWED; verdicts grounded).
- Mason's edits: build EXIT 0, links resolve, facts-frozen. Commander disk-checked + fixed the bonus 404.
- Rybbit adjudication data-backed (archived windows vs LIVE, controls). Product QA 9/9 viewed-clean.
- Fleet: 3× lieutenant (plans) · mason (links) · executor (Rybbit + product QA) · verifier (wiring contract) · cartographer (dedup, 36-min over-run with truncation warnings — its rulings were reconciled against the lieutenant viewings; plans are authoritative).
- Artifacts: `.squad/SQ-058/` (visual-plans/ ×10, wiring-rules.md, concept-dedup.md, rybbit-suspect-check.md, product-image-qa.md, packets/, results-wave1/).
