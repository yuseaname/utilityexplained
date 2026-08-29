#!/usr/bin/env python3
"""SQ-050 visual recon — formation: 5 swarm wing + msi local ONLY (no cloud)."""
import json
from pathlib import Path

REPO = "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained"
PARENT = "SQ-050 visual-content recon: highest-priority pages needing stronger imagery for storytelling, engagement, retention, accessibility, and image-search."
FACTS = [
    "Prior image audit (IMAGE_AUDIT_REPORT.md, 2026-08-10): 102 files/10.2MB; 91 articles have hero images (frontmatter); body visuals = 43 generic stock + ~40 article-specific; ONE sitewide og-image (og-default.png); 9 generic utility-*.jpg shared across 45 articles.",
    "Verifier (SQ-045): 90+ pages lack diagrams/tables-as-visuals where topical. Traffic: 860 sess/wk, bounce 91.3% (visual retention is a live hypothesis).",
    "Known visual assets: Bill Anatomy illustration series (Magica gpt-image-2, commit 2743d604), energy-hogs hero chart, annotation-sprite.svg, topic-icons.svg.",
]

def packet(role, mission, extra, *, writes=None, prohibited=("write_file", "edit_file")):
    p = {
        "role": role, "mission": mission, "parent_objective": PARENT,
        "context": extra, "known_facts": FACTS,
        "resources": {"roots": [REPO]},
        "constraints": [
            "Read-only recon — writes only to granted artifact paths. Analysis is of CURRENT state; recommendations belong to the Commander synthesis.",
            "Claims cite file paths / rendered HTML / line numbers.",
        ],
        "authorized_actions": ["read_file", "list_dir", "search", "run_command", "web_search", "web_fetch"],
        "prohibited_actions": list(prohibited),
        "success_criteria": ["Findings delivered with per-page/per-claim evidence."],
    }
    if writes:
        p["resources"]["write_paths"] = writes
        p["prohibited_actions"] = []
    return p

TOP = ("Priority surface (Commander-set): homepage, 6 hubs, flagship how-to-lower-electric-bill-complete-guide, "
       "30-sudden-spike, 06-water-bill-too-high, 28-reconnection, 23-billing-cycle, how-sewer-charges, 03-electric-high, "
       "what-is-ccf, water-meter-leak-indicator, water-meter-running, 05-lower-utility-bills, avg-water-usage, "
       "electric-bill-breakdown, 01-read-electric-bill, 44-lower-water-bill, ccf-calculator, which-rate-plan, "
       "04-fees-hub, 08-ToU, money pages (gadgets, phantom-power, 50-smart-plugs, ev-charging, hvac-stages, "
       "do-programmable-thermostats, 07-gas), 11-kwh, 12-gas-bill, 46-cheapest-hours.")

packets = {}

packets["prospector"] = packet("prospector",
    "Read the ~30 Commander-priority pages IN FULL and assess each page's CURRENT imagery as rendered narrative: hero image (what does it actually depict — check the frontmatter image path and, where possible, the file's presence; describe from filename/alt/context), body visuals (HTML <img> tags: count, subject, placement relative to the page's argument), and the VISUAL STORYTELLING GAP: which critical moments of the page's narrative have no visual anchor (the diagnosis step, the fee table, the before/after, the tool in use). Write the per-page assessment table to your artifact: page | hero (subject+quality) | body imgs (n, what) | alt-quality flag | top-3 missing visual moments. Envelope: the 15 most visually under-served pages among the priority set.",
    TOP + " For each, judge imagery against the page's actual narrative, not against a generic standard.",
    writes=["/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/.squad/SQ-050/artifacts/prospector-image-assessment.md"])

packets["cartographer"] = packet("cartographer",
    "Map visual NEED by page archetype across the whole corpus: (1) archetype taxonomy (diagnostic troubleshooter / fee-definer / how-to action page / product page / hub / tool-calculator / bill-anatomy explainer / comparison page); (2) for each archetype: the 3-5 visual types that archetype canonically needs (annotated-realia, flowchart, data chart, comparison matrix graphic, product-in-context, decision tree, icon set) and which the site currently provides vs lacks (evidence: sample 3-4 pages per archetype); (3) per-archetype visual inventory coverage %; (4) image-SEARCH opportunity map: which archetype queries surface image packs in SERPs (definitional 'what is CCF', 'read meter' how-tos) vs which never will (crisis pages). Envelope: ranked archetype->visual-pattern playbook the briefs will draw from.",
    "You provide the PATTERN layer; prospector provides the page layer. Do not duplicate page-by-page analysis.",
    prohibited=("write_file", "edit_file"))

packets["tracer"] = packet("tracer",
    "The visual RETENTION journey on the top-15 ENTRY pages (by traffic: flagship, 30-spike, 06-water, 28-reconnection, 23-billing, sewer, 03-electric, ccf, leak-indicator, water-meter-running, 07-gas, 05-lower, avg-water, breakdown, 01-read): for each, walk the scroll as a reader: Quick Answer (visual anchor present?), first diagnostic/definitional block, mid-page (where 91%-bounce readers abandon — the first complex block), comparison/tables (graphic or text?), end (product boxes/CTAs context). Report per page: the 2-3 scroll positions where a visual would most plausibly hold attention, and what that visual must SHOW to work there. ALSO trace the image-SEO surface: og:image tag content per page (single default vs per-page), whether an image sitemap exists, alt-text strategy sitewide. File:line evidence.",
    "You are the reader's eye-path. Every recommendation ties to a scroll moment, not a template slot.",
    prohibited=("write_file", "edit_file"))

packets["verifier"] = packet("verifier",
    "Mechanical image audit re-derivation (CONFIRMED/REFUTED/UNVERIFIED + data): (1) per rendered page in public/blog/: count <img> tags, hero presence, alt attribute present + length, loading/decoding attrs; (2) og:image meta per page — how many pages use og-default vs per-page images; (3) image file inventory: formats, sizes, the 9 shared utility-*.jpg usage count per file (generic-stock overuse map); (4) reconcile vs IMAGE_AUDIT_REPORT.md claims (91 heroes, 102 files); (5) accessibility: alt='' vs descriptive alt ratio, decorative vs informative; (6) list every priority page (Commander list in known context) whose ONLY imagery is a shared generic stock photo. Script-backed (write and run greps; quote them).",
    "Numbers from scripts only. The generic-stock overuse map is a key deliverable.",
    prohibited=("write_file", "edit_file"))

packets["mason"] = packet("mason",
    "Digest the STYLE and ASSET layer for brief-writing: (1) read IMAGE_AUDIT_REPORT.md fully — extract every standing decision/convention (naming, formats, sizes, what was deleted and why); (2) inventory static/images/ structure: the Bill Anatomy series files (filenames + the articles they serve), energy-hogs chart, all article-dir image naming patterns; (3) read assets/ + themes SVGs (annotation-sprite, topic-icons) — what reusable visual elements EXIST for composition; (4) from 3-4 of the best-served articles (find them: most images in rendered HTML), extract the de-facto house visual style (flat/photoreal/chart-led, palette cues from filenames + CSS vars in design-system.css if needed). WRITE the style bible + asset inventory to your artifact. Envelope: the 10 reusable style parameters a GPT-Image-2 brief must carry.",
    "Bulk digestion. No judgments about what's missing — inventory and conventions only.",
    writes=["/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/.squad/SQ-050/artifacts/mason-style-bible.md"])

packets["executor"] = packet("executor",
    "Mechanical sweep, script-backed, on the ~30 Commander-priority pages (list in known facts): for each rendered public/blog/<slug>/index.html output one row: slug | hero-img filename | body-img count | alt-present/total | og-image value | total image KB on page | formats. Quote your script. No interpretations.",
    "Pure numbers table. gemma counting rules apply: commands only.",
    prohibited=("write_file", "edit_file"))

packets["scout"] = packet("scout",
    "Tiny recon: list static/images/articles/ directory names and count files per dir (one line each); report which priority pages (from known facts list) have NO image directory. Leads only, fast.",
    "Speed over depth. First action must be a tool call.",
    prohibited=("write_file", "edit_file"))

out = Path("/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/.squad/SQ-050/packets")
out.mkdir(parents=True, exist_ok=True)
Path("/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/.squad/SQ-050/artifacts").mkdir(parents=True, exist_ok=True)
for name, p in packets.items():
    (out / f"{name}.json").write_text(json.dumps(p, indent=1)); print(f"wrote {name}.json")
