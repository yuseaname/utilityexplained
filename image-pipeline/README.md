# Universal Website Image Pipeline (Installer)

This folder installs a deterministic, portable image pipeline for scanning a repo, discovering image slots, generating prompts, creating images with the OpenAI Images API, and producing a placement plan. The pipeline is plan-only by default and does not modify site files unless you run placement with `--apply`.

## Execution policy

Scripts should only be executed after explicit confirmation. This installer never runs scripts automatically.

## Quick start (plan-only)

```bash
python image-pipeline/scripts/00_repo_analyze.py
python image-pipeline/scripts/01_discover_slots.py
python image-pipeline/scripts/02_refine_prompts.py
python image-pipeline/scripts/03_generate_images.py --dry-run
python image-pipeline/scripts/04_place_images.py
python image-pipeline/scripts/05_polish_audit.py
```

## Apply HTML placement (opt-in)

```bash
python image-pipeline/scripts/04_place_images.py --apply
```

## Environment

Set `OPENAI_API_KEY` in your environment. The pipeline enforces `gpt-image-1` only.

## Output locations

- Repo profile: `image-pipeline/REPO_PROFILE.md`, `image-pipeline/repo_profile.json`
- Slot prompts: `image-pipeline/prompts/slots/`
- Generated assets: `image-pipeline/generated/` (gitignored)
- Ledger: `image-pipeline/ledger/`

## Determinism and reversibility

- Slot IDs are deterministic and prompt hashes are stable.
- Placement uses backups under `image-pipeline/backups/` only when `--apply` is used.
- Re-running scripts is idempotent and safe by default.
