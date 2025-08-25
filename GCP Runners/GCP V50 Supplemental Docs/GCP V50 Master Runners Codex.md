Master Runners Codex – Flagship AI‑Native (GCP V50)
Release: TBD (2025)

This codex is the companion to GCP V50.  It defines a library of standard runners that an LLM can execute without outside context.  Each runner is a deterministic module with clearly defined inputs, required steps, outputs, gates, telemetry, and ready‑to‑run prompts.  Runners may call each other but never break the global order defined by the plan/sequence.json.  All artifacts are emitted into the run directory (see GCP V50 file layout).  This codex is AI‑native: it is designed for a chat‑based agent to read and execute.
0. How to use the codex
Initialization: After Init GCP, the early execution sequence (DataRights → CartridgesParsePack → Planner → Memory) sets up configuration and registers cartridges.  The planner emits plan/sequence.json which lists the ordered runner calls.
Runner call envelope: A runner is invoked with a RunnerCall JSON:

{

  "runner": "RUNNER_CREATIVE_DISCOVERY",

  "inputs": {"brief_md": "brief.md", "heilmeier_md": "heilmeier.md"},

  "settings": {"mode": "auto", "risk": "r1"},

  "run_id": "gcp‑a17e",

  "phase": "C‑1"

}

The runner returns a RunnerResult:

{

  "runner": "RUNNER_CREATIVE_DISCOVERY",

  "outputs": ["creative/Scan_Sources.json", "creative/Idea_Ledger.jsonl", "Gate_Signals.json"],

  "gate": {

    "name": "Creative_Discovery",

    "status": "pass|needs‑human|fail",

    "reason": "text",

    "artifact": "creative/Candidate_Set.csv",

    "waiver": null

  },

  "spans": ["..."],

  "exceptions": []

}

Chat‑only emission: If the environment lacks file I/O, the runner must embed artifacts verbatim using the BEGIN ARTIFACT … END ARTIFACT wrapper (see GCP V50).  The call/return envelopes may refer to these inlined artifacts by path.
Telemetry: All runners MUST emit OpenTelemetry spans for each model or tool invocation.  Each span uses the naming convention gcp.<phase>.<runner>.<operation> and includes attributes: gen_ai.operation, llm.provider, llm.model, llm.request.tokens, llm.response.tokens, phase, gate, tool, error (if any).  Exceptions must be recorded as events on the span with error.type, error.msg and stacktrace.
Gates and waivers: Each runner ends by writing its gate status to Gate_Signals.json.  A gate may be pass, needs‑human or fail.  Waivers may be recorded only by authorised roles (ComplianceOwner, EngineeringDirector, SafetyLead) with reason and timestamp.
1. Universal runner contract
Every runner MUST implement the following contract:

Field
Description
Inputs
File names or JSON values required to start the runner.  Inputs are resolved relative to the run root.
Steps (MUST)
Ordered list of actions that the LLM must perform.  Steps reference tools, prompts or sub‑runners.
Artifacts
Files that must be produced.  Their exact names and formats are defined by the GCP file layout.
Gate
Name of the gate, criteria for pass/needs‑human/fail, and threshold values (e.g., coverage ≥ 0.90).
Prompts/Templates
Pre‑defined prompts or scaffolds to help the LLM perform complex tasks.  Should be saved in prompts/.
Telemetry
Span names and important metrics to record (counts, durations, novelty scores, etc.).
Observability
Describe how to capture exceptions, rate limits, and retries.
Dependencies
List of other runners that must run before or after this one.

Mandatory artifacts and micro‑gates
All runners must write to Gate_Signals.json and, where applicable, update Evidence_Index.jsonl and ClaimGraph.json.  Runners implementing classification or generation tasks (e.g., RAG, creative discovery) must compute a Hallucination Confidence Bound (HCB) or Model Risk Metric (MRM) and update HCB.yaml and MRM_CARD.md.  Where personal data is processed, the runner must write a Data_Rights_Card.md describing consent lineage and licensing.
Security and risk controls
Runner steps must include input validation, rate limiting and adherence to the OWASP LLM Top‑10.  Tools must have explicit contracts with preconditions/postconditions and maximum token budgets.  For DP‑sensitive tasks, runners must enforce privacy budgets (ε, δ) and verify that noise addition meets NIST SP 800‑226 guidelines.
2. Runner index
The following runners implement the phases of GCP V50.  Their order is determined by the planner and may involve concurrency where dependencies allow.

RUNNER_DATARIGHTS – Set data rights, consent, license and retention; build Data_Rights_Card.md.
RUNNER_CARTRIDGES_PARSE_PACK – Parse CARTRIDGE.json files, validate schema v2.0 signatures and register them in registry/REGISTRY.json.
RUNNER_PLANNER – Build plan/sequence.json ordering runners according to phase dependencies and risk level.
RUNNER_MEMORY – Configure safe persistent memory; allocate embeddings and vector stores; prepare summarization hooks.
RUNNER_AMBIGUITY_TO_BRIEF – Execute C‑0 Heilmeier; generate brief.md and heilmeier.md.
RUNNER_CREATIVE_DISCOVERY – Execute C‑1; produce domain scans, patent landscape, ideation files, idea ledger and candidate set.
RUNNER_RESEARCH – Conduct R‑2 literature and evidence retrieval; build corpus and claims table; draft de‑risk plan.
RUNNER_SYSTEM_DESIGN – Draft D‑3 design spec, API, types, telemetry plan and test matrix.
RUNNER_ALGO_SPEC_VERIFY – Perform formal verification using TLA+ or proof assistants; update verify/.
RUNNER_PROTOTYPE_TOOLING – Implement reference prototype, tool contracts and fuzz testing; emit code and test harness.
RUNNER_EVALUATION_SAFETY – Plan and conduct experiments, compute HCB and MRM, build red‑team tests and threat map.
RUNNER_PRIVACY_DP_EVAL – Evaluate de‑identification, DP guarantees and HIPAA/PHI compliance; produce DP reports.
RUNNER_MITRE_ATLAS_THREATMODEL – Map red‑team results to ATLAS tactics; write mitigations and risk register.
RUNNER_FINOPS_SUSTAINABILITY – Create FinOps plan, compute SCI and forecast costs and carbon.
RUNNER_SBOM_AIBOM – Generate SPDX 3.0 SBOM and CycloneDX ML‑BOM; include SWHIDs and data lineage.
RUNNER_C2PA – Produce C2PA manifests and content credentials for all media outputs.
RUNNER_RO_CRATE_ARCHIVE – Package artifacts into an RO‑Crate v1.2 archive.
RUNNER_EU_AI_ACT_TECHDOC – Assemble EU AI Act Annex IV technical documentation.
RUNNER_REHYDRATE – Compute rehydration matrix and ensure reproducibility; run simulation of reproduction.
RUNNER_SOTA_CALIBRATE – Check SOTA freshness of models/data; update retrieval indexes; compute SOTA advantage.
RUNNER_RED_TEAM – Conduct adversarial and misuse testing beyond evaluation; log new attack vectors and mitigation strategies.
RUNNER_TOOL_FUZZ – Fuzz test all tool contracts; compute coverage and ensure robust error handling.
RUNNER_TELEMETRY_OTEL – Audit that spans and metrics are recorded; produce OTEL dashboards and summarise exceptions.
RUNNER_GOVERNANCE – Fill ISO 42001 manual, NIST cross‑walk, obligations matrix and run governance waiver logic.
RUNNER_DELIVERY – Prepare deliverables (executive brief, whitepaper, README, changelog); package release and assign identifiers.

Each runner below follows the universal contract.  Runners may be grouped by phase and share common gates, but each has an independent contract and metrics.
3. Runner contracts
RUNNER_DATARIGHTS
Purpose. Collect and record data rights, licenses, retention periods and consent.  Without a valid data rights card, no downstream runner may access data.

Inputs. None; prompts user and reads uploaded documents.

Steps (MUST):

Present the user with a list of uploaded files and ask for consent and licensing details (e.g., MIT, CC‑BY‑4.0, proprietary).  Record responses in memory.
Determine data retention rules (e.g., purge after run or store for 30 days) and whether the user allows training or evaluation usage.
Record any data rights claims from external sources (library terms, API TOS).  Link them in Evidence_Index.jsonl and ClaimGraph.json.
Emit Data_Rights_Card.md summarising consent lineage, licenses, retention and restrictions.
Update Gate_Signals.json for DataRights gate (pass if consent obtained for all inputs; needs‑human if unknown; fail if denied).

Artifacts. Data_Rights_Card.md, updated Gate_Signals.json.

Gate. DataRights – pass if all data has explicit consent and known license; needs‑human if unknown; fail if user denies use.

Telemetry. Span i0.datarights with attributes: files_n, consented_n, denied_n, licenses.  Record exceptions if user refuses.
RUNNER_CARTRIDGES_PARSE_PACK
Purpose. Parse domain cartridges, validate their schema and register them for use.  Without a valid cartridge pack, creative discovery and RAG cannot run.

Inputs. cartridges/ folder containing one or more CARTRIDGE.json files.

Steps (MUST):

For each CARTRIDGE.json, validate against the v2.0 schema (see Cartridges Pack) using JSON schema validation.  Fail if invalid.
Verify the cartridge’s signature using the Exotics meta‑cartridge public key; reject unsigned or expired cartridges.
Ensure that the declared embedding models, indexes and lexicons are available; load them or fetch if remote.
Register the cartridge in registry/REGISTRY.json with fields: domain, version, path, signature_status, supported_runners, trust_level.
Emit gate signals: CartridgeParse (pass if all required cartridges validated; needs‑human if optional cartridges invalid; fail if required missing).

Artifacts. registry/REGISTRY.json, updated Gate_Signals.json.

Gate. CartridgeParse – pass if all required cartridges are valid; needs‑human if optional cartridges invalid; fail if required missing.

Telemetry. Span i0.cartridges_parse with attributes: cartridges_n, valid_n, invalid_n, signed_n.
RUNNER_PLANNER
Purpose. Determine the sequence of runner calls based on configuration, risk level, and dependencies.

Inputs. MANIFEST.json (mode, risk), registry/REGISTRY.json (available cartridges), optional user instructions.

Steps (MUST):

Build a dependency graph of runners using this codex; each runner lists its dependencies.  Mark phases as optional or mandatory based on risk (e.g., MITRE_ATLAS runner mandatory for r2/r3).
Generate a topologically sorted list of runners.  Insert concurrency markers for independent runners (e.g., RUNNER_SBOM_AIBOM may run alongside RUNNER_C2PA).
Save the sequence to plan/sequence.json with objects {order, runner, phase, depends_on, optional}.
Output a summary plan to the user (table of runner names, phases, expected outputs).  Ask the user to confirm or adjust the plan.
Gate: PlannerReady – pass when sequence generated and user accepted; needs‑human if unresolved dependency or user edit needed; fail if graph invalid.

Artifacts. plan/sequence.json, updated Gate_Signals.json.

Telemetry. Span i0.planner with attributes: runners_n, concurrency, risk_level.
RUNNER_MEMORY
Purpose. Configure persistent memory and summarization for the run.

Inputs. plan/sequence.json, registry/REGISTRY.json (embedding models for memory), mode.

Steps (MUST):

Allocate an embedding model (e.g., from cartridges) for summarizing prior exchanges; set vector store parameters (index type, dimension, distance metric).
Persist earlier user messages and attachments to the memory store; compute chunking and embedding; record embed counts and approximate tokens.
Set summarization schedule: summarise every N messages or when context length > threshold.  Save memory configuration to memory/config.json.
Gate: MemoryReady – pass if memory configured and persistence working; needs‑human if storage unavailable; fail if embedding fails.

Artifacts. memory/config.json, updated Gate_Signals.json.

Telemetry. Span i0.memory with attributes: embeddings_model, vector_store, chunks_n.
RUNNER_AMBIGUITY_TO_BRIEF
Purpose. Implement C‑0.  Converts a vague spark into a structured brief using the Heilmeier framework.

Inputs. Raw user prompt or spark string.

Steps (MUST):

Ask the eight Heilmeier questions (what are you trying to do, how is it done today, what is new, who cares, why you, how to measure success, what are the risks, what is the schedule/cost?).  Record answers verbatim.
Select a target sub‑domain from available cartridges (e.g., energy_power, legal, code) and justify the choice.
Define at least one measurable target (e.g., performance gain, carbon reduction) and specify baseline metrics.
Write brief.md summarising the problem, scope, goals and success metrics.  Write heilmeier.md capturing the Q&A session.
Gate: AmbiguityToBrief – pass if all 8 questions answered and measurable targets defined; needs‑human if vague; fail if missing answers.

Artifacts. brief.md, heilmeier.md, updated Gate_Signals.json.

Telemetry. Span c0.heilmeier with attributes: questions_answered_n, domain, metrics_defined.
RUNNER_CREATIVE_DISCOVERY
Purpose. Implement the rich creative discovery and domain harvest of C‑1.

Inputs. brief.md, heilmeier.md, registry/REGISTRY.json (cartridges), optional creative_scoring_config.json.

Steps (MUST):

Use cartridges to run rapid domain scans.  Query at least three independent sources (materials databases, domain‑specific corpora, Papers with Code) and record hits to creative/Scan_Sources.json with metadata (source, title, URL, description, relevance).
Perform a patent landscape search using Google Patents and WIPO PATENTSCOPE.  Record queries, CPC/IPC clusters, top 10–20 patents, assignees and any prior art to creative/Patent_Landscape.md.
Decompose the problem into tensions or contradictions; record them in creative/contradictions.md.
Execute at least three ideation methods, ensuring diversity.  For each method, generate candidate ideas:
SCAMPER – at least 5 ideas per letter; log prompts and outputs to creative/SCAMPER_Prompts.md.
TRIZ – identify 3–7 contradictions and map to inventive principles; summarise in creative/TRIZ_Contradictions.md.
Morphological matrix – define 4–10 dimensions with 3–5 options each; produce creative/Morphological_Matrix.csv and at least 30 combinations.
Analogies – produce 10 analogies to remote domains; record in creative/Analogy_Maps.md.
Conceptual blends – create 5 double‑scope blends; record in creative/Blends.md.
Generative design algorithms – run at least one algorithmic generative design (e.g., topology optimisation, generative models) if applicable.
For each idea, write an entry in creative/Idea_Ledger.jsonl with fields: id, description, methods_used, supporting_hits[], novelty_score, feasibility_score, risk_notes, environmental_impact, data_rights_notes.
Load the scoring configuration from scoring/creative_scoring_config.json (weights for novelty, feasibility, risk, impact, data rights, sustainability) and compute a weighted score for each idea.  Save the top 10–30 to creative/Candidate_Set.csv with columns: id, score, top_methods, notes, evidence_refs.
Emit creative/concepts/<id>.md for the top three concepts summarising the idea, evidence, claims and next steps.
Update Evidence_Index.jsonl and ClaimGraph.json linking ideas to sources and hypotheses.  Compute MRM metrics and update MRM_CARD.md and HCB.yaml if large models used for scoring.
Gate: Creative_Discovery – pass if at least three ideation methods used, ≥20 ideas generated and scored, domain scans and patents logged; needs‑human if incomplete; fail if no evidence linking.

Artifacts. All files under creative/*, updated Evidence_Index.jsonl, ClaimGraph.json, HCB.yaml, MRM_CARD.md, Gate_Signals.json.

Telemetry. Span c1.creative with attributes: sources_n, ideas_n, methods_n, top_candidates_n.
RUNNER_RESEARCH
Purpose. Ground candidate concepts in evidence and plan de‑risking.

Inputs. creative/Candidate_Set.csv, creative/concepts/*.md, registry/REGISTRY.json.

Steps (MUST):

Conduct a targeted literature survey using domain cartridges, RAG pipelines and search APIs.  Assemble a corpus of at least 20 relevant documents (papers, specs, datasets) in research/corpus/ with metadata.
Summarise the landscape in research/landscape.md: state‑of‑the‑art, key players, benchmark datasets and performance metrics.  Map how each candidate addresses gaps.
Extract testable claims into research/claims.tsv with columns: claim, source, confidence (0–1), method_to_test.
Draft a de‑risk plan in research/derisk_plan.md addressing each major risk (technical, regulatory, ethical, environmental, cost) and mapping them to tests or analyses.
Update Evidence_Index.jsonl and ClaimGraph.json linking claims to sources and concept IDs.
Gate: ResearchGrounding – pass if corpus created, claims enumerated and de‑risk plan present; needs‑human if key sources missing or claims untestable; fail if no mapping to concepts.

Artifacts. research/landscape.md, research/claims.tsv, research/derisk_plan.md, research/corpus/*, updated evidence/claims/gate files.

Telemetry. Span r2.research with attributes: docs_n, claims_n, risks_n.
RUNNER_SYSTEM_DESIGN
Purpose. Produce a buildable system specification and API.

Inputs. creative/concepts/*.md (selected concept), research/derisk_plan.md, registry/REGISTRY.json.

Steps (MUST):

Based on the selected concept, write design/spec.md covering: purpose, scope, use cases, architecture diagram (text or PlantUML), data flows, invariants, non‑goals and constraints (performance, cost, privacy, sustainability).
Define a formal API in design/api/ (e.g., api_reference.md) with endpoint/function signatures, input/output schemas (JSON/YAML/proto), error models and security considerations.
Declare domain types or interfaces in design/types/ (TypeScript, Python or language appropriate).  Provide stub implementations if needed.
Plan instrumentation: create design/otel.md enumerating every span and metric, including PII redaction and user keys.
Define a design/test_matrix.md listing test cases: unit, integration, property‑based, adversarial; map them to requirements and risks.
Gate: DesignReady – pass if spec coherent, API complete and test matrix covers requirements; needs‑human if ambiguous; fail if missing invariants or unclear interfaces.

Artifacts. design/spec.md, design/api/*, design/types/*, design/otel.md, design/test_matrix.md, updated gate signals.

Telemetry. Span d3.design with attributes: endpoints_n, invariants_n, tests_n.
RUNNER_ALGO_SPEC_VERIFY
Purpose. Verify formal correctness of the design using mathematical proofs or model checking.

Inputs. design/spec.md, design/api/*, design/test_matrix.md.

Steps (MUST):

Determine whether the system requires formal verification (non‑deterministic, concurrent, safety critical).  If yes, proceed; otherwise, set gate status to pass with justification.
For stateful or concurrent systems, translate the specification into a TLA+ model (verify/spec.tla) and specify configurations in verify/MC.cfg.  Run the TLC model checker; capture output logs (verify/tlc_log.txt).  Document invariants, liveness properties and results.
For functional or mathematical algorithms, draft proofs in Lean 4 (verify/spec.lean) or Coq (verify/spec.v); run proof assistants; store proof scripts and logs.
Write verify/checklists.md mapping each invariant to design requirements and verification evidence.
Gate: Algorithm_Spec_Verification – pass if all relevant invariants are proven or checked; needs‑human if partial; fail if counterexamples or unproved invariants remain.

Artifacts. verify/spec.tla and verify/MC.cfg + logs OR verify/spec.lean/.v + logs, verify/checklists.md, updated gate signals.

Telemetry. Span v4.verify with attributes: proofs_n, invariants_proven_n, counterexamples_n.
RUNNER_PROTOTYPE_TOOLING
Purpose. Build a prototype implementation with instrumentation and testing harness.

Inputs. design/api/*, design/types/*, verify/* (if any), registry/REGISTRY.json (tool models).

Steps (MUST):

Implement a minimal reference version of the system, focusing on the core algorithm and API surfaces.  Use stub functions where necessary and annotate with TODOs.
Define tool contracts for any external tool interactions in tools/contracts/*.json: specify name, version, inputs, outputs, pre/postconditions, security controls, failure modes and rate limits.  Provide stub implementations in tools/stubs/.
Build unit tests and property‑based tests for each API function; integrate with a fuzz testing harness (e.g., AFL, HypoFuzz) to explore edge cases.  Record coverage metrics.
Instrument the code with OpenTelemetry and compute coverage; ensure all model/tool calls emit spans with correct attributes.  Save coverage report to eval/coverage.json.
Gate: SemConv – pass if spans present on all critical paths; ToolContractsFuzz – pass if code coverage ≥90 % and no fatal crashes; needs‑human if coverage low; fail if instrumentation missing or critical security control absent.

Artifacts. tools/contracts/*.json, tools/stubs/*, src/ code, tests/ harness, eval/coverage.json, updated gate signals.

Telemetry. Span p5.prototype with attributes: coverage, contracts_n, tools_n.
RUNNER_EVALUATION_SAFETY
Purpose. Evaluate the prototype, compute performance/safety metrics and red‑team the system.

Inputs. src/, tests/, creative/Candidate_Set.csv, research/claims.tsv, design/spec.md.

Steps (MUST):

Define evaluation plan in eval/plan.md with metrics (accuracy, latency, energy use, fairness), baselines and acceptance thresholds.  For generative models, adopt evaluation frameworks like HELM or RAISE.
Prepare evaluation datasets: curate or simulate relevant data; document lineage and licensing; produce eval/data_sets/* and cards/data_card.md for each dataset.  Ensure DP considerations are met.
Run experiments; log results, compute statistics, produce visualisations and write eval/eval_report.md summarising findings and gaps.
Compute the Hallucination Confidence Bound (HCB) and Model Risk Metric (MRM); record into HCB.yaml and MRM_CARD.md.  Flag any high‑risk behaviours.
Develop a red‑team suite targeting the OWASP LLM Top‑10 and MITRE ATLAS tactics.  Execute attacks; record outcomes in security/findings.md and map to ATLAS in security/atlas_map.md.  Propose mitigations.
Gate: EvaluationReady – pass if evaluation report covers metrics and data cards; HCB – pass if HCB below threshold; MRM – pass if risk manageable; ThreatModelReady – pass if ATLAS mapping covers major tactics.  Needs‑human if any fail; fail if metrics below baseline or red‑team uncovers critical vulnerabilities.

Artifacts. eval/plan.md, eval/eval_report.md, eval/data_sets/*, cards/data_card.md, HCB.yaml, MRM_CARD.md, security/findings.md, security/atlas_map.md, updated gate signals.

Telemetry. Span e6.eval with attributes: metrics_n, datasets_n, hcb, mrm, attacks_n.
RUNNER_PRIVACY_DP_EVAL
Purpose. Ensure that data handling complies with privacy regulations and differential privacy.

Inputs. All artifacts referencing personal data (research/corpus/*, eval/data_sets/*), Data_Rights_Card.md.

Steps (MUST):

Identify all personal data fields; classify into direct identifiers, quasi‑identifiers and sensitive attributes.
Apply de‑identification techniques (removal, generalisation, suppression) per NIST SP 800‑188.  Document operations and residual risk in privacy/deid.md.
Determine DP parameters (ε, δ, composition) for any data release or training; compute noise budgets; simulate DP release; record metrics in privacy/dp_eval.md.
If data falls under HIPAA, apply safe‑harbour or expert determination and document in privacy/hipaa_deid.md.
Create privacy/risks.tsv enumerating privacy risks, likelihood, impact and mitigation actions.
Gate: PrivacyReady – pass if de‑identification completed and DP parameters valid; needs‑human if uncertain; fail if PHI used without compliance.

Artifacts. privacy/deid.md, privacy/dp_eval.md, privacy/hipaa_deid.md (if needed), privacy/risks.tsv, updated gate signals.

Telemetry. Span p6.privacy with attributes: pii_fields_n, epsilon, delta, residual_risk.
RUNNER_MITRE_ATLAS_THREATMODEL
Purpose. Build a threat model using the MITRE ATLAS framework and propose mitigations.

Inputs. security/findings.md (from evaluation), design/spec.md, privacy/risks.tsv.

Steps (MUST):

Identify adversary objectives and potential attack surfaces (prompt injection, supply chain, model theft, data poisoning).
Map attacks and vulnerabilities to MITRE ATLAS tactics and techniques; create a table in security/atlas_map.md with columns: tactic, technique, scenario, likelihood, impact, mitigation.
Evaluate the effectiveness of existing mitigations; propose additional controls (rate limiting, input sanitisation, gating, human oversight) and record in security/mitigations.md.
Update risk register risk_register.yaml with threat IDs, severity and mitigation owners.
Gate: ThreatModelReady – pass if atlas map covers major tactics and mitigations; needs‑human if incomplete; fail if critical vulnerabilities unmitigated.

Artifacts. security/atlas_map.md, security/mitigations.md, risk_register.yaml, updated gate signals.

Telemetry. Span m7.atlas with attributes: tactics_n, techniques_n, mitigations_n.
RUNNER_FINOPS_SUSTAINABILITY
Purpose. Build cost and sustainability plans.

Inputs. Resource usage metrics (eval/coverage.json, logs), plan/sequence.json, creative/Candidate_Set.csv.

Steps (MUST):

Estimate compute resources for each runner and overall (CPU/GPU hours, memory, bandwidth) using heuristics and existing runs.  Summarise in finops/forecast.csv.
Draft a FinOps plan in finops/plan.md covering cost KPIs, budgets, alerts, resource allocation, and optimisation strategies (right‑sizing, caching, off‑peak scheduling).
Calculate Software Carbon Intensity (SCI) in finops/sci.json using methodology from the Green Software Foundation; include scope definitions, energy measurements, carbon intensity factors and confidence intervals.
Allocate costs to deliverables and produce finops/attribution.md.  Include overhead for compliance and red‑team work.
Gate: CostCarbonReady – pass if budgets set, SCI computed and forecast produced; needs‑human if unknown parameters; fail if budgets missing or unrealistic.

Artifacts. finops/plan.md, finops/forecast.csv, finops/sci.json, finops/attribution.md, updated gate signals.

Telemetry. Span f9.finops with attributes: estimated_cost, estimated_carbon, budget_met.
RUNNER_SBOM_AIBOM
Purpose. Generate software and model bills of materials.

Inputs. src/ code, tools/contracts/*.json, registry/REGISTRY.json.

Steps (MUST):

Use SPDX tools to scan the codebase and third‑party libraries; produce SBOM.spdx.json including package names, versions, licenses and SWHIDs.
Construct a CycloneDX ML‑BOM (MLBOM.cdx.json) capturing models, datasets, training pipelines, hyperparameters and dataset citations.
Cross‑validate that all dependencies used by runners are listed in the BOMs; if not, update manifests and code.
Gate: SBOMReady – pass if SBOM and ML‑BOM complete and validated; needs‑human if unknown dependencies; fail if BOM incomplete.

Artifacts. SBOM.spdx.json, MLBOM.cdx.json, updated gate signals.

Telemetry. Span s8.bom with attributes: packages_n, models_n, datasets_n.
RUNNER_C2PA
Purpose. Attach content credentials to all media outputs.

Inputs. Any media artifacts (images, videos, audio, docs) produced by earlier runners.

Steps (MUST):

For each media file, create a C2PA assertion chain including asset metadata (creator, provenance, license), actions taken (generation, editing), and hashes of inputs/outputs.
Sign the C2PA manifests using a trusted signer; embed or attach them to the files; save to C2PA/.
Gate: C2PAReady – pass if all media assets have valid C2PA assertions; needs‑human if unknown; fail if signatures invalid.

Artifacts. C2PA/*.manifest.json, updated gate signals.

Telemetry. Span s8.c2pa with attributes: media_n, assertions_n, signed_n.
RUNNER_RO_CRATE_ARCHIVE
Purpose. Package all artifacts into an RO‑Crate for reproducibility.

Inputs. All run artifacts; BOMs, provenance, evaluation reports.

Steps (MUST):

Create a ro_crate/ folder; generate a ro-crate-metadata.json describing the crate, its authors, version, context and entries.
Include all required artifacts as data entities with metadata (file path, description, type, relations).  For large data sets, include pointers (e.g., DOI or object storage URIs).
Validate the crate using the RO‑Crate validator; ensure the metadata graph is consistent.
Gate: ROCrateReady – pass if crate validated; needs‑human if warnings; fail if invalid.

Artifacts. provenance/ro_crate/*, updated gate signals.

Telemetry. Span s8.rocrate with attributes: entries_n, validation_errors_n.
RUNNER_EU_AI_ACT_TECHDOC
Purpose. Produce Annex IV technical documentation for EU AI Act compliance.

Inputs. All specification, evaluation, privacy and risk documents.

Steps (MUST):

Populate docs/eu/annex_iv/summary.md covering the system’s purpose, stage of maturity, and high‑risk classification (if applicable).
Fill out Annex IV Sections: (1) general description, (2) data description, (3) design & development, (4) performance evaluation, (5) risk management and mitigation, (6) monitoring, (7) documentation and record‑keeping.  Map each section to existing artifacts.
Include a conformity assessment plan and references to harmonised standards.
Gate: EUAIActReady – pass if technical document complete and accurate; needs‑human if incomplete; fail if high‑risk requirements unmet.

Artifacts. docs/eu/annex_iv/*, updated gate signals.

Telemetry. Span g7.euai with attributes: sections_completed.
RUNNER_REHYDRATE
Purpose. Evaluate reproducibility by rehydrating the project from released artifacts.

Inputs. Final release package (RO‑Crate), release/IDENTIFIERS.md, SBOM.spdx.json, MLBOM.cdx.json.

Steps (MUST):

Extract the RO‑Crate in a clean environment; verify file integrity using checksums and SWHIDs.
Use the included Makefile to rebuild the project; run tests; compare outputs to reference results.  Document any deviations.
Compute the rehydration matrix (rehydration/rehydration_matrix.csv) capturing reproducibility across software, model, data, environment, hardware and random seeds.  Compute the rehydration score (>0.90 expected).
Gate: RehydrateReady – pass if rehydration score ≥ threshold and no critical differences; needs‑human if minor issues; fail if reproducibility broken.

Artifacts. rehydration/rehydration_matrix.csv, updated gate signals.

Telemetry. Span d12.rehydrate with attributes: rehydration_score, deviations_n.
RUNNER_SOTA_CALIBRATE
Purpose. Assess SOTA calibration and benchmark advantages.

Inputs. research/landscape.md, evaluation metrics, creative/Scan_Sources.json.

Steps (MUST):

Identify SOTA baselines from literature (benchmarks, leaderboards) for the chosen domain; summarise in sota/baselines.md.
Compare project performance to SOTA; compute delta metrics (e.g., accuracy gain, latency reduction, carbon cost improvements).  Write sota/comparison.md.
Check freshness of retrieval indexes and embeddings; update if the SOTA baseline has changed since start of run.  Document updates in sota/freshness.md.
Gate: SOTAReady – pass if SOTA comparison shows meaningful improvement or justified parity; needs‑human if unclear; fail if project underperforms without justification.

Artifacts. sota/baselines.md, sota/comparison.md, sota/freshness.md, updated gate signals.

Telemetry. Span d13.sota with attributes: sota_improvement, fresh_updates.
RUNNER_RED_TEAM
Purpose. Execute advanced adversarial testing beyond evaluation.

Inputs. All previous artifacts; system accessible for attack.

Steps (MUST):

Generate a red‑team plan in security/red_team_plan.md including social engineering, prompt injection, data exfiltration, model extraction and backdoor insertion scenarios.
Execute attacks using automated agents and manual prompts; record results in security/red_team_results.md.  Include transcripts and system responses.
Rate each attack’s success and impact; propose mitigations and patch instructions; update risk_register.yaml and security/mitigations.md.
Gate: RedTeamReady – pass if attacks executed and mitigations proposed; needs‑human if results ambiguous; fail if critical vulnerabilities unresolved.

Artifacts. security/red_team_plan.md, security/red_team_results.md, updated mitigations and risk register, updated gate signals.

Telemetry. Span d14.redteam with attributes: attacks_executed, critical_vulnerabilities_n.
RUNNER_TOOL_FUZZ
Purpose. Fuzz test all tool contracts for robustness.

Inputs. tools/contracts/*.json, src/ code.

Steps (MUST):

Use a fuzz testing framework to generate random and adversarial inputs for each tool; instrument to capture crashes and incorrect outputs.
Mutate input shapes and lengths to explore edge cases; track code paths executed.
Collect coverage metrics; compute fuzz coverage percentage; record in eval/fuzz_coverage.json.
Gate: ToolContractsFuzz – pass if coverage ≥90 % and zero critical failures; needs‑human if moderate failures; fail if major failures.

Artifacts. eval/fuzz_coverage.json, updated gate signals.

Telemetry. Span d15.fuzz with attributes: coverage, failures_n.
RUNNER_TELEMETRY_OTEL
Purpose. Audit telemetry completeness and summarise exceptions.

Inputs. All OTel traces in observability/otel_traces/.

Steps (MUST):

Parse all spans; verify each runner and tool call has a corresponding span with required attributes; identify missing spans.
Generate dashboards (JSON or textual) summarising latency, token usage, error rates and phase durations.  Save to observability/summary.md and observability/dashboard.json.
Collate all exceptions; group by type; produce observability/exceptions.md with counts and sample stack traces.
Gate: TelemetryReady – pass if spans cover all calls and dashboards generated; needs‑human if missing spans; fail if critical events missing.

Artifacts. observability/summary.md, observability/dashboard.json, observability/exceptions.md, updated gate signals.

Telemetry. Span d16.telemetry with attributes: missing_spans_n, errors_n, latency_p99.
RUNNER_GOVERNANCE
Purpose. Compile governance documentation and enforce waiver policy.

Inputs. All compliance artifacts (docs/eu/annex_iv, docs/aims, compliance/*, privacy/*), Gate_Signals.json.

Steps (MUST):

Draft an ISO 42001 manual in docs/aims/ISO42001_manual.md covering policy statements, scope, roles (RACI), control objectives and CAPA (Corrective/Preventive Action) loops.
Map NIST RMF controls to evidence in docs/compliance/nist_rmf_mapping.md and fill any gaps.  Cross‑reference the risk_register.yaml and obligations_matrix.csv.
Populate governance/RACI.md listing responsibilities (Engineering Director, Compliance Owner, Safety Lead, Data Steward) across each phase.  Define approval workflow for waivers.
Process any outstanding waiver requests in HITL/waiver_log.jsonl; ensure roles sign off with reasons.  Update gate signals accordingly.
Gate: GovernanceReady – pass if manuals, mappings and waiver log complete; needs‑human if roles unassigned; fail if outstanding unwaived failures.

Artifacts. docs/aims/ISO42001_manual.md, docs/compliance/nist_rmf_mapping.md, governance/RACI.md, HITL/waiver_log.jsonl, updated gate signals.

Telemetry. Span g7.governance with attributes: waivers_n, controls_mapped_n.
RUNNER_DELIVERY
Purpose. Assemble deliverables, assign identifiers and finalise packaging.

Inputs. All upstream artifacts, Gate_Signals.json.

Steps (MUST):

Write release/README.md summarising the project scope, key results and reproduction instructions.  Prepare release/CHANGELOG.md capturing changes from initial version to final deliverable.
Produce a short executive_brief.pdf and long tech_whitepaper.pdf (via LLM summarisation and formatting).  Ensure citations link to evidence index.
Generate api_reference.md from design/api/*; update model/data/system cards (Model Card, Data Card, System Card) in docs/cards/.
Compile release/ro_crate/ with BOMs, provenance, evaluation results, annex documentation and C2PA manifests.  Compute checksums; store in rehydration/rehydration_matrix.csv.
Assign persistent identifiers (e.g., DOI via Zenodo).  Write release/IDENTIFIERS.md listing DOIs, commit hashes, version numbers, SWHIDs and citation file (CITATION.cff).
Gate: ShipIt – pass if all required deliverables prepared and all gates passed or waived; needs‑human if minor issues; fail if critical artifacts missing.

Artifacts. release/README.md, release/CHANGELOG.md, executive_brief.pdf, tech_whitepaper.pdf, api_reference.md, docs/cards/*, release/ro_crate/*, release/IDENTIFIERS.md, updated gate signals.

Telemetry. Span d11.delivery with attributes: docs_n, pdfs_n, identifiers_n.



This Master Runners Codex defines the behaviour of all runners required to execute GCP V50.  Runners should never deviate from the specified steps or skip gates.  Use the codex as a reference when building new runners or integrating additional cartridges and domains.

