# IMAGE-SPECS — 2026-09-26 space-heater-running-cost (next-5 #2)

Parent: PORTFOLIO-PM.md pickup item C. Article: content/blog/space-heater-running-cost.md (5dbd54da, held unpushed).
Model: NANO-BANANA-2-TEXT (owner mandate 9/22). Rule: every figure below is
copied verbatim from the article body/tables — if a number isn't here, it
doesn't go in the image. Style: match existing UE editorial infographics
(flat, clean labeled figures, cream/white background, gold+teal accents,
charcoal line work on graph paper per the sibling heater pages' image_alt
conventions).

Save as WebP, 1600px wide (hero can be 1920). Filenames exact — the article
frontmatter + {{< visual >}} shortcodes already reference them.

| # | File | Content (verbatim numbers only) | Alt text | Placement |
|---|------|--------------------------------|----------|-----------|
| 1 | space-heater-running-cost_hero.webp | A portable space heater next to a wall thermostat; the formula "cost/hour = watts ÷ 1,000 × your rate" written as clean hand-lettered math; NO dollar results in the image | Technical line illustration: space heater beside thermostat with the watts-to-dollars formula, charcoal on graph paper, one amber accent | Frontmatter hero (auto-renders) |
| 2 | cost-per-wattage-ladder.webp | Vertical ladder/bar chart, watts → $/hour: 200 W = $0.037 · 400 W = $0.073 · 750 W = $0.138 · 1,000 W = $0.183 · 1,500 W = $0.275; label "at 18.34¢/kWh US avg" | Bar chart of per-hour cost by heater wattage from 200 W to 1,500 W | After the per-wattage table |
| 3 | state-rate-spread.webp | Horizontal band chart: NV $0.20/h · US avg $0.275/h · CA-CT-MA band $0.42–0.53/h · HI $0.79/h; same heater, four bills; label "1,500 W heater, per hour" | Same 1,500 W heater's hourly cost across state rate bands, Nevada cheapest to Hawaii most expensive | After the state-spread table |
| 4 | duty-cycle-curve.webp | 24-hour timeline strip showing element ON/OFF blocks: full-power row (solid) vs thermostat-cycled row (~50% blocks); month labels "$66 full power" vs "$33 at 50% duty cycle" | Element-on timeline comparing a heater running non-stop versus thermostat cycling at about half duty | Duty-cycle section, after the three levers |
| 5 | zone-vs-whole-house.webp | Simple split scene: left = whole house heated at 70°F (all rooms lit); right = one warm room + cooler rest of house at 62°F with a small heater icon; tag "zone heating: >20% savings (DOE)" | Split illustration of whole-house heating versus zone heating one occupied room | Zone-heating section, after comparison table |

Notes:
- Hero (1) is REQUIRED to pass the image gate; 2–5 are the dwell-time
  visuals (target: match the 9/22 push's ToP gains).
- Numbers must render crisply — NANO-BANANA-2-TEXT, digits verbatim, no
  invented rates or extra figures.
- Hand them over in any format; I'll convert to WebP at the right sizes,
  wire the {{< visual >}} shortcodes, re-run gates, push, and verify live.
