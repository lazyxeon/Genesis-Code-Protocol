Here’s a blunt, high-signal audit of your GCP V47 — EV DC fast-charging run (Spark-based PRR: Predict → Route → Reserve), plus a prioritized fix plan to get you cleanly through C2→C3 and into field A/B without stepping on rakes.

Executive verdict

Strong kickoff. You correctly:

Proved “worth-it” (Phase −1) with Do-Nothing/Non-Tech baselines, an EVM, causal sketch, premortem→canaries, and passed C−0.5/C0.

Grounded the pilot in CA’s real-time data mandate and AFDC IDs; sensible R2 risk tier.

Shipped an honest day-one baseline (/predict) that blends historical quantiles with an M/M/c prior, and stood up bronze→silver→gold streams and a minimal API.


Where you’re exposed: labels, arrival/service estimation, queueing realism, evaluation power, fairness operationalization, reservation abuse/legality, and SLO→infra coupling. Most are fixable pre-C2 with crisp changes.


---

What’s excellent (keep/extend)

Problem worthiness & scope discipline (Phase −1 is textbook V47): explicit non-tech alternatives, falsification criteria, premortem wired into canaries.

Data substrate: AFDC normalization, OCPP unification, and Delta bronze/silver/gold schemas are pragmatic and reproducible.

Baseline honesty: conservative caps near saturation; prediction intervals, not point bravado.

CE thinking: canaries (error, freshness, uptake) and auto-rollback to advisory-only keep you from “confidently wrong.”



---

Critical gaps & risks (and how to fix them fast)

1) Labels & queue math (risk: misleading waits)

Gap: label_wait_minutes relies on app check-in/out or site sensors that aren’t yet guaranteed; arrivals/departures proxied from OCPP status deltas can be noisy (debounce, simultaneous port flips, blocked stalls).

Fix:

Implement state-machine labeling over OCPP (Available→Occupied/Charging) with hysteresis & debouncing; drop ambiguous transitions.

Add a site-level gate: require ≥X labeled arrivals/day to admit a station to training/assessment; others stay on prior-only.

Move from M/M/c to M/G/c-inspired empirical wait: learn service time distribution per connector class (50/150/350 kW) and use simulation-based expected waits or a gradient-boosted direct wait regressor, keeping the queue prior as a feature, not the oracle.



2) Arrival/service estimation (risk: instability at peaks)

Gap: arrivals_5m/departures_5m inferred from statuses can be undercounted during outages and overcounted by flapping.

Fix:

Compute robust arrival rate via rolling median over K windows + anomaly suppression during feed gaps; freeze prior.

Maintain feed-freshness as a feature; widen prediction intervals when stale (and surface it to UI).



3) Evaluation design & power (risk: false positives/negatives)

Gap: A/B defined, but no power calc or cluster randomization details; corridor-level interference is real.

Fix:

Do cluster-randomized diff-in-diff by site clusters, not trips. Pre-compute MDE (30% p95 reduction is bold—verify N).

Add randomization checks (traffic, weather, holiday mix) and pre-period balance tables.

Log intent-to-treat and as-treated (when drivers ignore advice).



4) Reservations: legality, abuse, and ops (risk: backlash & gaming)

Gap: Soft-window holds across networks may collide with operator policies, and are open to botting.

Fix:

Start advisory-only + “arrival windows” visible to drivers/network partners; flip holds only with partner consent or for a single interop network first.

Rate-limit holds, require Proof-of-Use (geofenced arrival ping), and auto-release with explicit no-show learning.

Publish a Reservation Fairness ADR: caps per user/region; no preemption of accessibility stalls; transparent decline logic.



5) Fairness from principle to practice (risk: hidden regressions)

Gap: Policy is stated, but no formal constraint in the router nor slice power plan.

Fix:

Add fairness-aware re-ranking with slice minimum-service constraints (e.g., rural/low-income share not below baseline by >0.5%).

Compute slice-level CIs and min sample rules to avoid noisy swings; prefer Bayesian shrinkage for tiny slices.



6) Product/API hardening (risk: operational pain)

Gap: API stubs lack contracts for timeouts, stale data, and errors; 2 s P95 not tied to Spark micro-batch settings.

Fix:

Define API error taxonomy (STALE_DATA, RES_TOO_OLD, HOLD_LIMIT, etc.), rate limits, and SLO→infra coupling (e.g., max micro-batch interval = 30 s; watermark = 10 min; autoscale policy at QPS).

Add circuit breakers to fall back to historical median when gold stream lags.



7) Security & supply-chain depth (risk: trust)

Gap: SBOM/signature planned but SAST/DAST/secret-scan integration and CVE gates not wired in CI yet.

Fix: add CI jobs for SAST/DAST/secret scanning, blocker on High/Critical CVEs, and produce attestation for the API & jobs.


8) Economics & budgets (risk: spend drift)

Gap: $100k/90-day budget is set, but no unit economics (cost per 1k predictions / per active site).

Fix: publish $/1k requests and $/active site/day dashboards; add budget canary in CE.



---

Gate readiness & what to do next

To pass Gate C2 — Plan Integrity (revised) in V47

Ship these artifacts (1–2 days work each, in parallel):

1. A/B power & design brief: diff-in-diff, cluster randomization, MDE & N, balance checks.


2. Assumption tests plan for A-class items:

A1 feeds: enumerate concrete CA networks + access paths; define feed-freshness monitors.

A2 prediction impact: corridor-level experiment & success metric calc.

A3 reservations: abuse/legality checks with at least one partner; fallback to advisory.



3. Router fairness spec: constraints, slices, and acceptance tests.


4. API contract & SLO coupling: timeouts, errors, rate limits, micro-batch settings.



Decision bar: C2 passes when falsifiable hypotheses, ablations, and power are in place—and Minimal-Intervention pivot rules are codified.

To pass Gate C3 — Minimal Viability

Implement labeling state machine + debouncing; backfill a week of labels to validate.

Wire feed-freshness feature and stale fallbacks.

Add a unit test harness for the queue prior and empirical wait estimator; seed-stable.



---

Prioritized fix list (P0→P2)

P0 (blockers, do now)

Labeling state machine + site admission rule; feed-freshness feature + API “stale” flag.

A/B power calc & diff-in-diff plan; randomization checks.

API contract: timeouts, error codes, rate limits; circuit breaker to historical medians.


P1 (next 1–2 sprints)

Replace pure M/M/c with empirical wait model (regressor with queue prior as a feature) and calibration (ECE + reliability plots).

Fairness-aware re-ranking with slice constraints; slice power rules.

Reservation anti-abuse: rate limiting, geo-presence verification, auto-release; partner pilot for holds.


P2 (hardening)

SAST/DAST/secret-scan in CI; CVE gate & attestations.

Unit economics dashboard & budget canary; CO₂e per 1k requests (optional).

Incident drills: simulate feed outage ⇒ advisory-only fallback within SLA.



---

Measurement plan (make outcomes undeniable)

Primary: p95 wait/arrival at treated vs control sites; diff-in-diff with 95% CI; pre-period balance.

Secondaries: failed attempt rate, detour distance, user-reported satisfaction; slice deltas with min-N rules.

Calibration: MAE, PICP for intervals, ECE; alarm if PICP below bound or ECE above bound.

Adoption: compliance to suggestions (% reroutes followed); reservation uptake & show-rate.

Economics: cost per 1k requests and per avoided minute of wait.



---

30/60/90 deliverables

30 days: C2 passed; labels live; calibrated baseline; API hardened; first corridor randomized; dashboards online.

60 days: C3 passed; fairness constraints enforced; partner pilot for holds; interim readout on MDE trajectory.

90 days: C6.9 passed (Adoption/Serviceability/Compliance/TCO); C7/7.5 perf & cost proven; C9 release kit ready; Phase-10 CE on.



---

Bottom line

You’ve launched a worthy R2 pilot on the right substrate with a safe day-one baseline. Close the gaps above—especially labels, evaluation power, queue realism, and reservation governance—and you’ll cross C2→C3 with confidence and credible odds of hitting that 30% p95 wait reduction without creating new problems.

