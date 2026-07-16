#!/usr/bin/env python3
"""
Validate committed evaluation records — the gate that runs at commit time (git
pre-commit hook) and in CI, so a malformed or mis-scored record never reaches
`main` and silently fails to import.

Three checks per deals/*/record.json:
  1. JSON Schema — validated against schema/report.schema.json (real jsonschema
     if installed, else the normalizer's structural check as a fallback).
  2. Score consistency (v2 records) — the stored score/verdict tier must match a
     fresh score.py run over the record's own dimensions+gates (catches
     hand-edits / mis-transcriptions).
  3. Prose-vs-structured — warns (does not fail) when the one-liner/notes mention
     $-figures or "x revenue" while metrics.mrr_usd / deal.revenue_multiple are
     null (the "numbers stuck in prose" pattern).

Exit non-zero if any record fails checks 1 or 2.

Usage:
    python acquisition-evaluator/scripts/validate_reports.py [--dir deals]
"""
import argparse
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import score as scorer  # noqa: E402
import normalize_report as nr  # noqa: E402

SCHEMA_PATH = os.path.join(HERE, "..", "schema", "report.schema.json")


def load_schema_validator():
    try:
        import jsonschema  # type: ignore

        schema = json.load(open(SCHEMA_PATH))
        return lambda rec: [e.message for e in sorted(jsonschema.Draft7Validator(schema).iter_errors(rec), key=str)]
    except Exception:
        # Fallback: the normalizer's structural check (no jsonschema installed).
        return lambda rec: nr.validate(rec)


def score_consistency(rec):
    if rec.get("scoring_version") != "v2":
        return []
    deal = rec.get("deal", {}) or {}
    c = scorer.evaluate({
        "target": rec.get("target"),
        "budget_ceiling": deal.get("budget_ceiling_usd"),
        "asking_price": deal.get("asking_price_usd"),
        "financing_possible": deal.get("financing_possible"),
        "dimensions": rec.get("dimensions", {}) or {},
        "gates": rec.get("gates", {}) or {},
    })
    out = []
    if rec.get("score") is not None and abs(float(rec["score"]) - c["total"]) > 0.5:
        out.append(f"score {rec['score']} != recomputed {c['total']}")
    tier = (rec.get("verdict_detail") or {}).get("tier")
    if tier and tier != c["tier"]:
        out.append(f"verdict tier {tier} != recomputed {c['tier']}")
    return out


MONEY_RE = re.compile(r"\$[\d,]|\bx revenue\b|\brevenue multiple\b", re.I)


def prose_warnings(rec):
    w = []
    prose = " ".join([str(rec.get("one_line_reason") or "")] + [str(x) for x in (rec.get("key_unknowns") or [])])
    m = rec.get("metrics", {}) or {}
    d = rec.get("deal", {}) or {}
    if MONEY_RE.search(prose) and m.get("mrr_usd") is None and d.get("revenue_multiple") is None:
        w.append("prose mentions $-figures / 'x revenue' but metrics.mrr_usd and deal.revenue_multiple are null")
    return w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="deals")
    ap.add_argument("--files", nargs="*", help="specific record.json files (pre-commit passes staged files)")
    args = ap.parse_args()

    files = args.files or sorted(glob.glob(os.path.join(args.dir, "*", "record.json")))
    files = [f for f in files if f.endswith("record.json") and os.path.exists(f)]
    if not files:
        print("No record.json files to validate.")
        return 0

    validate_schema = load_schema_validator()
    failures = 0
    for f in files:
        try:
            rec = json.load(open(f))
        except Exception as e:
            print(f"  ✗ {f}: not valid JSON — {e}")
            failures += 1
            continue
        errs = list(validate_schema(rec)) + score_consistency(rec)
        warns = prose_warnings(rec)
        name = os.path.basename(os.path.dirname(f))
        if errs:
            failures += 1
            print(f"  ✗ {name}")
            for e in errs:
                print(f"      - {e}")
        else:
            print(f"  ok {name}" + (f"   ! {warns[0]}" if warns else ""))

    print(f"\n{len(files)} record(s); {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
