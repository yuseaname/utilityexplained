# how-to-read-electric-meter — Visual Audit & Image Plan

_Audited 2026-08-29 by Lieutenant (SQ-058). All image descriptions grounded in read_image this run. ~1,100 words, 10 H2s, 1 in-body table (two-readings subtraction example), one ordered list (dial procedure), three bullet lists (digital, smart-meter, verify-bill). No product embeds on the page (grep-verified this run)._

## Hero

- **File:** `/images/articles/how-to-read-electric-meter/how-to-read-electric-meter_hero_v2.webp` (frontmatter `image:`) | **Viewed:** Flat-illustrated round gray meter socket mounted on dark-teal horizontal house siding; the meter's LCD reads **012345 kWh** in glowing digits, with a small amber lightning-bolt emblem above the display and a gold padlock hasp at the base; to the left, a golden-hour suburban backdrop — dusk sky, tree canopy, tan house with lit windows — rendered in the same flat illustration style; soft bevel highlights on the meter casing, gentle glow around the LCD.
- **Verdict: SUITABLE-WITH-NOTES.**
  - **(a) Topic relevance:** Strong — it is literally a meter with a legible reading and a kWh label; the page's subject on screen one.
  - **(b) Style consistency:** Mostly on-bible — teal/cream/ink family, flat suburban scene, no people; the beveled metal shading and LCD glow edge toward soft 3D, and the **amber is spent on the lightning emblem (decoration) rather than a data element** — a small breach of the amber-reserved-for-the-one-line-that-matters rule, softened by the glowing amber-adjacent digits.
  - **(c) Suitability:** Keep. It is a scene-setter, not a teaching figure, and it does that job well. Minor notes for any future v2: move amber onto the reading itself, and note the hero shows only a *digital* meter while the page teaches dial and digital equally — acceptable for a hero, but the dial instruction below deserves the in-body figure (row 1).

## Current state

- **Visual count now (hero + in-body): 1** (hero only).
- In-body visuals: **0** — no `{{< visual >}}` shortcodes (grep-verified this run). The brief's `dial-meter-reading.webp` belongs to the water-meter sibling (`how-to-read-a-water-meter`, confirmed by grep) — nothing on disk for this page beyond the hero, so the dial figure below must be built new and kept visually distinct from the water sibling's clock-dial plate.
- **Orphans on disk: none.**

## Recommended plan

- **Recommended total (3–7): 3** — justified: ~1,100 words sits at the band's low end; the page is action-dense but short, and its three retention-critical moments (the dial procedure, the subtraction, the bill-verification) each take exactly one figure. 1 keep + 3 new would over-plate a 1K-word page; 3 total keeps every image earning its scroll.

| # | Placement/section (exact heading) | Concept (style-bible-aligned) | Purpose | Format/orientation | Type | Affiliate-wired | Proposed filename |
|---|---|---|---|---|---|---|---|
| 1 | **`## How to read an analog dial electric meter`** — directly after the 3-step ordered list | **The dial sequence plate (the page's action demo).** Flat schematic of a 4-dial electric meter face on cream, labeled "kWh": pointers set mid-span, alternating-direction arrows over the dial pivots (**direction alternation is the visible point** — small teal arrows L-R / R-L), the dial whose pointer sits between two numbers amber-highlighted with a hand-entered auditor note "between 5 and 6 → record the lower: 5"; a mono strip below reads out the resulting 4-digit sequence like a ledger line. Electric context only (kWh label, no flow-direction hand) — deliberately distinct from the water sibling's clock-dial figure while sharing its one golden rule | Action moment: the reader is about to stand in front of a real dial meter; this shows the two failure modes (between-numbers, right-dial-not-passed) resolved in one look | 16:9 wide (`wide=`) | illustrative | N/A | `electric-dial-meter-sequence.webp` |
| 2 | **`## How to calculate your usage from two readings`** — directly after the subtraction table | **Two readings, one subtraction.** Two identical flat meter faces side by side, displays in mono: 48,120 → 48,540; a teal arrow carries the pair into a three-line ledger box where **420 kWh** is boxed amber, matching the page's own worked numbers; hand-entered note "same meter, 30 days apart" | Residual dense spot: makes the table's subtraction visual for readers who skip tables; the figure uses the page's own figures so prose, table, and image agree | 3:2 | illustrative | N/A | `two-readings-subtraction.webp` |
| 3 | **`## How to verify your bill using the meter`** — after the bullet list, before the utility-billing-cycle link paragraph | **Meter vs statement check.** Simple two-column reconciliation ledger: "my read, Aug 28 — 48,510" over "bill's current read, Aug 31 — 48,540," a small amber delta note hand-entered: "3-day gap ≈ timing, not error"; the bill row carries a teal "Actual" read-type stamp paralleling page 01's actual-vs-estimated plate | Pre-exit moment: the reconciliation is the page's payoff skill; a figure here holds the reader through the closing links and earns the scroll into Related Reading | 3:2 | illustrative | N/A | `meter-vs-bill-check.webp` |

**Affiliate verdict — deliberately NONE.** Kill A Watt P4400 (B00009MDBU) is on the verified inventory, but this page is about the **utility meter**: its verify path is meter-to-statement, and a plug-in monitor cannot verify a meter reading or a bill — it is a different instrument for a different job (appliance-level draw). Forcing it here would trade the page's authority for a box. Its defensible homes are the appliance-spike and usage pages (03 / 30 / 11), not this one. This is the packet's "judge strictly" case, judged: no box, no affiliate row.

**Not planned (earn-their-place rejects):** a digital-meter figure would merely redraw one sentence ("write down the full number") while duplicating the hero's digital meter; the smart-meter section stays text because a portal mock-up would invent UI the utility doesn't ship; the FAQ's dryer-cycle test is where a Kill A Watt *would* creep in — rejected above.

## Cohesion note

This page owns the **instrument side** of the tier's auditor binder: page 01's anatomy plate labels the statement fields, and this page's row-3 figure shows the reader checking those exact read rows against the physical meter — a deliberate two-page callback rendered in the same cream/grid-teal/mono grammar (teal stamps on "Actual," amber on the single decisive element per figure: the between-numbers dial, the 420 kWh box, the timing delta). The dial plate shares its record-the-lower-number rule with the water sibling's `dial-meter-reading.webp` — one house method across utilities — while staying electric-specific in dial count, kWh labeling, and orientation arrows. Hero amber-discipline note (emblem, not data) is the tier's one soft inconsistency and is corrected automatically in every new figure here.
