5.17 Religion & Theology (Scholarly Synthesis) Runner 
runner: 
name: "Religion & Theology (Scholarly Synthesis)" 
aliases: ["religion","theology","comparative","textual‑criticism"] risk_tier: "R2" 
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
- "No proselytizing, demeaning or disparaging content; comparative, respectful synthesis only." 
- "No claims beyond sources; mark conjectures; avoid personal PII." agent_graph: "agents/religion_agent_graph.json" 
memory_config: "memory/religion_memory_config.yml" 
policy_module: "Policies/religion.rego" 
micro_gates: 
- id: "Source‑Set" 
description: "Multi‑tradition canonical set defined (e.g., KJV vs DSS; Qur’an Uthmanic; Vedas critical editions)" 
evidence: "EVIDENCE_LEDGER.md" 
- id: "Textual‑Criticism" 
description: "Variant analysis & dating with citations (textual criticism)" 
49
evidence: "06_evidence/stats/TEXTUAL_VARIANT_TABLE.csv" 
- id: "Tradition‑Balance" 
description: "Balanced representation; no single school dominates" evidence: "07_ledgers/ASSUMPTION_LEDGER.md" 
- id: "Wisdom‑Voice" 
description: "Patterned, anonymized aggregation from vetted public forums; bias checks performed" 
evidence: "08_safety_privacy/WISDOM_VOICE_METHOD.md" 
- id: "C7.Repro" 
description: "List of sources and query seeds recorded" 
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Synthesis remains consistent under paraphrasing of input texts and alternate translation choices" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA comparative theology syntheses" 
evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Detection of misquotation, misattribution, or sectarian bias" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry logs sources consulted, claim IDs, and summary decisions" 
evidence: "observability/religion_otel-plan.md" 
- id: "SupplyChain" 
description: "Provenance for digital corpora; SBOM for software tools" evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test replays retrieval and synthesis; reproduces claim graph" 
evidence: "Rehydration_Test/religion_status.json" 
metrics: 
- name: "source_diversity_index" 
target: ">= threshold across traditions" 
- name: "bias_alerts" 
target: "0 critical" 
- name: "novelty_score" 
target: ">= 0.35" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
- name: "citation_accuracy" 
target: "100%" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
50
novelty_benchmarks: "novelty/sota_benchmarks.csv" # includes comparative  theology works and metrics 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/religion/*" 
observability_plan: "observability/religion_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/religion.intoto.jsonl" rehydration_script: "Rehydration_Test/religion.sh" 
carbon_report: "Cost_Carbon_Report.md" 
artifacts_add: 
- path: "13_docs/SOURCE_CANON_MAP.md" 
purpose: "List of canonical sources and editions" 
- path: "06_evidence/stats/TEXTUAL_VARIANT_TABLE.csv" 
purpose: "Table of textual variants and dating" 
- path: "08_safety_privacy/WISDOM_VOICE_METHOD.md" 
purpose: "Methodology for Wisdom‑Voice aggregation and bias checks" - path: "COMPARATIVE_THEOLOGY_BENCHMARKS.md" 
purpose: "Benchmark tasks for comparative synthesis" 
standards_refs: 
- name: "Leon Levy Dead Sea Scrolls Digital Library" 
url_or_citation: "Primary DSS images and transcriptions" 
- name: "King James Version (1611) historical context" 
url_or_citation: "History of KJV translation" 
- name: "Uthmanic codex tradition" 
url_or_citation: "Scholarly overview" 
- name: "Rigveda critical edition" 
url_or_citation: "Academic context" 
kickoff: 
prompt_template: | 
attach runner religion 
Initiate GCP V49 for Spark: <theological synthesis or tool> 
Mode: <Full‑Run|Auto> • Risk: R2 
Context: religious traditions to compare, languages, cultural  sensitivities 
Deliverables: canon map, textual variant table, balance checks,  wisdom‑voice analysis, metamorphic & adversarial test results, novelty score,  signed release
