5.6 Spaceflight / Aerospace Runner 
runner: 
name: "Spaceflight / Aerospace" 
aliases: ["space","aero","sat","avionics","g&c","adcs"] 
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
20
- Operator 
- Scribe 
refusal_policy: 
- "Refuse concepts without launch/ops safety margins and RF/regulatory compliance." 
- "Refuse to ignore deorbit or end‑of‑life disposal requirements." agent_graph: "agents/space_agent_graph.json" 
memory_config: "memory/space_memory_config.yml" 
policy_module: "Policies/space.rego" 
micro_gates: 
- id: "TVAC‑Vibe‑EMC" 
description: "Thermal‑vacuum, vibration and EMC test plan/results (or justified analyses)" 
evidence: "06_evidence/stats/*" 
- id: "SEE‑Resilience" 
description: "Single event effects (SEE) latch‑up/SEFI/SET analysis & safe‑mode drills" 
evidence: "ADVERSARY_LEDGER.md" 
- id: "AIT‑Flow" 
description: "Assembly, integration and test flow + flight rules defined" evidence: "11_product/ICD/*" 
- id: "C7.Repro" 
description: "Env lock & seeds; simulation seeds recorded" 
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Guidance & control invariants hold under sensor latency, actuator saturation and orbital perturbations" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA satellites/payloads" evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Resilience to cyber‑attacks, SEFI/SEU injection and RF interference" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry plan covers power, thermal, attitude, communication; spans correlate anomalies" 
evidence: "observability/space_otel-plan.md" 
- id: "SupplyChain" 
description: "Bill of materials, SBOM, provenance and counterfeit part detection" 
evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test reconstructs the simulation and ground tests; replicates key mission metrics" 
evidence: "Rehydration_Test/space_status.json" 
21
metrics: 
- name: "power_margin_EOL" 
target: ">= target" 
- name: "unrecoverable_faults" 
target: "0 in flight rules simulations" 
- name: "novelty_score" 
target: ">= 0.45" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
- name: "radiation_tolerance" 
target: ">= mission lifetime" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # includes power margins,  pointing accuracy, payload data rate vs SOTA missions 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/space/*" 
observability_plan: "observability/space_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/space.intoto.jsonl" rehydration_script: "Rehydration_Test/space.sh" 
carbon_report: "Cost_Carbon_Report.md" # may include launch emissions  calculations 
artifacts_add: 
- path: "TVAC_PLAN.md" 
purpose: "Thermal‑vacuum test plan and results" 
- path: "VIBRATION_PLAN.md" 
purpose: "Vibration test plan and results" 
- path: "EMC_PLAN.md" 
purpose: "Electromagnetic compatibility test plan and results" - path: "SEE_ANALYSIS.md" 
purpose: "Single event effects analysis and mitigation plan" - path: "FLIGHT_RULES.md" 
purpose: "Flight rules, safe modes and fault management procedures" - path: "END_OF_LIFE_PLAN.md" 
purpose: "Deorbit or disposal plan" 
standards_refs: 
- name: "ECSS Space Engineering Standards" 
url_or_citation: "European Cooperation for Space Standardization (ECSS)" - name: "NASA‑STD‑8719.14 (Space Flight Safety)" 
url_or_citation: "NASA safety and mission assurance requirements" - name: "MIL‑STD‑1540 (Environmental Test Requirements for Aerospace Equipment)" 
url_or_citation: "Environmental test requirements" 
kickoff: 
prompt_template: | 
22

attach runner space 
Initiate GCP V49 for Spark: <space system/payload> 
Mode: <Full‑Run|Auto> • Risk: R3 
Context: mission orbit, payload, lifetime and regulatory domain Deliverables: TVAC/vibration/EMC plans, SEE resilience, AIT flow and  flight rules, BOM/SBOM/provenance, metamorphic & adversarial test results,  novelty score, carbon report, signed release 
