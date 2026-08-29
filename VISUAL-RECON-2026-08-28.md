# Visual Content Recon — utilityexplained.com

**Date:** 2026-08-28 · **Formation:** swarm wing (prospector/tracer/cartographer/verifier/mason) + msi executor; cloud excluded per order (scout died twice; its angle absorbed; the harness's automatic cloud replay executed **zero actions** and was left idle).
**Method:** full read of ~30 priority pages + rendered-HTML mechanical audit + archetype mapping + scroll-position analysis + style-bible extraction, Commander-synthesized.

---

## Site-level findings (act on these first)

| # | Finding | Evidence | Action |
|---|---|---|---|
| V1 | **246 card images fail WCAG 1.1.1** — `alt class=card-image` broken attribute syntax | verifier, script-backed | Template fix in related-posts/card partial — one edit, sitewide accessibility |
| V2 | **Two pages have finished images sitting unreferenced on disk** — `how-sewer-charges` (3 webp) and `28-reconnection` (4 webp) | prospector, file-vs-HTML diff | Wire them in — zero generation cost |
| V3 | **3 pages have NO hero at all**: ccf-calculator, which-rate-plan, gadgets | frontmatter + rendered HTML | Heroes below |
| V4 | 70% of pages are hero-only; 8% have rich body visuals | cartographer | Briefs below target the gap |
| V5 | One sitewide og-image (og-default.png) — no per-page social/image-search surface | tracer | Generate 1200×630 og-variants for top pages |
| V6 | Old audit's "9 generic stock shared on 45 pages" is STALE — removed Aug 15; today's heroes are article-specific | verifier REFUTED | Retire that assumption |

**House style (mandatory for all briefs):** *"The Independent Bill Auditor"* — flat ledger surfaces, engineering-blueprint feel, no gradients/glassmorphism, mono type as the voice of numbers, **amber `#e8a33d` reserved for the one line that matters** on ink `#0e201c` / cream `#fffcfa` paper, faint grid-teal `#3c655c` scaffolding. Charts render data honestly; annotations look hand-entered by an auditor.

---

## Page-by-page recon report

### 1. `/blog/how-to-lower-electric-bill-complete-guide/` — How to Lower Your Electric Bill (flagship)
**Priority: P0 · Traffic: 123 pv/wk (#1) · Money page (4 boxes)**
**Current:** energy-hogs hero chart only; the 20-step cost-tier journey, payback tables, and Quick Answer decision line carry no visuals.
**Recommended: 5 images**

1. **Cost-tier ladder** — *Placement:* directly under the "Start here" decision line. Three ascending ledger steps (Free today / Under $50 / Big-ticket) with a small kWh coin-stack on each; amber highlights the middle rung ("where most homes start"). *Purpose:* converts the tier structure into a scannable commitment path. *File:* `cost-tier-ladder.webp` · *Alt intent:* "Three cost tiers for lowering an electric bill, from free behaviors to big-ticket upgrades." *GPT-2 note:* flat isometric steps, mono labels, house palette.
2. **Thermostat setback dial** — beside step 1: round dial at 78°F, amber arc showing the 7–10° setback window, small 10%-bill coin falling away. *Alt:* "Thermostat dial showing a 7–10 degree setback saving up to 10%." Filename `thermostat-setback-dial.webp`.
3. **Phantom-load wall audit** — in step 3: night interior wall of outlets, six devices glowing faint teal standby LEDs, one Kill-A Watt-style meter reading "43 W" in amber. *Alt:* "Standby power drawn by plugged-in devices at night, measured by a plug-in meter." `phantom-load-wall.webp`.
4. **Payback timeline** — after the payback table: horizontal ledger timeline, LEDs (0.5yr) → thermostat (2yr) → heat pump (8yr), amber marks break-even points. *Alt:* "Payback periods of electric-bill improvements on a timeline." `payback-timeline.webp`.
5. **OG-variant** — 1200×630 hero-style: descending bill staircase with amber trend line. `og-flagship.png`.

### 2. `/blog/30-sudden-spike-in-electricity-bill-no-usage/` — Sudden Bill Spike (monetized)
**Priority: P0 · 47 pv/wk · The missing hero moment is the flowchart**
**Current:** hero only; the 12-step investigation is wholly text.
**Recommended: 4**

1. **Diagnosis flowchart** — after Quick Answer: decision tree (bill longer than usual? → estimated read? → rate line changed? → meter test → appliance hunt), amber path = the 80% answer. *Purpose:* this is THE retention image; arrest the 93%-bounce reader at the exact moment they decide to stay. `spike-diagnosis-flowchart.webp` · *Alt:* "Decision flowchart for finding the cause of a sudden electricity bill spike."
2. **Estimated-read correction graphic** — in cause #1: two bill bars (34-day vs 28-day) + "EST" stamp, amber on the delta. `estimated-read-bars.webp`.
3. **Meter dial test** — in the meter section: analog dial close-up with red leak-dial highlighted. `meter-dial-test.webp`.
4. **OG-variant.**

### 3. `/blog/06-water-bill-too-high/` — Water Bill Too High (monetized)
**Priority: P0 · 45 pv/wk**
**Current:** hero only; 3-step diagnosis and household table unvisualized.
**Recommended: 4**

1. **Three-step diagnosis strip** — under Quick Answer: 1 compare bills → 2 meter test → 3 isolate valve, as three flat ledger panels with amber step numbers. `water-diagnosis-strip.webp` · *Alt:* "Three-step process to diagnose a high water bill."
2. **Household-size usage chart** — beside the usage table: gentle bar steps 1→5 persons, national-median band in teal, amber note "your bill is the audit, not the average." `household-usage-bars.webp`.
3. **Toilet-leak cost drip** — in the toilet section: tank with faint flapper leak, amber counter "$70/mo" ticking. `toilet-leak-cost.webp`.
4. **OG-variant.**

### 4. `/blog/28-utility-reconnection-fee-explained/` — Reconnection Fee (#4 traffic)
**Priority: P0 · 34 pv/wk · ⚡ FREE WINS FIRST**
**Current:** zero rendered imagery — but `reconnect-process.webp`, `reconnect_fees.webp`, `reconnect_avoid.webp`, `custom_inline.webp` **already exist unreferenced on disk**.
**Recommended: 4 (wire the 3 best existing + 1 new)**
1–3. Wire existing assets at: process image beside the restoration steps; fees image beside the fee table; avoidance image beside the programs section. Verify each file's actual content matches its section before placing.
4. **NEW — shut-off-avoidance timeline** — notice period (10–15 days) → payment arrangement → protection program, amber marking the last safe exit. `shutoff-avoidance-timeline.webp`.

### 5. `/blog/how-sewer-charges-work-on-your-water-bill/` — Sewer Charges (28 pv/wk)
**Priority: P1 · ⚡ FREE WINS — 3 existing webps unreferenced**
Wire `sewer-flow.webp` (billing-model section), `sewer-3-ways.webp` (three models), `sewer-why-higher.webp` (winter averaging). One NEW: **winter-averaging 7.75-CCF worked example** ledger card (`winter-averaging-example.webp`).

### 6. `/blog/04-hidden-fees-utility-bill/` — Fees Hub
**Priority: P1 (strategic hub, its own audit flagged this)**
**Current:** hero only; the fee table carries everything.
**Recommended: 4**
1. **Annotated bill with fees circled** — THE canonical house image: flat bill replica, amber auditor circles around customer charge, rider, franchise fee; mono callout numbers. `annotated-bill-fees-circled.webp` · *Alt:* "Annotated utility bill with hidden fees circled."
2. **Fee taxonomy tree** — usage-based vs fixed vs event-driven, three ledger branches. `fee-taxonomy-tree.webp`.
3. **Directory mosaic** — hub's linked fee pages as a labeled card wall (optional; can be CSS, not image — prefer CSS).
4. **OG-variant** (reuses annotated bill).

### 7. `/blog/03-why-is-my-electric-bill-so-high/` — Why Is My Bill High (monetized, 27 pv/wk)
**Recommended: 4** — (1) **diagnosis-sequence flowchart** (bill → rate → usage → equipment); (2) **seasonal usage ribbon** (summer/winter peaks across 12 ledger columns); (3) **rate-vs-usage leverage see-saw**; (4) OG-variant.

### 8. `/blog/ccf-calculator/` — CCF Calculator (NEW TOOL, no hero)
**Recommended: 3** — (1) **HERO: conversion chain** CCF box → 748 gallons → dollar coins on a conveyor (`ccf-conversion-chain.webp`); (2) **tier math graphic** two-rate staircase under the tier explainer; (3) OG-variant.

### 9. `/blog/which-rate-plan-is-right-for-me/` — Rate Hub (NEW, no hero)
**Recommended: 3** — (1) **HERO: three-door decision visual** (Fixed / Variable / ToU doors, amber on "start here"); (2) **24-hour ToU clock** (shared asset — also serves 46 + 08); (3) OG-variant.

### 10. `/blog/gadgets-that-lower-utility-bills/` — Gadgets (money page, no hero)
**Recommended: 4** — (1) **HERO: gadget workbench** flat-lay of thermostat/plug/monitor/leak sensor on ledger paper; (2) **savings-per-gadget bar set**; (3) **"when it does NOT pay" caution card** (amber underline style); (4) OG-variant.

### 11–16. Second tier (1–2 briefs each)
- **11-kwh**: appliance annual-kWh ladder chart (`appliance-kwh-ladder.webp`).
- **46-cheapest-hours**: the 24h ToU clock (shared with #9).
- **07-gas-too-high**: ranked-causes horizontal bars + HDD heating-degree worked chart.
- **12-gas-bill**: gas-bill anatomy annotated replica.
- **phantom-power**: standby-watts bar chart (15-row table → 8-bar honest chart).
- **hvac-stages**: capacity waveforms — single-stage square wave vs variable modulation (the inherently-visual concept with zero diagrams today).

---

## Ranked implementation order

1. **Wire the 7 existing free-win images** (sewer ×3, reconnection ×3–4) — zero generation cost, live today
2. **Fix the 246 broken card alts** (V1) — one template edit, WCAG restored
3. **Flagship 5-image set** — biggest traffic × money surface
4. **30-spike flowchart set** — the single highest-retention image on the site
5. **06-water strip + chart** — monetized, #3 traffic
6. **Fees-hub annotated bill** — becomes the cluster's canonical visual, reused sitewide
7. **Three no-hero pages** (calculator, rate hub, gadgets)
8. **Second tier** (11, 46, 07, 12, phantom, hvac) + per-page OG-variants for the top 10

*Every brief above carries the house style block ("Independent Bill Auditor," palette hexes, flat-ledger rules) — a generation agent receives style + placement + alt intent + filename per image, nothing decorative.*
