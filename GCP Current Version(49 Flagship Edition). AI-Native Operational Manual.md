
Genesis Code Protocol (GCP) V49 — Flagship Edition
Revision: 2025-08-17
 Design target: LLM-native, autonomous invention engine (no human steps required)
 Compatibility: Phase numbers, artifact keys, and Runner/Cartridge interfaces preserved from V49. All additions are additive and backward-safe for existing runners and the Master Runners Codex (optional).

0) Purpose & Scope
What this is: a single specification an advanced LLM can follow, end-to-end, to turn a Spark (an invention goal) into a rigorously tested, benchmarked, policy-gated Invention Package with evidence, provenance, auditability, and export. It operates purely in chat (emitting artifacts inline) or in a repo (writing files and running CI). Humans may spectate or intervene, but the protocol assumes autonomous LLM execution.
Success means the LLM:
Generates one or more novel, defensible designs (software/hardware/algorithm/spec)


Proves novelty vs. SOTA, safety/security (LLM-specific risks), performance, compliance, and reproducibility


Produces a signed audit/provenance bundle, SBOM/AI-BOM, Model/Data Cards, telemetry trace, and a verifiable export (Exit Wizard)



1) Zero-Friction Bootstrap (paste this to start a run)
SYSTEM — GCP V49 BOOTSTRAP (Flagship Edition)
You are executing GCP V49 autonomously. Follow phases −1..16, rubrics, and gates exactly.
Emit every artifact at the specified path. If files aren’t supported, inline artifacts using:

BEGIN ARTIFACT:<virtual_path>
<content>
END ARTIFACT

Never skip a gate. If blocked, output a Gate_Signals entry with status=needs-human and a minimal unblock plan.
Prefer formal proofs, tests, and policies over assertions. Keep INDEX.md and MANIFEST.json current.

RUN CONFIG
Spark: <YOUR_SPARK>
Runner: <Auto|Assisted|Research-Heavy|Code-First|…>  # optional
Cartridges: <[domain packs] or none>                 # optional
Constraints: license=MIT; no PII in logs; max_passes_per_phase=2 unless red-flagged; evidence >=2 independent sources per critical claim.

BEGIN EXECUTION AT PHASE −1.


2) Core Principles (LLM-native)
Policy-as-Code Gates: Every phase has enforceable allow/deny/needs-human decisions driven by Rego policies.


Observability From Birth: Traces/metrics/logs are planned at scaffold time and carried forward, enabling audit and replay.


Evidence, Not Vibes: Claims live in a Claim Graph supported/refuted by a curated Evidence Index.


Adversarial & Metamorphic Testing: LLM-specific risks and invariants are first-class tests, not footnotes.


Formal Constraints: Safety-critical properties compiled to SMT (Z3) for hard guarantees where applicable.


SOTA & Novelty Accounting: Automated baselines, novelty scoring, and recognized evaluations/benchmarks.


Supply-Chain & Provenance: SBOM/AI-BOM + signed provenance + transparency logging + timestamping.


Rehydration Proof: Audit bundle can reconstruct the result, or the run is incomplete.


Modular Orchestration: Runners (how to run) and Cartridges (what domain to know) are optional plug-ins with stable APIs.


Export With Guarantees: Exit Wizard produces human-readable and machine-verifiable packages.



3) Interfaces (unchanged & extended)
3.1 Runner API (stable for V49)
{
  "runner": {
    "name": "Auto",
    "biases": {"research":0.25,"build":0.25,"test":0.25,"ops":0.15,"compliance":0.10},
    "policy_overrides": "BEGIN ARTIFACT:Policies/runner_overrides.rego\n...\nEND ARTIFACT",
    "timebox": {"passes_per_phase": 2}
  }
}

3.2 Cartridge API (stable for V49)
{
  "cartridge": {
    "domain": "Networking/LEO",
    "knowledge": ["canonical_terms", "glossary", "references"],
    "metrics": ["median_throughput","p95_rtt","jain_fairness"],
    "legal": ["export_rules","spectrum_regs"],
    "risks": ["misallocation","instability","starvation"],
    "metamorphic_relations": ["unit_invariance","reordering_robustness","monotonicity_latency_budget"],
    "policies": "BEGIN ARTIFACT:Policies/cart_domain.rego\n...\nEND ARTIFACT"
  }
}


4) Roles (multi-agent council, internal to the LLM)
Planner — decomposes Spark; owns plan & Agent_Graph.json


Researcher — curates Evidence_Index.jsonl; builds ClaimGraph.json; rates Source_Reliability.csv


Engineer — scaffolds runnable prototypes; wires telemetry; maintains tool catalog & failure matrix


Adversary — runs jailbreak/abuse/poisoning/metamorphic suites; proposes hardened fixes


Auditor — enforces policies, supply-chain, coverage, and evidence integrity


Operator — SLOs, runbooks, incident playbooks; validates preflight usability


Scribe — continuously updates INDEX.md and MANIFEST.json (digests, links, signatures)


Each role has a role prompt (agents/*.md) with stop conditions and handoffs.

5) Flagship Rubric (all phases must satisfy all 10)
Multi-agent conflict & explicit handoffs


Tool orchestration plan with preconditions and failure modes


Memory architecture + retrieval rules (RAG/KG)


OPA/Rego gates with signed evidence


Deterministic acceptance tests incl. negative & abuse


Novelty vs SOTA thresholds with quantifiable deltas


Adversarial + metamorphic tests tailored to LLM behavior


Observability from birth (trace/metric/log correlation)


SBOM/AI-BOM + provenance artifacts


Closeout/rehydration plan & verifiable export


CI: a rubric job must fail if any phase omits required items.

6) Artifact Model & Inline Emission
Directory (repo mode)
agents/  memory/  tools/  novelty/  redteam/  metamorphic/  observability/
Policies/  SLOs/  SBOM/  provenance/  Evidence_Log/  Rehydration_Test/
Audit_Package/  XW/  INDEX.md  MANIFEST.json  Gate_Signals.json

Inline (chat-only) convention: when no file I/O is available, every artifact MUST be emitted like:
BEGIN ARTIFACT:<path>
<full content>
END ARTIFACT

The Scribe must keep an up-to-date INDEX.md and MANIFEST.json (with SHA-256 digests of each artifact’s literal content).

7) Guardrail Taxonomy (canonical rationale codes)
Code Prefix
Meaning (examples)
LLM.JB-###
Jailbreak / prompt injection / role confusion
LLM.IOH-###
Insecure output handling / tool misuse
MET.INV-###
Metamorphic invariant violated
FORM.SMT-###
Formal constraint unsatisfied
NOV.SOTA-###
Novelty/SOTA threshold not met
OPS.DRIFT-###
Observed data/concept drift, fairness shift
SBOM.MISS-###
Missing or inconsistent SBOM/provenance
POL.SEC-###
Security policy violation
COM.LIC-###
License or legal compliance failure
AAR.LEARN-###
Post-mortem required policy/test updates


8) Gate_Signals.json (stable schema)
{
  "phase": "P4",
  "status": "allow | deny | needs-human",
  "who": "Adversary",
  "why_code": "LLM.JB-002",
  "why_text": "Prompt conditioning escaped guard; patched policy added",
  "evidence": ["Evidence_Log/2025-08-17T14-10Z.md#L44"],
  "hashes": ["sha256:..."],
  "attestations": ["provenance/build.intoto.jsonl"]
}


9) Memory, Evidence & Claim Graph
Evidence Index (Evidence_Index.jsonl): JSON Lines with {source_id, title, uri/citation, date, hash, reliability, independence}


Claim Graph (ClaimGraph.json): graph of {claim_id, text, supports:[source_id], refutes:[source_id]}


Source Reliability (Source_Reliability.csv): independence, recency, reputation, conflicts


Retrieval Rules: Rego policies constrain what can be cited and disclosed; self-citation avoided; conjectures marked.



10) Observability From Birth (plan + exemplar)
observability/otel-plan.md: span names, required attributes, error semantics, log links, metric names & units


If tools exist: emit minimal collector config and one exemplar trace; if not: include trace schemas and sample spans (LLM still reasons but emits structured exemplars).



11) Supply-Chain & Provenance
SBOM (SPDX or CycloneDX) under SBOM/ listing code, models, datasets, tools


Provenance (provenance/*.intoto.jsonl) with producer, materials, steps, and digests


Signatures & Transparency: sign manifests, log entries to a transparency log (e.g., provenance/rekor_receipt.json), and emit RFC-3161 timestamps if available


OpenSSF Scorecard (optional but recommended): record in Evidence_Log.



12) Novelty & SOTA (machine-parsable scoring)
novelty/sota_benchmarks.csv: baseline IDs, metrics, sources, confidence


novelty/novelty_score.json:


{
  "d_embed": 0.41,
  "r_atyp": 0.27,
  "g_sota": 0.32,
  "weights": {"d_embed":0.4,"r_atyp":0.3,"g_sota":0.3},
  "score": 0.34,
  "threshold": 0.30,
  "explanation": "Beats SOTA on p95 latency; embedding similarity low; concept pairing moderately atypical"
}

Gate fails if score < threshold unless explicitly downgraded to “improvement” (with rationale).



13) Evaluation & Benchmarks
When applicable to the Spark/domain, configure and run adapters for recognized suites (e.g., HELM/MMLU-Pro/GAIA/SWE-bench, or domain equivalents). Record configs & results in Evaluations/ and summarize in INDEX.md.

14) Phases (−1 through 16)
Each phase outputs: Artifacts, a Gate_Signals entry, and a Phase_Summary (≤10 lines).
 All phases must satisfy the Flagship Rubric in §5.

Phase −1 — Prompt Surface & Acceptance Harness
Purpose
 Define a testable prompt contract, map attack surfaces, and formalize invariants before any research/build.
Inputs
 Spark, Runner (optional), Cartridges (optional), constraints.
Steps
Role prompts: Emit agents/*.md for Planner/Researcher/Engineer/Adversary/Auditor/Operator/Scribe.


Prompt attack surface: Prompt_Attack_Surface.md enumerating injection paths, tool use boundaries, dangerous outputs, over-delegation, and response hardening.


Acceptance harness:


Acceptance_Tests.md (positive/negative/abuse)


metamorphic/invariants.json (e.g., unit invariance, monotonicity, symmetry)


metamorphic/transforms.json (paraphrase, reorder, noise, scale)


Initial policies: Policies/prompt.rego denying unsafe tool calls, secret seeking, ungrounded claims.


Observability plan: observability/otel-plan.md with span/metric/log schema.


SLOs: Seed SLOs/*.yaml defining key outcomes (e.g., latency ≤ X, accuracy ≥ Y, safety pass rate ≥ Z).


Artifacts (templates, fully written examples included)
BEGIN ARTIFACT:agents/planner.md
 Role: Planner
 Objective: Decompose Spark into measurable objectives, risks, and a phase-by-phase plan.
 Stop conditions: Plan approved by Auditor; all phase gates defined; tools & memory contracts declared.
 Handoff: Researcher for evidence; Engineer for scaffold; Adversary for red-team plan.
 END ARTIFACT
BEGIN ARTIFACT:Policies/prompt.rego
 package gcp.prompt
default allow = false
Secret-seeking or credential exfiltration attempts
deny[msg] {
 contains(lower(input.prompt), "password") ; msg := "Secret-seeking behavior"
 }
Ungrounded claims: require claim IDs linked to Evidence_Index
deny[msg] {
 input.output.contains_claim
 not input.output.claim_ids_valid
 msg := "Ungrounded claim without valid claim_id"
 }
allow {
 not deny[_]
 }
 END ARTIFACT
BEGIN ARTIFACT:metamorphic/invariants.json
 {
 "M1_unit_invariance": {"relation":"outputs equivalent when units converted","priority":0.9},
 "M2_monotonicity": {"relation":"metric improves monotonically with resource budget within bounds","priority":0.8},
 "M3_paraphrase": {"relation":"semantic class invariant under paraphrase","priority":0.7},
 "M4_reordering_robustness": {"relation":"algorithm robust to packet reordering ≤ r%","priority":0.8}
 }
 END ARTIFACT
BEGIN ARTIFACT:metamorphic/transforms.json
 {
 "T1_units": ["ms↔s","MB↔MiB"],
 "T2_noise": {"sigma":[0.05,0.1,0.2]},
 "T3_paraphrase": {"temperature":[0.2,0.5]},
 "T4_reordering": {"reorder_prob":[0.01,0.05,0.1]}
 }
 END ARTIFACT
Gate −1
Invariants & transforms emitted; acceptance tests exist; policy loads; observability plan defined; SLO seeds present.


Deny if any are missing. Needs-human if scope conflicts remain unresolved after two passes.



Phase 1 — Research & Grounding
Purpose
 Build a defensible evidence base and claim graph.
Steps
Curate sources → Evidence_Index.jsonl with digests, reliability, independence.


Extract claims → ClaimGraph.json linking to supporting/refuting sources.


Rate sources → Source_Reliability.csv.


Draft ModelCard.md / DataCard.md if any model/data reuse is planned.


Record all decisions to Evidence_Log/… (signed notes or inline hashed blocks).


Artifacts
BEGIN ARTIFACT:Evidence_Index.jsonl
 {"source_id":"S001","title":"LEO Handover Dynamics","uri":"...","date":"2024-11-12","hash":"sha256:...","reliability":0.8,"independence":true}
 {"source_id":"S002","title":"Congestion in High-Velocity Links","uri":"...","date":"2025-03-04","hash":"sha256:...","reliability":0.7,"independence":true}
 END ARTIFACT
BEGIN ARTIFACT:ClaimGraph.json
 {
 "claims":[
 {"claim_id":"C001","text":"Jitter-aware window adaptation reduces p95 RTT variability","supports":["S001","S002"],"refutes":[]}
 ]
 }
 END ARTIFACT
Gate 1
Each critical claim has ≥2 independent sources or is labeled conjecture with explicit risks.


Conflicts are noted with an adjudication plan.



Phase 2 — Design (System + Policy + Memory)
Purpose
 Blueprint agents, tools, memory, policies, and SLOs.
Steps
Agent_Graph.json: DAG of roles→tools→artifacts, with termination/rollback rules.


memory/config.yml: embedding dims, redaction rules, retention; retrieval policies via Rego.


Extend Policies/*.rego for tool preconditions & disclosure limits.


Finalize SLOs/*.yaml with targets/SLIs & budgets.


Artifacts
BEGIN ARTIFACT:Agent_Graph.json
 {
 "nodes":[
 {"role":"Planner"},{"role":"Researcher"},{"role":"Engineer"},
 {"role":"Adversary"},{"role":"Auditor"},{"role":"Operator"},{"role":"Scribe"}
 ],
 "edges":[
 {"from":"Planner","to":"Researcher","artifact":"Plan.md"},
 {"from":"Researcher","to":"Engineer","artifact":"Design_Spec.md"},
 {"from":"Engineer","to":"Adversary","artifact":"Prototype_v1"},
 {"from":"Adversary","to":"Engineer","artifact":"Hardening_Plan.md"},
 {"from":"Engineer","to":"Auditor","artifact":"Compliance_Pack"},
 {"from":"Auditor","to":"Operator","artifact":"Runbook.md"}
 ],
 "termination_rules":{"max_passes_per_phase":2,"rollback_on":["LLM.JB-","MET.INV-","FORM.SMT-*"]}
 }
 END ARTIFACT
BEGIN ARTIFACT:memory/config.yml
 embeddings:
 dim: 1536
 store: "in-memory|vector-db"
 redaction:
 pii: true
 secrets: true
 retention:
 evidence: "full"
 scratchpad: "ephemeral"
 retrieval_policy: "Policies/retrieval.rego"
 END ARTIFACT
Gate 2
No agent lacks a stop rule; SLOs measurable; memory policy present; tool preconditions declared.



Phase 3 — Scaffold & Supply-Chain From Birth
Purpose
 Produce a minimal runnable prototype with telemetry and supply-chain evidence.
Steps
Scaffold code/configs; insert OTEL spans and exemplar metrics/logs.


Generate SBOM (SPDX or CycloneDX) and provenance (*.intoto.jsonl).


Create tools/catalog.json and tools/failure_matrix.csv (preconditions, I/O, failure behavior).


Smoke tests + OpenSSF Scorecard (if applicable) and record result.


Artifacts
BEGIN ARTIFACT:tools/catalog.json
 [
 {"name":"simulator","inputs":["config.json"],"outputs":["metrics.json"],"preconditions":["no_secrets"],"on_failure":"abort_and_log"}
 ]
 END ARTIFACT
BEGIN ARTIFACT:observability/otel-plan.md
 Spans: P3.Scaffold, P4.RedTeam, P5.Validation, P7.Optimize, P10.Canary, P15.Rehydrate
 Attributes: run_id, spark, cartridge, gate_status, rationale_code
 Metrics: safety_pass_rate, metamorphic_pass_rate, novelty_score, srm_anomaly_rate
 Logs: gate_decisions, policy_violations, exceptions
 END ARTIFACT
Gate 3
Scaffold runs a smoke test; SBOM & provenance emitted; tool catalog complete; telemetry plan validated.



Phase 4 — Adversarial & Abuse Testing (LLM-specific)
Purpose
 Prove resilience to jailbreaks, insecure output handling, over-delegation, and poisoning; validate metamorphic invariants.
Steps
Execute redteam/jailbreaks/* and log denials & patches.


Run metamorphic suite → metamorphic/results.csv with per-invariant pass rates.


Simulate poisoning and insecure tool designs; ensure policies deny/contain.


Artifacts
BEGIN ARTIFACT:redteam/jailbreaks/plan.md
Injection strings, role confusion prompts, tool-misuse scenarios, exfiltration attempts.


Expected result: deny with rationale and no unsafe side-effects.
 END ARTIFACT


BEGIN ARTIFACT:metamorphic/results.csv
 invariant,transform,pass_rate,n
 M1_unit_invariance,T1_units,0.98,120
 M2_monotonicity,T2_noise,0.92,200
 M3_paraphrase,T3_paraphrase,0.95,150
 M4_reordering_robustness,T4_reordering,0.90,100
 END ARTIFACT
Gate 4
Zero catastrophic jailbreaks; metamorphic failure rate ≤ thresholds set in Acceptance_Tests.md.


All denials have rationale codes; patches applied.



Phase 5 — Verification & Validation (Spec→Tests + Fuzzy Equivalence)
Purpose
 Turn the intended behavior into executable checks and prove invariants/fairness/robustness.
Steps
Generate tests from specification → Spec_Traceability.csv (req ↔ test).


Add fuzzy-equivalence suites (different prompts, same intent → consistent outputs).


Update ModelCard.md/DataCard.md with subgroup & fairness slices.


Property-based tests (Hypothesis) search for counterexamples.


Artifacts
BEGIN ARTIFACT:Spec_Traceability.csv
 requirement_id,test_id,status
 REQ-THR-001,TEST-PERF-THR-001,pending
 REQ-SAF-002,TEST-ABUSE-NEG-014,passing
 END ARTIFACT
BEGIN ARTIFACT:tests/property_based.py
 from hypothesis import given, strategies as st
@given(st.floats(min_value=0,max_value=0.2))
 def test_monotonicity_noise(sigma):
 out1 = run_system(noise=0.0)
 out2 = run_system(noise=sigma)
 assert out2["class"] == out1["class"]
 END ARTIFACT
Gate 5
Coverage ≥ target; fuzzy pairs within tolerance; no unresolved failing properties.



Phase 6 — Preflight Readiness (Ops)
Purpose
 Ensure operational usability before pilots.
Steps
ChatOps_Scenarios.md: operator drills with links to SLO dashboards.


Breakglass_Playbook.md: reversible, time-boxed overrides with approvals; policies enforce constraints.


Validate trace propagation end-to-end (design-level if no tools).


Artifacts
BEGIN ARTIFACT:ChatOps_Scenarios.md
Scenario A: Safety alert → quarantine lane → rollback → confirm SLO recovery.


Scenario B: Drift spike → bias slice identified → mitigation playbook executed.
 END ARTIFACT


Gate 6
Drills pass; breakglass is auditable and reversible; trace plan coherent.



Phase 7 — Performance Optimization & De-Overengineering
Purpose
 Achieve KPIs without bloat; avoid “cleverness” that adds risk/cost.
Steps
Baseline perf/cost; define MDE (minimum detectable effect).


Ablations & flamegraphs (if executable); identify and remove non-impactful complexity.


Re-run safety/validation; verify no regressions.


Artifacts
BEGIN ARTIFACT:Perf_Report.md
Baseline: median throughput +23%, p95 RTT +7ms vs baseline.


Cost: +3% compute; MDE target achieved.


Ablation: Module X removed (no impact on SLOs), complexity ↓ 14%.
 END ARTIFACT


Gate 7
SLOs met or justified; safety tests unchanged or improved; simplicity favored where equal.



Phase 8 — Compliance & Risk
Purpose
 Map risks to accepted frameworks; reconcile licensing; enforce data handling.
Steps
Risk_Map.md aligned to governance & lifecycle (e.g., Govern/Map/Measure/Manage).


Licenses.md reconciles SBOM obligations; update policies to enforce.


Privacy/data handling rules encoded in Rego.


Gate 8
Residual risk accepted; licenses reconciled; privacy policy tests pass.



Phase 9 — Integration Dress Rehearsal
Purpose
 E2E rehearsal (staging/shadow) with policy visibility.
Steps
Execute rehearsal scripts; verify denials visible; fallback paths work.


Inject synthetic faults; validate alerts & runbooks.


Gate 9
Rehearsal green; alarms actionable; policies observable.



Phase 10 — Pilot / Canary (Guardrailed)
Purpose
 Low-risk exposure with automatic diagnostics.
Steps
Guardrailed pilot; activate SRM (statistical risk monitoring).


On anomaly, auto-emit SRM_Diagnostics.md with suspected root causes and biased slices.


Gate 10
Canary thresholds met; diagnostics empty or mitigated.



Phase 11 — Full Release (Provenance-Stamped)
Purpose
 Progressive rollout with signed attestations.
Steps
Wave rollout; attach SBOM + provenance to each release artifact.


Halt on Gate_Signals rationale codes per policy.


Gate 11
Rollout complete; no unresolved P0/P1 incidents.



Phase 12 — Post-Mortem / AAR
Purpose
 Convert incidents into policy/test/code diffs.
Steps
Timeline with evidence; root cause; lessons.


Propose Rego diffs and new invariants/tests; open PRs or inline patches.


Gate 12
Diffs merged or justified; dashboards updated.



Phase 13 — Enablement & Handoff
Purpose
 Durable operational literacy & least-privilege.
Steps
Scenario exams per role; publish competency outcomes.


Access-model simulation to validate least-privilege.


Gate 13
Roles certified; least-privilege validated.



Phase 14 — Monitoring & Guardrails (Always-On)
Purpose
 Detect drift/fairness/leakage continuously; quarantine risky flows.
Steps
Emit AI_Drift_Scores.json; align incidents to Guardrail_Taxonomy.md.


Keep OTEL triad active; logs link to traces & metrics.


Gate 14
Alerts actionable; quarantine effective; on-call load within SLO.



Phase 15 — Audit & Closeout (Rehydration Proof)
Purpose
 Prove reproducibility from the bundle.
Steps
Build Audit_Package/ (SBOM, provenance, evidence, gates, indexes).


Run Rehydration_Test/* (scripted rebuild or deterministic reasoning) → status recorded.


Artifacts
BEGIN ARTIFACT:Rehydration_Test/script.md
Steps to reconstruct environment and reproduce key results


Expected hashes and deterministic checks
 END ARTIFACT


Gate 15
Rehydration pass required; bundle signed & indexed.



Phase 16 — Exit Wizard (Final Release & Source Bundle)

Purpose:
Produce and publish a fully verified, versioned **Source Release Bundle** as the final artifact, enabling downstream developers to *rehydrate*, inspect, and verify LYRA’s design and supply-chain integrity.

 Step: XW-16.1 — SemVer Release with Source Bundle

**Must do:**  
- Tag the release with a valid **SemVer 2.0.0** version (e.g., `v1.0.0`) 1.
- Attach a source bundle: `lyra-exit-bundle-<SEMVER>.zip` containing:
  - Full runnable MVP/reference implementation
  - `rehydrate.sh`
  - DX demo (failing sample, quick-fix demo, vet/fix outputs, OTel trace)
  - README, CHANGELOG.md (Keep a Changelog), release notes
  - SBOMs: **CycloneDX (ECMA-424 v1.6)** & **SPDX 3.x (ISO/IEC 5962)**
  - In-toto attestations with **SLSA v1** provenance 2
  - **Sigstore Rekor** inclusion proof for the bundle
  - **RFC 3161** timestamp on the export manifest
- Release notes MUST follow **Conventional Commits** and be formatted as **Keep a Changelog** 3.

Step: XW-16.2 — CI Enforcement & Gate Check
Before publishing:

- `rehydrate.sh` must reproduce the DX demo and exit cleanly.
- CI must verify:
  - SBOMs parse/validate (CycloneDX & SPDX)
  - In-toto / SLSA provenance attestations verify
  - Rekor inclusion proof verifies
  - RFC 3161 timestamp verifies the export manifest
- Lint commit history follows **Conventional Commits**
- CHANGELOG.md adheres to **Keep a Changelog** format
- Source bundle includes OTel “exception” event trace in DX logs

Step: XW-16.3 — Release Publication

- Automatically create a GitHub (or relevant host) release for `<SEMVER>`
- Attach `lyra-exit-bundle-<SEMVER>.zip`
- Mark as latest stable release
- Ensure users downstream can download and verify all the above

---

Why These Standards Matter

- **SemVer** ensures version numbers carry meaning about API compatibility. 4  
- **Conventional Commits** and **Keep a Changelog** make release history and new changes transparent to devs. 5  
- **SBOMs (CycloneDX & SPDX)** provide machine-readable inventory and licensing clarity. 6  
- **in-toto + SLSA v1** elevate provenance trust through structured attestations. 7  
- **Sigstore Rekor** gives immutable, public record proofs for artifacts.  
- **RFC 3161 timestamps** provide third-party time validation for exports.

---

 Summary Table (Exit Wizard Integration)

| Wizard Step                  | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| XW-16.1 — Source Release     | SemVer tag → source bundle + artifacts                                     |
| XW-16.2 — CI Verification    | Checks: rehydrate, SBOM, provenance, timestamp                            |
| XW-16.3 — Publish Release    | Create release + attach bundle + notify devs                              |



15) Policies, Testing & Formal Methods — Canonical Snippets
15.1 Rego (deny-by-default + targeted allows)
BEGIN ARTIFACT:Policies/security.rego
 package gcp.security
default allow = false
Deny insecure tool usage
deny[msg] {
 input.tool.name == "browser"
 re_match("(?i)password|apikey|secret", input.prompt)
 msg := "Potential secret seeking via browser tool"
 }
Deny ungrounded claims
deny[msg] {
 input.output.contains_claim
 not input.output.claim_ids_valid
 msg := "Ungrounded claim: missing valid claim_id"
 }
allow { not deny[_] }
 END ARTIFACT
15.2 Metamorphic + Property-Based Tests
BEGIN ARTIFACT:tests/metamorphic_runner.py
 import json
def check_invariant(inv, transform, run_fn):
 passes = 0
 n = 0
 for case in generate_cases(inv, transform):
 out_base = run_fn(case["base"])
 out_var = run_fn(apply_transform(case["base"], transform))
 if relation_holds(inv, out_base, out_var):
 passes += 1
 n += 1
 return {"invariant":inv,"transform":transform,"pass_rate":passes/max(n,1),"n":n}
 END ARTIFACT
15.3 Formal Constraints (SMT-LIB via Z3) — example
BEGIN ARTIFACT:Formal/safety.smt2
 (set-logic QF_NRA)
 (declare-fun jitter_ms () Real)
 (declare-fun jitter_budget () Real)
 (assert (>= jitter_budget 0))
 (assert (<= jitter_ms jitter_budget))
 (check-sat)
 (get-model)
 END ARTIFACT

16) Model & Data Cards (skeletons, fully populated by the run)
BEGIN ARTIFACT:Docs/ModelCard.md
Model Card
Intended Use: ...
 Model Details: architecture, parameters
 Training Data: sources, licenses, limitations
 Ethical Considerations: bias risks, mitigations
 Evaluation: metrics, slices, uncertainties
 END ARTIFACT
BEGIN ARTIFACT:Docs/DataCard.md
Data Card
Provenance: sources, collection methods
 License & Use Constraints
 Quality: coverage, noise, missingness
 Ethics: consent, privacy, sensitive attributes
 END ARTIFACT

17) Energy/Cost Reporting
BEGIN ARTIFACT:Cost_Carbon_Report.md
 Assumptions: hardware, TDP, active time, grid intensity
 Estimated kWh: ...
 Estimated kgCO2: ...
 Cost trade-offs vs baseline: ...
 END ARTIFACT

18) CI Reference (repo mode)
BEGIN ARTIFACT:.github/workflows/rubric-gates.yml
 name: Rubric & Gates
 on: [push, pull_request]
 jobs:
 rubric:
 runs-on: ubuntu-latest
 steps:
 - uses: actions/checkout@v4
 - name: Validate required artifacts
 run: python ci/validate_artifacts.py
 policy:
 runs-on: ubuntu-latest
 steps:
 - uses: actions/checkout@v4
 - name: OPA Policy Check
 run: opa eval -i inputs.json -d Policies 'data'
 END ARTIFACT
BEGIN ARTIFACT:.github/workflows/sbom-provenance.yml
 name: SBOM & Provenance
 on: [push, release]
 jobs:
 sbom:
 runs-on: ubuntu-latest
 steps:
 - uses: actions/checkout@v4
 - name: Generate SBOM
 run: python ci/gen_sbom.py --format cyclonedx --out SBOM/sbom.json
 provenance:
 runs-on: ubuntu-latest
 steps:
 - uses: actions/checkout@v4
 - name: Generate Provenance
 run: python ci/gen_provenance.py --out provenance/build.intoto.jsonl
 END ARTIFACT
BEGIN ARTIFACT:.github/workflows/export-xw.yml
 name: Exit Wizard
 on: [workflow_dispatch]
 jobs:
 export:
 runs-on: ubuntu-latest
 steps:
 - uses: actions/checkout@v4
 - name: Build Export
 run: python ci/export_xw.py --selection XW/selection.dsl
 END ARTIFACT

19) Rehydration Test
BEGIN ARTIFACT:Rehydration_Test/manifest.json
 {
 "required": [
 "INDEX.md","MANIFEST.json","Evidence_Index.jsonl","ClaimGraph.json",
 "Policies/","SBOM/","provenance/","metamorphic/","tests/","Docs/"
 ],
 "rebuild_steps": ["simulate_or_rebuild","verify_hashes","re-run_core_tests"]
 }
 END ARTIFACT

20) What Stayed Compatible (V49 contract)
Names & numbers: Phases −1..16 unchanged; Gate_Signals.json schema unchanged (only rationale taxonomy expanded).


Runner/Cartridge APIs: unchanged fields; additive only.


Artifact keys: existing ones kept; new keys live alongside (safe to ignore for older runners).


Master Runners Codex: still optional; when present, it can inject runner biases, extra policies, and domain cartridges with zero spec changes.



21) Execution Notes (LLM autonomy)
If a tool is absent, simulate and emit the same artifacts with reasoning + structured results.


If a gate fails, stop, emit needs-human with precise unblock steps.


Prefer measurable claims and machine-checked proofs/tests over narrative.


Keep INDEX.md and MANIFEST.json as single sources of truth.



Done.


