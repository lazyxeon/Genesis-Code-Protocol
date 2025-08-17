5.9 Culinary & Food Systems Runner 
runner: 
name: "Culinary & Food Systems" 
aliases: ["culinary","food","kitchen","haccp","fsms"] 
risk_tier: "R3" 
confidence_target: 0.975 
roles: 
- Planner 
- Researcher 
- Inventor 
- Engineer 
- Adversary 
28
- Optimizer 
- Auditor 
- Productizer 
- Operator 
- Scribe 
refusal_policy: 
- "Refuse unsafe temperatures or practices; require HACCP/FSMS compliance." - "Refuse allergen omission or substitution without disclosure." agent_graph: "agents/culinary_agent_graph.json" 
memory_config: "memory/culinary_memory_config.yml" 
policy_module: "Policies/culinary.rego" 
micro_gates: 
- id: "HACCPPlanOK" 
description: "Critical control points (CCPs) identified; monitoring & corrective actions defined" 
evidence: "Runners/Exotics/Cartridges/Culinary/HACCP_PLAN_TEMPLATE.md" - id: "FoodCodeOK" 
description: "Compliance with FDA Food Code and local regulations" evidence: "Runners/Exotics/Cartridges/Culinary/FOOD_CODE_CHECKLIST.csv" - id: "PublicHygieneOK" 
description: "WHO Five Keys to Safer Food summarised and posted" evidence: "Runners/Exotics/Cartridges/Culinary/WHO_5_KEYS_BRIEF.md" - id: "AllergenLogOK" 
description: "Allergens identified and logged; cross‑contamination controls in place" 
evidence: "Runners/Exotics/Cartridges/Culinary/ALLERGEN_LEDGER.md" - id: "C7.Repro" 
description: "Recipe scaling seeds logged; reproducibility in taste and safety tested" 
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Scaling and unit conversion invariants hold; recipe modifications preserve CCP safety" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SOTA culinary innovation (e.g., taste, nutritional profile, sustainability)" 
evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Detection of unsafe substitutions, allergen mislabeling, or instructions leading to foodborne illness" 
evidence: "redteam/results.csv" 
- id: "Observability" 
description: "Telemetry spans include ingredient handling, cooking time/ temperature, hygiene events" 
evidence: "observability/culinary_otel-plan.md" 
- id: "SupplyChain" 
29

description: "SBOM for kitchen software; provenance for ingredients and suppliers" 
evidence: "SBOM/*; provenance/*" 
- id: "Rehydration" 
description: "Rehydration test reproduces the dish and food safety metrics from recorded steps" 
evidence: "Rehydration_Test/culinary_status.json" 
metrics: 
- name: "ccp_coverage" 
target: "100%" 
- name: "food_code_violations" 
target: "0" 
- name: "allergen_incidents" 
target: "0" 
- name: "novelty_score" 
target: ">= 0.40" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # includes healthy/ sustainable recipes, taste metrics 
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/culinary/*" 
observability_plan: "observability/culinary_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/culinary.intoto.jsonl" rehydration_script: "Rehydration_Test/culinary.sh" 
carbon_report: "Cost_Carbon_Report.md" # includes life‑cycle assessment of  ingredients when possible 
artifacts_add: 
- path: "Runners/Exotics/Cartridges/Culinary/HACCP_PLAN_TEMPLATE.md" purpose: "HACCP plan template" 
- path: "Runners/Exotics/Cartridges/Culinary/FOOD_CODE_CHECKLIST.csv" purpose: "Compliance checklist for FDA Food Code" 
- path: "Runners/Exotics/Cartridges/Culinary/ALLERGEN_LEDGER.md" purpose: "Allergen log and cross‑contamination controls" 
- path: "Runners/Exotics/Cartridges/Culinary/WHO_5_KEYS_BRIEF.md" purpose: "Brief on WHO Five Keys to Safer Food" 
- path: "CULINARY_NUTRITION_PROFILE.md" 
purpose: "Nutritional analysis and sustainability profile" 
standards_refs: 
- name: "FDA Food Code (2022)" 
url_or_citation: "Official Food Code PDF" 
- name: "Codex HACCP (CXC 1‑1969) & ISO 22000:2018" 
url_or_citation: "HACCP and food safety management systems" 30
- name: "WHO Five Keys to Safer Food" 
url_or_citation: "World Health Organization guidance" 
- name: "Food Allergen Labeling and Consumer Protection Act (FALCPA)" url_or_citation: "US regulation on allergen disclosure" 
kickoff: 
prompt_template: | 
attach runner culinary 
Initiate GCP V49 for Spark: <food system/recipe tool> 
Mode: <Full‑Run|Auto> • Risk: R3 
Context: cuisine type, allergens, dietary goals, food safety requirements Deliverables: HACCP plan, Food Code checklist, WHO Five Keys brief,  allergen log, metamorphic & adversarial test results, novelty score, carbon &  nutrition report, signed release 
