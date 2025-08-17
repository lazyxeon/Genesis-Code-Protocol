5.20 Energy & Power Systems Runner 
runner: 
name: "Energy & Power Systems" 
aliases: ["energy","grid","storage","power","renewables"] 
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
- Scribe 
refusal_policy: 
- "Refuse unsafe interconnect proposals; grid safety first." 
- "Refuse designs that violate local or national interconnection standards." - "Refuse to proceed without resilience and reliability analysis (e.g., N‑1 contingency)." 
agent_graph: "agents/energy_agent_graph.json" 
memory_config: "memory/energy_memory_config.yml" 
policy_module: "Policies/energy.rego" 
micro_gates: 
- id: "Safety‑Interconnect" 
description: "Protection/relay/inrush analyses complete; islanding and grounding plans defined" 
evidence: "EVIDENCE_LEDGER.md" 
- id: "Reliability" 
description: "N‑1 contingency and tail‑risk checks performed" 
evidence: "BENCHMARK_LEDGER.md" 
- id: "C7.Repro" 
description: "Simulation seeds recorded; renewable resource profiles logged" 
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "System stability invariants hold under small changes in load, generation and faults" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA grid/storage solutions (efficiency, cost, resilience)" 
evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
57
description: "Detection of false data injection, SCADA attacks, or malicious demand/generation fluctuations" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry spans cover power flow, frequency, voltage, state of charge; metrics logged for operator dashboards" 
evidence: "observability/energy_otel-plan.md" 
- id: "SupplyChain" 
description: "BOM for hardware (transformers, inverters); SBOM for software (EMS, SCADA); provenance for renewable generation forecasts" evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test replays power flows and reproduces reliability metrics" 
evidence: "Rehydration_Test/energy_status.json" 
metrics: 
- name: "saidi_saifi_delta" 
target: "non‑negative" # improvements in reliability indices - name: "novelty_score" 
target: ">= 0.35" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
- name: "grid_stability_margin" 
target: ">= specified threshold" 
- name: "emissions_reduction" 
target: ">= specified target vs baseline" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # includes reliability and  efficiency metrics for comparable grids/storage systems 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/energy/*" 
observability_plan: "observability/energy_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/energy.intoto.jsonl" rehydration_script: "Rehydration_Test/energy.sh" 
carbon_report: "Cost_Carbon_Report.md" # includes life cycle emissions and  avoided emissions 
artifacts_add: 
- path: "PROTECTION_SCHEME.md" 
purpose: "Protection/relay scheme design and analysis" 
- path: "CONTINGENCY_ANALYSIS.md" 
purpose: "N‑1 contingency analysis and tail‑risk modelling" 
- path: "RENEWABLE_PROFILES.csv" 
purpose: "Historical/forecast generation profiles for renewables" - path: "SCADA_BOM.md" 
58
purpose: "Bill of materials for SCADA/EMS software and hardware" - path: "GRID_EMISSIONS_REPORT.md" 
purpose: "Report on emissions reductions vs baseline" 
standards_refs: 
- name: "IEEE 1547 (Interconnection Standards)" 
url_or_citation: "Standard for interconnecting distributed resources with electric power systems" 
- name: "NERC Reliability Standards" 
url_or_citation: "North American Electric Reliability Corporation standards" 
- name: "IEC 61850 (Substation Automation)" 
url_or_citation: "Communications networks and systems for power utility automation" 
- name: "Grid Codes (e.g., CAISO, ERCOT, UK Grid Code)" 
url_or_citation: "Regional grid connection and operation codes" 
kickoff: 
prompt_template: | 
attach runner energy 
Initiate GCP V49 for Spark: <power/grid/storage> 
Mode: <Full‑Run|Auto> • Risk: R2 
Context: system topology, generation mix, reliability targets, emissions  goals 
Deliverables: interconnect safety analysis, reliability analysis,  metamorphic & adversarial test results, novelty score, carbon report, signed  release
