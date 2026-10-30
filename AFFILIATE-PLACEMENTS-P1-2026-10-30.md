# P1 Placement Ledger — 2026-10-30 (utilityexplained)

Ranking basis: relevant traffic (Rybbit 30d, Oct 1–30) × buying intent × product fit.
Every product below is already in the site's verified bench (AMAZON-PRODUCT-DOSSIER-2026-08-30 + live re-checks 2026-10-30).

## Placed (with rationale)

| Page (30d pv) | Product (ASIN) | Why this placement belongs |
|---|---|---|
| how-sewer-charges-work-on-your-water-bill (230) | Govee leak 5-pack (B0DQLFC3Q6) | Article's own "Compare Like With Like" tells readers a hidden leak inflates usage-based sewer bills. The sensor confirms the diagnosis the text recommends — placed at exactly that decision point. |
| complete-guide-understanding-utility-bill (163) | Kill A Watt P4400 (B00009MDBU) | Step 2 ("verify meter and usage") ends at the wall the article itself names: the bill totals usage but never breaks it down per appliance. The meter is the direct next step. |
| 01-how-to-read-your-electric-bill (140) | Kill A Watt P4400 (B00009MDBU) | "What a kWh Means" teaches the unit; the meter converts that understanding into per-appliance dollars. Tapo P110M mentioned inside the description as the always-on alternative. |
| who-responsible-water-leak-before-after-meter (97) | Flume 2 (B08DX6MP8X) | The freeze-warning section explicitly recommends "a meter-mounted flow monitor" — Flume 2 IS that rung (straps on the existing meter). Truest text-to-product match on the page. |

## Comparison modules (decision-stage, no new products)

| Page | Module | Rationale |
|---|---|---|
| how-to-lower-electric-bill-complete-guide (1296) | Situation table (don't-know / HVAC-dominates / know-the-hogs) above the 3 tool boxes | Vision audit: 3 identical stacked boxes → banner blindness. Table routes by reader situation first. |
| 06-water-bill-too-high (527) | 3-rung ladder table (point sensors / meter monitor / monitor+shutoff) above the Govee+Flume boxes | The ladder content already existed as prose+links; the table makes the rungs comparable at a glance. |
| 30-sudden-spike (724) | "match tool to depth" table above the Kill A Watt + Tapo boxes | Spike readers arrive mid-diagnosis; the table picks the measurement depth before they scroll to boxes. |

## Deliberately NOT placed (examined and rejected — no count-padding)

| Page (pv) | Reason |
|---|---|
| water-meter-box-full-of-water (99) | Repair/maintenance intent (dig out, repair riser) — no honest Amazon product helps the next decision. |
| average-utility-bills-by-state-2026 (96) | Data/citation asset — monetizing it would undermine the neutrality AI engines and snippet tables reward. |
| average-water-usage-per-person (92) | Informational benchmark; no decision moment. |
| how-to-read-electric-meter (71) | The meter itself answers the question; a product adds nothing. |
| how-to-dispute-utility-bill (65) | Dispute intent — products are irrelevant to the next step (documentation + utility contact). |
| tankless-vs-tank-water-heater (57) | Genuine decision page, but water heaters are not honestly Amazon-adjacent (big-ticket, local install); forcing accessories would be irrelevant placement. |
| moving-utilities-checklist (54), can-utility-shut-off-service (44), others <50 pv | Traffic too thin to justify editorial insertion this wave. |

## Price bands (new system)

- All bands verified against LIVE Amazon listings today (2026-10-30, curl fetches of /dp/ pages; two ASINs via secondary price markers): Kill A Watt $29.99 buybox → "$25–35"; Govee $69.99 → "$60–75"; Flume ~$199.99 → "$195–225"; Vue 3 kit $199.99 → "$190–210"; Nest 4th-gen $279.99 → "$250–290" (stock caveat: "Only 1 left" at check); Kasa KP115 $15.99 → "$14–18"; Tapo P110M 2-pack $12.00–19.99 → "$12–22".
- Storage: data/product_prices.yaml (band + checked date + provenance). Rendering: product-box shortcode shows a band ONLY while ≤75 days fresh — stale bands silently stop rendering; a stale price can never display. Maintenance: scripts/check_price_bands.py monthly (portfolio rhythm).
- Markdown comparison tables intentionally carry NO hardcoded prices (they can't auto-expire); bands live only on the auto-gated boxes.

## Cart-link compliance (label truthing)

- Basis: Amazon's PA-API documentation expressly documents the Add to Cart form (AssociateTag required) and the Operating Agreement's Qualifying Purchase definition explicitly covers "adds a Product to shopping cart … no later than 89 days" — the mechanism is permitted.
- Fix: 8 cart-enabled boxes previously showed neutral "Check price on Amazon" copy while pre-loading Amazon's cart. All such overrides removed; cart boxes now render their default truthful label "Add to cart on Amazon" (heat-tape ×2, door-draft ×2, smart-thermostats ×4). Standard boxes keep "Check price on Amazon" with /dp/ links.

## Quick Answer promotion (sitewide template change)

- layouts/partials/qa-promote.html + design-system.css + single.html hook. Client-side DOM reorder (no content rewrites across 140 files): the #quick-answer section is wrapped in a styled box and moved ABOVE the TOC; the affiliate disclosure moves to just after the TOC (full text untouched). Crawler/no-JS source order unchanged; #quick-answer anchors still resolve.
- Desktop duplicate-TOC ended: when the sticky rail exists (has-rail), the in-column TOC hides at ≥1024px; mobile keeps the in-column TOC.
