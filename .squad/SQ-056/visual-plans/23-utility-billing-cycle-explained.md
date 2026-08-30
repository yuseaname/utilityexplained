# 23-utility-billing-cycle-explained — Visual Audit & Image Plan

_Audited 2026-08-29 by Lieutenant (SQ-056). All image descriptions grounded in read_image this run. ~1.6K words, 9 H2s, 8 tables (incl. worked example + normal-vs-second-look gate). No product boxes/links on this page._

## Hero

- **File:** `/images/articles/23-utility-billing-cycle-explained/23-utility-billing-cycle-explained_hero_v2.webp` (frontmatter `image:`) | **Viewed:** Flat-illustrated utility statement lying on a wooden desk under a black magnifier, whose lens holds an amber-highlighted "Electricity Charge" line with "$" marks; desk props include a green-shaded lamp, a fountain pen, a coffee mug, and a potted plant; generic abstracted bill (gray greeked lines, lightning-bolt emblem, faint leaf icon), no real utility name, no people.
- **Verdict: SUITABLE-WITH-NOTES.**
  - **(a) Topic relevance:** Strong — a statement under magnification is exactly the article's act (reading the period/line items closely), and the amber "one line that matters" treatment matches both the style bible and this page's audit-the-dates intent.
  - **(b) Style consistency:** Mostly on-bible — flat ledger surface, teal/cream/ink palette, no gradients, no 3D, no people, amber reserved for one highlighted line. The warm wood desk + lamp/mug vignette is more "cozy editorial" than "engineering blueprint," but it stops short of stock-photo people; acceptable for a hero whose job is scene-setting.
  - **(c) Suitability:** Keep as hero. One soft note: the magnified line reads "Electricity Charge" while the article covers electric, gas, and water periods alike — generic, not a real mismatch, but a future v3 could label it neutrally ("Service period").

## Current state

- **Visual count now (hero + in-body): 1** (hero only; 0 in-body).
- In-body visuals: none.
- **Orphan on disk, not referenced in the markdown:** `static/images/articles/23-utility-billing-cycle-explained/custom_inline.webp` — **Viewed:** photorealistic gray-desk stock shot of a tilted, blurred "Utility Bill" with garbled/unreadable type, coffee mug and pen. Off style-bible (photographic, illegible, no grid/teal/amber system) and referenced nowhere — **do not wire it in**; candidate for cleanup (out of SQ-056 write scope).

## Recommended plan

- **Recommended total (3-7): 4** — justified: at ~1.6K words the anchor is 3-4; this page leans to the top of the band because 9 H2s / 8 tables make it the densest short page in the set, so each figure must *clarify or demonstrate*, never decorate. 1 keep + 3 new.

| # | Placement/section (exact heading) | Concept (style-bible-aligned) | Purpose | Format/orientation | Type | Affiliate-wired | Proposed filename |
|---|---|---|---|---|---|---|---|
| 1 | **KEEP — hero (frontmatter, above Quick Answer)** | Magnifier-on-statement scene as viewed; amber "one line that matters" highlight | Emotional-context / topic signal | Intrinsic ratio as shipped (≈16:10 flat illustration) | editorial | N/A — no product | _(existing `_hero_v2.webp`)_ |
| 2 | **`## Why Cycle Lengths Vary`** — intro, before `### Meter-Read Schedules` | One-line horizontal ledger: a calendar month (28 gray day-cells) vs the actual billing period (two teal meter-read flagposts spanning 33 days), amber on the two read-date flags; annotation hand-entered: "read date → read date ≠ calendar month" | Demonstrate-concept: the article's core idea (period = read-to-read span) as one glanceable strip | 16:9 wide (`wide=`) | illustrative | N/A | `read-to-read-timeline.webp` |
| 3 | **`### Worked Example`** (inside `## The Long-vs-Short-Month Bill Math`) — ahead of the January/February table | Two-bar ledger per bill: Jan 28 days / Feb 33 days, equal-height daily-usage bars (30 kWh/day), amber on the identical daily-average row; mono figures only, using the page's own worked numbers (840 kWh / $130.20 vs 990 kWh / $153.45) | Demonstrate-concept: shows why the raw totals differ while daily usage is flat — the page's single most important math | 3:2 | illustrative | N/A | `daily-average-comparison.webp` |
| 4 | **`### How Estimated Reads Affect Your Bill`** (inside `## Estimated-vs-Actual Read Interaction`) — after the read-status table | Two-cycle timeline: Jan–Feb bar drawn as an outlined/dashed "estimated" block, Feb–Mar solid "actual" block, amber wedge between them labeled "correction lands here"; mono labels, no utility names, no invented dollar amounts | Clarify: the estimate/true-up lump that otherwise looks like a usage spike | 3:2 | illustrative | N/A | `estimated-vs-actual-tru-up.webp` |

**Not planned (earn-their-place rejects):** the "How to Check Your Cycle Dates" methods table and the normal-vs-second-look gate already carry their content as tables; icon rows or a re-drawn gate card would duplicate, not clarify. No product images exist on this page, so no affiliate-wired rows.

## Cohesion note

This page's set (magnifier hero + read-to-read timeline + daily-average ledger + true-up timeline) forms an "auditor's walkthrough": find the dates, divide honestly, then explain the lump. All three new figures are flat illustrative ledgers on cream with faint grid-teal scaffolding and mono figures — the same visual grammar as 07-gas's ranked-causes and HDD charts — so scrolling from this page's hero (a warm flat-illustrated scene, the site's editorial face) into schematic-teal figures will feel like moving from cover to inside pages of the same ledger book. Amber stays reserved for the single decisive element per figure (read flags, the flat daily average, the correction wedge), matching the house rule and the sibling pages. Nothing here touches product imagery; the page's commercial role is purely contextual links.
