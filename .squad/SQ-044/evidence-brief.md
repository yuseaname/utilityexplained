# SQ-044 Evidence Brief — utilityexplained.com (Commander-verified)

> Written 2026-08-27 by the Commander (ZCode/GLM-5.3). Every fact below was
> verified directly on disk or via the live Rybbit API this session. Workers:
> treat as ground truth unless your own evidence contradicts it — if it does,
> say so explicitly with file:line or command output.

## 1. What the site is

- **Domain**: utilityexplained.com — Hugo static site (theme `adsense-base`),
  ~121 content markdown files, 509 HTML files in `public/`.
- **Niche**: US utility-bill education — electricity, gas, water, HVAC,
  bill-fee explanations ("why is my electric bill high", "what is CCF on a
  water bill", "how to read a gas meter").
- **Git state**: clean-ish; last commits show a **pivot**: `6d4390c8` "feat
  (monetization): remove AdSense — affiliate pivot (ADR-006)" (2026-08-23),
  category consolidation 17→7, Bill Anatomy illustration series. Some
  modified files uncommitted (GROWTH_LOG, KPI_DASHBOARD, author pages).
- **Menu structure**: 6 hub pages (Electricity, Gas, Water, Heating & Cooling,
  Bill Basics, Glossary) + All Guides/About/Authors/Contact + legal footer.

## 2. Analytics truth (live Rybbit pull, 2026-08-27, TZ America/New_York)

Full snapshot: `.rybbit-snapshot-2026-08-27/snapshot.json` (windows: last7,
prior7, last30 — overview, top-150 pages, referrers, channels, countries).

| Metric | prior7 (08-13→08-20) | last7 (08-20→08-27) | last30 |
|---|---|---|---|
| Sessions | 650 | **860** (+32% WoW) | 1,717 |
| Pageviews | 744 | 943 | 2,108 |
| Bounce rate | 90.9% | **91.3%** | 89.1% |
| Pages/session | 1.14 | **1.10** | 1.23 |
| Avg session duration | 64s | **62s** | 78s |

- **Referrer mix last7**: duckduckgo 277, bing 192, yahoo 88, ecosia 26,
  **google only 22 (~2.6%)**. Bing ecosystem ≈ 68% of search traffic.
- **Countries last7**: US 700, **CN 88 (known ~99%-bounce bot noise)**, CA 19.
- **Top pages last7 (pageviews)**: how-to-lower-electric-bill-complete-guide
  123 (2× the #2), sudden-spike-electricity 52, water-bill-too-high 45,
  reconnection-fee 34, water-meter-running 33.
- Historical: Aug-21 7-day window was ~191 sessions/day with bounce 84.7%,
  pages/session 1.52, duration 80s → engagement has WORSENED since, though
  weekly sessions recovered after a dip.
- **AdSense status: BLOCKED** — Google "Low value content" finding (2026-08-23,
  KPI_DASHBOARD.md). AdSense since REMOVED from the site (ADR-006).

## 3. Monetization state (verified by grep, 2026-08-27)

- `grep -rn "amazon.com" content/` → **0 hits. Zero affiliate links live.**
- `grep -rn "utexplained-20"` → **0 hits anywhere in the repo.**
- `hugo.toml` params: `amazon_tag = 'litwd-20'` — **MISMATCH**: owner's real
  store ID is **`utexplained-20`**. Any links built before fixing this would
  attribute earnings to the wrong tag.
- Existing monetization plumbing to inspect: `add_product_boxes.py` (root),
  `layouts/` (product box partials?), `data/content-remediation-queue.json`.
- One obvious product-recommendation article exists:
  `content/blog/50-best-smart-plugs-standby-power.md`.

## 4. Editorial / trust state (verified)

- 5 author pages under `content/author/` (david-chen, roberto-mendoza,
  marcia-washington, margaret-harrington, tanya-patterson) + editorial-team,
  editorial-policy, methodology, corrections pages. **Authenticity of these
  personas is UNVERIFIED — a compliance/E-E-A-T risk to audit, not assume.**
- KPI_DASHBOARD references "P0 editorial remediation" in GROWTH_LOG Entry 9
  (corpus credibility, original information gain, source traceability,
  truthful author/review disclosures) — the site's own known debt.
- Prior planning docs exist on disk (avoid re-proposing what's already
  planned): `BLUEPRINT.md` (62K), `TRANSFORMATION_BLUEPRINT.md` (32K),
  `GROWTH_LOG.md` (35K), `data/content-remediation-queue.json`,
  `IMAGE_AUDIT_REPORT.md` (15K).

## 5. Mission constraints (from the client)

- Amazon Associates store ID: **utexplained-20**. Enhancement-only, NO rebuild.
- No fabrication of expertise, reviews, testing, pricing, firsthand
  experience. No manipulative SEO / misleading claims / fake reviews /
  hardcoded prices. FTC + Amazon Associates + search-engine policy compliant.
- Deliverable: agency-grade audit — exec summary, site/audience findings,
  competitor analysis, content+SEO audit, UX/conversion plan, compliance,
  prioritized backlog (pages, rationale, priority, effort, measurement,
  revenue relevance), 30/60/90-day roadmap.
- Every page classified: retain / improve / consolidate / redirect / remove /
  replace. Rewrite frameworks for thin/outdated/generic/AI-ish content.

## 6. Worker rules of engagement

- Roots: the repo dir only. Read-only wave 1 (writes only where your packet
  grants `write_paths`).
- Web-enabled seats: cite URL + retrieved date for every external claim.
- Label assumptions vs verified facts. Contradict this brief only with evidence.
