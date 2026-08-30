# SQ-058 — Product-Image Visual QA

**Date:** 2026-08-29  ·  **Dir:** `static/images/products/`  ·  **Scope:** 9 distinct `.webp` files, form-factor check against each ASIN's product identity.

## Verdict

**All 9 images PLAUSIBLE — each matches the real product's form factor.** No file is wrong-shaped for its mapping, and none misrepresents the product (no trust risk found). Clean sweep.

## Per-file table

| # | File | Product | What I see | Form-factor verdict | Trust risk |
|---|---|---|---|---|---|
| 1 | `plug-in-energy-meter.webp` | Plug-in energy meter | White passthrough plug with a 2-socket receptacle + bar-chart LCD + 4 buttons | ✅ Correct — plug-in meter reads usage via an inline socket | None |
| 2 | `smart-water-shutoff.webp` | Smart water shutoff | Brass ball valve body + gray electric actuator w/ blue LED + knurled end caps | ✅ Correct — motorized shutoff valve | None |
| 3 | `smart-plug.webp` | Smart plug (3 ASINs share) | White passthrough plug, single button, blue LED | ✅ Correct — smart plug form factor | None (see note) |
| 4 | `premium-smart-thermostat.webp` | Premium smart thermostat | Dark round sensor, glass ring, heat/cold/leaf icons + status dots | ✅ Correct — premium round thermostat | None |
| 5 | `level-2-ev-charger.webp` | Level-2 EV charger | White EVSE unit, coiled cable, Type-1 (J1772) connector, green charge LED | ✅ Correct — Level-2 home EVSE | None |
| 6 | `whole-home-energy-monitor.webp` | Whole-home energy monitor | Three current transformers + control box w/ green LED + Ethernet cable + velcro coil | ✅ Correct — CT-based whole-home monitor kit | None |
| 7 | `learning-thermostat.webp` | Learning thermostat | Round thermostat face, 72°F, mode ring, heat/cold/leaf icons | ✅ Correct — learning thermostat | None |
| 8 | `water-leak-detectors.webp` | Water leak detectors | One hub + three round water-drop sensors w/ teal LED | ✅ Correct — leak-detector sensor set | None |
| 9 | `programmable-thermostat.webp` | Programmable thermostat | White rectangular LCD w/ up/down buttons + 4 preset buttons + rotary | ✅ Correct — programmable thermostat | None |

## Notes

- **3 ASINs share `smart-plug.webp`.** I could not verify the ASIN→image mapping from disk; the single shared image is a **coverage/mapping flag** (the Commander's note says all 12 wired ASINs have yaml + on-disk files, so coverage is complete), not a form-factor defect. Worth confirming each of those 3 ASINs genuinely targets a smart plug and is not double-mapped to a different device.
- **Image quality:** all 9 are clean product renders on black backgrounds, sharp, correctly lit. No placeholder, no stock-photo mismatch, no mislabeled object.
- **No trust risk:** every file depicts the product it claims. No file is too generic or wrong-shaped for its mapping.
