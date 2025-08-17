5.14 Policy Design & Public Programs Runner 
runner: 
name: "Policy Design & Public Programs" 
aliases: ["policy","program","governance","public‑sector"] 
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
41

- Productizer 
- Operator 
- Scribe 
refusal_policy: 
- "Refuse partisan persuasion; only institutional design, evidence evaluation and scenario analysis." 
- "Refuse policies that diminish democratic rights or protections without deliberative process." 
agent_graph: "agents/policy_agent_graph.json" 
memory_config: "memory/policy_memory_config.yml" 
policy_module: "Policies/policy.rego" 
micro_gates: 
- id: "Causal‑Validity" 
description: "Counterfactual logic and confounders addressed; causal diagrams and DAGs validated" 
evidence: "EVIDENCE_LEDGER.md" 
- id: "Deliberation‑Plan" 
description: "Citizen assembly / deliberative process plan defined (CDD/ OECD principles)" 
evidence: "OPERATIONAL_README.md" 
- id: "Equity‑Impact" 
description: "Distributional effects analyzed across demographic groups; fairness deltas logged" 
evidence: "FAIRNESS_LEDGER.md" 
- id: "Transparency‑Log" 
description: "Decision rationale recorded in a public transparency log" evidence: "07_ledgers/DECISION_LEDGER.md" 
- id: "C7.Repro" 
description: "Simulation seeds and policy design scratchpads logged" evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Policy recommendations stable under minor parameter perturbations and alternative but plausible assumptions" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA governance innovations" evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Detection of manipulation, targeted messaging or disproportionate influence" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry covers simulation runs, deliberation events and decision outputs" 
evidence: "observability/policy_otel-plan.md" 
- id: "SupplyChain" 
description: "SBOM for modelling tools; provenance for datasets" 42

evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test replays simulations, deliberative processes and replicates key recommendations" 
evidence: "Rehydration_Test/policy_status.json" 
metrics: 
- name: "brier_score" 
target: "<= 0.15" # accuracy of probabilistic forecasts 
- name: "replication_ok" 
target: "true" 
- name: "equity_index" 
target: ">= target threshold across groups" 
- name: "novelty_score" 
target: ">= 0.35" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # includes social choice  innovations, deliberative processes outcomes 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/policy/*" 
observability_plan: "observability/policy_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/policy.intoto.jsonl" rehydration_script: "Rehydration_Test/policy.sh" 
carbon_report: "Cost_Carbon_Report.md" 
artifacts_add: 
- path: "CAUSAL_DAGS.md" 
purpose: "Causal diagrams and model assumptions" 
- path: "DELIBERATION_PLAN.md" 
purpose: "Citizen assembly design and deliberation schedule" - path: "EQUITY_IMPACT_REPORT.md" 
purpose: "Distributional effects analysis" 
- path: "TRANSPARENCY_LOG.md" 
purpose: "Public log of rationale and decisions" 
standards_refs: 
- name: "Deliberative Polling (Stanford CDD)" 
url_or_citation: "Official CDD resources" 
- name: "OECD Deliberative Principles" 
url_or_citation: "OECD guidance on public deliberation" 
- name: "Arrow’s Impossibility Theorem" 
url_or_citation: "Normative limits of social choice (SEP)" 
- name: "Gibbard–Satterthwaite Theorem" 
url_or_citation: "Limits on strategy‑proof voting systems (SEP)" kickoff: 
43

prompt_template: | 
attach runner policy 
Initiate GCP V49 for Spark: <governance system or public program> 
Mode: <Full‑Run|Auto> • Risk: R3 
Context: policy area, stakeholders, objectives, decision criteria,  
regulatory framework 
Deliverables: causal/equity analysis, deliberation plan, transparency log,  metamorphic & adversarial test results, novelty score, signed release 
