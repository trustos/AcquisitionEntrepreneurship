# The Rubric v2 — dimensions, weights, anchors, gates

Score each of the **nine** dimensions 0–5 and assign a confidence (high / med / low / unknown). Weighted total (max 100) = `sum((score/5) * weight)`. Then apply the gates. v2 changes are called out where they matter; the short version: **budget now bites, "unknown" no longer sinks merit, STRONG is reachable after verification, and "the value walks away with the founder" has its own dimension.**

| # | Dimension | Wt | What it answers |
|---|---|---|---|
| 1 | Operability & product upside | 15 | Can *this* team run/maintain it, and is there real engineering/product upside to unlock? |
| 2 | PMF & retention | 15 | Do real users pay and stay? |
| 3 | Unit economics & upside | 12 | Margins, recurring-ness, LTV:CoCA, pricing headroom. |
| 4 | Moat & defensibility | 12 | Durable advantage + channel *quality* — judged on the business, **not** whether this team can run it. |
| 5 | Growth & market | 8 | Product + category growing, flat, or dying (incl. AI impact). |
| 6 | Tech & IP health | 8 | Owned, transferable, modernisable without a rewrite. |
| 7 | Transfer / key-person | 10 | Does the growth engine (distribution, domain, relationships) survive the founder's exit? |
| 8 | Deal terms & value | 10 | Value-for-money: multiple, structure, **and absolute cash outlay**. |
| 9 | Seller & adverse-selection | 10 | Why is it *really* for sale, and what's hidden? |

Total = 100. **Note the v1→v2 shifts:** "is growth a marketing problem?" is no longer triple-counted across dimensions — it now lives once, in the **growth-lever gate**. Moat is judged team-independently. Seller/adverse-selection is up-weighted (7→10) because at this deal size "why is a working thing for sale?" is the whole ballgame.

## The golden rule for unknowns (read this — it was the #1 scoring bug)

**An unknown dimension is scored NEUTRAL (2) with confidence `unknown` — never 1.** A `1` means *you have evidence it's bad* (a leaky bucket, a dead market). Absence of evidence is not evidence of absence; scoring unknowns as `1` silently tanks the total and manufactures false PASSes. If you don't know, score 2/unknown and let the low completeness + the seller questions carry it.

---

## Dimension anchors

### 1. Operability & product upside (15)
Pure question: can the team **run and improve** it? (The separate "can they *grow* it" question is the growth-lever gate — don't double-count it here.)

- **5** — Squarely their stack; underbuilt/dated/missing obvious features they can 10x. Clear engineering/product upside.
- **4** — Their stack; modest upside.
- **3** — Runnable by them, but the product is mature/commodity — little left to add that moves the needle.
- **2** — Runnable but outside their comfort (unfamiliar stack, heavy ops) *or* unknown.
- **1** — Needs non-software expertise to even operate (regulated ops, content treadmill).
- **0** — They can't operate it at all → trips the OPERABLE gate.

### 2. PMF & retention (15)
- **5** — Verified low churn (~1–2%/mo or NRR ≥100%), long tenure, organic love.
- **4** — Good retention, mostly verified.
- **3** — Adequate, or retention only claimed.
- **2** — Weak/declining retention, one-time-purchase stickiness, **or unknown**.
- **1** — Verified leaky bucket / churn so high it's a treadmill.
- **0** — Verified no real paying base.

### 3. Unit economics & upside (12)
- **5** — Recurring, healthy margin, LTV ≥3× CoCA, obvious pricing headroom the team can capture.
- **4** — Solid recurring economics + some upside.  **3** — Okay, or good-but-tapped, or partly verified.
- **2** — Thin/erratic/one-time, LTV:CoCA ~1:1, **or unknown**.  **1** — Loses money per customer.  **0** — No path to LTV>CoCA.

### 4. Moat & defensibility (12)
Judge the *business*, not the team. (Whether the team can run the channel is the growth-lever gate.)

- **5** — Strong moat (switching costs, integrations, proprietary data, beloved brand/community) + durable organic demand.
- **4** — Decent moat.  **3** — Modest/replicable moat.  **2** — Weak moat, **or unknown**.
- **1** — Commodity in a crowded field; nothing to defend.  **0** — Zero moat + a channel one change from zero.

### 5. Growth & market (8)
- **5** — Growing product in a growing niche; AI a tailwind.  **4** — Growing/stable.  **3** — Flat/mature, **or unknown**.
- **2** — Slowly declining or category under pressure.  **1** — Declining / AI eating the category.  **0** — Structurally dying.

### 6. Tech & IP health (8)
Transferability + modernisability, **not** prettiness (mind the rewrite trap).

- **5** — Owned, clean transfer, sane architecture, no scary lock-in.  **4** — Owned/transferable, manageable debt.
- **3** — Workable with real debt or a single-API dependence, **or unknown**.  **2** — Heavy debt / unclear ownership.
- **1** — Contractor-owned or only-a-rewrite-fixes-it.  **0** — Can't transfer/own → trips the IP gate.

### 7. Transfer / key-person (10)  *(new in v2)*
Does the thing that actually drives acquisition & retention **survive the founder leaving**? (This kept recurring — WebTracky's YouTube, DentFlow's dentist — with no home in v1.)

- **5** — Growth engine is the product/brand/SEO/integrations — impersonal and fully transferable.
- **4** — Mostly transferable; minor founder involvement.  **3** — Mixed, or unknown, or a transition period needed.
- **2** — Much of the demand rides the founder's personal audience/relationships/expertise.
- **1** — The founder *is* the distribution/domain; little survives their exit.  **0** — Buying a brand with no business → trips the VALUE-TRANSFERS gate.

### 8. Deal terms & value (10)
Value-for-money **and** absolute cash reality (not just the multiple — a fair multiple on a huge price can still be unreachable).

- **5** — At/below fair multiple, comfortably affordable, buyer-friendly structure (seller note, retention earnout, holdback, asset purchase).
- **4** — Fair price + reasonable terms, affordable.  **3** — Fair-ish but rigid/all-cash, or a bit high but negotiable, or unknown.
- **2** — Overpriced for the metrics, or a fair multiple on a sum that strains the budget.  **1** — Clearly overpriced/inflexible.  **0** — Price detached from reality.

*(Absolute affordability is also a hard gate — see below. This dimension captures value; the gate captures "can we literally pay.")*

### 9. Seller & adverse-selection (10)
"Why is it *really* for sale?" Assume the seller knows more than you. **Interrogate a suspiciously low multiple** — cheap usually means declining or a lemon.

- **5** — Credible benign reason, transparent, verifiable numbers, no concentration.  **4** — Reasonable story, minor flags.
- **3** — Plausible + some concentration/key-person, or unknown.  **2** — Thin story, peak-metrics timing, real concentration.
- **1** — Red flags (penalties, cleaned-up decline, evasive).  **0** — A lemon dressed for sale.

---

## Confidence → completeness
high = 1.0 · med = 0.6 · low = 0.3 · unknown = 0.0.  Completeness % = `sum(conf_weight × weight)`.  **Below 45% the scorer returns INSUFFICIENT DATA** and refuses a confident tier — gather more first.

---

## Gates v2 — two kinds, and they behave differently

**A. Kill gates — a *verified-negative fact* caps the merit tier.** (Only `false`/`contradicted` bite. `unknown` does NOT bite here — that's the v1 bug.)

- **operable** `false` → **PASS.** Team can't run/maintain the core tech.
- **growth_lever_fits** `false` → **PASS.** The *primary* way this business gets customers is sales / SEO / paid / content / community the team can't run. **Decision tree:** What is the #1 acquisition channel *today*? Product-led / organic / word-of-mouth / integrations → fits (true). Field sales / SEO-content treadmill / paid ads / a personal audience → doesn't fit (false). This replaces v1's vague "operate *and* scale" competence gate, which was applied inconsistently (pomocalm true, WebTracky false — both in-stack).
- **ip_transferable** `false` → **MARGINAL.** Code/accounts can't legally transfer.
- **value_transfers** `false` → **MARGINAL.** The distribution/domain/relationships walk away with the founder.
- **not_fragile** `false` → **MARGINAL.** *Re-scoped for micro-scale:* single-channel/customer/person is the norm here and is NOT an automatic fail — only trip this on a **structural** single point of failure: a platform that controls your pricing/access (App Store, one API), one customer >~30% of revenue, or a sole channel that is both undefendable **and** non-transferable. Ordinary early thinness is graded in Moat / Transfer, not here.
- **revenue_evidence** `contradicted` → **MARGINAL** (numbers don't reconcile — see the reconciliation step).

**B. Verification gates — an *unknown* blocks STRONG and marks the verdict PROVISIONAL, but does NOT lower merit.** This is the core v2 fix: a genuinely strong deal you haven't verified yet reads "PROMISING (provisional) — 82/100," not the same "Promising" as a mediocre 62. After diligence you re-score with the gates resolved, and it can reach STRONG.

- `operable`, `growth_lever_fits`, `ip_transferable`, `value_transfers`, `not_fragile` = `unknown` → provisional.
- **revenue_evidence** graded: `buyer_verified` (you reconciled from source) clears; `marketplace_attested` (a badge — e.g. TrustMRR's "Stripe-verified"), `seller_claimed`, `none` all count as **not yet buyer-verified** → provisional, block STRONG. A marketplace badge is *attested*, not *reconciled* — don't treat it as source-verified.

**C. Affordability gate (computed).** From `asking_price`, `budget_ceiling`, `financing_possible`: if asking > 1.25× budget and no financing path → **OUT OF BUDGET** (reported alongside the merit tier, so you still see "STRONG on merits, but 33× budget"). If price/budget unknown → provisional.

## Verdict tiers (merit) + special states
- **75–100 STRONG** (only reachable when all gates verified — i.e. after diligence).
- **60–74 PROMISING** · **45–59 MARGINAL** · **<45 PASS**.
- Modifiers/overrides: **(provisional)** = unknowns block STRONG; **OUT OF BUDGET** = good but unaffordable; **INSUFFICIENT DATA** = completeness <45%, no trustworthy tier yet.

## Worked examples
1. **The reachable gem.** $40k asking on a $50k budget; verified $12k MRR from source, product-led, code owned, distribution impersonal, all gates true. Scores ~86 → **STRONG.** (In v1 this was impossible — unknown gates capped everything at Promising forever.)
2. **Same gem, wrong price.** Identical but $100k asking on a $3k budget → **OUT OF BUDGET — STRONG on merits, pursue only with financing/price drop.** (v1 scored it 56/Marginal and ranked it #1 on a price-blind sort — the exact trap this fixes.)
3. **The commodity in your wheelhouse.** Analytics SaaS, 5 subs, ~$40 MRR flat, free incumbents everywhere, only channel is the founder's YouTube. operable true, growth_lever_fits **false** (channel is a personal audience), value_transfers **false**. → merit ~40, capped **PASS**. Correct.
