#!/usr/bin/env python3
"""
Emit deals/deals.json — one array of all canonical records — for the importing
app / bulk import. Derived artifact (gitignored); regenerate anytime:
    python scripts/rebuild_dataset.py --dir deals/
"""
import argparse
import datetime
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normalize_report


def main():
    ap = argparse.ArgumentParser(description="Export all records to a single deals.json for the app.")
    ap.add_argument("--dir", "-d", default="deals")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    base = os.path.abspath(args.dir)
    out = args.out or os.path.join(base, "deals.json")
    recs = []
    for f in sorted(glob.glob(os.path.join(base, "*", "record.json"))):
        rec = json.load(open(f))
        recs.append(normalize_report.to_canonical(rec, os.path.basename(os.path.dirname(f))))
    recs.sort(key=lambda r: (r.get("score") or -1), reverse=True)
    payload = {
        "schema_version": normalize_report.SCHEMA_VERSION,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
        "count": len(recs),
        "reports": recs,
    }
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
    print(f"Wrote {out} with {len(recs)} reports.")


if __name__ == "__main__":
    main()
