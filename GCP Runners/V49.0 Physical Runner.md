5.2 Physical / Hardware Runner 
runner: 
name: "Physical / Hardware" 
aliases: ["hardware","device","mechatronics","embedded"] 
risk_tier: "R2" 
confidence_target: 0.95 
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
9
- Scribe 
refusal_policy: 
- "Refuse designs lacking safety margins or verification plans." - "Refuse to use materials without traceable provenance." 
agent_graph: "agents/hardware_agent_graph.json" 
memory_config: "memory/hardware_memory_config.yml" 
policy_module: "Policies/hardware.rego" 
micro_gates: 
- id: "Safety‑FMEA" 
description: "Hazard analysis (FMEA) complete; mitigations verified" evidence: "07_ledgers/RISK_SAFETY_LEDGER.md" 
- id: "Verification‑Plan" 
description: "Test matrix for function, stress and environment defined and executed" 
evidence: "04_benchmarks/results/TEST_MATRIX.csv" 
- id: "C7.Repro" 
description: "Fixture/jig configurations & seeds logged; reproducibility tests executed" 
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Mechanical invariants hold (e.g., symmetrical load distribution, unit conversions)" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA devices" 
evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Red‑team attempts to exceed load, vibration or temperature limits are detected and mitigated" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Sensor telemetry (force, vibration, temperature) captured and correlated via OTEL" 
evidence: "observability/hardware_otel-plan.md" 
- id: "SupplyChain" 
description: "BOM with traceable provenance, SBOM for firmware and software components" 
evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test re‑creates the prototype and replicates core benchmarks" 
evidence: "Rehydration_Test/hardware_status.json" 
metrics: 
- name: "MTBF_target_met" 
target: "true" 
- name: "safety_incidents" 
target: "0 during test" 
10
- name: "thermal_margin" 
target: ">= specified" 
- name: "novelty_score" 
target: ">= 0.35" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # e.g., performance/spec  weight vs SOTA 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/hardware/*" 
observability_plan: "observability/hardware_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/hardware.intoto.jsonl" rehydration_script: "Rehydration_Test/hardware.sh" 
carbon_report: "Cost_Carbon_Report.md" # include embodied carbon for  materials when available 
artifacts_add: 
- path: "FMEA_PLAN.md" 
purpose: "Detailed failure modes and effects analysis plan" 
- path: "07_ledgers/LOAD_CASE_LEDGER.md" 
purpose: "Record of structural load cases and margins" 
- path: "BOM.csv" 
purpose: "Bill of materials with supplier data and compliance codes" - path: "SAFETY_CERTIFICATIONS.md" 
purpose: "Certification requirements (UL, CE, FCC, etc.)" 
standards_refs: 
- name: "ISO 12100 Safety of Machinery" 
url_or_citation: "Safety design and risk assessment for machinery" - name: "IEC 60601 (Medical Electrical Equipment)" 
url_or_citation: "Standards for medical electrical equipment safety" - name: "IPC‑2221 (PCB Design)" 
url_or_citation: "Generic standard on printed board design" 
kickoff: 
prompt_template: | 
attach runner hardware 
Initiate GCP V49 for Spark: <hardware invention> 
Mode: <Full‑Run|Auto> • Risk: R2 
Context: operating environment, regulatory constraints, target MTBF and  safety margins 
Deliverables: FMEA, verification plan, test matrix results, BOM/SBOM,  provenance, telemetry plan, metamorphic & adversarial test outcomes, novelty  score, signed release 
11
Agent graph (hardware_agent_graph.json): The Planner defines functional requirements and safety margins; the Researcher collects material properties and relevant standards; the Inventor proposes mechanical and electrical architectures; the Engineer creates prototypes and test fixtures with OTEL sensors; the Adversary attempts to stress components beyond spec; the Optimizer iteratively reduces weight and power while maintaining safety; the Auditor checks FMEA and SBOM; the Productizer prepares manufacturing documentation and compliance filings; the Operator validates assembly procedures; the Scribe maintains the ledgers and manifest. 
Memory config: Stores supplier data, material properties, and regulatory citations; redacts any proprietary manufacturing processes; retention rules keep FMEA and BOM indefinitely; scratchpad logs expire after the build phase. 
Metamorphic invariants: Symmetry in load distribution under mirror transformations; invariance of functional output when units are converted (metric vs imperial); monotonic stress/strain relationships under small increments; consistency of thermal profile under ambient temperature drift. 
Novelty benchmarks: Compare against SOTA devices for weight‑to‑strength ratio, power efficiency and MTBF; measure improvements in assembly time or cost; compute embedding distances between design graphs. 
Adversarial tests: Include over‑voltage, over‑current, mechanical shock, vibration, thermal cycling and EMI/EMC interference; verify the design meets safety and failsafe requirements. 
Observability plan: Define spans for each functional test (e.g., stress test, vibration test, thermal test); metrics include sensor readings, environmental conditions, pass/fail rates; logs include anomaly detection events and gating decisions. 
