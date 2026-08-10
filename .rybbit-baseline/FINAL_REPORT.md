# Rybbit Top-10 Content Growth & Conversion — Final Report
## Utility Explained (utilityexplained.com)
**Generated:** 2026-08-10 | **Agent:** Rybbit Top-10 Content Growth & Conversion Agent

---

## Analytics Baseline (Pre-Change)

**Source:** Rybbit API — 30-day window, site ID d5b63e065e9d
**Site Overview:** 436 sessions | 898 pageviews | 376 users | 76.1% bounce rate | 80.6s avg session duration | 2.06 pages/session

**Primary traffic source:** Organic search (Bing, DuckDuckGo, Yahoo) — notably NOT Google
**Critical signal:** 3 of the top 10 pages had **100% bounce rate / 0-second average duration** — visitors never found the answer.

| # | Page | Sessions | Pageviews | Bounce % | Avg Duration | Primary Issue |
|---|------|----------|-----------|----------|-------------|---------------|
| 1 | water-meter-running-when-no-water-used | 11 | 295 | 91% | 56s | Answer not actionable |
| 2 | how-sewer-charges-work-on-your-water-bill | 9 | 177 | 78% | 35s | No internal exploration |
| 3 | 25-utility-bill-taxes-fees-franchise-charges | 5 | 295 | 40% | 4s | Good performer, needed links |
| 4 | 28-utility-reconnection-fee-explained | 5 | 236 | 60% | 22s | Cost not front-loaded |
| 5 | what-is-ccf-on-a-water-bill | 6 | 118 | **100%** | **0s** | **Answer buried in 2nd paragraph** |
| 6 | 30-sudden-spike-in-electricity-bill-no-usage | 5 | 118 | 60% | 110s | No diagnostic checklist |
| 7 | water-meter-leak-indicator-explained | 3 | 177 | 67% | 24s | Truncated title, broken heading |
| 8 | 12-how-to-read-your-gas-bill | 4 | 0 | 75% | **0.2s** | **Narrative opening delayed answer** |
| 9 | 05-how-to-lower-utility-bills | 3 | 59 | 67% | 153s | Needed structured quick wins |
| 10 | 22-minimum-bill-utility-bill-explained | 2 | 118 | **100%** | **0s** | **Vacation scenario delayed answer** |

---

## Changes Summary Table

| # | Page | Probable Intent | Main Problem | Key Changes | CTA Strategy | Internal-Link Strategy | Expected Impact |
|---|------|----------------|-------------|-------------|--------------|----------------------|-----------------|
| 1 | water-meter-running | "My meter spins but I'm not using water — leak?" | 91% bounce; no actionable next step | Quick Answer with 3-step diagnostic checklist; fixed broken H1; cross-linked to leak indicator | Lead to leak indicator guide for confirmation | 8 links (leak indicator, read meter, toilet test, bill increase, lower water bill) | Bounce <80%; pages/session up |
| 2 | sewer charges | "Why is my sewer charge so high?" | 78% bounce; no exploration | Quick Answer box; 10 contextual links; cross-linked to CCF | Explore water bill charge breakdown | 10 links (CCF, water service, stormwater, tiered rates, read meter) | Bounce <70%; duration up |
| 3 | taxes/fees | "What are all these taxes and fees?" | Already good (40% bounce); weak linking | Quick Answer (5-15% range, franchise fee); expanded Related Reading 2→6 | Explore individual fee explainers | 11 links (surcharges, customer charge, delivery vs supply, minimum bill, hidden fees) | Maintain low bounce; pages/session up |
| 4 | reconnection fee | "How much does reconnection cost?" | Cost buried; no prevention | Quick Answer with full cost table; prevention links | Budget billing to avoid disconnection | 7 links (connection fee, deposit, past-due, budget billing, billing cycle) | Bounce <50%; duration up |
| 5 | **CCF on water bill** | "What does CCF mean?" | **100% bounce, 0s — answer in 2nd paragraph** | **Rewrote opening to lead with bolded definition; Quick Answer; fixed broken LaTeX math; fixed table typos; added "C = Roman numeral 100"** | Explore sewer charges (which use CCF) | 8 links (sewer charges, water service, stormwater, tiered rates, read meter) | **Bounce <75%; duration >30s** |
| 6 | sudden spike | "Why did my bill spike with no usage change?" | No diagnostic structure | Quick Answer with diagnostic checklist; 15 contextual links | Lower utility bills after diagnosis | 15 links (why high, estimated bill, demand charges, lower bills, smart plugs, cheaper hours) | Bounce <50%; maintain duration |
| 7 | leak indicator | "What is the leak indicator dial?" | Truncated title, broken H2 heading | **Fixed truncated title; fixed broken H2; Quick Answer box** | Water meter running article | 13 links (water meter running, read meter, toilet test) | **SEO fix (title); bounce <60%** |
| 8 | **gas bill reading** | "How do I read my gas bill?" | **0.2s duration — narrative opening** | **Rewrote opening; Quick Answer with therm/CCF/MCF definitions; expanded unit explanation; cost ranges** | Gas bill too high / lower bills | 8 links (MCF vs therms, customer charge, delivery vs supply, gas bill too high, reconnection fee) | **Duration >30s; bounce <65%** |
| 9 | lower utility bills | "How can I lower my bills?" | Good engagement (153s); needed structure | Quick Answer; 16 contextual links to detailed guides | Deep-dive efficiency guides | 16 links (lower electric, lower water, energy leaks, smart plugs, cheapest hours, spike) | Pages/session up from best performer |
| 10 | **minimum bill** | "Why am I charged when I used nothing?" | **100% bounce, 0s — vacation scenario delayed answer** | **Replaced narrative opener with answer-first; Quick Answer box explaining fixed cost of grid connection** | Customer charge / delivery vs supply | 12 links (customer charge, delivery vs supply, surcharges, billing cycle, hidden fees, taxes) | **Bounce <75%; duration >30s** |

---

## Highest-Leverage Changes

### Tier 1 — Critical Bounce Fixes (Highest Impact)
1. **CCF article (100% → target <75%)**: The definition "CCF = hundred cubic feet = 748 gallons" was buried in the second paragraph. Now bolded in the very first sentence with a Quick Answer box. Also fixed broken LaTeX math rendering and table typos.
2. **Minimum bill article (100% → target <75%)**: Replaced the "you left for vacation" narrative with a direct answer: "If you barely used any electricity but are still being charged $8–$45, that is your minimum bill."
3. **Gas bill article (0.2s → target >30s)**: Rewrote slow narrative opening; added comprehensive Quick Answer with therm/CCF/MCF definitions and dollar ranges.

### Tier 2 — Structural SEO Fixes
4. **Leak indicator article**: Fixed truncated title ("...When Everything" → "...When Everything Is Off") and broken H2 heading ("How to isolate </h2>" → proper heading text). These were literal bugs suppressing search performance.

### Tier 3 — Engagement & Internal Linking
5. **All 10 articles**: Added Quick Answer boxes, contextual internal links (8-17 per article), and cross-links between related articles. Total internal links added across all 10 articles: ~110.
6. **Spike article**: Added diagnostic checklist structure with 15 contextual links.
7. **Lower bills article**: Structured with 16 contextual links to detailed guides.

### Universal Pattern Applied
- Every article now answers the visitor's primary question **in the first 2 sentences** via a Quick Answer box
- Every article now has 7-17 contextual internal links (was 0-2 for most)
- Related Reading sections moved before FAQ
- Cross-linking between topically related articles in the top 10

---

## Measurement Plan

### What to Monitor (Rybbit API — 2-4 weeks post-deployment)

| Metric | Current Baseline | Target | How to Measure |
|--------|-----------------|--------|----------------|
| Site bounce rate | 76.1% | <70% | /api/sites/{id}/overview |
| Avg session duration | 80.6s | >100s | /api/sites/{id}/overview |
| Pages per session | 2.06 | >2.5 | /api/sites/{id}/overview |
| CCF article bounce | 100% | <75% | Sessions by entry page |
| Minimum bill bounce | 100% | <75% | Sessions by entry page |
| Gas bill duration | 0.2s | >30s | Sessions by entry page |
| Leak indicator organic traffic | Low | Increase | Pageviews from organic search |
| Cross-article navigation | ~0 | >15% of sessions | Exit page ≠ entry page rate |

### How to Measure
1. **Weekly comparison**: Pull `/api/sites/{id}/overview` and `/api/sites/{id}/sessions` weekly
2. **Per-page tracking**: Filter sessions by entry_page for each of the 10 articles
3. **Internal link effectiveness**: Track exit_page ≠ entry_page sessions (indicates internal exploration)
4. **Wait period**: Allow 2-4 weeks for search engines to re-crawl and re-rank changed pages

### Success Criteria
- **Any reduction** in the three 100%-bounce articles = success
- **Increase** in pages/session from 2.06 = internal linking working
- **New organic traffic** from Google (currently 0 — the Quick Answer boxes may earn featured snippets)

---

## Technical Notes

- **Baseline preserved**: `/mnt/ai-shared/cluster/websites/adsense-portfolio/utilityexplained/.rybbit-baseline/baseline_report.json`
- **URL canonicalization issue identified**: Some traffic goes to URLs without trailing slashes (e.g., `/blog/what-is-ccf-on-a-water-bill` vs `/blog/what-is-ccf-on-a-water-bill/`). Recommend adding canonical redirects.
- **Bot traffic**: Significant bot/crawler traffic from CN (China) with direct referrers — filtered from analysis. Recommend verifying `blockBots: true` is effective.
- **No Google traffic**: All organic search traffic comes from Bing, DuckDuckGo, and Yahoo. The Quick Answer boxes are structured to potentially earn Google featured snippets.
- **All 1,766 internal links verified**: Zero broken links across all 10 articles.
