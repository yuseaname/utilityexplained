# ROADMAP — utilityexplained AdSense Restoration

Derived from COMPLETION_CONTRACT.md. Page-level truth: ../adsense-audit/. Portfolio truth: ../../PORTFOLIO-PM.md.

## M-001: Clear minor tracker items — Ready
- Goal: resolve the 5 remaining NEEDS-WORK pages
- Completion criteria: ccf-calculator + how-utility-rates-fees ≥1,500 words; zero-traffic pages have documented action; consumer-rights accepted (no action)
- Related ACs: AC-002
- Dependencies: none
- Deliverables: 2 deepened articles; tracker updated
- Risks: scope creep on deepening (keep additions grounded in existing claims/sources)
- Verification: build + qa gates + live word counts
- Status: In Progress

## M-002: Curation waves during wait window — Ready
- Goal: visible ongoing curation (Google "ongoing maintenance" signal)
- Completion criteria: ≥2 waves shipped with advanced `updated:` dates (AC-003)
- Related ACs: AC-003
- Dependencies: none (parallel to M-001; wave 1 = M-001 work itself can count if dated)
- Deliverables: content improvement commits
- Risks: regressions from edits → full gate sweep after each wave
- Verification: git log dates + gate sweep
- Status: Wave 1 in progress (M-001 items + review-fix commit 2156ef42 may seed wave 1)

## M-003: Weekly health monitoring — Ready
- Goal: catch regressions/redirect rot early
- Completion criteria: ≥1 recorded health artifact per week until submission (AC-004)
- Related ACs: AC-004
- Dependencies: health-check script (to create: adsense-audit/health_check.py)
- Deliverables: adsense-audit/data/health/YYYY-MM-DD.json
- Risks: cron output is local-only (no live delivery) — artifacts land in repo; Edgar sees them in sessions
- Verification: file presence per week
- Status: Planned (script this week)

## M-004: Go/no-go + re-review submission — Blocked (by time gate)
- Goal: submit with maximum approval odds
- Completion criteria: AC-001..004 green + go/no-go report delivered; Edgar submits
- Related ACs: AC-005, AC-006
- Dependencies: M-001..003 + date ≥ Nov 21
- Deliverables: FINAL-GO-NOGO.md in .project-manager/
- Risks: submitting too early (R-001)
- Status: Blocked until ~Nov 21

## M-005: Decision capture — Blocked (external)
- Goal: record Google's re-review outcome
- Related ACs: AC-007
- Dependencies: M-004
- Contingency: if rejected again → second remediation cycle from any reviewer signal; contract amendment discussion
- Status: Blocked

## M-006: Revenue progress — Blocked (partially)
- Goal: measurable revenue movement toward $100 portfolio goal
- Related ACs: AC-008 (≥$25 incremental — pending Edgar's confirmation of number)
- Dependencies: Associates baseline (record now); AdSense revenue starts post-approval
- Current baseline to record: Associates earnings since 2026-11-07 (dashboard or last known figure)
- Status: Baseline capture Ready; revenue accrual Blocked

## Now / Next / Later
- Now: M-001 (deepen 2 articles), M-003 (health script + first artifact)
- Next: M-002 wave 2 (second curation pass — pick from GROWTH_LOG backlog), record M-006 baseline
- Later: M-004 report (from ~Nov 21), M-005/M-006
- Out of scope: see contract
