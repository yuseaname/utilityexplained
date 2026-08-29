# SQ-057 Final Report — APEX Optimization, Traffic Ranks 21-30
**Site:** utilityexplained.com · **Window:** 2026-07-30 → 2026-08-29 (Rybbit, fresh pull 2026-08-29) · **Baseline:** `.rybbit-t11320-2026-08-29/baseline_21-30.json` · **Base commit:** 8628d171

## Formation (8 roles / 10 seats — cloud + swarm + msi; ray/evox2 down, excluded)
Wave 1 recon: prospector · tracer · cartographer · verifier (+ scout DEAD RUN — gemma4:e2b path failure, angles covered by wing). Wave 2 implementation: lieutenant ×3 (capacity duplicates, disjoint write_paths) + mason. Wave 3 verification: verifier (claim re-derivation) + executor (build sweep; protocol-dead — claims salvaged then Commander-verified on disk).

## Diagnosis (wave 1, verified)
The tier inherited the answer-first pattern — **all 10 pages answer their title question in the first ~60 words**. The disease is the journey OUT: every body link sat in the top quarter of every page, 6 endings stranded, 8 pages without Related Reading, 6 without FAQ schema, 2 pages (49-demand, 08-TOU) with ZERO internal links. All arithmetic on the tier was verifier-CONFIRMED pre-wave (0 refuted). All 4 potential cannibalization pairs ruled DISTINCT intents — no consolidations.

## Per-page table

| Page | Baseline (v/TOP/bounce) | Links | FAQ+schema | Main changes | Expected impact |
|---|---|---|---|---|---|
| why-did-water-sudden | 24 / 0.0s* / 91.7 | 3→8 | had | 5 moment-of-need links; 189w leak-check dead zone broken into 4-item checklist (pre-image EPA facts); anchored Next-step ending | journeys into water cluster; metric SUSPECT* |
| 49-demand-charges | 23 / 21.2s / 82.6 | 0→8 | ADDED (5 Q) | full APEX on zero-link page: 5 lattice links, self-check routing line, FAQ+schema from existing content, RR ×6, guided ending; rate-trio cross-links | exits from 0 → measurable |
| 27-connection-fee | 22 / 9.4s / 81.8 | 3→7 | ADDED (5 Q) | first-screen routing self-check (3 branches), 2 links, FAQ+schema, RR, guided ending | TOP watch target 9.4s → 30s+ |
| 08-time-of-use | 20 / 40.6s / 85.0 | 0→8 | ADDED | 6 links (Kasa KP115 box byte-preserved); FAQ+schema; RR; guided ending | zero-link vacuum closed |
| 26-utility-deposit | 20 / 78.0s / 95.0 | 3→7 | schema ADDED (3 Q existed) | links at hardship/refund moments; RR; Next-steps ending | long-read/95%-bounce: journey OUT fixed |
| how-to-read-electric-meter | 20 / 21.1s / 90.0 | 4→15 | had | 5 links (raw-HTML idiom); 85w prose wall → bullets; RR ×6 | reads-to-action journeys |
| 01-how-to-read-bill | 19 / 69.2s / 79.0 | 4→11 | had | 5 links incl. kWh dead-zone break; RR; 'Where to go next' ending | best reader in tier → hub |
| how-to-read-a-water-meter | 19 / 0.5s* / 79.0 | 3→8 | had | 4 links; dial prose → ordered list (pre-image wording); 4-step routine | metric SUSPECT*; structure fixed |
| 21-past-due | 18 / 29.6s / 88.9 | 4→7 | schema ADDED (3 Q existed) | 6 links; 125w LIHEAP dead zone → 4-bullet checklist; RR | assistance journeys |
| tiered-rates | 17 / 17.4s / 88.2 | 3→6 | ADDED (5 Q) | 2 links + trio cross-links; 76w dead zone broken; RR ×6; guided ending | rate-cluster circuits |

\* Commander ruling 1: both near-zero TOP metrics adjudicated LIKELY TRACKING ARTIFACTS (pages are link-dense with schema — inconsistent with mass instant-exit). Fixes shipped on structural grounds; do not chase the zero.

**Tier totals:** unique internal body links 30 → 85 (+183%); FAQ+schema 4/10 → 10/10; Related Reading 2/10 → 10/10; stranded endings 6 → 0.

## Highest-leverage changes
1. **Zero-link vacuum closed** — 49-demand and 08-TOU went from 0 to 8 unique links each; both were high-engagement pages stranding every reader.
2. **Rate-structure trio wired bidirectionally** (49 ↔ 08 ↔ tiered, one seat for consistency) — the site's rate-plan explainer circuit now exists.
3. **26-deposit exit fixed** — 78s reads with 95% exit had nowhere to go; hardship/refund-moment links + guided ending.
4. **Schema gaps**: 6 pages gained FAQPage JSON-LD (2 had FAQ blocks without schema — now closed).
5. **Watch-list structure**: 27-connection 9.4s TOP now has first-screen routing; both SUSPECT metrics structurally treated.

## Verification evidence (three independent layers)
- **Verifier (dsv4, cross-family vs GLM/mason):** 10/10 CONFIRMED, 0 REFUTED — every claim re-derived from git diff + pre-images; facts-frozen audit line-by-line: zero new numbers/dates/programs; Kasa box byte-identical; frontmatter only `updated:`; 3/3 skip-claims honest.
- **Commander disk-check:** hugo build EXIT 0; 667 internal hrefs across the 10 rendered pages — 0 dead; FAQPage schema ×10; Related Reading ×10; 0 template artifacts (scroll-script false positives ruled out vs untouched page); frontmatter grep clean; independent new-number scan — every flagged line traced to pre-image content.
- **Scope:** `git diff` confined to exactly the 10 target files (369 insertions / 58 deletions); write_paths held mechanically.

## Measurement plan (Rybbit, 14-day)
Primary: 27-connection TOP → 30s+; tier bounce (esp. 26-deposit 95→<88); pages/session site-wide (1.235 → 1.4+). Secondary: entrance→2nd-page rate on the 10; visits on leak-cluster pages (downstream of why-did-water links). Guardrail: TOP drops on fast-answer pages = success (answer-then-journey, not dwell). Do not declare success before 2-4 weeks of behavioral data.

## Follow-up queue (not this wave)
- Hub inbound-links per lattice §4 (edits to NON-target pages — e.g. electric-bill-breakdown → 49-demand, 06-water → why-did-water).
- Investigate the two SUSPECT metrics at session level (Rybbit) — likely tracking artifacts.
- Images: tier has zero imagery; SQ-056-style visual audit is a separate mission.

**Artifacts:** `.squad/SQ-057/` — evidence-brief.md, analysis-input/cartographer-lattice.md (84-page intent map), packets/, results-wave1|2|3/, FINAL-REPORT.md.
