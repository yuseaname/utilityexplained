# how-do-smart-meters-work — Visual Audit & Image Plan

## Hero
- File: /static/images/articles/how-do-smart-meters-work/how-do-smart-meters-work_hero_v2.webp | Viewed: A painterly 3:2 outdoor scene — a round dark-faced meter on a dark-green clapboard wall reads "035.42 kWh" in an LCD display, teal radio-wave arcs project toward a distant lattice cell tower over rooftops and foliage; no people present.
- Verdict: **SUITABLE-WITH-NOTES** — Topical fit is strong and literal: the article is about how smart meters measure and transmit, and the hero shows exactly a meter + a legible kWh register + transmission. Style notes: the painterly foliage/sky treatment and warm sunset palette drift from the flat ledger/blueprint bible (no grid-teal scaffolding, soft rendered surfaces), and the meter face carries an invented lightning-bolt badge. Not enough to demote — it is on-topic, uncluttered, people-free, and far closer to the bible than the smiling-person heroes removed elsewhere in this audit. If a regeneration budget appears, re-execute the same composition flat: ink-on-cream meter schematic, grid-teal radio arcs, amber on the one kWh readout. No urgency.

## Current state
- Visual count now (hero + in-body): 2 | in-body visuals:
  1. Product-box auto-render (B0C7B1LKDW Emporia Vue 3, inside the affiliate-wired `{{< product-box >}}` under "Benefits you actually get") → `/images/products/whole-home-energy-monitor.webp` — VIEWED: black rectangular monitor hub with four round clamp-on sensors, wiring harness, and coiled cable ending in an Ethernet-style connector; plain white background. VERDICT: EARNING — accurate to the real Vue 3 form factor (hub + clamp CTs), consistent with all 12 product cutouts in `data/product_images.yaml`, correct "Illustrative" alt, affiliate-wired by construction. KEEP.
- No `{{< visual >}}` / `{{< image >}}` editorials exist on this page.

## Recommended plan
- Recommended total (3-7): **4** — top of the 3-4 anchor for ~1.1K words; justified by the two post-SQ-055 load-bearing passages: the new AMR/AMI comparison table (earns a visualization) and the five-minute verification procedure (earns a worksheet). Hero + existing product visual supply the other two; anything more would decorate a compact page.

| # | Placement/section (exact heading) | Concept (style-bible-aligned) | Purpose | Format/orientation | Type | Affiliate-wired | Proposed filename |
|---|---|---|---|---|---|---|---|
| 1 | Hero — frontmatter `image:` (keep `hero_below_answer: true`) | **KEEP:** smart meter transmitting a reading (as viewed above) | clarify | 3:2 | illustrative | — | — (keep existing) |
| 2 | "How smart meters are different from analog meters" (immediately after the AMR/AMI table) | Three-station meter timeline: analog dial face → AMR one-way arrow to a drive-by van → AMI two-way arrows to a network node; flat cream surface, monospaced labels, hand-entered auditor note "two-way · 15-min intervals" | clarify | 16:9, rendered with `wide=` | illustrative | — | /images/articles/how-do-smart-meters-work/meter-evolution-strip.webp |
| 3 | "How to verify your smart meter is working" (after the 4-step list) | Verification worksheet reproducing the page's own procedure in monospace: meter read, second read 24 h later, subtraction, amber highlight on the daily-kWh delta, ledger note "compare to portal"; no invented utility branding | demonstrate-concept | 3:2 | illustrative | — | /images/articles/how-do-smart-meters-work/24h-meter-check.webp |
| 4 | "Benefits you actually get" (product box B0C7B1LKDW, visual exists) | **KEEP** existing auto-rendered product visual: Vue 3 monitor kit (hub + 4 clamp sensors), accurate to real product, "Illustrative" alt already in yaml | product-evaluation | ~3:2 (512×341, near-square card) | AI-product (illustrative product cutout) | **Y — inside `{{< product-box asin="B0C7B1LKDW" >}}`, auto-rendered, affiliate-wired by construction** | — (keep; no new file) |

- Keep-existing rows: #1 (hero KEEP) and #4 (product visual KEEP) count toward the total.
- Considered and cut: a privacy T-chart for "Privacy concerns (what utilities can and cannot see)" — the section is two short bullets that already answer it; a figure there would decorate, not clarify.
- Product-imagemery scope: row 4 is the ONLY product image on the page; it exists solely because the product box/link already sits there, per the binding rule. No other product concepts planned.

## Cohesion note
This is the only page in the 10-page set allowed product imagery, so its cohesion job is balance: the new editorial figures (rows 2–3) must speak the pure ledger bible — flat cream surfaces, monospaced kWh figures, one amber delta per figure — while the product cutout stays photographic-on-white inside its affiliate box, exactly like every other product card driven by `product_images.yaml` (plug-in meter, smart plugs, thermostats). The meter-evolution strip deliberately echoes the wide explanatory-strip compositions on sibling pages (time-of-use clock strips, kWh appliance ladder), and the verification worksheet previews the auditor-math style planned for the mcf-vs-ccf scenario stubs, so a reader crossing from this page into the gas-units or kWh pages meets one continuous house style: the meter as a ledger instrument, amber marking the one number that matters.
