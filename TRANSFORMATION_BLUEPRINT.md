# utilityexplained.com — Website Masterpiece Transformation Blueprint

**Mission:** SQ-016 · **Date:** 2026-08-21 · **Commander:** ZCode (GLM 5.3)
**Squad evidence base:** Analyst, Challenger, Twin Q, Twin Q2, Researcher, Scout + Operator (creative/monetization rounds) + Commander disk-verification of every load-bearing claim.
**Status:** DRAFT for approval — **STOP BEFORE PRODUCTION** (no images, no code, no irreversible changes until direction is approved).

---

## 1. Executive Diagnosis

utilityexplained.com is a **content-complete, trust-rich, technically sound site wearing a borrowed, generic suit**. Two prior optimization missions (Aug 10–12 growth mission; SQ-013 Aug 21) hardened the content and technical-SEO layers — and the engagement numbers still bleed: **84.7% bounce, 1.52 pages/session, 80s average duration** on ~191 sessions/day (95% Bing-ecosystem; Google barely present at 4.8%).

The audit wave converged on one conclusion from six independent directions: **the remaining lever is not content — it is the experience system**: how the answer is presented, how the site looks and feels, how the next step is offered, and how monetization is woven into it.

**Five structural findings (all disk-verified, most multi-source):**

1. **The hubs are not hubs.** All 5 pillar pages render through the prose article template (`layout: single`). The primary navigation leads to walls of prose with inline HTML link lists. No hub layout exists.
2. **The article funnel buries the next page.** Template order: content → FAQ → tags → ad → sources → author-bio → email-capture → related-posts. A satisfied reader must scroll past three conversion modules to find "Keep Reading." This is the structural driver of 1.52 pages/session.
3. **The answer is below the fold on 96 of 97 articles.** The hero image renders before the TOC and body (`hero_below_answer` set on exactly 1 article). On mobile (58% of traffic) the first screen is title + hero, not the answer.
4. **Monetization regression.** The docs claim 3 ad slots per article; reality: exactly ONE ad renders on articles (`end_article`, single.html:94). The `mid_article` slot (7429084400) is configured but invoked nowhere — almost certainly lost in the Aug 19 theme-v3 convergence. Revenue is being left on the table while trust-friction (ad placement) is simultaneously misallocated.
5. **E-E-A-T is asserted, not demonstrated.** "Licensed HVAC Technician" bylines with no credentials, no photos, no external links; a homepage trust strip saying "Updated 2026" while 0 of 121 files carry `updated:` frontmatter; one author on 52 of 96 articles; affiliate product boxes interrupting money-stress diagnoses.

**The opportunity:** the SERP gap is wide open. Competitors are provider self-explainers (self-serving), Texas-centric comparison/lead-gen sites (switch-your-provider agendas), and dry government pages. **Nobody owns independent consumer-advocate bill decoding across electricity + gas + water + heating.** This site's content already IS that — the transformation makes it look and feel like what it is.

---

## 2. Research Findings (Phase 1 evidence)

### Facts (directly observed, disk/live-verified)

| # | Finding | Evidence |
|---|---------|----------|
| F1 | 97 blog articles (median 1,957 words; p25 1,425; max 4,120; 1 article <800) + 5 hubs + glossary + 12 trust/static pages + 5 author pages | Commander metrics sweep; Analyst FACT 3 |
| F2 | Quick Answer blocks on 80/96 articles (not 97/97 as docs claim) | Twin Q2 CLM-02 |
| F3 | 589 internal `/blog/` links (avg 6.0/article) — docs claim "800+" | Twin Q2 CLM-15; Analyst FACT 8 |
| F4 | Ad render sites: home `end_article` (index.html:186), list `below_title` (list.html:16), single `end_article` (single.html:94). `mid_article` orphaned. | Twin Q [OBSERVED]; Challenger W1; Twin Q2 CLM-11; Commander grep — **4-source convergence** |
| F5 | Article template order buries related-posts behind ad/sources/author/email | Challenger W5; Analyst FACT 6 |
| F6 | Hero renders before answer on 96/97 articles | Challenger W8 |
| F7 | 0/121 files have `updated:` frontmatter; homepage claims "Updated 2026" | Challenger W3 |
| F8 | Authorship: Margaret Harrington 52/96, Tanya Patterson 17, Roberto Mendoza 12, Marcia Washington 8, David Chen 7; bios carry "drafted with AI assistance," no credentials/photos/links | Twin Q2 CLM-03; Challenger W2 |
| F9 | 17 fragmented categories (Electricity 17, Water 16, H&C 9, Fees 8, Billing 8, Troubleshooting 7, Gas 7, …) | Analyst FACT 3 |
| F10 | `data/navigation.yaml` is dead config — never consumed; menus driven by hugo.toml | Analyst FACT 5 |
| F11 | Visual system = canonical theme `design-system.css` (2,038 lines): deep green/amber/paper, Space Grotesk + Inter + Source Serif 4 | Twin Q tokens map |
| F12 | Generic-aesthetic violations in canonical CSS: `backdrop-filter: blur(8px)` (:756), six `linear-gradient(135deg,…)` (:274,:417,:660,:1449,:1872,:1969), SaaS hover `translateY(-2px)`/`scale(1.03)` (:255,:264,:1548,:2005), hardcoded Tailwind blue `#1e40af`/`#dbeafe` in Most Read chips (index.html:172) | Challenger code pass — **Commander disk-verified** |
| F13 | Editorial quality is genuinely strong: consistent plain-English voice, accurate unit math (1 CCF = 748 gal), formulas, fixed/variable cost discipline, clean tables, standardized FAQs | Researcher 8/8 categories pass |
| F14 | Performance posture solid: fonts preloaded+async, 16KB compiled Tailwind, fingerprinted CSS, deferred JS, eager hero with dimensions (CLS-safe), 21MB total webp images | Analyst FACT 10 |
| F15 | Accessibility baseline good: skip-link, landmarks, focus-visible, prefers-reduced-motion, aria labels, print styles | Analyst FACT 11 |
| F16 | FAQPage schema on 90 articles via deterministic post-R8 path (shortcode → Store → faq-schema-render) | Twin Q [OBSERVED]; Twin Q2 CLM-16 |
| F17 | HowTo schema exists in code (howto/step shortcodes) but used by 0 articles | Challenger W8 |
| F18 | Images: 103 palette-locked custom heroes (66 replaced Aug 15), educational diagrams live on 8 pages via Magica pipeline with vision-QA; 4 off-palette blue/teal inline graphics remain | IMAGE_AUDIT_REPORT cycles 2–4 |
| F19 | Email capture: static Mailchimp POST form, blog articles only, low-pressure framing | Twin Q [OBSERVED] |
| F20 | Hardcoded slug arrays in index.html "Most Read"/quick-links and footer taxonomy links — fragile | Challenger W11 |

### Inferences
- The Aug 19 theme-v3 convergence (Atlas R3) dropped the pre-consolidation single.html ad customizations → the mid-article ad regression (F4).
- The 80s/84.7% engagement floor is now mostly an *experience-architecture* artifact (F5, F6), not a content artifact — content rescues plateaued (Aug 12→21 numbers).
- Google's 4.8% share is an indexing/trust-ramp issue, not a content-quality issue; the Bing ecosystem indexed first and Google hasn't followed yet.

### Unknowns
- Rendered production metrics (LCP/CLS/INP field data) — no CWV lab/field pull this mission.
- Revenue per session and CTR by slot — AdSense dashboard not accessible to the squad.
- Whether Google's reticence is freshness-signal-driven, authority-driven, or simply time-lag — cannot verify without GSC access.

---

## 3. Competitive Insights

| Competitor class | Examples | Their stance | Our counter |
|---|---|---|---|
| Provider self-explainers | Constellation, Georgia Power | Charitable to their own bill; single-provider | Independence across ALL providers |
| Comparison/lead-gen | EnergySage, ComparePower, ChooseEnergy, EnergyOgre (Texas-heavy) | Explain bills to sell a switch | We sell understanding; no switching agenda |
| Government/extension | Texas PUC, CPUC, OK State Extension | Authoritative, dry, generic, unbranded | Same facts, human voice, actionable dollar ranges |
| Policy/B2B | Bipartisan Policy Center, EnergyCAP, Enel | Macro or commercial lens | Householder's kitchen-table lens |

**Open lane (verified by SERP research):** independent, cross-utility, consumer-advocate bill decoding. Exact-match consumer intent ("understand your utility bill") has no strong consumer-focused owner. The 2026 themes (rate hikes, AI-datacenter demand charges, extreme weather) are being covered institutionally — not for the person holding the bill.

---

## 4. Preserve / Improve / Remove / Reinvent

**PRESERVE (proven value — do not touch):**
- Quick Answer answer-first discipline (the snippet/retention engine)
- The five-pillar hub-and-spoke content architecture and 589-link mesh
- Trust page set (methodology, editorial policy, corrections, disclosure) — rare for this site class
- Source Serif 4 long-form reading surface; tabular numerals in tables
- The meter/dial motif seed (hero dial, 404 "0 kWh") — it becomes the brand
- Performance posture (F14) and a11y baseline (F15)
- The Magica image pipeline + palette-lock + vision-QA discipline (F18)

**IMPROVE:** article funnel order; hub pages (real hub layout); category taxonomy (17→~7); author substance and distribution; freshness signaling; related-content scoring; internal-link anchoring; ad placement quality (not just quantity).

**REMOVE:** glassmorphism, 135° gradients, SaaS hover lifts, off-palette blues (F12); hero-above-answer on article pages; affiliate boxes from mid-diagnosis positions; dead `data/navigation.yaml`; "decades of combined experience"-class unverifiable claims.

**REINVENT:** homepage (from category-card grid → bill-triage instrument); hub pages (from prose → audit desks); the Quick Answer (from gray box → signature statement-line readout); monetization architecture (from bolted-on slots → designed zones); the trust strip (from badges → live review dates).

---

## 5. North Star Creative Direction — "The Independent Bill Auditor"

*Fused from two independently generated concepts (Analyst's "Meter Reader" + Challenger's "Consumer-Rate Auditor") that converged unprompted on palette, mono-voice, statement imagery, and instrument-first answer delivery — the strongest possible signal that this direction fits the niche.*

> **North Star Statement:** Utility Explained is the independent auditor of your home. When a bill arrives that feels like a verdict, we are the second set of eyes that actually reads the fine print. Every page is a reading: the machine has already looked at your bill, points to the one line that matters — in amber — and hands you the dollar figure and the exact next move. A ledger precise enough to trust, a voice kind enough to hold. We build the bill out loud: line by line, charge by charge, in numbers you can check.

**Brand personality:** Forensic · Calm under pressure · Cent-exact · Consumer-sided · Generous (answers first, explains second).
**Editorial personality:** the meticulous auditor who walks you through it at the kitchen table. Article anatomy in three beats: **Findings** (the answer + dollar range) → **Basis** (how the charge works) → **Remedy** (the action, up to and including the dispute script).
**First-5-seconds impression:** *relief through audit* — the screen opens to a mono register readout of the answer, not a menu, not a hero photo.
**Could this belong to any other brand?** No — argued by both concepts independently: charge codes, statement lines, meter registers, unit conversions, and tear-off perforations are semantically welded to bills. A generic site has no "amount due" vocabulary.

---

## 6. Visual Design System

### Color (audit-ledger extension of the existing meter-reader palette)
| Token | Value | Role |
|---|---|---|
| `--paper` | `#F7F2EA` | Page surface |
| `--paper-raised` | `#FFFCFA` | Paid-statement cards |
| `--paper-muted` | `#EFE8DA` | Terms/audit zones |
| `--ink` | `#0C1116` | Structure, dark surface (back of the bill) |
| `--text` / `--text-muted` | `#1B2430` / `#5A6472` | Body copy |
| `--tariff-blue` | `#1B4E8F` (5.2:1 on paper) | Links — the regulator's ink |
| `--marker` / `--marker-ink` | `#E8930F` / `#B9740A` | Amber audit marks: rules, large display, THE highlighted line — never small body text |
| `--resolve` | `#3F7D56` | Money-saved confirmations only |
| `--leak` | `#C0392B` | Real money-loss warnings only |

### Typography (three voices, one instrument family)
- **Display:** IBM Plex Sans 600/700 — the regulator/instrument face (replaces Space Grotesk quirk)
- **Body:** Source Serif 4 (unchanged — premium long-form)
- **Identity voice:** IBM Plex Mono with tabular numerals — **every** number, unit (kWh, CCF, therms, gal), dollar amount, charge code, tier, and date renders mono. Alignment is the brand.

### Grid & spacing
Statement ledger: 12-col grid on paper; reading measure 48rem; 4px baseline rhythm; hairline rules (1px neutral) behind key sections; a right-aligned tabular "amount" column and a line-number gutter where the template allows (hubs, comparison tables).

### Signature elements (the untransferable six)
1. **The Bill Decoder (flagship, council-added)** — one canonical, line-by-line annotated sample bill per utility: interactive on hub + home (hover/click a line → the amber audit note and plain-English explanation; animated needle), static-SVG fallback everywhere else (no-JS, zero CLS, printable). No competitor has one; it is the "line by line" promise made literal.
2. **The Register Readout** — every article's Quick Answer renders as a meter-register: odometer-style mono digits presenting the answer figure ($ range, gallons, kWh) with a ≤300ms roll-up on first view (reduced-motion safe).
3. **The Line-Field Exploder** — the answer block styled as a statement line: line number, charge code (mono), description, amount, amber audit note. The article literally opens as a line from your bill.
4. **The "You Owe / You Save" total line** — closing block styled exactly like a bill's total-due seam: what this charge costs, what the fix saves, what to do next.
5. **The Unit-Converter Band** — a mono strip converting the article's core units (1 CCF = 748 gal; 1 therm ≈ 29.3 kWh) — functional, not decorative.
6. **The Thermal Tear-Off** — dotted perforation rule ("detach here") for card footers, section dividers, and the 404.

### Motion philosophy
Three signature motions only, each communicating a quantity: register roll-up, register-tape reading progress (receipt feel — evolves the existing progress bar), tier-band fill on scroll. All <300ms, all disabled under `prefers-reduced-motion`. Nothing else moves.

### Imagery rules
Technical SVG-first: annotated statement redraws, meter/register diagrams, rate-band visualizations. Photos only if real, unglamorous utility hardware. **Stock and lifestyle photography permanently banned.** All assets palette-locked (ink/amber/paper + tariff blue), produced through the existing Magica pipeline with vision-QA.

### De-slop demolition list (disk-verified targets — council-expanded)
`backdrop-filter: blur(8px)` (design-system.css:756) · six `linear-gradient(135deg,…)` (:274, :417, :660, :1449, :1872, :1969) · hover `translateY(-2px)`/`scale(1.03)` (:255, :264, :1548, :2005) · hardcoded `#dbeafe`/`#1e40af` chips (index.html:172) · **+ council finds (verified):** `text-gray-500`/`text-gray-900`/`group-hover:text-blue-600` Most-Read markup (index.html:165–177) · inline `#e5e7eb` borders + `#0891b2` cyan links in `content/blog/_index.md` · residual gray/blue audit across 404 + howto templates. End-to-end palette consistency is the goal: the meter system must reach every template.

---

## 7. Information Architecture

**Taxonomy consolidation: 17 → 7.** Electricity · Gas · Water · Heating & Cooling · Bills & Fees (merge Billing+Fees+Taxes) · Savings & Efficiency (merge energy-efficiency+savings) · Troubleshooting (merge Meters+Troubleshooting). Legacy categories 301 to their parents via `.htaccess` (protects existing URLs; tag taxonomy stays noindexed).

**New/changed templates (all site-level overrides — zero canonical-theme edits in Phase A):**
- `layouts/_default/hub.html` — real hub layout; hubs switch from `layout: single`
- `layouts/_default/index.html` — homepage override (copy-then-diverge from theme)
- `layouts/_default/single.html` — article funnel reorder + mid-article zone
- `layouts/partials/related.html` (or scoring override) — see §11–12
- Delete dead `data/navigation.yaml` (or wire it; recommend delete — hugo.toml menus are the live truth)

**Journey system ("Bill Triage"):** a four-step entry flow — *Which utility? → Which line looks wrong? → Findings → Remedy* — connecting homepage, hubs, and articles; the "Start with your bill" CTA becomes literal.

**Author redistribution:** cap primary author at ~40% of new/refreshed articles; redistribute across the five personas by domain (Mendoza→water/meters, Patterson→rates/fees, Washington→assistance programs, Chen→heating/cooling, Harrington→electricity + editorial lead). Add per-author credential lines that are TRUE (see §13).

**URL discipline:** all existing URLs preserved; consolidation only through 301s (pattern already proven in commit 36ca5a18).

---

## 8. Homepage Blueprint

**Purpose:** convert a vague arrival into a triaged bill question in one screen.
**Sections (top→bottom):**
1. **Register hero** — mono register readout cycling real numbers ("A typical US bill: $184/mo · 899 kWh · 3 CCF/day"), the amber needle marking "the line that matters," two CTAs: **Start with your bill** (triage flow) and **Search your bill line** (existing glossary search).
2. **Triage panel** — the 4 utilities as instrument tiles (dial per utility) + Bill Basics + Glossary; each tile states its top question ("Why is my electric bill high?").
3. **Start Here** — six numbered essentials (keep — already strong), restyled as audit-docket entries.
4. **Most Read** — keep, fix palette (kill blue chips), add per-card "finding" line (the answer in 8 words).
5. **Latest** — keep dated cards; add review-date stamp.
6. **Trust strip → live trust ledger:** replace static badges with real counters: "96 guides · last reviewed [real date] · corrections policy · methodology" — no claim without a live source.
**Mobile:** triage panel becomes a 2×2 grid; register hero scales via clamp(); zero layout shift (readout reserves height).
**Ads:** one `end_article` placement after Most Read (unchanged position, restyled frame).
**SEO:** homepage schema unchanged (WebSite/Organization/SearchAction); H1 carries the promise verbatim.

---

## 9. Article Experience Blueprint (the economic heart)

**Funnel reorder (the single highest-leverage template change):**
1. H1 + byline + review date + read time
2. **Register Readout** (Quick Answer as Line-Field Exploder) — THE answer, above everything, no hero above it
3. Hero image (demoted below the answer — flips current 96/97 inversion) OR inline at first relevant section
4. Body (Findings → Basis → Remedy structure; existing content already fits)
5. **Mid-article next-step card** (contextual, after the section that raises the question)
6. FAQ
7. **You Owe / You Save total line**
8. **Related guides (3, re-scored)** — promoted from the grave to first-class
9. `end_article` ad (framed as a demarcated zone, never adjacent to CTAs)
10. Sources strip · Author box · Email capture (last — earned, not begged)

**Scoring upgrade for related:** same-category +2 → same-utility-pillar +3 · shared tag +1 · complementary-intent flag (article front matter `pairs_with:`) +4 · fallback: editor-curated per hub.

**Affiliate rule:** product boxes only on commercial-intent articles (best-of/tool classes), always BELOW the diagnosis/remedy, labeled, with vendor claims attributed — never inside a money-stress diagnosis.

**Trust per article:** review date (real `updated:` frontmatter → rendered "Last reviewed"), named author with true credential line, sources strip (already present — upgrade to linked citations on refresh).

---

## 10. Page-by-Page Plan (condensed)

| Template | Treatment |
|---|---|
| Hub (new `hub.html`) | Answer-first intro (60–90 words) · jump-nav · utility stat strip · curated topic groups with one-line descriptions · featured decision paths · FAQ · end ad |
| List/category | Keep below_title ad; add group headers matching the 7-category model |
| Search | Instrument-panel styling; mono results with charge-code chips |
| Author | True credential line, focus areas, article list; ProfilePage+Person schema (already fixed in SQ-013) |
| About | The auditor's charter: independence statement, no-switch-agenda, how reviews work |
| Contact | Keep mailto; add "report an error" path feeding corrections policy |
| 404 | "No reading found" — dead meter at 0 kWh (motif already exists) + tear-off + triage links |
| Trust/legal | Consistent paper-muted audit zone styling; no ads on trust pages |

---

## 11. AdSense Monetization Architecture

*(Operator zone map — 94 tool steps, every placement grounded in verified template truth.)*

### Zone map
| Page class | Zones | Slots | Rules |
|---|---|---|---|
| Article (≥1,200 words — 53% of corpus) | mid-content + end | `mid_article` (reinstated) + `end_article` | Mid after H2#2–3 / ~45% depth; reserved min-height (the adslot partial currently reserves none — the one CLS gap; unfilled-slot collapse already exists at design-system.css:584); never within 2 viewports of the Register Readout |
| Article (≥1,800 words, desktop) | + sidebar rail (conditional) | existing `below_title` repurposed | Only if viewability proves out in measurement; mobile never |
| Article (<1,200 words — ~30%) | end only | `end_article` | Too short for a second ad without crowding |
| Affiliate articles (14) | end only, 2-ads-max | `end_article` | AdSense density lowered where product boxes exist — trust first |
| List/hub | above-grid | `below_title` (unchanged) | The one healthy in-feed placement — keep |
| Homepage | one content-boundary | `end_article` after Most Read (unchanged) | Restyled frame only |
| Trust/legal/search | none | — | Hard rule |

### Density doctrine
Article cap **3 desktop / 2 mobile** · list/hub 1 · homepage 1. With 84.7% bounce and 80s sessions, max-impression density is counterproductive: sustainable revenue per session = fewer, better-placed ads. Ads never adjacent to CTAs or affiliate boxes; framed "advertisement" hairline zones consistent with the ledger aesthetic; YMYL money-stress gate on every future placement idea.

### Structural revenue notes
- **Consent Mode v2 (default denied)** means non-consented first sessions serve non-personalized ads at lower CPM — a structural cap on exactly the sessions that dominate the 84.7% bounce. Policy-safe; the remedy is more second-pages (engagement), not more ads.
- **The reinstated `mid_article` slot (7429084400)** recovers the config-vs-render gap left by theme convergence — implemented via site-level single.html override, zero canonical-theme edits.

### Email capture (repositioned, not relocated)
Keep the late position (asking before helping converts poorly); rewrite the promise (replace "Get Free Tips" gradient-box with an audit-flavored offer: "One bill decoded per month"), and trigger on engagement signals (50% read · 60s dwell · scrolled past sources) instead of showing to every passerby.

### Session-depth systems
In-article **triage band** (the in-content "your next step" path — closes the loop Operator verified is missing: triage currently requires leaving the article for the hub) · re-scored related (pillar +3, `pairs_with:` +4, recency/popularity tiebreaks) · topic journeys across the 7-category model.

### Measurement plan
| Change | Metric | Target |
|---|---|---|
| Funnel reorder + answer-first | bounce (Rybbit) | 84.7% → <70% |
| Related re-scoring + triage band | pages/session | 1.52 → >1.9 |
| Register Readout / Findings hooks | avg duration | 80s → >120s |
| mid_article reinstatement | AdSense viewable impressions / session RPM | +20–40% vs 1-ad baseline (measure 14 days) |
| Email triggers | signups/1,000 sessions | 2× baseline |
| Hub layout | hub entrance → article CTR | +30% |

---

## 12. SEO & Content Discovery Strategy

- **Freshness made real:** `updated:` frontmatter discipline + rendered "Last reviewed" dates; review cadence published on methodology page. (Kills the F7 lie, feeds Google freshness signals.)
- **HowTo schema:** enable existing howto/step shortcodes on the ~15 strongest instructional articles (meter tests, dispute process) — zero new code, pure content templating.
- **Topic clusters:** 7-category model strengthens hub-and-spoke; hubs get FAQ schema (already) + itemized `ItemList` of guides. **Glossary upgrade (council add, Phase B):** the 233-line glossary is a natural `DefinedTermSet`/`DefinedTerm` schema target — currently absent; a phased add while refreshing glossary entries.
- **Google ramp:** continue IndexNow (Bing-side), request indexing via GSC on refreshed URLs; the review-date system + author substance are the E-E-A-T levers Google side specifically.
- **Discovery:** Unit-Converter Bands + Register Readouts are snippet-shaped blocks — each article's 40–50 word Finding doubles as the featured-snippet candidate (extending the proven Aug-12 pattern).
- **Internal linking:** target 8–10 contextual links/article via `pairs_with:` complements; hub → article descriptions become the anchor-text layer.

---

## 13. Trust, Mobile & Performance Plan

- **Author substance — DECISION REQUIRED (council escalation):** the council flagged the current state honestly: 5 named personas (52/96 articles concentrated in one), thin credential lines, explicit AI-assistance disclosure. Two defensible paths — **(A) Keep personas, harden them:** true credential lines only, redistribute authorship ≤40% each, retain the AI disclosure (honesty as moat); **(B) Consolidate to a truthful editorial-team identity:** retire individual personas, publish as "The Utility Explained editorial team" with a real methodology page. Fabricated credentials are forbidden either way. This is an owner-level call — see approval checklist.
- **Review workflow:** corrections policy gains a visible "report an error" loop; every KPI-claim in site docs gets a disk-verifiable source (this mission found 5 stale claims — the docs themselves need the freshness system).
- **Mobile as first-class:** register readouts scale via clamp(); triage grid 2×2; all new components touch-target ≥44px; test on mid-tier Android.
- **Performance budget (design-enforced):** new CSS ≤ +12KB gzipped total; no new webfont families beyond Plex pair (drop Space Grotesk + Inter = net-neutral); **self-host the font files** (council add: Google Fonts preload remains a render-blocking third-party request — self-hosting removes it); SVG-first imagery; keep eager-hero discipline (now below the answer — LCP candidate becomes the H1/readout text, faster); kill `background-attachment: fixed` jank (Challenger W12); reserved space on every ad zone.

---

## 14. AI Media Art Direction (PLAN ONLY — no generation before approval)

Pipeline: existing Magica `gpt-image-2-text` (High, 1536×1024 → webp q85) + gpt-5.5 vision-QA, palette-locked. Priorities:

1. **THE missing killer asset — Annotated Bill Anatomy series (4 masters):** one annotated statement redraw per utility (electric/gas/water/combined), amber audit circles on each charge zone, mono labels. Used in: the 4 relevant hubs + the complete-guide + hidden-fees article. This is the single highest-value visual investment (my rendered-site review: "a guide about visual documents with zero visuals").
2. **Hub hero instrument panels (5):** dial/register close-ups per utility.
3. **Unit-converter band graphics (6):** CCF↔gallons, kWh↔cost, therms↔kWh, etc.
4. **Rebuild 4 off-palette inline graphics** (already-queued debt: reconnect_fees, reconnect_avoid, ccf-convert, ccf-normal).
5. **OG system:** statement-frame OG template with mono readout of the article's answer.
6. **Optional single video** (only if motion proves value): "Read your meter in 60 seconds" — dial close-up, register roll — reused across water/electric articles.

All assets follow one visual language: ink/amber/paper, mono labels, no people, no lifestyle, no fake-bill text gibberish (vision-QA gate checks legibility — the Cycle-4 lesson).

---

## 15. Risks & Tradeoffs

| Risk | Severity | Mitigation |
|---|---|---|
| Canonical-theme edits ripple to 6 sites | High | Phase A = site-level overrides ONLY; theme-level token refresh (Phase B) only after Phase A proves, propagated per Atlas R3 flow |
| Ad changes trip policy/YMYL trust loss | Med | Conservative density, framed zones, never-adjacent rules, monitor Rybbit + AdSense |
| Editorial voice drift during restructuring | Med | Findings/Basis/Remedy maps onto existing content; no rewrites in Phase A |
| Byline redistribution confuses returning readers | Low | Gradual, new-content-first |
| Funnel reorder suppresses email/ad CTR short-term | Med | Measure per-zone; email moves last (earned), ad viewability should RISE with mid-article reinstatement |
| Blueprint doc staleness (this mission found 5 stale doc claims) | Med | This blueprint stamps verified-on date; every claim carries evidence reference |

---

## 16. Highest-Leverage Improvements (ranked)

1. **Article funnel reorder + answer-above-hero** (F5, F6) — directly attacks bounce/pages-session on 97 pages.
2. **Real hub layout for the 5 pillars** (F1) — unlocks nav-level engagement + cluster SEO.
3. **Reinstate mid_article + zone redesign** (F4) — recovers lost revenue while improving trust-framing.
4. **Register Readout / Line-Field Exploder on Quick Answers** — the brand signature + snippet engine on 80 pages.
5. **Freshness system (`updated:` + rendered review dates)** (F7) — kills the lie, feeds Google.
6. **Annotated Bill Anatomy series** — the missing visual core of a visual subject.
7. **Author substance + redistribution** (F8).
8. **De-slop demolition** (F12) — cheap, visible, portfolio-safe via overrides.

---

## 17. Approval Before Production — Checklist

> **Scope framing (council-sharpened):** this blueprint transforms an ALREADY-OPERATIONAL site. Nothing here has been implemented; every "Proposed" item describes a change to verified current state (§2). Approving this document approves direction, not deployment — production follows in bounded, site-local-first phases with rollback points.

- [ ] Creative direction ("The Independent Bill Auditor" fusion)
- [ ] Color system (audit-ledger palette, tariff-blue links)
- [ ] Typography (Plex Sans / Source Serif 4 / Plex Mono — self-hosted)
- [ ] Signature elements — incl. **flagship interactive Bill Decoder**
- [ ] Navigation & IA (17→7 categories, hub layout, Bill Triage)
- [ ] Homepage blueprint
- [ ] Article experience blueprint (funnel order, answer-above-hero)
- [ ] Hub/list/author/404 treatments
- [ ] AdSense architecture (mid_article reinstatement, word-count gates, measurement-first sidebar)
- [ ] **DECISION: author personas (A: hardened personas / B: editorial-team identity)**
- [ ] Trust plan (review dates, credentials, corrections loop)
- [ ] AI media plan (Annotated Bill Anatomy first)
- [ ] Phase A/B sequencing (site-local overrides first; canonical theme changes only after proof, propagated per Atlas R3)

**⏹ STOP. No production (code, templates, images, deploys) until the above is approved.**

---

*Evidence appendix: mission blackboard SQ-016; result packets /tmp/ue-transform/results{,-r2,-retry}/; every F-claim above is traceable to a named seat + disk check. Verified 2026-08-21.*
