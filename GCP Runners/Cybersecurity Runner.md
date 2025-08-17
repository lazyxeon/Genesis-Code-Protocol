5.19 Cybersecurity & Secure Systems Runner 
runner: 
name: "Cybersecurity & Secure Systems" 
aliases: ["security","cyber","infosec","appsec","cloudsec"] risk_tier: "R3" 
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
- "Refuse offensive tooling or exploitation instructions." 
- "Refuse to operate without threat modelling and secure development lifecycle." 
agent_graph: "agents/security_agent_graph.json" 
54
memory_config: "memory/security_memory_config.yml" 
policy_module: "Policies/security.rego" 
micro_gates: 
- id: "ThreatModel" 
description: "STRIDE/LINDDUN threat model complete; mitigations documented" 
evidence: "RISK_SAFETY_LEDGER.md" 
- id: "SAST‑DAST‑Secrets" 
description: "Static/dynamic scans green; secrets scans green; exceptions dual‑signed" 
evidence: "09_security_provenance/ATTESTATIONS/*" 
- id: "SBOM‑Signing" 
description: "SBOM + provenance + signatures present" 
evidence: "09_security_provenance/*" 
- id: "C7.Repro" 
description: "Environment lock & seeds; exploit seeds recorded" evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Security controls remain effective under minor configuration changes and environment shifts" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA security tooling (threat coverage, false positive rate, detection latency)" 
evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Simulated attacks (e.g., injection, SSRF, RCE, supply‑chain attack) are detected and mitigated" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry includes attack detection, alerting, and correlation across logs, metrics and traces" 
evidence: "observability/security_otel-plan.md" 
- id: "SupplyChain" 
description: "Supply‑chain integrity verified: SBOM, SLSA provenance, signature checks" 
evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test replays attack simulations and verifies detection" 
evidence: "Rehydration_Test/security_status.json" 
metrics: 
- name: "critical_findings" 
target: "0 open" 
- name: "false_positive_rate" 
target: "<= 5%" 
- name: "novelty_score" 
55
target: ">= 0.40" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
- name: "attack_detection_latency_ms" 
target: "<= target" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # includes MITRE ATT&CK  coverage, attack detection benchmarks 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/security/*" 
observability_plan: "observability/security_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/security.intoto.jsonl" rehydration_script: "Rehydration_Test/security.sh" 
carbon_report: "Cost_Carbon_Report.md" 
artifacts_add: 
- path: "THREAT_MODEL.md" 
purpose: "STRIDE/LINDDUN threat model document" 
- path: "SECURITY_TEST_PLAN.md" 
purpose: "Plan for SAST/DAST/penetration testing" 
- path: "INCIDENT_RESPONSE_PLAYBOOK.md" 
purpose: "Playbook for handling incidents detected by the system" - path: "09_security_provenance/SECRETS_SCAN_REPORT.md" 
purpose: "Report of secrets scan results and exceptions" 
standards_refs: 
- name: "NIST SP 800‑53" 
url_or_citation: "Security and privacy controls for information systems" - name: "OWASP ASVS & LLM Top‑10" 
url_or_citation: "Application security verification and LLM security guidance" 
- name: "MITRE ATT&CK & D3FEND" 
url_or_citation: "Attack and defensive technique frameworks" - name: "SLSA (Supply Chain Levels for Software Artifacts)" url_or_citation: "Provenance and integrity framework" 
kickoff: 
prompt_template: | 
attach runner security 
Initiate GCP V49 for Spark: <secure system/tool> 
Mode: <Full‑Run|Auto> • Risk: R3 
Context: threat landscape, regulatory requirements, attack surface Deliverables: threat model, SAST/DAST/secrets scans, SBOM/attestations/ signatures, metamorphic & adversarial test results, novelty score, signed  release 
