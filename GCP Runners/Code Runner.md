5.1 Code / Software Runner 
runner: 
name: "Code / Software" 
aliases: ["code","software","api","service","platform"] 
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
- "Refuse to generate secrets, credentials, or exploit code." 
- "Refuse to bypass license compliance or signature/SBOM gates." - "Refuse to operate outside defined API rate limits or budgets." agent_graph: "agents/code_agent_graph.json" 
memory_config: "memory/code_memory_config.yml" 
6
policy_module: "Policies/code.rego" 
micro_gates: 
- id: "API‑Acceptance" 
description: "Functional, negative and performance criteria met (p50/p95/ p99 latencies) with error taxonomy coverage" 
evidence: "11_product/api/ACCEPTANCE_CRITERIA.md; 04_benchmarks/results/ TEST_MATRIX.csv" 
- id: "SupplyChain" 
description: "SBOM + signatures + attestations present; reproducible build" 
evidence: "09_security_provenance/*" 
- id: "C7.Repro" 
description: "Environment lockfile & seeds recorded; tail metrics reported" 
evidence: "06_evidence/replication/*" 
- id: "Metamorphic" 
description: "Metamorphic invariants hold (idempotence, commutativity, monotonicity)" 
evidence: "metamorphic/results.csv" 
- id: "Novelty" 
description: "Novelty score ≥ threshold vs SWE‑Bench & GAIA baselines" evidence: "novelty/novelty_score.json" 
- id: "Adversarial" 
description: "Prompt injection / insecure output handling tests pass" evidence: "redteam/results.csv" 
- id: "Observability" 
description: "OpenTelemetry spans/metrics/logs configured from birth" evidence: "observability/code_otel-plan.md" 
- id: "Rehydration" 
description: "Rehydration test rebuilds the API and reproduces acceptance tests" 
evidence: "Rehydration_Test/code_status.json" 
metrics: 
- name: "test_pass_rate" 
target: ">=95% unit; >=90% integration" 
- name: "latency_p95_ms" 
target: "<= target; no regression" 
- name: "error_budget" 
target: "within SLO" 
- name: "novelty_score" 
target: ">= 0.40" 
- name: "metamorphic_pass_rate" 
target: ">= 0.90" 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
novelty_benchmarks: "novelty/sota_benchmarks.csv" # e.g., SWE‑Bench tasks,  GAIA tool‑use tasks 
7
metamorphic_relations: "metamorphic/invariants.json" 
transforms: "metamorphic/transforms.json" 
adversarial_corpus: "redteam/code/*" # injection strings, insecure tool  prompts, etc. 
observability_plan: "observability/code_otel-plan.md" 
sbom: "09_security_provenance/SBOM.spdx.json" 
provenance: "09_security_provenance/ATTESTATIONS/code.intoto.jsonl" rehydration_script: "Rehydration_Test/code.sh" 
carbon_report: "Cost_Carbon_Report.md" 
artifacts_add: 
- path: "11_product/api/ACCEPTANCE_CRITERIA.md" 
purpose: "API contract of done and test definitions" 
- path: "01_code/ARCHITECTURE_DECISIONS/ADR-0001.md" 
purpose: "Decision trace (ADR)" 
- path: "11_product/api/ERROR_TAXONOMY.md" 
purpose: "Uniform error taxonomy for clients" 
- path: "14_deployment/env_profiles/PIPELINE.yml" 
purpose: "CI/CD pipeline configuration" 
- path: "01_code/api/openapi.yaml" 
purpose: "OpenAPI specification" 
- path: "Policy_Diffs.md" 
purpose: "Record of policy updates from post‑mortem/AAR" 
standards_refs: 
- name: "OWASP Application Security & LLM Top‑10" 
url_or_citation: "https://owasp.org/www-project-top-ten/" 
- name: "SLSA framework" 
url_or_citation: "https://slsa.dev" 
- name: "OpenTelemetry specification" 
url_or_citation: "https://opentelemetry.io/docs/specs/" 
kickoff: 
prompt_template: | 
attach runner code 
Initiate GCP V49 for Spark: <new API/service idea> 
Mode: <Full‑Run|Auto> • Risk: R2 
Context: target users, SLOs, budgets 
Deliverables: OpenAPI spec, acceptance tests, CI/CD pipeline, SBOM/ provenance, telemetry plan, metamorphic & adversarial test results, novelty  score, signed release 
Agent graph (code_agent_graph.json): The Planner hands off design requirements to the Researcher to gather relevant literature (e.g., best practices in API design, performance patterns). The Researcher stores claims and sources into the claim graph. The Inventor proposes architecture options which the Engineer scaffolds into a runnable prototype with OTEL hooks and acceptance tests. The Adversary injects malicious prompts and invalid inputs; the Engineer hardens the system and updates policies accordingly. The Optimizer tunes performance while respecting budget and safety constraints. The Auditor evaluates policy compliance, SBOM completeness and test coverage; the Productizer prepares documentation and client 
8
onboarding; the Operator verifies SLO dashboards and incident playbooks; the Scribe maintains the index and manifest. 
Memory config (code_memory_config.yml): Defines a 2048‑dimensional embedding store for code snippets and API docs; redacts secrets and proprietary logic; retains evidence indefinitely; scratchpad memory has a TTL of one phase. Retrieval policies restrict exposure of internal architecture decisions to the Productizer and Operator roles. 
Policy module (Policies/code.rego): Implements the refusal rules (deny secret‑seeking or exploit generation) and micro‑gate conditions. It denies tool invocations when rate limits would be exceeded or when SBOM signatures are missing; it enforces that every output containing a claim references a valid claim ID. 
Metamorphic invariants: Idempotent responses (same request yields same logical result), monotonic throughput when concurrency increases within capacity, commutativity of parameter ordering, robustness under whitespace/noise injection. 
Novelty benchmarks: SWE‑Bench tasks (GitHub issue resolution), GAIA tool‑use tasks, CodeEval datasets; the novelty score uses embedding distance vs nearest prior art, atypical API pattern analysis and improvement over SOTA baseline metrics. 
Adversarial corpus: Includes prompt‑injection sequences, insecure serialization payloads, dependency confusion packages, and policies for secure handling. Tests ensure the system refuses to process or exfiltrate secrets and prevents SSRF/RCE conditions. 
Observability plan: Spans are defined for each major sub‑phase (scaffold, test, optimization, release); metrics include API latency p50/p95/p99, error budgets, success/fail rates of metamorphic tests, and novelty scores. Logs capture policy decisions with rationale codes and tool call transcripts. 
