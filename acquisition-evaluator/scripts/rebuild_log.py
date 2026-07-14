#!/usr/bin/env python3
"""
Rebuild deals/deal-log.csv and deal-log.xlsx from every per-deal record.json.

Why this exists (TEAM USE): the combined deal-log is a DERIVED artifact. On a
shared repo, two people saving evaluations would both touch the binary .xlsx and
git can't merge it. So treat the log as regenerable: everyone commits their
per-deal `record.json` (which never conflicts — one file per evaluation), and
anyone can run this to rebuild the combined log from the full set. If the log
ever conflicts in git, don't resolve it by hand — accept either side, then run:

    python scripts/rebuild_log.py --dir deals/

Sorted by merit score (desc) so the strongest candidates float to the top.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import save_evaluation as SE  # shares COLUMNS, row_from, write_csv, write_xlsx


def _score_key(row):
    try:
        return float(row[5])   # Score column
    except (TypeError, ValueError):
        return -1.0


def main():
    ap = argparse.ArgumentParser(description="Rebuild the combined deal log from all record.json files.")
    ap.add_argument("--dir", "-d", default="deals", help="Deals base folder (default: ./deals)")
    args = ap.parse_args()
    base = os.path.abspath(args.dir)
    if not os.path.isdir(base):
        sys.exit(f"No such folder: {base}")

    rows, n = [], 0
    for name in sorted(os.listdir(base)):
        rec_path = os.path.join(base, name, "record.json")
        if os.path.isfile(rec_path):
            try:
                with open(rec_path) as f:
                    rec = json.load(f)
            except Exception as e:
                print(f"  ! skipped {name}: {e}")
                continue
            rows.append(SE.row_from(rec))
            n += 1

    rows.sort(key=_score_key, reverse=True)
    SE.write_csv(os.path.join(base, "deal-log.csv"), rows)
    print(f"Rebuilt deal-log.csv from {n} record.json files.")
    if SE.HAVE_XLSX:
        SE.write_xlsx(os.path.join(base, "deal-log.xlsx"), rows)
        print("Rebuilt deal-log.xlsx.")
    else:
        print("deal-log.xlsx SKIPPED (pip install openpyxl --break-system-packages).")


if __name__ == "__main__":
    main()
