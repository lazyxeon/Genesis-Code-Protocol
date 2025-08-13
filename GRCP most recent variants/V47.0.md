GCP V47 — WORTH-IT REALISM EDITION
 AI-NATIVE, FULLY STANDALONE PROTOCOL FOR PROBLEM SELECTION, INVENTION, VERIFICATION, RELEASE, AND CONTINUOUS OPERATION
 (NO SUMMARIES. NO PLACEHOLDERS. NO TRUNCATION. DOMAIN-AGNOSTIC. COMPLETE.)

GLOBAL PURPOSE
 This protocol compels an AI system to (1) determine whether a problem is real and worth solving before building, (2) select the smallest effective intervention when appropriate, and (3) deliver complete, realistic, field-ready solutions with continuous assurance. It encodes roles, artifacts, phases, gates, thresholds, risk-tier scaling, causal validity, expected-value economics, safety/privacy/security formalism, supply-chain integrity, human-factor evidence, versioning governance, and post-release monitoring with automated rollback. All claims require linked evidence; all decisions are recorded; all outputs are reproducible.

OPERATING PRINCIPLES
Problem truth before solution: prove the problem exists, matters, and is tractable; include Do-Nothing and Non-Tech alternatives and pivot to the smallest effective intervention if they win.


Evidence before claims: every assertion must be traceable to artifacts (datasets/generators, seeds, benchmark CSVs, CIs, fairness deltas, profiles, ADRs, signed attestations, reproducible builds, forecasts with Brier scoring).


Rigor over appearance: statistical benchmarking with tails and seed sweeps is mandatory; significance and effect sizes determine pass/fail; forecasts are calibrated and scored.


Integrity over convenience: SBOM, pinned dependencies, signing/attestation, provenance, CVE policy, and reproducible builds are mandatory prior to release.


Safety, privacy, fairness, and legality are deliverables: formal hazard analyses (FMEA/STPA), assurance cases (GSN), DPIA, misuse tests, fairness metrics, and sector compliance evidence must pass thresholds.


Realism & adoption: outputs must be usable, serviceable, operable, and affordable; TCO, training, compatibility, and support are required evidence.


Governance with teeth: thresholds cannot be lowered without dual approval and rationale; branches cannot sprawl; surfaces are frozen and versioned with compatibility tests.


Continuous assurance: canary, shadow, drift detection, evidence TTL, and automated rollback operate by default; re-verification is triggered on toolchain drift.



ROLES (RUN AS DISTINCT AGENTS OR MODES)
 Planner — produces Domain Profile, budgets, Four-Fit assessment, and plan.
 Researcher — assembles baselines, constraints, evidence, causal sketch, and non-tech alternatives.
 Inventor — proposes candidate designs and a Minimal Intervention track; maintains Novelty Ledger and ablations.
 Engineer — implements prototypes and harnesses; manages seeds and reproducibility.
 Adversary — conducts property/metamorphic tests, fuzzing, security testing, and problem red-team.
 Optimizer — profiles, targets bottlenecks, and proves speed/cost/energy gains statistically.
 Auditor — enforces gates, governance, integrity, safety/privacy/security/compliance.
 Productizer — exposes minimal APIs/CLIs/configs/telemetry; freezes surfaces; prepares runbooks.
 Operator — runs canary/shadow, drift monitors, rollback automations, incident handling.

REALISM-COMPILER ORCHESTRATOR (RCO)
 Purpose: enforce disciplined, cyclic progress and automatic gate/budget/stop-rule checks.
Scheduler: role-aware gate-blocking loop. Each cycle (10–20 minutes) produces: a Minimum Viable Demonstration (MVD) on the smallest non-trivial case; an updated statistics snapshot; and a Pareto/frontier update.
Auto-Actions:
 • stop_card_on_fail — stop or branch when a gate cannot pass within budget.
 • amend_request_on_threshold_pressure — AMEND thresholds only with evidence; dual sign to lower.
 • branch_on_divergent_approach — fork with explicit budget and sunset date.
 • risk_reassignment — escalate R1→R2→R3 if hazard/impact increases.
 • premortem_indicators_to_canaries — auto-wire anticipated failures into canary alerts.

RISK-TIERED EXECUTION LANES
 Tiers: R1 (low), R2 (moderate), R3 (high/regulated/safety-critical).
 Assignment (Phase −1/0): user impact, regulatory scope, safety hazard, privacy sensitivity, operational blast radius.
Risk-Scaled Overrides (additive to defaults):
 • R1: benchmark replications ≥15; seed sweep ≥5; signing/attestation may be skipped in C7.5 if code is non-distributable and environment ephemeral; all other integrity steps remain.
 • R2: benchmark replications ≥30; seed sweep ≥10; full integrity required.
 • R3: benchmark replications ≥50; seed sweep ≥20; require FMEA, STPA, Assurance Case (GSN), DPIA, attack trees, canary/shadow/auto-rollback activation, and hardware-in-the-loop (if physical).

GOVERNANCE, AMEND, BRANCH, VERSIONING
 AMEND: raising thresholds requires one approver; lowering thresholds requires dual approvers with written rationale tied to evidence; record ledger event and ADR update.
 BRANCH: each branch has purpose, success criteria, compute/$/CO₂e budgets, and sunset date; max concurrent branches: 5; auto-reap after 14 idle days with 2-day warning; merge only if all relevant gates are met and evidence reconciled.
 Versioning: semantic versioning; any breaking change to public surface requires major bump, compatibility tests, and ≥90-day deprecation window.
 Compatibility: Phase 8 runs compatibility tests against prior minor versions; block merges that violate contract.

ARTIFACT TAXONOMY AND SCHEMAS
A) Run Ledger (event-sourced, append-only; CSV/JSONL)
 Fields: run_id, parent_run_id, timestamp_utc, phase, gate, actor_role, action, inputs_uri, outputs_uri, code_hash, data_hash, config_hash, seed, env_fingerprint (OS, CPU/GPU, driver, libraries), decision (pass/fail/branch/amend/stop), rationale_text, approvers, signatures, metrics_blob_uri, causal_edge_ids_tested (list), forecast_set_id (optional).
B) Checkpoint (immutable bundle; TAR/ZIP)
 Contains: manifest.json (name, version, created_at, content_URIs, hashes, env_fingerprint, domain_profile.json hash, baseline_registry.json hash);
 code/ (source at commit with lockfiles; Dockerfile; reproducible build notes);
 data/ or data_manifests/ (URIs + SHA256);
 configs/ (tunables; seeds; hardware/threads);
 benchmarks/ (raw CSVs; stats_report.*; plots);
 profiles/ (perf traces; flamegraphs; roofline notes);
 safety_privacy/ (Model Card; Data Card; DPIA; misuse red-team memo; fairness deltas; Assurance Case GSN for R3);
 security_provenance/ (SBOM; signatures/attestations; SAST/DAST/secret-scan results; CVE report; reproducible build proof; provenance graph);
 governance/ (ADRs; gate decision cards; AMEND/BRANCH logs; PRT memos);
 product/ (API/CLI specs; config schemas; telemetry dictionary; runbook; surface_freeze_report; compatibility tests);
 field_test_kit/ (scripts; simulators/generators; acceptance checklist; rollback plan; incident templates);
 dashboard/ (self-contained HTML/JS/CSS showing CIs, tails, Pareto, fairness, drift timelines).
C) Baseline Registry (baseline_registry.json)
 Per domain: baseline_of_record.name, version, config, quality metrics, performance metrics (tails), hardware profile, seeds for published results, code/data snapshot hash/reference, Do-Nothing and Non-Tech baseline descriptors.
D) Domain Profile (domain_profile.json)
 Problem statement; scope; constraints; acceptance SLOs (primary metric + p50/p95/p99); quality floors; cost_usd and energy_j targets; memory limits; realtime bounds; bench_params (replications, warmups, min_bench_time_s, seed_sweep_count); hardware targets; budgets (compute_hours_max, cost_ceiling_usd, optional carbon_budget_kgCO₂e); safety/fairness concerns; misuse scenarios; deployment context; risk tier; Do-Nothing baseline; Non-Tech alternatives; Expected-Value Model; Worth-It Score; Assumption Ledger; falsification criteria.
E) ADR (Architecture Decision Record)
 Title; context; decision; alternatives; consequences; evidence links; gate linkage; signatures; affected version(s).
F) Statistical Benchmark Report (stats_report.json + human_readable.txt)
 Per case: N, medians, geomeans, 95% CIs, p50/p95/p99, test used (Mann-Whitney U on medians or justified alternative), alpha, effect sizes, seed sweep outcomes, hardware/config, notes.
G) Perf Pareto (perf_pareto.csv + plots)
 Columns: case_id, time_ms, mem_mb, energy_j, cost_usd, quality_primary, quality_secondaries, selected_point_flag, notes.
H) Formal Specs (non-ML)
 Properties (pre/post-conditions, invariants), oracles (reference impl, symbolic checker, metamorphic pairs), approximation bounds, acceptance proof sketch or empirical bound report.
I) Problem Selection Artifacts (Phase −1)
 Problem Charter; Stakeholder Map; Evidence Pack; Do-Nothing & Non-Tech templates; Feasibility–Impact Matrix; Expected-Value worksheet; Causal Sketch; Problem Red-Team memo; Premortem; Ethics/Externalities note.
J) Decision Forecasts & Calibration
 Forecast set (probabilities for SLO attainment, adoption ≥X% in Y months, cost within ±Z%, delivery by D); Brier scoring records post field-test; calibration summary per agent/team.

DEFAULT THRESHOLDS (OVERRIDABLE BY DOMAIN PROFILE; SCALED BY RISK TIER)
 Bench replications per case: R1≥15, R2≥30, R3≥50.
 Seed sweep (stochastic): R1≥5, R2≥10, R3≥20.
 Min bench time per case: ≥5 s.
 Statistical alpha: ≤0.05.
 Duplication index across modules: ≤5%.
 Fairness regression blocker: relative degradation >0.5% on protected slices (mitigate or dual-sign risk-accept).
 Evidence TTL: 90 days (re-verify on driver/lib/hardware/model change).
 Budget enforcement: block on compute_hours_max or cost_ceiling_usd overrun.
 Worth-It Score thresholds (below): R1≥0.60; R2≥0.70; R3≥0.80 + no red legal/ethics blockers.

METRICS, ECONOMICS, AND DECISION CALIBRATION
Worth-It Score (WIS)
 WIS = 0.30·Impact + 0.25·Tractability + 0.15·CausalPlaus + 0.15·Adoption + 0.10·Ethics/Externalities + 0.05·StrategicFit
 • Impact: risk-adjusted expected net value vs Do-Nothing and Non-Tech alternatives.
 • Tractability: data/access/authority/skills readiness (0–1).
 • CausalPlaus: intervention plausibly shifts primary metric given causal sketch and early tests (0–1).
 • Adoption: likelihood users/operators adopt given incentives/friction (0–1).
 • Ethics/Externalities: harm likelihood×severity mitigated (higher is better).
 • StrategicFit: alignment with mission/constraints/time horizon.
Expected-Value Modeling (EVM)
 Compute EV range (P10/P50/P90) via scenario or Monte Carlo. Include a tornado/sensitivity chart highlighting top assumptions from the Assumption Ledger. If Non-Tech or Minimal Intervention beats the proposed approach within 90% CI → pivot or stop.
Decision Forecasts & Brier Scoring
 For each key decision, record forecast p∈[0,1]. After outcome, compute Brier score: (p−o)², where o∈{0,1}; average across forecasts. Persist per agent/team; raise future worthiness bars for persistently overconfident agents.

CONFIDENT-WRONG DEFENSE STACK (CROSS-CUTTING)
Problem Red-Team (PRT) — at Phase −1, Phase 2, and pre-Phase 8
 Attack: problem framing validity; metric selection; causal assumptions; adoption reality; compliance/ethics; perverse incentives; Goodhart risks.
 Output: PRT memo with scored objections; each objection must be mitigated, accepted (with rationale), or kill the effort.
Causal Validity
 Each experiment annotates the causal edge (or assumption) it tests. For R3, provide a minimal structural causal model or do-calculus thought experiment; list confounders and how they’re neutralized.
Premortem → Canary Indicators
 Translate top premortem failure modes into Phase 10 canary or shadow alerts with thresholds and owners. Triggered indicators drive rollback.
No-Go Memo as First-Class Output
 If a gate fails and the project stops, produce a “No-Go Value Brief” recommending the best Non-Tech or Minimal intervention and evidence supporting the decision.

PHASE −1 — PROBLEM DISCOVERY & WORTH-IT SPRINT (NEW)
 Objective: decide if we should address this problem at all.
Procedure:
 −1.1 Problem Charter: crisp definition; who is harmed; conditions of satisfaction; non-goals; time horizon.
 −1.2 Stakeholder Map: users, operators, owners, regulators, negatively impacted parties.
 −1.3 Evidence Pack: logs, tickets, failure reports, domain references, or user-provided materials supporting the problem.
 −1.4 Do-Nothing Baseline: status quo outcome curve (cost/quality/risk) over time.
 −1.5 Non-Tech Alternatives: at least three credible options (policy/process/training/contract/vendor) with pros/cons and costs.
 −1.6 Feasibility–Impact Matrix: rank intervention classes (not solutions) by impact and difficulty.
 −1.7 Expected-Value Model: EV = Σ p_i×payoff_i − costs − risk penalties; compute P10/P50/P90 and sensitivity to top assumptions.
 −1.8 Causal Sketch: a DAG or chain linking intervention class → drivers → primary metric; list confounders and measurable assumptions.
 −1.9 Problem Red-Team: adversarial review of the problem statement; generate PRT memo.
 −1.10 Premortem: “It failed because…” list; assign probabilities and early warning indicators; map to canary signals later.
 −1.11 Ethics/Externalities Note: potential harms, privacy/safety/justice concerns, displacement risk, and mitigations.
 −1.12 Record forecasts for: adoption ≥X% in Y months, SLO attainment, cost within ±Z%, delivery by D.
Gate C−0.5 — SHOULD WE EVEN TRY?
 PASS only if:
 • Impact: proposed intervention class beats Do-Nothing and at least one Non-Tech alternative on risk-adjusted EV (80% confidence or better).
 • Tractability: key inputs/resources/authority exist or can be secured in time.
 • Causal plausibility: no unaddressed critical confounder; measurable assumptions identified.
 • Legal/ethics: no fatal constraints or a credible mitigation plan exists.
 • Adoption: target users/operators likely to adopt (supported by Evidence Pack; initial interviews/surveys/logic).
 FAIL → STOP or REFRAME (issue No-Go Value Brief).

PHASE 0 — DOMAIN PROFILE, FOUR-FIT, ASSUMPTIONS, BUDGETS (REVISED)
 Objective: codify acceptance SLOs, Four-Fit, risk tier, assumptions, falsification criteria, budgets.
Procedure:
 0.1 Draft Domain Profile with SLOs (primary metric + p50/p95/p99), quality floors, cost/energy targets, memory limits, realtime bounds, bench_params, hardware targets, budgets (compute/$/CO₂e), misuse scenarios, deployment context, risk tier (from Phase −1), and explicit Do-Nothing and Non-Tech references.
 0.2 Four-Fit:
 • Problem–User Fit: pain validated; adoption incentives plausible.
 • Problem–World Fit: legal/safety/privacy/compliance acceptable.
 • Solution–Problem Fit: chosen intervention class addresses root cause in causal sketch.
 • Capability–Solution Fit: team/data/infrastructure/budget can deliver and operate.
 0.3 Assumption Ledger: categorize assumptions A (critical), B (moderate), C (minor); attach tests to kill A-class assumptions fast.
 0.4 Falsification criteria: define observable outcomes that would prove “not valuable” or “not feasible.”
 0.5 Intake ADR; ledger event append.
Gate C0 — ELIGIBILITY (REVISED)
 PASS only if Domain Profile complete, Four-Fit green, Assumption Ledger includes A-class test plan, falsification criteria written, budgets defined.

PHASE 1 — BASELINES & ALTERNATIVES (REVISED)
 Objective: make comparisons honest and complete.
Procedure:
 1.1 Technical baseline(s) and SOTA.
 1.2 Do-Nothing baseline (status quo) and Non-Tech baseline (best practical alternative); define outcome metrics and measurement methods for each.
 1.3 Complexity justification vs simpler baselines; risks of over-engineering.
 1.4 Novelty Ledger: claimed novelties and expected measurable benefits.
 1.5 Kill Criteria: conditions to STOP (e.g., baseline meets SLOs; novelty fails thresholds; quality floors violated; adoption infeasible).
 1.6 For non-ML: Formal Specs and oracles (reference impl/symbolic/metamorphic).
 1.7 ADR & Baseline Registry updates; ledger event append.
Gate C1.7 — WORTHINESS & COMPLEXITY (REVISED)
 PASS only if value is clear, novelty non-trivial, simpler alternatives inadequately meet SLOs, and non-solution baselines do not beat the proposed approach on risk-adjusted EV within 90% CI. Unresolved A-class assumptions without near-term tests → FAIL/REFRAME.

PHASE 2 — DESIGN SPACE WITH MINIMAL INTERVENTION TRACK (REVISED)
 Objective: propose candidate designs and include the simplest viable option.
Procedure:
 2.1 Enumerate ≥3 designs/variants with material tradeoffs.
 2.2 For each: hypotheses→measurable outcomes; ablations; risks; complexity; simplification prospects; causal edge under test.
 2.3 Minimal Intervention track: policy tweak, tiny script, checklist, wizard-of-oz manual process.
 2.4 Select Primary/Fallback and record rationale; include pivot trigger if Minimal ties/beats EV.
 2.5 Experiment plan: datasets/tests; bench configs; statistical tests; seed sweep; fairness slices; misuse probes; causal edge IDs to test; power analysis.
 2.6 PRT memo #2; ledger event append.
Gate C2 — PLAN INTEGRITY (REVISED)
 PASS only if plan is falsifiable, powered, ablation-ready, includes Minimal track, and cites causal edges per experiment. If Minimal beats/ties EV within CI → pivot.

PHASE 3 — PROTOTYPE BUILD AND REPRODUCIBILITY
 Objective: implement minimal correct prototypes and deterministic harnesses.
Procedure:
 3.1 Scaffold repository: code with lockfiles; Dockerfile; reproducible build notes; CI pipeline.
 3.2 Implement Primary/Fallback prototypes for correctness.
 3.3 Harnesses: seed management; benchmark runners; quality evaluators; synthetic generators with invariants.
 3.4 Environment fingerprint (OS, CPU/GPU, drivers).
 3.5 Checkpoint 3; ledger event append.
Gate C3 — MINIMAL VIABILITY
 PASS only if end-to-end runs succeed with pinned seeds, captured environment, and reliable harnesses.

PHASE 4 — ADVERSARIAL ROBUSTNESS
 Objective: expose brittleness early.
Procedure:
 4.1 Metamorphic tests: ≥3 transformations/domain (invariance or predictable change).
 4.2 Property-based tests: generate valid inputs; enforce invariants (bounds, conservation, idempotence where applicable).
 4.3 Fuzzing: random and structure-aware; track crashes/timeouts; enforce graceful handling.
 4.4 Misuse & negative inputs: attempt harmful outputs/behaviors; record mitigations.
 4.5 Fairness probes: subgroup slicing; fragile segment discovery; mitigation plan.
 4.6 Remediate high-severity failures; retest; ledger event append.
Gate C4 — ROBUSTNESS
 PASS only if high-severity issues mitigated and coverage adequate.

PHASE 5 — QUALITY PROXIES AND REALITY CHECKS
 Objective: validate quality vs floors before optimization.
Procedure:
 5.1 Compute primary/secondary quality on validation or justified synthetic sets.
 5.2 Cross-check with independent evaluators; sanity constraints.
 5.3 Differential testing vs baseline(s) on overlapping inputs; explain divergences.
 5.4 Estimate error bars; parameter sensitivity.
 5.5 Ledger event append.
Gate C5 — QUALITY SUFFICIENCY
 PASS only if quality floors are met/exceeded and deviations vs baseline justified.

PHASE 6 — BENCHMARKING WITH STATISTICAL RIGOR
 Objective: measure performance with variance control and tails.
Procedure:
 6.1 Suites: latency/throughput (typical & worst paths); memory peak/sustained; realtime jitter/dropout where applicable.
 6.2 Noise controls: CPU pinning/affinity; fixed threads; warmups; min bench time ≥5s; background isolation; HW/driver versions recorded.
 6.3 Replications & seed sweeps: risk-scaled N and seeds; capture across-seed variance.
 6.4 Statistics: geomean and 95% CI; Mann-Whitney U on medians (or justified alternative); p50/p95/p99; jitter for realtime.
 6.5 Stats Report & raw CSVs; ledger event append.
Gate C7 — BENCHMARK HYGIENE
 PASS only with replication counts, noise controls, tails, and HW pinning.
 Sub-Gate C7.Sigma — STATISTICAL SIGNIFICANCE
 PASS only if deltas significant at α≤0.05 or justified as practically significant with effect sizes and tight CIs.

GATE C6.9 — FIELD REALISM & ADOPTION FEASIBILITY (NEW; RUNS AFTER PHASE 6)
 Objective: ensure the solution can realistically be adopted, supported, and sustained.
Checklist (all required):
 • Adoption Plan: roles, incentives, behavior change, rollout plan, success criteria.
 • Serviceability: support model, MTTR targets, spares/data refresh policies.
 • Compliance Readiness: privacy/licensing/SPDX/sector regs mapped to artifacts.
 • Training & Materials: operator job-aids, user quick-starts, safety signage/scripts.
 • Total Cost of Ownership: ops headcount, training, audits, monitoring, deprecation.
 • Non-Goal Guardrails: explicit exclusions to avoid scope creep.
 PASS only if all green; otherwise REFRAME (e.g., Minimal Intervention) or STOP.

PHASE 7 — SCALE, COST/ENERGY, SECURITY & PROVENANCE
 Objective: prove operability at scale; quantify cost/energy; secure the supply chain.
Procedure:
 7.1 Scale/soak: 1×/2×/3× expected QPS; p50/p95/p99, error budgets, stability; confidence intervals.
 7.2 Cost/energy: cost_usd per op/1k ops; energy_j per op (metered or estimated with method & uncertainty); memory; price sensitivity ±20%.
 7.3 Security/provenance: SBOM; pinned deps; signatures/attestations; reproducible builds; provenance graph; SAST/DAST/secret scans; CVE report with exceptions dual-signed.
 7.4 Attack trees (R3): enumerate attacker goals/paths; verify mitigations mapped to tests and runbook procedures.
 7.5 Operations: runbook; SLO/SLA with alerts; rollback plan; incident templates; on-call & escalation.
 7.6 Ledger event append.
Gate C7.5 — SCALE/COST/SECURITY
 PASS only if targets met; SBOM/signatures/attestations, reproducible proof, scans/CVE policy pass; ops materials complete.

GATE 8.4 — SIMPLICITY (BEFORE PRODUCTIZATION)
 Objective: remove unjustified complexity and finalize minimal surface.
Procedure:
 8.4.1 Maintainability indices; cyclomatic/cognitive complexity.
 8.4.2 Dead-code and unused-dep scrub; minimize graph.
 8.4.3 Duplication index ≤5% (or ADR-justified).
 8.4.4 Public API audit: only intentional symbols.
 8.4.5 Reviewer note: confirm design-level simplification (not cosmetic).
 8.4.6 ADR; ledger event append.
Gate C8.4 — PASS if thresholds met and design simplification evidenced; else AMEND/FAIL.

GATE 8.5 — OPTIMIZATION (BEFORE PRODUCTIZATION)
 Objective: targeted optimization with statistical proof; no regressions.
Acceptance (domain-aware):
 • Realtime: latency p95 ≤ target; jitter bound; dropout/xrun within bounds; quality floors intact.
 • Batch/offline: throughput ≥ baseline×(1+X%); cost/energy ≤ baseline×(1−Y/Z%); zero quality regressions.
Procedure:
 8.5.1 Profile with appropriate tools (perf/VTune/Nsight/heap/IO/roofline).
 8.5.2 Apply targeted changes; document before/after.
 8.5.3 Re-benchmark via C7; regenerate Stats Report.
 8.5.4 Perf Pareto: update table/frontier; select point and record tradeoffs.
 8.5.5 Stop Card: if speedup <X% and complexity ↑, deprecate unless dual-signed value case.
 8.5.6 ADR; ledger event append.
Gate C8.5 — PASS only with statistically proven gains (or cost/energy wins), no correctness regressions, quality floors intact, Pareto selection recorded.

PHASE 8 — PRODUCTIZATION, COMPATIBILITY, SURFACE FREEZE
 Objective: expose stable, minimal interface with compatibility guarantees.
Procedure:
 8.1 Minimal API/CLI: exact signatures, I/O schemas, error codes, timeouts.
 8.2 Config system: typed parameters, defaults; reproducibility configs.
 8.3 Telemetry dictionary: structured logs/metrics with privacy annotations.
 8.4 Compatibility tests: exercise previous minor version contracts; block on regressions.
 8.5 Surface Freeze: lock public surface; post-freeze changes require semver bump and deprecation.
 8.6 Runbook updates; ledger event append.
Gate C8 — PASS if API/CLI/config/telemetry complete, surface frozen, compatibility tests pass.

PHASE 9 — RELEASE PACKAGING, SAFETY/PRIVACY, HUMAN FACTORS
 Objective: package for field testing and responsible distribution.
Procedure:
 9.1 Full Checkpoint built with manifests and artifacts.
 9.2 Safety/Privacy: Model & Data Cards; DPIA (if applicable); misuse memo; fairness deltas vs Phase 5; Assurance Case (GSN) for R3 linking hazards→controls→evidence.
 9.3 Integrity: SBOM; signatures/attestations; reproducible build proof.
 9.4 Evidence bundle: benchmarks CSVs/Stats Reports; profiles; Perf Pareto; ADRs; risk register extract; budget status.
 9.5 Human Factors: usability (≥3 think-aloud; SUS≥70 where UI exists); explainability (SHAP/IG and counterfactuals for decision support); operator training (≥2 runbook walkthroughs; ≥1 on-call drill).
 9.6 Field-Test Kit: deployment scripts/steps; configs for typical/high-load/failure-injection; simulators/generators; acceptance checklist; rollback plan; incident templates.
 9.7 Dashboard: self-contained artifact rendering CIs, tails, Pareto, fairness, drift timelines.
 9.8 Ledger event append.
Gate C9 — RELEASE READINESS
 BLOCK if: missing safety/privacy artifacts; fairness regression >0.5% unmitigated; integrity artifacts incomplete; benchmarks lack stats/tails; surface drift; missing runbook/field kit; failed usability threshold where human use applies.

PHASE 10 — CONTINUOUS EVALUATION, DRIFT, AUTO-ROLLBACK
 Objective: verify real-world performance/fairness/safety continuously and enforce automated rollback.
Procedure:
 10.1 Canary: ramp 5%→25%→100%; abort on SLO violations, fairness regression, anomaly z-score >3, or premortem indicators.
 10.2 Shadow Mode: mirror traffic ≥7 days; alert if p95 discrepancy >5% vs current production.
 10.3 Drift: data shift (PSI/KL), performance shift (CUSUM/ADWIN); run every 24h; record alerts.
 10.4 Auto-Rollback: trigger on two consecutive SLO breaches or security events; rollback within 10 minutes; notify; open incident.
 10.5 Evidence TTL: 90 days; re-verify on driver/compiler/critical-dep change; quick battery = smoke bench, fairness spot-check, security smoke.
 10.6 RCO monitors risk deltas; escalate R1→R2→R3 if incident severity rises.
 10.7 Ledger event append.
Gate C10 — CONTINUOUS ASSURANCE ACTIVATION
 PASS only if canary/shadow/drift/rollback configured, dry-run tested, alarms and ownership documented.

PRIVACY & DATA GOVERNANCE (WHEN PERSONAL/REGULATED DATA APPLIES)
 DPIA mandatory for R3 or whenever personal/sensitive data is used.
 Re-identification checks (where relevant): k-anonymity ≥10; l-diversity ≥2; t-closeness ≤0.2; document scope/limits.
 Retention/erasure: default 365 days; honor erasure on request; purpose limitation and consent trace (purpose, scope, expiry).
 Data-use audit logging and access controls documented in runbook.

UNCERTAINTY & CALIBRATION (FOR PROBABILISTIC OUTPUTS)
 Calibration: reliability diagrams; Expected Calibration Error (ECE).
 Prediction intervals: provide for decision-support outputs; document empirical coverage.
 Abstention policy: abstain when uncertainty > τ; fallback to human review; log rate and outcomes; analyze abstention bias.

SIM-TO-REAL & HIL (PHYSICAL/CYBER-PHYSICAL)
 Domain randomization across noise/latency/friction/lighting; documented coverage.
 Hardware-in-the-loop (R3): acceptance if |real−sim|/sim ≤5% on key metrics; investigate and remediate larger gaps.

SECURITY TESTING DEPTH
 SAST, DAST, secret scanning in CI; block on critical/high CVEs; dual-sign exceptions.
 Threat modeling with attack trees (R3); mitigations mapped to tests and runbook.
 Pen-test hooks and fuzz coverage summaries included in security_provenance.

LICENSE/IP COMPLIANCE
 SPDX license scan; blockers: non-commercial licenses in production; incompatible copyleft without compliance; attribution bundle included in release artifacts.

SURFACE FREEZE CHECKLIST
 API/CLI signatures recorded and versioned; public symbols audited; config schema locked; telemetry fields fixed; compatibility tests green; semver/deprecation documented; post-freeze changes require appropriate version bump.

FIELD-TEST KIT CONTENTS
 Deployment steps/scripts; parameterized configs; data generators/simulators; acceptance checklist aligned to SLOs and tails; failure-injection scripts; rollback & incident templates; contact/escalation paths; log/metric quick reference.

FAILURE RECOVERY
 On any gate FAIL: propose AUTO-FIX scripts where known; otherwise open HUMAN-REVIEW with owner, checklist, and a 3-day SLA to next action.
 Incident template must capture detection, impact, mitigation, root cause, corrective/preventive actions, and AMEND/ADR updates.

PROBLEM RED-TEAM PROMPT BANK (EXCERPTS)
 • “If this intervention succeeds perfectly, what harmful incentives or metric gaming could emerge?”
 • “What evidence would convince a skeptic that this problem does not exist or is trivial?”
 • “Which single assumption, if false, invalidates the entire approach? How can we test it fastest?”
 • “Who bears the risk if adoption fails? What non-tech option avoids that risk?”
 • “What legal, compliance, or contract clause could shut this down at deployment time?”

END-TO-END EXECUTION SCRIPT (FOLLOW EXACTLY)
Phase −1 → Gate C−0.5 (Problem Discovery & Worth-It). STOP/REFRAME or proceed.


Phase 0 → Gate C0 (Four-Fit, Assumption Ledger, falsification, budgets).


Phase 1 → Gate C1.7 (Baselines incl. Do-Nothing & Non-Tech; Novelty; Formal Specs if non-ML).


Phase 2 → Gate C2 (Design Space + Minimal Intervention; PRT #2; pivot if Minimal ties/beats EV).


Phase 3 → Gate C3 (Prototypes; Checkpoint 3).


Phase 4 → Gate C4 (Adversarial; mitigate and retest).


Phase 5 → Gate C5 (Quality floors).


Phase 6 → Gate C7 & C7.Sigma (Bench hygiene + stats significance).


Gate C6.9 (Field Realism & Adoption). Reframe or proceed.


Phase 7 → Gate C7.5 (Scale/Cost/Energy/Security/Runbook).


Gate C8.4 (Simplicity) → ADR and reviewer note.


Gate C8.5 (Optimization) → profiles, re-benchmarks, Pareto, ADR.


Phase 8 → Gate C8 (Productization, compatibility, surface freeze).


Phase 9 → Gate C9 (Safety/Privacy/Integrity/HF/Field-Kit/Dashboard).


Phase 10 → Gate C10 (Canary/Shadow/Drift/Rollback).


Operate CE loop; re-verify at evidence TTL or toolchain drift; escalate risk tier if warranted.


Throughout: RCO cycles produce MVDs, snapshot stats, Pareto updates; budgets enforced; AMEND/BRANCH rules and ADRs maintained; forecasts logged and later Brier-scored.



COMPLIANCE STATEMENT
 A run that completes all phases and passes all gates has:
 • Proved the problem is real, timely, and worth addressing versus Do-Nothing and Non-Tech alternatives.
 • Selected the smallest effective intervention when appropriate, or justified a more complex approach with EV and causal evidence.
 • Met quality floors and domain acceptance SLOs (including tails) with statistical significance.
 • Withstood problem red-team, metamorphic/property/fuzz/misuse testing; documented fairness deltas and mitigations.
 • Proven performance, cost, and energy with a declared Pareto tradeoff; demonstrated adoption feasibility, serviceability, compliance, training, and TCO.
 • Established scale readiness, supply-chain integrity (SBOM, signing, provenance), and security depth (SAST/DAST/secrets/CVEs/attack trees).
 • Frozen and versioned the public surface with compatibility tests and deprecation windows.
 • Produced a signed, reproducible checkpoint, human-factor evidence, a field-test kit, and a self-contained dashboard.
 • Activated continuous assurance (canary/shadow/drift/auto-rollback), enforced evidence TTL, and defined re-verification triggers.
 • Logged forecasts and later Brier-scored them to improve decision calibration over time.
This is GCP V47 — Worth-It Realism Edition. It is exhaustive by design and explicitly prevents “confidently wrong” solutions to problems that were never worth solving.

