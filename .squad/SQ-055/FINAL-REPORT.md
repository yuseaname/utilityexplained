# SQ-055 Final Report — APEX Optimization, Traffic Ranks 11-20
**Site:** utilityexplained.com · **Window analyzed:** 2026-07-30 → 2026-08-29 (Rybbit, fresh pull 2026-08-29) · **Baseline:** `.rybbit-t11320-2026-08-29/baseline_11-20.json`

## Site context at start
1,925 sessions (+4.4× vs Aug-10) · 89% organic search (Bing/DDG/Yahoo) · 56% mobile · 89.2% bounce · 1.235 pages/session · 78s avg session. Ranks 18/19 by raw traffic were alias redirects (consolidated pages) — replaced with next real articles per Commander ruling; alias targets stayed untouched to protect the SQ-053/054 measurement watch.

## Per-page table

| Page | Baseline (visits/TOP/bounce) | Probable intent | Main problem | Key changes | CTA strategy | Internal-link strategy | Expected impact |
|---|---|---|---|---|---|---|---|
| 23-billing-cycle | 59 / 56s / 83% | "why do my bill's dates/length look wrong?" | body-link vacuum; stranded ending | reassurance in QA; normal-vs-second-look table; mini-template; FAQ+schema; Related Reading; body links (dispute, proration, spike, estimated, minimum) | NONE (doctrine NOT-A-FIT) | 4→11 links, body-context | pages/session ↑; bounce <75% |
| 07-gas-too-high | 56 / 92s / 84% | "why is my gas bill high — what do I do first?" | mid-troubleshooting dead zone; count mismatch; Related dump after Sources | triage line; thermostat/AFUE/duct/DIY/billing-cycle links at fix moments; meter section compressed; Related Reading curated+deduped before FAQ; 10-vs-11 fixed | keep single Nest box as-is (move VETOED) | 25 links re-homed to moment-of-need | read→act conversion; exits to action pages |
| electric-breakdown | 52 / 58s / 73% | "explain every line on my bill" | LIVE 404 link; link-dead back half | 404 fixed→10-fixed; category→explainer map (5); +2 FAQs; Related Reading; escalation link; QA citation de-cluttered | NONE (definitional hub) | 13→~30 rendered anchors | protect best performer; deeper sessions |
| 25-taxes | 39 / 5.6s / 82% | "what is this tax/fee line and is it legit?" | no label-matching on first screen | routing self-check line; "Often appears as" column; dispute link; Related Reading (5); FAQ→shortcodes; gross-receipts trim | NONE (NOT-A-FIT) | 4→10 links | TOP 5.6s→30s+ (watch-list target) |
| state-avg-2026 | 30 / 14s / 87% | "is my bill normal for my state / moving costs?" | methodology before dollars; phantom tool promise; self-link; no nav | hero_below_answer; answer-first QA; jump-row; phantom+self-link removed; "read table vs your bill" bridge; FAQ unified+schema; Related Reading | NONE (comparison moment) | 4→10 links incl. moving checklist, rate-plan | bounce 87%→<78%; planner journeys |
| 19-surcharges | 28 / 4.2s / 93% | "is this named rider charge legit, will it go away?" | matching table buried; 120-word QA wall | two-beat QA + routing; jump-row; named-label list; "Will my rider go away?" FAQ; definition tightened (quotes verbatim); FAQ→shortcodes; Related Reading | NONE (NOT-A-FIT) | 4→9 links | TOP 4.2s→30s+ (watch-list target) |
| mcf-vs-therms | 27 / 37s / 89% | "what do CCF/MCF/therms mean on MY bill?" | title-echo glitch; keyword stuffing; self-correcting example; unit contradiction | QA rebuilt (house pattern); stuffing stripped ×3; Scenario C cleaned (math verified); 1 MCF=10 CCF fixed; "where to find on your bill" checklist; inverse-conversion FAQ; Related Reading; hero_below_answer | NONE (definitional) | 4→8 links (12-gas-bill, 18, 07, meter) | trust repair → bounce <80% |
| smart-meters | 25 / 20s / 92% | "how does it work / should I trust it?" | double answer; JSX artifacts in links; no data-visibility exit | answers merged + mechanism chain in QA; artifacts stripped; AMR/AMI table; Vue 3 box; Related Reading fixed (dedup); +1 FAQ; 5 journey links | ADD ONE Vue 3 box (B0C7B1LKDW, problem-language) | 8→13 links | curiosity→tool journeys; first affiliate signal from tier |
| 18-fuel-adjustment | 24 / 26s / 96% | "what is this fuel line and is it computed right?" | ZERO links; no FAQ; dead end at 560w | 9 links (19, 24, 11, 43, why-did-up); 3 FAQs+schema; symbolic worked example (no numbers); checklist bulletized; Related Reading; disclosure chip | NONE (verification intent — hard no per brief) | 0→9 links | exits from 0 → measurable; TOP holds |
| avg-water-usage | 25 / 13s / 88% | "is my water usage normal?" | never answers its own keyword; no example | answer-first QA reorder; worked example (12 CCF÷30÷3); 2-4 CCF/person benchmark (attributed link); calculator link; 3 FAQs; Related Reading; hero_below_answer | NONE (pre-diagnosis benchmark) | 5→8 links (leak cluster, 44, seasonal) | benchmark satisfied on-page → TOP 13s→30s+ |

## Highest-leverage changes
1. **Production 404 repair** (electric-breakdown → 10-fixed): every click on that link was a lost reader on the tier's best page.
2. **Watch-list TOP fixes** (25-taxes 5.6s, 19-surcharges 4.2s): first-screen routing + label-matching — the site's own 30s+ targets now structurally reachable.
3. **mcf trust repair**: the page's visible glitches (title-echo, stuffing, self-correcting math) were actively signaling low quality.
4. **Journey lattice**: tier went from ~46 → ~105 verified internal links, nearly all at moment-of-need positions; 10/10 pages now have Related Reading; 8/10 gained FAQ+schema.
5. **Smart-meters Vue 3 box**: first intent-matched monetization in the tier; Rybbit tracks `affiliate_click` per ASIN.

## Analytics baseline (pre-change, persisted)
`.rybbit-t11320-2026-08-29/baseline_11-20.json` — per-page visits/pageviews/TOP/bounce + site overview. **Attribution caveat:** this cohort's baseline predates BOTH today's SQ-051..054 evidence wave AND this wave — treat post-deploy deltas directionally.

## Measurement plan (Rybbit, 14-day)
- **Weekly pull:** `scripts/rybbit_snapshot.py` pattern → `metric?parameter=pathname` last-7/last-14 vs baseline json.
- **Primary:** per-page TOP (25-taxes, 19-surcharges, water-usage, state-avg: →30s+); per-page bounce (mcf, smart-meters: −10pts); pages/session site-wide (1.235 → 1.5).
- **Secondary:** visits on 10-fixed (dead-link repair downstream); entrance→2nd-page rate on the 10 (internal-journey success); `affiliate_click` events for B0C7B1LKDW on smart-meters.
- **Guardrail:** if TOP falls while pages/session rises on state-avg/smart-meters (fast-answer effect), that is success, not regression — the plan optimized for answer-then-journey, not dwell maximization.
- **Success = demonstrated by behavioral data 2-4 weeks post-deploy.** Do not declare success at merge.

## Verification evidence
- hugo build EXIT 0 (Commander, independent, full site) · 92/92 unique internal hrefs resolve in rendered tree · 0 JSX artifacts in rendered HTML · faq-schema present on all FAQ pages · frontmatter audit: exactly the ruled changes · arithmetic re-derived (mcf scenario, water example) · PUCO/Duke quotes verbatim in 19.
- Full audit trail: `.squad/SQ-055/` (analysis/, packets/, results-wave1-3/, verification-report.md).
