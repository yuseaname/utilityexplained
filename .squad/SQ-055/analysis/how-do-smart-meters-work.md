# APEX Reader-Experience Analysis — how-do-smart-meters-work

**Squad:** SQ-055 planning wave · **Author:** lieutenant · **Date:** 2026-08-29
**Baseline (Rybbit 2026-07-30 → 08-29):** 25 visits / 27 pv · TOP 19.9s · bounce 92% [RYBBIT]
**File:** `content/blog/how-do-smart-meters-work.md` — read in full this run. Page already carries `hero_below_answer: true` (verified in frontmatter and the site's flag list — the Aug-10/28 layout remediation reached this page).

---

## Execution Log (implemented 2026-08-29 by lieutenant)

- S1 applied: double answer merged — QA now carries definition + interval mechanism; "The short answer" H2 deleted; time-of-use link retargeted into a QA capability bullet.
- S2 applied: both `{" "}` artifacts stripped (bill line item guide anchor; Benefits anchor).
- S3 applied: analog/AMR/AMI bullet cluster replaced with comparison table; summary sentence kept.
- S4 applied per Commander ruling: ONE Emporia Vue 3 box (asin B0C7B1LKDW), problem-language anchor "See your own usage in real time", verified doctrine copy in description, at end of "Benefits you actually get"; no second box.
- S5 applied: 5 journey links — why-did-my-utility-bill-go-up-this-month (QA), 30-sudden-spike (Benefits), 11-understanding-kwh-usage (verify step 4), 04-hidden-fees (opt-out), phantom-power-draw (Benefits, after box).
- S6 applied: Related Reading moved before FAQ (house convention), duplicate complete-guide entry dropped, smart-plugs entry kept, FAQ reordered to lead with RF + bill-jump, IG-3 interval-data FAQ added.
- S7 applied: why-did-my-utility-bill-go-up link added to QA closing line.
- S8: hero_below_answer already set; meta description untouched (proposal-only, out of scope).
- Skipped: IG-5 (opt-out fee ranges, [NEEDS-VERIFICATION]) not executed — no verified fee figures on disk.
- Self-check: all internal links resolve to verified slugs; raw-HTML heading idiom preserved; no new facts beyond the approved box copy; faq-schema is the final content element before Sources.

## 1. Intent Model

- **Primary intent:** conceptual/curiosity — "how does the thing on my house actually work?" This is the only assigned page that is NOT a bill-emergency decode: the visitor often isn't holding a problem, they're satisfying curiosity (sometimes post-installation, sometimes meter-adjacent anxiety). [INFERENCE — consistent with the mission brief and the page's title promise]
- **Secondary intent:** reassurance/decision — "should I trust it / can I opt out / did it change my bill?" The title's parenthetical "(And Should You Trust Them?)" and the on-disk sections ("Are they accurate?", "Privacy concerns", "Can you opt out?", "Common misconceptions") are built for exactly this second reader. [CONTENT]
- **Desired outcome:** reader can explain the mechanism in one sentence AND knows what to do if they distrust a reading (compare meter↔bill, request a meter test). [CONTENT]
- **Next logical need:** see their OWN usage data (which the article says the portal can show, and which a home energy monitor delivers directly) → then the diagnosis path (why is my bill high) if the data surprises them. [INFERENCE]
- **Metric read:** TOP 19.9s + 92% bounce on a curiosity page ≈ the definition gets read, the tail doesn't hold. Curiosity intent self-selects fast exits, but 19.9s is roughly half the engaged class (37.1s sibling) — the plan should compress the path to mechanism and give one reason to stay. [RYBBIT]

## 2. First-Screen Verdict

- **Layout:** `hero_below_answer: true` is set — the hero renders below the answer, so the mobile first screen is **title + Quick Answer**. Structurally, this page already has the correct first screen; do not re-flag it. [CONTENT]
- **QA quality:** opens with a bolded direct answer ("A smart meter is a digital electricity meter that can provide utilities and customers with more detailed electricity-use data than a basic monthly total.") — passes the 2-sentence test. [CONTENT]
- **But the QA's four bullets are hedge-mush:** "Can provide more detailed use data / May report remotely / Can support time-varying programs / Can help you compare usage patterns" — four capability disclaimers, no mechanism. A reader whose question is *how does it work* gets insurance language first. The word "work" appears in the title, not in the QA. [CONTENT]
- **The "this isn't giving me what I came for" point:** immediately after the QA, the very next H2 — "The short answer (what a smart meter actually does)" — RE-ANSWERS the same question with the same definitional move ("A smart meter is a digital device that records... usage in short intervals"). The reader who scrolls past the QA to find the mechanism finds the answer repeated, in a section titled "short answer" that is itself a second answer. [CONTENT — duplication documented in §3]
- Net verdict: answer reachable in 2 sentences + scroll: **YES** — but with a duplicated second answer and no working-mechanism hook in the first screen, momentum bleeds at exactly the wrong spot for a curiosity reader.

## 3. Gap Analysis

**P0 — kills satisfaction**
- **P0-1 · Double answer, delayed mechanism.** "Quick Answer" defines the device; H2 "The short answer (what a smart meter actually does)" re-defines it ("records your electricity usage in short intervals (often 15 minutes to 1 hour) and sends that data to your utility"). Two answers back-to-back — the title's actual question (how it WORKS) is answered twice at definition depth, and the reader needs two more H2s ("How smart meters are different", "How smart meters measure and transmit") before the mechanism arrives. On a 19.9s page this duplication is the likeliest exit amplifier. [CONTENT]
- **P0-2 · Literal rendering garbage in link anchors.** Raw-HTML JSX artifacts `{" "}` inside two link anchors (lines 92 and 131 — the "bill line item guide" link in "Are they accurate?" and the "bill spikes" link in "Benefits you actually get"). Hugo does not evaluate JSX: these render as visible `{" "}` text inside the underlined link. Two of the page's links show code fragments. [CONTENT — grep verified: exactly 2 occurrences]

**P1 — degrades satisfaction**
- **P1-1 · Related Articles block violates house convention and contains a duplicate.** It sits AFTER `{{< faq-schema >}}` at the very end of the file (house convention: "Related Reading" bulleted, BEFORE the FAQ), and lists `/blog/complete-guide-understanding-utility-bill/` twice under two different titles ("A Practical Workflow for Understanding Your Utility Bill" and "Understanding Your Utility Bill"). [CONTENT]
- **P1-2 · Zero monetization despite the mission's flagged natural fit.** 0 product boxes, 0 affiliate links [CONTENT]. The reader's literal next need — *see my own usage data* — is exactly what a home energy monitor does (doctrine's verified Emporia Vue 3 `B0C7B1LKDW`, already scripted for `03-why-is-my-electric-bill-so-high` in Tier 1). This is not decoration: the product continues the article's own promise that the utility controls what data reaches you.
- **P1-3 · Fee references dangling with no off-ramp.** The "Can you opt out?" section warns of "a one-time setup charge and a monthly meter reading fee" but links nowhere, while the QA's post-install advice says "do not assume the cause" and links nothing for the full changed-bill walkthrough — both moments name a next question the site can answer. [CONTENT]

**P2 — polish**
- FAQ ordering leads with "Can smart meters catch electricity theft?" — the least-asked homeowner question; the common ones (RF, bill jump) sit below. [CONTENT]
- No table anywhere (metrics index: 0 tables) despite "analog vs AMR vs AMI" being a natural 3-row comparison. [CONTENT]
- Raw-HTML sections carry heavy source indentation (harmless in render, maintenance hazard). [CONTENT]

## 4. Momentum & Structure

- **Heading skeleton is traveler-friendly for the trust-reader:** what it does → vs analog → how it measures → accuracy → privacy → benefits → verify yourself → opt out → misconceptions → FAQ → Sources. The trust/privacy/misconceptions trio matches the title's second half. [CONTENT]
- **Duplication is the momentum killer:** QA ↔ "short answer" (same definition); "how-they-measure" ↔ "smart-vs-analog" (both cover kWh and intervals); two "Benefits" bullets restate QA hedge-bullets. [CONTENT]
- **Paragraph bulk:** fine — short mobile-friendly paragraphs, bolded lead-ins. [CONTENT]
- **Scannability verdict:** structure lucid, sections skimmable — the problem is not scannability, it's that the scan double-serves the answer and under-serves the mechanism. One merge + one table fixes the flow.

## 5. Information Gain Plan

Additive, zero padding; nothing new factually except where flagged.

- **IG-1 · "Analog vs AMR vs AMI" comparison table** (3 rows × 3 cols: how it reads, data direction, what you notice). Every cell restructures claims already on-page in the bulleted list — no new facts; gives mobile a scannable anchor. [CONTENT]
- **IG-2 · One-sentence mechanism chain in QA** — "Meter measures → stores an interval reading → transmits it in short radio bursts → your portal/bill aggregates it." Assembled entirely from sentences already on-page (measure + transmit sections). Gives the curiosity reader the "how" in the first screen. [CONTENT]
- **IG-3 · FAQ addition: "How do I see the interval data myself?"** — answer: the utility's account portal first (already asserted on-page), plus the meter-display 24-hour check from "How to verify." Cross-structure answer, zero new claims. [CONTENT]
- **IG-4 · Product-context gain (business-side):** one paragraph in "Benefits" naming what real-time whole-home data unlocks — the Vue 3 box (below) is the hardware form of that exact sentence. No new factual claims beyond the doctrine's verified copy ("16 circuit-level sensors, real-time app data"). [CONTENT]
- **IG-5 · OPTIONAL, [NEEDS-VERIFICATION]:** typical opt-out fee ranges by state — reader will hunt for them; no verified figures on disk; do not add without verification.

## 6. Internal Journey

All targets verified on disk this run (file present under `content/blog/` + slug frontmatter confirmed in a full site inventory). Five new journey links:

1. **"Why your bill went up this month — every likely cause"** → `content/blog/why-did-my-utility-bill-go-up-this-month.md` — placement: "Are they accurate?" ¶2 (the correction-not-error paragraph). *Why:* that is the reader mid-worry; the QA's "do not assume the cause" advice needs its dedicated walkthrough one hop away. [target verified]
2. **"What a sudden kWh spike with no behavior change means"** → `content/blog/30-sudden-spike-in-electricity-bill-no-usage.md` — placement: "Benefits you actually get" daily-charts bullet (beside or replacing the generic "bill spikes" link to `03`). *Why:* the chart-curious reader's sharpest next question. [target verified]
3. **"What a month of kWh looks like"** → `content/blog/11-understanding-kwh-usage.md` — placement: "How to verify your smart meter is working," step 4 ("Compare that daily kWh to your utility portal and bill"). *Why:* the verify-steps reader immediately needs context to judge their number. [target verified]
4. **"Every charge on your utility bill, explained"** → `content/blog/04-hidden-fees-utility-bill.md` — placement: "Can you opt out?" ("a monthly meter reading fee"). *Why:* names the fee class the sentence introduces; keeps the trust-reader answering questions on-site. [target verified]
5. **"Phantom power draw: the load interval data reveals"** → `content/blog/phantom-power-draw-explained.md` — placement: "Common misconceptions" (after the rates bullet) or "Benefits" beside the monitor paragraph. *Why:* curiosity reader → curiosity-adjacent answer; keeps the session on-site after the concept resolves. [target verified]

Fix (counted as layout cleanup §3 P1-1, not new journey links): move Related Articles up before the FAQ, dedupe the double `complete-guide-understanding-utility-bill` entry, keep one retitled line. [target verified on disk]

## 7. CTA Fit

- **Reader's intent stage:** pre-diagnosis curiosity — not crisis, not definition-only. The reader is deciding whether to trust a device and (secondarily) wondering what its data could do for them. That is the doctrine's sweet spot: *the product IS the reader's next step*, not decoration.
- **Existing placements:** none on page. [CONTENT]
- **Doctrine fit:** AFFILIATE-PLACEMENTS Tier 1 already scripts the verified Emporia Vue 3 (`B0C7B1LKDW`, "16 circuit-level sensors, real-time app data") for the bill-diagnosis page — the same product serves this page's "Better usage insight" promise without new claims. This page's reader is EARLIER in the funnel than `03`'s — so the box goes at the END of "Benefits you actually get" (the section that already argues daily/hourly visibility is valuable), with a problem-language anchor like "See your own usage in real time", never product-first. One box only; no smart-plug companion here (doctrine reserves the diagnosis→action pair for `30-spike`).
- **Verdict: REFRAME — add ONE Emporia Vue 3 box at end of "Benefits you actually get."** Anchor must stay problem-language per doctrine. If the Commander prefers strict restraint on conceptual pages, NONE - informational is the acceptable fallback and the journey links (§6) carry the session — the page's trust role argues against stacking.

## 8. Edit Plan

Ordered, section-level, targeted; the skeleton survives. No wholesale rewrite.

| # | Change | Section | Size |
|---|---|---|---|
| S1 | Merge the double answer: extend the QA paragraph with IG-2's mechanism chain; **delete** the duplicated "The short answer (what a smart meter actually does)" H2, folding its interval detail (dedupe — already stated in QA's second sentence); retarget the time-of-use link from the deleted section into the QA capability bullet. | Quick Answer + short answer | medium |
| S2 | Strip the two `{" "}` artifacts (lines 92, 131) from link anchors; convert those raw-HTML anchors to markdown links while there. | accuracy + Benefits links | small |
| S3 | Replace the analog/AMR/AMI bullet cluster with the 3-row comparison table (IG-1); keep one summary sentence. | smart-vs-analog | small–medium |
| S4 | Insert the Emporia Vue 3 box at the end of "Benefits you actually get" using the doctrine's verified language and a problem-language anchor; one paragraph, one box. | Benefits | small |
| S5 | Insert the 5 journey links (§6). | per §6 | small ×5 |
| S6 | Rebuild end-matter: move Related Articles BEFORE `{{< faq >}}` as "## Related Reading" bullets; drop the duplicate complete-guide entry; append IG-3 FAQ; reorder FAQs to lead with RF and bill-jump. | end matter | small–medium |
| S7 | Add the why-did-my-utility-bill-go-up link to the QA's closing "do not assume the cause" line (one sentence after "...what meter-testing process applies to your account."). | Quick Answer | small |
| S8 | Frontmatter: no change needed — `hero_below_answer: true` already set. Meta description PROPOSAL (out of scope, proposal only): current description is compliance-flavored ("Learn what a smart meter can report..."); suggest one that answers the title's two-part promise, e.g. "How a smart meter records and reports your kWh, how it differs from an analog meter, and what the data means for your bill." | frontmatter | proposal |

Net word delta: ≈0 (dedupe offsets additions); 8 edits, all targeted.

## 9. Dual Reasoning + Self-Critique

**Reader test — "I came here because I want to understand the meter on my house (and whether to trust it)."** Post-plan: the first screen defines the device AND states the mechanism chain; the analog/AMI comparison is a table scannable on a phone; trust questions stay where they are (accuracy, privacy, misconceptions all preserved); and the reader who wants more gets the same story one level deeper (kWh numbers, interval data, bill walkthrough) one hop away. The 19.9s reader gets the "how" they were promised — earlier and once. [RYBBIT + CONTENT]

**Business test — what natural action follows trust?** For THIS reader: "I'd like to see that data myself." That sentence is exactly what a home energy monitor sells. The Vue 3 box converts the article's own benefit claim into its hardware form, at the funnel stage where curiosity converts. One box only; if it performs, extend the pattern elsewhere, don't stack here.

**What an expert editor would criticize about this plan:**
1. **S1 merges the two answers but leaves the QA's hedge-bullets untouched** — an editor would compress the four "Can provide / May report" disclaimers to two. I kept them: they are the post-audit sourcing posture, and rewriting them risks softening audit-driven precision. Explicit taste call for the Commander.
2. **The Vue 3 box on a conceptual page is the plan's boldest call.** The doctrine's NOT-A-FIT table bans definitional pages, and this page is definitional-PLUS-insight (the insight half argues for the box). If the reviewer weighs the definitional half heavier, choose NONE and keep the journey links; the page still improves.
3. **FAQ-theft-first ordering** (§3 P2) is my editorial judgment, not metric-backed — no scroll data proves readers stop there.
4. **The `{" "}` fix (S2)** must be verified in rendered HTML (build + view-source), not just source markdown, before claiming the artifacts are gone. Recommend the implementation wave run a `hugo` build and grep the rendered page for `{" "}` as the acceptance test.
5. **Uncorrelated check requested:** have a second seat (different model family) re-derive §6 link-target existence and confirm the S1 merge doesn't orphan the time-of-use link slug (`/blog/08-time-of-use-electricity/` — verified live this run, but the edit moves it).
