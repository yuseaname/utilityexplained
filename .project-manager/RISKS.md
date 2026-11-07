# RISKS — utilityexplained AdSense Restoration

## R-001: Re-review submitted too early
- Probability: Medium | Impact: High
- Evidence: Google's rejection was recent; fixes deployed 2026-11-07
- Trigger: submitting before ~2 weeks clean serving + re-indexation of new URLs
- Mitigation: hard date gate Nov 21; AC-004 health artifacts must show stable serving
- Contingency: if submitted early and rejected, wait longer before second request (requests are limited)
- Status: Monitoring

## R-002: Google rejects again despite quality fixes
- Probability: Medium | Impact: Critical
- Evidence: "low value content" verdicts often include site-age/footprint factors; site is ~11 months old with small Google-indexed share (841 Google referrals vs 5,300 Bing/DDG, 90d)
- Trigger: reviewer samples pages but site-level factors dominate
- Mitigation: curation waves (M-002) + time; grow Google footprint before submission
- Contingency: second cycle from any reviewer signal; contract amendment discussion with Edgar
- Status: Open

## R-003: Old-URL 301 rot or re-indexation failure
- Probability: Low | Impact: Medium
- Evidence: 35 redirects verified 2026-11-07; RedirectMatch fix deployed
- Trigger: hosting config changes, .htaccess regeneration drift
- Mitigation: weekly health check samples redirects (T-004)
- Status: Monitoring

## R-004: Revenue threshold (≥$25 proposed) not reached by completion
- Probability: Medium | Impact: Low (definition flexibility)
- Evidence: revenue is market-dependent; Associates clicks exist (89 monetized pages) but volume unproven
- Mitigation: honest trajectory documentation if absolute number missed; contract allows amendment
- Status: Open

## R-005: Content edits during wait introduce regressions
- Probability: Low | Impact: Medium
- Evidence: today's review caught a pre-existing leak class; edits always carry risk
- Mitigation: full gate sweep after every wave (established pattern)
- Status: Mitigated (process exists)

# DECISIONS

## D-001: Definition of completion includes Google's approval
- Date: 2026-11-07 | Status: Accepted (Edgar, clarify session)
- Decision: project runs until AdSense approval, not just submission
- Consequence: timeline is partly external; M-005 may take weeks

## D-002: Wait-window scope = full momentum
- Date: 2026-11-07 | Status: Accepted (Edgar)
- Decision: fix 5 minor items + keep shipping curation improvements
- Consequence: M-001/M-002 active now

## D-003: Revenue included in completion
- Date: 2026-11-07 | Status: Accepted (Edgar); threshold number pending
- Decision: ≥$25 incremental proposed; Edgar to confirm/adjust

## D-004: PM system location
- Date: 2026-11-07 | Status: Accepted
- Decision: .project-manager/ in repo; adsense-audit/ stays page-level truth; PORTFOLIO-PM.md stays portfolio truth
- Rationale: no duplicate sources of truth

# CHANGELOG
- 2026-11-07: PM system created; contract drafted (2 params flagged); M-001 started
