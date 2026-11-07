# Completion Contract — utilityexplained AdSense Restoration

Status: DRAFT awaiting Edgar's confirmation (2 parameters flagged: revenue number, submission window)

## Desired Outcome
utilityexplained.com is re-approved by Google AdSense (ads serving again), the site's quality system is verified green at submission time, and the site shows measurable revenue progress toward the portfolio's $100 commission goal.

## Required Deliverables
1. Remediated site — DONE 2026-11-07 (4 waves + review fix, live-verified; see adsense-audit/)
2. All 5 minor tracker items resolved or explicitly accepted (M-001)
3. Ongoing-curation evidence: ≥2 content-improvement waves shipped during the wait window, with visible updated-dates (M-002)
4. Weekly health checks recorded while waiting (301 integrity, sitemap, traffic, indexation) (M-003)
5. Final go/no-go verification report delivered to Edgar (M-004)
6. AdSense re-review requested by Edgar (owner action) (M-004)
7. Google's decision captured; if approved → revenue tracking begins (M-005/M-006)

## Acceptance Criteria
- [ ] AC-001: Live gate sweep passes on all 174 URLs: 0 non-200, exactly 1 H1 each, JSON-LD parses, 0 shortcode/heading leaks, 0 numbered slugs (tool: adsense-audit/crawl.py + gate script)
- [x] AC-002: 5 minor tracker items cleared or explicitly accepted — consumer-rights accepted-thin; ccf-calculator (1,347w) + rates-fees (1,448w) deepened past the audit's <1,200 thin gate; 3 zero-traffic pages documented MONITORING (seasonal). Evidence: commit 5e1bb624, adsense-audit/data/inventory.json (170 FIXED + 4 monitoring/accepted)
- [ ] AC-003: ≥2 curation waves shipped post-2026-11-07 with `updated:` dates advancing (git evidence)
- [ ] AC-004: Weekly health check artifacts recorded in adsense-audit/data/health/ (≥1 per week during wait)
- [ ] AC-005: Go/no-go report issued with GO recommendation grounded in AC-001..004 evidence
- [ ] AC-006: Edgar confirms re-review submitted (dashboard screenshot or statement)
- [ ] AC-007: AdSense approval confirmed (ads serving — dashboard status or live ad-slot rendering)
- [ ] AC-008: Revenue progress: ≥$25 cumulative incremental revenue (Associates + AdSense) from project start (2026-11-07) to completion — FLAGGED NUMBER, needs Edgar's confirmation or adjustment

## Quality Requirements
- Reliability: every deploy passes CI (hugo build + check_rendered_output + qa_content)
- Factual integrity: no fabricated claims ever; EIA/gov figures verified same-day; FAQ answers restate in-article claims only
- Monetization hygiene: affiliate disclosures preserved; AdSense suppressed on affiliate pages (existing design)
- Maintainability: tracker (adsense-audit/) updated at every wave; PM records current

## Launch or Handoff Requirements
- Edgar clicks "request review" in the AdSense dashboard after receiving the go/no-go report (his explicit choice, answer #4)

## Constraints
- Time: re-review submission target window Nov 21–28, 2026 (≥2 weeks clean serving after 2026-11-07 fixes)
- Budget: $0 additional spend (existing infra)
- Technology: Hugo static site, GitHub Actions → Hostinger; no stack changes
- Permissions: no destructive actions without approval; AdSense dashboard is owner-only
- Unknown (needs checking): direct GSC access for indexation monitoring (site has verification meta; dashboard access unconfirmed)

## Explicitly Out of Scope
- Other portfolio sites (see PORTFOLIO-PM.md)
- Site redesign / rebranding
- New revenue channels beyond AdSense + Amazon Associates
- Chasing Google's new-domain ranking suppression with black-hat tactics

## Acceptance Authority
Edgar (owner). Final Completion Report requires his acceptance.

## Completion Evidence
Live sweep outputs, adsense-audit/data/ inventory state, git history, weekly health artifacts, go/no-go report, Edgar's submission confirmation, AdSense status, Associates/AdSense revenue reports.
