# Prior Planning Artifact Inventory — utilityexplained.com

**Generated:** 2026-08-27 by Mason (SQ-044)  
**Purpose:** Full inventory of every planned initiative, its status, evidence, and gap analysis, so the SQ-044 audit does not re-propose known work.

---

## 1. INITIATIVE REGISTER

### Legend
| Code | Meaning |
|------|---------|
| ✅ DONE | Built, committed, deployed, verified on production |
| 🟡 PARTIAL | Started but incomplete (some files done, or committed but not fully deployed) |
| 📋 PLANNED | Documented in a planning doc but no code written or committed |
| 🗑️ ABANDONED | Planned then explicitly superseded or deprecated |

---

### Initiative 1: Technical SEO Foundation
| Field | Value |
|-------|-------|
| **Name** | Trailing-slash 301, HTTPS, security headers, browser caching |
| **Source doc** | BLUEPRINT.md §4 (Remove/Fix); GROWTH_LOG Entry 1; MISSION_REPORT_2026-08-10 |
| **Status** | ✅ DONE — `.htaccess` created and deployed live (curl-verified 301, HTTPS, headers) |
| **Goal/KPI** | Consolidate duplicate URLs, improve crawl efficiency, PageRank distribution |
| **Evidence** | GROWTH_LOG Entry 1: "Created .htaccess with 301 trailing slash redirects, HTTPS enforcement, non-www redirect, security headers, Gzip, browser caching" — committed 832f361, deployed to Hostinger; MISSION_REPORT confirms live |

### Initiative 2: Image Performance (284MB→8MB PNG→WebP)
| Field | Value |
|-------|-------|
| **Name** | Swap 284 MB article PNGs for webp/AVIF + responsive srcset |
| **Source doc** | BLUEPRINT.md §1 (performance emergency); BLUEPRINT.md §6 (Imagery style); TRANSFORMATION_BLUEPRINT.md §4 (PRESERVE/IMPROVE) |
| **Status** | 🟡 PARTIAL — IMAGE_AUDIT_REPORT completed a separate cleanup (307→102 files, 32.7MB→10.2MB); 76 webp files exist but most article frontmatter still references PNGs per the original audit |
| **Goal/KPI** | Fix LCP, Core Web Vitals, crawl budget, ranking suppression |
| **Evidence** | BLUEPRINT.md: "284 MB across 191 uncompressed PNGs … 8 MB of ready-made .webp alternatives exist and are mostly unused". IMAGE_AUDIT_REPORT: cleaned 307→102 files (67% reduction), 32.7MB→10.2MB (69% reduction) — but this was orphaned-variant deletion, not frontmatter-swap. TRANSFORMATION_BLUEPRINT.md F14: "21MB total webp images" — still referencing PNGs in frontmatter is UNRESOLVED |

### Initiative 3: Hub Page Rebuild (article links)
| Field | Value |
|-------|-------|
| **Name** | Add "Browse Our Guides" sections to all 5 hub pages |
| **Source doc** | GROWTH_LOG Entry 1; BLUEPRINT.md §7 (Information Architecture) |
| **Status** | ✅ DONE — committed 832f361, live on production |
| **Goal/KPI** | Create 86+ new inbound links, reduce orphan pages |
| **Evidence** | GROWTH_LOG Entry 1: "All 5 hub pages rebuilt with comprehensive Browse Our Guides sections — electricity 24 links, water 16, gas 11, utility-bills 21, heating-cooling 14". Later superseded by real hub layout (Initiative 17) |

### Initiative 4: High-Bounce Page Rescues (Phase 1)
| Field | Value |
|-------|-------|
| **Name** | 6 high-bounce article rescues + Quick Answers |
| **Source doc** | GROWTH_LOG Entry 1; MISSION_REPORT_2026-08-10 |
| **Status** | ✅ DONE — committed 832f361 |
| **Goal/KPI** | Reduce bounce on 6 high-traffic pages (sewer charges 90%, past-due 100%, water-meter 91.7%, CCF 88.9%, stormwater 75%, electric rising 100%) |
| **Evidence** | GROWTH_LOG Entry 1: per-page details on Quick Answer additions, internal links, AI-pattern removal; deployed to production |

### Initiative 5: Internal Linking Waves (Phase 2)
| Field | Value |
|-------|-------|
| **Name** | 22-article internal linking + 4 more page rescues |
| **Source doc** | GROWTH_LOG Entry 2 |
| **Status** | ✅ DONE — committed 04fa5ba, deployed |
| **Goal/KPI** | 100+ new contextual internal links; reduce 100% bounce pages |
| **Evidence** | GROWTH_LOG Entry 2: "Electricity batch 7 articles/34 links, Water/Gas batch 7/28, Bills/Fees batch 8/~40". 4 more 100%-bounce pages rescued with Quick Answers. Cumulative: ~250+ new internal links across 30+ articles |

### Initiative 6: 100% Quick Answer Coverage
| Field | Value |
|-------|-------|
| **Name** | Quick Answer sections on all articles |
| **Source doc** | GROWTH_LOG Entry 3 |
| **Status** | ✅ DONE — 97/97 articles (100%) achieved Entry 3; later fluctuated but GROWTH_LOG Entry 7 records 96/96 |
| **Goal/KPI** | Answer-first discipline on every article |
| **Evidence** | GROWTH_LOG Entry 3: "97/97 articles (100%) now have Quick Answer sections" committed via multiple waves (5 commits: 7f9ec01, 69c331e, ea1bbbf, f0034da). Entry 7 baseline says 96 published guides |

### Initiative 7: Email Capture / Newsletter
| Field | Value |
|-------|-------|
| **Name** | Email capture form on all blog articles |
| **Source doc** | GROWTH_LOG Entry 3; TRANSFORMATION_BLUEPRINT.md §11 |
| **Status** | ✅ DONE (Mailchimp static POST form, low-pressure framing). Planned improvements (engagement-triggered, audit-flavored offer) are 📋 PLANNED |
| **Goal/KPI** | Capture email signups |
| **Evidence** | GROWTH_LOG Entry 3: "Email capture: Created newsletter signup partial, integrated on all blog articles". TRANSFORMATION_BLUEPRINT.md §11: planned rewrite of promise + engagement triggers — not yet done |

### Initiative 8: AdSense Slot Architecture
| Field | Value |
|-------|-------|
| **Name** | 3 AdSense slots per article (below_title, mid_article, end_article) |
| **Source doc** | BLUEPRINT.md §10; GROWTH_LOG Entry 3; TRANSFORMATION_BLUEPRINT.md §11 |
| **Status** | 🗑️ ABANDONED — AdSense REMOVED per ADR-006 (commit 6d4390c8, 2026-08-23) after Google "Low value content" block. Site pivoting to Amazon Associates |
| **Goal/KPI** | Revenue per session through AdSense display |
| **Evidence** | Evidence brief: "AdSense status: BLOCKED — Google 'Low value content' finding… AdSense since REMOVED from the site (ADR-006)". GROWTH_LOG Entry 9: formal AdSense review finding. GROWTH_LOG Entry 10: remediation in progress. hugo.toml still carries `amazon_tag = 'litwd-20'` (mismatch) — no Amazon links in content |

### Initiative 9: Top-Tier Page Optimization (Day 2)
| Field | Value |
|-------|-------|
| **Name** | Targeted enhancement of 13 highest-traffic pages |
| **Source doc** | GROWTH_LOG Entry 4 |
| **Status** | ✅ DONE — committed 0db8f7e, deployed |
| **Goal/KPI** | Reduce bounce on 100%-bounce pages (CCF 16s, leak-indicator 10s, taxes/fees 20s, etc.) |
| **Evidence** | GROWTH_LOG Entry 4: per-page analytics-driven fixes (Quick Answer, FAQ schema, broken-markdown repair). Hugo build 547 pages, 0 errors, 0 broken links. Live-verified |

### Initiative 10: Deep-Enhance 16 Pages + Featured-Snippet Pivot
| Field | Value |
|-------|-------|
| **Name** | Feature-snippet Quick Answers + AI-slop removal on 16 articles |
| **Source doc** | GROWTH_LOG Entry 5 |
| **Status** | ✅ DONE — committed, deployed. Pivot from FAQ rich results (deprecated by Google May 7, 2026) to 40-50 word featured-snippet answer blocks |
| **Goal/KPI** | Featured-snippet candidate blocks; semantic completeness |
| **Evidence** | GROWTH_LOG Entry 5: 16 files processed, 165 internal links (allowlist-verified), 0 broken links, Hugo 559 pages. Key strategic pivot documented: Google deprecated FAQ rich results → reinvest in top-answer snippet |

### Initiative 11: SQ-013 Full-Squad Audit Fixes (Aug 21)
| Field | Value |
|-------|-------|
| **Name** | Phantom TOC H2 fix, 444 links canonicalized, footer deterministic, stub article expanded, hub titles shortened, schema corrected, sitemap hygiene, 10 consolidation 301s, IndexNow wired |
| **Source doc** | GROWTH_LOG Entry 6 |
| **Status** | ✅ DONE — all committed 36ca5a18, deployed and live-verified |
| **Goal/KPI** | Technical SEO correctness, crawl efficiency, engagement |
| **Evidence** | GROWTH_LOG Entry 6: 12 items listed with verification (3× deterministic builds, 0 broken links, FAQPage=96 stable, independent Twin Q review). IndexNow key at /f8c073… + CI step |

### Initiative 12: Article Funnel Reorder
| Field | Value |
|-------|-------|
| **Name** | Reorder article template: hero below TOC/answer-first, related promoted before ads, email demoted to last |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §9; GROWTH_LOG Entry 7 |
| **Status** | ✅ DONE — committed 352a3a36 (Phase A batch 1), deployed |
| **Goal/KPI** | Attack 84.7% bounce, 1.52 pages/session — the structural driver |
| **Evidence** | GROWTH_LOG Entry 7: "Article funnel reorder (site single.html override): hero below TOC by default (answer-first on 96/97), related-posts promoted before ad/sources/author/email, email demoted to final slot". Verified in built HTML |

### Initiative 13: mid_article Ad Reinstatement
| Field | Value |
|-------|-------|
| **Name** | Recover mid_article AdSense slot (7429084400, lost in Aug-19 theme-v3 convergence) |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §4; GROWTH_LOG Entry 7 |
| **Status** | 🗑️ ABANDONED — slot was reinstated in code, BUT AdSense has since been REMOVED per ADR-006. Slot config remains in templates but AdSense is gone |
| **Goal/KPI** | Recover lost ad revenue (5-source confirmed regression) |
| **Evidence** | GROWTH_LOG Entry 7: "mid_article ad reinstated (slot 7429084400, lost in Aug-19 theme-v3 convergence — 5-source confirmed): injected after 2nd H2 on eligible articles (59/96)". Superseded by ADR-006 — AdSense removal |

### Initiative 14: Real Hub Layout (hub.html)
| Field | Value |
|-------|-------|
| **Name** | New hub layout template for 5 pillar pages |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §7, §10; GROWTH_LOG Entry 7 |
| **Status** | ✅ DONE — committed 352a3a36, deployed |
| **Goal/KPI** | Unlock nav-level engagement + cluster SEO |
| **Evidence** | GROWTH_LOG Entry 7: "Real hub layout (hub.html): all 5 pillars render answer-first + auto-generated grouped directory + cross-desk nav. Counts: electricity 21, gas 7, water 16, heating 12, bills 29". Twin Q2 50-step review: APPROVE |

### Initiative 15: Homepage Overhaul
| Field | Value |
|-------|-------|
| **Name** | Register readout strip; Most Read rebuilt on theme tokens; trust strip honesty fixes |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §8; GROWTH_LOG Entry 7 |
| **Status** | ✅ DONE (Phase A core) — committed 352a3a36. Full guided-entry triage panel (planned in BLUEPRINT §8 and TRANSFORMATION §8) is 📋 PLANNED |
| **Goal/KPI** | Convert vague arrival → triaged bill question; kill the "Updated 2026" fib |
| **Evidence** | GROWTH_LOG Entry 7: "Register readout strip; Most Read rebuilt on theme tokens (Tailwind blue/gray chips eliminated); trust strip honesty fixes (live guide count; 'Independent — no provider or switch-site ties' replaces the 'Updated 2026' fib)". More extensive homepage blueprint remains planned |

### Initiative 16: Freshness System (updated: frontmatter + rendered review dates)
| Field | Value |
|-------|-------|
| **Name** | Git-derived `updated:` frontmatter on 118 files, rendered "Reviewed:" dates + JSON-LD dateModified + OG |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §9, §12; GROWTH_LOG Entry 7 |
| **Status** | ✅ DONE — committed b22bd82c, deployed |
| **Goal/KPI** | Kill the false "Updated 2026" home page claim; feed Google freshness signals |
| **Evidence** | GROWTH_LOG Entry 7: "118 files git-derived updated: → rendered Reviewed: dates + JSON-LD dateModified + OG article:modified_time (scalar-date fix)". Independent Twin Q2 review: 0 collateral in 118 stamped files |

### Initiative 17: Design De-Slop (CSS overrides)
| Field | Value |
|-------|-------|
| **Name** | Remove generic SaaS visual patterns (glassmorphism, 135° gradients, hover lifts, Tailwind blue/gray chips) |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §4 (Remove), §6; GROWTH_LOG Entry 7 |
| **Status** | ✅ DONE (site-overrides.css) — committed b22bd82c. Full theme-level token refresh (Phase B) is 📋 PLANNED |
| **Goal/KPI** | Palette consistency; distinctive "meter reader" identity |
| **Evidence** | GROWTH_LOG Entry 7: "De-slop (site-overrides.css, loads after canonical design-system): nav backdrop-filter, six 135° gradients, SaaS hover lifts, newsletter gradient flattened; mobile fixed-attachment repaint killed". Canonical theme untouched — Twin Q2 50-step review: APPROVE |

### Initiative 18: Category Consolidation (17→7)
| Field | Value |
|-------|-------|
| **Name** | Merge 17 categories into 7 with 12 server 301s for retired term URLs |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §7; GROWTH_LOG Entry 7 |
| **Status** | ✅ DONE — committed b22bd82c, deployed. URL redirects live |
| **Goal/KPI** | Simplify site architecture, strengthen topical authority clusters |
| **Evidence** | GROWTH_LOG Entry 7: "Categories consolidated 17→7 (Electricity 21 · Gas 7 · Water 16 · H&C 12 · Bills & Fees 29 · Savings & Efficiency 4 · Troubleshooting 7) with 12 server 301s for retired term URLs. Article URLs unchanged". Live-verified 301s correct, new term pages 200 |

### Initiative 19: Trust Page Fixes
| Field | Value |
|-------|-------|
| **Name** | Fix author/_index.md claims, editorial-policy, AI-assistance disclosure |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §13; GROWTH_LOG Entry 7 |
| **Status** | ✅ DONE (Phase A) — committed b22bd82c. Author substance decision (keep personas vs editorial-team identity) is 📋 PLANNED — council escalation, owner-level call |
| **Goal/KPI** | Honest framing; E-E-A-T compliance |
| **Evidence** | GROWTH_LOG Entry 7: "author/_index.md claims fixed ('decades of experience'/'Licensed HVAC Technician' → honest team framing; AI-assistance disclosure retained)". Entry 10 adds editorial-policy/team/author-bio honesty fixes (local, not yet committed) |

### Initiative 20: Image Audit & Cleanup
| Field | Value |
|-------|-------|
| **Name** | Full image inventory, dedup, relevance fix, alt text correction |
| **Source doc** | IMAGE_AUDIT_REPORT.md |
| **Status** | ✅ DONE — 307→102 files (67% reduction), 32.7MB→10.2MB (69% reduction). 36 fabricated alt texts corrected |
| **Goal/KPI** | Eliminate duplicate/orphaned images, fix accessibility, reduce bandwidth |
| **Evidence** | IMAGE_AUDIT_REPORT.md: Full cycle. 222 orphaned files deleted, 40/155 unused variant sets deleted, all alt texts corrected for accurate description. Remaining concern: 4 off-palette blue/teal inline graphics (TRANSFORMATION §14 debt) — 📋 PLANNED for Phase B |

### Initiative 21: Annotated Bill Anatomy Series
| Field | Value |
|-------|-------|
| **Name** | 4 annotated bill diagrams (electric, gas, water, combined) via Magica gpt-image-2-text |
| **Source doc** | GROWTH_LOG Entry 8; TRANSFORMATION_BLUEPRINT.md §14 |
| **Status** | ✅ DONE — committed 2743d604, deployed live |
| **Goal/KPI** | "A guide about visual documents with zero visuals" — provide the missing visual core |
| **Evidence** | GROWTH_LOG Entry 8: "4 original annotated-bill diagrams via Magica, quality high, 1024×1536 portrait. Vision-QA gate: 4/4 PASS (1 regen). 9 figure instances on 6 pages." 2× deterministic builds clean. Footnoted: "4 off-palette inline graphics" still queued (see Initiative 28) |

### Initiative 22: P0 Editorial Remediation (AdSense gate)
| Field | Value |
|-------|-------|
| **Name** | Quarantine + source-led remediation of unsupported data-heavy guides |
| **Source doc** | GROWTH_LOG Entry 9 + Entry 10 |
| **Status** | 🟡 PARTIAL — 7 articles quarantined (draft + 301). Source-led repairs done on 30+ guides. 52 remaining remediation flags. Automated worker running. NO CHANGES COMMITTED YET — all local |
| **Goal/KPI** | Satisfy AdSense "Low value content" policy finding; enable re-review |
| **Evidence** | GROWTH_LOG Entry 9: P0 list (3 articles with impossible/fabricated claims). Entry 10: quarantined 7 articles (3 P0 + 4 future-claim), source-led repairs on LIHEAP, CCF, leak indicator, toilet leak + batches covering electric bill, high bill, water meter, smart meter, standby power, net metering, HVAC, heating, first-apartment, fees. 52 remaining flags |

### Initiative 23: Content Quality Gate
| Field | Value |
|-------|-------|
| **Name** | scripts/content_quality_audit.py + npm run audit:content |
| **Source doc** | GROWTH_LOG Entry 10 |
| **Status** | ✅ DONE — code exists local (uncommitted). Flags future-dated claims + quantitative guides missing source metadata |
| **Goal/KPI** | Automated detection of unsupported claims |
| **Evidence** | GROWTH_LOG Entry 10: "Added scripts/content_quality_audit.py, tests, npm test, and npm run audit:content. Baseline after quarantine: 93 published guides, 85 still flagged for source remediation" |

### Initiative 24: What the site's own docs say about audience/personas
| Field | Value |
|-------|-------|
| **Name** | Audience definition consistency |
| **Source doc** | All planning docs |
| **Status** | ✅ CONSISTENT across all docs — see §5 below |

### Initiative 25: ADR-006 Affiliate Pivot
| Field | Value |
|-------|-------|
| **Name** | Remove AdSense, pivot to Amazon Associates (store ID utexplained-20) |
| **Source doc** | Evidence brief; GROWTH_LOG Entry 9→10; KPI_DASHBOARD.md |
| **Status** | 🟡 PARTIAL — AdSense REMOVED (commit 6d4390c8). Amazon tag in hugo.toml is `litwd-20` (WRONG tag — should be `utexplained-20`). ZERO Amazon affiliate links in content/. Migration NOT complete |
| **Goal/KPI** | Amazon Associates monetization with correct tracking |
| **Evidence** | Evidence brief: "grep -rn 'amazon.com' content/ → 0 hits. grep -rn 'utexplained-20' → 0 hits anywhere in repo. hugo.toml amazon_tag = 'litwd-20' — MISMATCH: owner's store ID is utexplained-20" |

### Initiative 26: Self-Host Fonts
| Field | Value |
|-------|-------|
| **Name** | Self-host Inter, Space Grotesk, Source Serif 4 (remove Google Fonts third-party request) |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §13 |
| **Status** | 📋 PLANNED — listed as council add in transformation blueprint; no code written |
| **Goal/KPI** | Remove render-blocking third-party font request, improve LCP |
| **Evidence** | TRANSFORMATION_BLUEPRINT.md §13: "self-host the font files (council add: Google Fonts preload remains a render-blocking third-party request — self-hosting removes it)" |

### Initiative 27: Search Page (Fuse.js / client-side)
| Field | Value |
|-------|-------|
| **Name** | Add client-side search via Fuse.js |
| **Source doc** | BLUEPRINT.md §7; TRANSFORMATION_BLUEPRINT.md §7 |
| **Status** | 📋 PLANNED — no code written. `/search/` URL exists? (was noindexed in sitemap hygiene — Initiative 11) |
| **Goal/KPI** | Enable self-discovery across 91+ guides |
| **Evidence** | BLUEPRINT.md §7: "Add: /search/ (essential for 91-guide discovery, client-side Fuse.js)". TRANSFORMATION_BLUEPRINT.md §7 lists search as a new/changed template. GROWTH_LOG Entry 6 sitemap hygiene: noindexed /search/ — suggests the page exists but is empty |

### Initiative 28: Off-Palette Inline Graphic Fixes
| Field | Value |
|-------|-------|
| **Name** | Rebuild 4 blue/teal inline graphics (reconnect_fees, reconnect_avoid, ccf-convert, ccf-normal) |
| **Source doc** | IMAGE_AUDIT_REPORT.md; TRANSFORMATION_BLUEPRINT.md §14 |
| **Status** | 📋 PLANNED — queued debt, no code written |
| **Goal/KPI** | Palette consistency |
| **Evidence** | TRANSFORMATION_BLUEPRINT.md §14: "Rebuild 4 off-palette inline graphics (already-queued debt: reconnect_fees, reconnect_avoid, ccf-convert, ccf-normal)". IMAGE_AUDIT_REPORT flagged them |

### Initiative 29: HowTo Schema Enablement
| Field | Value |
|-------|-------|
| **Name** | Enable existing howto/step shortcodes on ~15 instructional articles |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §12 |
| **Status** | 📋 PLANNED — shortcode exists in code (TRANSFORMATION F17: "HowTo schema exists in code but used by 0 articles"); just needs content wiring |
| **Goal/KPI** | Rich results for instructional content (meter tests, dispute process) |
| **Evidence** | TRANSFORMATION_BLUEPRINT.md §12: "HowTo schema: enable existing howto/step shortcodes on the ~15 strongest instructional articles — zero new code, pure content templating" |

### Initiative 30: Glossary Schema Upgrade
| Field | Value |
|-------|-------|
| **Name** | Add DefinedTermSet/DefinedTerm schema to 233-line glossary |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §12 |
| **Status** | 📋 PLANNED — listed as Phase B council add |
| **Goal/KPI** | Rich results for glossary; structured data completeness |
| **Evidence** | TRANSFORMATION_BLUEPRINT.md §12: "Glossary upgrade (council add, Phase B): the 233-line glossary is a natural DefinedTermSet/DefinedTerm schema target — currently absent" |

### Initiative 31: Journey System / Bill Triage
| Field | Value |
|-------|-------|
| **Name** | Four-step entry flow: Which utility? → Which line looks wrong? → Findings → Remedy |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §7, §8 |
| **Status** | 📋 PLANNED — only described as concept; no code written |
| **Goal/KPI** | 1.52→>1.9 pages/session; guided discovery |
| **Evidence** | TRANSFORMATION_BLUEPRINT.md §7: "Journey system ('Bill Triage'): a four-step entry flow — Which utility? → Which line looks wrong? → Findings → Remedy — connecting homepage, hubs, and articles" |

### Initiative 32: Article pairs_with Scoring System
| Field | Value |
|-------|-------|
| **Name** | Add pairs_with frontmatter flag for complementary-intent article linking (score +4) |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §9, §12 |
| **Status** | 📋 PLANNED — requires frontmatter field addition + related.html scoring logic update |
| **Goal/KPI** | Better related-article quality than same-category baseline |
| **Evidence** | TRANSFORMATION_BLUEPRINT.md §9: "same-category +2 → same-utility-pillar +3 · shared tag +1 · complementary-intent flag (pairs_with:) +4" |

### Initiative 33: Hub Instrument Panel Graphics
| Field | Value |
|-------|-------|
| **Name** | 5 hub hero instrument panels (dial/register close-ups per utility) |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §14 |
| **Status** | 📋 PLANNED — not generated |
| **Goal/KPI** | Visual distinctiveness per hub page |
| **Evidence** | TRANSFORMATION_BLUEPRINT.md §14: "Hub hero instrument panels (5): dial/register close-ups per utility" |

### Initiative 34: Unit-Converter Band Graphics
| Field | Value |
|-------|-------|
| **Name** | 6 converter graphics (CCF↔gallons, kWh↔cost, therms↔kWh, etc.) |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §14 |
| **Status** | 📋 PLANNED — not generated |
| **Goal/KPI** | Visual explanation of unit conversions |
| **Evidence** | TRANSFORMATION_BLUEPRINT.md §14: "Unit-converter band graphics (6): CCF↔gallons, kWh↔cost, therms↔kWh, etc." |

### Initiative 35: OG Template (Statement Frame)
| Field | Value |
|-------|-------|
| **Name** | OG social image template with mono readout of article's answer |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §14 |
| **Status** | 📋 PLANNED — not built |
| **Goal/KPI** | Social sharing; SERP CTR |
| **Evidence** | TRANSFORMATION_BLUEPRINT.md §14: "OG system: statement-frame OG template with mono readout of the article's answer" |

### Initiative 36: Video (Optional)
| Field | Value |
|-------|-------|
| **Name** | "Read your meter in 60 seconds" video |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §14 |
| **Status** | 📋 PLANNED — optional, not started |
| **Goal/KPI** | Engagement; visual demonstration |
| **Evidence** | TRANSFORMATION_BLUEPRINT.md §14: "Optional single video (only if motion proves value)" |

### Initiative 37: Author Substance Decision
| Field | Value |
|-------|-------|
| **Name** | Owner-level decision: keep 5 personas with hardened credentials vs consolidate to editorial-team identity |
| **Source doc** | TRANSFORMATION_BLUEPRINT.md §13 |
| **Status** | 📋 PLANNED — council escalation flagged as "DECISION REQUIRED'" owner-level call not yet made |
| **Goal/KPI** | E-E-A-T compliance; truthful representation |
| **Evidence** | TRANSFORMATION_BLUEPRINT.md §13: "Two defensible paths — (A) Keep personas, harden them… (B) Consolidate to a truthful editorial-team identity… Fabricated credentials are forbidden either way. This is an owner-level call" |

---

## 2. P0 EDITORIAL REMEDIATION SCOPE (GROWTH_LOG Entry 9)

Exact demands from GROWTH_LOG Entry 9 (2026-08-23):
> "BLOCKED — do not request another AdSense review yet."

### Immediate P0 Quarantine (done locally, not committed)
| # | Article | Problem | Resolution |
|---|---------|---------|------------|
| 1 | content/blog/7-states-with-worst-utility-spikes-2026.md | Impossible citation "BLS, December 2026" + precise state claims without auditable sources | Quarantined `draft: true` + 301→/blog/why-did-my-utility-bill-go-up-this-month/ |
| 2 | content/blog/2026-utility-cost-index-by-state.md | Claimed "original analysis" with no data file, source URLs, or reproducible methodology | Quarantined `draft: true` + 301→/blog/complete-guide-understanding-utility-bill/ |
| 3 | content/blog/02-average-utility-costs-2026.md | Conflicting total-cost ranges, no source material | Quarantined `draft: true` + 301→/blog/complete-guide-understanding-utility-bill/ |

### Plus 4 future-claim quarantines (from Entry 10 continuation):
| # | Article | Resolution |
|---|---------|------------|
| 4 | content/blog/average-utility-bills-by-state-2026/ | 301→/blog/complete-guide-understanding-utility-bill/ |
| 5 | content/blog/how-to-lower-electric-bill-complete-guide/ | 301→/blog/05-how-to-lower-utility-bills/ |
| 6 | content/blog/stormwater-fee-on-water-bill-explained/ | 301→/blog/44-how-to-lower-water-bill/ |
| 7 | content/blog/why-your-electric-bill-keeps-rising-2026/ | 301→/blog/why-did-my-utility-bill-go-up-this-month/ |

### Required for EVERY retained guide (Entry 9 gate):
1. Verify each material factual claim against a primary source; add visible Sources section
2. Replace generic tables/ranges with cited reproducible calculations or labeled examples
3. Rewrite for distinct reader task (decision rule, worked example, jurisdiction-specific path)
4. Add only useful contextual internal links; remove templated "Related Reading"
5. Keep title, canonical URL, and redirect plan explicit
6. Rebuild, run image + internal-link gates, sample mobile, only then request re-review

### Current state (Entry 10 baseline):
- 89 published guides (after 7 quarantined)
- 52 remaining source-remediation flags (down from 85)
- 0 future-claim findings
- Automated remediation worker running every 5 minutes
- **All changes local/uncommitted — NOT deployed, NOT committed, NOT submitted for re-review**

---

## 3. REMEDIATION QUEUE

### content-remediation-queue.json (generated 2026-08-23)
| Count | Status |
|-------|--------|
| **6 remaining** | All P2 — `missing_sources` issue only |
| 0 | P0 items in queue (handled separately via quarantine) |
| 0 | P1 items |
| **6** | **P2 items** |

### P2 items (6):
| Path | Title | Words | Issue |
|------|-------|-------|-------|
| content/blog/mcf-vs-ccf-vs-therms-on-gas-bill.md | MCF vs CCF vs Therms on Your Gas Bill | 3,228 | missing_sources |
| content/blog/gas-delivery-charge-vs-supply-charge.md | Gas Delivery Charge vs Supply Charge | 3,307 | missing_sources |
| content/blog/tiered-water-rates-explained.md | Tiered Water Rates Explained | 3,421 | missing_sources |
| content/blog/30-sudden-spike-in-electricity-bill-no-usage.md | Sudden Spike in Electricity Bill | 3,583 | missing_sources |
| content/blog/07-gas-bill-too-high.md | Why Is My Gas Bill So High? | 3,616 | missing_sources |
| content/blog/how-to-read-gas-meter.md | How to Read Your Gas Meter | 3,643 | missing_sources |

### Remediation progress (beyond queue):
| Stage | Count |
|-------|-------|
| Original flagged guides | ~92 |
| Quarantined (P0 + future-claim) | 7 |
| Source-remediated (Entry 10 batches) | ~33 guides (LIHEAP, CCF, leak indicator, toilet leak + batches covering electric bill, high bill, water meter, smart meter, standby power, net metering, HVAC, heating, first-apartment, fees) |
| Remaining flags | **52** |
| P2 in remediation queue | 6 (subset of 52) |

---

## 4. DECISIONS / ADRs REFERENCED

| ID | Decision | Source | What it committed to | Status |
|----|----------|--------|---------------------|--------|
| ADR-006 | Remove AdSense, pivot to Amazon Associates | Commit 6d4390c8; evidence brief; GROWTH_LOG Entry 9→10 | AdSense removed from site; switch to Associates store ID `utexplained-20` | 🟡 PARTIAL — AdSense removed. Amazon tag in hugo.toml is WRONG (`litwd-20` not `utexplained-20`). Zero Amazon links in content. Migration not complete |
| (implicit) | Google deprecated FAQ rich results (May 7, 2026) → pivot to featured-snippet Quick Answers | GROWTH_LOG Entry 5 | Replaced FAQ-schema optimization with 40-50 word featured-snippet blocks; keep FAQ sections for readers/AI | ✅ DONE — all articles have featured-snippet QA |
| (implicit) | Category consolidation 17→7 | GROWTH_LOG Entry 7; TRANSFORMATION_BLUEPRINT.md §7 | 12 server 301s; article URLs unchanged; new category taxonomy | ✅ DONE |
| (implicit) | Phase A: site-level overrides only — zero canonical-theme edits | TRANSFORMATION_BLUEPRINT.md §15 | All Phase A changes via site-level overrides; theme-level token refresh deferred to Phase B | ✅ DONE — all committed via site-level overrides |
| (implicit) | Preserve ALL existing URLs — no redirects except for consolidation | BLUEPRINT.md §7; all subsequent docs | Zero URL slug changes; only 301s for retired categories and quarantined posts | ✅ DONE — all existing blog URLs preserved |
| (council escalation) | Author substance — keep personas vs editorial-team identity (owner decision) | TRANSFORMATION_BLUEPRINT.md §13 | Owner must decide; committed to truthful representation regardless | 📋 PENDING — not yet decided |
| (council add) | Self-host fonts | TRANSFORMATION_BLUEPRINT.md §13 | Remove Google Fonts third-party request | 📋 PLANNED |
| (council add) | Glossary DefinedTermSet schema (Phase B) | TRANSFORMATION_BLUEPRINT.md §12 | Add structured data to 233-line glossary | 📋 PLANNED |

---

## 5. AUDIENCE / PERSONAS DEFINED IN SITE DOCS

All five planning docs are **consistent** on the audience:

| Doc | Definition |
|-----|-----------|
| **BLUEPRINT.md** §2 | "US renters, first-time homeowners, and budget-conscious households who open a bill, feel confused/anxious, and Google the specific charge or symptom (why is my electric bill so high, what is CCF on my water bill, delivery charge vs supply charge)." |
| **TRANSFORMATION_BLUEPRINT.md** §2 | Same audience framing: "person holding the bill" — independent consumer-advocate bill decoding. No switching agenda. |
| **MISSION_REPORT** §1 | Implicit: US householder confused by their bill — 77% US traffic, informational intent. |
| **GROWTH_LOG** (all entries) | Analytics confirm: US ~78% users, mobile ~58%, overwhelming informational intent (why/what/how). |
| **Evidence brief** §1 | "US utility-bill education — electricity, gas, water, HVAC, bill-fee explanations" |

**Personas (5 named bylines):**
| Name | Article count (from TRANSFORMATION F8) | Domain (suggested per TRANSFORMATION §7) | Authenticity |
|------|---------------------------------------|----------------------------------------|-------------|
| Margaret Harrington | 52/96 (~54%) | Electricity + editorial lead | UNVERIFIED — compliance/E-E-A-T risk flagged in evidence brief. Bios carry "drafted with AI assistance," no credentials/photos/links |
| Tanya Patterson | 17/96 (~18%) | Rates/fees | UNVERIFIED |
| Roberto Mendoza | 12/96 (~13%) | Water/meters | UNVERIFIED |
| Marcia Washington | 8/96 (~8%) | Assistance programs | UNVERIFIED |
| David Chen | 7/96 (~7%) | Heating/cooling | UNVERIFIED |

**Search intent** (all docs agree): Overwhelmingly **informational + problem-solving** ("why", "what is", "how to read"). Commercial/transactional intent is low. Site docs originally asserted AdSense display was the right model; ADR-006 has since pivoted to Amazon Associates (affiliate), creating an intent-model tension that needs resolution.

---

## 6. TOP-LINE SUMMARY FOR ENVELOPE

### What's Done (verified deployed on production)
1. Technical SEO: trailing-slash 301, HTTPS, security headers, browser caching
2. Hub pages: article-linked hubs (5) + real hub layout (hub.html)
3. Quick Answer sections: 96/96 articles
4. Internal linking: ~775+ links across corpus
5. 13 + 16 = 29 deep article optimizations (bounce fixes, featured-snippet QA, AI-slop removal)
6. SQ-013 fixes: phantom TOC, footer determinism, schema correction, sitemap, 10 consolidation 301s, IndexNow
7. SQ-016 Phase A: article funnel reorder, mid_article reinstated, real hub layout, homepage overhaul, freshness system, de-slop CSS, categories 17→7, trust page fixes
8. Annotated Bill Anatomy series (4 masters, 9 instances on 6 pages)
9. Image audit: 307→102 files, 32.7MB→10.2MB, 36 alt texts corrected
10. AdSense removal (ADR-006)

### What's Owed (planned but not done, or partially done)
1. **Amazon Associates migration**: hugo.toml has WRONG tag (`litwd-20` vs `utexplained-20`). Zero Amazon links in content. This is the #1 revenue gap.
2. **P0 editorial remediation**: 52 remaining source-remediation flags. All remediation work is local/uncommitted — NOT deployed. Automated worker running.
3. **Image frontmatter swap**: 76 webp files exist but most articles still reference heavy PNGs in frontmatter `image:` field.
4. **Author substance decision**: Owner-level call NOT made — personas vs editorial-team identity.
5. **Self-host fonts**: Google Fonts still a render-blocking third-party request.
6. **Search page** (Fuse.js): planned but not built.
7. **HowTo schema**: code exists in templates but used by 0 articles.
8. **Glossary schema** (DefinedTermSet): planned Phase B.
9. **Journey system / Bill Triage**: concept only.
10. **pairs_with scoring**: frontmatter field + scoring logic not implemented.
11. **Hub instrument panels, unit-converter bands, OG template**: media assets not generated.
12. **4 off-palette inline graphics**: queued debt.

### 5 Biggest Gaps Between Planned and Shipped
1. 🚨 **Amazon Associates not operational**: Pivot decided (ADR-006) but no links live, wrong affiliate tag, zero migration — revenue model has no implementation.
2. 🚨 **AdSense remediation incomplete**: 52 content flags remain, 7 articles quarantined, code NOT committed — the site is unmonetized AND cannot re-apply for AdSense.
3. 🔶 **Image PNG→WebP frontmatter swap not done**: 76 webp files exist unused while 284MB of PNGs are still referenced in article frontmatter — LCP/CWV risk persists.
4. 🔶 **P0 editorial work (52 flags) not committed or deployed**: All source-led repairs, quarantine, quality gate are local-only — one disk failure or rollback loses everything.
5. 🔶 **Author compliance unresolved**: Owner-level decision on persona authenticity not made; current state (AI-assistance-disclosed thin personas) is a continuing E-E-A-T risk.
