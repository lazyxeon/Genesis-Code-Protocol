5.7 Disaster Relief & Humanitarian Ops Runner 
runner: 
name: "Disaster Relief & Humanitarian" 
aliases: ["disaster","humanitarian","emergency","ics","nims","sphere"] risk_tier: "R3" 
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
- "Refuse bypass of Incident Command System (ICS) or National Incident Management System (NIMS) structures." 
- "Refuse PII data sharing without Accountability and Privacy (AAP)/DPIA." - "Refuse plans that violate Sphere minimum standards or local laws." agent_graph: "agents/disaster_agent_graph.json" 
memory_config: "memory/disaster_memory_config.yml" 
policy_module: "Policies/disaster.rego" 
micro_gates: 
- id: "ICS‑Structure" 
description: "Incident Command System structure defined and aligned with FEMA NIMS" 
evidence: "Runners/Exotics/Cartridges/Disaster/artifacts/ICS_STRUCTURE.md" - id: "Sphere‑Matrix" 
description: "Response mapped to Sphere minimum standards for 
humanitarian response" 
evidence: "Runners/Exotics/Cartridges/Disaster/artifacts/ 
SPHERE_MATRIX.csv" 
- id: "Data‑Responsibility" 
description: "Data responsibility assessment (IASC/OCHA) complete; PII 23

and sensitive info handled appropriately" 
evidence: "Runners/Exotics/Cartridges/Disaster/artifacts/ 
DATA_RESP_ASSESSMENT.md" 
- id: "TTX" 
description: "Tabletop exercise (TTX) performed; after‑action items closed" 
evidence: "Runners/Exotics/Cartridges/Disaster/artifacts/ICS_TTX.md" - id: "C7.Repro" 
description: "Environment lock; scenario seeds and simulation states logged" 
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Response recommendations robust under variations in hazard magnitude, demographics and resource availability" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA disaster response frameworks" 
evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Detection and mitigation of misinformation, adversarial classification and resource misallocation attacks" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry logs resource allocation, incident timeline and decision rationale" 
evidence: "observability/disaster_otel-plan.md" 
- id: "SupplyChain" 
description: "Supply chain for relief goods documented; SBOM for supporting software" 
evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test replays the response simulation and reproduces key metrics (lives saved, resources delivered on time)" evidence: "Rehydration_Test/disaster_status.json" 
metrics: 
- name: "lives_livelihoods_at_risk" 
target: "document reduction logic; no harm introduced" 
- name: "aap_compliance" 
target: "100%" # accountability and privacy compliance 
- name: "novelty_score" 
target: ">= 0.40" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
- name: "ttx_action_closure" 
target: "100% closed" 
tool_catalog: "tools/catalog.json" 
24

failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # e.g., Sphere indicator  scores, response times in similar crises 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/disaster/*" 
observability_plan: "observability/disaster_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/disaster.intoto.jsonl" rehydration_script: "Rehydration_Test/disaster.sh" 
carbon_report: "Cost_Carbon_Report.md" # optional energy use for simulations  and logistics 
artifacts_add: 
- path: "Runners/Exotics/Cartridges/Disaster/standards_map.md" purpose: "Normative mapping of humanitarian standards (Sphere, NIMS, Data Responsibility)" 
- path: "Runners/Exotics/Cartridges/Disaster/micro_gates.md" 
purpose: "Detailed descriptions of micro‑gates" 
- path: "Runners/Exotics/Cartridges/Disaster/metrics.md" 
purpose: "Metrics definitions and targets" 
- path: "Runners/Exotics/Cartridges/Disaster/artifacts/ICS_STRUCTURE.md" purpose: "ICS organisational chart and roles" 
- path: "Runners/Exotics/Cartridges/Disaster/artifacts/SPHERE_MATRIX.csv" purpose: "Matrix mapping Sphere minimum standards to response activities" - path: "Runners/Exotics/Cartridges/Disaster/artifacts/ 
DATA_RESP_ASSESSMENT.md" 
purpose: "Data responsibility and privacy assessment" 
- path: "Runners/Exotics/Cartridges/Disaster/artifacts/ICS_TTX.md" purpose: "TTX script and after‑action report" 
standards_refs: 
- name: "Sphere Handbook" 
url_or_citation: "Sphere minimum standards in humanitarian response" - name: "FEMA NIMS & Incident Command System" 
url_or_citation: "IS‑700 NIMS; IS‑200 initial response" 
- name: "IASC/OCHA Data Responsibility Guidance" 
url_or_citation: "Operational guidance (2021)" 
- name: "ReliefWeb Code of Conduct" 
url_or_citation: "Humanitarian principles and code of conduct" kickoff: 
prompt_template: | 
attach runner disaster 
Initiate GCP V49 for Spark: <response tool/plan> 
Mode: <Full‑Run|Auto> • Risk: R3 
Context: hazard type, jurisdiction, affected population, available  resources 
Deliverables: Incident command structure, Sphere mapping, data  25

responsibility note, TTX and after‑action report, metamorphic & adversarial test  results, novelty score, signed release 
