# Long Book: AI Hardware — ~6-Month Horizon (Sep 2026 → ~Mar 2027)

**Author:** Equity research (point-in-time exercise)
**As-of date:** 2026-09-10
**Horizon:** Approximately 6 months (now through ~March 2027)
**Coverage:** AI compute, memory, foundry, custom silicon, networking/interconnect, semicap, and data-center power/thermal.

> **DISCLAIMER — READ FIRST.** This document is **research/educational analysis, not investment advice**, and is **not** a recommendation, solicitation, or offer to buy or sell any security. It was produced by an AI research agent as a point-in-time exercise. It is based on **public information available around 2026-09-10 that may be incomplete, stale, mis-transcribed, or simply wrong.** Several figures below were gathered via web search and could not all be reconciled against primary filings; where that is true, it is flagged. Some 2026 datapoints (notably in the memory complex) reflect an unusually extreme reported upcycle and should be treated with elevated skepticism. **Past performance and forward projections are not guarantees of future results.** Markets can move violently against any thesis here, and single-stock concentration can produce large losses. Do your own due diligence and consult a licensed professional before making any investment decision. The author holds no position and has no ability to verify the accuracy of third-party quotes/prices used herein.

---

## 1. Executive summary & market backdrop

**The setup.** As of September 2026, the AI hardware complex is in the steepest capital-spending cycle in the history of the technology sector, and — unlike prior "narrative" phases — the spending is now landing in reported revenue and guidance across the supply chain. The debate has shifted from *"is demand real?"* to *"how is it financed, and when does it break?"*

**Capex scale (the demand engine).**
- Combined 2026 hyperscaler capex guidance across the four largest US hyperscalers has climbed to roughly **US$720bn–745bn**, ~US$835bn including Oracle's fiscal-2027 guide (*TMT Finance, post-Q2-2026 earnings, Sep 2026*).
- Bank of America now sees CY2026 hyperscaler capex **>US$860bn (up ~80% YoY)** and a "path toward **US$1.2 trillion in 2027**" (*BofA note via EdgeX, Aug 2026*). S&P Global models the group at **~US$870bn in 2026 and ~US$1.3tn in 2027**, with only Microsoft FCF-positive in 2027 (*S&P Global Ratings, Aug 27, 2026; The Motley Fool, Sep 6, 2026*).
- BofA flags the single most important number as the **US$2.3tn backlog** of customer cloud commitments across the top four providers, up 16% QoQ (*BofA, Aug 2026*).
- NVIDIA's CFO cited third-party forecasts of hyperscale capex topping **US$1tn in 2027** and total AI infrastructure spend of **US$3–4tn/yr by 2030** (*NVIDIA Q2 FY2027 call, Aug 26, 2026*). This is management framing, not independent fact — treat as directional.

**The key structural feature: supply is the binding constraint, not demand.** Across the chain — CoWoS advanced packaging, HBM, leading-edge wafers, substrates, optics, and even data-center power/cooling — capacity is sold out well into 2027. Multiple suppliers now describe multi-year, prepaid, take-or-pay agreements that convert a historically cyclical business into something closer to a booked backlog. That is the crux of the bull case for a 6-month long book: near-term revenue is unusually *visible*.

**The dominant shared risk: circular financing / an "AI capex air pocket."** The same ecosystem funding the buildout is increasingly interlinked. S&P projects the hyperscaler group runs **negative free operating cash flow through 2026–2027**, funded by long-dated debt (top-5 raised ~US$270bn since Jan 2026, 30–40yr maturities) and off-balance-sheet leases/project finance (disclosed data-center lease obligations ~US$1.4tn, ~US$1.1tn off-balance-sheet) (*S&P Global, Aug 2026; JPMAM, 2026; BofA, Aug 2026*). PIMCO and others warn that prepayments/offtake/vendor financing create "induced demand" that is "not the same as organic demand" (*PIMCO, 2026*). **If any large model lab or neocloud stumbles on funding, the correlated unwind would hit every name in this book simultaneously.** This is not a tail I can dismiss; it is the central macro risk and is reflected in conservative sizing and the invalidation triggers in §3.

**How I'm positioned.** A **six-name long book** built as a barbell:
- **Anchor compounders with defensible moats and (relatively) reasonable valuations:** NVIDIA, TSMC.
- **The cheapest, most asymmetric leg — the memory supercycle:** Micron.
- **Custom-silicon growth with secured supply:** Broadcom.
- **Physical-infrastructure diversification away from silicon:** Vertiv (power/thermal).
- **Networking/interconnect:** Arista.

This spans five different layers of the supply chain to diversify *company-specific* risk, while being honest that all six share the *same* underlying capex-cycle beta (see §3).

**Ranked long book (detail in §2):**

| Rank | Name | Ticker | Conviction | Weight |
|---|---|---|---|---|
| 1 | NVIDIA | NVDA | High | 24% |
| 2 | TSMC (ADR) | TSM | High | 18% |
| 3 | Micron | MU | High | 17% |
| 4 | Broadcom | AVGO | Medium-High | 16% |
| 5 | Vertiv | VRT | Medium | 13% |
| 6 | Arista Networks | ANET | Medium | 12% |
| | **Total** | | | **100%** |

---

## 2. The long book

> **On valuation figures:** Prices and multiples below are third-party web-sourced snapshots as of early-to-mid September 2026 and are approximate. Forward P/Es depend heavily on which fiscal year is used as "forward"; in a cycle inflecting this fast, consensus EPS is a moving target. Treat every multiple as ±a wide band.

### 1) NVIDIA (NVDA) — *core anchor* — **Conviction: High — Weight: 24%**

**(a) Core thesis.** NVIDIA remains the default AI compute platform (silicon + NVLink + CUDA/software + systems). Q2 FY2027 (quarter ended ~Jul 2026, reported **Aug 26, 2026**): **revenue $96.2bn (+106% YoY)**, **Data Center $89.0bn (+117% YoY, +18% QoQ)**; Q3 FY2027 guide **$108.0bn ±2%** with **~74% gross margin**, and — importantly — that guide assumes **zero China data-center compute revenue** (*NVIDIA IR press release & 10-Q materials, Aug 26, 2026*). The moat is widening, not narrowing: even the most credible custom-silicon competitor (Broadcom/OpenAI "Jalapeño") is described by its own backers as merely *comparable* to Vera Rubin on their specific workloads (*AVGO Q3 FY26 call, Sep 2026*) — i.e., NVIDIA is still the benchmark.

**(b) Catalysts (next ~6 months).**
- **Vera Rubin ramp:** initial shipments in Q3 (now), volume ramp Q4 and into 1H2027, at partners incl. CoreWeave, Google Cloud, Azure, Oracle, Nebius (*NVIDIA release + earnings call, Aug 2026*). Successful Rubin execution is the single biggest 6-month swing factor.
- **Q3 FY2027 print (~Nov 2026):** first clean read on Blackwell→Rubin transition economics and margins.
- **Reported >15% price increase on Rubin/Grace-Blackwell servers in early 2027** (*Bloomberg via TrendForce, Aug 25, 2026*) — supports revenue/mix even as HBM costs rise.
- Potential optionality (not in guide): any China re-opening would be incremental upside.

**(c) Valuation snapshot (as-of ~Sep 4–10, 2026).** Price ~**$215–225**; market cap ~**$5.2–5.5tn**; **forward P/E ~23–25x** on non-GAAP FY-ahead EPS; consensus "Strong Buy," average PT ~**$319–323** (range $180–$515) (*stockanalysis.com, pevaluator, vcpscanner, Aug–Sep 2026*). For ~50–90% forward EPS growth, a low-to-mid-20s forward multiple is the most reasonable large-cap valuation in the group. **Caveat:** the trailing multiple is far higher; "cheap" here is entirely a function of consensus forward EPS being right.

**(d) Primary risks.** Rubin execution/yield slip; the circular-financing/air-pocket macro (NVDA is the highest-beta expression of it); customer concentration in a handful of hyperscalers + neoclouds; China policy whiplash; the long-term threat that custom ASICs erode share at the margin.

**(e) Conviction: High.** Best combination of moat, visibility, and (relative) valuation sanity.

**(f) Weight: 24%.** Largest single position, but deliberately capped below ~25% given it is also the purest embodiment of the shared macro risk.

---

### 2) TSMC (TSM) — *the indispensable foundry* — **Conviction: High — Weight: 18%**

**(a) Core thesis.** Every credible AI accelerator — NVIDIA, AMD, and the custom XPUs from Broadcom/Marvell — is fabricated at TSMC on leading-edge nodes and packaged with TSMC CoWoS. It is the lowest-drama way to be long *all* of AI compute regardless of which chip designer wins. Q2 2026 (**reported Jul 16, 2026**): revenue **NT$1,270bn (~US$40.2bn), +36% YoY**; **gross margin 67.7%**; HPC now the dominant platform. Full-year 2026 revenue growth guided **"slightly above 40%" in USD**; 2026 capex raised to **US$60–64bn** (*TSMC Q2 2026 earnings release & call, Jul 16, 2026*).

**(b) Catalysts (next ~6 months).**
- **Q3 2026 print (~mid-Oct 2026):** guide is **US$44.6–45.8bn revenue, 65–67% GM** despite 3–4pt dilution from the 2nm ramp — a beat/raise here is a clean positive.
- **2nm (N2) ramp** (3% of wafer revenue in Q2, ramping steeply) and continued **CoWoS capacity expansion** (management repeatedly expanding advanced-packaging capacity; industry checks point to ~120–140k wafers/mo in 2026 heading toward ~190–200k/mo in 2027 — *note: the 2027 figure is analyst/press estimate, not company-confirmed*).
- January 2027 full-year 2027 guide will set the tone but lands right at the edge of the horizon.

**(c) Valuation snapshot (as-of Sep 4, 2026).** Price ~**$428.91** (ADR); **forward P/E ~19.3x** (trailing ~28x); 3-yr EPS growth forecast ~40%; consensus "Strong Buy," average PT ~**$554** (*stockanalysis.com, Sep 4, 2026*). Cheapest large-cap on a growth-adjusted basis in this book.

**(d) Primary risks.** **Single-geography/single-fab concentration in Taiwan** — the dominant idiosyncratic risk (geopolitical/seismic); overseas-fab margin dilution; FX (NT$/US$); customer concentration; and the same end-market capex-cycle risk. A Taiwan shock would be catastrophic and is un-hedgeable within this book.

**(e) Conviction: High.** Highest quality/valuation trade-off; lower single-product risk than the chip designers.

**(f) Weight: 18%.**

---

### 3) Micron (MU) — *the memory supercycle, cheapest asymmetry* — **Conviction: High — Weight: 17%**

**(a) Core thesis.** HBM and DRAM are the tightest links in the AI chain. Micron's fiscal Q3 2026 (ended ~May 2026, **reported Jun 24, 2026**) was a record, and — most importantly — **FQ4 guidance was revenue $50.0bn ±$1.0bn, gross margin ~86%, EPS $31.00 ±$1.00** (*Micron 8-K, Jun 24, 2026*). **⚠️ Uncertainty flag:** these figures imply a memory upcycle of extraordinary magnitude (a multiple of Micron's historical quarterly revenue and far above historically normal DRAM gross margins). I am reporting the guidance as published; I could **not** fully reconcile the revenue magnitude against Micron's historical run-rate, and readers should treat the absolute levels with heightened skepticism even as the *direction* (severe tightness, rising ASPs) is corroborated by many independent sources. HBM4 is shipping in volume (>$1bn already), ramping ~2x faster than HBM3E 12-high; HBM4E volume production expected CY2027 (*Micron 8-K + call, Jun 24, 2026*).

**Corroborating supply/pricing evidence:** SK Hynix's HBM is "sold out" for ~3 years and its 2027 HBM4 capacity is reportedly effectively committed; SK Hynix's CEO called 2027 the "worst" memory shortage year in history; HBM4 is estimated at **~$31–32/GB for NVIDIA (~2x HBM3E)**, with 2027 HBM ASPs projected **+50% to +79%** (*Seoul Economic Daily Apr 2026; NeuralWired Aug 2026; TrendForce Aug 25, 2026; Cantor/Fubon via aistockwire, Aug 2026*). Conventional DRAM ASPs are also rising sharply as HBM consumes wafers.

**(b) Catalysts (next ~6 months).**
- **FQ1 2027 print (~late Sep 2026):** imminent; first confirmation of whether the ~$50bn/86%-GM trajectory is holding.
- **2027 HBM/DRAM price negotiations** finalizing at large step-ups.
- Ongoing HBM4 qualification wins across accelerator platforms (NVIDIA, AMD, Broadcom).

**(c) Valuation snapshot (as-of ~Aug 16, 2026).** Price ~**$971**; market cap ~**$1.10tn**; **forward P/E ~13.3x**, **forward PEG ~0.51**; consensus PT ~**$1,562** (~+61%) across ~70 analysts (*vcpscanner, Aug 16, 2026*). On its face the cheapest name in the book — but memory multiples are *supposed* to look cheap at the top of a cycle (peak earnings, trough multiple).

**(d) Primary risks.** **Cyclicality is the whole story:** memory has always mean-reverted, and a low forward P/E on possibly-peak earnings is the classic value trap. If the capex air-pocket hits, memory over-earns then over-corrects fastest. Also: capacity additions from SK Hynix/Samsung; execution on HBM4E; and the reliability of the extraordinary reported financials (see flag above).

**(e) Conviction: High — but explicitly the highest-variance High in the book.** The asymmetry (13x forward, PEG ~0.5, sold-out supply) is too compelling to underweight, but it is sized below the anchors because of cyclicality.

**(f) Weight: 17%.**

---

### 4) Broadcom (AVGO) — *custom silicon + AI networking* — **Conviction: Medium-High — Weight: 16%**

**(a) Core thesis.** Broadcom is the primary arms-dealer for hyperscaler *custom* accelerators (XPUs) plus the leader in AI networking (Tomahawk/Jericho Ethernet). Q3 FY2026 (ended Aug 2, 2026, **reported Sep 2, 2026**): **revenue $29.6bn (+86% YoY)**; **AI semiconductor revenue $16.7bn (+221% YoY, +54% QoQ)**; record ~68% operating margin. Q4 guide **$34.8bn revenue** with **AI $21.7bn (+236% YoY)**. Management raised FY2026 AI revenue to **$58bn** and put hard numbers on the out-years: **~$115bn FY2027 and ~$230bn FY2028, with "supply secured"** (*Broadcom PRNewswire release + Q3 FY26 call, Sep 2–9, 2026*). Customers now include Google (TPU), Anthropic, Meta (MTIA), and OpenAI (Jalapeño), with Anthropic on track to become the largest XPU customer in 2027.

**(b) Catalysts (next ~6 months).**
- **Q4 FY2026 print (~Dec 2026):** first test of the $21.7bn AI-quarter guide and any refresh of the FY2027 $115bn framing.
- **Tomahawk 6/Ultra ramp and Tomahawk 7 (200 Tbps) tape-out** milestones.
- New/expanded XPU program disclosures (the "7th customer"/incremental gigawatt announcements have been recurring catalysts).

**(c) Valuation snapshot (as-of ~Sep 9, 2026).** Price ~**$364**; **trailing P/E ~46.5x** (≈5-yr median); forward P/E not cleanly available; Piper Sandler initiated Overweight, PT **$460** (Sep 9, 2026) (*GuruFocus, Sep 9, 2026*). Richer than NVDA/TSM/MU; the multiple already prices successful execution of a very steep ramp.

**(d) Primary risks.** **Customer concentration is acute:** the multi-hundred-billion out-year AI framework rests on ~6 XPU customers, several of them cash-burning model labs dependent on external funding — the epicenter of the circular-financing risk. "Supply secured" is a management assertion about capacity, not a demand guarantee. Valuation leaves little margin for a single program slip.

**(e) Conviction: Medium-High.** Elite execution and genuine second-source-to-NVIDIA status, marked down from High purely on concentration + valuation.

**(f) Weight: 16%.**

---

### 5) Vertiv (VRT) — *power & thermal (the physical bottleneck)* — **Conviction: Medium — Weight: 13%**

**(a) Core thesis.** The buildout is increasingly gated by **power and cooling**, not just chips. Vertiv is a leading vendor of data-center power distribution and (liquid) thermal management, with content-per-megawatt rising as racks move to higher density and AC→DC architectures. It is deliberately included as **diversification away from silicon** — a different bottleneck, a different failure mode. Q2 2026 (**reported Jul 29, 2026**): **revenue $3.274bn (+24% YoY, +18% organic)**; FY2026 guide raised to **~$14.0bn revenue (~31% organic growth)** and **adjusted EPS $6.65–6.75 (+~60%)** (*Vertiv IR release + 10-Q, Jul 29, 2026*).

**(b) Catalysts (next ~6 months).**
- **Q3 2026 print (~late Oct 2026) is a genuine binary.** Q2 revenue *missed* (~$3.274bn vs ~$3.38bn consensus) on "supply-chain congestion and project timing," and the stock fell as much as **17% on Jul 29, 2026** (*top1markets analysis, 2026*). The FY midpoint requires a large H2 ramp (Q4 ≈$4.33bn implied); Q3 in-range would validate the "timing" explanation, a second miss would turn "timing" into "trend."
- Continued order/pipeline commentary (note: **Vertiv did not disclose a backlog or orders figure in the Q2 2026 release** — a transparency step-down vs the ~$8.5bn backlog it led with in Q2 2025; this is itself a yellow flag).

**(c) Valuation snapshot (as-of ~Sep 2026).** Price ~**$252.83**; **~44x forward earnings**; consensus ~29.7% 3–5yr EPS CAGR (*finviz, 2026*). Rich for an electrical-equipment company; prices continued flawless execution.

**(d) Primary risks.** **Execution/conversion risk** (turning orders into on-time revenue) is the near-term crux, not demand; long fixed-price contracts; tariffs/supply chain; competition (Schneider, Eaton). Higher operational-execution risk than the semiconductor names, hence Medium.

**(e) Conviction: Medium.** Best *diversifying* exposure in the book, but the Q3 print is a real coin-flip.

**(f) Weight: 13%.**

---

### 6) Arista Networks (ANET) — *AI back-end/front-end Ethernet* — **Conviction: Medium — Weight: 12%**

**(a) Core thesis.** Arista is the leader in high-performance data-center Ethernet, riding the shift of AI fabrics toward Ethernet (scale-out, and increasingly scale-up/scale-across vs proprietary interconnects). Q2 2026 (**reported Aug 4, 2026**): **revenue $3.036bn (+37.7% YoY)** — its first $3bn quarter; FY2026 guidance **raised (3rd time this year) to ~$12.6bn (+40%)**, with **AI fabrics ≥$3.5bn** and broader AI networking ~$3.6bn; Q3 guide ~**$3.3bn**, op margin **48–49%** (*Arista 8-K/earnings release + call, Aug 4, 2026*).

**(b) Catalysts (next ~6 months).**
- **Q3 2026 print (~early Nov 2026):** the "$1.1bn upside question" management left open on how they ship mix could resolve favorably.
- **1.6T Etherlink platforms** heading toward 2027 production; scale-up/scale-across Ethernet displacing NVLink/InfiniBand over time (a multi-year, not 6-month, driver).

**(c) Valuation snapshot (as-of Sep 4–10, 2026).** Price ~**$191.56**; **forward P/E ~42–47x**, **PEG ~1.76**, EV/EBITDA ~50x (*stockanalysis.com/exa, Sep 2026*). Cheaper than MRVL, richer than the anchors.

**(d) Primary risks.** **Gross-margin pressure from memory/silicon cost inflation** — management explicitly kept FY GM at 62–64% "inclusive of anticipated supply-chain cost increases for memory and silicon" (*Arista Q2 2026 call*). This is the one place in the book where the memory shortage (bullish for MU) is a *headwind*. Also: hyperscaler self-build/white-box competition; NVIDIA/Broadcom competing in Ethernet; customer concentration (Microsoft/Meta historically large). Rated Medium.

**(f) Weight: 12%.**

---

### Names considered but not included (and why)

- **AMD (AMD).** Real #2 accelerator momentum: Q2 2026 (Aug 4, 2026) revenue **$11.5bn (+50%)**, Data Center **$6.7bn (+107%)**, Q3 guide **~$13bn**, MI450/Helios ramping late Q3 with Anthropic (up to 2GW) and OpenAI/Meta deals (*AMD IR, Aug 4, 2026*). **Excluded on valuation/timing:** forward P/E reported ~**67x** (*vcpscanner, Aug 2026*), and the biggest Helios volumes (e.g., Anthropic's first GW) are **1H2027** — largely *after* the 6-month window's core catalysts. A strong candidate to add on a pullback; it is my top "next-in."
- **Marvell (MRVL).** Excellent custom/connectivity story (Q2 FY27 rev **$2.739bn +37%**, FY27 raised to ~$12bn, FY28 ~$18bn; *Aug 27, 2026*), but **forward P/E ~76x** (*tgmcharts, Aug 2026*) is the richest large-cap here; overlaps AVGO's custom-silicon thesis with less scale. Redundant given AVGO.
- **Astera Labs (ALAB) / Credo (CRDO).** Hyper-growth interconnect (ALAB Q2'26 rev **$392.4m +104%**, Q3 guide $540–560m; CRDO FQ2'26 rev **$268m +272%**). Superb fundamentals but small-cap, very expensive, and highly volatile — too much single-name risk for a concentrated 6-name book. Best expressed as small satellite positions, not core.
- **ASML.** The ultimate monopoly (Q2 2026 rev €9.3bn, FY26 €43–45bn, capacity +30% for 2027; *Jul 15, 2026*), but its revenue is **one step further removed** from the 6-month capex pulse (litho tools lead fabs by quarters/years). Great long-term hold, less optimal for a 6-month catalyst window; TSM is the more direct semicap-adjacent expression.
- **Memory alternatives (SK Hynix / Samsung).** Arguably purer HBM plays than Micron, but ADR/foreign-listing liquidity and disclosure make MU the cleaner US-listed expression; Samsung also carries more diversified/non-AI drag.
- **AMAT / LRCX / KLA / COHR / ARM.** Fine businesses; omitted to keep the book concentrated and to avoid stacking more of the same capex beta. COHR (optics) partially overlaps ANET's networking exposure.

---

## 3. Portfolio-level view

### Concentration & factor exposure
- **Single shared macro factor:** all six names are long the **AI data-center capex cycle**. Diversification here is across *supply-chain layer* (compute / foundry / memory / custom silicon / power / networking), **not** across *demand drivers*. In a broad "AI capex air-pocket," correlations go to ~1 and the book draws down together. This is the most important limitation of the book and is why total exposure should be sized as a single high-conviction *theme*, not six independent bets.
- **Style:** high-growth, high-multiple, high-beta, large-cap-tech-tilted (except MU, which is deep-cyclical/lower-multiple and acts as the book's "value"/mean-reversion ballast — though it is cyclical, not defensive).
- **Rough weightings by layer:** Compute (NVDA) 24% · Foundry (TSM) 18% · Memory (MU) 17% · Custom silicon + networking ASIC (AVGO) 16% · Power/thermal (VRT) 13% · Ethernet networking (ANET) 12%.

### Supply-chain interlock (idiosyncratic-but-shared exposures)
- **TSMC single-point-of-failure:** NVDA, AVGO (and excluded AMD/MRVL) **all** depend on TSMC leading-edge wafers + CoWoS. A Taiwan disruption hits the whole book (and TSM itself). No intra-book hedge exists for this.
- **HBM/DRAM two-way exposure:** the memory shortage is **bullish MU** but a **cost headwind for ANET (and NVDA/AVGO BoMs)**. The book is net-long memory tightness via MU; ANET is the partial offset. NVDA passing through a >15% server price increase (Bloomberg, Aug 2026) suggests pricing power absorbs much of the memory cost — a mild internal hedge.
- **Customer concentration overlaps:** the same ~5 hyperscalers + a handful of model labs (OpenAI, Anthropic) are the end-buyers for **every** name. AVGO is the most exposed (~6 XPU customers). If one large model lab's financing falters, AVGO and NVDA are hit first, then the rest.
- **Financing risk:** the demand is increasingly debt-/lease-/prepay-financed and, per S&P/PIMCO/JPMAM, partly *circular*. This is the systemic risk that the diversification above does **not** address.

### What would INVALIDATE each thesis (falsification triggers)
Written so each can be checked against hard evidence in the next ~6 months:

- **NVDA:** A Vera Rubin yield/ramp slip that forces a Q3 FY2027 (~Nov) revenue guide *below* the $108bn ±2% already given, **or** gross margin guided below ~72% (mix/HBM cost), **or** a hyperscaler publicly cutting/deferring 2027 orders. Any of these breaks the "visibility" pillar.
- **TSM:** Q3 2026 (~Oct) revenue below the US$44.6bn floor, **or** a cut to the "slightly above 40%" FY26 USD growth, **or** a CoWoS/2nm capacity or yield problem, **or** (catastrophic) any Taiwan geopolitical/seismic event. FX (NT$ strength) beyond guide assumptions is a softer negative.
- **MU:** FQ1 2027 (~late Sep) guide that fails to confirm the extraordinary revenue/margin trajectory, **or** any evidence the reported figures were mis-stated, **or** SK Hynix/Samsung announcing accelerated HBM/DRAM capacity that breaks the "sold out through 2027" narrative, **or** spot DRAM/HBM contract prices rolling over. Given the cyclicality, MU's thesis is the fastest to flip.
- **AVGO:** Any XPU customer publicly reducing/canceling a program, **or** a Q4 FY26 (~Dec) AI-revenue miss vs the $21.7bn guide, **or** a walk-back of the FY2027 ~$115bn framing. Because so much value is in out-year promises, *guidance* (not just prints) is the trigger.
- **VRT:** A **second** consecutive revenue miss/timing shift at the Q3 2026 (~late Oct) print, **or** failure to re-disclose backlog/orders (continued opacity), **or** an H2 that doesn't deliver the implied ~$8bn to hit the FY midpoint. VRT has the nearest-term, most concrete binary.
- **ANET:** Gross margin guided below the 62–64% range (memory/silicon cost pass-through failing), **or** a hyperscaler shifting AI back-end networking to white-box/NVIDIA/Broadcom at Arista's expense, **or** a Q3 (~Nov) miss vs the ~$3.3bn guide.

**Portfolio-level kill switch:** if two or more of the following occur — a hyperscaler *cuts* 2027 capex guidance, a major model lab reports a financing shortfall, or the IG/HY credit spreads on hyperscaler/neocloud debt gap wider — the correlated-downside thesis for the *entire* book is triggered and the theme should be de-risked, not just the single name.

---

## 4. Methodology & data provenance

**Approach.** Top-down (capex cycle & financing) → bottom-up (most-recent quarterly results/guidance per name) → cross-checked supply/demand signals (HBM, CoWoS, power) → valuation snapshots → ranked construction with explicit conviction, catalysts, risks, and falsification triggers. Emphasis on **most-recent 2026 datapoints** and on flagging uncertainty rather than manufacturing precision.

**Primary sources (company filings / IR / press releases):**
- NVIDIA — Q2 FY2027 results, IR press release / SEC 8-K materials, **Aug 26, 2026** (rev $96.2bn; DC $89.0bn; Q3 guide $108bn ±2%; Vera Rubin ramp).
- Broadcom — Q3 FY2026 results, PRNewswire release + earnings call, **Sep 2 & 9, 2026** (rev $29.6bn; AI semi $16.7bn; Q4 & FY26/27/28 AI framing).
- TSMC — Q2 2026 earnings release, management report, call transcript & presentation, **Jul 16, 2026** (rev NT$1,270bn/US$40.2bn; GM 67.7%; Q3 & FY26 guide; capex $60–64bn).
- Micron — FQ3 2026 8-K / earnings release, **Jun 24, 2026** (record results; FQ4 guide $50bn ±$1bn, GM ~86%, EPS $31 ±$1; HBM4 >$1bn shipped). *Absolute magnitudes flagged as not fully reconciled.*
- AMD — Q2 2026 results (8-K + slides + call), **Aug 4, 2026** (rev $11.5bn; DC $6.7bn; Q3 ~$13bn; Helios/MI450).
- Marvell — Q2 FY2027 release + call, **Aug 27 & 31, 2026** (rev $2.739bn; FY27 ~$12bn / FY28 ~$18bn).
- Arista — Q2 2026 8-K / earnings release + call, **Aug 4, 2026** (rev $3.036bn; FY26 ~$12.6bn; Q3 ~$3.3bn).
- Astera Labs — Q2 2026 release + 10-Q + call, **Aug 4, 2026** (rev $392.4m; Q3 $540–560m).
- Vertiv — Q2 2026 IR release + 10-Q + call, **Jul 29, 2026** (rev $3.274bn; FY26 ~$14.0bn; adj EPS $6.65–6.75).
- ASML — Q2 2026 results + call/presentation, **Jul 15, 2026** (rev €9.3bn; FY26 €43–45bn; capacity +30% for 2027).
- Credo — FQ2 2026 earnings call transcript (rev ~$268m; scale-up roadmap). *Fiscal-period labeling verify against Credo filings.*

**Secondary / market-data sources (used with more caution):**
- Capex & financing: TMT Finance (Sep 2026); BofA via EdgeX (Aug 2026); S&P Global Ratings (Aug 27, 2026) & The Motley Fool summary (Sep 6, 2026); Citi via Investing.com (2026); PIMCO (2026); J.P. Morgan Asset Management (2026); Pivot-to-AI/FT (Sep 2026); The Regulatory Review (Sep 10, 2026); Philstar (Sep 9, 2026) — the last two are opinion/bubble-skeptic pieces, used only for framing the bear case.
- Memory supply/pricing: Seoul Economic Daily (Apr 2026); NeuralWired (Aug 18, 2026); TrendForce (Aug 25, 2026); Cantor/Fubon via aistockwire (Aug 2026); 404kresearch/Goldman-cited (2026).
- Valuations/prices: stockanalysis.com, pevaluator, vcpscanner, gurufocus, tgmcharts, finviz, exa.ai — snapshots dated **Aug 10 – Sep 10, 2026**.

**Explicit limitations & uncertainty.**
- **Prices/multiples are third-party web snapshots**, intraday and approximate; not verified against a paid market-data terminal. Forward P/Es vary by which fiscal year is "forward" and by GAAP vs non-GAAP.
- **Micron's reported revenue/GM magnitudes could not be fully reconciled** to historical run-rates and are flagged; the *direction* (severe tightness) is well-corroborated, the *levels* are not independently confirmed here.
- **Some out-year figures are management guidance** (AVGO FY27/28 AI revenue; NVDA/Broadcom capex framing) — assertions, not facts.
- **CoWoS 2027 capacity, HBM 2027 ASP (+50–79%), and 2027 hyperscaler capex ($1.2–1.3tn)** are analyst/press estimates with wide dispersion; ranges are given rather than point estimates.
- **Transcripts from third-party aggregators** (Motley Fool, Roic, Globe & Mail, exa.ai, etc.) may contain transcription errors; primary IR/SEC documents were preferred where available.
- No independent DCF or scenario model was built; conviction reflects qualitative synthesis of the above, not a proprietary quantitative forecast.

---

## 5. Disclaimer (full)

**This is research/educational analysis, not investment advice.** Nothing herein is a recommendation, solicitation, or offer to buy or sell any security or to adopt any investment strategy. It was generated by an AI research agent as a point-in-time exercise on **2026-09-10** and reflects **public information that may be incomplete, out-of-date, mis-transcribed, or incorrect.** Specific figures — especially prices, multiples, and the extraordinary reported memory-segment financials — were gathered via web search and are **not** verified against audited filings or a professional market-data terminal; some could not be reconciled and are explicitly flagged as uncertain.

Forward-looking statements (company guidance, analyst targets, capex forecasts, price/ASP projections) are inherently uncertain and **are not guarantees**; actual results may differ materially. **Past performance and projections are not indicative of future results.** The securities discussed are volatile, and the book is intentionally **concentrated in a single macro theme (AI capex)** — meaning the names can and likely will move together, and losses can be large and rapid, including permanent loss of capital, particularly if the AI capital-spending cycle disappoints or its circular/debt-financed demand unwinds.

The author holds no position in the named securities, has no ability to guarantee the accuracy of third-party data used, and accepts no liability for decisions made in reliance on this document. **Do your own due diligence and consult a licensed financial professional before making any investment decision.**
