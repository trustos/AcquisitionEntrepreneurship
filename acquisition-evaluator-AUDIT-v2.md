# Acquisition Evaluator — audit & v2 upgrade

*Audit of the skill after 8 real evaluations, an independent red-team pass, and a line-by-line review of the scoring code. Then: what I changed (v2), and a before/after re-score of all 8 deals.*

---

## Executive summary

The skill's **research and honesty were good** — it correctly steered away from four marketing-dependent content/affiliate sites, tagged provenance, and generated sharp seller questions. But the audit found that **the rigor lived in prose the score never enforced.** The number that ranked deals was miscalibrated in four ways that a real buyer would feel:

1. **Budget was collected, then ignored by the math** — so a $100k business (Synta) sat at the *top* of the leaderboard as "Marginal 56," 33× over budget.
2. **"Unknown" was punished like "bad,"** and gate-caps made **STRONG literally unreachable** — so a great-but-unverified deal was indistinguishable from a mediocre one, and the tool could only ever say Pass/Marginal.
3. **No data-integrity step** — which is exactly how the 100× TrustMRR error reached a scorecard.
4. **The competence gate was too vague to apply the same way twice** — it flipped between two near-identical in-stack SaaS.

All four are fixed in **v2** (packaged, ready to install). The re-score below shows the practical effect: the unaffordable "winner" is now flagged **OUT OF BUDGET**, two pre-revenue deals correctly become **INSUFFICIENT DATA** instead of false-confident tiers, and the junk stays Pass — now via a *reproducible* gate rather than a judgment call.

Note: we ran **8** evaluations, not 9 — 1Lookup was researched but never formally scored. (The red-team caught that.)

---

## Method

- **Test set:** the 8 saved evaluations (`deals/`), scores 23.6–56.
- **Independent red-team:** a fresh agent with no prior context critiqued the rubric, weights, gates, and `score.py`, grounded in the files. It independently re-discovered the 100× data failure and proved (by running the script) that STRONG was unreachable.
- **Code review:** line-by-line of `score.py` + the rubric anchors.

---

## Gap analysis (prioritized) — and what v2 does about each

### P0 — critical

**P0-1 · Affordability was never scored.** Budget was asked for in Phase 3 and used nowhere. Deal Quality scored the *multiple*, not the *cash*. Evidence: Synta ($100k, 33× budget) scored highest of all 8.
→ **v2:** a computed **affordability gate** (`asking_price` vs `budget_ceiling`, with a financing flag). Over budget with no financing → **OUT OF BUDGET**, shown next to the merit tier ("STRONG on merits, but 33× budget"). Deal-terms dimension now weighs absolute cash, not just the multiple.

**P0-2 · "STRONG" was unreachable; unverified deals were mislabeled "Promising."** `ip_transferable` and `not_fragile` are ~always unknown/false pre-diligence, and v1 capped merit on `unknown` the same as on `false` — so every deal was clamped to "Promising" forever, and a 95-merit unverified gem read identically to a mediocre 62. There was also no re-score loop, so STRONG was dead code.
→ **v2:** two kinds of gate. **Kill gates** (verified-*false* facts) cap merit. **Verification gates** (*unknown*) do **not** lower merit — they mark the verdict **(provisional)** and block STRONG until verified. STRONG is now reachable after diligence, and the re-score loop is written into the workflow. Tier names are consistent (the phantom "Investigate" is gone).

**P0-3 · No figure-reconciliation — the hole the 100× bug fell through.** The revenue gate checked whether the seller *could* show data, not whether our own numbers were sane or cross-checked. A marketplace badge counted as "verified."
→ **v2:** a mandatory **Phase 2.5 "Verify & reconcile"**: two-source rule (for TrustMRR, the `.md` page, not the MCP), a bundled **`verify_figures.py`** that flags arithmetic impossibilities (subs×ARPU ≈ MRR, etc. — it catches the exact 100× error), and **graded revenue evidence** (`buyer_verified` > `marketplace_attested` > `seller_claimed` > `none`) where only source-reconciled clears to STRONG.

**P0-4 · The competence gate was vague and applied inconsistently.** "Operate *and* scale" bundled two questions; the operator set it `true` for pomocalm and `false` for WebTracky — both in-stack SaaS.
→ **v2:** split into **`operable`** (can we run the stack — engineering test) and **`growth_lever_fits`** (is the #1 acquisition channel product-led/organic vs sales/SEO/paid/personal-audience — with a decision tree). Only the second is the "buying your weakness" cap.

### P1 — important

**P1-1 · "The value walks away with the founder" had no home** (WebTracky's YouTube, DentFlow's dentist). → **v2:** a new dimension **Transfer / key-person** (weight 10) + a **`value_transfers`** gate.

**P1-2 · The "marketing problem" was triple-counted** (build-fit + moat + competence = 35 pts + a gate), so the total carried little independent signal. → **v2:** dimensions orthogonalized — operability = can-we-run-it; moat = defensibility judged team-independently; "can we run the channel" lives only in the gate. Weights rebalanced.

**P1-3 · Unknowns were double-penalized** (scored as 1 = "bad business," then confidence was merely decorative and never gated the tier). → **v2:** the **golden rule — score unknowns NEUTRAL (2) + confidence `unknown`**, and **completeness < 45% → INSUFFICIENT DATA** (no false-confident tier on thin data).

**P1-4 · Two gates fired on 100% of deals** (`ip_transferable` unknown 8/8; `not_fragile` false 7/8) — non-discriminating constants that just lowered the ceiling. → **v2:** `not_fragile` re-scoped to *structural* single-points-of-failure only (platform lock, one customer >30%, a sole non-transferable channel); ordinary early thinness is graded in Moat/Transfer, not a kill-gate. Unknown IP no longer caps merit.

### P2 — addressed
Seller/adverse-selection up-weighted 7→10 (P2-1); compliance/privacy added to the DD guide + seller questions (P2-2); consistent tier naming (P2-3); input validation in `score.py` — missing dims / bad confidence are flagged, not silently zeroed (P2-5); "re-verify comps per use" note (P2-6). Partly addressed: anchor subjectivity (P2-4) — reduced via decision trees + worked examples, not eliminated.

---

## Before / after — all 8 re-scored under v2

| Target | v1 | v2 | What changed & why |
|---|---|---|---|
| **Synta** | MARGINAL 56 *(ranked #1)* | **OUT OF BUDGET** (Marginal 57 merit) | The headline fix. Real merit is similar, but it's now correctly flagged as unreachable at $100k on a $3k budget instead of topping the leaderboard. |
| **pomocalm.com** | MARGINAL 45 | **INSUFFICIENT DATA** (49 merit) | Pre-revenue with little verifiable — v2 refuses a confident tier rather than implying one. Honest. |
| **Telegram SaaS** | PASS 41 | **INSUFFICIENT DATA** (45 merit) | Same: too little verified to score; the seller literally says it "needs marketing." |
| **DentFlow** | PASS 43.6 | **MARGINAL (provisional)** 49 | More nuanced: cheap ($350) + a partnership path lift it, but `value_transfers=false` (the dentist's domain/community) caps it at Marginal. |
| wattstovolts | PASS 33.6 | PASS 32 | Unchanged — now via the sharp `growth_lever_fits=false` gate (SEO), not a judgment call. |
| AlixCadet | PASS 35.2 | PASS 41 | Unchanged verdict; content/affiliate → gate. (Also over budget, but a Pass is a Pass, so the budget flag is suppressed.) |
| Flipnzee | PASS 23.6 | PASS 29 | Unchanged — the clearest junk. |
| WebTracky | PASS 36.4 | PASS 35 | Unchanged — `growth_lever_fits=false` (commodity + founder's YouTube). |

**Read of the change:** v2 didn't turn junk into gems (correctly — they were junk). It fixed the two ways v1 would have *misled* you: it stopped ranking an unaffordable deal at the top, and it stopped emitting confident tiers on deals it barely knows. Every verdict now traces to a reproducible gate, and the leaderboard is finally trustworthy — nothing sits at the top that you can't actually buy *or* grow.

---

## What's still open (your call)

- **Compliance is a flag, not a full dimension.** Fine for now; promote it to a scored dimension if you start looking at health/fintech/regulated targets.
- **Some anchors stay subjective** (moat "modest" vs "decent"; seller "thin" vs "plausible"). Decision trees + examples help, but two runs of the same deal can still differ by a few points. If you want, I can add a self-consistency check (score a deal twice, flag divergence).
- **Historical records are still v1** (9-dimension re-scores live only in this report). I deliberately didn't overwrite them, so the before/after evidence is preserved. New evaluations use v2.
- **The v2 record schema changed** (nine dimensions, new gate names) — `save_evaluation.py` still works, but the deal-log columns are format-agnostic so it's fine.

## To adopt v2

Re-install the updated `acquisition-evaluator.skill` (Save skill / Settings → Capabilities — it replaces v1 in place, same name). From then on every evaluation runs Phase 2.5 figure-reconciliation, scores nine dimensions, enforces budget, and can actually reach STRONG after you verify a deal.
