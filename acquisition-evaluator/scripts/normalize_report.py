#!/usr/bin/env python3
"""
Normalize an evaluation record into the canonical, import-ready shape
(see ../schema/report.schema.json). Non-destructive & additive: it ADDS the
structured fields an importing app needs (id, schema_version, verdict_detail,
deal, metrics, contact, pipeline, timestamps) and derives numbers from prose
where possible, while preserving everything the human/scorer already wrote.

Used three ways:
  - by save_evaluation.py on every save (new reports are born canonical);
  - to migrate existing records in place:  python normalize_report.py --dir deals/
  - to validate:                           python normalize_report.py --dir deals/ --check

Dependency-free (no jsonschema needed); the formal JSON Schema is the app's contract.
"""
import argparse
import datetime
import glob
import json
import os
import re
import sys

SCHEMA_VERSION = "acq-eval-report/1.0"
TIERS = ["STRONG", "PROMISING", "MARGINAL", "PASS"]
PIPELINE_STATUSES = ["new", "screening", "contacted", "in_dd", "offer", "won", "passed"]
DEFAULT_BUDGET_CEILING = 3000  # team config; used when a record omits budget_ceiling (S8)
CURRENCY_SYMBOLS = {"$": "USD", "€": "EUR", "£": "GBP"}


def slugify(s):
    s = re.sub(r"^https?://", "", str(s or "target").strip().lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "target"


def parse_currency(v):
    """Detect currency from a symbol in the price string; None if none present."""
    for sym, code in CURRENCY_SYMBOLS.items():
        if sym in str(v or ""):
            return code
    return None


def parse_price(v):
    """'$4,900 BIN (Flippa)' -> 4900 ; '$100k' -> 100000 ; 4000 -> 4000 ; None -> None.
    S10: prefer a currency-anchored amount so '2 payment plans, $5k' -> 5000 (not 2),
    and reject implausibly small BARE integers (a lone '2' is not a price)."""
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return int(v)
    if not v:
        return None
    s = str(v)
    # Prefer a currency-anchored amount.
    m = re.search(r"[$€£]\s*([\d,]+(?:\.\d+)?)\s*([kKmM])?", s)
    if m:
        num = float(m.group(1).replace(",", ""))
        suf = (m.group(2) or "").lower()
    else:
        # Fall back to a bare number, but require a k/m suffix or a plausible size.
        m = re.search(r"([\d,]+(?:\.\d+)?)\s*([kKmM])?", s)
        if not m:
            return None
        num = float(m.group(1).replace(",", ""))
        suf = (m.group(2) or "").lower()
        if not suf and num < 50:
            return None  # reject "2 payment plans" and similar noise
    if suf == "k":
        num *= 1_000
    elif suf == "m":
        num *= 1_000_000
    return int(round(num))


def norm_verdict(v):
    if isinstance(v, dict):
        d = {"tier": v.get("tier", "PASS"),
             "provisional": bool(v.get("provisional")),
             "out_of_budget": bool(v.get("out_of_budget")),
             "insufficient_data": bool(v.get("insufficient_data"))}
        return d
    s = str(v or "").upper()
    tier = next((t for t in TIERS if t in s), "PASS")
    return {"tier": tier,
            "provisional": "PROVISIONAL" in s,
            "out_of_budget": "OUT OF BUDGET" in s or "OUT_OF_BUDGET" in s,
            "insufficient_data": "INSUFFICIENT" in s}


def scoring_version(rec):
    d = set((rec.get("dimensions") or {}).keys())
    if "operability_upside" in d:
        return "v2"
    if "build_scale_fit" in d:
        return "v1"
    return "unknown"


def budget_fit(ask, ceiling):
    if not ask or not ceiling:
        return "unknown"
    if ask <= ceiling:
        return "in"
    if ask <= ceiling * 1.25:
        return "at"
    return "over"


def _revenue_evidence(rec):
    g = rec.get("gates", {}) or {}
    if g.get("revenue_evidence"):
        return g["revenue_evidence"]
    rv = g.get("revenue_verifiable")  # v1
    if rv is True:
        return "marketplace_attested"
    if rv is False:
        # S3: v1 `false` meant "seller can't/won't evidence revenue" = v2 "none",
        # NOT "contradicted" (a kill-gate-grade "figures don't reconcile" fact).
        return "none"
    return "unknown"


def _listing_url(rec):
    for s in (rec.get("sources") or []):
        u = (s.get("url") if isinstance(s, dict) else str(s)) or ""
        if any(k in u for k in ("reddit.com", "flippa.com", "acquire.com", "trustmrr.com",
                                "empireflippers", "microns.io", "sideprojectors", "tinyacquisitions")):
            return u
    return None


def _merge(defaults, provided):
    out = dict(defaults)
    for k, v in (provided or {}).items():
        if v is not None or k not in out:
            out[k] = v
    return out


def to_canonical(rec, rec_id=None, now=None):
    """Return rec with canonical fields added (in place-safe: returns a new dict)."""
    r = dict(rec)
    now = now or datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
    date = r.get("date") or datetime.date.today().isoformat()

    if not rec_id:
        rec_id = f"{slugify(r.get('target'))}_{date}"
        if r.get("analyst"):
            rec_id += "_" + slugify(r["analyst"])

    r["schema_version"] = SCHEMA_VERSION
    r["id"] = rec_id
    r["scoring_version"] = scoring_version(r)
    r.setdefault("created_at", f"{date}T00:00:00Z")
    r["updated_at"] = now

    r["verdict_detail"] = norm_verdict(r.get("verdict"))

    ask = parse_price(r.get("asking_price"))
    ceiling = r.get("budget_ceiling")
    if isinstance(ceiling, str):
        ceiling = parse_price(ceiling)
    if ceiling is None:
        ceiling = DEFAULT_BUDGET_CEILING  # S8: team ceiling applies unless overridden
    currency = parse_currency(r.get("asking_price")) or ("USD" if ask is not None else None)
    deal_defaults = {
        "asking_price_usd": ask, "currency": currency,
        "revenue_multiple": None, "budget_ceiling_usd": ceiling,
        "budget_fit": budget_fit(ask, ceiling),
        "financing_possible": r.get("financing_possible"),
    }
    r["deal"] = _merge(deal_defaults, r.get("deal"))

    metrics_defaults = {k: None for k in
                        ["mrr_usd", "arr_usd", "subscriptions", "customers", "growth_30d_pct",
                         "monthly_visitors", "churn_pct", "margin_pct", "domain_rating", "age_months"]}
    metrics_defaults["revenue_evidence"] = _revenue_evidence(r)
    r["metrics"] = _merge(metrics_defaults, r.get("metrics"))

    contact_defaults = {"seller_handle": None, "listing_url": _listing_url(r), "marketplace": None,
                        "method": None, "contacted_on": None, "notes": None}
    r["contact"] = _merge(contact_defaults, r.get("contact"))

    # S4: an insufficient-data / out-of-budget verdict must NOT be filed as
    # "passed" (rejected) — it stays in screening (gather data / find financing).
    # Only a genuine PASS-tier merit maps to the "passed" (we-declined) stage.
    vd = r["verdict_detail"]
    if vd["insufficient_data"] or vd["out_of_budget"]:
        default_status = "screening"
    elif vd["tier"] == "PASS":
        default_status = "passed"
    else:
        default_status = "screening"
    pipeline_defaults = {"status": default_status,
                         "owner": r.get("analyst"), "last_updated": now}
    r["pipeline"] = _merge(pipeline_defaults, r.get("pipeline"))
    return r


def validate(r):
    issues = []
    for k in ("schema_version", "id", "target", "date", "verdict_detail", "score", "scoring_version"):
        if k not in r:
            issues.append(f"missing '{k}'")
    if r.get("verdict_detail", {}).get("tier") not in TIERS:
        issues.append(f"verdict tier not in {TIERS}")
    if r.get("pipeline", {}).get("status") not in PIPELINE_STATUSES:
        issues.append("pipeline.status invalid")
    for k in ("asking_price_usd", "budget_ceiling_usd"):
        v = r.get("deal", {}).get(k)
        if v is not None and not isinstance(v, (int, float)):
            issues.append(f"deal.{k} not numeric")
    return issues


def main():
    ap = argparse.ArgumentParser(description="Normalize/migrate evaluation records to the canonical schema.")
    ap.add_argument("--dir", "-d", default="deals", help="Deals base folder")
    ap.add_argument("--file", "-f", help="Single record.json")
    ap.add_argument("--check", action="store_true", help="Validate only; don't write")
    args = ap.parse_args()

    files = [args.file] if args.file else sorted(glob.glob(os.path.join(args.dir, "*", "record.json")))
    if not files:
        sys.exit("No record.json files found.")
    total_issues = 0
    for f in files:
        rec = json.load(open(f))
        rec_id = os.path.basename(os.path.dirname(f)) if not args.file else None
        canon = to_canonical(rec, rec_id)
        issues = validate(canon)
        tag = f"  ! {', '.join(issues)}" if issues else "  ok"
        total_issues += len(issues)
        print(f"- {canon['id']:<44} scoring={canon['scoring_version']} verdict={canon['verdict_detail']['tier']} ${canon['deal']['asking_price_usd']}{tag}")
        if not args.check:
            with open(f, "w") as out:
                json.dump(canon, out, indent=2, ensure_ascii=False)
    print(f"\n{'Validated' if args.check else 'Normalized'} {len(files)} records; {total_issues} issue(s).")
    sys.exit(1 if (args.check and total_issues) else 0)


if __name__ == "__main__":
    main()
