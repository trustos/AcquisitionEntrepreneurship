#!/usr/bin/env python3
"""
verify_figures.py — internal-consistency checks on a target's numbers.

Exists because an evaluation was once scored on figures that were 100x wrong
(a marketplace tool under-reported all dollar values). Every dollar figure must
be reconciled against a second/authoritative source AND pass arithmetic sanity
checks before it feeds the score. This catches the arithmetic half automatically:
260 subs x $47 ARPU should be ~$12k MRR, not $122 — a 100x flag.

Pass any subset as flags; missing values are skipped. Tolerance is generous (25%)
because real ARPU/plan mixes vary — a flag means "reconcile before trusting," not
"wrong."

Usage:
    python scripts/verify_figures.py --subs 260 --arpu 47 --mrr 122 --asking 1000 --multiple 0.69
    python scripts/verify_figures.py --mrr 12180 --arr 113325 --rev30 12001 --asking 100000 --multiple 0.7
"""
import argparse
import sys

TOL = 0.25  # 25%


def close(a, b, tol=TOL):
    if a is None or b is None:
        return None
    if a == 0 and b == 0:
        return True
    denom = max(abs(a), abs(b), 1e-9)
    return abs(a - b) / denom <= tol


def ratio(a, b):
    if not a or not b:
        return None
    return a / b


def main():
    ap = argparse.ArgumentParser(description="Internal-consistency checks on a target's numbers.")
    for name, help_ in [
        ("subs", "active paying subscriptions"), ("arpu", "avg revenue per user / mo"),
        ("mrr", "monthly recurring revenue"), ("arr", "annual recurring revenue"),
        ("rev30", "last-30-day revenue"), ("asking", "asking price"),
        ("multiple", "stated revenue multiple"),
    ]:
        ap.add_argument(f"--{name}", type=float, default=None, help=help_)
    args = ap.parse_args()
    v = vars(args)

    flags, notes = [], []

    # subs x arpu ~ mrr  (the check that catches a 100x data error)
    if v["subs"] and v["arpu"] and v["mrr"] is not None:
        implied = v["subs"] * v["arpu"]
        r = ratio(implied, v["mrr"])
        notes.append(f"subs x ARPU = {implied:,.0f}  vs  MRR {v['mrr']:,.0f}  (x{r:.2f})")
        if not close(implied, v["mrr"]):
            sev = "  <<< ~100x OFF — likely a units/data bug" if r and (r > 50 or r < 0.02) else ""
            flags.append(f"subs x ARPU ({implied:,.0f}) != MRR ({v['mrr']:,.0f}){sev}")

    # mrr x 12 ~ arr
    if v["mrr"] is not None and v["arr"] is not None:
        notes.append(f"MRR x 12 = {v['mrr']*12:,.0f}  vs  ARR {v['arr']:,.0f}")
        if not close(v["mrr"] * 12, v["arr"]):
            flags.append(f"MRR x 12 ({v['mrr']*12:,.0f}) != ARR ({v['arr']:,.0f})")

    # rev30 ~ mrr
    if v["rev30"] is not None and v["mrr"] is not None:
        if not close(v["rev30"], v["mrr"]):
            flags.append(f"last-30-day revenue ({v['rev30']:,.0f}) != MRR ({v['mrr']:,.0f}) — check one-offs/annual")

    # asking / annual_revenue ~ stated multiple
    annual = v["arr"] if v["arr"] is not None else (v["mrr"] * 12 if v["mrr"] is not None else (v["rev30"] * 12 if v["rev30"] is not None else None))
    if v["asking"] is not None and annual and v["multiple"] is not None:
        implied_mult = v["asking"] / annual
        notes.append(f"asking / annual-rev = {implied_mult:.2f}x  vs  stated {v['multiple']:.2f}x")
        if not close(implied_mult, v["multiple"], tol=0.35):
            flags.append(f"implied multiple ({implied_mult:.2f}x) != stated ({v['multiple']:.2f}x) — a figure is off by ~{implied_mult/v['multiple']:.0f}x" if v['multiple'] else "multiple mismatch")

    print("=" * 56)
    print("FIGURE RECONCILIATION")
    print("=" * 56)
    for n in notes:
        print("  " + n)
    print("-" * 56)
    if flags:
        print("FLAGS (reconcile against a primary source before scoring):")
        for f in flags:
            print("  ! " + f)
        print("\nVERDICT: DO NOT SCORE until these reconcile.")
        sys.exit(1)
    else:
        print("No internal inconsistencies found. (Still cross-check against a")
        print("second/authoritative source — arithmetic consistency != correct.)")
        print("\nVERDICT: figures internally consistent.")


if __name__ == "__main__":
    main()
