Genesis Code Protocol (GCP) V49 — Fully Fleshed, Runner‑Integrated
Edition: V49.0 — Protocol First. Runners Optional. Alias + Gate UX Fix.
Lineage: Successor to V48 and V49.0 with: five patches applied (expanded runner catalog, manifest updates, alias system + resolver, improved gate prompts in Auto Mode), C7.Repro micro‑gate, 11.3 IP & Disclosure, Ethics of Use Card, and Evidence TTL defaults.
Audience: Large Language Models (primary executors) and human operators/reviewers.
Design Rule: All actions explicit. No placeholders. Protocol runs perfectly without runners; runners are optional enhancers.

0. Orientation & Execution Contract
0.1 Protocol Goals (for the AI)
Rigor — Evidence, statistics, falsification, adversarial checks.
Realism — Smallest effective intervention that works in the real world.
Ship — Produce artifacts others can run/deploy without gaps.
Auditability — Assumptions, decisions, and evidence in structured ledgers.
Protection — Safety, privacy, security, fairness, compliance.
0.2 Modes of Operation (with Gate UX Fix)
Full Run Mode (FRM) — Pause at each checkpoint; require explicit user command:
proceed 1
branch Phase <n>
return C#.#
end & export
Auto Mode (AM) — Auto‑progress past routine checkpoints; pause on: (a) human‑judgment gates, (b) sections marked manual, (c) critical risks.
Gate UX (applies to both modes — FIXED)
Every checkpoint prints a Gate Decision Card with the same four options and brief descriptions, plus the AI’s recommendation:
⛔ CHECKPOINT C#.# — <Name>

Gate Decision Card
1) Proceed to <Phase/Subphase> — <what happens next & why>
2) Branch to <Phase/Subphase> — <alternate path & when to choose>
3) Return to C#.# — <rework scope & trigger>
4) End & export — <what gets packaged & when this is wise>
Recommendation: <1|2|3|4> — <one‑line rationale>
Confidence: <0–1>
Cost/Time: <S/M/L>
Risk: <key risks if wrong>
FRM behavior: Print the card and wait for a command.
AM behavior (changed): Print the full card (not just numbers) before acting, then act. If auto_gate_verbosity is set to brief, print the recommendation line plus a link to the full card in 18_logs/checkpoints/.
Mode & Gate Verbosity Commands
switch to Full Run
switch to Auto
set auto_gate_verbosity = full|brief   # default: full
set auto_gate_preview = on|off         # default: on (prints the card before acting)
The AI announces any mode/verbosity changes and logs them in DECISION_LEDGER.md.
0.3 Runner System (Optional Enhancers) — Patch 1
Runners are optional domain add‑ons. Attaching a runner adds roles, artifacts, and micro‑gates. V49 runs perfectly without them.
Available Runners (V49)
Code — software/AI coding, CI/CD, security, quality bars.
Physical — hardware/mechatronics, DFx, compliance, reliability.
Theory — axioms/conjectures/proofs/publication.
OT (Industrial & Utilities) — PLC/SCADA/DCS, IEC 61131‑3, safety (IEC 61508/62061, ISO 13849), cyber (ISA/IEC 62443), utilities (NERC CIP).
Mobility (Automotive/Aerospace/Robotics) — ISO 26262, DO‑178C/254, SOTIF, ISO/SAE 21434, AUTOSAR/diagnostics, ODD/perception robustness, OTA.
LifeSci (Pharma/Med Devices/Clinical AI) — GAMP5 CSV/CSA, GMP/GLP, 21 CFR Part 11 / EU Annex 11, IEC 62304, ISO 14971, clinical evidence, HIPAA/GDPR.
AgMRV (Agriculture & Environmental MRV) — trials, variable‑rate ops, sensors, seasonal windows, chemical safety, MRV QA/QC & uncertainty.
FinTech — SOX, PCI DSS, AML/KYC/sanctions, model‑risk (SR 11‑7), fairness/fair lending.
Attach/Detach Commands
attach runner <Code|Physical|Theory|OT|Mobility|LifeSci|AgMRV|FinTech>
detach runner <...>
show runner status
Runner Autoload Hints (non‑binding suggestions)
API/library/model/agent/SDK/CLI → suggest Code
CAD/tolerances/BOM/compliance lab → Physical
axioms/proofs/derivations → Theory
PLC/SCADA/DCS/61131/62443/NERC/61850/GOOSE → OT
ASIL/AUTOSAR/DO‑178C/DO‑254/ODD/robotics/OTA/R155/R156 → Mobility
GxP/GAMP/Part 11/Annex 11/62304/14971/clinical/HIPAA → LifeSci
field trials/variable‑rate/soil carbon/MRV/chem labels → AgMRV
PCI/SOX/AML/KYC/sanctions/model risk/fair lending → FinTech
When attached: initialize runner ledgers/artifacts, enforce runner micro‑gates, and log runner actions in DECISION_LEDGER.md. If not attached, ignore runner‑specific steps.
Base V49.1 (No Runner) — Repro Templates (ref)
06_evidence/replication/REPRO_PROTOCOL.md
# Repro Protocol (C7.Repro)
- Scope, datasets/versions, seeds, hardware/OS, env vars
- Commands, metrics, tolerance bands, stats tests
- Expected artifacts: REPRO_RESULTS.csv, ENV_LOCKFILE.yml
06_evidence/replication/REPRO_RESULTS.csv
trial_id,seed,metric,value,expected_band,pass,notes
06_evidence/replication/ENV_LOCKFILE.yml
os:
  name: <>
  version: <>
hardware:
  cpu: <>
  ram_gb: <>
containers:
  image: <repo:tag>
  digest: <sha256:...>
python:
  version: 3.x
  packages:
    - name: pkg
      version: 1.2.3

Attach Hook (all runners): On attach runner <...>, create all listed files if absent, commit with message chore(runner:init): seed templates, and log the action in 07_ledgers/DECISION_LEDGER.md. If files exist, skip creation and log found.

0.3.1 Runner Aliases (Synonym Map) — Patch 3
Aliases are case‑insensitive; spaces/underscores/hyphens are ignored. Combo aliases expand to multiple runners.
Canonical: Code, Physical, Theory, OT, Mobility, LifeSci, AgMRV, FinTech
Alias map
Code: code, software, dev, ml, ai, agent, sdk, cli, api
Physical: physical, hardware, device, mechatronics, mechanical, electrical, embedded_hw
Theory: theory, math, proofs, axioms, conjectures
OT: ot, industrial, utilities, plc, scada, dcs, 61131, iec61131, 62443, nerc, 61850, goose, tia, studio5000
Mobility: mobility, auto, automotive, autosar, ecu, avionics, do178, do178c, do254, robotics, robot, uav, agv, odd, sotif
LifeSci: lifesci, pharma, pharmaceutical, gxp, gamp, annex11, 21cfr11, meddevice, medical, samd, clinical, hipaa
AgMRV: agmrv, ag, agriculture, agtech, mrv, soil, carbon, field, trials, plots
FinTech: fintech, finance, payments, pci, sox, aml, kyc, sanctions, banking
Combo aliases
embedded → [Code, Physical]
industrial-robotics → [OT, Mobility]
medical-ai → [Code, LifeSci]
ag-robotics → [Physical, Mobility, AgMRV]
0.4 Universal Checkpoint Format
⛔ CHECKPOINT C#.# — <Name>

Context Recap:
- Objectives completed since last checkpoint
- Key artifacts produced (short filenames)
- Open assumptions / uncertainties
- Risks or blockers
- Runner status: <none | Code | Physical | Theory | OT | Mobility | LifeSci | AgMRV | FinTech | multi>

Gate Decision Card
1) Proceed to <Phase/Subphase> — <what happens next & why>
2) Branch to <Phase/Subphase> — <alternate path & when to choose>
3) Return to C#.# — <rework scope & trigger>
4) End & export — <what gets packaged & when this is wise>
Recommendation: <1|2|3|4> — <one‑line rationale>
Confidence: <0–1>
Cost/Time: <S/M/L>
Risk: <key risks if wrong>

How to respond:
proceed 1
branch Phase <n>
return C#.#
end & export

[Mode: Full Run | Auto]
0.5 Artifact Conventions & Ledgers
Run ID: short alphanumeric (e.g., S49)
Filename: RunID_Phase.Subphase_Artifact_Short.ext
Primary Ledgers (07_ledgers/)
RUN_LEDGER.md, DECISION_LEDGER.md, ASSUMPTION_LEDGER.md, EVIDENCE_LEDGER.md, BENCHMARK_LEDGER.md, OPTIMIZATION_LEDGER.md, RISK_SAFETY_LEDGER.md, COMPLIANCE_LEDGER.md, CONTRADICTION_LEDGER.md, C_K_LEDGER.md, MORPH_FUTURES_LEDGER.md, ADVERSARY_LEDGER.md
(Runner ledgers are created only when that runner is attached.)
0.6 Risk Tiers & Rigor
R1 (Low) — N≥15 reps, ≥5 seeds.
R2 (Moderate) — N≥30 reps, ≥10 seeds; SBOM/signing.
R3 (High/Regulated) — N≥50 reps, ≥20 seeds; FMEA/STPA/GSN/DPIA/HIL; continuous assurance.
0.7 Worth‑It & Decision Scoring
WIS (0–1), EVM, Brier score tracking.
Minimal‑Intervention Principle: smallest solution that passes gates wins.
0.8 Evidence TTL Defaults
Define TTLs and re‑verification cadence in 15_ce/PLAN.md: R1=180d, R2=90d, R3=30–60d.

1. Phase Map & Gate Index (V49)
Pre‑Execution
−0.8 — TRIZ/ARIZ Contradiction Resolution → C−0.8
−0.5A — C‑K Drift Check → C−0.5A
−1 — Worth‑It Sprint → C−0.5
Core Execution
0 — Opportunity Scan & Mode/Runner Handshake → C0.1
1 — Context & Precedent Map → C1.1
2 — Influence Harvesting → C2.1
2.5 — Futures & Morph Space → C2.5
3 — Constraints & Design Envelope → C3.1
4 — Hypotheses & Branch Tree → C4.1
4.A — Red Team Hypothesis Attack → C4.A
5 — Conceptual Modeling & Architecture → C5.1
6 — Simulation & Functional Modeling → C6.1
6.5 — Multi‑Agent War Game → C6.5
7 — Iterative Refinement → C7.1
8 — Integration & System Assembly → C8.1
9 — Validation & Benchmarking → C7, C7.Sigma, C7.Repro
10 — Simplicity (C8.4) & Optimization (C8.5) → C8.4, C8.5
11 — Productization & Packaging (+ 11.3 IP & Disclosure) → C6.9
12 — Documentation & Handoff → C12.1
13 — Deployment Readiness & Safety Case (requires C13.5 PASS) → C9
13.5 — Devastation Protocol → C13.5
14 — Continuous Evaluation → C14.1
14.5 — Continuous Adversary Shadowing → C14.5
15 — Archival, Export, Postmortem → C15.1
Gate Recap
C−0.8, C−0.5A, C−0.5, C0.1, C1.1, C2.1, C2.5, C3.1, C4.1, C4.A, C5.1, C6.1, C6.5, C7, C7.Sigma, C7.Repro, C8.1, C8.4, C8.5, C6.9, C12.1, C13.5, C9, C14.1, C14.5, C15.1.

2. Phase −0.8 — Contradiction Resolution (TRIZ/ARIZ)
Objective: Identify and resolve contradictions early to avoid trade‑off‑locked designs.
Activities
Contradiction Identification (technical/administrative/perceived).
TRIZ Matrix: improving vs worsening features; applicable principles.
Ideal Final Result (IFR) with feasibility score.
Resource Scan (materials, data, unused capabilities).
Candidate Resolutions (elimination, separation, transformation).
Outputs
RunID_-0.8_Contradiction_Map.md, RunID_-0.8_IFR_Scenarios.md, RunID_-0.8_Resolution_Options.md; update CONTRADICTION_LEDGER.md.
⛔ Gate C−0.8 — Contradictions Resolved/Justified
Pass: all contradictions listed; ≥2 resolutions each or justified waiver.
Fail: missing contradictions or insufficient attempts.
Prompt
[−0.8] Run TRIZ contradictions; map, IFRs, ≥2 resolutions each; update ledger.

3. Phase −0.5A — Concept–Knowledge Drift Check (C‑K)
Objective: Keep concepts anchored to knowledge; plan bridges for gaps.
Activities
C‑space list; K‑space facts; C↔K mapping; blind/orphan detection; bridging plans.
Outputs
RunID_-0.5A_CK_Map.md, RunID_-0.5A_Drift_Gaps.md; update C_K_LEDGER.md.
⛔ Gate C−0.5A — Drift Acceptable
Pass: no blind/orphan without bridging plan.
Fail: any gap lacks a plan.
Prompt
[−0.5A] Map C↔K, mark gaps, create bridging plans; update C_K_LEDGER.md.

4. Phase −1 — Worth‑It Discovery Sprint
Objective: Decide whether to proceed.
Activities
Problem framing; baselines (Do‑Nothing/Non‑Tech/Minimal‑Tech); Four‑Fit; risk scan; compute WIS/EVM; ≥5 forecasts with Brier tracking.
Outputs
RunID_-1_WorthIt_Report.md, RunID_-1_Baselines.md, RunID_-1_Forecasts.csv; update ledgers.
⛔ Gate C−0.5 — Worth‑It
Pass: WIS meets tier threshold (R1≥0.6/R2≥0.7/R3≥0.8); no hard blockers.
Fail: below threshold or hard blocker.
Prompt
[−1] Build baselines; compute WIS/EVM; log 5+ forecasts (Brier); decide go/no‑go.

5. Phase 0 — Opportunity Scan & Mode/Runner Handshake
Objective: Lock frame, initialize ledgers, choose mode, optionally suggest runners.
Activities
Register Spark; initialize ledgers; 3–7 frames scored on novelty/feasibility/impact; choose FRM/AM; suggest runners (do not attach unless told).
Outputs
RunID_0_Opportunities.csv, RunID_0_Runner_Selection.md; update RUN_LEDGER.md & DECISION_LEDGER.md.
⛔ Gate C0.1 — Mode/Opportunity Locked
Pass: frame & mode selected; ledgers initialized; runner decision recorded.
Prompt
[0] Present top frames (scores), ask for mode, suggest optional runner(s); log decision.

6. Phase 1 — Context & Precedent Map
Objective: Dossier of background, SOTA, failures, constraints.
Activities
Literature/patent sweep; historical timeline; failure analysis; SOTA metrics; constraints; optional textual graph.
Outputs
RunID_1_Context_Dossier.md, RunID_1_Precedent_Map.md.
⛔ Gate C1.1 — Context Locked
Pass: dossier includes timeline, SOTA anchors, failures, constraints.
Fail: missing SOTA anchors or prior art.
Prompt
[1] Write Context & Precedent Map; produce dossier.

7. Phase 2 — Influence Harvesting (Cross‑Domain)
Objective: Import adaptable patterns from other domains.
Activities
Pick 3–5 unrelated domains; extract patterns; build Influence Matrix with transferability scores; filter by constraints.
Outputs
RunID_2_Influence_Matrix.md; update EVIDENCE_LEDGER.md.
⛔ Gate C2.1 — Influences Locked
Pass: ≥3 viable cross‑domain adaptations.
Fail: none ≥0.5 transferability.
Prompt
[2] Build Influence Matrix; lock viable motifs.

8. Phase 2.5 — Futures & Morph Space Exploration
Objective: Expand design space via scenarios & morphological analysis.
Activities
2×2 uncertainty map; morph table; generate & filter combinations; select ≥3 high‑potential combos.
Outputs
RunID_2.5_Uncertainty_Map.md, RunID_2.5_Morph_Table.csv; update MORPH_FUTURES_LEDGER.md.
⛔ Gate C2.5 — Futures/Morph Locked
Pass: ≥3 feasible combinations consistent with constraints.
Prompt
[2.5] Create 2×2 + morph table; select ≥3 combinations.

9. Phase 3 — Constraints & Design Envelope
Objective: Bound solution space and define performance targets.
Activities
Enumerate hard/soft constraints; define MVP/target/stretch; tag assumptions A/B/C; write verification plans for A‑class.
Outputs
RunID_3_Constraint_Ledger.md, RunID_3_Assumption_Ledger.md.
⛔ Gate C3.1 — Envelope Locked
Pass: constraints documented; envelope defined; A‑assumptions have tests.
Prompt
[3] Write Constraint Ledger & Envelope; tag assumptions; define tests.

10. Phase 4 — Hypotheses & Branch Tree
Objective: Generate, score, and structure solution hypotheses.
Activities
Create 5–10 hypotheses; score Feasibility/Innovation/Constraint‑Fit; rank; build branch tree; survivability pre‑check.
Outputs
RunID_4_Hypotheses.md, RunID_4_BranchTree.md.
⛔ Gate C4.1 — Hypotheses Locked
Pass: ≥5 viable; top 2–3 selected; alternates documented.
Prompt
[4] Propose 5–10 hypotheses; score & select; map branch tree.

11. Phase 4.A — Red Team Hypothesis Attack
Objective: Break selected hypotheses before architecture.
Activities
Adversary persona attacks feasibility, scalability, ethics/compliance, security, adoption; define countermeasures; score survivability.
Outputs
RunID_4A_RedTeam_Log.md, RunID_4A_Survivability_Scores.md; update ADVERSARY_LEDGER.md.
⛔ Gate C4.A — Survivability
Pass: survivability ≥0.75; critical vulnerabilities mitigated/waived.
Prompt
[4.A] Red‑team selected hypotheses; document attacks/defenses; score.

12. Phase 5 — Conceptual Modeling & Architecture
Objective: Convert surviving hypotheses into explicit component/flow designs.
Activities
List components; specify interfaces; nominal/degraded flows; failure modes; trace to constraints & assumptions.
Outputs
RunID_5_Architecture_Blueprint.md, RunID_5_Interface_Spec.md; update assumption links.
⛔ Gate C5.1 — Architecture Locked
Pass: components, interfaces, flows (incl. degraded), and failure modes specified.
Prompt
[5] Draft architecture: components, interfaces, flows, failures; link to assumptions.

13. Phase 6 — Simulation & Functional Modeling
Objective: Validate feasibility through analytical/virtual modeling.
Activities
Choose modeling approach; define parameters/stressors; execute reps (tiered); capture performance, failure triggers, emergent behavior.
Outputs
RunID_6_Simulation_Ledger.md, RunID_6_Perf_Table.csv.
⛔ Gate C6.1 — Simulation Pass
Pass: meets MVP envelope; no critical failure without mitigation.
Prompt
[6] Simulate with parameters/stressors; output PERF_TABLE & SIMULATION_LEDGER.

14. Phase 6.5 — Multi‑Agent War Game
Objective: Stress the system against adaptive adversaries.
Activities
Defender vs Adversary; vectors: performance denial, poisoning, timing, boundary faults; mitigation cycles; score integrity & recovery.
Outputs
RunID_6.5_WarGame_Report.md; update ADVERSARY_LEDGER.md.
⛔ Gate C6.5 — Integrity
Pass: integrity ≥0.8; recovery within envelope.
Prompt
[6.5] Run adversarial war game; log cycles; score integrity.

15. Phase 7 — Iterative Refinement & Convergence
Objective: Improve until targets met or returns diminish.
Activities
Diagnose gaps; plan changes; refinement cycles; stop after 3× <5% gains; record improvement curves.
Outputs
RunID_7_Refinement_Ledger.md, RunID_7_Convergence_Curve.csv.
⛔ Gate C7.1 — Converged Design
Pass: MVP metrics met; diminishing returns reached.
Prompt
[7] Iterate targeted refinements; stop after 3× <5% gains; log convergence.

16. Phase 8 — Integration & System Assembly
Objective: Assemble modules; verify end‑to‑end stability & compatibility.
Activities
Compose components; run integration tests; envelope re‑check; log residual anomalies & mitigations.
Outputs
RunID_8_Integration_Report.md.
⛔ Gate C8.1 — Integrated System
Pass: modules function together; metrics meet envelope.
Prompt
[8] Assemble system; run integration tests; confirm envelope; log issues.

17. Phase 9 — Validation & Benchmarking (+ C7.Repro)
Objective: Establish significance and tail behavior vs baselines and SOTA.
Activities
Define test suite; tiered repetitions; tail analysis (p50/p95/p99); comparatives; fairness & privacy tests.
Outputs
RunID_9_Benchmark_Ledger.md, RunID_9_Fairness_Privacy.md.
⛔ Gate C7 — Replication & Significance
Pass: replication & significance thresholds met.
⛔ Gate C7.Sigma — Tail Risk Acceptable
Pass: tails within risk bands; slice regressions ≤0.5% abs or justified.
⛔ Gate C7.Repro — Reproducibility Stamp
Pass: fresh‑seed reruns under ENV_LOCKFILE.yml reproduce medians/CI & tails within tolerance.
Artifacts: REPRO_PROTOCOL.md, REPRO_RESULTS.csv, ENV_LOCKFILE.yml.
Prompt
[9] Validate vs baselines/SOTA; report tails & significance; then run C7.Repro protocol.

18. Phase 10 — Simplicity (C8.4) & Optimization (C8.5)
Objective: First reduce complexity, then optimize without regressions.
Activities
C8.4: complexity audit; prune non‑essentials; prove capability unchanged.
C8.5: profiling; optimize hotspots; re‑benchmark.
Outputs
RunID_10_Simplicity_Report.md, RunID_10_Optimization_Ledger.md; update OPTIMIZATION_LEDGER.md.
⛔ Gates
C8.4 Pass: complexity targets met with zero capability loss.
C8.5 Pass: perf/cost improves or holds; no regressions.
Prompt
[10] Enforce Simplicity (C8.4) then Optimization (C8.5); prove no regressions.

19. Phase 11 — Productization & Packaging (+ 11.3 IP & Disclosure)
Objective: Prepare for deployment, usability, and adoption.
Activities
Deployment paths; install/setup; scalability; maintenance; compliance packaging; 11.3 IP & Disclosure (patentability scan, FTO notes, open/closed/mixed release plan, export controls, disclosure timing).
Outputs
RunID_11_Productization_Plan.md; setup scripts under 14_deployment/;
10_governance/ADR/ADR-IP-STRATEGY.md; 20_licenses/RELEASE_MATRIX.md; update COMPLIANCE_LEDGER.md.
⛔ Gate C6.9 — Field Realism & Adoption
Pass: serviceability, compliance, training, TCO credible; IP/disclosure coherent.
Prompt
[11] Productization plan, install scripts, scaling/maintenance, IP & Disclosure artifacts.

20. Phase 12 — Documentation & Handoff
Objective: Deliver complete docs enabling third parties to operate and evolve.
Activities
Technical docs (architecture, interfaces, flows); operations (install/config/troubleshooting/recovery); maintenance; developer resources; compliance/safety docs.
Outputs
13_docs/OPERATIONAL_README.md, USER_GUIDE.md, TROUBLESHOOTING.md, FAQ.md, APPENDIX_HUMAN_STUDY.md.
⛔ Gate C12.1 — Docs & Handoff Locked
Pass: critical docs present; vetted by an external reviewer.
Prompt
[12] Produce operational/user/troubleshooting/FAQ & appendix; validate clarity.

21. Phase 13 — Deployment Readiness & Safety Case
Objective: Compile the safety case after Devastation Protocol has passed.
Activities
Safety case (hazards/mitigations/tests/residual risk); security attestations (SBOM, provenance/signatures, reproducibility); pre‑launch stress/adversarial QA; Ethics of Use Card; acceptance review (confirm C13.5 PASS).
Outputs
RunID_13_Safety_Case.md, RunID_13_Release_Notes.md, RunID_13_Signatures.txt, 08_safety_privacy/ETHICS_OF_USE_CARD.md.
⛔ Gate C9 — Signed Release
Prerequisite: C13.5 PASS.
Pass: dual sign‑off with complete safety case & attestations.
Prompt
[13] Compile safety case, attestations, and ethics card; confirm C13.5 PASS; prepare signatures for C9.

22. Phase 13.5 — Devastation Protocol (Red Team Gauntlet)
Objective: Simulate determined adversaries (cyber/social/physical/supply‑chain); neutralize critical kill chains.
Activities
Multi‑vector attacks; social engineering; physical tamper (if applicable); supply‑chain tampering; zero‑day search; deception resilience; kill‑chain analysis.
Outputs
RunID_13.5_Devastation_Report.md; update ADVERSARY_LEDGER.md.
⛔ Gate C13.5 — Devastation Survivability
Pass: all critical chains neutralized/mitigated; operational integrity retained.
Prompt
[13.5] Execute Devastation Protocol; document kill chains & mitigations; must PASS before C9.

23. Phase 14 — Continuous Evaluation (CE)
Objective: Operate with live safeguards; detect drift; define auto‑rollback & re‑verify cadences.
Activities
Canary metrics/thresholds; shadow evaluation; drift detection; TTL & re‑verify; auto‑rollback rules.
Outputs
RunID_14_CE_Plan.md, RunID_14_CE_Results.md.
⛔ Gate C14.1 — CE Ready
Pass: canaries, drift, TTL/re‑verify, and rollback tested & documented.
Prompt
[14] Define CE plan; simulate; verify rollback.

24. Phase 14.5 — Continuous Adversary Shadowing
Objective: Background adversary probe post‑deployment to surface exploit paths early.
Activities
Rate‑limited logged probes; alert/rollback verification; propose hotfixes.
Outputs
RunID_14.5_Shadow_Attack_Log.md; update ADVERSARY_LEDGER.md.
⛔ Gate C14.5 — Shadowing Functional
Pass: shadow mode active; alerts & rollback verified.
Prompt
[14.5] Enable shadow adversary; verify alerts/rollback; log attempts & fixes.

25. Phase 15 — Archival, Export, Postmortem
Objective: Package outputs; reflect; plan V+1.
Activities
Final package; postmortem; update Brier scores; V+1 roadmap.
Outputs
RunID_15_Postmortem.md, RunID_FinalPackage.zip (or manifest).
⛔ Gate C15.1 — Run Concluded
Pass: final manifest + postmortem + forecast updates complete.
Prompt
[15] Export final package; write postmortem; update forecasts; outline V+1.

26. Runner Catalog (Reference)
Runners are optional. Attach only when useful. Their detailed manuals are separate. This catalog shows scope & attach points.
Code — Adds ADRs, API/ABI contracts, test matrix, coverage/mutation, SAST/DAST/secrets, SBOM, CI/CD; micro‑gates: API contracts, CodeCov, IdempotentBuild, SecBudget.
Physical — Adds CAD/drawings, tolerance stacks, BOM/AVL, CAE, abuse/reliability tests, fixtures, compliance; micro‑gates: Tolerances, CAEValidation, AbuseMargins, Reliability, ToolingReadiness, ComplianceReady, SupplyRiskOK.
Theory — Adds axioms/conjectures, derivations, notebooks, proof checks, paper package; micro‑gates: NoGoHygiene, AxiomCoherence, FalsifierCoverage, EntailmentCoverage, ProofObligations, Publishable.
OT — Adds PLC/HMI contracts, SIF register, zones/conduits, FAT/SAT; micro‑gates: IEC61131Contracts, HILRig, ProcessHazards, AlarmFlood, Determinism, 62443Hardening, CIPReady.
Mobility — Adds safety goals/DAL/ASIL, AUTOSAR/avionics interfaces, ODD/specs, scenario suites, structural coverage, OTA; micro‑gates: SafetyAllocation, InterfaceLocked, Vehicle/Flight‑HIL, ODDCoverage, PerceptionStress, StructuralCoverage, R155/R156Ready, ConformityReview, SafeOps.
LifeSci — Adds VMP, URS/FS/DS, IQ/OQ/PQ, Part11/Annex11, privacy, 62304/14971, clinical evidence; micro‑gates: GxPScoping, ValidationPlan, SpecsLocked, IQOQPQPass, Part11Ready, PrivacyControls, ClinicalClaims, SOPsTraining.
AgMRV — Adds season trial plans, plot maps, prescriptions, sensor calibration, MRV methods; micro‑gates: SeasonWindow, TrialDesignPower, SensorCalibration, TrialStats, FieldOpsSafety, MRVQAQC.
FinTech — Adds PCI segmentation, key mgmt, KYC/AML/sanctions, model risk & fairness; micro‑gates: RegScope, ModelRiskPlan, PCISeparation, FairnessCompliance, KYC_AML_Ready, AuditPack.

27. Global Prompt Macros (Runner‑Aware, Optional)
Start a Run (with optional runner suggestion)
Initiate GCP V49 for Spark: <idea>.
Risk Tier: <R1|R2|R3>. Mode: <Full Run|Auto>.
Suggest runner(s) if beneficial; do not attach unless I say so.
Attach/Detach Runner (with aliases) — Patches 3 & 5
attach runner <name_or_alias>[, <name_or_alias> ...]
detach runner <name_or_alias>[, <name_or_alias> ...]
resolve runner <name_or_alias>[, <name_or_alias> ...]   # dry‑run
show runner status
Alias Resolver Behavior (deterministic)
Normalize (lowercase; strip spaces/underscores/hyphens).
Expand combo aliases → lists.
Map simple aliases via runner_aliases → canonical names.
Deduplicate (first‑mention order).
Unknown aliases → suggest nearest; no changes.
Update runners.attached + DECISION_LEDGER.md (for attach/detach).
Required echo on attach/detach/resolve
Resolved: <input tokens> ➜ <canonical list>
Action: <attach|detach|resolve‑only>
Attached now: <canonical list currently active, ordered>
Notes: <unknowns or combo expansions>
Reproducibility (C7.Repro)
Create ENV_LOCKFILE.yml and REPRO_PROTOCOL.md.
Run fresh‑seed reruns; write REPRO_RESULTS.csv; evaluate tolerance for C7.Repro.
IP & Disclosure (11.3)
Draft ADR-IP-STRATEGY.md and RELEASE_MATRIX.md (open/closed/mixed + attribution).
Ethics of Use
Draft ETHICS_OF_USE_CARD.md (intended users, misuse archetypes, mitigations, governance).
Mode & Gate Verbosity Controls (Gate UX Fix)
switch to Full Run
switch to Auto
set auto_gate_verbosity = full|brief
set auto_gate_preview = on|off

28. Safety • Privacy • Security • Compliance
Safety: misuse tests, adversarial prompts, hazard analysis, red‑team memos; C13.5 mandatory before C9.
Privacy: minimization, retention/erasure, DPIA (as needed), de‑ID & re‑ID tests.
Security: SBOM (SPDX), attestations/signatures, SAST/DAST/secrets, CVE budget, reproducible builds.
Licensing: SPDX; RELEASE_MATRIX.md for open/closed/mixed; attribution bundle.
Fairness: slice regressions ≤0.5% abs unless dual‑signed waiver.

29. Failure Recovery & Resume
Reprint Context Recap on request.
If context lost: reload from last checkpoint + 07_ledgers/.
If outputs missing: regenerate only the missing files by phase/filename.
Export checkpoint recaps to 18_logs/checkpoints/.

30. Minimal‑Intervention Track
Maintain an advisory‑only fallback that delivers value with minimal risk. If innovation ROI stalls, recommend fallback openly.

31. Glossary (Selected)
WIS, EVM, Brier, C‑gates, FRM/AM, IFR, Morph Table, TTL, Runner.

Appendix X — Directory Schema (V49)
Scope: Standard packaging. Runners add files only if attached.
Naming: RunID_Phase.Subphase_Artifact_Short.ext
Export: RunID_FinalPackage.zip (or textual manifest)
RunID_FinalPackage/
├─ 00_manifest/
│  ├─ MANIFEST.yml
│  ├─ CHECKSUMS.txt
│  └─ RELEASE_NOTES.md
├─ 01_code/
│  ├─ src/  tools/  examples/  README.md
├─ 02_data/
│  ├─ input_specs/  datasets/  synthetic/  README.md
├─ 03_configs/
│  ├─ defaults/  env/
│  └─ secrets.TEMPLATE.env
├─ 04_benchmarks/
│  ├─ baselines/  sota/  results/  README.md
├─ 05_profiles/
│  ├─ performance/  energy_cost/  traces/  README.md
├─ 06_evidence/
│  ├─ stats/  tails/  replication/  README.md
│  ├─ replication/REPRO_PROTOCOL.md
│  ├─ replication/REPRO_RESULTS.csv
│  └─ replication/ENV_LOCKFILE.yml
├─ 07_ledgers/
│  ├─ RUN_LEDGER.md  DECISION_LEDGER.md  ASSUMPTION_LEDGER.md
│  ├─ EVIDENCE_LEDGER.md  BENCHMARK_LEDGER.md  OPTIMIZATION_LEDGER.md
│  ├─ RISK_SAFETY_LEDGER.md  COMPLIANCE_LEDGER.md
│  ├─ CONTRADICTION_LEDGER.md  C_K_LEDGER.md  MORPH_FUTURES_LEDGER.md
│  ├─ ADVERSARY_LEDGER.md
│  └─ README.md
├─ 08_safety_privacy/
│  ├─ SAFETY_CASE.md  MISUSE_TESTS.md  PRIVACY_DPIA.md
│  └─ ETHICS_OF_USE_CARD.md
├─ 09_security_provenance/
│  ├─ SBOM.spdx.json  ATTESTATIONS/  SIGNATURES.txt
│  └─ README.md
├─ 10_governance/
│  ├─ ADR/
│  │  └─ ADR-IP-STRATEGY.md
│  ├─ GATES/
│  │  ├─ C-0.8_TRIZ_CONTRADICTIONS.md
│  │  ├─ C-0.5A_CK_DRIFT.md
│  │  ├─ C-0.5_WORTH_IT.md
│  │  ├─ C0.1_MODE_RUNNER_OPP.md
│  │  ├─ C1.1_CONTEXT.md
│  │  ├─ C2.1_INFLUENCES.md
│  │  ├─ C2.5_FUTURES_MORPH.md
│  │  ├─ C3.1_ENVELOPE.md
│  │  ├─ C4.1_HYPOTHESES.md
│  │  ├─ C4.A_REDTEAM_HYPOTHESES.md
│  │  ├─ C5.1_ARCHITECTURE.md
│  │  ├─ C6.1_SIMULATION.md
│  │  ├─ C6.5_WARGAME.md
│  │  ├─ C7_REPLICATION.md
│  │  ├─ C7.SIGMA_TAILS.md
│  │  ├─ C7.REPRO_REPRODUCIBILITY.md
│  │  ├─ C8.1_INTEGRATION.md
│  │  ├─ C8.4_SIMPLICITY.md
│  │  ├─ C8.5_OPTIMIZATION.md
│  │  ├─ C6.9_FIELD_REALISM.md
│  │  ├─ C12.1_DOCS_LOCKED.md
│  │  ├─ C13.5_DEVASTATION.md
│  │  ├─ C9_SIGNED_RELEASE.md
│  │  ├─ C14.1_CONTINUOUS_EVAL.md
│  │  ├─ C14.5_ADVERSARY_SHADOW.md
│  │  └─ C15.1_RUN_CONCLUDED.md
│  └─ README.md
├─ 11_product/
│  ├─ api/  cli/  configs/  telemetry_hooks/  README.md
├─ 12_field_kit/
│  ├─ runbooks/  checklists/  dashboards/  README.md
├─ 13_docs/
│  ├─ OPERATIONAL_README.md  USER_GUIDE.md  TROUBLESHOOTING.md  FAQ.md
│  └─ APPENDIX_HUMAN_STUDY.md
├─ 14_deployment/
│  ├─ packages/  env_profiles/  SELF_TESTS/  README.md
├─ 15_ce/
│  ├─ PLAN.md  RESULTS.md  README.md
├─ 16_graphs/
│  ├─ knowledge/  design/  ops/  README.md
├─ 17_artifacts_phasewise/
│  ├─ P-0.8_TRIZ/ … P15_Archival_Postmortem/
├─ 18_logs/
│  ├─ checkpoints/  traces/  README.md
├─ 19_assets/
│  └─ README.md
├─ 20_licenses/
│  ├─ LICENSES.spdx  THIRD_PARTY_NOTICES.md  RELEASE_MATRIX.md
└─ 99_reports/
   ├─ POSTMORTEM.md  KPI_SUMMARY.md  CHANGELOG.md
MANIFEST.yml (V49.0) — with Runner Catalog, Aliases & Gate UX — Patches 2 & 4
run_id: "S49"
title: "Spark: <short title>"
version: "V49.0"
risk_tier: "R2"
settings:
  mode: Full Run            # or Auto
  auto_gate_verbosity: full # full|brief
  auto_gate_preview: on     # on|off
runners:
  attached: []              # e.g., [code, physical]
  notes: "<why attached or declined>"
runner_catalog:
  code: true
  physical: true
  theory: true
  ot: true
  mobility: true
  lifesci: true
  agmrv: true
  fintech: true
runner_aliases:
  code:      [code, software, dev, ml, ai, agent, sdk, cli, api]
  physical:  [physical, hardware, device, mechatronics, mechanical, electrical, embedded_hw]
  theory:    [theory, math, proofs, axioms, conjectures]
  ot:        [ot, industrial, utilities, plc, scada, dcs, 61131, iec61131, 62443, nerc, 61850, goose, tia, studio5000]
  mobility:  [mobility, auto, automotive, autosar, ecu, avionics, do178, do178c, do254, robotics, robot, uav, agv, odd, sotif]
  lifesci:   [lifesci, pharma, pharmaceutical, gxp, gamp, annex11, 21cfr11, meddevice, medical, samd, clinical, hipaa]
  agmrv:     [agmrv, ag, agriculture, agtech, mrv, soil, carbon, field, trials, plots]
  fintech:   [fintech, finance, payments, pci, sox, aml, kyc, sanctions, banking]
runner_combo_aliases:
  embedded:             [code, physical]
  industrial-robotics:  [ot, mobility]
  medical-ai:           [code, lifesci]
  ag-robotics:          [physical, mobility, agmrv]
gates:
  c-0_8:     {status: PENDING, notes: ""}
  c-0_5a:    {status: PENDING, notes: ""}
  c-0_5:     {status: PENDING, notes: ""}
  c0_1:      {status: PENDING, notes: ""}
  c1_1:      {status: PENDING, notes: ""}
  c2_1:      {status: PENDING, notes: ""}
  c2_5:      {status: PENDING, notes: ""}
  c3_1:      {status: PENDING, notes: ""}
  c4_1:      {status: PENDING, notes: ""}
  c4_a:      {status: PENDING, notes: ""}
  c5_1:      {status: PENDING, notes: ""}
  c6_1:      {status: PENDING, notes: ""}
  c6_5:      {status: PENDING, notes: ""}
  c7:        {status: PENDING, notes: ""}
  c7_sigma:  {status: PENDING, notes: ""}
  c7_repro:  {status: PENDING, notes: ""}
  c8_1:      {status: PENDING, notes: ""}
  c8_4:      {status: PENDING, notes: ""}
  c8_5:      {status: PENDING, notes: ""}
  c6_9:      {status: PENDING, notes: ""}
  c12_1:     {status: PENDING, notes: ""}
  c13_5:     {status: PENDING, notes: ""}
  c9:        {status: PENDING, notes: ""}
  c14_1:     {status: PENDING, notes: ""}
  c14_5:     {status: PENDING, notes: ""}
  c15_1:     {status: PENDING, notes: ""}
ledgers:
  run: "07_ledgers/RUN_LEDGER.md"
  decisions: "07_ledgers/DECISION_LEDGER.md"
  assumptions: "07_ledgers/ASSUMPTION_LEDGER.md"
  evidence: "07_ledgers/EVIDENCE_LEDGER.md"
  benchmark: "07_ledgers/BENCHMARK_LEDGER.md"
  optimization: "07_ledgers/OPTIMIZATION_LEDGER.md"
  risk_safety: "07_ledgers/RISK_SAFETY_LEDGER.md"
  compliance: "07_ledgers/COMPLIANCE_LEDGER.md"
  contradiction: "07_ledgers/CONTRADICTION_LEDGER.md"
  ck: "07_ledgers/C_K_LEDGER.md"
  morph_futures: "07_ledgers/MORPH_FUTURES_LEDGER.md"
  adversary: "07_ledgers/ADVERSARY_LEDGER.md"
security_provenance:
  sbom: "09_security_provenance/SBOM.spdx.json"
  attestations_dir: "09_security_provenance/ATTESTATIONS"
  signatures: "09_security_provenance/SIGNATURES.txt"
safety_privacy:
  safety_case: "08_safety_privacy/SAFETY_CASE.md"
  misuse_tests: "08_safety_privacy/MISUSE_TESTS.md"
  dpia: "08_safety_privacy/PRIVACY_DPIA.md"
  ethics_of_use: "08_safety_privacy/ETHICS_OF_USE_CARD.md"
docs:
  operational: "13_docs/OPERATIONAL_README.md"
  user_guide: "13_docs/USER_GUIDE.md"
  troubleshooting: "13_docs/TROUBLESHOOTING.md"
  appendix_human: "13_docs/APPENDIX_HUMAN_STUDY.md"
deployment:
  packages: "14_deployment/packages/"
  env_profiles: "14_deployment/env_profiles/"
continuous_evaluation:
  plan: "15_ce/PLAN.md"
  results: "15_ce/RESULTS.md"
ttl_defaults:
  r1_days: 180
  r2_days: 90
  r3_days: 45
phase_artifacts_dir: "17_artifacts_phasewise/"
reports:
  postmortem: "99_reports/POSTMORTEM.md"
  kpi_summary: "99_reports/KPI_SUMMARY.md"
  changelog: "99_reports/CHANGELOG.md"
checksums_file: "00_manifest/CHECKSUMS.txt"
release_notes: "00_manifest/RELEASE_NOTES.md"
End of GCP V49.0— Fully Fleshed with Runner Aliases & Gate UX Fix.

