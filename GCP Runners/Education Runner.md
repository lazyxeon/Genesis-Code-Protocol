5.13 Education & Assessment Runner 
runner: 
name: "Education & Assessment" 
aliases: ["education","assessment","lms","irt","curriculum"] 
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
- "Refuse biased or opaque evaluation without fairness deltas." - "Refuse to share student data without DPIA and parental or institutional consent." 
- "Refuse content that violates academic integrity policies." 
agent_graph: "agents/education_agent_graph.json" 
memory_config: "memory/education_memory_config.yml" 
policy_module: "Policies/education.rego" 
micro_gates: 
- id: "Learning‑Objectives" 
description: "Measurable learning objectives mapped to assessment tasks" evidence: "USER_GUIDE.md" 
- id: "Assessment‑Validity" 
description: "Validity and reliability plan (e.g., IRT models) documented and executed" 
evidence: "EVIDENCE_LEDGER.md" 
- id: "Privacy‑EEA" 
description: "Student data DPIA complete; compliance with FERPA/GDPR" evidence: "08_safety_privacy/PRIVACY_DPIA.md" 
- id: "Fairness‑Metrics" 
description: "Fairness delta across demographic slices measured and minimized" 
evidence: "07_ledgers/FAIRNESS_LEDGER.md" 
- id: "C7.Repro" 
description: "Assessment seeds and randomization logged" 
39
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Assessment scoring invariant under distractor permutations and wording variations" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA educational tools (personalization, fairness improvements, predictive validity)" evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Detection of cheating, prompt exploitation or collusion; mitigation in place" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry captures item‑level response times, fairness metrics, engagement and drop‑off rates" 
evidence: "observability/education_otel-plan.md" 
- id: "SupplyChain" 
description: "SBOM for LMS platforms; provenance for test banks and question pools" 
evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test reproduces assessments and scores from recorded seeds" 
evidence: "Rehydration_Test/education_status.json" 
metrics: 
- name: "fairness_delta" 
target: "<= 0.5% across groups" 
- name: "validity_index" 
target: ">= 0.7" # correlation with external criterion 
- name: "novelty_score" 
target: ">= 0.35" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
- name: "drop_off_rate" 
target: "<= 10%" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # includes MMLU‑Pro tasks,  HELM evaluation tasks 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/education/*" 
observability_plan: "observability/education_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/education.intoto.jsonl" rehydration_script: "Rehydration_Test/education.sh" 
40
carbon_report: "Cost_Carbon_Report.md" 
artifacts_add: 
- path: "CURRICULUM_MAP.md" 
purpose: "Mapping of curriculum standards to learning objectives" - path: "IRT_MODEL_CONFIG.yaml" 
purpose: "Configuration for Item Response Theory model" 
- path: "FERPA_COMPLIANCE_POLICY.md" 
purpose: "Policy on student data privacy and parental rights" - path: "FAIRNESS_LEDGER_TEMPLATE.csv" 
purpose: "Template for logging fairness metrics" 
standards_refs: 
- name: "Every Student Succeeds Act (ESSA)" 
url_or_citation: "US federal law on K‑12 assessment and accountability" - name: "FERPA (Family Educational Rights and Privacy Act)" 
url_or_citation: "US law protecting student education records" - name: "GDPR (education context)" 
url_or_citation: "EU General Data Protection Regulation applied to education" 
- name: "Standards for Educational and Psychological Testing (AERA/APA/ NCME)" 
url_or_citation: "Guidelines on test development and use" 
kickoff: 
prompt_template: | 
attach runner education 
Initiate GCP V49 for Spark: <learning tool/assessment> 
Mode: <Full‑Run|Auto> • Risk: R2 
Context: learning domain, grade level, fairness goals, privacy  requirements 
Deliverables: objectives map, validity/reliability plan, DPIA, fairness  analysis, metamorphic & adversarial test results, novelty score, signed release 
