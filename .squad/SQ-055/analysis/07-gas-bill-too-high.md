# APEX Reader-Experience Analysis — 07-gas-bill-too-high

## Execution Log (implemented by lieutenant, wave 2, 2026-08-29)

- Applied item 1: H2 relabeled to "Common causes, ranked by likelihood" (count-free option); frontmatter title untouched per rules.
- Applied item 2: Quick Answer unit paragraph trimmed to one sentence + existing MCF/CCF/therms and customer-charge links; the 1.037 conversion fact survives in the meter-tracking steps. Net ≈ −35 words.
- Applied items 3–5 + IG-1 + IG-2: triage line under the ranking H2; thermostat-evidence link (#4) after the DOE setback sentence; AFUE explainer bracket + link (#1) at cause #3; DIY-assessment link (#3) after the incense test and duct-leak symptom link (#5) on the ductwork bullet.
- Applied item 6 (IG-4): meter section compressed to the between-bills tracking steps + one pointer to the full dial-by-dial walkthrough (#2); 12-link retained at top of section. Net ≈ −120 words.
- Applied item 7: billing-cycle link (#6) inside cause #10.
- Applied item 8: Related-guides block (post-Sources, 13 entries, one duplicate-12 bullet) → "Related Reading" of 10 deduplicated entries with normalized one-line descriptions, now placed after the Next-step paragraph and BEFORE the FAQ, per house convention. Dropped in curation per IG-5: duplicate 12 entry, 03/04/10 as overlap trims; meter + 23 promoted.
- **Item 9 NOT executed — Commander veto stands:** the Nest box was not moved; verified still after faq-schema, before Sources, shortcode identical.
- Skipped: none besides vetoed item 9; no NEEDS-VERIFICATION items. Frontmatter untouched (`updated: 2026-08-29` already set). Net page delta ≈ −250 words.

**File:** content/blog/07-gas-bill-too-high.md · 3,716 words (longest in tier) · 10 H2 / 19 H3 · 8 tables · 25 internal links · 10 FAQs + faq-schema · 1 product box (Nest, B0D5BBYRJM) · aliases: why-is-my-gas-bill-so-high-in-winter/-in-summer · updated 2026-08-29
**Traffic (Rybbit baseline 2026-07-30 → 08-29, pre-change):** 56 visits · 63 pv · TOP 92.3s (longest read of the tier) · bounce 84% [RYBBIT]
**Analyst:** lieutenant, planning wave SQ-055. Analysis only — an implementation wave executes Edit Plans after Commander review.

---

## 1. Intent Model

**Primary intent [CONTENT][RYBBIT]:** winter-spike diagnosis — the gas bill arrived high, the reader is scared/annoyed about money, and wants the likely cause ranked, with dollar figures and the fix that pays. Evidence: title, Quick Answer (40–50% heating-driven, 2–3× winter), and the 10 ranked causes with savings.

**Secondary intent [CONTENT]:** the summer variant — the reader’s bill is high *out of season* and suspects something is quietly wrong (aliases point at exactly this audience). Served by cause #7 (gas leak), #11 (outdoor appliances), the summer FAQ, and the WNA explainer.

**Desired outcome [CONTENT]:** the reader can name their most likely cause, sanity-check it against their own bill (therms vs last year, HDD, period length), and either apply the matched fix or engage the utility with a specific complaint.

**Next logical need [INFERENCE]:** move from diagnosis to execution — how to actually do the fixes (meter tracking, DIY leak checks, thermostat scheduling), how to read the bill’s line items, and where the money relief is if the bill is genuinely unaffordable. Maps to the meter walkthrough, programmable-thermostat, duct-leak, billing-cycle, and LIHEAP pages.

**Journey note [RYBBIT]:** TOP 92.3s means readers genuinely work this article; 84% bounce means the page never converts that investment into a next step at the moment of need. The links exist (25) but are parked in the intro cluster, inside end-of-page FAQs, and in a 13-bullet dump *after* Sources — see §6.

## 2. First-Screen Verdict

Mobile sees: affiliate disclosure, Quick Answer (bolded percentage answer, fastest fix, cause triage, unit note, Next-step links), then the Quick-diagnosis four questions. [CONTENT]

- **Verdict: PASS — the strongest first screen of the assigned tier.** Answer in sentence one; dollar-anchored fastest fix in sentence two; the whole cause-space is previewed within a scroll. [CONTENT]
- **Friction [CONTENT]:** the third first-screen paragraph re-explains therms/CCF units — the page itself links MCF vs CCF vs Therms for exactly this. Two sentences of explainer here slow a triage-minded reader; it is short, but it is the only avoidable dip before Quick diagnosis.
- **No this-isn’t-for-me moment identified [INFERENCE on CONTENT + RYBBIT]:** the diagnostic block (*Did your therm usage actually increase?*) pre-empts the mismatch case; the 92.3s TOP says readers engage rather than abandon early.

## 3. Gap Analysis

### P0 — kills satisfaction
- **P0-1 · The mid-troubleshooting dead zone [CONTENT].** The article’s highest-momentum stretch — causes #1 through #5 (weather, thermostat, furnace, insulation/leaks, water heater), where the reader is actively forming their fix — carries essentially zero onward links to action pages: no link to the DIY energy-assessment guide at the air-leak incense test, none to the programmable-thermostat explainer inside the setback/tip section, none to the AFUE-rating explainer where AFUE numbers drive the replacement decision, none to the duct-leak symptom page, none to the meter-tracking page from the between-bills tracking steps. The links that exist mid-body serve billing-side causes #6/#10 and left-side infrastructure (#18, #19); the *fix* paragraphs — 1,500+ words — strand the reader. With bounce 84% despite a 92s read [RYBBIT], this is the mechanical explanation: readers finish (or bail within) the diagnosis and exit; nothing was on the road.

### P1 — degrades satisfaction
- **P1-1 · Count mismatch: 10 promised, 11 delivered [CONTENT].** H2 says 10 common causes; numbered H3s run 1–11 (outdoor gas appliances is #11). A trust defect on a page whose stock is trust—not fixed in title (frontmatter untouchable), fixable in the H2 wording or by relabeling #11 as a summer special-case callout.
- **P1-2 · Related-guides block breaks two house conventions [CONTENT].** (a) It sits *after* Sources — the house pattern puts Related Reading *before* the FAQ (exemplar what-is-ccf-on-a-water-bill). (b) Named Related guides, not Related Reading. Placement after Sources is where readers never go; 13 valuable links render dead.
- **P1-3 · Duplicate related entries [CONTENT].** Two bullets in that list point to the same URL (/blog/12-how-to-read-your-gas-bill/) under different titles (How to Read Your Gas Bill; Understanding Natural Gas Bill Charges) — visible sloppiness in the block that carries the page’s whole onward journey.
- **P1-2b · On-page meter micro-course duplicates the dedicated page [CONTENT].** How to read your gas meter (analog dial rules, digital readouts, 3-step tracking) compresses the 3,579-word how-to-read-gas-meter.md; duplication lengthens the tier’s longest article and splits the more thorough treatment.

### P2 — polish
- **P2-1 [CONTENT]** Quick Answer’s second paragraph and the unit paragraph can shed ~40 words; the linked units page carries them.
- **P2-2 [CONTENT]** Affirmation markers: the cost table already carries honest estimate framing — no filler risk here; minor.
- **P2-3 [CONTENT]** Related-guides bullets use inconsistent description styles (some have descriptions, some not) — normalize in the relocation edit.

## 4. Momentum & Structure

- **Heading usefulness: strong [CONTENT].** Ranked causes + HDD worked example + seasonal tables give the scanner real nav; H3 numbering inside causes is individually navigable.
- **Paragraph bulk: mixed [CONTENT].** Causes read fast; the three mega-tables (seasonal shares, month-by-month, savings) plus two visuals give the eye landing points; the meter section’s inline how-to and the fixed/variable/budget subsections are the sag points.
- **Repetition: real [CONTENT].** Meter instructions duplicate the meter page; the seasonal-comparison tables partially restate cause #1 and the intro’s 2–3× claim; the 12-URL appears three times total (intro, Next step, two related bullets).
- **Filler: low [CONTENT].** Additions are data and dollar figures, not throat-clearing; length is earned, though the owner’s no-bloat bar means the plan must be net-negative on words.
- **Scannability: 8/10.** Visual shortcodes, bolded leads, ranked structure — genuinely good. The failures are routing (P0-1/P1-2), not readability.

## 5. Information Gain Plan

The page is long; every addition must displace or pay for itself. New factual claims: **none** (all reuses of verified on-page or verified sibling content).

- **IG-1 · Three-minute triage row (small).** Under 10 common causes, ranked by likelihood, one line: *short on time? check #1 (weather), #2 (thermostat), #10 (period length) first — the three most common explanations.* Pure reflow of the page’s own ranking claim; cuts perceived length.
- **IG-2 · AFUE definition-in-place (small).** One bracketed line at cause #3’s first AFUE mention pointing to the site’s AFUE/SEER/HSPF explainer (verified target) — no new facts, removes jargon friction.
- **IG-3 · Triage-to-fix table row additions — none.** The What-to-do pattern already works; do not add.
- **IG-4 · Meter micro-panel (net-negative, medium).** Compress the on-page How to read your gas meter to its 3-line between-bills tracking steps + one link to the full meter walkthrough (verified). Recovers ~150 words and removes duplication; the reader needing dial-by-dial detail gets the better page.
- **IG-5 · Related Reading curation (net-neutral, small).** In the relocated block (Edit Plan #2), deduplicate the double-12 entries and keep the strongest 8–10; identical content, honest list length, house name.

## 6. Internal Journey

All targets verified present under content/blog/ with draft:0 in .squad/content-metrics.json (verified this run). [CONTENT, verified]

1. **what AFUE ratings actually mean** → content/blog/afue-vs-seer-vs-hspf-vs-cop.md — cause #3 (furnace efficiency decline), at the 92%→80–85% passage. The replacement decision hinge should not rely on in-line parentheticals [CONTENT].
2. **the full dial-by-dial meter walkthrough** → content/blog/how-to-read-gas-meter.md — in How to read your gas meter (pairs with IG-4 compression). Serves the between-bills tracker’s next need [CONTENT].
3. **run a full DIY energy assessment** → content/blog/47-check-energy-leaks-home-diy.md — cause #4, immediately after the incense-stick quick test. The incense test IS the assessment page’s method; the link completes the amateur-inspection arc [CONTENT].
4. **do programmable thermostats really cut heating bills** → content/blog/do-programmable-thermostats-cut-heating-bills.md — cause #2, thermostat tip paragraph (the DOE 7–10°F setback sentence). The natural evidence-check before a $25–$250 purchase [CONTENT].
5. **if uneven rooms are the symptom** → content/blog/duct-leaks-symptoms-hvac-running-all-day.md — cause #4’s ductwork bullet. Captures the reader whose leak test pointed indoors [CONTENT].
6. **why the billing period makes the bill look bigger** → content/blog/23-utility-billing-cycle-explained.md — cause #10 (billing cycle length/estimated readings). Sister page already links *toward* this family; closes the loop. Must ship with 23’s plan for symmetry [CONTENT].

**Curation (not new links):** replace the duplicated 12-bullet in Related Reading with either the meter page or the billing-cycle link from #6; keep LIHEAP and the utility-assistance thread [CONTENT]. **Note on target depth:** every proposal is draft:0 and verified; gas-customer-charge-explained and other draft:1 pages were never candidates [verified this run].

## 7. CTA Fit

**Verdict: keep — the existing single box stays; one optional reframe needs Commander sign-off.**

- Current state: one Nest Learning Thermostat product box (B0D5BBYRJM), siting between faq-schema and Sources; zero inline affiliate links. [CONTENT]
- Doctrine check [DOCTRINE]: AFFILIATE-PLACEMENTS-2026-08-28.md names 07-gas under EXISTING placements: *1 box — correct as-is. 3.6k words + one relevant box = restraint that reads as honesty.* The verified-ASIN inventory confirms B0D5BBYRJM is real. Keep it; do not add a second box (the page already has 10 FAQs and 25 links — more chrome is the failure mode of this page type).
- **Reframe option (flag for Commander, not in default plan):** the box currently renders after the FAQ block, past structured output, where TOP-based scroll behavior suggests a minority of readers arrive. Moving the identical box up to cause #2 (thermostat settings — the section that recommends exactly this device class; the box line even says the retrofit applies there) converts the box from footer to moment-of-need without touching copy or ASIN. This is doctrine-compliant (problem-language, fix-context) but is a discretionary move — doctrine marked the existing placement correct-as-is, so the implementation wave should only do it on explicit instruction.
- No crisis-intent conflict: affordability readers are served by the LIHEAP exit (kept), not by products [DOCTRINE trust rule].

## 8. Edit Plan

Ordered, section-level, targeted. No wholesale changes; frontmatter, slug, aliases untouched.

1. **[small | H2 10 common causes]** Renumber-safe fix for the 10-vs-11 mismatch: relabel the H2 to Common causes, ranked by likelihood (count-free), or fold #11 under #1 as a seasonal sub-cause. Do not touch the frontmatter title.
2. **[small | Quick Answer]** Trim the therm/CCF unit paragraph to one sentence + the existing MCF/CCF/therms link (P2-1). Net −30 words.
3. **[small | cause #2]** Add thermostat-page link (#4) after the DOE setback sentence; add IG-1 triage line under the ranking H2.
4. **[small | cause #3]** Insert AFUE explainer link (#1) + IG-2 bracket line.
5. **[small | cause #4]** Add links #3 and #5 at the ductwork and incense-test points respectively.
6. **[medium | How to read your gas meter]** Execute IG-4: keep the between-bills tracking steps, replace dial instructions with a 1-line pointer + link #2. Net −120 words.
7. **[small | cause #10]** Add link #6 to the billing-cycle page (ships together with 23’s plan).
8. **[medium | page tail]** Move Sources-block order: FAQ (+faq-schema) stays, then Related Reading (renamed, deduplicated per IG-5) placed BEFORE the FAQ block, then Sources. House convention restored.
9. **[small | optional, Commander-gated]** Reposition the Nest box from post-faq-schema to the end of cause #2 (see §7). Identical shortcode; siting-only change. Default plan leaves it as-is per doctrine.

**Sequencing:** 1–2 (consistency + first screen), 3–7 (mid-body journey, the P0 fix), 8 (conventions), 9 optional last. Every item independently shippable. Net word delta ≈ −150 + additions (triage line, bracket line, related-row) ≈ −80 net — satisfies the owner’s no-bloat rule.

## 9. Dual Reasoning + Self-Critique

**Reader test** — *I came here because my gas bill is scarily high and I need to know why and what to do first.* The page already wins the diagnosis half — ranked causes, dollars, degree-day math, safety warnings [CONTENT] — and the 92.3s TOP proves the reader works it [RYBBIT]. What the plan adds is not more explanation but movement: links at the moment each cause proves itself, a meter page for the tracker, a billing-cycle page for the artifact case, a thermostat-evidence page before the purchase.READ → ACT. The reader finishes either with a fix in motion or a confident handoff — not a 92-second dead end.

**Business test** — trust peaks where the article converts diagnosis into action (thermostat, insulation, water heater). The Nest box is the single correct product and its restraint reads as honesty [DOCTRINE]; the moment-of-need reposition (item 9) is the only conversion-relevant move and is deliberately gated because the doctrine called the current placement correct. The rest of the CTA value flows onward to the action pages (how-to-lower…, energy-leaks) which already carry boxes — this page’s job is to send qualified, problem-diagnosed readers there.

**What an expert editor would criticize about this plan:**
1. The 10-vs-11 fix (item 1) is cosmetics if the frontmatter title still says 10 — the editor will flag that the H2/frontmatter mismatch survives; acknowledged (frontmatter is out of scope) and the H2 fix still removes the visible on-page contradiction.
2. IG-4 compresses the meter section while cause #11 referencesBetween-bills tracking — the implementer must confirm the compressed section still contains the tracking steps before deleting dial detail.
3. Six new links into an already link-dense page (25) risks champagne-stop clutter; the plan defends each as moment-of-need, but the wave should not also add inline-footer link rows into the seasonal tables.
4. Moving Related Reading before the FAQ slightly reduces FAQ-schema visibility distance — trivial, but the editor will ask why the block should be above a schema-marked FAQ at all; answer: house convention is explicit and the exemplar demonstrates it.
5. The plan adds no FAQ entries and no new tables — right call for a 3,7-word page, but a bonhead editor might miss that; the self-defense is the owner’s explicit no-padding rule and the net-negative word delta.