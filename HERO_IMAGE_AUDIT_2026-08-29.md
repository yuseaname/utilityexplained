# Top 30 Hero Image Audit — 2026-08-29

Scope: the 30 highest-traffic blog guides in the refreshed Rybbit 30-day snapshot (2026-07-30 through 2026-08-29).

## Shared display correction

The previous shared hero rules forced a 340px-tall crop. Every audited hero now uses its intrinsic aspect ratio:

```css
.hero-figure-frame { height: auto; max-height: none; aspect-ratio: auto; }
.hero-figure-frame .hero-img {
  position: static;
  width: 100%;
  height: auto;
  max-height: none;
  object-fit: contain;
}
```

This keeps the full focal area visible, avoids stretching, and lets each image scale to the article column on desktop and mobile. “Shared full-ratio hero” in the table refers to this exact treatment. Standard placement is the existing in-flow hero slot immediately before the article body; the restored guide uses the header slot directly under its summary.

## Implementation record

| # | Page URL | Current hero status | Action taken | Recommended asset / concept | Placement / display |
|---|---|---|---|---|---|
| 1 | `/blog/how-to-lower-electric-bill-complete-guide/` | Present, relevant (16:9) | Reframed | EIA-style home-energy-cost bar chart | Shared full-ratio hero |
| 2 | `/blog/30-sudden-spike-in-electricity-bill-no-usage/` | Present, relevant (16:9) | Reframed | Electric panel, bill, and meter display | Shared full-ratio hero |
| 3 | `/blog/water-meter-running-when-no-water-used/` | Present, relevant (3:2) | Reframed | Active water meter when household use is off | Shared full-ratio hero |
| 4 | `/blog/what-is-ccf-on-a-water-bill/` | Present, relevant (3:2) | Reframed | “1 CCF = 748 gallons” explainer | Shared full-ratio hero |
| 5 | `/blog/28-utility-reconnection-fee-explained/` | Present, relevant (3:2) | Reframed | Utility technician restoring service at a meter | Shared full-ratio hero |
| 6 | `/blog/06-water-bill-too-high/` | Present, relevant (3:2) | Reframed | Household faucet and water-use scene | Shared full-ratio hero |
| 7 | `/blog/how-sewer-charges-work-on-your-water-bill/` | Present, relevant (3:2) | Reframed | Home-to-treatment-plant sewer-charge diagram | Shared full-ratio hero |
| 8 | `/blog/water-meter-leak-indicator-explained/` | Present, relevant (3:2) | Reframed | Labeled water-meter leak-indicator dial | Shared full-ratio hero |
| 9 | `/blog/05-how-to-lower-utility-bills/` | Present, relevant (3:2) | Reframed | Homeowner adjusting a smart thermostat | Shared full-ratio hero |
| 10 | `/blog/03-why-is-my-electric-bill-so-high/` | Present, relevant (3:2) | Reframed | Reader investigating a higher electric bill | Shared full-ratio hero |
| 11 | `/blog/23-utility-billing-cycle-explained/` | Present, relevant (3:2) | Reframed | Utility statement under a magnifier | Shared full-ratio hero |
| 12 | `/blog/07-gas-bill-too-high/` | Present, relevant (3:2) | Reframed | Household gas use, meter, and furnace scene | Shared full-ratio hero |
| 13 | `/blog/electric-bill-breakdown-understanding-line-items/` | Present, relevant (3:2) | Reframed | Electricity-dollar allocation chart | Shared full-ratio hero |
| 14 | `/blog/25-utility-bill-taxes-fees-franchise-charges-explained/` | Asset present but suppressed (3:2) | Restored existing asset | Layered utility-bill charge breakdown | Header slot below summary, then shared full-ratio hero |
| 15 | `/blog/average-utility-bills-by-state-2026/` | Present, relevant (3:2) | Reframed | U.S. utility-cost comparison map | Shared full-ratio hero |
| 16 | `/blog/19-utility-bill-surcharges-and-riders-explained/` | Present, relevant (3:2) | Reframed | Itemized statement showing bill add-ons | Shared full-ratio hero |
| 17 | `/blog/mcf-vs-ccf-vs-therms-on-gas-bill/` | Present, relevant (3:2) | Reframed | Household gas use with visible meter context | Shared full-ratio hero |
| 18 | `/blog/why-your-electric-bill-keeps-rising-2026/` | Present, relevant (3:2) | Reframed | Reader comparing a rising electric bill | Shared full-ratio hero |
| 19 | `/blog/stormwater-fee-on-water-bill-explained/` | Present, relevant (3:2) | Reframed | Rainwater entering a marked storm drain | Shared full-ratio hero |
| 20 | `/blog/how-do-smart-meters-work/` | Present, relevant (3:2) | Reframed | Smart meter transmitting a reading | Shared full-ratio hero |
| 21 | `/blog/18-fuel-adjustment-charge-on-utility-bill-explained/` | Present, relevant (3:2) | Reframed | Reader reviewing a fuel-adjustment line item | Shared full-ratio hero |
| 22 | `/blog/average-water-usage-per-person/` | Replaced (3:2) | Generated and wired a new hero | Water bill → billing days → household size → calculator | Shared full-ratio hero |
| 23 | `/blog/49-demand-charges-electricity-bill-explained/` | Present, relevant (3:2) | Reframed | Demand peak flowing from meter to household load | Shared full-ratio hero |
| 24 | `/blog/why-did-my-water-bill-suddenly-increase/` | Present, relevant (3:2) | Reframed | Reader investigating an unexpectedly high water bill | Shared full-ratio hero |
| 25 | `/blog/27-utility-connection-fee-explained/` | Present, relevant (3:2) | Reframed | Customer reviewing a service-start statement | Shared full-ratio hero |
| 26 | `/blog/08-time-of-use-electricity/` | Present, relevant (3:2) | Reframed | Peak versus off-peak electricity comparison | Shared full-ratio hero |
| 27 | `/blog/26-utility-deposit-explained/` | Present, relevant (3:2) | Reframed | Utility deposit notice under magnification | Shared full-ratio hero |
| 28 | `/blog/how-to-read-electric-meter/` | Present, relevant (3:2) | Reframed | Close view of a digital electric meter | Shared full-ratio hero |
| 29 | `/blog/01-how-to-read-your-electric-bill/` | Present, relevant (16:9) | Reframed | Electric meter and bill ready for comparison | Shared full-ratio hero |
| 30 | `/blog/how-to-read-a-water-meter/` | Present, relevant (3:2) | Reframed | Reading a water meter in its service box | Shared full-ratio hero |

## Verification

- Desktop: 30 of 30 rendered heroes verified present, loaded, un-stretched, and matched to their natural image ratio.
- Mobile (375px): 30 of 30 rendered heroes verified within the viewport and matched to their natural image ratio.
- The hero images do not cause the existing horizontal overflow found in 12 article pages at 375px; those are separate content-layout issues and were intentionally left out of this hero-image repair.

## New image asset

- `static/images/articles/average-water-usage-per-person/average-water-usage-per-person_hero_v3.png`
- Created with the built-in image generation tool from a purpose-written editorial-infographic prompt; no text, logos, or watermarks.
