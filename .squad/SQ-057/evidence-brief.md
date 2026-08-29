# SQ-057 Evidence Brief — Wave 2 (Implementation)
**Mission:** APEX engagement pass, traffic ranks 21-30 · **Baseline:** `.rybbit-t11320-2026-08-29/baseline_21-30.json` · **Pristine base:** git 8628d171

## Wave-1 verified findings (all seats, read-only)

| Seat | Verdict | Load-bearing findings |
|---|---|---|
| tracer | COMPLETE | 0 dead links in tier (126-entry slug+alias lookup). ALL 10 pages pass first-screen (Quick Answer present ~60w). **ALL body links sit in the top quarter of every page** — mid/late page is a link desert. 6 stranded endings. Dead zones: why-did-water 189w, water-meter 128w, 21-past-due 125w, 01 114w, electric-meter 85w, 49-demand 82w, 26-deposit 79w, TOU/tiered 76w, 27-connection 68w. |
| cartographer | COMPLETE | 84-page corpus mapped, 7 intent families. All 4 cannibalization pairs = DISTINCT intents (link, never consolidate). Per-page link topology with anchor text in `.squad/SQ-057/analysis-input/cartographer-lattice.md` §3 (lines 260-562). Commander disk-checked ALL 21 proposed new link targets — every one exists. |
| prospector | COMPLETE (1 claim violation: extraction file never landed — findings live in envelope only) | Only 08-TOU has monetization (Kasa KP115 box). Only 01 has a "Next step" line. 0/10 have self-check gates. Priority: 49-demand > 08-TOU > tiered > 27-connection > electric-meter > 26-deposit > 01 > 21 > why-did-water > water-meter. |
| verifier | COMPLETE | 13 claims: 9 CONFIRMED / 0 REFUTED / 4 UNVERIFIED. ALL arithmetic on the 10 pages confirmed (water-meter 1255−1247=8 CCF ×748=5,984 gal ✓; tiered 400×$0.28+$150×$0.38=$169 ✓; TOU load-shift table ✓). Baseline matches snapshot 10/10 (visits/pageviews). None of the 10 targets is a protected SQ-053/054 watch alias. |
| scout | DEAD RUN | gemma4:e2b path failure + confabulated files_touched. Angles fully covered by the wing. No rescue. |

## Commander rulings (BINDING for wave 2)

1. **top_s anomalies (why-did-water 0.0s, water-meter 0.5s):** tracer adjudicates LIKELY TRACKING ARTIFACT (both pages are link-dense with FAQ+schema — inconsistent with mass instant-exit). RULING: implement the engagement fixes anyway (needed on structural grounds); record both metrics as SUSPECT in reporting; do not "chase the zero."
2. **VETO — Load-Shift table rounding corrections** (verifier flagged ~$66→$67, ~$80→$82 on 08-TOU). The tilde-marked figures are approximations within $2 of the re-derived values; the intermediate exact values are correct. No edit. Trust repairs are for WRONG math, not tilde-consistent rounding.
3. **NO new product boxes.** Keep 08-TOU's existing Kasa KP115 box as-is. No ASIN is approved for invention anywhere in this tier.
4. **NO consolidations.** All 4 cannibalization pairs ruled distinct intents.
5. **Every inserted internal link must resolve** — the 21 new targets in the lattice are Commander-verified, but verify the exact slug at insertion time (typo guard); skip+log anything that doesn't match.
6. **Images are out of scope** (mission boundary; none of the 10 has image wiring).
7. **No `hugo` builds from worker seats** (parallel build races). Wave 3 owns the single authoritative build.
8. **Scope = the 10 target files only.** Hub inbound-links from other pages (lattice §4) go to the follow-up queue, not this wave.
9. **Facts frozen:** SQ-051..054 audited the facts. FAQ answers must be derived from the page's EXISTING content — no new numbers, no new sources, no new claims. Frontmatter: change ONLY `updated:` → 2026-08-29.

## FAQ inventory (Commander grep, supersedes prospector's misassignment)

- FAQ+schema PRESENT (do not duplicate): why-did-water, how-to-read-electric-meter, 01, how-to-read-a-water-meter
- FAQ MISSING (add, from existing content): 49-demand, 27-connection, 08-TOU, 26-deposit, 21-past-due, tiered
- Related Reading MISSING on 8 (all but why-did-water, water-meter)

## Per-page APEX plans

Full link tables (section, anchor text, target, why-here) live in `cartographer-lattice.md` §3 — each packet names its targets. Summary:

| # | Page (rank) | Links now→plan | Add FAQ | Add RR | Ending | Special |
|---|---|---|---|---|---|---|
| 23 | why-did-my-water-bill-suddenly-increase | 3→8 | has | has | fix to guided | Break 189w leak-check dead zone; hub page |
| 30 | how-to-read-a-water-meter | 3→6 | has | has | guided-thin → strengthen | Break 128w dial dead zone; metric SUSPECT |
| 24 | 49-demand-charges | 0→5 | ADD | ADD | stranded → guided | Thinnest page (441w); routing self-check line; FAQ from existing content only |
| 26 | 08-time-of-use-electricity | 0→6 | ADD | ADD | stranded → guided | Keep Kasa box; no new boxes |
| 32 | tiered-electricity-rates-explained | 3→5 | ADD | ADD | stranded → guided | Cross-link trio w/ 49 + 08 (one seat owns all three) |
| 29 | 01-how-to-read-your-electric-bill | 4→5 | has | ADD | semi-guided → guided | Break 114w kWh dead zone; keep Next-step line |
| 28 | how-to-read-electric-meter | 1→5 | has | ADD | stranded → guided | Dead zone 85w |
| 31 | 21-past-due-balance | 4→6 | ADD | ADD | fix | Break 125w LIHEAP dead zone |
| 27 | 26-utility-deposit-explained | 3→5 | ADD | ADD | stranded → guided | 78s-read/95%-exit: journey OUT is the disease |
| 25 | 27-utility-connection-fee | 3→5 | ADD | ADD | stranded → guided | TOP 9.4s watch target → 30s+ via first-screen routing |

## House patterns (exemplars on disk)

- "Next step:" journey line after Quick Answer: `content/blog/what-is-ccf-on-a-water-bill.md`
- FAQ shortcodes + single `{{< faq-schema >}}` after content, before `## Sources`: `content/blog/how-utility-rates-fees-usage-work-together.md`
- Full SQ-055 treatment reference: `content/blog/23-utility-billing-cycle-explained.md`
- `## Related Reading` goes after main content, BEFORE FAQ section
- Contextual inline links with descriptive reader-purpose anchors (never "click here"), placed at moment-of-need — NOT end-of-page dumps
