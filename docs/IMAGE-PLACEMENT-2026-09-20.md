# Image Placement Report — Next-5 Articles (2026-09-20)

For the image agent. 12 images total: 5 heroes (REQUIRED — CI fails without them) + 7 inline visuals.
Delivery target: static/images/articles/<article-slug>/<exact-filename>.webp — filenames below are literal,
already referenced in the live markdown; do not rename.

## House style (match existing site visuals)

- Format: .webp, graph-paper / technical line-art illustration style, charcoal lines, ONE amber accent color
  (see existing examples: static/images/articles/why-did-my-water-bill-suddenly-increase/*.webp,
  level-1-ev-charging-cost/*_hero.webp). No photorealism, no AI-text-garble — if the image carries text,
  keep it to 1–4 short labels and double-check spelling.
- Hero size: landscape ~1200×630 (og:image crop-safe). Inline visual: ~1200×800; wide=true items ~1200×600.
- Alt text in the markdown is final; the image must actually depict what the alt says (accessibility + SEO).
- HARD RULE: no fake testing implications (no "our lab", no hands-with-multimeter "we measured" vibes),
  no brand logos, no readable utility-bill trademarks.

## Article 1 — why-is-my-heating-bill-so-high (Electricity/Heating; hero + 2)

1. HERO static/images/articles/why-is-my-heating-bill-so-high/why-is-my-heating-bill-so-high_hero.webp
   Alt: split-screen technical illustration: thermostat on one side; gas flame, electric coil, heat-pump fan
   on the other; rising cost arrow. (Landscape 1200×630.)
2. INLINE (wide) .../blower-motor-draw.webp
   Alt: furnace blower motor diagram with ammeter showing high current draw due to a clogged MERV filter.
   Context: sits in "Ranked Cause 2" — show airflow restriction → higher wattage.
3. INLINE (wide) .../heating-cost-comparison.webp
   Alt: bar chart comparing cost of 100,000 BTU across Natural Gas, Heat Pump, Electric Resistance.
   Use the article's verified numbers: Gas (80% AFUE @ $1.50/therm) $1.88 · Electric resistance
   (18.34¢/kWh) $5.37 · Heat pump (COP 3) ≈ $1.79 — label bars with $ values.

## Article 2 — how-to-tell-if-neighbor-is-stealing-electricity (Electricity; hero + 1)

4. HERO .../how-to-tell-if-neighbor-is-stealing-electricity_hero.webp
   Alt: digital electric meter with a hand holding a flashlight to the display.
5. INLINE (wide) .../breaker-test-logic.webp
   Alt: one-line electrical flow diagram: grid → meter → main breaker → house circuits, with a branch
   point between meter and breaker labeled "tap/shared circuit here = meter runs with breaker OFF".

## Article 3 — how-much-does-dripping-faucet-add-to-water-bill (Water; hero + 1)

6. HERO .../how-much-does-dripping-faucet-add-to-water-bill_hero.webp
   Alt: close-up of a single water droplet at a chrome faucet spout (this one may be the more
   photographic/realistic of the set — the alt says "photograph").
7. INLINE (wide) .../drip-math-breakdown.webp
   Alt: infographic chain: 1 drip/second → 3,000 gal/yr → 4 CCF → $ band. Steps as connected boxes;
   numbers exactly: "1 drip/sec", "3,000 gallons/year", "4 CCF", "water $15–30 · +sewer ≈ doubles".

## Article 4 — why-is-my-sewer-bill-higher-than-my-water-bill (Water; hero + 1)

8. HERO .../why-is-my-sewer-bill-higher-than-my-water-bill_hero.webp
   Alt: split illustration — clean water from a tap (left) vs wastewater treatment plant (right).
9. INLINE (wide) .../sewer-vs-water-math.webp
   Alt: bar chart comparing a ~$26 water bill vs the $86.77 typical Seattle sewer bill, with the split
   of volumetric vs fixed service fee. Label: "Water ≈ $25.80 (4.3 CCF est.)" vs "Sewer $86.77 (SPU 2026)".

## Article 5 — how-much-does-it-cost-to-run-a-window-or-portable-ac (Electricity; hero + 2)

10. HERO .../how-much-does-it-cost-to-run-a-window-or-portable-ac_hero.webp
    Alt: split illustration: window AC unit (left) vs portable AC with exhaust hose (right),
    cost-per-hour overlays in amber.
11. INLINE (wide) .../ac-wattage-math.webp
    Alt: conversion diagram: BTU ÷ EER = Watts, with the worked example 8,000 ÷ 10 = 800 W.
12. INLINE .../efficiency-comparison.webp
    Alt: 3-bar relative-efficiency chart: Portable (lowest) → Window (middle) → Mini-split (highest).

## After the images land (Boss checklist)

1. `python3 scripts/check_image_paths.py .` → must print OK (heroes + inline).
2. `hugo --minify --gc --destination /tmp/verify` → build green, sitemap still 153 URLs.
3. Vision-QA each image: motif matches alt, no garbled text, house style.
4. Commit + push → CI deploys → cache-busted live check on the 5 URLs.

## Repo state at handoff

Articles are committed LOCALLY on main (not pushed — push would fail CI on missing heroes).
Slates/research: docs/NEXT-5-SLATE-2026-09-20.md. Push only after checklist items 1–3 pass.
