5.16 Archaeology & Experimental History Runner 
runner: 
name: "Archaeology & Experimental History" 
aliases: ["archaeology","experimental","megalithic","ancient","replica"] risk_tier: "R2" 
confidence_target: 0.95 
roles: 
46

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
- "Refuse destructive proposals; prioritize stewardship and community consent." 
- "Refuse pseudo‑scientific claims without evidence or reproducibility." agent_graph: "agents/archaeology_agent_graph.json" 
memory_config: "memory/archaeology_memory_config.yml" 
policy_module: "Policies/archaeology.rego" 
micro_gates: 
- id: "Stewardship" 
description: "Site/people stewardship and permits documented; community engagement recorded" 
evidence: "13_docs/COMMUNITY_ENGAGEMENT_AND_PERMITS.md" 
- id: "Plausibility‑Physics" 
description: "Materials properties (MEP) and route/slope analyses justified; FEA performed for load/drag" 
evidence: "06_evidence/stats/*" 
- id: "NonDestructive‑Priority" 
description: "Non‑destructive testing (NDT) prioritized; reversible trials only" 
evidence: "SAFETY_CASE.md" 
- id: "C7.Repro" 
description: "Replication seeds and 3D model data logged" 
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Reconstruction hypotheses invariant under minor material substitutions and scaling" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA experimental archaeology findings" 
evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Detect pseudoscience, anachronisms, or cultural misappropriation" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry logs excavation steps, replication trials and 47

consensus commentary" 
evidence: "observability/archaeology_otel-plan.md" 
- id: "SupplyChain" 
description: "Material provenance and ethical sourcing recorded" evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test rebuilds 3D models and replicates physical trials" 
evidence: "Rehydration_Test/archaeology_status.json" 
metrics: 
- name: "community_acceptance" 
target: "documented and positive" 
- name: "plausibility_index" 
target: ">= threshold" 
- name: "novelty_score" 
target: ">= 0.35" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
- name: "pseudoscience_alerts" 
target: "0" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # includes known  experimental archaeology projects (e.g., Kon‑Tiki, Stonehenge replica) metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/archaeology/*" 
observability_plan: "observability/archaeology_otel-plan.md" sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/archaeology.intoto.jsonl" rehydration_script: "Rehydration_Test/archaeology.sh" 
carbon_report: "Cost_Carbon_Report.md" 
# optional; includes CO₂ for materials transport and digital modelling artifacts_add: 
- path: "02_data/input_specs/CULTURE_TECH_PROFILE.yml" 
purpose: "Cultural & technological context profile" 
- path: "06_evidence/stats/MATERIALS_PROP_TABLE.csv" 
purpose: "Material properties (density, tensile strength, etc.)" - path: "07_ledgers/STEWARDSHIP_LEDGER.md" 
purpose: "Ledger of stewardship commitments and community feedback" - path: "3D_MODELS/" 
purpose: "CAD/mesh files for replicas" 
standards_refs: 
- name: "ICOMOS Charter for the Protection and Management of Archaeological Heritage" 
url_or_citation: "Charter on ethical archaeological practice" - name: "Experimental Archaeology Methodology" 
48
url_or_citation: "Academic guidelines on experimental archaeology" - name: "Community Archaeology principles" 
url_or_citation: "Guidelines for inclusive and respectful archaeology" kickoff: 
prompt_template: | 
attach runner archaeology 
Initiate GCP V49 for Spark: <ancient‑tech reconstruction> 
Mode: <Full‑Run|Auto> • Risk: R2 
Context: site, culture, artefact, ethical considerations, community  stakeholders 
Deliverables: stewardship dossier, physics/FEA, replica test SOP,  metamorphic & adversarial test results, novelty score, signed release 
