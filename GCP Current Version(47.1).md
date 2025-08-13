Genesis Code Protocol (GCP) V47.1 — Worth-It Realism Edition (Revised)
AI-Native, Fully Standalone Protocol for Problem Selection, Invention, Verification, Release, and Continuous Operation
 (No summaries. No placeholders. No truncation. Domain-agnostic. Complete.)
Global Purpose
This protocol compels an AI system to (1) determine whether a problem is real and worth solving before building anything, (2) select the smallest effective intervention when appropriate, and (3) deliver complete, realistic, field-ready solutions with continuous assurance. It encodes distinct roles, artifacts, phases, gates, thresholds, risk-tier scaling, causal validity, expected-value economics, safety/privacy/security formalism, supply-chain integrity, human-factor evidence, versioning governance, and post-release monitoring with automated rollback. All claims require linked evidence; all decisions are recorded; all outputs are reproducible.
Operating Principles
Problem truth before solution: Prove the problem exists, matters, and is tractable. Include Do-Nothing and Non-Tech alternatives; pivot to the smallest effective intervention if they win.


Evidence before claims: Every assertion must be traceable to artifacts (datasets/generators, seeds, benchmark CSVs, CIs, fairness deltas, profiles, ADRs, signed attestations, reproducible builds, forecasts with Brier scoring).


Rigor over appearance: Use statistical benchmarking with variance analysis (tail metrics and seed sweeps). Significance and effect sizes determine pass/fail; forecasts are calibrated and Brier-scored.


Integrity over convenience: Enforce supply-chain integrity. SBOM, pinned dependencies, signing/attestation, provenance tracking, CVE policy, and reproducible builds are mandatory prior to release.


Safety, privacy, fairness, and legality as deliverables: Include formal hazard analyses (e.g. FMEA, STPA), assurance cases (GSN), Data Protection Impact Assessment (DPIA), misuse testing, fairness metrics, and sector-specific compliance evidence meeting defined thresholds.


Realism & adoption: Outputs must be usable, serviceable, operable, and affordable in the real world. Total cost of ownership (TCO), training needs, compatibility, and support plans are required evidence.


Governance with teeth: Thresholds cannot be lowered without dual approval and documented rationale; branches cannot sprawl uncontrolled; public interfaces are frozen and versioned with compatibility tests.


Continuous assurance: Canary releases, shadow testing, drift detection, evidence time-to-live, and automated rollback operate by default. Re-verification is triggered on toolchain or dependency drift.


Roles (Run as Distinct Agents or Modes)
Planner — Produces the Domain Profile, budgets, Four-Fit assessment, and project plan.


Researcher — Assembles baselines, constraints, supporting evidence, causal sketch, and Non-Tech alternatives.


Inventor — Proposes candidate solution designs and a Minimal Intervention option; maintains the Novelty Ledger and plans ablation tests.


Engineer — Implements prototypes and harnesses; manages reproducibility (seed control, environment capture).


Adversary — Conducts adversarial testing: property-based checks, metamorphic tests, fuzzing, security audits, and problem red-teaming.


Optimizer — Profiles and targets performance bottlenecks; proves speed/cost/energy improvements statistically.


Auditor — Enforces gates, governance rules, integrity, safety/privacy/security compliance; approves threshold changes.


Productizer — Prepares minimal APIs/CLIs/configs/telemetry; freezes public interfaces; produces support runbooks.


Operator — Runs canary and shadow deployments, monitors drift, manages rollback automation, and incident response.


Realism-Compiler Orchestrator (RCO)
Purpose: Enforce disciplined, cyclic progress through phases with automatic gate checks, budget enforcement, and stop rules. The RCO orchestrates role-specific actions in a loop until completion or a stop condition.
Scheduler: The RCO runs a role-aware, gate-blocking cycle. Each cycle (e.g. 10–20 minutes) produces: a Minimum Viable Demonstration (MVD) on the smallest non-trivial test case; an updated statistics snapshot; and a Pareto frontier update for performance vs. quality.
Auto-Actions:
stop_card_on_fail — On gate failure within budget, automatically issue a Gate Card with failure context and either stop the run or branch (see Failure Recovery).


amend_request_on_threshold_pressure — If thresholds block progress but evidence supports a change, trigger an AMEND (increase/decrease threshold) request; lowering requires dual sign-off.


branch_on_divergent_approach — If a fundamentally different approach is suggested, fork a branch with its own budget and sunset date.


risk_reassignment — If hazard or impact increases (e.g. discovering higher risk), escalate the risk tier R1→R2→R3 accordingly.


premortem_indicators_to_canaries — Auto-wire top failure modes (from premortem analysis) into canary alerts in Phase 10.


Deterministic IDs: Each run is tagged with a RunID (e.g. an ISO8601 timestamp or hash) used in logs and file outputs. Each gate evaluation is assigned a GateID combining the gate name and timestamp (e.g. C0_20250813T134500Z for Gate C0 decided at that time). These IDs ensure traceability of decisions and artifacts across the run.
Risk-Tiered Execution Lanes
Tiers: R1 (low risk), R2 (moderate risk), R3 (high risk / regulated / safety-critical). The risk tier is assigned during problem definition (Phase −1/0) based on user impact, regulatory scope, safety hazards, privacy sensitivity, and operational blast radius.
Risk-Scaled Overrides: Each higher risk tier imposes stricter requirements (additive to default thresholds):
R1: Benchmark replications ≥15; stochastic seed sweep ≥5. Signing/attestation steps may be skipped in Gate C7.5 only if code is not distributed and environment is ephemeral; all other integrity steps remain mandatory.


R2: Benchmark replications ≥30; seed sweep ≥10. Full supply-chain integrity (SBOM, signing, etc.) is required; no skips.


R3: Benchmark replications ≥50; seed sweep ≥20. Additionally require formal hazard analysis (FMEA, STPA), Assurance Case (GSN), DPIA, threat modeling (attack trees), activation of canary/shadow monitoring and auto-rollback, and hardware-in-the-loop testing if physical components are involved.


Governance: Amend, Branch, and Versioning
AMEND: Raising any acceptance threshold requires at least one approver; lowering a threshold requires two independent approvers with written rationale tied to evidence. All threshold changes are recorded as ledger events and update an ADR (Architecture Decision Record).


BRANCH: Each branch (forked approach) must have a clear purpose, success criteria, explicit compute/financial/CO₂e budgets, and a sunset date. At most 5 branches can run concurrently. Branches auto-terminate after 14 days of inactivity (with a 2-day warning). Merging a branch back requires all relevant gates to be passed and evidence reconciled.


Versioning: Use semantic versioning for releases. Any breaking change to a public interface requires a major version bump, with compatibility tests and at least a 90-day deprecation window for the old version.


Compatibility: Phase 8 includes compatibility testing against the previous minor version; any backward-incompatibility blocks merging/release.


Artifact Taxonomy and Schemas
(Key artifacts produced during the run, with standardized formats and content requirements.)
A) Run Ledger – An append-only event log (CSV or JSON Lines) recording every significant action and decision. Fields: run_id, parent_run_id, timestamp_utc, phase, gate, actor_role, action, inputs_uri, outputs_uri, code_hash, data_hash, config_hash, seed, env_fingerprint (OS, hardware, driver versions), decision (pass/fail/branch/amend/stop), rationale_text, approvers, signatures, metrics_blob_uri, causal_edge_ids_tested (list of experiment IDs), forecast_set_id (if any).


B) Checkpoint – An immutable bundle (TAR/ZIP archive) capturing a snapshot of the solution at a gate (notably after Phase 3 prototype and at final release). Contents:


manifest.json (name, version, creation timestamp, content URIs, hashes, environment fingerprint, references to domain_profile and baseline_registry).


code/ – Source code at the corresponding commit (with lockfiles), Dockerfile, and reproducible build notes.


data/ (or data_manifests/) – Data files or data manifest listing external data URIs with their checksums.


configs/ – Configuration files, including tunable parameters, random seeds, and hardware/runtime settings used.


benchmarks/ – Raw benchmark result CSVs, statistical summary reports (JSON and human-readable text), and any performance plots.


profiles/ – Performance profiles and traces (e.g. CPU/GPU utilization logs, flamegraphs, roofline analyses).


safety_privacy/ – Safety, privacy, and fairness documentation: Model Card, Data Card, DPIA report (if applicable), misuse red-team findings, fairness delta analysis, and for R3 an Assurance Case (GSN) linking hazards to controls to evidence.


security_provenance/ – Supply-chain and security artifacts: SBOM (Software Bill of Materials), vulnerability scan results (SAST/DAST, secret scanning), CVE report, cryptographic signatures/attestations, reproducible build proof, and a provenance graph.


governance/ – Governance records: ADRs, gate decision Gate Cards, AMEND/BRANCH logs, and Problem Red-Team memos (PRT).


product/ – Productization outputs: API/CLI specifications, configuration schemas, telemetry dictionary, user/operator runbook, interface freeze report, compatibility test results.


field_test_kit/ – Deployment and field testing tools: deployment scripts, simulators/generators, acceptance test checklists, rollback plans, incident response templates.


dashboard/ – A self-contained interactive dashboard (HTML/JS/CSS) visualizing key results: confidence intervals, tail performance, Pareto frontiers, fairness trends, drift over time.


C) Baseline Registry – A JSON file (baseline_registry.json) cataloging baseline references for the domain. For each relevant baseline method: name and version, configuration details, quality metrics, performance metrics (including tail metrics), hardware profile, seeds used for published results, reference to code/data snapshot, plus descriptions of the Do-Nothing baseline and Non-Tech alternative.


D) Domain Profile – A JSON file (domain_profile.json) capturing the problem definition and scope. Contents: Problem statement and scope, constraints, acceptance SLOs (primary metric definition with target values at p50/p95/p99), quality floor thresholds, cost (USD) and energy (J) targets, memory limits, real-time latency bounds (if applicable), benchmarking parameters (replications, warmups, minimum runtime, seed sweep count), hardware targets, budgets (max compute hours, cost ceiling, and optionally carbon budget in kgCO₂e). Also includes identified safety/fairness concerns, misuse scenarios, deployment context, assigned risk tier, explicit descriptions of the Do-Nothing baseline and top Non-Tech alternative, an Expected-Value Model summary, a Worth-It Score calculation, an Assumption Ledger summary, and falsification criteria (conditions that would make the solution not valuable or not feasible).


E) ADR (Architecture Decision Record) – For each significant decision: document title, context, the decision made, alternatives considered, consequences, evidence links supporting the decision, mapping to any relevant gate or phase, approver signatures, and the versions affected. ADRs are stored in the ADRs/ directory and updated at each decision point.


F) Statistical Benchmark Report – Structured performance results, saved as stats_report.json (machine-readable) plus a human-readable summary text. For each benchmarked test case: sample size (N), median and geometric mean performance, 95% confidence intervals, distribution metrics (p50, p95, p99), statistical test used (e.g. Mann-Whitney U on medians unless otherwise justified), significance level α, effect sizes, outcomes of seed sweep analysis, hardware and configuration details, and any pertinent notes.


G) Performance Pareto Data – A CSV (perf_pareto.csv) and accompanying plots illustrating the performance vs quality trade-off frontier. Each row (or point) corresponds to a configuration or variant, listing metrics such as time (ms), memory (MB), energy (J), cost (USD), primary quality metric, secondary metrics, a flag for the selected operating point, and notes. The Pareto frontier can be visualized to choose an optimal trade-off.


H) Formal Specifications (for non-ML components) – If the solution involves algorithmic components, include formal specification artifacts: documented properties (pre-conditions, post-conditions, invariants), oracle implementations or references (for example a reference implementation or a symbolic checker), metamorphic test pair definitions, any approximation bounds, and an outline of proof or empirical evidence that acceptance criteria are met.


I) Problem Selection Artifacts – Outputs from Phase −1 (Problem Discovery), which include: the Problem Charter, Stakeholder Map, Evidence Pack, templates describing the Do-Nothing and Non-Tech alternatives, a Feasibility–Impact matrix, an Expected-Value worksheet or model, a causal influence sketch, the Problem Red-Team memo (PRT from Phase −1), the premortem analysis, and an Ethics/Externalities note.


J) Decision Forecasts & Calibration Records – For major decisions (e.g. whether the project will meet SLOs, be adopted, delivered by deadline, etc.), the forecasts made and later outcomes. Contains the set of probability forecasts (with time frame and conditions), and after outcomes are known, the Brier scores for each (measuring accuracy). A summary of forecast calibration for each agent or team is maintained to adjust future decision confidence thresholds.


Default Directory Structure and Naming Conventions
Each GCP run produces a structured directory (named after the RunID) that organizes all artifacts, ensuring reproducibility and easy navigation. A recommended structure is:
Run_<RunID>/
├── ADRs/                   # Architecture Decision Records (e.g., ADR-<ID>-<Title>.md)
├── Artifacts/              # Key output artifacts (e.g., final checkpoint ZIPs, release packages)
├── Benchmarks/             # Benchmark results (raw CSVs, stats_report.json, plots)
├── CodeSnapshots/          # Code snapshots (source archives or diffs) at key checkpoints
├── RunLogs/                # Logs and ledgers (run_ledger.csv or .jsonl, gate decision JSON records)
├── SafetyDocs/             # Safety, privacy, fairness docs (ModelCard.md, DPIA.pdf, etc.)
├── SBOMs/                  # SBOM files and security scan reports (e.g., sbom.spdx.json, cve_report.txt)
└── Seeds/                  # Random seed files or notes for reproducibility (seed_list.txt, etc.)

Run Directory: Named Run_<YYYYMMDD>T<HHMMSS>Z (UTC timestamp) or similar deterministic identifier. All files within are associated with this run ID.


ADRs: Stored as individual markdown or text files in ADRs/, named with an index and title (e.g., ADR-001-ChooseDatabase.md).


Artifacts: Final artifacts such as release bundles or checkpoint archives. For example, a final model/package might be Artifacts/final_checkpoint_<RunID>.zip. Intermediate checkpoint bundles (e.g., after Phase 3) can also reside here or in a subfolder.


Benchmarks: Contains stats_report.json and stats_report.txt summaries, raw benchmark output files (*.csv), and any performance graphs or figures. File names include context, e.g., bench_results_phase6.csv, perf_pareto_run<RunID>.csv.


CodeSnapshots: Contains source code snapshots at important milestones (especially after prototype in Phase 3 and at final release). Could be a zipped source tree or exported git commit diff. Naming example: code_snapshot_phase3.zip and code_snapshot_final.zip.


RunLogs: Contains the Run Ledger (run_ledger.csv or run_ledger.jsonl with all events) and structured Gate decision logs (each gate’s machine-readable output, e.g., JSON files named Gate_<GateID>_decision.json). The gate decision JSON uses keys as described in Artifact A) and is produced as part of each Gate Card.


SafetyDocs: Contains documentation related to safety, ethics, compliance and human factors, such as ModelCard.md, FairnessReport.md (including bias/fairness analysis), DPIA.md (Data Protection Impact Assessment), AssuranceCase.gsn, UsabilityTestResults.txt, etc.


SBOMs: Contains software bill-of-materials files and security attestation materials. For example, SBOM.spdx.json or SBOM.cdx.json (CycloneDX format), vulnerability scan outputs (vuln_scan_report.txt), code signing certificates, and any attestation signatures.


Seeds: Contains records of random seeds used for experiments and runs. This could be a simple text listing seed values per test (seeds_used.txt) or configuration files capturing seed constants. This ensures experiments are reproducible by using the same seeds.


Naming Conventions: All artifact files include identifiers for traceability. Use the RunID in filenames where needed (especially if aggregating multiple runs in one place). For example, stats_report_<RunID>.json if stored outside the run folder. Phase-specific outputs include the phase or gate number in the name (e.g., phase1_baselines.csv, gateC5_quality_check.json). Timestamps in ISO 8601 format (or YYYYMMDDHHMMSS) are used for unique identification down to second-level. GateIDs embedded in file names tie outputs to decision points (e.g., GateC2_20250813T151030Z.json for the decision at Gate C2). This deterministic naming allows machine parsing and correlation of files to the corresponding run events.
Default Thresholds (Overridable by Domain Profile)
(Baseline acceptance thresholds, scaled by risk tier where applicable.)
Benchmark replications per test case: R1 ≥ 15; R2 ≥ 30; R3 ≥ 50.


Stochastic seed sweep count: R1 ≥ 5; R2 ≥ 10; R3 ≥ 20.


Minimum benchmark duration per case: ≥ 5 seconds of runtime (to ensure stable measurement).


Statistical significance level (α): ≤ 0.05 (95% confidence) unless a different alpha is justified and approved.


Code duplication index: ≤ 5% overlap between modules (higher requires explicit ADR justification).


Fairness regression tolerance: ≤ 0.5% relative degradation on protected groups or metrics (any larger regression must be mitigated or explicitly dual-approved with risk acceptance).


Evidence TTL (time-to-live): 90 days. After 90 days, previously gathered evidence (e.g. benchmarks, data profiles) is considered stale and must be re-verified if there have been changes in hardware, drivers, or critical dependencies.


Budget enforcement: The run must halt or branch if compute_hours_max or cost_ceiling_usd (from Domain Profile budgets) would be exceeded.


Worth-It Score (WIS) minimum: R1 ≥ 0.60; R2 ≥ 0.70; R3 ≥ 0.80, and no critical ethical/legal blocker flags for R3. (The Worth-It Score is defined below.)


(These defaults can be overridden by the Domain Profile to tailor to domain needs, and are automatically scaled up for higher risk tiers as noted.)
Metrics, Economics, and Decision Calibration
Worth-It Score (WIS): A composite score (0–1) to quantify the value of proceeding with the project. It is a weighted sum of six factors:
Impact (30%): Risk-adjusted expected net benefit compared to the Do-Nothing and Non-Tech alternatives. This includes the magnitude of the problem and the improvement the solution would bring, adjusted for probability of success.


Tractability (25%): Feasibility given available data, resources, authority, and time. Essentially, how solvable the problem is with the means at hand.


Causal Plausibility (15%): Evidence that the proposed intervention can causally drive the primary metric in the desired direction (based on the causal sketch and any early experiments).


Adoption (15%): Likelihood that target users/operators will adopt the solution, considering incentives, ease of use, and organizational or market friction.


Ethics/Externalities (10%): The extent to which harms are minimized and benefits outweigh any negative externalities. Higher if the solution has strong ethical alignment and mitigations for potential harms.


Strategic Fit (5%): Alignment with the organization's mission, strategy, or constraints (including time horizon and broader goals).


Expected-Value Modeling (EVM): Develop an expected-value analysis for the proposed solution vs alternatives. Compute a range of outcomes (e.g. P10/P50/P90 scenarios) via analytic estimation or Monte Carlo simulation. Include a tornado sensitivity chart highlighting which assumptions (from the Assumption Ledger) most influence the outcome. If the Non-Tech alternative or a Minimal Intervention approach has an overlapping outcome with the proposed solution (within the 90% confidence interval), pivot or stop – this indicates the more complex solution might not be justified. The EVM should clearly show the risk-adjusted net value of proceeding.
Decision Forecasts & Brier Scoring: For each key decision or milestone, record a probabilistic forecast (0–100%) of success or specific outcomes (e.g. “SLO will be met,” “Adoption ≥ X% by Y date”). After the outcome is known, score the forecast using the Brier score: $ (p - o)^2 $ where p is the predicted probability and o is the outcome (1 if happened, 0 if not). Maintain a log of these forecasts per agent or team. Use this to calibrate future decisions – if an agent is consistently over-confident or under-confident (poor Brier scores), adjust the threshold for what constitutes acceptable evidence from that agent.
"Confidently Wrong" Defense Stack (Cross-Cutting)
Problem Red-Team (PRT): Conduct adversarial reviews of the problem framing at multiple points (end of Phase −1, end of Phase 2, and before Phase 8). The PRT attacks the validity of the problem and solution by questioning assumptions: Is the problem real and significant? Are metrics chosen appropriately or are they gamable? Are causal assumptions justified? What if users don’t actually adopt it? Are there ethical, legal, or incentive issues? For each PRT session, produce a PRT memo with a list of scored objections. Every objection must either be mitigated, marked as an acceptable risk (with rationale), or lead to terminating or pivoting the project if it uncovers a fatal flaw.


Causal Validity Assurance: Every experiment in the project should be tied to a causal hypothesis. Document which causal relationship or assumption each test is validating (the causal_edge_id in the Run Ledger). For high-risk (R3) projects, provide at least a minimal structural causal model or perform a do-calculus reasoning thought experiment to justify that the intervention can impact the outcome. List potential confounders and how they are controlled or measured.


Premortem to Canary: Perform a premortem analysis (end of Phase −1, revisited later) where the team imagines the project has failed and brainstorm reasons why. The top failure mode indicators from the premortem are directly translated into monitors or canary checks in Phase 10. For example, if “users abandon the tool due to complexity” is a premortem risk, a corresponding canary metric (such as drop-off rate) is set with a threshold in production. When such an indicator trips, it triggers alerts or auto-rollback (see Phase 10).


No-Go as First-Class Outcome: If at any gate the decision is to stop the project, produce a No-Go Value Brief as a final artifact. This brief summarizes the findings, recommends the best alternative (perhaps a Non-Tech solution or a simpler intervention) and provides evidence as to why it’s preferable. In other words, “stopping” is treated as a valid outcome with documented rationale, not a silent failure.



Phase −1 — Problem Discovery & Worth-It Sprint
Objective: Decide if this problem is worth addressing at all before any solution work begins. The AI (Planner/Researcher roles) must gather evidence of the problem’s reality and importance, explore non-solution approaches, and estimate the value of solving it.
LLM Prompt (Phase −1):
You are in Phase -1 (Problem Discovery & Worth-It). Investigate the problem and its context to determine if it’s real, significant, and tractable. Complete the following:
Problem Charter: Define the problem clearly, including who is harmed by it, the conditions of satisfaction, any non-goals or out-of-scope aspects, and the time horizon for a solution.


Stakeholder Map: Identify all stakeholders (end users, operators, owners, regulators, negatively impacted parties) and their roles/interests.


Evidence Pack: Gather concrete evidence that the problem exists and matters. Include logs, support tickets, failure reports, user interviews, domain research, or any user-provided materials that demonstrate the problem’s impact.


Do-Nothing Baseline: Describe the status quo outcomes over time if we do nothing – e.g. the “outcome curve” for cost, quality, or risk if the problem remains unaddressed.


Non-Tech Alternatives: Identify at least three plausible solutions that don’t involve building new tech (policy changes, process improvements, training, hiring, outsourcing, etc.). For each, list pros/cons and estimated costs.


Feasibility–Impact Matrix: Rank broad categories of possible interventions (not specific solutions yet) by their potential impact vs difficulty. This will highlight if simpler approaches could yield good results.


Expected-Value Model: Estimate the expected net benefit of solving the problem. Calculate scenarios (pessimistic/likely/optimistic) for payoff vs. cost. Provide P10, P50, P90 values and identify which assumptions most influence these outcomes.


Causal Sketch: Draw a causal diagram or outline explaining how a potential solution would lead to improvement in the primary metric. Identify key drivers and any confounding factors or assumptions that would need to hold true.


Problem Red-Team: Perform an adversarial review of the above. Challenge the problem framing, metrics, and assumptions. Document this in a PRT memo.


Premortem: Imagine it’s a year later and the effort failed – list the reasons why. Assign a likelihood to each and identify early warning indicators for those failure modes (these indicators will become canary monitors if we proceed).


Ethics/Externalities Note: Identify any potential harms or externalities if the problem is solved. Consider safety, privacy, fairness, job displacement, etc., and note mitigation ideas.


Forecasts: Record forecasts for key future outcomes: e.g., “If we pursue this, chance that ≥X% of target users adopt in Y months,” “Chance we meet the SLOs,” “Chance we deliver by date D within budget Z,” etc. These will later be scored for calibration.
 Provide all the above outputs clearly for Gate C-0.5 evaluation.


Procedure: The AI completes the above steps in detail, producing the following artifacts in the Problem Selection Artifacts (I) category: a Problem Charter, Stakeholder Map, Evidence Pack, Do-Nothing baseline description, list of Non-Tech Alternatives, a Feasibility–Impact matrix, an Expected-Value Model analysis, a causal influence sketch, a Phase −1 PRT memo, a Premortem analysis, an Ethics/Externalities note, and documented forecast estimates. Each of these should be saved (e.g., as documents in SafetyDocs/ or Artifacts/) for reference at Gate C−0.5.
Gate C−0.5 — “Should We Even Try?”
Objective: Evaluate whether the problem is real, significant, and tractable enough to proceed. This Worth-It Gate determines if the project should continue or stop before any solution development.
Pass Criteria: All of the following must hold true:
Impact: The proposed class of interventions (solutions) shows clearly higher expected value than doing nothing and beats at least one credible Non-Tech alternative on a risk-adjusted expected-value basis, with high confidence (≈80% or greater certainty).


Tractability: It appears feasible to solve given current or attainable resources. The key inputs (data, knowledge, authority, etc.) exist or can be secured within the needed timeframe.


Causal plausibility: The causal sketch reveals no critical unaddressed confounders; we have identified measurable assumptions that can be tested, and there's a plausible cause-and-effect path from intervention to outcome.


Legal/Ethical viability: There are no known legal, compliance, or ethical constraints that would outright prevent this project. If any serious concern exists, a credible mitigation strategy is in place.


Adoption likelihood: The target users and operators are likely to adopt the solution if built. This should be supported by some evidence (preliminary user feedback, logic, or analogies) in the Evidence Pack.


If any of these criteria are not met, the gate FAILS.
Context Digest: At Gate C−0.5, compile a concise summary of findings from Phase −1: the size and severity of the problem (with evidence), the best alternative solutions considered, and the expected value of intervening. Include the Worth-It Score calculation and key insights (e.g., any A-class assumption that would be project-killing if false). Highlight any major risks or unknowns (legal issues, adoption doubts, etc.) that came up. This digest ensures the decision is based on a shared understanding of Phase −1 outputs.
Options:
Proceed (PASS) – Continue to Phase 0 (formalizing problem and assumptions) only if all Pass Criteria are satisfied and the problem is deemed worth solving.


Stop – Terminate the project now if the evidence suggests the problem is not worth pursuing. If stopped, immediately compile a No-Go Value Brief recommending the best alternative (e.g., a Non-Tech solution) with supporting evidence.


Reframe/Pivot – If the problem or approach can be reframed (for instance, focusing on a different scope or a simpler intervention) to meet the criteria, you may choose to redefine the project and restart Phase −1 or Phase 0 with the new framing. For example, pivot to the identified Minimal Intervention if it appears more promising.


Branch – Not typical at this early phase (since no solution built yet), but if there are multiple fundamentally different problem framings, one could branch (run a separate discovery track) for another framing while pausing the original.


Rationale Prompt: “Based on the Phase −1 findings, should we proceed with solving this problem? Summarize how the proposed intervention compares to doing nothing and Non-Tech alternatives on value and feasibility. Are all the Gate C−0.5 criteria met? If yes, justify why proceeding is worthwhile. If no, recommend stopping or reframing, and explain which criterion failed and why.”
Next-Step Instruction:
If PASS: Acknowledge the project is worth pursuing. The RCO should log the decision and instruct the Planner to initiate Phase 0.


If FAIL (Stop): Log the failure decision. Prepare the No-Go Value Brief artifact summarizing why the project won’t continue and highlighting the preferred alternative solution. No further phases are executed.


If Reframe/Pivot: Log a decision to pivot. Clearly document the changes in problem framing or approach (update the charter or scope), then either repeat Phase −1 with new parameters or jump to Phase 0 if the new framing is sufficiently solid.


If Branch: (Unusual here) start a parallel Phase −1/0 track for the alternative problem framing with its own RunID (the original may be paused or continue in parallel if resources allow).


Machine-Readable Metadata: Upon gate evaluation, generate a JSON record (to be appended to the Run Ledger and saved in RunLogs/) summarizing the decision. For example:
{
  "run_id": "<RUNID>",
  "gate_id": "C-0.5",
  "timestamp_utc": "2025-08-13T17:45:00Z",
  "decision": "FAIL",
  "selected_option": "Stop",
  "criteria_summary": {
    "impact": false,
    "tractability": true,
    "causal_plausibility": true,
    "legal_ethics": true,
    "adoption": false
  },
  "rationale": "Projected solution EV did not significantly exceed Non-Tech alternatives; user adoption is uncertain based on evidence.",
  "next_step": "No-Go Brief issued; project terminated."
}

This metadata includes the gate ID, timestamp, the decision outcome, a breakdown of criteria pass/fail, a brief rationale, and the next step. It should be logged in the Run Ledger.
Source: Phase −1 outputs and Gate C−0.5 criteria.

Phase 0 — Domain Profile, Four-Fit, Assumptions, Budgets
Objective: Codify the problem’s definition and constraints formally, enumerate assumptions, and set all project acceptance criteria and resource budgets. This phase produces a Domain Profile and related planning artifacts to ensure the project is well-framed and feasible.
LLM Prompt (Phase 0):
You are now in Phase 0 (Domain Profile & Planning). Formalize the project’s scope and plan:
Domain Profile: Draft the domain_profile.json with all key parameters: define the primary success metric (and its target values at median/p95/p99), quality floor thresholds for that metric or others, target cost and energy usage, memory limits, realtime latency bounds if any, and the test/benchmark parameters (number of replications, etc.). Include the risk tier (from Phase −1’s assessment) and reference the Do-Nothing and Non-Tech baselines identified earlier. Capture the deployment context and any misuse scenarios in this profile as well.


Four-Fit Analysis: Evaluate and record the four “fits” for the project:


Problem–User Fit (does the target user genuinely need this? Is their pain validated and will they have incentive to adopt?),


Problem–World Fit (is the solution permissible and responsible in the real world? Consider legal, safety, compliance constraints),


Solution–Problem Fit (will the chosen type of solution actually address the root cause identified in the causal sketch?),


Capability–Solution Fit (can the team, with available data and resources, realistically build and operate this solution?).


Assumption Ledger: List all key assumptions about the problem and solution. Categorize each as A (critical – would kill the project if false), B (important but survivable if false), or C (minor). For each A-level assumption, plan a “fast kill” test or validation to run as early as possible (so we can fail fast if it's untrue).


Falsification Criteria: Define clear criteria or observable events that would prove this project is not valuable or not feasible. Essentially, under what conditions would we decide to stop later? (e.g., “If baseline already meets X, then project is not valuable” or “If no model can beat metric Y by Z, then it’s not tractable”).


Budgets: Set the budget limits: maximum compute hours, cost ceiling in USD, and if relevant a carbon emission budget (CO₂e) for this project. These come from the Domain Profile and ensure we know constraints.


Intake ADR: If any significant decisions or frameworks are chosen in this planning (like choosing a particular platform or defining a key method), record an Architecture Decision Record capturing why. Append any new decisions to the Run Ledger.
 Provide the Domain Profile (in JSON or structured form), the Four-Fit assessment, the Assumption Ledger (with categories and planned tests), falsification criteria, and a summary of budgets as outputs for Gate C0.


Procedure: The AI (Planner role) creates a Domain Profile document capturing all the above details. Key steps include: drafting the Domain Profile with SLOs and constraints (Step 0.1), performing the Four-Fit assessment (0.2) and recording the results, preparing an Assumption Ledger with categorized assumptions and planned tests (0.3), defining falsification criteria (0.4), and noting any initial decisions in an ADR and the run ledger (0.5). All these artifacts are saved (e.g., domain_profile.json, assumption_ledger.md, etc.). The budgets in compute hours, money, etc., are explicitly recorded as part of the profile. The Planner also ensures the Domain Profile references the baseline approaches (Do-Nothing and Non-Tech) for context.
Gate C0 — “Eligibility”
Objective: Confirm that the project is well-founded and ready to move into solution exploration. This gate checks that Phase 0 produced a complete and consistent plan.
Pass Criteria: The project can proceed only if all of the following are true:
The Domain Profile is complete with all required fields filled (metrics, targets, budgets, risk tier, baselines, constraints, etc.).


The Four-Fit assessment is positive/green – no “fit” category is signaling a major misalignment. (Any serious issue in user fit, world fit, etc., should cause a re-think.)


An Assumption Ledger exists and includes tests or validation plans for each A-class (critical) assumption.


Falsification criteria are defined – clear conditions under which the project would be considered not valuable or not feasible are documented.


Budgets are set – the team has defined the resource limits (time, compute, money, etc.) and they are deemed reasonable for the project scope.


If any of these are missing or inadequate, the gate fails.
Context Digest: Summarize the Phase 0 outputs: present the key points of the Domain Profile (primary metric and goal, risk tier, major constraints), highlight any critical assumptions identified, and note the overall outcome of the Four-Fit analysis (e.g., “three fits are solid, one fit (Problem–World) has a potential issue with compliance which is mitigated by X”). This digest should give enough context to judge if planning is sufficient and realistic.
Options:
Proceed (PASS): All planning artifacts are in place and satisfactory. Proceed to Phase 1 (Baseline comparison).


Fix and Re-run Phase 0: If some planning elements are incomplete or weak (e.g., an assumption with no test plan, or budgets not defined), pause here. The system can iterate within Phase 0: refine the Domain Profile, get missing approvals (e.g., if risk tier assignment needs sign-off), or add necessary details, then attempt Gate C0 again.


Stop: If fundamental misalignments are found (e.g., Four-Fit reveals the team cannot solve it, or a falsification criterion is already triggered by known data), it might signal to stop the project early. In this case, produce a No-Go brief explaining the decision.


Amend (Threshold Adjustments): If everything is good except some threshold set in Domain Profile seems unrealistic or too strict (for example, budget too low to ever succeed), an option is to formally AMEND that threshold via governance (with approval) and update the Domain Profile, then reassess.


Branch: Unlikely at this stage, but if there are two competing ways to frame the project (e.g., two different definitions of success metrics or scopes), one could branch into parallel tracks with different Domain Profiles and see which passes gates further on.


Rationale Prompt: “Evaluate Gate C0. Is the Domain Profile complete and coherent? Are acceptance criteria and assumptions thoroughly documented? Four-Fit check: do we have a good Problem–User, Problem–World, Solution–Problem, Capability–Solution fit? Explain any gaps. Should the project proceed to Phase 1?”
Next-Step Instruction:
If PASS: Log the successful gate. The RCO instructs the Researcher role to begin Phase 1 (Baselines & Alternatives).


If FAIL (Fix): Log the deficiencies. The AI should loop back within Phase 0 to address the issues (update the Domain Profile or other artifacts). After fixes, re-run the Gate C0 check.


If FAIL (Stop): Log the stop decision and produce a No-Go brief as in C−0.5, since the project won’t move forward.


If AMEND: Route to the Auditor for threshold approval. After adjusting any threshold or budget (with rationale recorded in an ADR and ledger), update Phase 0 artifacts and re-evaluate Gate C0.


If Branch: Initiate a new branch with an alternative Domain Profile; proceed with both in parallel up to a certain point (this is rare and resource-intensive).


Machine-Readable Metadata: A JSON summary for Gate C0, for example:
{
  "run_id": "<RUNID>",
  "gate_id": "C0",
  "timestamp_utc": "2025-08-13T18:12:00Z",
  "decision": "PASS",
  "criteria_check": {
    "domain_profile_complete": true,
    "four_fit_green": true,
    "assumptions_test_plans": true,
    "falsification_defined": true,
    "budgets_set": true
  },
  "rationale": "Domain Profile complete with SLOs, budgets, and risk tier; Four-Fit shows all fits acceptable; all critical assumptions have tests.",
  "next_phase": "1"
}

This record is logged in RunLogs/ and appended to the Run Ledger, capturing the gate outcome and reasoning.
Source: Phase 0 outputs and Gate C0 criteria.

Phase 1 — Baselines & Alternatives
Objective: Establish honest baselines and alternatives to compare against any proposed solution. This phase ensures we know how well existing solutions or simpler approaches perform, so we only pursue a new invention if it clearly offers value beyond these baselines.
LLM Prompt (Phase 1):
Enter Phase 1 (Baselines & Alternatives). Assemble and analyze baseline solutions:
Technical Baselines: Identify one or more technical baseline methods or state-of-the-art (SOTA) solutions relevant to this problem. This could include simple existing algorithms, open-source tools, or prior versions of a solution. Gather their performance on our metrics if available.


Do-Nothing & Non-Tech Baselines: Clearly describe the Do-Nothing baseline (the outcomes if we make no change, as defined in Phase −1) and a Non-Tech baseline (the best non-technical alternative approach, from Phase −1). Define how we would measure outcomes for each (what metrics, what data).


Outcome Metrics for Baselines: For each baseline (tech, Do-Nothing, Non-Tech), define the exact metrics and how to measure them so we can compare fairly. (E.g., if the primary metric is response time improvement, measure current response times under baseline conditions).


Complexity Check: Justify the complexity of the proposed solution by comparing to simpler baselines. Are we introducing unnecessary complexity? Document why the simpler baseline(s) cannot meet the SLOs or requirements (risks of over-engineering).


Novelty Ledger: Start a Novelty Ledger listing any novel ideas or techniques our solution will use, and what measurable benefit we expect from each. (This will be expanded as we design).


Kill Criteria: Define clear criteria that would trigger stopping the project during development. For example, “If a baseline already meets all SLOs, then there's no point in continuing,” or “If our novelty doesn’t produce at least X% improvement, we stop.” These are conditions under which continuing development is not justified.


Formal Specs (if non-ML): If this problem isn’t primarily an ML problem, prepare any formal specifications or oracles needed (e.g., a reference implementation to compare against, or invariants for correctness).


ADR Updates: Record any decisions about baseline selection or scope changes as needed, and update the Baseline Registry artifact with the chosen baselines.
 Provide metrics comparisons for all baselines, the Novelty Ledger (initial entries), and any kill criteria as outputs for Gate C1.7.


Procedure: The AI (Researcher role, with Planner oversight) performs the above steps. It compiles a list of Technical Baselines and SOTA with descriptions and known metrics. It defines the Do-Nothing and Non-Tech baseline measurements explicitly. It checks for any simpler solution that might already solve the problem (to avoid over-engineering) and notes why those are insufficient. It creates or updates the Novelty Ledger (artifact listing proposed innovations and expected benefits). It also defines Kill Criteria for early termination conditions. If this project involves classical software (non-ML), Phase 1 includes preparing any formal specification or test oracle needed. Finally, relevant ADRs are written (e.g., to record the choice of baselines or any scope decision) and the Baseline Registry is updated with baseline performance data. All outputs (baseline results, Novelty Ledger, etc.) are saved for gate review.
Gate C1.7 — “Worthiness & Complexity Check”
Objective: Decide if the project is still justified given the baseline comparisons and ensure we are not pursuing an unnecessarily complex solution. Essentially, confirm that the new solution offers potential value beyond what baseline or simpler approaches achieve.
Pass Criteria: The gate passes only if:
The value proposition is clear: The baselines (including Do-Nothing and Non-Tech) do not meet the acceptance SLOs or other key requirements. The proposed solution (as envisioned) is expected to surpass them in meaningful ways (impact, efficiency, etc.).


Novelty is non-trivial: If claiming any novel approach, it should not be a trivial variation of existing solutions unless that’s justified. There should be a real, explained advantage. (If our solution has no significant edge over existing ones, why build it?).


No simpler alternative would suffice: We have evidence or reasoning that a simpler baseline or a non-technical measure cannot achieve the required outcomes. (We’re not over-engineering.).


Unresolved critical assumptions are addressed or planned: If any A-class assumption from Phase 0 remains untested and could undermine the project, there is a near-term plan to test it. If an A assumption is already proven false or remains highly doubtful with no mitigation, that’s a fail (reframe or stop).


If these conditions hold, the project is “worthy” to continue. If not, the gate fails or triggers a pivot.
Context Digest: Summarize how the best baselines perform. For example: “Baseline (Do-Nothing) yields metric = X, best Non-Tech yields Y, our target is Z, gap remains significant.” Highlight any Novelty Ledger entries and expected benefits. Note if any baseline nearly meets the goals (warning sign) or if any assumption is hanging by a thread. This context sets the stage for either continuing or reconsidering the approach.
Options:
Proceed (PASS): Continue to Phase 2, confident that new development is justified.


Reframe/Pivot: If a baseline or alternative is nearly as good as the proposed solution (within ~90% CI of performance or value), consider pivoting to that simpler solution or altering the plan. For instance, if a “Minimal Intervention” (from Phase 2 planning) or a Non-Tech approach could achieve similar results with less risk, pivot towards that. This might involve going back to refine Phase 2 or even Phase −1 reasoning.


Stop: If the analysis reveals that the problem can essentially be solved by existing means (or not worth solving), stop the project. Issue a No-Go brief explaining that a baseline suffices or project value is not there.


Branch: If there are two viable solution paths (e.g., a complex new approach vs an incremental improvement on a baseline), one might branch to pursue an experimental path on the novel idea while also considering adopting the simpler path. Set success criteria and budgets for the branch.


Mitigate Assumptions: If an untested critical assumption is the only blocker, you might temporarily proceed but with a condition: immediately address that assumption in the next phase (e.g., design an experiment in Phase 2 or 3 to test it). In some cases the gate could be conditionally passed with a requirement to validate the assumption early.


Rationale Prompt: “Assess Gate C1.7. Do the baseline solutions (including doing nothing) fall short enough to justify our project? Is our planned approach clearly better and not overly complex for the gain? Summarize baseline vs target comparison, and decide if continuing is worthwhile. Note any critical assumption that could stop us later.”
Next-Step Instruction:
If PASS: Record that building a new solution is justified. Proceed to Phase 2 (Design Space Exploration).


If FAIL (Reframe/Pivot): Log the decision to pivot or change course. Possibly jump to Phase 2 but focusing on a simpler “Minimal Intervention” design (if not already planned), or go back to adjust assumptions and approach. The RCO could involve the Inventor role immediately to integrate the simpler alternative as the primary path.


If FAIL (Stop): Log the outcome and produce a No-Go brief, as earlier, stating that baselines suffice or value isn’t there (include the evidence from Phase 1).


If Branch: Initiate a parallel track for an alternate approach (ensuring resources and budgets are defined), while possibly still proceeding with main Phase 2 on the primary plan.


If Conditional Pass: Proceed but flag the unvalidated assumption or borderline case, and schedule an immediate test (e.g., ensure Phase 2 experiment plan includes a test for that assumption).


Machine-Readable Metadata: Example JSON log for Gate C1.7:
{
  "run_id": "<RUNID>",
  "gate_id": "C1.7",
  "timestamp_utc": "2025-08-13T19:05:00Z",
  "decision": "PASS",
  "baseline_comparison": {
    "do_nothing_metric": 0.5,
    "non_tech_metric": 0.6,
    "target_metric": 0.8,
    "proposed_expected": 0.85
  },
  "novelty_ledger": ["New algo expected +20% efficiency"],
  "unresolved_assumptions": [],
  "rationale": "Baselines fall short of required performance (max 0.6 vs target 0.8). Proposed approach with novel algorithm is expected to reach 0.85. No simpler solution meets requirements.",
  "next_phase": "2"
}

This includes a summary of baseline vs target, any novelty highlights, and confirms no critical assumptions block progress.
Source: Phase 1 outputs and Gate C1.7 criteria.

Phase 2 — Design Space Exploration (with Minimal Intervention Track)
Objective: Propose and evaluate multiple candidate solution designs, explicitly including the simplest viable option (the “Minimal Intervention”). The goal is to map out the design space and not jump to complexity if a simpler approach could work.
LLM Prompt (Phase 2):
Begin Phase 2 (Design Space & Solution Ideation). Develop solution design options:
Enumerate Designs: Come up with at least three distinct solution designs or variants, each with meaningful trade-offs. (For example, different architectures, algorithms, or approaches to the problem.) Document each design.


Hypotheses & Metrics: For each design, state the hypothesis of why it would succeed and what measurable outcomes it targets. Identify which part of the causal sketch it addresses. List what aspects might be ablated (i.e., if this component is removed or simplified, how would performance change) and known risks or unknowns for each design (complexity, data needs, etc.).


Complexity & Simplification: Note the complexity of each design and possibilities to simplify it. Could any design be made smaller or more efficient while still solving the problem?


Minimal Intervention Track: Propose a Minimal Intervention solution. This should be the simplest possible approach that could have a meaningful impact – e.g., a policy change, a tiny script or tool, a manual process (“Wizard-of-Oz”), or a very lightweight automation. Even if it’s not tech-heavy, include it as one of the designs.


Select Primary & Fallback: Choose a primary design to pursue and at least one fallback/backup design. Base this on expected value and feasibility. For example, primary might be the more innovative solution, fallback could be a simpler one.


Minimal Pivot Trigger: Decide on a trigger condition under which you would pivot to the Minimal Intervention approach. (For instance, “If by Gate C5 the complex solution hasn’t beaten baseline by X%, we switch to the minimal solution.”)


Experiment Plan: Formulate a high-level experiment and evaluation plan for the next phases. Determine what datasets or test cases will be used, how benchmarks will be configured, which statistical tests will be applied, how many seeds (see risk tier defaults), fairness checks, and what specific causal edges from the Phase −1 sketch will be tested by these experiments. Also plan any necessary power analysis to ensure statistical significance.


PRT #2: Conduct a second Problem Red-Team on the chosen designs. Have the Adversary role critique the proposed solutions: are we solving the right problem, any new failure modes introduced, any ethical issues? Document this as PRT memo #2.


ADR & Ledger: Record design decisions in an ADR (especially rationale for primary vs fallback choice, and inclusion of Minimal Intervention). Append a summary to the Run Ledger.
 Provide a summary of each candidate design (with pros/cons), identify the primary and fallback, the minimal solution, and the experiment plan outline as outputs for Gate C2.


Procedure: The AI (Inventor role, with input from Researcher/Planner) generates multiple design proposals. It thoroughly documents at least three distinct approaches (2.1), including a deliberately simple one (2.3 Minimal Intervention). For each, it lists hypotheses and metrics (2.2), complexity and possible ablations (2.2), and any foreseen risks. The team then selects a Primary design and a Fallback design, noting why (expected higher EV vs. safer bet, etc.). It also explicitly notes a pivot condition to the Minimal Intervention if the complex path underperforms (e.g., a check at some gate). Next, the team drafts an Experiment Plan for Phase 3–5: which data, which benchmarks, how many trials, what statistical tests (ensuring it aligns with power requirements and fairness checks). Importantly, the plan ties back to the causal edges identified – ensuring each key assumption or mechanism will be tested. A second adversarial review (PRT #2) is done on the plan and designs, and any issues found are mitigated or noted. Finally, an ADR capturing the design selection and experiment plan is written, and an entry added to the run ledger.
Gate C2 — “Plan Integrity”
Objective: Ensure that the chosen solution design and experimental plan are sound, testable, and include the simplest viable option as a check. This gate validates that Phase 2 yielded a falsifiable plan with clear hypotheses.
Pass Criteria: The plan is solid and can proceed only if:
The project has a falsifiable plan: there are specific hypotheses for each design that can be tested and potentially proven wrong. The experiment plan should be capable of invalidating a design if it doesn’t work (not just confirming biases).


Statistical power and rigor: The experiment plan includes sufficient replication, appropriate statistical tests, and consideration for significance thresholds (per default or adjusted by domain need). Essentially, the plan would detect meaningful differences if they exist.


Ablation-ready design: The designs include plans for ablation or variant testing so we can attribute which components actually contribute to outcomes (especially for the novel aspects).


Minimal Intervention included: A clearly simpler alternative (Minimal Intervention) is in the comparison. If the “fancy” solution doesn’t greatly outperform this minimal track, the plan acknowledges a pivot will occur. (In other words, we won’t ignore a cheaper solution that works nearly as well.)


Causal links identified: Each key causal assumption or “edge” in the problem’s causal sketch has at least one experiment in the plan aiming to test it.


PRT feedback addressed: Any serious issue raised by the second Problem Red-Team has been mitigated or accepted with rationale.


If these conditions are satisfied, the gate passes.
If the Minimal Intervention actually appears to meet the goals or ties the expected value of the complex solution within the planned confidence interval, the instruction is to pivot to that simpler approach now instead of continuing on a complex path. (This is a special case where Gate C2 can redirect the project.)
Context Digest: Summarize the selected primary design and the fallback. Mention the Minimal Intervention option and why it is or isn’t sufficient. Outline the key points of the experiment plan: what will be tested, on what data, and how success will be measured. Include any critical thresholds (like “if design doesn’t beat baseline by >10% by Phase 5, pivot to minimal”). Also briefly mention any PRT #2 findings if they affected the plan.
Options:
Proceed (PASS): The design and plan are good. Continue to Phase 3 (Prototype Build) focusing on the Primary design (and possibly initial steps for fallback or minimal track as needed).


Pivot to Minimal: If evidence or analysis at this point suggests the simplest solution might actually achieve acceptable results (for example, maybe during Phase 2 it became clear that a policy change could solve 80% of the problem at a fraction of complexity), you might decide here to implement the Minimal Intervention as the main solution. In effect, drop the complex design and proceed with a scaled-down plan. This might skip some later phases or alter acceptance criteria.


Refine Plan: If the experiment plan is incomplete or not convincing (e.g., lacks a fairness check or enough replications), hold here. Iterate on Phase 2: adjust design details or plan specifics, possibly consult the Auditor to ensure compliance with thresholds, then re-evaluate.


Stop: If no proposed design seems plausible or if the plan cannot be made testable (e.g., if hypotheses are too vague or resources inadequate for the needed experiments), it may be better to halt. Document why (e.g., “no viable solution design found that we can test properly”).


Branch: If two designs are equally promising and fundamentally different (say one ML-based, one rule-based), you could branch: pursue both in parallel as separate implementations up through Phase 3 or 4 to gather comparative data, within allocated budgets.


Rationale Prompt: “Review Gate C2. Do we have at least three well-considered designs including a minimal one? Is our experimental plan thorough and testable? Will we know if our solution actually works better than the minimal alternative? State if the plan is ready to execute or if changes are needed.”
Next-Step Instruction:
If PASS: Log the outcome. The RCO triggers Phase 3, instructing the Engineer role to start prototyping the primary (and possibly the minimal/fallback in parallel if resources permit).


If FAIL (Refine): Note the deficiencies. The team remains in Phase 2 to improve the plan – e.g., add missing experiments, clarify hypotheses – then attempt Gate C2 again.


If Pivot: Log that a pivot to the Minimal Intervention has occurred. Realign phases accordingly: possibly jump to building that simpler solution (Phase 3, but for the minimal design) and adjust later phase criteria as needed (some later gates might simplify if minimal solution is less complex).


If Stop: Record the decision and reasoning (in No-Go brief format). End the run.


If Branch: Allocate separate run branches for each design path, marking the original run as branched at Gate C2. Each branch gets its own RunID (with reference to parent) and proceeds through Phase 3+ independently up to a planned merge or comparison point.


Machine-Readable Metadata: Example for Gate C2 decision:
{
  "run_id": "<RUNID>",
  "gate_id": "C2",
  "timestamp_utc": "2025-08-13T20:10:00Z",
  "decision": "PASS",
  "design_options": 3,
  "primary_design": "NeuralNetModel_A",
  "fallback_design": "LinearModel_B",
  "minimal_intervention_included": true,
  "pivot_condition": "If Primary < 5% better than Minimal by Phase 5",
  "plan_checks": {
    "falsifiable": true,
    "statistical_power": true,
    "causal_edges_covered": ["data_quality->accuracy", "training_time->performance"]
  },
  "rationale": "Three designs evaluated; chosen primary vs fallback. Experiment plan covers all critical assumptions with adequate power. Minimal alternative present with pivot criteria set.",
  "next_phase": "3"
}

This indicates that multiple designs were considered, that the plan meets criteria, and what the pivot trigger is.
Source: Phase 2 outputs and Gate C2 criteria.

Phase 3 — Prototype Build and Reproducibility
Objective: Implement minimal working prototypes of the primary (and possibly fallback/minimal) solution and set up deterministic evaluation harnesses. The emphasis is on correctness and reproducibility rather than optimization.
LLM Prompt (Phase 3):
Proceed with Phase 3 (Prototype Build & Reproducibility). Focus on creating a basic, correct implementation and a testing environment:
Repository Scaffold: Set up a version-controlled repository for the project code. Include necessary configuration to ensure reproducibility: initialize dependency lockfiles (pin library versions), create a Dockerfile or environment description, and write notes on how to perform a reproducible build. Also set up a simple continuous integration (CI) pipeline to run tests.


Implement Prototypes: Develop the primary solution design as a prototype (and the fallback or minimal solution as well, if parallel prototyping is planned). These prototypes should be minimally functional, focusing on correctness of output rather than performance. For example, if it’s an algorithm, implement it in clear, simple code.


Deterministic Harnesses: Build harnesses for testing and evaluation. This includes code to run benchmarks, manage random seeds, evaluate quality metrics, and generate reproducible results. Ensure that every run can be done with a fixed seed to yield identical results (for debugging and consistency).


Synthetic Data Generators (if needed): If real data is limited or specific scenarios are hard to get, implement synthetic data generators or simulators with known invariants for testing purposes. Ensure they can seed control to produce consistent outputs.


Environment Fingerprint: Record the environment details. Capture OS version, CPU/GPU details, driver versions, and library versions. This can be done by generating an environment fingerprint (e.g., hashing the environment details or listing them in a file) so that we can later ensure tests run in the same environment.


Checkpoint 3: Once prototypes and harnesses are ready, create Checkpoint 3 – a snapshot of the code and environment at this stage. Package the repository, lockfiles, any initial data, and configuration into a checkpoint archive. This ensures we can reproduce Phase 3 results exactly later.


Run basic end-to-end test: Using the harness, run the prototype on a trivial test case or subset to verify end-to-end functionality with a fixed seed. It should produce output without errors. Save this output for reference.


Ledger Update: Log a ledger event that prototypes are complete and reproducibility infrastructure is in place.
 Provide the repository structure, notes on reproducibility (e.g., how to build/run deterministically), and confirmation of an end-to-end run as outputs for Gate C3.


Procedure: The Engineer role sets up the project repository and environment to ensure reproducibility. They implement the Primary prototype (and any other necessary prototypes) focusing on correctness. They also implement harnesses: scripts or tools for running experiments consistently (managing random seeds, input data, and capturing outputs). The random seed management is critical – e.g., the code should allow specifying a seed so that results are repeatable. They gather environment info (e.g., use pip freeze or container base image details) to produce an environment fingerprint. After implementation, the team performs an end-to-end run on a simple case to ensure everything is wired correctly. Then they create Checkpoint 3: archiving the code, configuration, environment spec, etc., likely in the Artifacts/ directory as something like checkpoint_phase3_<RunID>.zip. Finally, they append an event to the Run Ledger (noting completion of Phase 3, commit hash, etc.).
Gate C3 — “Minimal Viability”
Objective: Verify that the prototype works end-to-end in a controlled setting and that the groundwork for reproducibility is laid. Essentially, ensure we have a working base to iterate on.
Pass Criteria: The gate passes if:
End-to-end functionality: The prototype can run from start to finish on at least a simple test case without errors, producing output. This demonstrates the solution is “minimally viable” in a basic sense (it runs and solves a trivial instance of the problem).


Determinism and Reproducibility: Running the prototype with a fixed seed yields consistent results. The harness and environment setup must allow exact repetition of results (within floating-point tolerance, if applicable).


Environment captured: An environment fingerprint (OS, dependencies, versions) has been recorded, and key dependencies are pinned/locked. This criterion ensures we can recreate the software environment later.


Checkpoint created: The checkpoint archive for this phase is saved and contains the necessary artifacts (code, configs, perhaps initial data or model if any).


Basic tests passed: Any basic unit tests or invariant checks included in the harness (like sanity checks on outputs, invariants from synthetic data tests) are passing.


If these are all true, we consider the prototype “minimally viable.”
Context Digest: Outline what was built: mention the primary prototype’s nature (e.g., “A neural network with architecture X implemented; a fallback Y also implemented”), and the setup for reproducibility (e.g., “All dependencies pinned in requirements.txt, Dockerfile prepared, random seed control in place”). Summarize the results of the end-to-end test (for example: “On a sample input, the prototype produced plausible output and the run can be repeated exactly with seed 42, yielding identical output file hash”). Confirm that Checkpoint 3 was created with commit hash ABC123.
Options:
Proceed (PASS): Prototype is sound. Proceed to Phase 4 (Robustness testing).


Fix Issues: If minor issues exist (like a nondeterministic element or a small bug), fix them while staying in Phase 3, then re-run tests and re-check gate. Examples: ensure sorting of dictionary iteration for determinism, correct a failing unit test, update a dependency version to match expected environment. Once fixed, attempt Gate C3 again.


Revisit Design: If major functionality is broken or performance is drastically off even on trivial cases, it might indicate a deeper design flaw. Possibly go back to Phase 2 or adjust the approach (maybe switch to fallback design) and then rebuild prototypes.


Stop: Unlikely at this point unless the team cannot even get a basic prototype working or environment issues are insurmountable. Stopping here would be extreme; more often one would iterate until it passes.


Branch: If the primary prototype fails but a quickly-made fallback prototype works (or vice versa), one could effectively branch by switching the roles (adopt the fallback as primary going forward or maintain both). However, this is more a design decision than a typical branch at this stage.


Rationale Prompt: “Evaluate Gate C3. Can the prototype run end-to-end successfully and repeatably? Is the environment properly captured for reproducibility? List any problems found (e.g., nondeterministic outputs, failing test) or confirm that all looks good to proceed.”
Next-Step Instruction:
If PASS: Document the success. The RCO moves the process to Phase 4 (Adversarial Robustness), engaging the Adversary role to test the prototype’s limits.


If FAIL (Fixable issues): Log what failed. Remain in Phase 3; address the issues (e.g., ensure seeding is fixed, patch the code bug, update the environment spec). Re-run the end-to-end test until criteria are met, then mark gate as passed.


If FAIL (Design flaw): Potentially step back to Phase 2 to modify the design or switch to fallback. After design changes, Phase 3 may need to be re-executed (build a different prototype).


If Stop: Not typically expected; would produce a No-Go with reasons (like "unresolvable technical hurdles in prototyping").


Machine-Readable Metadata: Example log entry for Gate C3:
{
  "run_id": "<RUNID>",
  "gate_id": "C3",
  "timestamp_utc": "2025-08-13T21:30:00Z",
  "decision": "PASS",
  "prototype": "Primary",
  "e2e_test_case": "simple_input_1",
  "output_hash": "abcdef123456",
  "reproducible": true,
  "checkpoint_ref": "checkpoint3_<RUNID>.zip",
  "rationale": "Prototype ran to completion on simple_input_1 with correct output. Re-running with same seed produced identical output hash. Environment and code snapshot saved in checkpoint."
}

This indicates the prototype is working and reproducible, with an example output hash to show determinism.
Source: Phase 3 outputs and Gate C3 criteria.

Phase 4 — Adversarial Robustness
Objective: Test the prototype’s robustness by subjecting it to adversarial and edge-case inputs early in development. The aim is to uncover brittleness, errors, or unintended behaviors now, rather than later.
LLM Prompt (Phase 4):
Start Phase 4 (Adversarial Robustness Testing). Challenge the prototype with aggressive tests:
Metamorphic Tests: Identify at least three transformations of inputs that should not change the output (invariance) or should change it in predictable ways. For each, generate altered test cases. Example invariances: adding irrelevant whitespace to input text, rotating an image that should yield the same classification, etc. Example predictable change: if input is scaled by factor, output should scale accordingly. Verify the prototype’s output remains correct under these transformations.


Property-Based Tests: Define properties or invariants the output should always satisfy. Generate a broad range of random inputs (where possible) to test these properties. E.g., outputs should never be negative for a certain function; or conservation laws in calculations; or idempotence when applicable. Implement generators for valid random inputs and check invariants.


Fuzzing: Perform fuzz testing by feeding random, unexpected, or malformed inputs to the system. Include both completely random inputs and structured fuzzing that respects some input format. Monitor for any crashes, exceptions, or severe slowdowns (hangs). Ensure the system fails gracefully (no crashes or undefined behavior).


Misuse & Negative Testing: Intentionally try inputs or scenarios that aim to produce harmful or undesired outcomes. For instance, if it’s a text model, input prompts aiming for disallowed content; if it’s an algorithm, inputs at extremes to see if it breaks constraints. Verify that the system either handles these safely or explicitly rejects them.


Fairness Probes: If the problem involves human-related data, test the system on different subgroup slices or edge demographics. See if performance or outputs degrade for any particular group. Identify any biases or disparate behaviors emerging. Plan mitigations for any severe issues.


Remediate & Retest: For any high-severity failures found (crashes, wrong outputs violating invariants, security issues, etc.), implement fixes or mitigations now. Then re-run the relevant tests to ensure the issues are resolved. Document what was done for each issue (in code comments or design notes).


Log Results: Summarize the adversarial tests performed and their outcomes. Update the run ledger with what tests were done and which issues were fixed.
 Provide a list of tests (metamorphic transformations, properties, fuzz cases, etc.), their outcomes (pass/fail), and any fixes applied as outputs for Gate C4.


Procedure: The Adversary role (or testing agent) systematically goes through the above categories of tests. They design metamorphic test cases and verify outputs are consistent. They write property-based tests (could use frameworks like Hypothesis/QuickCheck if coding, or manually create variations) to generate lots of inputs and check invariants. They fuzz the system with random data to see if it crashes or behaves unexpectedly. Misuse testing is done (especially important if output can be harmful - ensure safe fail for bad inputs). If data is human or socially sensitive, fairness checks across subgroups are done to spot any unacceptable biases. All issues found are logged; the Engineer will fix critical ones and adjust the prototype accordingly. After fixes, tests are re-run to confirm resolution. The Adversary writes a short report (could be an internal document or part of the run log) summarizing all the robust tests done and outcomes. This phase may iterate until the prototype passes the critical robustness tests.
Gate C4 — “Robustness”
Objective: Ensure that major vulnerabilities or brittleness have been addressed. Gate C4 checks that the system can handle a reasonable range of anomalous or adversarial inputs without critical failure.
Pass Criteria: The system passes Gate C4 if:
All high-severity issues discovered in Phase 4 have been mitigated or fixed, and the tests have been re-run to confirm. (High-severity means anything causing crashes, security vulnerabilities, large errors, etc.)


Coverage of adversarial tests is deemed adequate. That means a variety of metamorphic tests, property tests, fuzz inputs, and misuse scenarios were tried, and any gaps are justified as low-risk. Essentially, we are confident we didn’t skip testing obvious edge areas.


Any remaining minor issues are documented with a plan to address if needed (and are not serious enough to stop the project).


For fairness or misuse tests, if any major problem was found (like clear bias or unsafe behavior), there is either a fix applied or at minimum a mitigation strategy committed to (with an issue logged to revisit it by Phase 9 if needed).


The system demonstrates graceful handling of unexpected inputs (no uncontrolled crashes or unchecked exceptions in tests).


If critical failures are still present, the gate fails.
Context Digest: Summarize what adversarial tests were done and the overall result. E.g., “Tested invariances (X, Y, Z) – all held except Z, which was fixed by adjusting module M. Fuzzed 1000 random inputs – no crashes observed, only 2 minor errors which were fixed. Misuse test showed system gracefully rejects disallowed input. Fairness check noted a slight performance drop for group B (we plan mitigation later but accepted for now within threshold).” This gives context that the system has been hardened to some extent.
Options:
Proceed (PASS): The prototype is robust enough to move on. Continue to Phase 5 (Quality evaluation).


Mitigate and Retest: If a significant issue was found but not fully resolved (e.g., a stubborn bug or a design flaw causing vulnerability), stay in Phase 4. The team should focus on fixing or adding safeguards, then rerun tests. Only proceed once fixed.


Revisit Design: If Phase 4 reveals a fundamental design weakness (for instance, the approach is inherently unstable for certain valid inputs), it might necessitate redesign or choosing the fallback design. This could mean going back to Phase 2 or 3 with adjustments, then coming through Phase 4 again.


Document & Defer: For some issues (like minor fairness discrepancies or rare edge cases) the team might document them and plan to address by Phase 9 (safety/human factors) if they are not blockers now. Gate C4 could still pass if those are truly minor and have an owner and timeline for resolution.


Stop: If the solution fails robust tests in a way that indicates it’s not viable or safe (and no reasonable fix is apparent), a stop or major pivot could be considered. For example, if the model always produces something dangerous with certain inputs that can’t easily be mitigated, that might halt the project.


Rationale Prompt: “Review Gate C4 results. Have all major robustness issues (crashes, invariants, security, misuse) been fixed? Describe any lingering concerns. If acceptable, confirm that the solution is robust enough to proceed. If not, explain what needs further work.”
Next-Step Instruction:
If PASS: Record the robustness testing outcome. Move to Phase 5 (Quality Proxies & Reality Checks), where the focus shifts to validating solution quality against requirements.


If FAIL (Mitigate): Log issues. Continue Phase 4 until resolved. Possibly call for additional expertise or tools to fix issues (like a deeper security review if fuzz found memory leaks, etc.). Then re-test and attempt gate again.


If FAIL (Revisit Design): Document that current design might be flawed in robustness. Possibly revert to fallback plan: implement that (Phase 3 for fallback) and then subject it to Phase 4 tests, or adjust architecture. This might effectively fork or branch (the original design might be parked or retired).


If Proceed with Known Issues: If passing with minor issues noted, ensure those issues are added to an issue tracker or ADR for later phases (especially Phase 9 or continuous monitoring if relevant). The Auditor should track that these are addressed by release.


Machine-Readable Metadata: Example for Gate C4:
{
  "run_id": "<RUNID>",
  "gate_id": "C4",
  "timestamp_utc": "2025-08-13T22:15:00Z",
  "decision": "PASS",
  "tests_summary": {
    "metamorphic_passed": 3,
    "property_tests": 5,
    "fuzz_inputs": 1000,
    "misuse_scenarios": 4,
    "fairness_issues": false
  },
  "issues_fixed": ["Crash on empty input", "Output negative on overflow - fixed range check"],
  "remaining_notes": "Slight accuracy drop on edge case inputs; logged for later tuning.",
  "rationale": "All critical robustness tests passed after fixes. No crashes or high-severity bugs remain. Minor edge issues will be handled in Phase 5/9."
}

This gives a count of tests and fixes, documenting that the gate was passed after addressing important points.
Source: Phase 4 outputs and Gate C4 criteria.

Phase 5 — Quality Proxies and Reality Checks
Objective: Before optimizing, ensure the solution’s core quality metrics meet minimum requirements (quality floors) and that results make sense in reality. Phase 5 evaluates the solution on validation datasets or real-like data to see if it’s on track to solve the problem in a meaningful way.
LLM Prompt (Phase 5):
Enter Phase 5 (Quality Proxies & Reality Checks). Evaluate the solution’s quality:
Compute Primary & Secondary Quality: Run the prototype on a validation dataset or a justified synthetic test set and measure the primary quality metric, as well as secondary metrics if any. Compare these results to the acceptance criteria (the quality floor or SLO targets). Ensure the dataset used is representative enough or has known difficulty.


Independent Cross-Check: If possible, use an independent method or evaluator to double-check the outputs. For example, if the system is a model making predictions, have a separate evaluation script or a human review a sample to validate correctness. Or use an alternative calculation to verify outputs. This helps catch any systematic errors (sanity check).


Baseline Comparison: Compare the solution’s outputs/metrics against the baseline solutions and SOTA identified in Phase 1 on the same test cases. Document how much better (or worse) the prototype is currently vs. those baselines for each key metric. If it’s worse or only on par, note that clearly.


Explain Divergences: For any cases where the solution output differs significantly from the baseline or expectation, analyze why. E.g., if our solution did worse on a particular subset or had weird outputs, provide hypotheses or debug those cases.


Error Bars & Uncertainty: Estimate the uncertainty or variability in the quality metrics. If possible, compute error bars (e.g., standard error or confidence intervals) or do a quick sensitivity analysis: how sensitive are outputs to slight input changes or parameter changes? This gives a sense of reliability.


Parameter Sensitivity: If the solution has key parameters or hyperparameters, do a coarse check of their impact. For example, run with a different seed or slightly different configuration to ensure no huge swings in performance (unless expected).


Document Results: Log the results of this quality evaluation. If quality floors (minimum acceptable performance) are not met, flag that. If any surprising result came up, note it. Add an entry to the ledger with current metrics and any decisions (e.g., to proceed or to do further tuning now).
 Provide the measured performance (with error estimates) on primary metrics, comparison to baselines, and any issues discovered as outputs for Gate C5.


Procedure: The team runs the prototype on a reasonably sized validation set (could be a subset of real data withheld for testing or a high-quality simulated set). They measure the primary metric (e.g., accuracy, error rate, response quality, etc.) and check it against the quality floor defined in the Domain Profile. Secondary metrics (like latency, throughput in a non-optimized state, or secondary quality measures) are also noted. They cross-verify outputs either through a manual check or alternative approach to catch anomalies. They then line up these results next to baseline results from Phase 1. If the prototype is not yet beating the baseline or meeting the SLO, that’s okay at this phase, but it should at least meet the “quality floor” (minimum usable quality). They examine any large deviations or fails (for example, maybe on some category of input, performance is much worse than baseline – they try to reason why). They compute approximate error bars, for instance by looking at performance on different data splits or using bootstrapping if possible. Also, perhaps run the system with a few different seeds or small parameter tweaks to see if the metric varies widely, which would indicate instability. All findings are documented. If the quality is below acceptable levels, this phase might trigger adjustments (like improving training, tweaking algorithms, or even going back to drawing board if it's fundamentally too low).
Gate C5 — “Quality Sufficiency”
Objective: Confirm that the solution’s quality is on track and at least meets the minimum acceptable levels (quality floors), and that any differences from baseline are understood. Essentially, ensure we’re not proceeding with something that isn’t working.
Pass Criteria: Gate C5 passes if:
The primary quality metric meets or exceeds the pre-defined floor (minimum acceptable level) on the validation tests. If the quality is below the floor, the solution isn’t sufficient yet.


Any deviations or regressions relative to baseline are explained and acceptable. For instance, if baseline method actually outperforms our prototype on some aspect, we either have a plan to address that or a conscious decision to accept it (with reason).


The quality results make sense given the problem. No glaring issues like the model doing well on average but catastrophically failing certain cases without reason (unless discovered in Phase 4 and deferred).


If there were quality-related kill criteria defined (Phase 1’s kill criteria might say “if novelty doesn’t give X improvement by now, stop”), check those. If any kill criterion is triggered (e.g., “project fails if accuracy < 90% but it’s 85%”), then this gate would fail unless overriding with explicit approval.


All outputs differences vs baseline have been justified or mitigated. (E.g., “Our solution is slower than baseline currently, but we haven’t optimized yet – acceptable for now,” or “We have slightly lower quality on one rare class, will fix in Phase 7 fairness tuning.”)


Context Digest: Summarize the measured quality: e.g., “Primary metric = 0.82 (floor was 0.80, baseline was 0.78) – so we beat baseline modestly and meet floor.” Note any secondary metrics: “Throughput is currently lower than baseline (because unoptimized) but within tolerance for now.” Highlight if any quality criteria are not yet met and what the plan is (maybe needing more training, data, etc.). Confirm that overall the solution appears viable quality-wise.
Options:
Proceed (PASS): Quality is sufficient. Move to Phase 6 (Performance Benchmarking).


Iterate on Quality: If quality floors are not met, do not proceed. The team may need to improve the model/solution now – e.g., refine training, add data, adjust algorithms – and re-evaluate quality. Essentially stay in Phase 5 until either it meets the floor or it's concluded that it cannot. Minor shortfalls might be allowed if there's strong evidence we can fix them later, but that’s risky unless justified.


Adjust Targets (AMEND): If the quality is below target but the team has evidence that original targets were too strict or unrealistic, they could consider an AMEND to revise the acceptance criteria – but this requires approval and evidence. For example, “We aimed for 95% accuracy, but industry state-of-art is 90%; we currently have 88%. Perhaps adjust target to 90% after demonstrating that’s near upper bound.” This must go through governance (Auditor sign-off with rationale). If approved, floor is adjusted and gate can pass given new threshold.


Stop: If quality is far from acceptable and no clear path to improvement, the project might be halted. Or perhaps fallback design could be tried if primary underperforms. This is where a kill criterion triggers a stop. A No-Go brief would note “Quality not sufficient to justify continuation.”


Branch: In rare cases, if one aspect of quality is problematic, a specialized branch could be spun to handle it (for example, a branch to develop a particular module to improve a secondary metric without slowing main work). But usually, one would just iterate rather than formal branch here.


Rationale Prompt: “Assess Gate C5. Does the solution meet the minimum quality requirements? Provide current metric values vs goals. If below, is there a plan or should we stop? If above, confirm that quality is sufficient to proceed to performance optimization.”
Next-Step Instruction:
If PASS: Record that quality is acceptable. The RCO signals Phase 6 (Benchmarking & Performance) to begin, shifting focus to efficiency and performance.


If FAIL (Improve Quality): Note what aspects failed. The team should acquire more data, tune models, adjust methods, or possibly incorporate elements of other designs, then re-run Phase 5 evaluation. Only move on when quality floor is reached.


If AMEND Threshold: If an adjustment is made to the target, the Auditor must sign off (recorded in an ADR and ledger). After adjustment, re-evaluate if current quality passes the new threshold. If yes, proceed (with caution that this was done).


If Stop: Log the decision. Provide a No-Go or pivot brief (maybe pivot to a simpler solution or to solving a different problem if partial success indicates a different direction).


If Fallback/Branch: If the fallback design might yield better quality, perhaps pause primary, build out fallback quickly (Phase 3/5 for it) and compare. This could be done as an experiment branch. Then choose path with better outlook.


Machine-Readable Metadata: Example for Gate C5:
{
  "run_id": "<RUNID>",
  "gate_id": "C5",
  "timestamp_utc": "2025-08-13T23:00:00Z",
  "decision": "PASS",
  "primary_metric": 0.82,
  "primary_metric_floor": 0.80,
  "baseline_primary": 0.78,
  "secondary_metrics": {"precision": 0.80, "recall": 0.85},
  "met_floor": true,
  "vs_baseline": "better",
  "rationale": "Primary accuracy 82% exceeds floor (80%) and baseline (78%). Secondary metrics acceptable. Quality sufficient to proceed."
}

If it had failed, met_floor would be false and we might include an explanation or plan field.
Source: Phase 5 outputs and Gate C5 criteria.

Phase 6 — Benchmarking with Statistical Rigor
Objective: Measure the solution’s performance (speed, efficiency, resource usage) rigorously, controlling for variance and capturing tail behavior. This phase focuses on obtaining reliable performance metrics under standardized conditions.
LLM Prompt (Phase 6):
Begin Phase 6 (Performance Benchmarking & Statistical Analysis). Benchmark the system thoroughly:
Benchmark Suites: Define and run a suite of performance tests. This includes measures of latency and throughput (for typical and worst-case scenarios), memory usage (peak and sustained), and any relevant domain-specific performance (e.g., frame rate if applicable, or transaction throughput). If the system has a real-time requirement, include jitter or dropout rates.


Noise Controls: Ensure consistency in the benchmarking environment. Pin CPU affinity or set process priorities to reduce noise, fix number of threads, disable frequency scaling if possible, and run warm-up iterations to stabilize caches/JIT compilers. Ensure each test runs for a minimum time (e.g., ≥5 seconds) to average out fluctuations. Also isolate background processes if possible.


Replication & Seeds: For each benchmark scenario, run multiple repetitions (N times) and, if the process is stochastic, use multiple different seeds. Risk tier dictates N (see default thresholds: R1≥15, R2≥30, R3≥50 replications) and number of seeds (R1≥5, etc.) to capture variance. Collect all these runs' data.


Statistical Analysis: Calculate summary statistics. For each metric (latency, etc.), compute geometric mean and median, and 95% confidence intervals (or appropriate CI for distribution). Use a non-parametric test (e.g., Mann-Whitney U for medians) to compare distributions (especially vs baseline performance). Note p50, p95, p99 values for metrics to understand tail performance. For real-time systems, measure jitter.


Significance Check: Determine if performance differences (between our solution and baseline, or between versions) are statistically significant at α ≤ 0.05. If not, consider it essentially “no improvement” unless practical significance is argued. Mark results that are significant.


Document Raw Data & Stats: Save the raw timing/usage logs (e.g., CSV files for each run) and compile a Stats Report (JSON and human-readable text) with the computed medians, CIs, significance test results. These will form artifact F (Statistical Benchmark Report).


Update Ledger: Append an event with summary statistics and note if performance meets expectations or if issues were found.
 Provide the aggregated benchmark results (with medians, p95/p99, CI, significance) and highlight any performance issues as outputs for Gate C7 and C7.Sigma.


Procedure: The team sets up controlled benchmarking runs. They likely use tools or scripts prepared in Phase 3 harnesses but now ensure that external variability is minimized. They run, say, the solution on a set of test inputs repeatedly to get timing, memory usage, etc. They also run baseline solutions under identical conditions for direct comparison (if relevant). They gather a large sample of timings. They follow the risk-tier guidelines for how many replicates and seeds to use (e.g., for moderate risk, run each test 30 times, using 10 different random seeds if the algorithm has randomness, etc.). After collecting data, they calculate median, mean, tail latencies (95th percentile, etc.), and use statistical tests to see if differences are real. For example, if new solution median latency is 100ms vs baseline 120ms, they check if that difference is statistically significant across runs. They pay attention to outliers and variability. The results and methodology are documented in the Stats Report artifact. They ensure the environment details (hardware, CPU governor, etc.) are recorded, possibly adding to the environment fingerprint if needed. This phase doesn’t itself decide pass/fail except as feed into gates, but ensures data is ready for gating.
Gate C7 — “Benchmark Hygiene”
Objective: Verify that the benchmarking was conducted properly and meets the protocol’s standards (sufficient replications, controlled conditions, tail metrics reported).
Pass Criteria: Gate C7 is about the process of benchmarking rather than the result values. It passes if:
The benchmarks include enough runs and seeds as per thresholds (or justified if slightly different). (E.g., "We did 20 replications, which is above R1 minimum of 15.")


Noise controls were in place: evidence that CPU pinning/affinity was used, warm-ups done, etc. Basically, we trust the data isn’t skewed by random OS fluctuations.


Tail metrics (p95, p99) and variance measures are captured, not just an average.


The environment (hardware/software) for benchmarks is clearly documented, so results are reproducible on the same setup.


Raw data is saved and a Stats Report is generated.


If any of these aspects is missing, it's a fail. The aim is to ensure rigorous benchmarking "hygiene."


If all conditions are met, Gate C7 passes.
Context Digest: Summarize how the benchmarking was performed: e.g., “Benchmarks run on dedicated machine (8-core CPU) with CPU affinity set, repeated 30 times per case, 10 seeds. Warm-ups done. We have median latency = X ms (p95 = Y), memory = Z MB, etc. Data recorded in stats_report.json.” This assures reviewers that the methodology was sound.
Options:
Proceed (PASS): If all methodology checks out. (Note: we might still wait for Gate C7.Sigma next, but logically if C7 passes and then significance will be checked.)


Fix Benchmark Setup: If something was done poorly (like too few replications, or forgot to fix CPU frequency leading to noisy data), fix and re-run benchmarks. This might be time-consuming but necessary for credible results. Then attempt gate again.


Adjust Risk Tier Requirements: Possibly the domain might allow fewer replicates if extremely time-consuming, but that would require an AMEND (lowering threshold needs dual approval). If done, record and justify it.


Proceed with caution: If environment had slight noise but results are still clear, one might proceed but note to refine later. However, GCP expects strictness here, so better to get it right now.


Stop: Unlikely to stop entirely just for benchmarking issues; you'd fix methodology instead.


Rationale Prompt: “Evaluate Gate C7. Were performance benchmarks run rigorously? Confirm that replication counts, seed sweeps, and noise controls are sufficient for reliable measurements. If not, what needs improvement?”
Next-Step Instruction:
If PASS: Acknowledge proper benchmarking. Immediately evaluate Gate C7.Sigma (the statistical significance of performance improvements), which is effectively part of this step.


If FAIL: Stay in Phase 6 to correct the benchmarking procedure: increase runs, adjust environment, etc., then regenerate data. After that, re-evaluate Gate C7 (and C7.Sigma).


If AMEND thresholds: If truly necessary (for example, running 50 replicates is infeasible due to long runtime, and project is risk-tier R3 requiring 50 by default), propose a threshold amendment (e.g., reduce to 30 replicates with justification that variance is low). Get approvals, update Domain Profile thresholds, and then if accepted, consider that requirement met.


Continue to C7.Sigma analysis once C7 is satisfied.


Machine-Readable Metadata: Example record for Gate C7:
{
  "run_id": "<RUNID>",
  "gate_id": "C7",
  "timestamp_utc": "2025-08-14T00:30:00Z",
  "decision": "PASS",
  "replications_per_case": 30,
  "seed_sweep_count": 10,
  "min_bench_time_s": 5,
  "tail_metrics_recorded": true,
  "noise_controls": ["CPU_affinity", "warmup_runs"],
  "rationale": "Benchmarking conducted with 30 reps & 10 seeds per test, CPU pinned, ≥5s runs. Collected median, p95, p99, CI for metrics. Data quality is good."
}

This shows the parameters of the benchmarking and confirms everything was done.
Source: Phase 6 outputs and Gate C7 criteria.
Sub-Gate C7.Sigma — “Statistical Significance”
Objective: Determine whether performance improvements are statistically significant (or practically justified). This sub-gate uses the statistical analysis from Phase 6 to evaluate if the solution’s performance advantage is real.
Pass Criteria: Gate C7.Sigma passes if:
The performance differences critical to the project’s value are statistically significant at α ≤ 0.05 (95% confidence), or if not, there is a strong argument for practical significance instead.


For example, if our solution’s median latency is 5% faster than baseline but p-value is 0.1 (not statistically significant with 30 runs), we either need to accept that it’s not a proven improvement or justify that 5% is practically meaningful enough and consistent to accept (maybe then one would gather more data to lower p-value, or if it's borderline, consider it risk).


Essentially, either p-value < 0.05 for improvements, or if p-value is higher, the effect size must be large enough and confidence interval tight enough to argue practical significance.


No performance regression should be ignored: if solution is slower or more resource-heavy than baseline beyond tolerance, and it's statistically significant, either mitigate or get an approved exception with rationale (e.g., we accept 10% slowdown for double accuracy, etc.).


In short: proven statistically or justified convincingly.


Context Digest: Summarize key stats: e.g., “Solution median latency = 95ms vs baseline 120ms, Mann-Whitney U test p = 0.03, so improvement is statistically significant. Throughput improvement is similarly significant. Memory usage is slightly higher but within acceptable range (no significance test needed).” If not significant: “Difference in X is not statistically significant (p=0.2) but effect size is small anyway, so we consider it essentially no improvement on that metric.”
Options:
Proceed (PASS): The performance gains (or required metrics) are statistically confirmed or otherwise justified as sufficient. Move to Gate C6.9 (additional adoption check) or Phase 7 next, depending on sequence.


Investigate More Data: If results are inconclusive (p-value too high), possibly gather more benchmarking data to reach a conclusion (increase N). If performance target is critical and we can’t confirm improvement, we might need to iterate on design to improve it.


Accept with Risk: If improvement is borderline but time is short, the team might proceed but mark this as a risk (maybe to be verified again after optimizations in Phase 8.5). However, GCP typically expects high confidence by now.


Pivot/Stop: If we expected a performance gain and it’s clearly not there (and not fixable), maybe pivot strategy (e.g., if minimal intervention had similar performance, maybe stick with simpler solution). Or stop if performance is a key value driver and we can’t achieve it.


Amend Requirement: In some cases, perhaps initial expectations for performance were too optimistic; one could amend targets if justified (again requiring approval and evidence that current performance is “good enough” for users).


Rationale Prompt: “Assess Gate C7.Sigma. Are the solution’s performance improvements statistically significant at the 95% level? Provide p-values or CIs. If not, can we still justify the performance as sufficient? Decide whether to proceed.”
Next-Step Instruction:
If PASS: Note that performance evidence is strong. Now proceed to Gate C6.9 (the field realism check, inserted after Phase 6 if sequence calls for it).


If FAIL (Inconclusive): Possibly run more benchmarks or refine performance in Phase 7 before claiming improvement. Don’t yet celebrate improvement; perhaps hold a technical review to decide if design changes needed for speed. Re-run analysis after changes or more data.


If FAIL (No improvement): If we cannot demonstrate performance benefit over baseline or meet performance requirements, we must decide to either optimize further (Phase 7/8.5) or accept that maybe this project’s value is not in performance. If performance was crucial to worthiness, this might violate original expected value; could trigger pivot or stop.


Document decision: for instance, “Proceed but note to optimize more in Phase 8.5 to achieve significance.”


Machine-Readable Metadata: Example for Gate C7.Sigma:
{
  "run_id": "<RUNID>",
  "gate_id": "C7.Sigma",
  "timestamp_utc": "2025-08-14T00:35:00Z",
  "decision": "PASS",
  "metrics": {
    "latency_ms": {"solution_median": 95, "baseline_median": 120, "p_value": 0.02},
    "throughput_ops": {"solution_mean": 1050, "baseline_mean": 1000, "p_value": 0.15}
  },
  "effect_sizes": {"latency_reduction": 0.21, "throughput_increase": 0.05},
  "practical_significance": "Throughput p=0.15 but 5% increase is minor; focus on latency improvement (significant).",
  "rationale": "Latency improvement 21% is statistically significant (p=0.02). Throughput gain 5% not significant (p=0.15) - considered negligible. Performance goals met via latency."
}

Here, it logs per metric whether differences are significant and notes the decision rationale.
Source: Phase 6 outputs and Gate C7.Sigma criteria.

Gate C6.9 — Field Realism & Adoption Feasibility (Checkpoint)
(This gate occurs after Phase 6, before scaling up in Phase 7, to validate practical adoption factors.)
Objective: Ensure the solution as developed so far can realistically be adopted, supported, and sustained in its intended context. This gate checks non-technical readiness: operations, support, compliance, etc., which are critical for field deployment.
Checklist Pass Criteria: Gate C6.9 uses a checklist of readiness items. All must be addressed (with “green” status) to pass:
Adoption Plan: There is a clear plan for how this solution will be rolled out and adopted by users/organization. This includes identifying who needs to change their behavior or process, incentives for adoption, a rollout strategy (phases, training, etc.), and success criteria for adoption.


Serviceability: A support and maintenance model is defined. E.g., who will support the system, target metrics like Mean-Time-To-Repair (MTTR) for issues, spare parts or data refresh schedules if applicable. Basically, can the system be kept running and fixed when broken?


Compliance Readiness: All privacy, licensing, and regulatory obligations are mapped to artifacts or processes. For example, if personal data is involved, we have a DPIA draft; if open-source is used, licenses are known and compatible (SPDX scan done); if in a regulated sector, we've identified what approvals might be needed.


Training & Materials: There are user guides, operator manuals, or training resources planned or in draft. This could be quick-start guides for end users, admin runbooks, or safety signage/procedures if physical. People who interact with it can learn how.


Total Cost of Ownership (TCO): There’s an analysis of ongoing costs for using this solution. That includes operational expenses: necessary headcount to operate/support, training costs, periodic audit or monitoring costs, hardware/cloud costs, etc. It should show the solution is economically viable to operate and not exceeding what stakeholders expect.


Non-Goal Guardrails: Explicitly document what is out of scope or not intended, to prevent scope creep. This means clear boundaries like “This system will not do X,” so stakeholders don’t later push it beyond safe/viable use.


All items must be in a satisfactory state (they don't all have to be fully completed documents, but plans and evidence should exist for each). If any is missing or clearly insufficient, the gate fails.
Context Digest: Summarize the state of each checklist item: e.g., “Adoption plan: prepared initial rollout strategy targeting two pilot teams, identified incentive (faster workflow for them). Serviceability: have on-call plan and support runbook drafted. Compliance: All open-source licenses checked (no issues), privacy impact assessed (DPIA in progress, no blockers so far). Training: user manual outline done, training session scheduled. TCO: estimated $50k/year incl. cloud and support staff, within acceptable range. Non-goals: documented to avoid expanding to unrelated tasks.”
Options:
Proceed (PASS): All adoption feasibility aspects look good or have concrete plans. Continue to Phase 7 (scaling and hardening).


Reframe or Add Work: If something like TCO looks too high, or no clear adoption plan exists, pause here. Possibly pivot to a simpler solution if this one seems too expensive or complicated to adopt (e.g., if minimal intervention was far cheaper and adoption-friendlier, maybe switch). Or do more work now: for instance, engage with potential users to refine adoption approach, or simplify system to reduce cost.


Stop: If it’s determined that despite technical success, the solution won’t be adopted (e.g., users won’t use it or operational burden is too high), the project might be halted. Issue a No-Go brief focusing on these non-technical reasons.


Minor Fixes: If one or two small items are missing (maybe training materials not yet written but will be by Phase 9), one could proceed but mark as action items. However, since checklist says “all required,” ideally do them now or ensure owners assigned.


Rationale Prompt: “Evaluate Gate C6.9. Does the project have a solid adoption plan, support model, compliance checks, training materials, TCO analysis, and defined scope limits? Identify any gaps and decide if we can proceed to scaling or need to address these first.”
Next-Step Instruction:
If PASS: Log that solution appears feasible to deploy and maintain. Proceed to Phase 7 (Scale & Security).


If FAIL (Fixable issues): Address them. For example, quickly draft missing documents (like a training guide outline or support plan) or adjust the solution to improve TCO (maybe simplify something to reduce cost). Possibly involve domain experts (like compliance officer) if needed. Re-run a mini-review of Gate C6.9 after fixes.


If FAIL (Reframe): It may mean we realize a heavy AI solution is not worth it when a process tweak (Minimal Intervention) could solve problem cheaper. That could pivot the whole strategy. Possibly return to Phase 2 to emphasize minimal design, or spin off a new approach.


If Stop: Document reasons in a No-Go brief so stakeholders see that while technically it worked, it wasn’t worth deploying (with evidence like “no user willing to adopt due to complexity/cost”). End project or maybe start anew with different problem.


Machine-Readable Metadata: Example for Gate C6.9:
{
  "run_id": "<RUNID>",
  "gate_id": "C6.9",
  "timestamp_utc": "2025-08-14T01:00:00Z",
  "decision": "PASS",
  "checklist": {
    "adoption_plan": true,
    "serviceability": true,
    "compliance_ready": true,
    "training_materials": true,
    "tco_analysis": true,
    "non_goal_guardrails": true
  },
  "rationale": "All field readiness checks green. Adoption plan in place with pilot users identified. Support runbook drafted. Compliance review shows no blockers. Training guide outline completed. TCO ~$50k/yr is acceptable. Non-goals documented to keep scope in check."
}

All checklist items are booleans indicating readiness; rationale gives context.
Source: Gate C6.9 criteria.

Phase 7 — Scale, Cost/Energy, Security & Provenance
Objective: Prove the solution works at scale, quantify its operational costs/efficiency, and secure the software supply chain. In this phase, the focus is on testing in scaled environments and finalizing security/provenance measures.
LLM Prompt (Phase 7):
Begin Phase 7 (Scaling & Hardening). Prepare the solution for production-level operation:
Scale/Soak Testing: Simulate or test the system under increased load and duration. Test at 1×, 2×, 3× the expected peak load (queries per second, users, throughput) to ensure it meets performance SLOs at scale. Observe p50/p95/p99 latencies under these loads, track error rates, and validate stability over time (soak test for extended period). Check that error budgets (allowable failure rates) are respected and the system remains stable without memory leaks or crashes.


Cost/Energy Measurement: Measure how much it costs to run the solution at scale. Compute cost per operation or per 1k operations (in USD) and energy consumption per operation (Joules), if possible. For energy, use actual measurements or estimates with documented method and uncertainty. Check memory usage stays within limits. Also do a sensitivity check: if input volume grows by 20%, how does cost scale?


Security/Provenance Hardening: Finalize supply chain security steps. This includes generating an SBOM (software bill of materials) listing all dependencies, verifying dependency integrity (checksums, signatures), enabling code signing or attestations for the build, and ensuring the build is reproducible (document steps and test that a fresh build yields same results). Run security scans: Static App Security Testing (SAST) on code, Dynamic AST on running service if applicable, secret scanning for credentials in code, dependency vulnerability scan (CVE check). Prepare a provenance graph showing sources of all components.


CVE Policy & Exceptions: Review any vulnerabilities found (CVE reports). Address or patch critical/high vulnerabilities. If any are not fixable now, prepare an exception with dual-approval and mitigation (e.g., “using library X v1.2 with CVE Y because no alternative; risk accepted by security officer”).


Attack Trees (for R3): If risk tier is R3 or otherwise high security, complete an attack tree analysis. Enumerate potential attacker goals and paths, verify that each is mitigated by some security control or test. Ensure these mitigations are tested or included in runbook.


Operations & Runbook: Finalize the operations materials. This means update the runbook with all necessary information: how to monitor the system, SLOs/SLAs and alerting thresholds, a rollback plan (already partly done by Phase 10 planning), incident response templates, on-call rotations, escalation paths. Verify that someone operating the system would have all needed info to handle incidents.


Ledger Update: Append logs of scale test results, security scans, and provenance outputs to the ledger.
 Provide the results of scale tests (throughput, latency at 3× load, etc.), cost per operation, an SBOM and summary of security checks, and note any remaining security exceptions as outputs for Gate C7.5.


Procedure: The team runs large-scale tests on either a staging environment or using load testing tools. They confirm the system can handle at least the expected load and some margin above (2×, 3×) with acceptable performance. They measure long-run stability (maybe run it continuously for several hours) to see if any resource leaks or degradation occur. They measure actual cloud resource usage or machine power consumption to estimate cost and energy. Meanwhile, the engineering team completes security tasks: generating an SBOM (perhaps using a tool like Syft or CycloneDX), performing static code analysis and dynamic testing to find vulnerabilities or secrets, and ensuring all dependencies are pinned and scanned. They gather any CVEs and either update libs or document acceptance if needed. If in R3, they do a formal attack tree exercise or threat model session to list attack vectors and ensure mitigations (like authentication, input validation, etc.) are in place. They update the support runbook with any new findings (like add steps for certain alerts, or note how to verify signatures of components). The phase ends with documentation of results: e.g., the SBOM goes into SBOMs/ directory, vulnerability scan report filed, runbook updated in SafetyDocs/ or Artifacts/, and scale test logs perhaps saved in Benchmarks/.
Gate C7.5 — “Scale/Cost/Security”
Objective: Confirm that the solution is ready for deployment from a scale and security standpoint. This gate ensures it meets performance targets at scale, has integrity safeguards, and operational support is ready.
Pass Criteria: Gate C7.5 passes if:
The solution meets its scale targets: At expected peak load (and a bit beyond), it operates within acceptable response times and error rates. Essentially, Phase 7 scale tests show it can handle production volume. If any capacity shortfall was found, mitigations (like scaling out, adding resources) are identified.


Cost/Energy targets met: The cost per operation or overall cost is within the budget (cost_ceiling_usd in Domain Profile), and energy usage is within targets. If not, there's a plan (like optimize or get hardware) or a conscious decision to accept higher cost with approval.


Security integrity complete: SBOM is generated, all components are accounted for; all critical and high vulnerabilities are resolved or have signed exceptions. There are cryptographic signatures or attestations for the build, demonstrating provenance (meaning we can trust the build).


All required security tests (SAST/DAST/secret scan) have been executed, and any findings addressed or accepted formally.


If risk tier R3, the additional requirements (FMEA, STPA from earlier, attack trees, canary/rollback default on, etc.) are done as required. Specifically here, attack tree mitigations verified.


Ops readiness: The runbook is complete enough (maybe final touches will be in Phase 9, but at least outlines are there including rollback and incident templates).


Summarily: performance scale ✔, cost ✔, security ✔, ops ✔.


Context Digest: Summarize results: e.g., “At 3× expected load, throughput = 300 qps, p99 latency = 800ms (SLO was 1s, so OK). No crashes in 8-hr soak. Cost per 1k ops = $0.05, below budget. SBOM done (100 deps), 2 high vulns patched, 1 medium accepted. All code signed. SAST/DAST found no critical issues (report filed). Runbook updated with on-call rotation and rollback steps.” This indicates readiness.
Options:
Proceed (PASS): The system is ready for final productization and release steps. Move to Phase 8 (Productization & Interface Freeze).


Fix and Retest: If something fails (e.g., can’t handle load, or a major security hole discovered), address it now. Possibly optimize code or add servers for scale, patch security issues, etc., then re-run relevant tests. Gate C7.5 should not pass until these are resolved.


Accept Risk via Governance: If there’s a known issue we cannot fully fix now (like a cost slightly above budget or a moderate vulnerability with no fix available), one could get an approval to proceed with that risk accepted, but it must be documented and likely addressed later or monitored. E.g., sign off that cost is 10% over now but plan to optimize in Phase 8.5 or re-negotiate budget. Or accept a moderate CVE with compensating controls. This should be accompanied by an ADR or risk memo.


Stop/Pause: Unlikely to stop here if earlier gates passed, but if e.g. security is a showstopper (like discovered it’s impossible to secure due to fundamental issue), it could theoretically stop. More likely, fix rather than stop.


Branch: If performance at scale requires a different architecture (like current architecture can’t scale, need a redesign), that might trigger a branch or major refactor, but then you'd essentially go back to earlier phases.


Rationale Prompt: “Assess Gate C7.5. Does the system meet scale and performance requirements? Are SBOM, security scans, signing complete with no unresolved critical issues? Is the operations plan in place? If all good, proceed. If any gap, explain and address before continuing.”
Next-Step Instruction:
If PASS: Note that we have achieved scale and security readiness. Proceed to any pre-Phase 8 gates (like Gate 8.4 Simplicity, Gate 8.5 Optimization, which come next) or directly to Phase 8 if those were already done. In sequence, after 7.5, next is Gate 8.4 Simplicity.


If FAIL: Remain in Phase 7. Tackle the deficiency: e.g., tune system or add caching for scale, reduce cost by adjusting infrastructure, fix security holes, etc. Possibly involve other teams (security team for pen-test, etc.). Update artifacts (SBOM, etc.) and retest. Then re-evaluate gate.


If Defer minor issues: If something small like documentation incomplete, you might pass gate but ensure it's done in Phase 9. But significant items (like unresolved high CVEs) cannot be deferred without proper sign-off.


Document all final adjustments in the ledger and proceed accordingly.


Machine-Readable Metadata: Example for Gate C7.5:
{
  "run_id": "<RUNID>",
  "gate_id": "C7.5",
  "timestamp_utc": "2025-08-14T02:00:00Z",
  "decision": "PASS",
  "scale_results": {
    "peak_load_qps": 300,
    "p99_latency_ms": 800,
    "error_rate": "0.1%"
  },
  "cost_per_1k_ops_usd": 0.05,
  "within_budget": true,
  "sbom_completed": true,
  "vuln_status": "No high vulns (2 patched, 1 med accepted)",
  "signing_attestation": true,
  "ops_runbook": "Completed",
  "rationale": "System handles 3x load within SLO. Running cost is under budget. SBOM and signing done; all critical vulns resolved. Ops materials are ready. Ready for productization."
}

This shows scale testing metrics and security/ops completion status.
Source: Phase 7 outputs and Gate C7.5 criteria.

Gate 8.4 — Simplicity (Pre-Productization)
(This gate occurs before final productization to ensure the design is as simple and maintainable as possible.)
Objective: Remove unnecessary complexity and ensure the codebase is clean and minimal before freezing public interfaces. It's a final refactoring/cleanup checkpoint.
Procedure (8.4.x): The team assesses code complexity metrics and cleans up:
Compute maintainability indices (like cyclomatic complexity, cognitive complexity) for modules. Possibly use static analysis tools to get these metrics.


Remove dead code and unused dependencies. Ensure no orphan code or libraries remain. The dependency graph is minimized to only what's needed.


Check duplication across code: ensure duplication index ≤ 5% (meaning very little copy-paste or redundant logic). If above threshold, refactor into common modules or justify why not (maybe duplication for performance might be allowed if documented).


Audit public APIs (if any): ensure only intended functions/classes are exposed in the final package. Hide or remove any dev/test interfaces not meant for users.


Conduct a design review focusing on simplicity: a knowledgeable reviewer (perhaps someone from outside the core team) reads through architecture and confirms no over-engineering. This is captured as a “reviewer note” and possibly an ADR if any decisions to simplify design further.


Document any complexity that remains with justification (ADR or code comments).


Pass Criteria: Gate 8.4 passes if:
Complexity metrics are within thresholds (e.g., duplication index ≤ 5%, other complexity measures at acceptable levels), or any exceedance is justified and documented in an ADR.


All obvious opportunities to simplify have been taken. The code has no large sections of unused code or needless layers.


The design reviewer signs off that the design is as simple as it can be without losing functionality (not just cosmetic changes, but actual simplification).


Public interface is trimmed to only what’s necessary and intended.


If any complexity is kept for a reason (like performance hacks), there's documentation for it.


Context Digest: Summarize what was done: e.g., “Removed 10% of code as dead/unused, dropped 2 libraries not needed. Current duplication index ~3%. Cyclomatic complexity average < 10 per function, maintainability high. Only intended API endpoints are exposed (others made internal). Reviewer confirms design is straightforward with no excess features.”
Options:
Pass: If metrics good and reviewer happy. Continue to Gate 8.5 (Optimization).


Amend/Fail: If thresholds not met (e.g., duplication 8%), either refactor more to reduce it or if not feasible, write an ADR explaining why it's acceptable (maybe the 8% duplication is test code or something). If not justified, that’s a fail - do more cleanup.


Possibly, not passing here would rarely cause a full stop, but it can delay productization until cleaned.


If the design is overly complex by nature, one could consider a heavier refactor or in worst case pivot to simpler approach, but by now that’s unlikely.


Rationale Prompt: “Evaluate Gate 8.4. Is the solution’s design as simple as possible now? Provide any code complexity metrics and confirm dead code removal and minimal public API. If everything is lean and intentional, proceed. If there's unjustified complexity, address it before release.”
Next-Step Instruction:
If PASS: Document the simplicity achievements (maybe produce an ADR that states final complexity status). Proceed to Gate 8.5 (targeted optimization).


If FAIL (excess complexity): Clean up code further. Possibly schedule an extra refactoring sprint to remove complexity. Re-run complexity analysis and attempt gate again.


If ADR Exception: If some metric is beyond threshold but you decide to accept it (with signatures), record that in an ADR and maybe get Auditor sign-off (since threshold lowering needs dual approval normally, but this might be a minor internal threshold). Then pass gate with noted exception.


Possibly minor cosmetic stuff can be deferred but recommended to do now before freeze.


Machine-Readable Metadata: Example Gate 8.4:
{
  "run_id": "<RUNID>",
  "gate_id": "C8.4",
  "timestamp_utc": "2025-08-14T03:00:00Z",
  "decision": "PASS",
  "duplication_index_pct": 3.0,
  "max_cyclomatic_complexity": 12,
  "dead_code_removed": true,
  "public_api_symbols": 5,
  "reviewer_note": "Design simplified; no extraneous components. All complexity justified.",
  "rationale": "Codebase cleaned and simplified. Duplication 3% < 5% threshold. No dead code or unnecessary deps. Only intended 5 API functions exposed. External review confirms simplicity."
}

Source: Gate 8.4 criteria.

Gate 8.5 — Optimization (Pre-Productization)
(This gate focuses on performance optimization without regressing correctness, after all functional work is done.)
Objective: Achieve targeted optimizations for performance (speed, cost, energy) with statistical proof, ensuring no regressions in quality.
Procedure (8.5.x): The team profiles the system and optimizes:
Profile the system using appropriate tools (CPU profilers like perf or VTune, GPU profilers, memory profilers). Identify bottlenecks (which functions or steps consume most time or energy). Possibly look at a roofline model if HPC-related.


Apply targeted optimizations to address these bottlenecks. This could mean algorithm improvements, parallelization, using more efficient libraries, caching results, etc. Each change should be documented with before/after measurements to quantify its effect.


Ensure none of these changes break correctness: re-run the test suite, verify quality metrics remain above floors (no accuracy regression). Quality floors must remain intact.


After optimizations, re-run the benchmarking (like Phase 6) to measure improvements. Particularly regenerate the Stats Report focusing on performance metrics.


Update the performance Pareto data: If multiple configurations or trade-off points exist, update the table of performance vs quality to see if a new optimal point was chosen. For instance, maybe one optimization improves speed at cost of slight memory increase; record that. Mark which configuration is chosen as final (selected_point_flag).


If no significant speedup was achieved or improvements come at cost of complexity, consider the “Stop Card” rule: if the attempted optimization yields < X% improvement and increased complexity, consider abandoning it (i.e., do not accept complexity for tiny gain unless dual-signed value case says it's worth it).


Finalize an ADR documenting the optimizations and their impact, and append to ledger.


Acceptance Criteria: Gate C8.5 passes if:
The optimizations deliver statistically proven performance gains (or cost/energy reductions) over the prior baseline. The improvements should be backed by data with significance analysis (like before vs after p < 0.05 or clearly better effect size).


No regressions in correctness or quality: all quality floors still met and no new bugs introduced.


If an optimization didn’t give meaningful improvement, it’s either rolled back or justified as needed for perhaps maintainability. But basically the focus is that any included optimization provides value.


The team has selected a point on the performance vs cost/quality Pareto frontier and recorded it. The chosen trade-off (like how much speed vs resource usage) is documented and makes sense.


Pareto selection recorded in ledger and ADR (they likely updated artifact G Perf Pareto CSV and maybe wrote an ADR on final trade-off choice).


If some optimization made things worse or negligible, the protocol expects you remove it (don’t add unhelpful complexity), unless there's a dual-signed rationale to keep for future potential.


Context Digest: Summarize what was achieved: e.g., “Profiled and optimized critical loop; gained 15% speed-up. Memory usage reduced by 10%. No accuracy change. Stats: median latency improved from 95ms to 80ms (p<0.01). All tests pass. Selected final config with this optimization. Documented trade-offs: slightly higher CPU usage for lower latency, acceptable.” If any stop card decision: “We attempted parallelization, but it added complexity for only 2% gain, so per Stop Card guidelines, we dropped that optimization.”
Options:
Pass: Gains achieved, no harm done. Proceed to Phase 8 (final productization steps).


Fail (try more): If targets not met (e.g., maybe had a goal to reduce latency by X% to meet a realtime target and not there yet), possibly do another round of optimization or consider hardware changes. If cannot improve further easily, decide if current state is acceptable or if constraints must be adjusted.


Possibly, if optimization efforts risk destabilizing system or are hitting diminishing returns, one might accept current performance. Or escalate (like require more engineering or specialized help).


Drop unsuccessful optimizations: Ensure any attempt that didn’t pan out is removed so as not to complicate maintenance.


It's rare to stop the whole project here unless performance was absolutely critical and failed badly. More likely, adjust expectations or plan improvements post-release if minor.


Rationale Prompt: “Evaluate Gate C8.5. Did we achieve meaningful performance improvements without breaking anything? Provide before/after performance metrics and confirm quality still OK. If yes, approve final optimization. If not, consider further tuning or accept current performance as is.”
Next-Step Instruction:
If PASS: Note final performance metrics in the ledger and proceed to Phase 8 (Surface Freeze and productization). Actually after 8.5, the next step according to sequence is Phase 8 and Gate C8.


If FAIL (optimize more): Possibly allocate time for deeper optimizations or consider out-of-scope improvements (like requiring different hardware, which might not be in initial plan). Could also be that no further improvements can be done with current approach – if performance is below requirement, might need to reconsider design or accept lower performance (with stakeholder approval). That would be an AMEND to acceptance criteria.


Document the final decision and proceed accordingly.


Machine-Readable Metadata: Example Gate C8.5:
{
  "run_id": "<RUNID>",
  "gate_id": "C8.5",
  "timestamp_utc": "2025-08-14T04:00:00Z",
  "decision": "PASS",
  "optimization_summary": {
    "latency_before_ms": 95,
    "latency_after_ms": 80,
    "p_value": 0.001,
    "quality_regression": false,
    "stop_card_invoked": false
  },
  "pareto_tradeoff": "Chose config with 80ms latency, $0.05/1k ops cost, slight +5% CPU use.",
  "rationale": "Targeted optimizations yielded ~15% latency improvement (95->80ms, p=0.001) with no accuracy loss. All tests pass. Final configuration balances speed and cost optimally."
}

Source: Gate 8.5 criteria.

Phase 8 — Productization, Compatibility, Surface Freeze
Objective: Finalize the solution as a product: define stable interfaces (API/CLI), lock down configurations, ensure backward compatibility (if applicable), and “freeze” the public surface. Essentially, package the solution for external use.
LLM Prompt (Phase 8):
Begin Phase 8 (Productization & Interface Freeze). Finalize the product details:
Minimal API/CLI: Define the final public API endpoints or command-line interface for the solution. Specify function signatures, input/output formats, error codes, and timeouts. Ensure they are minimal and sufficient (no unnecessary complexity). Document these clearly (this becomes part of user-facing docs).


Configuration System: Implement or finalize a configuration mechanism. This includes how users can set parameters, with typed configuration options, default values, and a way to reproduce runs via config (e.g., a config file or flags). Ensure that all magic numbers or tunables in code are exposed or fixed as needed for reproducibility.


Telemetry Dictionary: Define what telemetry (logs/metrics) the system will emit in production. For example, log formats, metric names and units, and any tags for tracing. Annotate any telemetry with privacy considerations if needed (no personal data in logs unless consented, etc.). Document this for operators.


Compatibility Tests: If there was a previous version or if maintaining backward compatibility, run tests to ensure this version does not break existing integrations. For example, test that any input-output contracts remain the same or that deprecated features still behave for now. If this is initial version (v1.0), then establish a baseline of tests to preserve compatibility in future.


Surface Freeze: Officially “freeze” the public interface. This means from this point, any change to API/CLI or config that would break users needs a version bump (according to semantic versioning) and deprecation process. Document that the interface is now stable in an ADR. Set up a version tag (like v1.0.0) for this release.


Runbook Updates: Finalize any remaining runbook sections now that interface is final (like add troubleshooting for specific error codes, update screenshots if CLI output included, etc.). Append to ledger.


Ledger: Log that surface freeze occurred at this version and attach compatibility test results.
 Provide the final API/CLI specification, config schema, telemetry spec, and note that interface is frozen (with version number) as outputs for Gate C8.


Procedure: The team defines the public-facing aspects clearly. They likely create an “API Spec” document and possibly generate examples or schema (like OpenAPI spec if it's an API, or usage docs if CLI). They ensure that config files or environment variables are all listed and have defaults, etc.. They verify or add tests to make sure these interfaces work as expected (and to serve as future regression tests). If an earlier version exists (like maybe a minor earlier prototype used somewhere), they run compatibility tests to ensure no break, or decide to bump major version if breaks exist. They then mark this version as freeze (perhaps by tagging code in repo and noting in documentation that this is the stable interface). They incorporate any slight adjustments needed to finalize (like maybe unify naming conventions for parameters). They update documentation and the runbook accordingly. The freeze means no one should change function signatures etc., except via formal versioning going forward. This is recorded likely in an ADR or version release notes.
Gate C8 — “Release Interface Freeze”
Objective: Ensure the product’s external interface is complete, well-defined, and stable. Gate C8 checks that we’re ready to hand this to users or external systems with a guarantee of stability.
Pass Criteria: Gate C8 passes if:
The API/CLI and configuration are fully specified and implemented. There are no “TODOs” left in how someone uses the system.


The interface is minimal but sufficient: no extraneous endpoints or options beyond what’s needed (keeping attack surface and maintenance surface small).


Compatibility tests (if any apply) all pass: meaning we didn’t break previous contracts or we bumped version appropriately.


The “surface” (public interface) is frozen: any changes are now gated by versioning policy. This is recognized and documented.


Telemetry outputs are defined and in place (so operations can monitor the system).


Essentially the product is ready to be packaged for release.


Context Digest: Summarize: “API endpoints: 3 endpoints finalized (list X, get Y, update Z), CLI tool supports these 3 commands with described options. Config is via YAML file with schema documented. Telemetry includes request count, latency, error codes. All interface elements tested. Marking version 1.0.0 frozen – any further interface changes require new version. Compatibility tests show no break from v0.9 (or not applicable since first release).”
Options:
Proceed (PASS): Interface locked in. Move to Phase 9 (Packaging, Safety, etc.).


Fail (complete work): If something is incomplete (maybe documentation not finished, or found an issue in API design last minute), fix it now. Possibly iterate design slightly if needed (but that’s late; ideally this is final polish). If a compatibility test failed and indicates a break, decide to either restore compatibility or accept a breaking change and bump major version accordingly before release.


Not much scope for alternative actions beyond finishing the tasks, since at this point it’s largely paperwork and polish if not done.


Rationale Prompt: “Evaluate Gate C8. Is the external interface (API/CLI/config) fully defined and stable? Are compatibility or regression tests passing? Confirm that version is set and interface is frozen for this release.”
Next-Step Instruction:
If PASS: The product definition is complete. Proceed to Phase 9 (Release Packaging & Safety Checks).


If FAIL: Wrap up whatever is pending. That might delay the release slightly but better than releasing a half-baked interface. Then re-check and pass.


Record the final version number and proceed.


Machine-Readable Metadata: Example Gate C8:
{
  "run_id": "<RUNID>",
  "gate_id": "C8",
  "timestamp_utc": "2025-08-14T05:00:00Z",
  "decision": "PASS",
  "api_endpoints": 3,
  "cli_commands": 3,
  "config_schema": "YAML, 10 options",
  "telemetry_defined": true,
  "version": "1.0.0",
  "compatibility_tests": "N/A (first release)",
  "rationale": "Public API & CLI finalized (3 endpoints/commands). Config schema locked. Telemetry metrics listed. Marking version 1.0.0; interface frozen going forward."
}

Source: Gate C8 criteria.

Phase 9 — Release Packaging, Safety/Privacy, Human Factors
Objective: Package the solution for release, complete all safety/privacy documentation, and validate human factors (usability, explainability, training). This is the final readiness check before field deployment.
LLM Prompt (Phase 9):
Begin Phase 9 (Final Release Preparation). Complete remaining tasks for a responsible release:
Full Checkpoint Build: Create a final Checkpoint bundle with all artifacts and manifests. This includes a manifest.json listing content and hashes, code at release commit, data manifests, config files, compiled binaries if any, etc. This checkpoint should be reproducible and signed. Essentially, the final release bundle.


Safety & Privacy Artifacts: Finalize all safety documentation. Prepare a Model Card (if ML model) or similar documentation including intended use, limitations; Data Card for any data; the completed DPIA (Data Protection Impact Assessment) if personal data is involved; a “misuse case” analysis memo (how the system could be misused and what mitigations or warnings are in place); fairness assessment results (from Phase 5) summarized (any deltas or biases and mitigations). If risk tier R3, complete an Assurance Case (Goal Structuring Notation) linking identified hazards to implemented controls to evidence (basically a formal argument that system is safe/secure).


Integrity Artifacts: Ensure all supply chain integrity docs are included. That means attach the SBOM, the signatures/attestations from Phase 7, and a proof or log of reproducible build. If applicable, include a provenance graph or any third-party audit attestations.


Evidence Bundle: Assemble a pack of evidence outputs. This would include the raw benchmark CSVs, the Stats Reports, performance profiles, the Perf Pareto chart, all ADRs, an extract of risk register if maintained, and the status of budgets (how much compute/money used vs planned). Essentially, everything needed to verify claims.


Human Factors: Conduct final usability and human-factor checks. If there's a UI or user interaction, perform at least 3 think-aloud usability tests and ensure a SUS (System Usability Scale) score ≥ 70 (if applicable). If the system provides outputs to users, ensure explainability: e.g., provide feature importance or rationale for decisions (like using SHAP values or counterfactual examples for AI decisions). For operations team, conduct a training: at least 2 runbook walkthroughs and 1 on-call drill (simulate an incident and ensure they can handle it). Document results of these tests (if any issues, fix them or note as future improvement).


Field-Test Kit: Prepare a deployment and field-testing kit. This includes scripts or documented steps to deploy in target environment(s), parameterized config files for typical, high-load, and failure-injection scenarios, any simulators or generators to test in field, an acceptance test checklist that field engineers can run to ensure installation is correct, a rollback plan (specific steps to revert to previous version if needed), and incident report templates (so field incidents are logged consistently).


Dashboard Artifact: Ensure the self-contained dashboard (with charts of CIs, tails, Pareto, fairness trends, etc.) is finalized and included for stakeholders. This helps them monitor and understand system performance over time.


Ledger: Update the ledger indicating all release artifacts are prepared and safety checks passed.
 Provide a summary of all release artifacts (what is in the checkpoint zip, list of safety docs, summary of usability tests, description of field-test kit) as outputs for Gate C9.


Procedure: The team compiles the final release artifact set. They likely create a directory or zip that contains everything enumerated (source code, documentation, manifests, SBOM, etc.). They thoroughly fill out safety documentation (they probably had drafts from earlier phases like DPIA started in Phase −1, updated hazard logs, etc.). They ensure any sector compliance is addressed (like if this was medical, ensure compliance doc; if it's a web service, maybe a privacy policy included). They collect all evidence outputs which might be scattered in Benchmarks/, Artifacts/, etc., and either list them or include in an evidence directory or shareable package. They do the final human factor evaluations (if not done earlier) like a mini user study or internal test. If a UI, they gather feedback, fix minor issues. They check that operations team have done at least one practice incident (like simulate a outage, see if runbook is clear). They finalize the field-test kit - basically a package that someone in the field can use to test the system in a pilot environment. The dashboard (likely created in earlier phases partially) is finalized with all updated data and is included as an HTML or similar in Artifacts/dashboard/. After assembling everything, they update the ledger and maybe sign off with relevant stakeholders (like product owner, safety officer) that all is ready.
Gate C9 — “Release Readiness”
Objective: Verify that everything required for a responsible release is in place. This gate is a final checklist before shipping to real users or external deployment.
Block Criteria: Gate C9 is typically a block gate meaning if any of these are missing, release is blocked:
Safety/Privacy artifacts missing: If any required safety docs or analysis is not done or incomplete (e.g., no DPIA where needed, or hazard analysis incomplete), block. Also if any serious known safety issue remains unmitigated.


Fairness regression >0.5% unmitigated: If during final tests any fairness or bias issue was discovered (like system performs worse for a protected group by more than 0.5% relative) and it hasn’t been addressed or explicitly accepted with sign-off, block release. Either mitigate it or get risk acceptance.


Integrity artifacts incomplete: If SBOM, signing, or reproducible build proof are missing, block. These are required for supply chain trust.


Benchmark evidence lacking: If we don't have the statistical proof of performance (like if we somehow lost the CSVs or didn't actually have the tail metrics to show, or maybe if something was not tested under realistic conditions), block until fixed. The idea is we must release with evidence backing claims.


Surface drift: If since Phase 8 something changed in the interface (shouldn’t, since frozen; but if a bug fix accidentally altered output format perhaps?), block until resolved or version bumped. Essentially ensure what we froze is indeed what we release.


Missing runbook/field kit: If those operational materials are not present, block because deployment would be risky.


Usability failure: If for systems with a human user component, the usability threshold isn't met (SUS score below 70 for a user-facing UI, or if testers still confused by system), consider blocking until improved. However, the text specifically mentions "failed usability threshold where human use applies", implying if we set a threshold like SUS 70 and scored below, block.


If none of these blocking issues, then gate passes and release can proceed.
Context Digest: Outline readiness: e.g., “All safety/privacy docs completed (Model Card, DPIA done, no unresolved issues). Fairness tests show no segment >0.5% worse than others after mitigations. SBOM and signed release in artifact. All benchmarks and profiles packaged. Interface same as frozen. Runbook & field-test kit included. Usability test average SUS 75, so good. Ready to release.” If any red flag: should be resolved or mentioned as resolved.
Options:
Proceed (Release): Everything is good, go to Phase 10 (post-release monitoring, though that's more continuous after release). Actually after Gate C9, typically they'd do a field test (Phase 10 covers continuous eval). But release can be done to a limited audience or generally.


Block and Fix: If any item triggers a block, do not release. E.g., if fairness issue found, address it (maybe retrain model to fix bias or add calibration) and re-evaluate. If SBOM not done, do it. If runbook lacking, complete it. Essentially, fix the gating issue then attempt Gate C9 again.


Risk Accept with Approvals: In rare cases, one might push for release with a known issue, but requires sign-off. For instance, if a minor privacy concern exists but mitigations in progress, maybe sign a temporary exception with plan to fix soon. But extremely careful as Gate C9 supposed to ensure responsible release. Usually better to delay than release unsafely.


Possibly partial release: if not ready for full release, maybe do another internal field test and treat it as extended Phase 9 until ready.


Rationale Prompt: “Evaluate Gate C9. Are all release artifacts complete? Any safety, fairness, or compliance concerns unresolved? Is the product usable and supportable? If all checks out, approve release. If not, list issues to fix before release.”
Next-Step Instruction:
If PASS: The product can be released to the field (maybe to Canary/production with monitoring as Phase 10 covers). The RCO moves into continuous evaluation mode (Phase 10).


If FAIL: Communicate to stakeholders that release is postponed due to gating issues. Fix them. Possibly run an emergency meeting on fairness if that’s the issue, etc. Only try release when resolved.


Log final results and prepare for operational monitoring (Phase 10).


Machine-Readable Metadata: Example Gate C9:
{
  "run_id": "<RUNID>",
  "gate_id": "C9",
  "timestamp_utc": "2025-08-14T06:00:00Z",
  "decision": "PASS",
  "release_artifacts": {
    "checkpoint_bundle": "checkpoint_final_v1.0.0.zip",
    "safety_docs": ["ModelCard.md", "DPIA.pdf", "MisuseAnalysis.md", "AssuranceCase.gsn"],
    "integrity_docs": ["SBOM.spdx.json", "signatures.asc", "repro_build.log"],
    "evidence_bundle": ["benchmarks.csv", "stats_report.json", "perf_pareto.csv", "ADRs/"],
    "field_test_kit": "DeplScripts v1.0, accept_checklist.docx, rollback_plan.md"
  },
  "fairness_check": "no >0.5% regression",
  "usability_SUS": 75,
  "runbook_present": true,
  "rationale": "All release criteria met. Full artifact bundle prepared, safety/privacy docs completed, fairness within limits, usability OK (SUS 75). Releasing version 1.0.0."
}

Source: Gate C9 criteria.

Phase 10 — Continuous Evaluation, Drift, Auto-Rollback
Objective: Monitor the solution in real-world operation, detect performance or data drift, and enforce automated rollback if issues arise. This phase is ongoing after deployment.
LLM Prompt (Phase 10):
Enter Phase 10 (Continuous Assurance). Now that the solution is live (even if just canary or shadow), set up and manage continuous evaluation:
Canary Deployment: Deploy the solution to a small percentage of users or traffic (e.g., 5%) and gradually ramp up. Monitor key SLOs during this ramp. If any SLO violation occurs (e.g., error rate spike, latency too high) or any fairness regression or anomaly with z-score > 3 is detected, automatically abort the rollout (stop increasing traffic or revert to 0%). Use the premortem indicators set earlier as specific monitors.


Shadow Mode: If possible, run the solution in shadow mode alongside the current production system for at least a week. Mirror real traffic to the new system without affecting users, and compare outcomes. Set alerts if the new system’s outputs deviate significantly (e.g., p95 difference > 5%) from the current production outputs. This helps catch issues without impact.


Drift Detection: Implement daily (or continuous) checks for data drift and performance drift. Use statistical tests like Population Stability Index (PSI) or KL divergence on input data distributions to detect data distribution shifts, and tests like CUSUM or ADWIN on performance metrics to detect degradation over time. Set thresholds for when drift is significant and needs attention. Log or alert on any drift events.


Auto-Rollback: Configure automation to rollback to the previous stable version if certain conditions are met. For instance, if two consecutive canary intervals show SLO breaches or a critical security alert triggers, the system should automatically revert to the last known good version within 10 minutes. Ensure notifications are sent to on-call engineers when rollback occurs, and an incident is opened. Test this mechanism in a dry-run (simulate conditions to see that rollback triggers as expected without affecting production).


Evidence TTL Re-verification: Since evidence (tests, benchmarks) have a TTL of 90 days by default, set reminders or pipelines to re-run a quick battery of tests periodically or whenever significant changes occur (like driver updates or library upgrades). A quick battery may include a smoke benchmark, a fairness spot-check, and a security scan to ensure nothing has silently degraded. Update evidence artifacts if needed.


Risk Monitoring: Have the RCO or monitoring scripts watch for any changes in risk factors. For example, if incident severity or frequency increases, consider escalating risk tier (e.g., treat system as R2 or R3 if incidents show higher impact than initially thought).


Ledger Updates: Continuously append events like canary start/stop, drift detected, rollback executed, re-verification results to the Run Ledger for audit.
 Provide evidence that canary/shadow deployments are set up, drift detection is running, and rollback was tested, and that owners for alerts are documented, as outputs for Gate C10.


Procedure: The operations team deploys version 1.0 into a canary environment (maybe 5% traffic), using automated deployment scripts from field-test kit. They have monitoring dashboards and alerts tied to SLOs (like throughput, error rate, response time, fairness metrics if automated). They gradually increase to 25% then 100% if all looks good, over time. They also possibly run a parallel shadow test if feasible (like in ML, you might shadow requests to new model to compare decisions). They implement drift detection jobs: e.g., a daily job that pulls new data and compares distribution to training data or prior data, and performance trend monitors that apply sequential analysis to key metrics. The auto-rollback mechanism is configured, likely in deployment pipeline or orchestrator (maybe a script or config that will trigger a rollback action if conditions met). They test rollback by simulating a scenario (for example, manually toggle a flag that simulates "two SLO breaches" to see if pipeline reverts to old version). They ensure evidence TTL re-check tasks are scheduled (maybe a Jenkins or cron job that re-runs tests each month or triggers on environment change). They put in place processes or even automated risk re-evaluation (like if an incident gets a certain severity, a procedure says "revisit risk tier, possibly upgrade to R2 requiring more process"). They keep logging everything into the ledger.
Gate C10 — “Continuous Assurance Activation”
Objective: Ensure that the continuous monitoring and rollback mechanisms are in place and tested before considering the deployment fully live. Gate C10 checks we have not just deployed but set up the safety nets for ongoing operation.
Pass Criteria: Gate C10 passes if:
Canary, shadow, drift detection, and rollback are all configured and either active or ready to activate with the release. There should be documentation of each: e.g., "Canary deploy on 5% traffic with these thresholds, shadow test running on offline environment, drift job daily 2am, rollback script monitoring alerts."


They have been dry-run tested to ensure they work (especially rollback).


Alerts/alarms are set up and have owners: each automated alert has someone on-call or a team that will respond. This includes specifying who is notified on triggers and that those people know their roles (which should be in runbook).


The team has documented what constitutes triggering events and that those triggers are currently green (i.e., initial deployment did not immediately trigger something unintended).


Essentially, continuous assurance is not a vague plan but an active system.


If any of these is not done, Gate C10 fails and you should not proceed to full scale without them.
Context Digest: Summarize continuous assurance setup: e.g., “Canary deployment enabled at 5% traffic, ramping plan to 100% over 1 week if no issues. Shadow testing in place comparing outputs, no major diffs so far. Drift detection running daily (monitoring input distribution shift, threshold set to PSI 0.2). Auto-rollback configured via deployment pipeline: tested yesterday, it successfully reverted version in staging on simulated error spike. All alerts go to on-call (Team X). Documentation of owners and procedures is done.”
Options:
Pass: If everything is in place and tested. At this point, the project transitions to ongoing operations mode.


Fail (fix now): If say rollback wasn't tested or drift monitor not set up, do it immediately. It's important to do these as part of initial launch, not "we'll do later," because by then it might be too late if an incident occurs.


Possibly if something like shadow test is not possible (some systems can't easily shadow), they'd justify that but have extra canary caution. That should be documented and risk accepted if skip.


If the team lacks something (like no one set up drift detection, or not enough monitoring), definitely fix before proceeding.


Rationale Prompt: “Evaluate Gate C10. Are continuous monitoring and rollback measures in place and tested? Confirm canary/shadow processes are working and that alerts have owners. If yes, we can fully operate the system with confidence. If not, address those gaps now.”
Next-Step Instruction:
If PASS: The system is now under continuous watch. The formal development process ends here, and the system enters Continuous Operation with the assurance mechanisms running. The protocol GCP V47.1 run is complete, except for any scheduled re-verification tasks.


If FAIL: Set up the missing pieces immediately. For example, if auto-rollback not tested, run a test scenario now; if alerts not assigned, assign and train that person. Then re-check.


After passing, schedule a retrospective or any final governance tasks (like final version tagging, releasing docs to public, etc.) as needed outside of gates.


Machine-Readable Metadata: Example Gate C10:
{
  "run_id": "<RUNID>",
  "gate_id": "C10",
  "timestamp_utc": "2025-08-14T07:00:00Z",
  "decision": "PASS",
  "canary_status": "Deploying at 25%, no SLO breaches",
  "shadow_status": "Running, output diff < 2%",
  "drift_monitor": "Enabled (PSI, CUSUM), no alerts",
  "rollback_tested": true,
  "alarms_configured": true,
  "oncall_owner": "Team X rotation",
  "rationale": "Continuous evaluation in place: canary and shadow running smoothly, drift detection active, rollback auto-tested successfully, alerting configured with on-call. Continuous assurance activated."
}

Source: Gate C10 criteria.

Compliance Statement: A run that completes all phases (−1 through 10) and passes all gates (C−0.5 through C10) has achieved the following:
Validated Problem Worthiness: It proved the problem is real, significant, and tractable versus doing nothing or non-technical alternatives.


Minimal Effective Solution: It chose the simplest effective intervention where appropriate, or justified any additional complexity with evidence of superior expected value.


Quality and Performance Assurance: It met or exceeded all defined quality floors and SLOs, including in the tail cases, with statistical significance.


Robustness and Fairness: It withstood adversarial testing (no high-severity issues), and documented fairness impacts with mitigations for any biases.


Performance and Adoption Evidence: It demonstrated required performance, cost, and energy efficiency, and provided evidence of adoption feasibility (including training, support, and total cost of ownership analysis).


Integrity and Security: It established supply chain integrity (SBOM, signed artifacts, vulnerability management) and depth in security (tests, threat mitigations, etc.).


Interface Stability: It froze a minimal, stable public interface with compatibility guarantees and version governance.


Complete Artifacts: It produced a signed, reproducible release checkpoint, along with all documentation (safety, human factors) and a field-test kit (deployment tools, rollback plan, monitoring dashboard).


Continuous Assurance: It activated continuous monitoring (canary, shadow, drift detection, auto-rollback) and set up evidence renewal processes to maintain trust over time.


Decision Calibration: It logged key decision forecasts and will Brier-score them after outcomes to improve future planning accuracy.


This is GCP V47.1 — Worth-It Realism Edition (Evolutionary Revision). It is exhaustive by design and explicitly prevents “confidently wrong” solutions to problems that were never worth solving.

