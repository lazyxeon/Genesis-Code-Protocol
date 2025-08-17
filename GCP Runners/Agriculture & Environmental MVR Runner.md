5.4 Agriculture & Environmental MRV Runner 
runner: 
name: "Agriculture & Environmental MRV" 
aliases: ["ag","mrv","env","carbon","soil","yield"] 
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
- "Refuse unverifiable MRV claims; require QA/QC and uncertainty bounds." - "Refuse to ignore indigenous or local knowledge; require community engagement." 
agent_graph: "agents/ag_mrv_agent_graph.json" 
memory_config: "memory/ag_mrv_memory_config.yml" 
policy_module: "Policies/ag_mrv.rego" 
micro_gates: 
- id: "Trial‑Design" 
description: "Randomized blocks/power analysis specified with replication and sample size justified" 
evidence: "07_ledgers/TRIAL_DESIGN_LEDGER.md" 
15
- id: "Sensor‑Cal" 
description: "Sensor calibration & drift model verified" 
evidence: "07_ledgers/SENSOR_CALIB_LEDGER.md" 
- id: "MRV‑QAQC" 
description: "Blanks, duplicates and outliers handled; QC checks documented" 
evidence: "07_ledgers/MRV_QAQC_LEDGER.md" 
- id: "C7.Repro" 
description: "Environment lock & seeds; plot maps and data collection protocols logged" 
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Model predictions and measurement invariants hold under noise, unit conversion and scaling of inputs" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA yield/carbon MRV methods" evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Simulation of seed poisoning or sensor tampering does not bias the MRV outputs" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry spans capture trial design, data collection and model inference phases" 
evidence: "observability/ag_mrv_otel-plan.md" 
- id: "SupplyChain" 
description: "Instrumentation SBOM and provenance recorded; calibration certificates attached" 
evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test rebuilds the trial dataset and recalculates MRV metrics and uncertainty intervals" 
evidence: "Rehydration_Test/ag_mrv_status.json" 
metrics: 
- name: "uncertainty_ci" 
target: "report 95% CI; justified" 
- name: "replication_power" 
target: ">=0.8" 
- name: "novelty_score" 
target: ">= 0.40" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
- name: "aap_compliance" 
target: "100%" # Accountability and participation compliance tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
16
novelty_benchmarks: "novelty/sota_benchmarks.csv" # e.g., carbon MRV  protocols, yield models 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/ag_mrv/*" 
observability_plan: "observability/ag_mrv_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/ag_mrv.intoto.jsonl" rehydration_script: "Rehydration_Test/ag_mrv.sh" 
carbon_report: "Cost_Carbon_Report.md" # includes greenhouse gas accounting  methodology 
artifacts_add: 
- path: "SEASON_TRIAL_PLAN.md" 
purpose: "Season plan and block randomization design" 
- path: "PLOT_MAP.geojson" 
purpose: "Geospatial mapping of trial plots" 
- path: "MRV_METHOD.md" 
purpose: "Measurement, reporting and verification protocol" 
- path: "07_ledgers/TRIAL_DESIGN_LEDGER.md" 
purpose: "Trial design log" 
- path: "07_ledgers/SENSOR_CALIB_LEDGER.md" 
purpose: "Sensor calibration and drift log" 
- path: "07_ledgers/MRV_QAQC_LEDGER.md" 
purpose: "QA/QC ledger for MRV measurements" 
standards_refs: 
- name: "IPCC 2019 Refinement" 
url_or_citation: "Guidelines for National Greenhouse Gas Inventories" - name: "FAO Sustainable Soil Management" 
url_or_citation: "Principles and guidelines for sustainable soil management" 
- name: "MRV requirements under Article 6 of the Paris Agreement" url_or_citation: "UNFCCC guidance on MRV for NDCs and carbon trading" - name: "PEPA soil carbon method" 
url_or_citation: "Australian Clean Energy Regulator (example MRV method)" kickoff: 
prompt_template: | 
attach runner ag-mrv 
Initiate GCP V49 for Spark: <MRV innovation> 
Mode: <Full‑Run|Auto> • Risk: R2 
Context: cropping system, baseline carbon stocks, measurement instruments,  community engagement plans 
Deliverables: Trial design, sensor calibration plan, MRV QA/QC records,  uncertainty model, metamorphic & adversarial test results, novelty score, signed  release 
17
The Agriculture & MRV runner emphasises rigorous experimental design, calibration, quality control, and community participation. Metamorphic tests verify that MRV models produce consistent estimates under permutations of sensor noise, scale and units. Novelty is measured against emerging carbon/yield measurement methods. Adversarial tests simulate data poisoning and sensor drift. Observability logs each data collection and processing step. Rehydration reproduces the trial dataset and recalculates carbon/yield estimates and uncertainty. The carbon report includes the greenhouse gas emissions associated with field operations and computational analysis. 
