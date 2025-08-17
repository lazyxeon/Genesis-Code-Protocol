5.5 Deep‑Sea Exploration Runner 
runner: 
name: "Deep‑Sea Exploration" 
aliases: ["deepsea","auv","rov","hadal","subsea"] 
risk_tier: "R3" 
confidence_target: 0.975 
roles: 
- Planner 
- Researcher 
- Inventor 
- Engineer 
- Adversary 
- Optimizer 
- Auditor 
- Productizer 
- Operator 
- Scribe 
refusal_policy: 
- "Refuse concepts lacking legal permits or habitat protection plans." - "Refuse operations without pressure/safety margins and recovery plans." agent_graph: "agents/deepsea_agent_graph.json" 
memory_config: "memory/deepsea_memory_config.yml" 
policy_module: "Policies/deepsea.rego" 
micro_gates: 
- id: "Sea‑Legal‑ScopeOK" 
description: "Jurisdiction/EEZ/permits documented; community engagement complete" 
evidence: "13_docs/COMMUNITY_ENGAGEMENT_AND_PERMITS.md" 
- id: "SOTA‑DepthClassOK" 
description: "Depth‑rated components credible for target class; SOTA comparison performed" 
evidence: "EVIDENCE_LEDGER.md; novelty/novelty_score.json" 
- id: "Recovery‑Plan" 
description: "Recovery and emergency procedures defined and validated" evidence: "07_ledgers/RISK_SAFETY_LEDGER.md" 
- id: "C7.Repro" 
description: "Bench simulations and test tank experiments logged" evidence: "06_evidence/replication/*" 
18
- id: "Metamorphic" 
description: "Sensor and control invariants hold under pressure, temperature and salinity variations" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA deep‑sea vehicles/ instruments" 
evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Adversary attempts to cause loss of control, sensor spoofing or data exfiltration are mitigated" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry from sensors, control loops and mission logs captured via OTEL" 
evidence: "observability/deepsea_otel-plan.md" 
- id: "SupplyChain" 
description: "Parts provenance (pressure vessels, electronics), SBOM for firmware and software" 
evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test reruns bench simulations and control loops; replicates mission logs" 
evidence: "Rehydration_Test/deepsea_status.json" 
metrics: 
- name: "structural_margin" 
target: ">= safety factor target" 
- name: "mission_success_rate" 
target: ">= 0.9 in trials" 
- name: "novelty_score" 
target: ">= 0.45" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
- name: "permit_compliance" 
target: "100%" # All required permits obtained and respected tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # includes hadal vehicle  depth ratings, sensor payload capability 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/deepsea/*" 
observability_plan: "observability/deepsea_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/deepsea.intoto.jsonl" rehydration_script: "Rehydration_Test/deepsea.sh" 
carbon_report: "Cost_Carbon_Report.md" 
19
artifacts_add: 
- path: "13_docs/COMMUNITY_ENGAGEMENT_AND_PERMITS.md" 
purpose: "Documentation of stakeholder engagement, ethics review and permits" 
- path: "RECOVERY_PLAN.md" 
purpose: "Emergency procedures and fail‑safe plan" 
- path: "07_ledgers/DEPTH_CLASS_LEDGER.md" 
purpose: "Depth rating evidence ledger" 
- path: "MISSION_PROFILE.md" 
purpose: "Mission profile and operational constraints" 
standards_refs: 
- name: "UNCLOS (United Nations Convention on the Law of the Sea)" url_or_citation: "Jurisdictional framework for ocean exploration" - name: "ICRA Deep‑Sea Submersible Guidelines" 
url_or_citation: "Best practices for human and robotic deep‑sea exploration" 
- name: "ISO 13354 (Petroleum and natural gas industries – Drilling and production)" 
url_or_citation: "Guidance on subsea equipment design" 
kickoff: 
prompt_template: | 
attach runner deepsea 
Initiate GCP V49 for Spark: <subsea system/instrument> 
Mode: <Full‑Run|Auto> • Risk: R3 
Context: target depth class, payload requirements, habitat protection  plan, regulatory jurisdiction 
Deliverables: permits & ethics dossier, depth class evidence, recovery  plan, SBOM/provenance, metamorphic & adversarial test results, novelty score,  signed release 
