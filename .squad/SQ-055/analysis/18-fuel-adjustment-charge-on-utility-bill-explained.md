# Reader-Experience Analysis — 18-fuel-adjustment-charge-on-utility-bill-explained

## Execution Log

- Applied Commander-approved items 1–6 and 8; item 7 (description proposal) executed as approved. Frontmatter: `updated:` set 2026-08-28 → 2026-08-29; description updated; no other fields touched.
- Item 8: `{{< affiliate-disclosure >}}` chip added under the frontmatter (family consistency — ship as ruled).
- Item 1: `## Related Reading` added (19-mechanism, 24-delivery-vs-supply, 11-kwh-usage, 12-gas-bill-charges — all resolve).
- Item 2 (body links): 24 linked in the verify-table "Related items" row; 19 linked in the post-table placement paragraph; 11 linked on the "Metered usage" checklist item.
- Item 3: compare dimensions bulletized into a 7-item checklist; why-did-my-utility-bill-go-up link added at the section close.
- Item 4: 3-entry FAQ block added under `{{< faq >}}` shortcodes + single `{{< faq-schema >}}`, ordered body → Related Reading → FAQ → faq-schema → Sources. FAQ facts drawn solely from on-page material (rate basis/usage basis; rider-mechanism vs line-item distinction; the five provider questions).
- Item 5: symbolic worked example shipped with NO numbers — italic formula line (tariff fuel rate × usage basis = fuel-adjustment line) placed after the Identify table, per Commander ruling.
- Item 6 (trim): the "record the line exactly" instruction now appears in Quick Answer + Identify section; the Compare-section duplicate opening was absorbed into the checklist intro.
- Item 8 (description): now reads "…provider-specific calculation — how to identify it, verify it against the tariff, and compare it to prior bills." No title/slug changes.
- **Journey #4 correction:** the 43-understand-natural-gas-bill-charges target was NOT linked as a new URL — that path exists only as an **alias of 12-how-to-read-your-gas-bill**; the Related Reading bullet points at the canonical 12 slug instead. Zero unresolved links.
- Skipped: none — no NEEDS-VERIFICATION items shipped or pending (the numeric worked example remains excluded per the NEEDS-VERIFICATION gate; symbolic form only).

---

# Reader-Experience Analysis — 18-fuel-adjustment-charge-on-utility-bill-explained

SQ-055 planning wave · Rybbit last-30 baseline: 24 visits, 29 pv, TOP 25.7s, bounce 96% [RYBBIT]. **THIN page: ~560 words live** (metrics says 396 words, dated pre-rewrite: live file read is authoritative). Full file read this run.

## 1. Intent Model

- **Primary intent:** the reader's electric (sometimes gas) bill carries a "fuel adjustment" / "fuel cost recovery" / "PSCCO"-type line and they want (a) what it is, (b) why it changes month to month, (c) whether it's why their bill jumped [TITLE + TAGS + INFERENCE].
- **Secondary intent:** self-verification — "is my fuel-adj line computed right?" The page's whole workflow (record exact line → pull tariff → compare to prior bill → 5 provider questions) is a verification kit [CONTENT].
- **Desired outcome:** reader stops attributing a bill jump to fuel costs without comparing statements; knows the charge is provider-defined; walks away with a provider-question list. [CONTENT]
- **Next logical need:** given the site's answer pattern, the reader either (a) wants to see *their* fuel line calculated as an example, (b) wants the surrounding bill's line map (delivery vs supply vs riders vs taxes), or (c) wants to know what to do about a high bill overall. Today the page offers ZERO onward affordances: no Related Reading, no body links, nothing. [CONTENT + INFERENCE]

Engagement context [RYBBIT]: TOP 25.7s is HIGH for this set — with 96% bounce + 29pv/24visits (1.2 pv/v), this reads as genuine reader attention to a page that *ends* without guidance: the mission packet calls this "info-gain is legitimately additive;" the page is data-complete but journey-empty. TOP 25.7s with zero exits = reader finishes the SHORT page, wants more, page offers none. [INFERENCE]

## 2. First-Screen Verdict

Mobile: affiliate-disclosure (not in the file — wait: **no affiliate-disclosure chip on this page [CONTENT, full read]** — a family inconsistency only worth noting, not fixing) → hero below answer (flag true) → "## Quick Answer" → one ~90-word para with the bolded definitional answer + 3 caveat clauses + a DOE footnote line.

The Quick Answer handles the test: first bolded sentence does answer "what is this" within 2 sentences + a partial scroll [CONTENT]. The fold-order flag is present and correct. **Bail-risk point: END of the Quick Answer itself** — after≈3 screens, the reader has the answer, the page has 4 more sections (Identify / Compare bills / Questions for the Provider) — but no early affordance tells them the page HAS the table and the workflow below. The 25.7s TOP suggests they DO scroll (good), but the 96% bounce says once done they leave.* Zero exits = zero captures. [INFERENCE]

Minor scratch: the title says "Fuel Adjustment Charge"; the Quick Answer handles-name variability as *the* first content move. Elegant, but for a reader whose line says "PSCCO" or "Fuel Cost Recovery" with zero context, no same-screen labelcue exists (the table below has "Charge name / The provider's label and tariff reference" — that row is one screen down). [INFERENCE]

## 3. Gap Analysis

- **P0 — Zero internal links.** The page has no body links, no Related Reading, no end-matter exits (metrics agrees: internal_links 0 at 08-28 stale). The reader finishes a solid 560-word verification kit and is dropped at "## Sources" with no next step. This is the ONE page of the four where the journey gap is total. [CONTENT]
- **P1 — No FAQ block.** The site's template family (19, 25, exemplar CCF) carries FAQ + faq-schema close; 18 lacks both. FAQs — one of the strongest additions for a thin page — are missing entirely. [CONTENT]
- **P1 — No worked example.** The page's core math fact ("rate basis × usage basis") is stated only as an abstract checklist; a 2-line symbolic example ("billed usage × the tariff's per-unit fuel rate = the line, bill-end") would rebuild reader confidence without new numbers. Any real dollar/rate figure is NEEDS-VERIFICATION — excluded from this plan. [CONTENT + INFERENCE]
- **P1 — "Compare Bills Before Drawing a Conclusion" section ends flat** — 3 dense sentences + a DOE cite, when that section is the page's differentiator (compare-the-bills discipline). One structural beat: pull the compare-dimensions into a bullet list (billing days / metered usage / estimated status / rate-plan version / line-item rates / credits / one-time items) — these ARE on-page as a folded comma-list today. [CONTENT]
- **P2 — "Questions for the Provider" list is strong but unanchored** — if the reader prints/emails it, the request lives mid-page with no portable cue. Minor. [INFERENCE]
- **P2 — Word-count thinness ~560** — legal per this page's family (see 17: 353 words, 20: 417, 22: 379, 24: 339 — the whole review-family ships short); the fix is additive ONLY in the form of FAQ + links, not a long-form rewrite. [CONTENT]

## 4. Momentum & Structure

- **Heading usefulness: good for a short page.** Four action-verb H2s (Quick Answer / Identify the Exact Charge / Compare Bills Before Drawing a Conclusion / Questions for the Provider). Better-than-family-average verb headings. [CONTENT]
- **Paragraph bulk: fine.** Short paras, two tables. The one density flag is the single Quick Answer paragraph. [CONTENT]
- **Filler: none visible. Nothing says nothing. For a 560-word page, that's the point.** [CONTENT]
- **Repetition: "record the line exactly" idea appears in Quick Answer + Identify section + Compare section — three tellings of one instruction family; acceptable for a how-to, honest trim opportunity in the Compare section.** [CONTENT]
- **Scannability verdict: clean, complete, and a dead end.** This page is 90% house-pattern compliant and 100% journey-broken. [INFERENCE]

## 5. Information Gain Plan (useful-only; the thin-page exception the mission packet explicitly allows)

1. **IG-1 (small, on-page restructure):** bulletize "Compare Bills Before Drawing a Conclusion" into a 7-item checklist (billing days / metered usage / estimated status / rate-plan version / line-item rates / credits / one-time items) — list composed from the sentence ALREADY in the file. Zero padding, pure restructure. [CONTENT]
2. **IG-2 (medium): 3-entry FAQ block, facts 100% from on-page material:**
   - "Why does my fuel adjustment change when my usage didn't?" → tariff-based rate resets, usage basis (on-page §2: rate basis + effective dates + usage basis).
   - "Is the fuel adjustment charge the same as a rider?" → the rider-is-the-mechanism/charge-is-the-line distinction already cross-linked from page 19's FAQ (mirror fact; the 19 page FAQ states it verbatim; quoting it here is a family-crosstalk, not a new claim).
   - "How do I get the exact rate for my account?" → the 5-question provider list, condensed. [CONTENT]
3. **IG-3 (small, additive — NEEDS-VERIFICATION gated): a symbolic worked example.** 2 lines, variables only ("label rate × billed usage = line amount, from the tariff, not from the label"). **NEEDS-VERIFICATION if the owner wants an actual illustrative tariff rate** (e.g., a real published per-kWh fuel-factor) — no number ships without a source. The symbolic form satisfies the reader without any new claim. [CONTENT + gated]
4. **IG-4 (small, additive):** one-sentence "where this sits in the bill" pointer to the line-item map (Journey #2 below) placed right after the Identify table.
5. **Do NOT add:** rate tables (any state), fuel-price history, grid-fundamentals essay, or a conservation pitch. The page's power is its narrowness. The one legal exception would be a product box — and the CTA verdict below says why that's not the play. [INFERENCE]

## 6. Internal Journey (all targets existence-verified under content/blog/ this run)

Five links; the page currently has zero.

1. **Anchor:** "surcharges and riders: the mechanism behind metered add-on lines"
   **Target:** `/blog/19-utility-bill-surcharges-and-riders-explained/` (live; sibling; already links *to* 18 twice)
   **Placement:** "Identify the Exact Charge" — after the table's "Calculation" row explanation.
   **Why:** mechanism-vs-line-item is the family's core distinction; 19's FAQ already states it (“the fuel cost adjustment rider is the mechanism; the fuel adjustment charge is the line item”)—the reciprocal anchor closes the loop the sibling already opened. [CONTENT]
2. **Anchor:** "delivery vs supply charges — where the fuel line fits"
   **Target:** `/blog/24-delivery-charge-vs-supply-charge-utility-bill/` (metrics draft:0; read-confirmed live this wave)
   **Placement:** "Identify the Exact Charge" — the "Related items" row of the verify table.
   **Why:** the reader staring at "fuel adjustment" usually asks whether it belongs to supply or delivery; this is the exact map. [CONTENT + INFERENCE]
3. **Anchor:** "how to read the kWh usage on your bill"
   **Target:** `/blog/11-understanding-kwh-usage.md` (metrics draft:0; live)
   **Placement:** Compare-Bills section bulletized checklist, on the "metered usage" item.
   **Why:** step 2 of the compare workflow is "metered usage" — the 11 page is the site's usage-reading primer. [CONTENT]
4. **Anchor:** "understanding natural gas bill charges (if your fuel line is on gas)"
   **Target:** `/blog/43-understand-natural-gas-bill-charges/` (metrics draft:0; live)
   **Placement:** Quick Answer tail OR Related Reading; recommend end-matter placement to keep the electric focus of the Quick Answer intact.
   **Why:** the fuel-adj family exists on gas bills too; the 43 page is the gas equivalent. [CONTENT]
5. **Anchor:** "why did my utility bill go up this month?"
   **Target:** `/blog/why-did-my-utility-bill-go-up-this-month/` (file verified in blog listing)
   **Placement:** the "Compare Bills" section's conclusion, as the reader's next diagnostic step if the compare *doesn't* reconcile.
   **Why:** the reader who confirms their fuel-adj line moved — or suspects something else — needs the general bill-increase diagnostic; this is the canonical entry. [CONTENT + INFERENCE]

Optional 6th (only if the owner approves Related Reading with 5 entries): "every charge on a utility bill, explained" (`/blog/04-hidden-fees-utility-bill/`) as the map-view exit. Prefer 5 — page is thin; end-matter should not outweigh body. [INFERENCE]

## 7. CTA Fit — **NONE - informational**

Affiliate doctrine: this page belongs in the NOT-A-FIT family (definitional charge explainers — "no product answers the question; a box here is decoration"). A Kill A Watt box would be decoration pretending the fuel-adj line can be metered at home (it can't — it's a tariff line, not a device measurement). No existing boxes; nothing to keep/reframe. The honest action after trust = verify with the provider + explore the family pages. [CONTENT-backed INFERENCE per doctrine]

The closest-fitting product on the whole verified list would be a usage-monitor (Emporia Vue), but the *page's* need is "verify the line against the tariff", not "measure your watts." A tool box here would sell a solution to a question the reader isn't asking yet. Hard no. [INFERENCE]

## 8. Edit Plan (ordered; the thin-page additive exception the packet grants this URL)

1. **[medium | end matter] Add `## Related Reading` (bulleted, before any FAQ additions, house convention) with 4 bullets: 19-surcharges (mechanism), 24-delivery-vs-supply (location), 11-kwh-usage (usage), 43-gas-charges (gas family). One-line descriptors, house phrasing. Zero new claims.**
2. **[small | body placements]** Add the three body-context links: 19 (post-table, row-anchored), 24 (Related-items row), 11 (metered-usage item) per §6. Keep bodies at ≤1 link per section — house-exemplar norm.
3. **[small | "Compare Bills…"]** Bulletize the 7 comparison dimensions (IG-1) + add the why-did-my-utility-bill-go-up link at the section close (Journey #5) — the ONE high-momentum anchor the page currently misses.
4. **[small | FAQ block]** Add the 3-entry FAQ under `{{< faq "…" >}}` shortcodes + `{{< faq-schema >}}` after Related Reading, matching the exemplar order (FAQ → faq-schema → Sources; check exemplar placement of the Sources sheet after faq-schema — **pattern parity check for the implementer, since 18 currently has FAQ a the very end after Sources with NO FAQ — order after this edit should be: body → Related Reading → FAQ → faq-schema → Sources**).
5. **[small | symbolic worked example — DOES NOT SHIP A NUMBER]** Insert a 2-line worked example (IG-3) in symbolic form ("label rate from tariff × billed usage = fuel-adj line on your bill") directly below the Identify table. If the owner later supplies a verified numeric example, replace the symbolic line (NEEDS-VERIFICATION gate; no number proposed here).
6. **[small | trim]** Collapse the "record the line exactly" instruction family from 3 tellings to 2 (keep in Quick Answer + Identify table; drop the duplicate sentence opening "Compare Bills...") — net word-count change: negative.
7. **[PROPOSAL ONLY — frontmatter description, Commander-approved]** Suggest a one-line upgrade with the reader's true job: "…how to identify it, verify it against the tariff, and compare it to prior bills." Proposes no title/slug change.
8. **[small | affiliate-disclosure]** Add the standard `{{< affiliate-disclosure >}}` chip under the frontmatter for family consistency (all three sibling pages carry it; 18 is the only one without).

## 9. Dual Reasoning + Self-Critique

**Reader test.** "I came here because I need to know what this fuel-adjustment line is and whether it's charging me fairly." Post-plan: first screen unchanged (already answer-first and correct); NEW: after the verification kit completes, 4 exits (rider mechanism, bill-position, usage, gas-cousin) plus an FAQ answering the two questions the body raises but never states ("why does it change", "how do I get my rate"). The thin page stops being a dead end. TOP may RISE or stay: that's the right trade for a page whose reading time is already high and whose exits are zero.

**Business test.** The affiliate answer is NONE - informational, and firmly so — the reader's verification task has no product surface; the CTA-fit case the doctrine makes explicitly. Business value: journeys per session on a page already capturing 25.7s of attention and converting to zero family reads today. If the owner strongly wants one honest product hook, the land would be a single inline `{{< amazon >}}` on the meter-read page — but the reader on THIS page isn't meter-diagnosing; the correct end-state is: none.

**What an expert editor would criticize:**

1. **The additive plan grows the page from ~560 to ~750–800 words.** For the mission that's the sanctioned info-gain case; an editor could still counter "all five sections were fine; you're deferring the thin-page problem through links and FAQ rather than solving it with substance." True — the honest structural fix is a real numeric example or a state rate-comparison table, both requiring NEW sourced facts. I refuse it here (NEEDS the verification the mission can't do), and the symbolic example + FAQ is the best within-wave approximation. The broader fix is a follow-up sourcing mission, not this plan.
2. **The 3-FAQ count is deliberately modest;** an editor will ask why not 5. Because each FAQ would need either new facts or a restate of existing ones; 3 keeps the block non-padding. Revisit only as part of the sourcing follow-up.
3. **The affiliate-disclosure-chip addition (#8) is house-consistency, not reader-impact** — swapping it in when ZERO affiliate links exist on-page could theoretically trigger disclosure-vs-content mismatch ("why is this chip here?"). Counterpoint: sitewide disclosure near links is the doctrine's own baked-in rule and the chip renders as a single unobtrusive line. Fine either way; flagged rather than silently included.
4. **The ordering recommendation in #4 flips the current ending** (today: FAQ→Sources absent, body→Sources). The house example (CCF page) ends: FAQ → faq-schema → Related-Reading-in-QA area → Sources. The plan conforms; the implementer must double-check short-code rendering order on the live theme before shipping.
5. **The symbolic worked example is the plan's weakest reader-impact item** — an editor could call it decoration. My defense is that it operationalizes the page's only math concept without inventing a number. If the owner prefers zero additions, cut #5 first; the other 4 moves carry the plan.
6. **Recommendation to Commander (next mission):** this page is the family's best candidate for the one legitimate additive upgrade the owner might greenlight: a *sourced* worked example using a real published tariff figure (needs new evidence mission + a verified source, NEEDS-VERIFICATION as written). Worth listing in the APEX backlong rather than forcing it here.
