5.3 Life Sciences (GxP) Runner 
runner: 
name: "Life Sciences (GxP)" 
aliases: ["gxp","lab","clinical","med‑device","pharma","biotech"] risk_tier: "R3" 
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
12
- "No medical diagnosis/treatment advice; defer to licensed reviewer." - "No PHI/PII without DPIA and lawful basis." 
- "Refuse protocols lacking validation and regulatory compliance." agent_graph: "agents/gxp_agent_graph.json" 
memory_config: "memory/gxp_memory_config.yml" 
policy_module: "Policies/gxp.rego" 
micro_gates: 
- id: "Validation‑VMP" 
description: "Validation master plan + URS/FS/DS + IQ/OQ/PQ defined and executed" 
evidence: "VALIDATION_MASTER_PLAN.md; URS.md; FS.md; DS.md; IQ/OQ/ PQ_PROTOCOL.md" 
- id: "Part11‑Annex11" 
description: "Audit trails and electronic signatures configured & tested (21 CFR Part 11 / Annex 11)" 
evidence: "PART11_ANNEX11_CONFIG.md" 
- id: "ALCOA+" 
description: "Data integrity controls in place (Attributable, Legible, Contemporaneous, Original, Accurate, plus completeness, consistency, endurance and availability)" 
evidence: "DATA_INTEGRITY_ALCOA+.md" 
- id: "C7.Repro" 
description: "Environment lock & seeds recorded" 
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Assay and measurement invariants hold under dilution, time or reagent batch variations" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA assays/devices" evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Red‑team attempts to corrupt or falsify data are detected and mitigated" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Data provenance and audit trail spans captured via OTEL" evidence: "observability/gxp_otel-plan.md" 
- id: "SupplyChain" 
description: "BOM, SBOM and provenance for all reagents, devices and software" 
evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test rebuilds the lab setup, replays core assays and reproduces key results" 
evidence: "Rehydration_Test/gxp_status.json" 
metrics: 
13
- name: "validation_deviations_closed" 
target: "100%" 
- name: "data_integrity_findings" 
target: "0 critical" 
- name: "novelty_score" 
target: ">= 0.30" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
- name: "audit_trail_completeness" 
target: "100% of critical events logged" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # e.g., assay sensitivity,  accuracy vs gold standard 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/gxp/*" 
observability_plan: "observability/gxp_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/gxp.intoto.jsonl" rehydration_script: "Rehydration_Test/gxp.sh" 
carbon_report: "Cost_Carbon_Report.md" 
artifacts_add: 
- path: "VALIDATION_MASTER_PLAN.md" 
purpose: "GxP validation master plan (VMP)" 
- path: "07_ledgers/VALIDATION_TRACEABILITY_LEDGER.csv" 
purpose: "Traceability between requirements, specs and test cases" - path: "URS.md" 
purpose: "User requirements specification" 
- path: "FS.md" 
purpose: "Functional specification" 
- path: "DS.md" 
purpose: "Design specification" 
- path: "IQ/OQ/PQ_PROTOCOL.md" 
purpose: "Installation, operational and performance qualification protocols" 
- path: "DATA_INTEGRITY_ALCOA+.md" 
purpose: "Plan to implement and verify ALCOA+ controls" 
standards_refs: 
- name: "FDA 21 CFR Part 11" 
url_or_citation: "Electronic records and signatures regulation" - name: "EU Annex 11" 
url_or_citation: "EU GMP guidelines on computerized systems" - name: "ICH Q7/Q10" 
url_or_citation: "Good manufacturing practices for APIs" 
- name: "ALCOA+ Data Integrity Guidance" 
url_or_citation: "Good practice for data integrity in regulated labs" kickoff: 
14
prompt_template: | 
attach runner gxp 
Initiate GCP V49 for Spark: <regulated life‑science tool> 
Mode: <Full‑Run|Auto> • Risk: R3 
Context: indication, intended use, regulatory region 
Deliverables: VMP, URS/FS/DS, IQ/OQ/PQ, Part11/Annex11 config, ALCOA+  plan, metamorphic & adversarial test reports, novelty score, signed release 
Additional notes: The GxP runner configures the memory store to handle sensitive personal data: PHI/PII is redacted at ingestion and only decrypted when absolutely required by a licensed operator. Metamorphic tests include dilution/replicate consistency, reagent batch change tolerance and time‑series stability. Novelty scoring uses bibliometric atypicality and improvement vs FDA/EMA‑approved assays. Adversarial tests simulate data falsification, contamination and unauthorized access. Observability covers audit‑trail events and multi‑agent decisions. Rehydration includes building the lab configuration from the audit bundle and rerunning critical assays to confirm results. 
