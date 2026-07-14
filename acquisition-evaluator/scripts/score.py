#!/usr/bin/env python3
"""
Acquisition Evaluator — deterministic weighted scorer (v2).

v2 fixes (from the 8-deal audit + red-team):
- Affordability is now a first-class gate (v1 collected budget then ignored it).
- "unknown" gates no longer sink the MERIT tier — they mark the verdict PROVISIONAL
  and block STRONG until verified. Only VERIFIED-FALSE facts cap merit down.
  (v1 treated "unknown" and "false" the same, which made STRONG unreachable and
  labelled a 95-merit unverified deal identically to a mediocre 62.)
- The vague "competence" gate is split into OPERABLE (can we run it) and
  GROWTH_LEVER_FITS (is the primary growth lever one this team can execute).
- New dimension: transfer_key_person (does the growth engine survive founder exit).
- Revenue evidence is graded (buyer_verified > marketplace_attested > seller_claimed
  > none > contradicted) instead of a single boolean badge.
- Low completeness now overrides to INSUFFICIENT DATA rather than a confident tier.
- Input validation: missing dims / bad vocab are flagged, not silently zeroed.

Usage:
    python scripts/score.py --input scores.json
    cat scores.json | python scripts/score.py
    python scripts/score.py --example
"""

import argparse
import json
import sys

# ---- Dimensions (9, orthogonalised) --------------------------------------
WEIGHTS = {
    "operability_upside": 15,       # can WE run it + is there engineering/product upside (NOT "is growth marketing" — that's a gate)
    "pmf_retention": 15,            # do real users pay and stay
    "unit_economics": 12,           # margins, recurring, LTV:CoCA, pricing headroom
    "moat_defensibility": 12,       # durable advantage + channel QUALITY, judged team-independently
    "growth_market": 8,             # is the product + category growing / dying (incl. AI)
    "tech_ip": 8,                   # owned, transferable, modernisable without a rewrite
    "transfer_key_person": 10,      # does distribution/domain survive the founder's exit
    "deal_terms": 10,               # value-for-money: multiple, structure, absolute cash outlay
    "seller_adverse_selection": 10, # why is it really for sale; what's hidden
}
LABELS = {
    "operability_upside": "Operability & product upside",
    "pmf_retention": "PMF & retention",
    "unit_economics": "Unit economics & upside",
    "moat_defensibility": "Moat & defensibility",
    "growth_market": "Growth & market",
    "tech_ip": "Tech & IP health",
    "transfer_key_person": "Transfer / key-person",
    "deal_terms": "Deal terms & value",
    "seller_adverse_selection": "Seller & adverse-selection",
}
CONF_WEIGHT = {"high": 1.0, "med": 0.6, "medium": 0.6, "low": 0.3, "unknown": 0.0}

# ranks
PASS, MARGINAL, PROMISING, STRONG = 1, 2, 3, 4
TIERS = {STRONG: "STRONG", PROMISING: "PROMISING", MARGINAL: "MARGINAL", PASS: "PASS"}

REVENUE_EVIDENCE = ("buyer_verified", "marketplace_attested", "seller_claimed", "none", "contradicted")

EXAMPLE = {
    "target": "Acme Scheduling",
    "budget_ceiling": 3000,
    "asking_price": 2500,
    "financing_possible": False,
    "dimensions": {
        "operability_upside": {"score": 5, "confidence": "high"},
        "pmf_retention": {"score": 4, "confidence": "med"},
        "unit_economics": {"score": 4, "confidence": "med"},
        "moat_defensibility": {"score": 4, "confidence": "med"},
        "growth_market": {"score": 3, "confidence": "med"},
        "tech_ip": {"score": 4, "confidence": "low"},
        "transfer_key_person": {"score": 4, "confidence": "med"},
        "deal_terms": {"score": 4, "confidence": "high"},
        "seller_adverse_selection": {"score": 3, "confidence": "med"},
    },
    "gates": {
        "operable": True,
        "growth_lever_fits": True,
        "value_transfers": "unknown",
        "ip_transferable": "unknown",
        "not_fragile": True,
        "revenue_evidence": "marketplace_attested",
    },
}

COMPLETENESS_FLOOR = 45   # below this -> INSUFFICIENT DATA
BUDGET_TOLERANCE = 1.25   # asking up to 1.25x ceiling is still "affordable"


def norm_gate(v):
    if isinstance(v, bool):
        return v
    if v is None:
        return "unknown"
    s = str(v).strip().lower()
    if s in ("true", "yes", "y", "pass", "1"):
        return True
    if s in ("false", "no", "n", "fail", "0"):
        return False
    return s  # pass through strings like "unknown" / revenue-evidence values


def base_rank(total):
    if total >= 75:
        return STRONG
    if total >= 60:
        return PROMISING
    if total >= 45:
        return MARGINAL
    return PASS


def evaluate(data):
    warnings = []
    dims = data.get("dimensions", {})
    total = 0.0
    completeness = 0.0
    rows = []
    for key, weight in WEIGHTS.items():
        d = dims.get(key)
        if d is None:
            warnings.append(f"dimension '{key}' missing — treated as neutral 2/unknown (fix your input)")
            d = {"score": 2, "confidence": "unknown"}
        score = d.get("score", 2)
        conf = str(d.get("confidence", "unknown")).strip().lower()
        if conf not in CONF_WEIGHT:
            warnings.append(f"dimension '{key}' has unrecognised confidence '{conf}' — treated as unknown")
            conf = "unknown"
        try:
            score = int(score)
        except (TypeError, ValueError):
            warnings.append(f"dimension '{key}' has non-integer score — treated as 2")
            score = 2
        score = max(0, min(5, score))
        contrib = (score / 5.0) * weight
        total += contrib
        completeness += CONF_WEIGHT[conf] * weight
        rows.append((key, weight, score, conf, contrib))
    total = round(total, 1)
    completeness = round(completeness, 1)

    g = {k: norm_gate(v) for k, v in data.get("gates", {}).items()}

    # ---- affordability (computed) ----
    asking = data.get("asking_price")
    ceiling = data.get("budget_ceiling")
    financing = bool(data.get("financing_possible", g.get("financing_possible", False)))
    affordable = "unknown"
    afford_note = "asking price or budget not provided"
    if isinstance(asking, (int, float)) and isinstance(ceiling, (int, float)) and ceiling > 0:
        if asking <= ceiling * BUDGET_TOLERANCE:
            affordable, afford_note = True, f"asking ${asking:,.0f} within budget ${ceiling:,.0f}"
        elif financing:
            affordable, afford_note = True, f"asking ${asking:,.0f} > budget ${ceiling:,.0f} but financing flagged possible"
        else:
            affordable = False
            afford_note = f"asking ${asking:,.0f} is {asking/ceiling:.0f}x the ${ceiling:,.0f} budget, no financing path"

    # ---- kill gates (verified-negative facts cap MERIT) ----
    kill = []  # (rank_cap, reason)
    if g.get("operable") is False:
        kill.append((PASS, "OPERABLE = false: team can't run/maintain the core tech"))
    if g.get("growth_lever_fits") is False:
        kill.append((PASS, "GROWTH-LEVER-FITS = false: the primary growth lever is sales/marketing the team can't run"))
    if g.get("ip_transferable") is False:
        kill.append((MARGINAL, "IP-TRANSFERABLE = false: code/accounts can't legally transfer"))
    if g.get("value_transfers") is False:
        kill.append((MARGINAL, "VALUE-TRANSFERS = false: the distribution/domain walks away with the founder"))
    if g.get("not_fragile") is False:
        kill.append((MARGINAL, "NOT-FRAGILE = false: a structural single point of failure (platform lock / one customer / sole non-transferable channel)"))
    if g.get("revenue_evidence") == "contradicted":
        kill.append((MARGINAL, "REVENUE = contradicted: the figures don't reconcile (possible bad data or inflation) — do not trust the tier"))

    # ---- verification gates (unknowns block STRONG + mark provisional; NO merit drop) ----
    prov = []
    for k in ("operable", "growth_lever_fits", "ip_transferable", "value_transfers", "not_fragile"):
        if g.get(k) == "unknown" or k not in g:
            prov.append(k)
    rev = g.get("revenue_evidence", "none")
    if rev in ("marketplace_attested", "seller_claimed", "none", "unknown"):
        prov.append(f"revenue={rev} (not buyer-verified from source)")
    if affordable == "unknown":
        prov.append("affordability (price/budget unknown)")

    base = base_rank(total)
    final = base
    for cap, _ in kill:
        final = min(final, cap)
    provisional = len(prov) > 0
    if provisional:
        final = min(final, PROMISING)   # can't be STRONG until verified — but unknowns don't drop merit further

    # ---- terminal overrides ----
    override = None
    if affordable is False and final >= MARGINAL:
        override = "OUT_OF_BUDGET"  # only flag if it'd otherwise be worth considering
    if completeness < COMPLETENESS_FLOOR:
        override = "INSUFFICIENT_DATA"  # takes precedence — too little to trust any tier

    tier = TIERS[final]
    return {
        "target": data.get("target", "target"),
        "total": total, "completeness": completeness,
        "rows": rows, "gates": g, "warnings": warnings,
        "affordable": affordable, "afford_note": afford_note,
        "kill": kill, "provisional": provisional, "prov_reasons": prov,
        "base_rank": base, "final_rank": final,
        "tier": tier, "override": override,
    }


def render(r):
    o = []
    o.append("=" * 66)
    o.append(f"ACQUISITION SCORECARD (v2) — {r['target']}")
    o.append("=" * 66)
    o.append(f"{'Dimension':<30}{'Wt':>4}{'Score':>7}{'Conf':>9}{'Pts':>8}")
    o.append("-" * 66)
    for key, weight, score, conf, contrib in r["rows"]:
        o.append(f"{LABELS[key]:<30}{weight:>4}{str(score)+'/5':>7}{conf:>9}{contrib:>8.1f}")
    o.append("-" * 66)
    o.append(f"{'WEIGHTED MERIT TOTAL':<30}{100:>4}{'':>7}{'':>9}{r['total']:>8.1f}")
    o.append("")
    o.append(f"Information completeness: {r['completeness']:.0f}%")
    o.append(f"Affordability: {r['affordable']}  ({r['afford_note']})")
    o.append("")
    o.append("Gates:")
    for k in ("operable", "growth_lever_fits", "revenue_evidence", "value_transfers", "ip_transferable", "not_fragile"):
        o.append(f"  - {k:<20} {r['gates'].get(k, 'unknown')}")
    if r["kill"]:
        o.append("")
        o.append("Merit caps (verified-negative):")
        for _, reason in r["kill"]:
            o.append(f"  - {reason}")
    if r["provisional"]:
        o.append("")
        o.append("Provisional — blocks STRONG until verified: " + ", ".join(r["prov_reasons"]))
    o.append("")
    o.append(f"Merit tier (score + verified caps): {r['tier']}  ({r['total']:.0f}/100)")

    # headline verdict
    if r["override"] == "INSUFFICIENT_DATA":
        verdict = f"INSUFFICIENT DATA — merit reads {r['tier']} but completeness {r['completeness']:.0f}% is too low to trust. Gather more, then re-score."
    elif r["override"] == "OUT_OF_BUDGET":
        verdict = f"OUT OF BUDGET — {r['tier']} on merits, but {r['afford_note']}. Pursue only with financing/earnout or a price drop."
    else:
        verdict = r["tier"] + (" (provisional — verify the flagged items to confirm/upgrade)" if r["provisional"] else "")
    o.append("")
    o.append(f">>> VERDICT: {verdict}")
    if r["warnings"]:
        o.append("")
        o.append("Input warnings:")
        for w in r["warnings"]:
            o.append(f"  ! {w}")
    o.append("=" * 66)
    return "\n".join(o)


def main():
    ap = argparse.ArgumentParser(description="Deterministic weighted scorer (v2) for the Acquisition Evaluator.")
    ap.add_argument("--input", "-i", help="Path to scores JSON (default: stdin)")
    ap.add_argument("--example", action="store_true", help="Print an example input JSON and exit")
    ap.add_argument("--json", action="store_true", help="Also print machine-readable result JSON")
    args = ap.parse_args()
    if args.example:
        print(json.dumps(EXAMPLE, indent=2))
        return
    if args.input:
        with open(args.input) as f:
            data = json.load(f)
    else:
        raw = sys.stdin.read().strip()
        if not raw:
            ap.error("no input (use --input FILE, pipe JSON, or --example)")
        data = json.loads(raw)
    r = evaluate(data)
    print(render(r))
    if args.json:
        print("\n--- result json ---")
        print(json.dumps({k: v for k, v in r.items() if k != "rows"}, indent=2, default=str))


if __name__ == "__main__":
    main()
