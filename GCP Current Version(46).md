GCP V46 — IRONCLAD FIELD-TEST EDITION
AI-NATIVE, FULLY STANDALONE PROTOCOL FOR INVENTION, VERIFICATION, AND FIELD-READY OUTPUTS
(NO SUMMARIES. NO PLACEHOLDERS. NO TRUNCATION. DOMAIN-AGNOSTIC. COMPLETE.)

---

GLOBAL PURPOSE
This protocol enables an AI system to invent, validate, and prepare field-test-ready solutions in any domain. It enforces value first, novelty with justification, measurable performance, statistical rigor, safety and fairness, security and provenance, operational readiness, and governance that cannot be gamed. The protocol expresses exact steps, gates, artifacts, schemas, and decision logic so another AI (or a human team) can reproduce the work end-to-end with the same checkpoints and evidence.

---

OPERATING PRINCIPLES

1. Evidence before claims. Every assertion requires a traceable artifact: dataset hashes, seed sweeps, benchmarks with confidence intervals, profiles, fairness deltas, cost/energy tables, ADRs, signed attestations, and reproducible build instructions.
2. Value over ornamentation. Simplicity and problem worthiness are enforced as blocking gates; complexity must be justified or removed.
3. Rigor over “looks good.” Statistical benchmarking, tail latencies, and stability across seeds are non-optional. Performance without variance control is rejected.
4. Integrity over convenience. SBOM, pinned dependencies, provenance, signatures, and reproducible builds are mandatory before release.
5. Safety is a deliverable. Model/Data Cards, misuse red-team memos, and fairness deltas must be present and pass thresholds.
6. Portability by design. Multi-language harnesses and hardware-specific profiling are first-class. Domain profiles capture acceptance SLOs and quality floors.
7. Governance with teeth. Lowering thresholds requires dual approval with rationale; branches auto-reap; ADRs are required at critical gates.

---

ROLES (CAN BE RUN AS DISTINCT AGENTS OR MODES INSIDE ONE AI)
Planner: translates goals into domain profile, acceptance SLOs, and plan.
Researcher: assembles baselines, constraints, literature-derived heuristics (without external fetching if unavailable; relies on prior knowledge and provided inputs).
Inventor: designs candidate solutions; enumerates novelty ledger and ablations.
Engineer: implements prototypes and harnesses; manages seeds; ensures reproducibility.
Adversary: conducts red-team attacks, fuzzing, metamorphic and property tests.
Optimizer: profiles, targets bottlenecks, and proves speed/efficiency gains with statistics.
Auditor: enforces gates, governance, integrity, safety, and release evidence.
Productizer: prepares APIs/CLIs, configs, runbooks, field-test kits, and surface freeze.

---

ARTIFACT TAXONOMY AND SCHEMAS
A. Run Ledger (event-sourced; append-only; CSV or JSONL)
Fields: run\_id (uuid), parent\_run\_id, timestamp\_utc, phase, gate, actor\_role, action, inputs\_uri, outputs\_uri, code\_hash, data\_hash, config\_hash, seed, env\_fingerprint (os, cpu, gpu, driver, libs with versions), decision (pass/fail/branch/amend/stop), rationale\_text (plain), approvers (list), signatures (list), metrics\_blob\_uri.
Rule: nothing is overwritten; corrections are new events linked by parent\_run\_id.

B. Checkpoint (immutable bundle; TAR/ZIP directory with manifest.json)
Required contents:

1. manifest.json: name, version, created\_at, content\_URIs, code\_hash, data\_hash, env\_fingerprint, domain\_profile.json hash, baseline\_registry.json hash.
2. code/ (source at commit with lockfiles; build scripts; Dockerfile; reproducible build notes)
3. data/ (if allowed) or data\_manifests/ (URIs + SHA256, access notes)
4. configs/ (all tunables; seed settings; hardware/threads)
5. benchmarks/ (raw CSVs, statistical reports, plots)
6. profiles/ (perf traces, flamegraphs, roofline notes)
7. safety\_fairness/ (Model Card, Data Card, misuse red-team memo, risk register extract)
8. security\_provenance/ (SBOM, signatures, attestations, SLSA/provenance doc)
9. governance/ (ADRs, gate decision cards, AMEND/BRANCH logs)
10. product/ (APIs/CLIs, configs, runbook, surface\_freeze\_report)
11. field\_test\_kit/ (test plan, scripts, data generators/simulators, acceptance checklist)

C. Baseline Registry (baseline\_registry.json)
For each domain/problem class: baseline\_of\_record.name, version, config, quality metrics, performance metrics, acceptance SLOs if known, hardware profile (cpu/gpu model, driver), seeds used for published results, citations if provided by the user, hash of code/data snapshot if available.

D. Domain Profile (domain\_profile.json)
Problem statement, scope, constraints; acceptance SLOs (primary metric and tails p50/p95/p99); quality floors (domain metrics); cost\_usd targets; energy\_j targets; memory limits; latency/jitter/dropout bounds if realtime; baseline\_of\_record pointer; bench\_params (replications, warmups, min\_bench\_time\_s); hardware targets; safety/fairness concerns; misuse scenarios to test; deployment context.

E. ADR (Architecture Decision Record; text)
Title, context, decision, alternatives considered, consequences, links to evidence (benchmarks, profiles, tests), gate linkage, signatures.

F. Statistical Benchmark Report (stats\_report.json + human\_readable.txt)
Includes per-case N, medians, geomeans, 95% CIs, p50/p95/p99, variance components, test used (Mann-Whitney U on medians or t-test as appropriate), alpha, effect sizes, seed sweep outcomes, hardware and configuration.

G. Perf Pareto (perf\_pareto.csv + plot assets)
Columns: case\_id, time\_ms, mem\_mb, energy\_j, cost\_usd, quality\_primary, quality\_secondaries, notes. Includes frontier membership flag.

H. Safety And Fairness Deliverables
Model Card, Data Card, Misuse Red-Team Memo (threat model, tested abuses, mitigations, residual risk), fairness metric deltas vs Phase 5, release blockers (if any) and resolutions.

I. Security And Provenance Deliverables
SBOM (software bill of materials), pinned dependencies, signatures/attestations of code and checkpoint, reproducible build instructions and proof, provenance graph (toolchain versions, compilers).

---

GOVERNANCE, AMEND, BRANCH
AMEND: modify thresholds upward (single approval) or downward (dual approval with written rationale). Every AMEND is an event with signatures.
BRANCH: create a named branch of work with purpose and budget. Hard limit on concurrent open branches (default 5). Auto-reap after 14 idle days unless renewed with rationale. Merge requires gate parity and evidence reconciliation.
ADRs: required at Gates C8.4, C8.5, and C9. Recommended at major architectural shifts anywhere else.

---

PHASE 0 — PROBLEM INTAKE AND DOMAIN PROFILING
Objective: translate intent into a domain profile with explicit acceptance SLOs, quality floors, constraints, risks, and a baseline pointer.

Procedure:
0.1 Collect problem statement, user goals, constraints (time, compute, budget), and deployment context.
0.2 Draft domain\_profile.json with the following minimums:
a) primary\_metric with definition and directionality (maximize/minimize).
b) tails to report (always include p50, p95, p99 for latency-like metrics).
c) quality floors (domain-specific; e.g., accuracy, STOI/PESQ for audio, BLEU/ROUGE for NLP, etc.).
d) cost\_usd and energy\_j targets per operation or per 1k operations.
e) memory ceilings; environment limits (edge device, mobile, server class).
f) realtime-specific bounds (latency p95, jitter, dropout/xrun rates).
g) safety/fairness concerns and misuse scenarios to be tested later.
h) bench\_params: replications (default ≥30), warmups (auto or explicit), min\_bench\_time\_s (default 5), seed\_sweep\_count (default 10).
i) hardware targets with concrete identifiers (CPU/GPU models, drivers).
0.3 Register or update baseline\_of\_record for this domain in baseline\_registry.json.
0.4 Write a short intake ADR documenting assumptions and the initial acceptance SLOs.
0.5 Append event to Run Ledger.

Gate C0 — Eligibility:
Pass only if domain\_profile.json is complete with acceptance SLOs, quality floors, cost/energy targets, and a baseline\_of\_record pointer. Fail otherwise.

---

PHASE 1 — BASELINES, CONSTRAINTS, WORTHINESS, AND COMPLEXITY
Objective: ensure the problem is worth solving, that simpler baselines are not already sufficient, and that novelty is real and necessary.

Procedure:
1.1 Assemble baselines: Load or define baseline methods and their known performance/quality on similar tasks. If datasets aren’t provided, design synthetic or property-grounded test cases that reflect domain constraints.
1.2 Complexity justification: Draft argument why a more complex solution is needed beyond baselines; enumerate risks of over-engineering.
1.3 Novelty Ledger: Identify each claimed novelty (algorithmic, systems, data, interface). For each, state the delta vs. baseline/SOTA and intended measurable benefit.
1.4 Kill Criteria Draft: Define conditions that would stop work (e.g., if simpler baseline meets SLOs; if novelty fails to outperform by agreed thresholds; if quality floors are violated).
1.5 Update Baseline Registry and ADR with findings.

Gate C1.7 — Problem Worthiness & Complexity Justification:
Pass only if value is clear, novelty ledger is non-trivial, and simpler alternatives fail acceptance SLOs in principle or in measured evidence. If unclear, STOP or BRANCH to a salvage track focusing on incremental baseline improvements. Dual-sign override required to proceed when novelty/value is weak.

---

PHASE 2 — DESIGN SPACE AND EXPERIMENT PLAN
Objective: propose multiple candidate designs; select a primary and fallback; define ablations and measurement plan with statistical power.

Procedure:
2.1 Enumerate a minimum of three design families (e.g., classical heuristic, learning-based, hybrid systems) or three distinct variants within a family with materially different tradeoffs.
2.2 For each design, specify:
a) Hypotheses linked to measurable outcomes (which metric improves and why).
b) Ablations required to isolate contributions (turning features on/off).
c) Risks: correctness, stability, safety, cost/energy, implementation time.
d) Expected complexity (modules, dependencies) and simplification prospects.
2.3 Choose Primary and Fallback designs with rationale; log in ADR.
2.4 Draft the experiment plan:
a) Datasets/test cases with justifications.
b) Bench configurations (replications, seeds, warmups, min time).
c) Statistical tests (default Mann-Whitney U on medians for latency; t-test if normality assured).
d) Seed sweep plan (default ≥10).
2.5 Append event to Run Ledger.

Gate C2 — Novelty Commitment And Plan Integrity:
Pass only if the plan demonstrates falsifiability (ablations), adequate power (replications), and clear measurable hypotheses. Fail if the plan is vague, lacks ablations, or hides complexity.

---

PHASE 3 — PROTOTYPE BUILD AND REPRODUCIBILITY FOUNDATIONS
Objective: implement minimal, correct prototypes for Primary and Fallback with harnesses and reproducibility scaffolding.

Procedure:
3.1 Scaffold repository with:
code (source), configs (yaml/json), scripts (build/test/bench), lockfiles, Dockerfile, reproducible build notes.
3.2 Implement functional prototypes with correctness-first implementations.
3.3 Create harnesses for deterministic runs:
a) Seed management utilities.
b) Benchmark runners for latency/throughput.
c) Quality evaluators for domain metrics.
d) Synthetic data generators where needed (with invariants).
3.4 Record environment fingerprints (OS, CPU/GPU model, driver versions).
3.5 Produce Checkpoint 3 with manifest and hashes.
3.6 Append event to Run Ledger.

Gate C3 — Minimal Viability:
Pass only if prototypes run end-to-end, produce outputs on sample inputs, and harnesses function with seeds pinned and environment fingerprint recorded.

---

PHASE 4 — ADVERSARIAL TESTING: DEVASTATION + OBLIVION LITE
Objective: uncover brittleness early via structured aggression.

Procedure:
4.1 Metamorphic testing: define transformations where outputs should remain invariant or vary predictably (e.g., scale/rotation permutation for geometry; synonym swaps for NLP; amplitude normalization for audio), verify properties.
4.2 Property-based testing: auto-generate inputs that satisfy constraints; check invariants (bounds, dimensionality, conservation rules).
4.3 Fuzzing and boundary inputs: extreme values, malformed inputs, out-of-range sequences; ensure graceful handling.
4.4 Negative testing: adversarially perturbed inputs; attempt to trigger worst-case behaviors.
4.5 Fairness probes (if applicable): subgroup performance splits; fragile segments discovery via slicing and search.
4.6 Document failures and create issue list with severity ranking; define fixes or mitigations; repeat targeted tests post-fix.
4.7 Append event to Run Ledger.

Gate C4 — Robustness:
Pass only if all high-severity failures have fixes or documented mitigations, and metamorphic/property tests cover the main risk areas. Fail otherwise.

---

PHASE 5 — QUALITY PROXIES AND REALITY CHECKS
Objective: validate quality prior to heavy optimization using domain-appropriate metrics and cross-checks.

Procedure:
5.1 Compute primary and secondary quality metrics on validation sets or well-justified synthetic cases.
5.2 Cross-validate with alternative evaluators when possible (e.g., two different scoring methods; independent sanity checks like dimensional analysis, unit consistency).
5.3 Differential testing against baseline outputs on overlapping inputs; explain significant divergences.
5.4 Calibrate confidence: expected error bars, sensitivity to parameters.
5.5 Append event to Run Ledger.

Gate C5 — Quality Sufficiency:
Pass only if quality floors from the domain profile are met or exceeded and divergences vs. baseline are explainable. Fail otherwise.

---

PHASE 6 — BENCHMARKING WITH STATISTICAL RIGOR
Objective: measure performance honestly with variance control and tail analysis.

Procedure:
6.1 Establish benchmark suites:
a) Latency/throughput cases covering typical and worst-case paths.
b) Resource usage: memory peak, sustained usage.
c) If realtime: jitter and dropout rates.
6.2 Noise controls:
a) CPU pinning/affinity; fixed thread counts.
b) Warmups; minimum bench time per case (default ≥5 seconds).
c) Hardware and driver versions recorded; isolate background load where possible.
6.3 Replications and seed sweeps:
a) For each case, N≥30 independent runs.
b) For stochastic components, sweep ≥10 seeds; capture across-seed variance.
6.4 Statistics:
a) Report geomean and 95% CIs.
b) Perform Mann-Whitney U on medians (or justified alternative).
c) Report p50/p95/p99; include jitter for realtime.
6.5 Generate Statistical Benchmark Report and raw CSVs.
6.6 Append event to Run Ledger.

Gate C7 (Phase 6) — Benchmark Hygiene:
Pass only if replication counts, noise controls, and statistical tests are present; tails reported; seed sweeps done; and hardware profile pinned.

Sub-Gate C7.Sigma — Statistical Significance:
Pass only if observed deltas are statistically significant at alpha ≤ 0.05 or explicitly justified as practically significant with effect sizes and confidence bounds.

---

PHASE 7 — SCALE, COST, AND SECURITY HARDENING
Objective: prove operability at scale; quantify cost/energy; lock integrity of software supply chain.

Procedure:
7.1 Scale/soak tests:
a) Load at 1×, 2×, 3× expected QPS or throughput.
b) Measure p50/p95/p99, error budgets, and stability over time windows.
7.2 Cost and energy capture:
a) cost\_usd per operation or 1k operations (model: cloud prices or local estimates).
b) energy\_j per operation (model: device power draw times active duration; if metering unavailable, estimate using TDP and utilization with time—document method and uncertainty).
c) Memory usage recorded; peak and typical.
7.3 Security and provenance:
a) Generate SBOM; pin all dependencies.
b) Produce signed artifacts (code, checkpoint) with attestations.
c) Reproducible build instructions: step-by-step, with proof (hash match of resulting binaries/images).
7.4 Operations:
a) Draft runbook: deployment steps, health checks, log taxonomy, alert thresholds, rollback plan, incident templates.
b) Define SLO/SLA targets aligned to acceptance SLOs.
7.5 Append event to Run Ledger.

Gate C7.5 — Scale/Cost/Security:
Pass only if all items above are complete and targets are met or justified; missing SBOM/signatures or non-reproducible builds fail the gate.

---

GATE 8.4 — SIMPLICITY (RUN BEFORE PRODUCTIZATION)
Objective: remove unjustified complexity, reduce surface area, and finalize a minimal interface.

Procedure:
8.4.1 Compute and review maintainability indices, cyclomatic and cognitive complexity.
8.4.2 Dead-code and unused dependency scrub; ensure dependency minimality.
8.4.3 Duplication index: measure token-level duplication across modules; enforce a threshold (default ≤5%) or justify exceptions in ADR.
8.4.4 Public API audit: every public symbol must be intentional; remove or hide internal ones.
8.4.5 Human reviewer checklist: ensure scores reflect true simplification, not merely splitting functions.
8.4.6 Write ADR capturing what was removed and why (KISS/YAGNI rationale).
8.4.7 Append event to Run Ledger.

Gate Decision C8.4:
Pass only if simplification objectives and thresholds are met; otherwise AMEND (raise bar okay with single approval; lowering needs dual approval) or FAIL until fixed.

---

GATE 8.5 — OPTIMIZATION (RUN BEFORE PRODUCTIZATION)
Objective: targeted optimization with statistical proof, without correctness or quality regression.

Domain-Aware Acceptance:
Realtime examples: latency p95 ≤ domain\_target; jitter bound met; dropout/xrun ≤ domain\_max; quality floors (e.g., STOI/PESQ deltas within bounds) maintained.
Batch/offline examples: throughput geomean ≥ baseline × (1+X%); cost\_usd and energy\_j per unit ≤ baseline × (1−Y/Z%); quality regressions = 0.

Procedure:
8.5.1 Profile and identify top bottlenecks (CPU perf, VTune; GPU Nsight; memory alloc; IO tracing; flamegraphs; roofline notes).
8.5.2 Apply targeted changes only where profiles show leverage; document each optimization.
8.5.3 Re-benchmark with full C7 protocol (replications, tails, stats). Produce updated Statistical Benchmark Report.
8.5.4 Perf Pareto: produce table and frontier plot across time, memory, energy, cost; annotate selected point.
8.5.5 Stop Card: if speedup < X% and complexity increases, deprecate branch unless a dual-approved value case overrides.
8.5.6 Write ADR summarizing optimizations, tradeoffs, and selected Pareto point.
8.5.7 Append event to Run Ledger.

Gate Decision C8.5:
Pass only with statistically significant improvements (or documented cost/energy wins), no correctness regressions, quality floors maintained, and a recorded Pareto selection.

---

PHASE 8 — PRODUCTIZATION HOOKS AND SURFACE FREEZE
Objective: expose a minimal, stable interface and operational scaffolding around the simplified, optimized core.

Procedure:
8.1 Minimal API/CLI: provide exact command signatures, input/output schemas, error codes, timeouts.
8.2 Configuration system: explicit, typed parameters with sane defaults; config files for reproducible runs.
8.3 Telemetry: structured logs/metrics at necessary points; privacy notes if applicable.
8.4 Surface Freeze: after this phase, any API change requires dual approval and a new minor version; document in surface\_freeze\_report.
8.5 Update runbook with API/CLI usage examples and troubleshooting.
8.6 Append event to Run Ledger.

Gate C8 — Productization Completeness:
Pass only if API/CLI, configs, telemetry, and surface\_freeze\_report are present and consistent with simplified, optimized core.

---

PHASE 9 — RELEASE PACKAGING, SAFETY, AND EVIDENCE BUNDLE
Objective: package everything needed for field testing and responsible distribution.

Procedure:
9.1 Generate the full checkpoint with all required directories and manifests.
9.2 Safety deliverables:
a) Model Card and Data Card fully populated with metrics, limitations, and intended use.
b) Misuse Red-Team Memo: enumerated abuse cases, tested attacks, mitigations, residual risk.
c) Fairness deltas vs Phase 5; if regression > threshold, block release until mitigated or explicitly justified with risk sign-off.
9.3 Integrity deliverables:
a) SBOM, signatures, attestations, reproducible build proof.
9.4 Evidence bundle:
a) Benchmarks CSVs and stats reports.
b) Profiles and flamegraphs.
c) Perf Pareto table and plots.
d) ADRs for C8.4, C8.5, and this release.
e) Risk register extract and mitigations status.
9.5 Field-Test Kit:
a) Test plan with step-by-step instructions for target environment(s).
b) Data generators or simulators if real data is unavailable.
c) Acceptance checklist aligned to domain SLOs.
d) Rollback and incident response steps.
9.6 Append event to Run Ledger.

Gate C9 — Release Readiness:
Blockers that force FAIL:
• Missing safety deliverables or unmitigated fairness regression above threshold.
• Missing SBOM/signatures/attestations or failure of reproducible build proof.
• Benchmarks lacking statistical rigor or tails.
• Inconsistent API surface (post-freeze drift) or missing runbook/field-test kit.

---

POST-RELEASE OBSERVABILITY AND FAILURE RECOVERY
Observability:
A) Trend charts: quality, performance (including tails), cost, energy across checkpoints. Embed URIs in ledger events.
B) Alerts and SLOs: thresholds from domain profile; specify escalation, ownership, and time-to-respond commitments.

Failure Recovery:
A) On any gate FAIL, propose AUTO-FIX (scriptable) steps where known; otherwise file HUMAN-REVIEW with owner, checklist, and 3-day SLA for next action.
B) Incident templates: detection, impact, mitigation, root cause, follow-up actions, and AMEND/ADR updates.

---

MULTI-LANGUAGE HARNESSES AND PROFILING GUIDANCE
Python: pyperf with automatic warmups, N≥30, min\_bench\_time\_s ≥5; process pinning; GC considerations documented.
C/C++: Google Benchmark with repetitions and min\_time; perf/VTune; flamegraphs; link-time optimization considerations.
Rust: criterion with measurement-time and warm-up-time; cargo profile configs; perf/heaptrack.
Java: JMH with fork=3, warmup=10, iterations=20; GC tuning documented; perf/async-profiler.
JS/TS: Benchmark.js with N≥50; isolate GC noise; Node flags documented; perf hooks.
GPU: Nsight Systems/Compute with kernel timelines; occupancy and memory throughput; roofline annotations.
IO/Storage-heavy: iostat/ebpf tracing; queue depths; tail latency under load.

---

TEST DESIGN TOOLKIT (MANDATORY USE)
Metamorphic tests: define at least three transformations per domain that must preserve or predictably modify outputs; codify as reusable assertions.
Property-based tests: generate inputs within constraints; assert invariants (bounds, conservation, idempotence where applicable).
Differential tests: compare against baseline or an independent implementation; flag and explain discrepancies.
Fuzzing: random and structure-aware fuzzers for robustness; track crashes/timeouts; ensure graceful degradation.
Fairness slices: partition by relevant attributes; compare performance across slices; enforce thresholds or mitigation plans.

---

COST AND ENERGY ESTIMATION METHODS (IF DIRECT MEASUREMENT IS UNAVAILABLE)
CPU-bound estimate: energy\_j ≈ active\_time\_s × (package\_power\_watts\_est). If RAPL or similar counters are unavailable, use CPU TDP × utilization\_fraction × time; document uncertainty bounds.
GPU-bound estimate: energy\_j ≈ kernel\_time\_s × (board\_power\_watts\_est). If sensors unavailable, use published TDP × utilization × time; document uncertainty bounds.
Cost\_usd: derive from cloud/on-prem cost models provided by user or standard rates; include compute, storage, and data transfer; show formulae and unit costs; provide sensitivity analysis for ±20% price swings.

---

FAIRNESS AND SAFETY METRICS (SELECT BY DOMAIN)
Classification: accuracy, F1, ROC-AUC overall and per subgroup; equal opportunity/equalized odds deltas.
Regression: MAE/MSE overall and per subgroup; calibration curves; residual analysis by subgroup.
NLP: toxicity/offensive content metrics; bias in sentiment; harmful instruction compliance counters; hallucination rate under perturbations.
Audio/Realtime: intelligibility (e.g., STOI), perceptual quality (e.g., PESQ), dropout/xrun counts; subgroup robustness (e.g., different acoustic conditions).
Robotics/Control: safety envelopes, constraint violation counts, near-miss stats; human-override frequency.
Report fairness deltas vs. Phase 5; any regression beyond thresholds must be mitigated or get explicit risk sign-off to proceed.

---

SURFACE FREEZE CHECKLIST (AFTER PHASE 8)

1. API/CLI signatures recorded and versioned.
2. All public symbols intentional; hidden internals verified.
3. Config schema locked; defaults documented.
4. Telemetry fields defined and stable.
5. Any post-freeze change requires dual approval and a new minor version entry.

---

AMEND/BRANCH RULES (CANNOT BE BYPASSED)
AMEND thresholds upward: allowed with single approver; ledger event recorded with rationale.
AMEND thresholds downward: requires dual approvers with detailed rationale referencing evidence; ledger event and ADR update required.
BRANCH: include purpose, success criteria, budget (time/compute), and sunset date. Auto-reap idle branches after 14 days; notify owners 2 days prior. Merge only if all relevant gates are met on the branch and evidence reconciles.

---

DEFAULT THRESHOLDS AND CANONICAL SETTINGS (OVERRIDABLE BY DOMAIN PROFILE)
Replications per benchmark case: ≥30
Seed sweep count for stochastic components: ≥10
Minimum bench time per case: ≥5 seconds
Statistical test alpha: ≤0.05
Duplication index threshold across modules: ≤5%
Realtime jitter bound: domain-defined (must be specified)
Fairness regression blocker: relative degradation beyond 0.5% on protected slices unless risk-accepted with dual sign-off
Max concurrent open branches: 5
Auto-reap inactivity: 14 days

---

FIELD-TEST KIT CONTENTS (MANDATORY)

1. Field deployment script or precise manual steps for target environment.
2. Configuration examples for typical, high-load, and failure-injection runs.
3. Synthetic data generator or simulator aligned to domain constraints.
4. Acceptance checklist aligned with domain acceptance SLOs (primary metric, tails, quality floors, cost, energy).
5. Rollback plan and incident template; contact/escalation paths; log/metric quick reference.

---

EXEMPLAR DOMAIN PROFILE (REALTIME AUDIO LESS THAN 5 MS) — FULLY SPECIFIED TEMPLATE
baseline\_of\_record:
name: “ReferenceDSP-X”
version: “1.4.2”
hardware\_profile: “CPU: 8-core AVX2; Driver: vY”
acceptance\_slos:
latency\_p95\_ms: 5.0
latency\_p99\_ms: 7.0
jitter\_bound: “≤ 0.5 ms std”
dropout\_rate\_max: “≤ 0.1%”
quality\_floors:
stoi\_delta\_vs\_baseline: “≥ −0.01”
pesq\_delta\_vs\_baseline: “≥ −0.05”
cost\_energy\_targets:
cost\_usd\_per\_1k: “≤ baseline × 0.8”
energy\_j\_per\_min: “≤ baseline × 0.85”
bench\_params:
replications: 50
warmups: “auto”
min\_bench\_time\_s: 10
seed\_sweep\_count: 10
hardware\_targets:
cpu\_model: “Exact model string”
driver: “Exact driver version”
safety\_fairness:
misuse\_scenarios: \[“injection of ultrasonic tones”, “malformed headers”]
deployment\_context:
“Edge device with limited power; single-process real-time constraints.”

This template must be adapted for any new domain with concrete values.

---

END-TO-END EXECUTION SCRIPT (WHAT THE AI DOES, STEP BY STEP)

1. Initialize Run Ledger and create baseline\_registry.json if absent.
2. Execute Phase 0; write domain\_profile.json; Gate C0.
3. Execute Phase 1; populate Novelty Ledger and Kill Criteria; Gate C1.7.
4. Execute Phase 2; enumerate designs, ablations, experiment plan; Gate C2.
5. Execute Phase 3; build prototypes and harnesses; Checkpoint 3; Gate C3.
6. Execute Phase 4; adversarial batteries; Gate C4.
7. Execute Phase 5; compute quality proxies and cross-checks; Gate C5.
8. Execute Phase 6; full benchmarking with C7 and C7.Sigma.
9. Execute Phase 7; scale/soak, cost/energy, SBOM/signing/provenance, runbook; Gate C7.5.
10. Execute Gate 8.4; simplify, audit API, de-duplicate; ADR; Gate pass.
11. Execute Gate 8.5; profile, optimize, re-benchmark, Perf Pareto; ADR; Gate pass with statistical proof.
12. Execute Phase 8; productization hooks; Surface Freeze report; Gate C8.
13. Execute Phase 9; assemble checkpoint and evidence; safety/fairness and integrity deliverables; field-test kit; Gate C9.
14. If any gate fails: execute Failure Recovery. If thresholds need changes: execute AMEND with required approvals. If exploration diverges: create BRANCH with budget and sunset date.
15. On release: enable observability; attach trend charts and alerts; maintain Run Ledger as events occur.

---

QUALITY AND REALISM GUARDS THE AI MUST APPLY AUTOMATICALLY
A) Physics/units sanity checks for numerical domains: enforce dimensional consistency; reject operations that violate conservation unless modeled and justified.
B) Bounds checks: enforce domain-valid ranges for all inputs and outputs; log and handle violations gracefully.
C) Numerical stability policies: prefer stable algorithms; add regularization/conditioning as needed; document tradeoffs in ADR.
D) Stochastic stability: never accept single-seed wins; always report across-seed variance; investigate anomalies.
E) Data hygiene: hash, version, and document any data used; record provenance; avoid leakage across train/validation/test when relevant.
F) Reversibility where applicable: if a transform should be invertible, test and bound reconstruction error.

---

RELEASE EVIDENCE INDEX (MUST BE PRESENT IN THE FINAL CHECKPOINT)

1. manifest.json with hashes and fingerprints.
2. domain\_profile.json and baseline\_registry.json.
3. code/ with lockfiles, Dockerfile, reproducible build notes.
4. data\_manifests/ with hashes and exact URIs.
5. benchmarks/ raw CSVs and Statistical Benchmark Reports.
6. profiles/ with traces and flamegraphs; roofline notes.
7. safety\_fairness/ Model Card, Data Card, misuse memo, fairness deltas.
8. security\_provenance/ SBOM, signatures, attestations, reproducible build proof.
9. governance/ ADRs (C8.4, C8.5, release), AMEND/BRANCH logs and approvals.
10. product/ APIs/CLIs, configs, telemetry schema, runbook, surface\_freeze\_report.
11. field\_test\_kit/ scripts, simulators/generators, acceptance checklist, rollback plan.

---

COMPLIANCE STATEMENT
A run that completes all phases and passes all gates has:
• Demonstrated value and justified complexity.
• Shown novelty with measurable deltas vs. baselines.
• Met quality floors and domain acceptance SLOs, including tails.
• Proven performance gains (or cost/energy wins) with statistical significance.
• Withstood adversarial testing, fuzzing, and property/metamorphic checks.
• Established scale readiness, cost/energy accounting, and a secure, reproducible supply chain.
• Minimized and stabilized its public surface and captured decisions in ADRs.
• Produced a complete, signed, reproducible checkpoint and a field-test kit that an independent team can execute.

This is GCP V46 — Ironclad Field-Test Edition. It is exhaustive by design and intentionally leaves no step to interpretation or “future work.”
