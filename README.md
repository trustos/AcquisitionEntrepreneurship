# Acquisition Enterpreneurship — team repo

A shared workspace for our "buy small software, rebuild it, scale it" strategy. It holds the strategy playbook, an installable **evaluation skill** that scores any acquisition target, and the growing **deal pipeline** we all contribute to.

## What's in here

| Path | What it is |
|---|---|
| `Software-Acquisition-Playbook.docx` / `.pdf` | The strategy — Bending Spoons lessons + the 24-step framework adapted to a bootstrapped dev team. **Start here.** |
| `acquisition-evaluator.skill` | The **installable skill** that scores any target 0–100. Install this (below). |
| `acquisition-evaluator/` | The skill's editable source (SKILL.md, rubric, scripts). Edit here → repackage. |
| `acquisition-evaluator-AUDIT-v2.md` | The audit that produced v2 of the skill — what was wrong and what changed. |
| `deals/` | The **shared deal pipeline**: one folder per evaluation (`scorecard.md` + `record.json`) plus a combined `deal-log.xlsx`. This is what we all contribute to. |
| `leads/` | Sourcing: `where-to-hunt.md` (marketplaces + communities), the current lead shortlists (`leads.xlsx`, `*-shortlist.md`). |

## Quick start (new colleague, ~5 min)

1. **Get the repo.** Clone it (git) or open the shared folder (Dropbox/Drive). In Claude (Cowork), connect this folder so Claude can read and write it.
2. **Install the skill.** Open `acquisition-evaluator.skill` → click **Save skill** (or Settings → Capabilities → add from the file). It installs into your Claude profile and persists across sessions.
3. **Run your first evaluation.** In any chat: *"evaluate this acquisition target: &lt;url or details&gt;"*. Claude runs the workflow and saves the result into `deals/`.

## How to run an evaluation

Give Claude a target — a listing URL, an asking price, a description, or screenshots — and say "evaluate/score this deal." The skill will reconcile the figures, research the unknowns, ask you only what you can answer, score nine dimensions with hard gates, list what's still unknown, generate seller due-diligence questions, and **save everything to `deals/`**.

Two things that make the score better: tell Claude **your budget ceiling** (e.g. "$3k") so affordability is scored, and **your name** so the evaluation is attributed to you.

## Working as a team (please read)

We all save into the **same `deals/` folder**. To keep that conflict-free:

- **`deals/<target>_<date>[_<analyst>]/record.json` is the source of truth.** One file per evaluation — these never collide in git. Commit/sync these.
- **`deals/deal-log.xlsx` (and `.csv`) is a *derived* file** — regenerated from all the record.json files. **Never hand-merge it.** If git flags a conflict on it, accept either side, then ask Claude to *"rebuild the deal log"* (runs `scripts/rebuild_log.py --dir deals/`), which rebuilds the combined log from everyone's records, sorted by score.
- **Attribution:** each record can carry an `analyst` name, and your evaluation folder gets your name appended — so two people can evaluate the same target without overwriting each other.

**If you use git:** commit each per-deal `record.json` + `scorecard.md`. After pulling teammates' changes, run *"rebuild the deal log."* (`.gitignore` already excludes OS/Python cruft.)

**If you use a shared drive:** it mostly just works — each per-deal folder syncs independently. Only caution: simultaneous saves can create a "conflicted copy" of `deal-log.xlsx`; delete it and rebuild the log.

## Data-integrity rules (don't skip — we got burned once)

A marketplace tool once reported prices **100× too low**, and a $100k business was nearly scored as $1k. v2 guards against this, but the human rules matter:

- **Never trust one source for a number.** Cross-check every dollar figure against a second/authoritative source. For **TrustMRR, read the listing's `.md` page** (`trustmrr.com/startup/&lt;slug&gt;.md`) — **not** the MCP tool, whose dollar fields are unreliable.
- The skill runs `verify_figures.py` automatically (subs×ARPU ≈ MRR, MRR×12 ≈ ARR, asking ÷ annual ≈ multiple). If it flags, stop and reconcile.
- A marketplace "verified" badge is *attested*, not *reconciled from source*. Only source-reconciled revenue lets a deal reach the top tier.

## The framework in one paragraph

Each target scores 0–100 across nine dimensions (operability & upside, PMF/retention, unit economics, moat/defensibility, growth/market, tech/IP, transfer/key-person, deal terms, seller/adverse-selection). Hard **gates** cap the verdict: `growth_lever_fits=false` (the only way to grow it is marketing we can't do) → **Pass**; unaffordable → **Out of Budget**; completeness &lt;45% → **Insufficient Data**; and *unknown* gates keep a verdict **provisional** until verified (so a great-but-unverified deal reads "Promising (provisional)", and reaches **Strong** only after diligence). Tiers: **Strong 75+ · Promising 60–74 · Marginal 45–59 · Pass &lt;45.** Full detail in `acquisition-evaluator/references/rubric.md` and the audit.

## Updating the skill

Edit the source in `acquisition-evaluator/` (the team-competence profile + save config are at the top of `SKILL.md`; weights live in `references/rubric.md` and `scripts/score.py`), then repackage into a fresh `acquisition-evaluator.skill` (keep the same name so it updates in place, not as a duplicate) and re-install. Or just ask Claude to do it.

## Requirements

The skill runs inside Claude's sandbox (Python 3 + openpyxl, handled automatically). To run the scripts yourself: Python 3, plus `pip install openpyxl` for the `.xlsx` log (the `.csv` works without it).
