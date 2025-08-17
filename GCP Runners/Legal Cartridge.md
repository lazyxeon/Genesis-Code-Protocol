5.10 Legal (Advisory‑Safe) Runner 
runner: 
name: "Legal (Advisory‑Safe)" 
aliases: ["legal","law","compliance","policy‑legal"] 
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
- "Refuse jurisdiction‑specific legal advice; require licensed review." - "No client‑confidential data or privileged information may be ingested or reproduced." 
- "Mark outputs as informational only; not legal advice." 
agent_graph: "agents/legal_agent_graph.json" 
memory_config: "memory/legal_memory_config.yml" 
policy_module: "Policies/legal.rego" 
micro_gates: 
- id: "LegalCompetenceOK" 
description: "Cite primary sources; attach non‑advice disclaimer" evidence: "Runners/Exotics/Cartridges/Legal/LEGAL_USE_POLICY.md" - id: "ConfidentialityProtectedOK" 
description: "PII/privileged data not ingested; controls and redaction in 31

place (DPIA complete)" 
evidence: "08_safety_privacy/PRIVACY_DPIA.md" 
- id: "ConflictCheckOK" 
description: "Conflict ledger scanned (abstracted)" 
evidence: "Runners/Exotics/Cartridges/Legal/CONFLICT_LEDGER.md" - id: "ComplianceReferenceOK" 
description: "Model Rules/Bar guidance cited where used; cite relevant statutes" 
evidence: "EVIDENCE_LEDGER.md" 
- id: "C7.Repro" 
description: "Input hypotheticals and seeds logged; reasoning trace reproducible" 
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Answers remain consistent under paraphrased fact patterns and minor changes in irrelevant details" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA legal research tools (e.g. improved retrieval or summarization)" 
evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Detection of hallucinations, invented case law, or unauthorized practice of law" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry records sources cited, decision rationale and role hand‑offs" 
evidence: "observability/legal_otel-plan.md" 
- id: "SupplyChain" 
description: "SBOM for legal research tools; provenance for datasets" evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test replays the queries and reproduces answers and citations" 
evidence: "Rehydration_Test/legal_status.json" 
metrics: 
- name: "legal_review_required" 
target: "true for deliverables" # always require human lawyer sign‑off - name: "hallucination_rate" 
target: "0 critical" 
- name: "novelty_score" 
target: ">= 0.35" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
- name: "conflict_detection_precision" 
target: ">= 0.95" 
32
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # includes performance of  legal research tools, citation accuracy 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/legal/*" 
observability_plan: "observability/legal_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/legal.intoto.jsonl" rehydration_script: "Rehydration_Test/legal.sh" 
carbon_report: "Cost_Carbon_Report.md" 
artifacts_add: 
- path: "Runners/Exotics/Cartridges/Legal/LEGAL_USE_POLICY.md" purpose: "Non‑advice policy and disclaimer" 
- path: "Runners/Exotics/Cartridges/Legal/SEVEN_CS_ASSESSMENT.md" purpose: "Assessment of competence, confidentiality, candor, conflict of interest, communication, compliance and cost" 
- path: "Runners/Exotics/Cartridges/Legal/CONFLICT_LEDGER.md" purpose: "Abstract conflict ledger (anonymized)" 
- path: "Runners/Exotics/Cartridges/Legal/CLIENT_INTAKE_TEMPLATE.md" purpose: "Template for client intake while preserving privacy" standards_refs: 
- name: "ABA Model Rules (Competence, Confidentiality, Candor, Conflicts of Interest)" 
url_or_citation: "American Bar Association Model Rules of Professional Conduct" 
- name: "LLM‑Safe Guidance for Legal Tech" 
url_or_citation: "Best practices for AI in legal domain" 
- name: "GDPR / CCPA / HIPAA compliance" 
url_or_citation: "Data protection regulations relevant to legal data" kickoff: 
prompt_template: | 
attach runner legal 
Initiate GCP V49 for Spark: <compliance tooling/contract analyzer> Mode: <Full‑Run|Auto> • Risk: R3 
Context: jurisdiction, practice area, client confidentiality needs Deliverables: Legal use policy, DPIA, conflict ledger (abstract),  metamorphic & adversarial test results, novelty score, signed release 
