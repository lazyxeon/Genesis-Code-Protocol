5.8 Sports & Athletics Runner 
runner: 
name: "Sports & Athletics" 
aliases: ["sports","athlete","coaching","sport‑science"] 
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
- "Refuse medical guidance; defer to licensed clinician." 
- "Refuse doping circumvention; enforce WADA rules." 
- "Refuse programmes that ignore athlete consent and welfare." 
agent_graph: "agents/sports_agent_graph.json" 
memory_config: "memory/sports_memory_config.yml" 
policy_module: "Policies/sports.rego" 
micro_gates: 
- id: "ConcussionProtocolOK" 
description: "Use latest consensus return‑to‑play model (Amsterdam 2022) with individual baseline testing" 
evidence: "EVIDENCE_LEDGER.md" 
- id: "HydrationHeatOK" 
description: "Heat acclimatization & hydration plan based on ACSM/NFHS guidance" 
evidence: "Runners/Exotics/Cartridges/Sports/artifacts/ 
SPORTS_USE_POLICY.md" 
- id: "AntiDopingOK" 
description: "WADA Prohibited List screening and therapeutic use exemption handling" 
evidence: "Runners/Exotics/Cartridges/Sports/artifacts/WADA_SCREEN.csv" - id: "LoadMgmtOK" 
description: "Acute:Chronic load monitoring and delta limits defined" evidence: "Runners/Exotics/Cartridges/Sports/artifacts/LOAD_MONITOR.csv" - id: "C7.Repro" 
26
description: "Training plans and sensor data seeds recorded" evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Training outcomes invariant to moderate scheduling shifts and minor parameter perturbations" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA training & recovery regimes" 
evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Detection of overtraining, dehydration, doping, and misclassification of injury risk" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry covers training load, HRV, RPE, sleep and environmental factors; dashboards configured" 
evidence: "observability/sports_otel-plan.md" 
- id: "SupplyChain" 
description: "SBOM for wearables/app and provenance for supplements" evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test reproduces training outcomes from log data" evidence: "Rehydration_Test/sports_status.json" 
metrics: 
- name: "medical_deferral_compliance" 
target: "1.0" # all flagged athletes referred to clinician 
- name: "wada_conflict_hits" 
target: "0" 
- name: "load_spike_index" 
target: "within threshold policy" 
- name: "novelty_score" 
target: ">= 0.40" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # includes normative  training benchmarks, return‑to‑play metrics 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/sports/*" 
observability_plan: "observability/sports_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/sports.intoto.jsonl" rehydration_script: "Rehydration_Test/sports.sh" 
carbon_report: "Cost_Carbon_Report.md" 
27
artifacts_add: 
- path: "Runners/Exotics/Cartridges/Sports/standards_map.md" purpose: "Mapping of sports‑science standards (concussion consensus, WADA, ACSM)" 
- path: "Runners/Exotics/Cartridges/Sports/micro_gates.md" 
purpose: "Detailed descriptions of micro‑gates" 
- path: "Runners/Exotics/Cartridges/Sports/metrics.md" 
purpose: "Metrics definitions and targets" 
- path: "Runners/Exotics/Cartridges/Sports/artifacts/SPORTS_USE_POLICY.md" purpose: "Use limits and hydration/heat policy" 
- path: "Runners/Exotics/Cartridges/Sports/artifacts/WADA_SCREEN.csv" purpose: "Matrix for doping screening" 
- path: "Runners/Exotics/Cartridges/Sports/artifacts/LOAD_MONITOR.csv" purpose: "Load monitoring and acute:chronic ratios" 
standards_refs: 
- name: "6th Int’l Concussion in Sport Consensus (Amsterdam 2022)" url_or_citation: "Return‑to‑sport framework" 
- name: "WADA 2025 Prohibited List" 
url_or_citation: "List in force 1 Jan 2025 + Q&A" 
- name: "ACSM/NFHS Heat Hydration & Acclimatization" 
url_or_citation: "Position and consensus resources on heat & hydration" - name: "IOC Athlete Safeguarding" 
url_or_citation: "International Olympic Committee guidelines on athlete safety" 
kickoff: 
prompt_template: | 
attach runner sports 
Initiate GCP V49 for Spark: <athlete performance tool> 
Mode: <Full‑Run|Auto> • Risk: R3 
Context: sport, age group, competition level, environmental conditions Deliverables: concussion/heat policies, WADA screen, load plan,  metamorphic & adversarial test results, novelty score, signed release 
