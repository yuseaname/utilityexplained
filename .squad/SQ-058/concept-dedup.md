# SQ-058 Concept Dedup Map

**Cartographer · 2026-08-29** · Merged from 3 lieutenant packets (LT-A/water+deposit, LT-B/rate-trio, LT-C/bill+meter+crisis)

## 1. Concept Matrix: Shared vs Split Ruling

| Concept | Pages wanting it | Ruling | Reason |
|---------|-----------------|--------|--------|
| **Meter dial reading** | how-to-read-a-water-meter, how-to-read-electric-meter, why-did-my-water-bill-suddenly-increase (meter test step) | **SPLIT** — two distinct assets needed | Water meter dials (sweep hand, odometer, leak triangle) are structurally different from electric meter dials (5 clock-face dials with alternating direction). The why-did-water page's meter test step is a close-up of the leak indicator (small triangle/spinner), which is a different crop than the full dial-decoding figure. Each needs context-specific labels and numbers. |
| **Bill anatomy (annotated statement)** | 01-how-to-read-your-electric-bill, 21-past-due-balance | **SHARED** — one asset, two context-identical wirings | Both pages want a labeled electric-bill figure showing account summary, charges, usage, and due date. The line items are identical for both pages (supply, delivery, taxes, total). The past-due version adds a red "PAST DUE" stamp and late fee line — but that's a single-element overlay, not a different figure. **Propose ONE canonical bill anatomy with a past-due variant** (same base, amber overlay stamp). Write once; two pages wire the same file with different captions. |
| **TOU clock** | 08-time-of-use-electricity (already has it), 49-demand-charges (contextual reference), tiered-rates (contextual) | **SHARED** — already reused across 3 pages (08, which-rate-plan, 46-what-time) | The TOU clock is context-identical: a 24h dial with off-peak/shoulder/peak periods. 08 currently wires its own copy. 49-demand would reference it only as sibling context (not a new figure).  which-rate-plan and 46-what-time already reuse the same concept from their own slug dirs. **Consolidate to ONE canonical file** under `08-time-of-use-electricity/` (already wired there) and have all other pages reference it. No new asset needed. |
| **Tier ladder / staircase** | tiered-electricity-rates-explained, 49-demand-charges | **SPLIT** — different worked examples | Tiered page: 400 kWh @ $0.28 + 150 kWh @ $0.38 = $169. 49-demand: 12 kW @ $8.50 + energy at $0.11. The tiered page shows a consumption staircase (kWh thresholds); 49-demand shows a demand-charge table (kW peak). Different numbers, different labels, different worked examples. |
| **Deposit lifecycle timeline** | 26-utility-deposit-explained | **UNIQUE** — no other page wants it | Only 26-deposit covers the pay→hold→review→refund cycle. No overlap. |
| **Leak-check flow / diagnosis strip** | why-did-my-water-bill-suddenly-increase | **SHARED** with 06-water-bill-too-high (existing asset: `water-diagnosis-strip.webp`) | Both pages have a 3-step water diagnosis: compare bills, test meter, isolate valve. The why-did-water page's leak-check section was restructured into a 4-item checklist covering EPA facts, dye test, meter test, and leak indicators. The diagnosis strip on 06 covers the same workflow. **Reuse** `06-water-bill-too-high/water-diagnosis-strip.webp` with a caption adapted to the sudden-increase context. |
| **Toilet dye test** | why-did-my-water-bill-suddenly-increase | **SHARED** with 06-water-bill-too-high (existing `toilet-leak-cost.webp`) and is-your-toilet-running-leak-test (hero only) | The dye-test action moment is the same: dropping a tablet into the tank. 06's `toilet-leak-cost.webp` shows a toilet tank cross-section with a leaking flapper and cost counter — that's more about cost than procedure. The most suitable reuse is **is-your-toilet-running-leak-test's hero** (which shows the dye test), but that's a hero, not a body figure. **Recommend:** generate a NEW dedicated dye-test figure (toilet tank with dye-colored water, amber arrow on leak path). |
| **Water meter leak indicator** | why-did-my-water-bill-suddenly-increase, how-to-read-a-water-meter | **SHARED** with water-meter-leak-indicator-explained (existing `leak-indicator-dial.webp`) | The leak indicator (small triangle/spinner) is identical across both pages. `water-meter-leak-indicator-explained/leak-indicator-dial.webp` shows a close-up of the leak indicator dial. **Reuse** it on why-did-water's meter-test step and water-meter's leak-check section. |
| **Disconnection / shutoff timeline** | 21-past-due-balance (unwired `past-due-disconnection-timeline.webp`), 28-utility-reconnection-fee (existing `shutoff-avoidance-timeline.webp`) | **SPLIT** — different audience/stakes | 21-past-due: timeline from 10-15 day notice → payment arrangement → protection programs. 28-reconnect: timeline from notice → shutoff → reconnect fee → payment. Both exist on disk independently. The 21 asset is past-due specific (crisis tone); the 28 asset is reconnect specific (recovery tone). **Keep both.** Each is already written for its page's context. |
| **Demand-vs-energy (kW vs kWh)** | 49-demand-charges-electricity-bill-explained | **UNIQUE** — only 49-demand covers this | The concept figure showing kW vs kWh as speed vs distance is unique to 49-demand. No overlap. |
| **CCF conversion** | how-to-read-a-water-meter | **SHARED** with ccf-calculator (existing `ccf-conversion-chain.webp`) | The conversion chain (CCF → gallons → cost) is identical: 1 CCF = 748 gallons. The water-meter page's worked example (1255-1247=8 CCF × 748 = 5,984 gal) is the same math. **Reuse** `ccf-calculator/ccf-conversion-chain.webp` with a caption referencing the worked example. |
| **Connection fee flow / routing** | 27-utility-connection-fee-explained | **UNIQUE** — only 27-connection covers this | The routing self-check (3 branches: new service, same address, different address) is unique to 27-connection. No overlap. |
| **Estimated read** | how-to-read-electric-meter, why-did-my-water-bill-suddenly-increase | **SHARED** with 30-sudden-spike (existing `estimated-read-bars.webp`) | The estimated-read concept (dashed bar vs actual bar) is the same across all pages. 30's `estimated-read-bars.webp` shows a 34-day estimated vs 28-day actual comparison. **Reuse** on electric-meter page's estimated-read section and why-did-water's spike-diagnosis context. |
| **Rate structure comparison (trio)** | 49-demand-charges, 08-time-of-use, tiered-electricity-rates-explained | **SHARED** — ONE trio comparison table/diagram | The rate-structure trio is a cross-page concept: the three pages are wired as a circuit. A single comparison table (flat rate vs TOU vs tiered) showing when each is optimal would serve all three. **Generate ONE new shared asset** placed on the most central page (tiered or 49-demand) and linked from the other two. |

## 2. Existing Asset Reuse Table

| Existing asset (source slug/filename) | Pages that can wire it | Condition |
|--------------------------------------|----------------------|-----------|
| `08-time-of-use-electricity/time-of-use-clock.webp` | 08-TOU (already wired), 49-demand (contextual reference), tiered (contextual), which-rate-plan (already wired separately), 46-what-time (already wired separately) | Use as-is; canonical file under 08-TOU. Pages that currently have their own copy should reference the 08-TOU copy. |
| `how-to-read-a-water-meter/dial-meter-reading.webp` | how-to-read-a-water-meter (already wired) | Water-meter specific. Not reusable for electric meter (different dial types). |
| `21-past-due-balance-utility-bill-explained/past-due-bill-anatomy.webp` | 21-past-due-balance (unwired on disk), 01-how-to-read-your-electric-bill (if unbranded generic) | **Conditional:** if the anatomy is a generic electric bill (no past-due stamps), it can serve 01's bill-anatomy figure. If it has past-due markings, it's 21-only. Need to verify the image content. |
| `21-past-due-balance-utility-bill-explained/past-due-disconnection-timeline.webp` | 21-past-due-balance (unwired on disk) | Crisis-context specific. Not reusable for 28-reconnect (different tone). |
| `06-water-bill-too-high/water-diagnosis-strip.webp` | 06-water-bill-too-high (already wired), why-did-my-water-bill-suddenly-increase | Reuse directly. 3-step diagnosis matches the leak-check checklist. |
| `06-water-bill-too-high/toilet-leak-cost.webp` | 06-water-bill-too-high (already wired), why-did-my-water-bill-suddenly-increase | Partial reuse: shows cross-section of leaking flapper with cost. Not a dye-test demo. Best as a supporting figure, not the primary dye-test action moment. |
| `water-meter-leak-indicator-explained/leak-indicator-dial.webp` | water-meter-leak-indicator-explained, why-did-my-water-bill-suddenly-increase, how-to-read-a-water-meter | Reuse directly. The leak indicator is the same physical component. |
| `ccf-calculator/ccf-conversion-chain.webp` | ccf-calculator, how-to-read-a-water-meter | Reuse directly. 1 CCF = 748 gallons is universal. |
| `ccf-calculator/tier-math-staircase.webp` | ccf-calculator, tiered-electricity-rates-explained | **Conditional:** the tiered-rates page uses electricity (kWh) not water (CCF). The staircase concept is the same but the units and numbers differ. Not reusable directly. |
| `how-to-lower-electric-bill-complete-guide/cost-tier-ladder.webp` | how-to-lower-electric-bill-complete-guide, tiered-electricity-rates-explained | **Not reusable:** shows cost tiers for saving (free/cheap/expensive fixes), not rate tiers for electricity pricing. Different concept. |
| `30-sudden-spike-in-electricity-bill-no-usage/estimated-read-bars.webp` | 30-sudden-spike, how-to-read-electric-meter, why-did-my-water-bill-suddenly-increase | Reuse directly. The estimated-vs-actual bar comparison is universal. |
| `30-sudden-spike-in-electricity-bill-no-usage/meter-dial-test.webp` | 30-sudden-spike, how-to-read-electric-meter | **Partial:** shows electric meter dial test. Reusable for electric-meter page's meter-test step. Not for water meter. |
| `electric-bill-breakdown-understanding-line-items/bill-anatomy-category-map.webp` | electric-bill-breakdown, 01-how-to-read-your-electric-bill, 21-past-due-balance | **Conditional:** this is a category-map (7 numbered lines), not a real bill. If the plan calls for a real bill figure, this won't fit. If the plan calls for a line-item map, it's reusable. |
| `electric-bill-breakdown-understanding-line-items/ebill-4numbers.webp` | electric-bill-breakdown, 01-how-to-read-your-electric-bill | Shows 4 key numbers on an electric bill. Reusable for 01's bill-reading walkthrough. |
| `electric-bill-breakdown-understanding-line-items/ebill-tou.webp` | electric-bill-breakdown, 08-time-of-use-electricity | Shows a TOU line on a bill. Reusable on 08-TOU to show where TOU charges appear on a bill. |
| `28-utility-reconnection-fee-explained/shutoff-avoidance-timeline.webp` | 28-utility-reconnection-fee (already wired) | Not reusable for 21-past-due (different tone and audience). |
| `28-utility-reconnection-fee-explained/reconnect-process.webp` | 28-utility-reconnection-fee (already wired) | Reconnect-specific. Not applicable to other pages. |
| `28-utility-reconnection-fee-explained/reconnect_fees.webp` | 28-utility-reconnection-fee | Unwired orphan. Reconnect-specific. |
| `28-utility-reconnection-fee-explained/reconnect_avoid.webp` | 28-utility-reconnection-fee | Unwired orphan. Reconnect-specific. |
| `28-utility-reconnection-fee-explained/custom_inline.webp` | 28-utility-reconnection-fee | Orphan (photorealistic stock photo — off style-bible). Do not wire. |
| `12-how-to-read-your-gas-bill/gas-bill-anatomy.webp` | 12-how-to-read-your-gas-bill | Gas-specific. Not reusable for electric bill pages. |

## 3. Canonical Filenames for NEW Shared Assets

When a shared asset is generated (not reused from an existing sibling), propose ONE canonical filename under the most central page's slug directory:

| Shared concept | Canonical filename | Host slug | Pages that wire it |
|---------------|-------------------|-----------|-------------------|
| Bill anatomy (generic electric, with optional past-due overlay) | `bill-anatomy.webp` | `01-how-to-read-your-electric-bill` | 01, 21 (with past-due overlay) |
| Rate-structure trio comparison | `rate-structure-trio-comparison.webp` | `tiered-electricity-rates-explained` | tiered, 49-demand, 08-TOU |
| Dye test (toilet tank with dye-colored water) | `toilet-dye-test.webp` | `why-did-my-water-bill-suddenly-increase` | why-did-water only (unique) |

**Note:** The TOU clock already exists as `time-of-use-clock.webp` under 08-TOU. Its canonical home is `08-time-of-use-electricity/time-of-use-clock.webp`. Other pages should reference this single file via `{{< visual src="/images/articles/08-time-of-use-electricity/time-of-use-clock.webp" ... >}}` rather than maintaining copies in their own slug dirs.

## 4. Generation Count: Distinct NEW Images Codex Must Generate

Target: **the smallest honest set** after reuse.

### Existing assets REUSED (no generation needed):
1. `time-of-use-clock.webp` — already exists on 08-TOU, reused across rate trio
2. `water-diagnosis-strip.webp` — 06 page, reused on why-did-water
3. `leak-indicator-dial.webp` — water-meter-leak-indicator, reused on why-did-water and water-meter
4. `ccf-conversion-chain.webp` — ccf-calculator, reused on water-meter
5. `estimated-read-bars.webp` — 30-sudden-spike, reused on electric-meter and why-did-water
6. `meter-dial-test.webp` — 30-sudden-spike, reused on electric-meter
7. `past-due-bill-anatomy.webp` — 21-past-due (unwired on disk, wire in)
8. `past-due-disconnection-timeline.webp` — 21-past-due (unwired on disk, wire in)
9. `bill-anatomy-category-map.webp` — electric-bill-breakdown, if 01's plan fits a category map
10. `ebill-4numbers.webp` — electric-bill-breakdown, if 01's plan fits
11. `toilet-leak-cost.webp` — 06 page, partial reuse on why-did-water (cost context)

### NEW assets to generate:

**LT-A pages (water/deposit):**
- **why-did-my-water-bill-suddenly-increase:**
  - `toilet-dye-test.webp` — NEW (dye test action moment, no existing asset)
  - (reuses: water-diagnosis-strip, leak-indicator-dial, toilet-leak-cost, estimated-read-bars)
- **how-to-read-a-water-meter:**
  - `water-meter-read-sequence.webp` — NEW (dial-decoding arrows, direction alternation) — water meter specific, not shared with electric meter
  - (reuses: dial-meter-reading (existing), ccf-conversion-chain, leak-indicator-dial)
- **26-utility-deposit-explained:**
  - `deposit-lifecycle-timeline.webp` — NEW (pay→hold→review→refund timeline, unique)
- **27-utility-connection-fee-explained:**
  - `connection-fee-routing.webp` — NEW (3-branch self-check, unique; thin page, 3 images max)

**LT-B pages (rate trio):**
- **49-demand-charges-electricity-bill-explained:**
  - `demand-vs-energy-analogy.webp` — NEW (kW vs kWh speed vs distance, unique)
  - (reuses: rate-structure-trio-comparison [new shared below])
- **08-time-of-use-electricity:**
  - `load-shift-dishwasher.webp` — NEW (load-shift example, unique to 08's Kasa example)
  - (reuses: time-of-use-clock, ebill-tou, rate-structure-trio-comparison)
- **tiered-electricity-rates-explained:**
  - `tier-ladder-worked-example.webp` — NEW (400×$0.28 + 150×$0.38 = $169, unique numbers)
  - (reuses: rate-structure-trio-comparison)

**LT-C pages (bill/meter/crisis):**
- **01-how-to-read-your-electric-bill:**
  - `bill-anatomy.webp` — NEW (canonical labeled electric bill; shared with 21 via overlay)
  - `kwh-explanation-dial.webp` — NEW (kWh concept figure, 114w dead zone breaker)
  - (reuses: ebill-4numbers, bill-anatomy-category-map)
- **how-to-read-electric-meter:**
  - `electric-meter-dial-read-sequence.webp` — NEW (5 dials, direction alternation, unique to electric)
  - (reuses: meter-dial-test, estimated-read-bars)
- **21-past-due-balance:**
  - (reuses: past-due-bill-anatomy, past-due-disconnection-timeline [both unwired on disk], bill-anatomy with past-due overlay)

**Shared new assets (generated once):**
- `rate-structure-trio-comparison.webp` — NEW (shared across tiered, 49-demand, 08-TOU)

### TOTAL NEW IMAGES TO GENERATE: **12**

| # | Filename | Host slug | Pages served |
|---|----------|-----------|-------------|
| 1 | `toilet-dye-test.webp` | why-did-my-water-bill-suddenly-increase | why-did-water only |
| 2 | `water-meter-read-sequence.webp` | how-to-read-a-water-meter | water-meter only |
| 3 | `deposit-lifecycle-timeline.webp` | 26-utility-deposit-explained | 26-deposit only |
| 4 | `connection-fee-routing.webp` | 27-utility-connection-fee-explained | 27-connection only |
| 5 | `demand-vs-energy-analogy.webp` | 49-demand-charges-electricity-bill-explained | 49-demand only |
| 6 | `load-shift-dishwasher.webp` | 08-time-of-use-electricity | 08-TOU only |
| 7 | `tier-ladder-worked-example.webp` | tiered-electricity-rates-explained | tiered only |
| 8 | `bill-anatomy.webp` | 01-how-to-read-your-electric-bill | 01 (primary), 21 (past-due overlay) |
| 9 | `kwh-explanation-dial.webp` | 01-how-to-read-your-electric-bill | 01 only |
| 10 | `electric-meter-dial-read-sequence.webp` | how-to-read-electric-meter | electric-meter only |
| 11 | `rate-structure-trio-comparison.webp` | tiered-electricity-rates-explained | tiered, 49-demand, 08-TOU |
| 12 | `past-due-overlay-stamp.webp` | 21-past-due-balance-utility-bill-explained | 21 only (overlay on shared bill-anatomy) |

### Existing assets to WIRE IN (no generation): 8
- `time-of-use-clock.webp` (08-TOU, already wired)
- `dial-meter-reading.webp` (water-meter, already wired)
- `past-due-bill-anatomy.webp` (21, unwired → wire in)
- `past-due-disconnection-timeline.webp` (21, unwired → wire in)
- `water-diagnosis-strip.webp` (06→why-did-water reuse)
- `leak-indicator-dial.webp` (water-meter-leak-indicator→why-did-water/water-meter reuse)
- `ccf-conversion-chain.webp` (ccf-calculator→water-meter reuse)
- `estimated-read-bars.webp` (30→electric-meter/why-did-water reuse)
- `meter-dial-test.webp` (30→electric-meter reuse)

## 5. Cross-Seat Reconciliation Notes

- **LT-A (water pages)** and **LT-C (electric meter)** both want meter dial figures. These are **split** — water vs electric dials are structurally different. Each seat should plan their own dial figure.
- **LT-A (why-did-water)** and **LT-C (how-to-read-electric-meter)** both want estimated-read figures. These are **shared** — reuse `estimated-read-bars.webp` from 30-sudden-spike.
- **LT-A (why-did-water)** and **06-water-bill-too-high** share leak-check diagnosis and toilet-leak concepts. Reuse the 06 assets.
- **LT-B (rate trio)** all share the TOU clock concept. Reuse 08's existing `time-of-use-clock.webp`.
- **LT-B and LT-C** both want bill anatomy figures. LT-C's 01 page and LT-A's none. LT-C's 01 and LT-C's 21 share bill anatomy (with past-due overlay).

## 6. Blank Spots / Unsurveyed

- The actual content of `past-due-bill-anatomy.webp` and `past-due-disconnection-timeline.webp` was not read (text-only seat). Rulings assume they are past-due-specific. If they are generic enough to serve 01's bill anatomy, the NEW count drops by 1.
- The `bill-anatomy-category-map.webp` and `ebill-4numbers.webp` from electric-bill-breakdown were not read. Their fitness for 01's plan depends on the visual style matching the Style Bible.
- The `custom_inline.webp` on 28-reconnect was confirmed as off-style-bible photorealistic stock. Do not wire.
- The `custom_hero.webp` on 01 is the hero. No judgment on body visual reuse.
