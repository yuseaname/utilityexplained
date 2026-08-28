# AdSense Content Remediation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn Utility Explained’s published corpus into a source-traceable, reader-useful, technically validated site before requesting another Google AdSense review.

**Architecture:** Remove or redirect objectively unreliable pages first, preserving visitors through explicit server redirects. Add a small, dependency-free Python audit that turns the editorial requirements into repeatable evidence. Then repair the highest-risk trust pages and published guides in focused, sourced batches; no large-scale AI expansion or invented citations.

**Tech Stack:** Hugo 0.141, Markdown content, Apache `.htaccess`, Python 3 standard library, existing Hugo build and asset checker.

## Global Constraints

- Do not request an AdSense review, deploy, commit, or push in this remediation pass.
- Do not fabricate sources, credentials, statistics, editorial review, or author identities.
- Retain URL equity: every removed published URL must receive a permanent redirect to the closest truthful replacement.
- Use primary sources for material rates, regulatory rules, program eligibility, and numerical claims.
- Do not use raw word count as a publication-quality proxy; use it only to prioritize manual review.
- Preserve the current theme and approved SQ-016 UX work unless a content-policy defect requires a targeted change.

---

## File Structure

| File | Responsibility |
|---|---|
| `static/.htaccess` | Permanent redirects for withdrawn pages. |
| `content/blog/*.md` | Published guides; P0 pages become Hugo drafts after redirect coverage exists. |
| `scripts/content_quality_audit.py` | Dependency-free content inventory and evidence gate; reports each missing requirement deterministically. |
| `tests/test_content_quality_audit.py` | Regression tests for source parsing, future-date detection, and audit failure semantics. |
| `package.json` | Repeatable `audit:content` and `verify` commands. |
| `content/editorial-policy.md`, `content/editorial-team.md`, `content/author/*.md` | Truthful disclosure of authorship, review, and sourcing. |
| `GROWTH_LOG.md`, `KPI_DASHBOARD.md` | Handoff status and re-review gate. |

---

### Task 1: Build the deterministic content inventory and quality gate

**Files:**
- Create: `tests/test_content_quality_audit.py`
- Create: `scripts/content_quality_audit.py`
- Modify: `package.json`

**Interfaces:**
- Produces: `python3 scripts/content_quality_audit.py [--strict] [--content-root PATH]`.
- Exit codes: `0` for a readable inventory in normal mode; `1` in strict mode when a published guide has an audit failure.
- A published guide must be flagged when it has a future-dated factual claim, a missing source URL for a material quantitative claim, or no `sources:` front-matter list.

- [ ] **Step 1: Write failing tests**

Create fixture Markdown with a valid `sources:` front-matter list, a future date string, and a quantitative claim. Assert that `audit_file()` returns the expected `future_claim` and `missing_sources` issue codes.

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_content_quality_audit -v`

Expected: failure because `scripts.content_quality_audit` does not exist.

- [ ] **Step 3: Implement the minimal audit**

Parse YAML-style front matter without third-party dependencies; inventory published `content/blog/*.md`; detect direct `http(s)` links, a nonempty `sources:` list, material quantitative claims, and dates later than the current date. Print a page-level table and totals. Strict mode must return `1` if any published guide has an issue.

- [ ] **Step 4: Run tests and inventory**

Run:

```bash
python3 -m unittest tests.test_content_quality_audit -v
python3 scripts/content_quality_audit.py
```

Expected: tests pass; inventory exits `0` and reports existing gaps without modifying content.

- [ ] **Step 5: Add repeatable package scripts**

Add:

```json
"audit:content": "python3 scripts/content_quality_audit.py",
"verify": "hugo --minify --gc && python3 scripts/check_image_paths.py public && python3 scripts/content_quality_audit.py"
```

Do not replace `npm test` with a green claim while the site still has known content findings.

### Task 2: Quarantine objectively unreliable P0 content without dead URLs

**Files:**
- Modify: `content/blog/7-states-with-worst-utility-spikes-2026.md`
- Modify: `content/blog/2026-utility-cost-index-by-state.md`
- Modify: `content/blog/02-average-utility-costs-2026.md`
- Modify: `static/.htaccess`

**Interfaces:**
- Each withdrawn article gets `draft: true` in its existing front matter.
- Apache redirects each old route to the closest live, truthful general guide:
  - `/blog/7-states-with-worst-utility-spikes-2026/` → `/blog/why-your-electric-bill-keeps-rising-2026/`
  - `/blog/2026-utility-cost-index-by-state/` → `/blog/average-utility-bills-by-state-2026/`
  - `/blog/02-average-utility-costs-2026/` → `/blog/average-utility-bills-by-state-2026/`

- [ ] **Step 1: Confirm redirect syntax and existing route convention**

Read `static/.htaccess`; add exact `Redirect 301` or `RewriteRule` entries consistent with its existing rules.

- [ ] **Step 2: Add redirects before drafts**

Add the three permanent redirects, then inspect the generated `public/.htaccess` after a Hugo build.

- [ ] **Step 3: Mark only the three P0 articles as drafts**

Add `draft: true` to their existing YAML front matter. Do not delete files or alter their body text; they remain available for source-led rebuilding.

- [ ] **Step 4: Build and prove withdrawal**

Run `hugo --minify --gc`. Assert the three old output routes are absent from `public/`, their redirect rules exist in `public/.htaccess`, and no retained article directly links to those URLs.

### Task 3: Correct trust disclosures that overstate verification

**Files:**
- Modify: `content/editorial-policy.md`
- Modify: `content/editorial-team.md`
- Modify: `content/author/*.md`

**Interfaces:**
- Public language distinguishes drafting assistance from documented source verification.
- It never says every article was reviewed against primary sources unless that article has visible dated source links.
- It does not make unverified personal credential or identity claims.

- [ ] **Step 1: Inventory claims**

Search trust and author pages for “reviewed,” “primary sources,” “editor,” “credentials,” and “fact-check.”

- [ ] **Step 2: Apply minimal truthful copy changes**

State the actual standard going forward: data-heavy guides are published or refreshed only with visible source links and a review date; older content is being reviewed. Avoid claiming a review that cannot be evidenced.

- [ ] **Step 3: Verify rendered trust routes**

Build Hugo and inspect the generated pages for the retired claims and the new remediation disclosure.

### Task 4: Start source-led repair of the retained high-priority guides

**Files:**
- Modify one guide at a time from the highest-risk retained list generated by Task 1.
- Modify `GROWTH_LOG.md` with the exact source URLs and review status per guide.

**Interfaces:**
- A repaired guide must expose a dated `## Sources` section containing direct first-party/official URLs.
- Source-linked quantitative claims must match its listed sources or be removed/recast as illustrative examples.
- Each repaired guide must preserve its slug, title, and factual scope unless consolidation is explicitly chosen.

- [ ] **Step 1: Select one retained guide only**

Prioritize a high-traffic guide with material claims and a clear authoritative source set. Do not batch-create citations.

- [ ] **Step 2: Retrieve and read primary sources before editing**

Use EIA, DOE, state PUC, program-owner, or utility tariff pages. Capture exact URLs and update date.

- [ ] **Step 3: Rewrite only claims supported by retrieved evidence**

Remove stale unsupported tables, label worked math as an example, and add a visible Sources section.

- [ ] **Step 4: Verify the guide**

Run the quality gate against the guide, Hugo build, HTML source inspection, and internal-link validation.

### Task 5: Final verification and agent handoff

**Files:**
- Modify: `GROWTH_LOG.md`
- Modify: `KPI_DASHBOARD.md` only if the actual gate status changes.

- [ ] **Step 1: Run the full local verification suite**

```bash
python3 -m unittest tests.test_content_quality_audit -v
npm run audit:content
hugo --minify --gc
python3 scripts/check_image_paths.py public
git diff --check
```

- [ ] **Step 2: Document actual results, not projected results**

Record withdrawn pages, redirect map, quality-gate findings, repaired pages, outstanding count, and the explicit “do not request review” status if any strict findings remain.

- [ ] **Step 3: Handoff without deploying**

Leave all changes uncommitted for review. The next agent must begin with `git diff`, run the audit, and use the plan’s Task 4 source-led workflow.

## Plan self-review

- Coverage: P0 unsafe content, source traceability, disclosure truthfulness, automated prevention, retained-page repair, build verification, and handoff are each assigned to a task.
- Scope: no theme redesign, ad-density change, mass AI expansion, deployment, commit, or re-review is included.
- Ambiguity resolved: “quality” means evidence-backed reader utility and honest disclosures; a word-count threshold alone does not determine publication.
- No placeholder scan: no TBD/TODO items remain.
