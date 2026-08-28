# UtilityExplained — Agency Growth Audit & Amazon Associates Pivot Blueprint

**Client:** utilityexplained.com (Amazon Associates store ID: `utexplained-20`)
**Engagement:** Audit & enhance existing approved site — no rebuild
**Date:** 2026-08-27 · **Prepared by:** THE SQUAD (SQ-044) — Commander synthesis over 9 specialist workstreams
**Evidence tiers:** [T1] Commander-verified on disk/production · [T2] multi-seat corroborated · [T3] single-seat lead — verify before acting

---

## 1. Executive Summary

**Verdict: FIX.** The corpus is a genuinely strong affiliate foundation with an engaged-growth
traffic curve — but the Amazon pivot is currently **non-compliant in production**, **mis-configured**,
and **operationally stalled**, and engagement metrics are moving the wrong way. Nothing here requires
a rebuild; everything material is fixable in 30 days.

The five facts that define the engagement:

1. **You are earning nothing from links that are already live — and they violate policy.** Two
   production pages carry Amazon links built with the **wrong associate tag (`litwd-20`**, not your
   `utexplained-20`**)** — any click revenue is being attributed elsewhere. One of them
   (`30-sudden-spike`) has **no affiliate disclosure at all** in production. [T1]
2. **The site cannot ship fixes.** Repository and production have drifted: the #1 traffic page
   (123 sessions/wk) is flagged `draft: true` with a 301 in the repo — yet still returns **200 live**;
   the AdSense removal shipped to production but 89 stale build pages in `public/` still carry dead
   ad scripts. Until the build→deploy pipeline is re-established, no audit recommendation can land. [T1]
3. **Traffic is growing on one engine.** 860 sessions last 7 days (+32% WoW), but ~68% is
   Bing-ecosystem and **Google is 2.6%** of referrers vs ~86.6% US market share — an inversion that
   reads as Google suppression, consistent with the August AdSense rejection ("low value content"). [T1/T2]
4. **Engagement is failing intent.** Bounce 91.3% (target <70%), 1.10 pages/session (target 1.9),
   62s duration. Links placed into content that readers abandon will not convert; engagement repair
   is the revenue prerequisite, not a nice-to-have. [T1]
5. **The monetization plumbing already exists and is unused.** `product-box` / `amazon` shortcodes
   read one config value (`hugo.toml → params.amazon_tag`). One line fixes every future link
   sitewide. The single product-adjacent article (smart plugs) contains zero links. [T2]

**Recommended sequence:** stop the bleeding (compliance + tag + deploy) → fix the top 15 traffic
pages' engagement → monetize only remediated, source-linked pages → then expand into the mapped gaps.

---

## 2. Site & Audience Findings

### 2.1 Analytics truth (live Rybbit pull, 2026-08-27, TZ America/New_York) [T1]

| Metric | prior7 | last7 | 30-day | Target |
|---|---|---|---|---|
| Sessions | 650 | **860** | 1,717 | sustain 150+/day |
| Bounce | 90.9% | **91.3%** | 89.1% | <70% |
| Pages/session | 1.14 | **1.10** | 1.23 | >1.9 |
| Duration | 64s | **62s** | 78s | >120s |

- Referrers (last7): DDG 277 · Bing 192 · Yahoo 88 · Ecosia 26 · **Google 22 (2.6%)**. [T1]
- Geo: US 700 (81%), **CN 88 @ ~95% bounce = bot noise** (discount ~10% of reported traffic). [T1]
- Top pages: how-to-lower-electric-bill-complete-guide 123 · sudden-spike 52 · water-bill-too-high 45 ·
  reconnection-fee 34 · water-meter-running 33. [T1]
- AdSense: **blocked** ("Low value content", 2026-08-23) → removed from source (ADR-006). [T1]

### 2.2 Audience & intent [T2 — prospector classification + analyst map]

The corpus serves **three distinct reader intents**, and they monetize differently:

| Persona | Intent | Example queries | Monetization fit |
|---|---|---|---|
| **Bill-shock urgent** (largest) | Diagnose an anomaly *now* | "why is my electric bill so high", "sudden spike no usage", "water meter running" | Energy monitors, leak detectors, smart plugs — problem→tool is a natural CTA |
| **Bill-literate optimizer** | Understand & reduce recurring cost | "what is CCF", "delivery vs supply charge", "time of use" | Smart thermostats, weatherization, tariff-switching context |
| **Planning researcher** | Major decision ahead | "heat pump vs furnace savings", "EV charging impact" | High-AOV: thermostats, HVAC, EV chargers; lead-gen alternative |

**Topical authority state:** 6 hubs cover 85/96 posts; authority is real in bill-anatomy/fee
explainers, thin in the money category — **Savings & Efficiency holds only 4 of 96 posts**. [T2]

### 2.3 E-E-A-T posture [T2]

Bones are right: editorial-policy, methodology, corrections, editorial-team, disclosure page,
per-article sources strip. Two weaknesses: (a) authors are transparent **desk bylines, not verifiable
individuals** — honest, but a ceiling on trust that competitors' named-staffer model beats;
(b) the AdSense "low value content" finding is an unresolved market signal about the corpus itself.

---

## 3. Competitor Analysis [T2 — analyst, retrieved 2026-08-27]

| Competitor | Model | What they do that we should note |
|---|---|---|
| EnergySage | Quote marketplace (solar, heat pumps, EV, plans) | ZIP-code lead capture; named authors with dates & read-times; editorial-guidelines page |
| ChooseEnergy (Red Ventures) | Deregulated plan comparison, 15 states | State/city/provider hub-and-spoke at scale; explicit "how we make money"; regulator IDs in footer |
| SaveOnEnergy (Red Ventures) | Same model | "18+ years", BBB A+, transparency-first monetization page |
| EnergyBot | Plan marketplace + tools | Free tools (Rate Tracker, Compare My Bill) as linkable assets; explicit FAQ on earnings |
| Wirecutter (NYT) | Product-review affiliate | The E-E-A-T gold standard: canonical one-line disclosure, staffer bylines, real testing methodology |

**Monetization reality for this niche (verified rates, Amazon rate table, retrieved 2026-08-27):**
smart thermostats / leak detectors / smart plugs / energy monitors fall under **Home Improvement /
Home / Tools ≈ 3.00%** (Kitchen 4.50%, "All other" 4.00%). At info-content EPC assumptions
($0.05–0.15/click info pages; $0.20–0.50 product pages — *industry assumptions, not Amazon-published*),
Amazon links are a **volume game** here. The structural upside in this niche is **lead-gen**
(EnergySage/ChooseEnergy-style, $50–500/qualified lead for plan-switching and heat-pump/solar quotes)
— flagged as a Phase-3 option, not a now-action.

**Competitive gaps mapped to our corpus:** (a) no per-state average-bill coverage (only 4 national/state
hybrid pages); (b) no heat-pump/IRA-rebate content; (c) no EV-charging cost cluster; (d) no dedicated
product pages (energy monitors, leak detectors, thermostats); (e) no free tools/calculators despite
high tool-intent in the niche.

---

## 4. Content & SEO Audit

### 4.1 Inventory & classification basis

121 content files (96 blog + hubs + legal/author). Full per-page dataset:
`.squad/SQ-044/artifacts/prospector-page-table.md` [T3 — classifications corroborated by
cartographer/verifier where checked; **word-count column is approximate — re-derive before
page-level surgery**]. Architecture dataset: results `05-cartographer`. [T2]

### 4.2 Page-classification verdicts (cluster level)

| Cluster / set | Verdict | Rationale & action |
|---|---|---|
| CLUSTER-READ-ELEC (7 pages on reading the electric bill) | **Consolidate** | Severe cannibalization on one intent; merge into 1 authoritative guide + 301 the rest |
| CLUSTER-COST (5 average-cost pages) | **Replace** | All draft:true or unsupported state-level claims; rebuild ONE source-linked 50-state resource |
| CLUSTER-SAVE (7 lower-your-bill pages incl. the #1 draft) | **Improve + differentiate** | Rescue the complete-guide (draft) as the money page; make 50-smart-plugs/phantom-power/gadgets a product cluster with distinct angles |
| 4 canonicalized twin pairs (e.g. 15-why… vs why-my…) | **Retain** | Already rel=canonical — verify canonicals survive rebuilds [T2] |
| CLUSTER-FEES (12+ fee-explainer pages) | **Consolidate selectively** | Distinct fees = distinct queries; merge only true duplicates (connection/reconnection) |
| 7 draft:true pages | **Improve or remove** | Must not ship as-is; the #1 traffic page is in this set — resolve its deployment paradox (see §6 P0) [T1] |
| 11 orphan posts (0 hub inlinks) | **Improve (link in)** | Wire into hubs; orphans waste crawl equity [T2] |
| 48 dead-end posts (0 outlinks) | **Improve** | 50% of posts leak readers; add contextual next-steps |
| Glossary hub | **Improve** | Main-menu destination with **zero** onward links — dead end [T2] |
| Bottom-15 (thin/duplicate/unsourced) | **Remove or redirect** | Mostly duplicate twins & sub-600-word unsourced pages; prune before Google re-evaluates |

### 4.3 Thin / outdated / generic / AI-flagged content

- Site's own remediation ledger (GROWTH_LOG Entry 9): **92/96 guides originally had zero outbound
  sources**; queue now shows 0 P0 / 0 P1 / **6 P2** remaining — remediation is *mostly done* but
  incomplete, and AdSense's rejection predates trusting it. [T2]
- Hardcoded undated price ranges are widespread ("$500–$2,000 professional sealing", "$80–$200
  tune-up") — medium risk: stale-misleading numbers undermine the "exact savings" promise. [T2]
- Reads-AI-generated flags concentrate in CLUSTER-COST and the complete-guide draft. [T3]

### 4.4 Technical SEO & architecture fixes (ranked) [T2]

1. **Deployment pipeline** (blocks everything — §6 P0-1)
2. Rescue/replace #1 traffic page (draft/301 paradox) [T1]
3. CLUSTER-READ-ELEC consolidation + 301s
4. Wire 11 orphans into hubs; add outlinks to 48 dead-ends (prioritize top-traffic dead-ends)
5. Fix ghost link `electricity-explained.md:259` → alias-only URL; truncated title in
   `gas-delivery-charge-vs-supply-charge.md`; add Savings & Efficiency to footer categories
6. URL hygiene: numbered-prefix slugs (01–28, 30, 41–50 with gaps) — do NOT mass-rename now
   (churn risk); normalize only via the consolidations in 4.2
7. Schema: verify Article/FAQPage markup survives the template work; add to hubs

---

## 5. UX & Conversion Plan [T2 — operator rendered-experience audit]

**What works:** answer-first Quick Answer card (5/5 sampled), CLS-safe hero images, TOC >800 words,
breadcrumbs, per-article sources strip, homepage guided-entry architecture, hubs with auto-directories.

**Gaps (in reader order):**

1. **Editorial-policy/methodology never appear above the fold** — trust surfaces only post-scroll;
   add a compact trust line to the byline strip on money-adjacent pages.
2. **One product-box maximum per page, no comparison tables** — affiliate-ready articles need a
   2–4 product comparison block with per-item "why this / who it's for / check price" and NO
   fabricated testing claims.
3. **Email capture exists in exactly one position** (article foot). Add homepage placement +
   one contextual in-article offer on top-15 pages. Current asset: "Stop Overpaying" tips (Mailchimp).
4. **Dead `adsbygoogle.js` in repo builds' `<head>`** — remove (privacy-policy mismatch + weight). [T1]
5. Mobile: meta strip 14px is borderline; nav tap targets pass; keep 16px+ inputs.
6. Page weight healthy (41KB avg HTML) — no core-web-vital emergency detected from markup.

**Affiliate-ready article template spec (implement once, reuse):**
byline+trust strip → Quick Answer → (money pages: **disclosure line**) → body with H2/H3 scan
structure → comparison/product block (first product above fold on high-intent pages) → FAQ →
sources strip → related posts → email capture. Disclosure must sit **visually before the first
link**, per FTC and Amazon OA §5.

---

## 6. Compliance Requirements (Amazon Associates + FTC) [T1/T2 — verifier OA diff, retrieved 2026-08-27]

**Live violations — fix before ANY new link work:**

| # | Violation | Where | Fix |
|---|---|---|---|
| C1 | Wrong associate tag live | `hugo.toml:10` `amazon_tag='litwd-20'` + both live product pages in production | Set `amazon_tag='utexplained-20'`, rebuild, redeploy [T1] |
| C2 | No disclosure on monetized page | `30-sudden-spike` (source has product-box, no disclosure shortcode; production confirmed) | Inject `{{< affiliate-disclosure >}}` above first product box [T1] |
| C3 | Required statement absent near links | Inline shortcode + footer say "may earn a small commission" — **Amazon OA §5 requires "As an Amazon Associate I earn from qualifying purchases" (or substantially similar) clearly on the site where links appear**; the full disclosure page has it but placement is insufficient | Update shortcode + footer text [T2] |

**Standing requirements:** Special Links only (tagged, via the shortcode — never hand-built URLs);
no price hardcoding for *Amazon products* (utility-service price ranges are editorial content, but
date/source them); no fabricated reviews/testing (currently clean — verified zero "we tested/our
review" claims); FTC clear-and-conspicuous placement before links.

**E-E-A-T (non-violation, ceiling):** desk bylines are honest and disclosed as such; consider one
verifiable human editor-of-record for the money cluster before scaling product content.

---

## 7. Prioritized Backlog

Format: **ID · action · affected pages · effort · measurement · revenue relevance**

### P0 — Stop the bleeding (Week 1)

| ID | Action | Pages | Effort | Measure | Revenue |
|---|---|---|---|---|---|
| P0-1 | Restore build→deploy pipeline; reconcile repo/public/production drift | sitewide | M | Deployed state == repo HEAD (curl spot-checks) | Enables everything |
| P0-2 | Fix `amazon_tag` → `utexplained-20`; rebuild | hugo.toml + 2 live pages | S | Live URLs show `tag=utexplained-20` | Recovers mis-attributed clicks |
| P0-3 | Compliant disclosure: shortcode+footer carry Amazon-required statement; inject on every monetized page | layouts/shortcodes, footer, 2 pages | S | OA §5 text visible near links | Keeps the account |
| P0-4 | Resolve #1 page paradox: un-draft & improve the complete-guide (it's the top traffic+money page) OR deploy the 301 deliberately — decide, don't drift | complete-guide + 05 | M | One canonical live URL; rankings stabilize | 13.7% of traffic |

### P1 — Engagement repair + first ethical monetization (Weeks 2–4)

| ID | Action | Pages | Effort | Measure | Revenue |
|---|---|---|---|---|---|
| P1-1 | Engagement pass on top-15 traffic pages: internal next-steps after Quick Answer, dead-end outlinks, related-posts relevance | top-15 by sessions | M | Bounce <75% → <70%; pages/session >1.5 | CTR precondition |
| P1-2 | Monetize 5 remediated, source-linked, high-intent pages with product-boxes (30-spike, 50-smart-plugs, phantom-power, gadgets, do-programmable-thermostats) — comparison format, no testing claims | 5 pages | M | Rybbit outbound CTR 3–8% target; Amazon clicks/reports | First real revenue |
| P1-3 | CLUSTER-READ-ELEC consolidation (7→1+301s) | 7 pages | M | Cannibal pages de-indexed; consolidated URL sessions | Concentrates authority |
| P1-4 | Finish P2 remediation queue (6 items) + date/source the worst hardcoded price ranges | 6+ pages | S | Queue empty; spot-check citations | Google re-trust |
| P1-5 | Prune bottom-15 (redirect/remove duplicates & unsourced thin) | ~15 pages | S | Index quality; no traffic loss in 14d window | Crawl budget to money pages |
| P1-6 | Email capture: homepage + 1 contextual slot on top-15 | sitewide | S | Signups/week baseline → 2× | Owned channel, later CRO |

### P2 — Scale what works (Weeks 5–12)

| ID | Action | Pages | Effort | Measure | Revenue |
|---|---|---|---|---|---|
| P2-1 | CLUSTER-COST rebuild: one 50-state average-bill resource (sourced: EIA) | 1 big + 301s | L | Entrances, rankings on state queries | Programmatic ad of affiliate surface |
| P2-2 | Product cluster: energy monitors / leak detectors / thermostats — honest "what to look for" formats | 6–10 new | L | Organic entries; EPC per page | Core product revenue |
| P2-3 | HVAC/heat-pump + IRA rebate cluster; EV-charging cluster | 8–12 new | L | Rankings, hub entrances | High-AOV intent |
| P2-4 | Free tool #1 (transcription of existing calculators, e.g. bill-anatomy or CCF calculator) | 1 | M | Tool entrances, links earned | Linkable asset |
| P2-5 | Glossary hub activation (link terms → guides) | glossary | S | Pages/session from glossary | Discovery |
| P2-6 | Evaluate lead-gen partners (plan-switching/heat-pump quotes) after content trust is re-established | n/a | M | Lead EPC vs Amazon EPC | Diversification |

---

## 8. 30 / 60 / 90-Day Roadmap

**Days 1–30 — Compliance, pipeline, engagement triage**
Ship P0-1..4 (pipeline, tag, disclosure, #1-page decision). Complete P1-1 on the top 15. Monetize the
first 5 pages (P1-2) only after their engagement pass. Start P1-3/P1-4. *Exit criteria: zero live
compliance violations, deploy pipeline proven, bounce ≤78%, first attributed Amazon clicks on the
correct tag.*

**Days 31–60 — Consolidation & trust**
Finish P1-3..6. Re-request Google re-evaluation indirectly via improved signals (no AdSense reapply
yet). Publish 2–3 product-cluster pages (P2-2 start). *Exit criteria: pages/session ≥1.5,
Google-referrer share rising off the 2.6% floor, Amazon EPC data on ≥5 pages to replace assumptions
with measured reality.*

**Days 61–90 — Scale & diversify**
P2-1 state resource, P2-3 clusters, tool #1. Decision gate on lead-gen (P2-6) using 60 days of
Amazon EPC data. *Exit criteria: 150+ sessions/day sustained with bounce <70%, ≥15 monetized pages,
email list compounding, second revenue path decided on evidence.*

---

## 9. KPIs & Measurement

| KPI | Now [T1] | 30d | 60d | 90d | Source |
|---|---|---|---|---|---|
| Sessions/wk | 860 | 950 | 1,100 | 1,400 | Rybbit (weekly snapshot via `scripts/rybbit_snapshot.py`) |
| Bounce | 91.3% | ≤78% | ≤72% | <70% | Rybbit |
| Pages/session | 1.10 | 1.3 | 1.5 | 1.7 | Rybbit |
| Google referrer share | 2.6% | 5% | 10% | 15% | Rybbit referrers |
| Affiliate CTR (monetized pages) | 0 | 3% | 5% | 6%+ | Rybbit outbound events vs Amazon reports |
| Tag correctness in production | FAIL | PASS | PASS | PASS | curl spot-check |
| Email signups/wk | ~0 | 10 | 25 | 50 | Mailchimp |
| Revenue | $0 | first clicks | measured EPC | second-path decision | Amazon Associates reports |

---

## 10. Assumptions & Evidence Register

**Labeled assumptions:** EPC/conversion/AOV figures are industry-typical estimates (analyst), not
Amazon-published — replace with measured values after P1-2. Lead-gen value range ($50–500) is
market-reported. "Google suppression" is an inference from the referrer inversion + AdSense finding,
not a confirmed action.

**Known data-quality flags:** prospector word-count column approximate (spot-check: 30-spike actual
3,664 vs ~1,500 claimed); challenger's formal verdict did not survive envelope truncation (its risk
findings did, and were disk-verified); executor's sweep was salvaged from ground-truth logs after a
protocol failure (its angle was independently covered by prospector/cartographer/verifier).

**Artifacts:** `.squad/SQ-044/artifacts/prospector-page-table.md` (121-page dataset) ·
`mason-prior-art-inventory.md` (37 initiatives) · `.rybbit-snapshot-2026-08-27/snapshot.json` ·
result envelopes in `.squad/SQ-044/packets/results/`.

*This audit honors the constraints: no fabricated expertise, reviews, testing, pricing, or firsthand
experience; enhancement-only; FTC/Amazon/search-policy compliant tactics only.*
