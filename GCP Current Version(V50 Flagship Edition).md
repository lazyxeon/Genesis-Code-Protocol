GCP V50 – Flagship AI‑Native Protocol (Standalone) Release: TBD (2025)
This document supersedes GCP v49 and integrates the refinements from v49.1–v49.3. It is designed for LLM/agent runners operating in chat or API mode. The protocol is fully AI‑native: every phase provides machine‑readable instructions, artifacts, gates, and ready‑to‑run prompts. The goal is to transform a vague problem spark into a reproducible, auditable invention with minimal human intervention.
0. How to use this document (bootstrap)
GCP_BOOTSTRAP
You are executing GCP V50 – Flagship AI‑Native Protocol .  
•  
mode: auto , full , or manual (select one).  
•  
startup_mode: spark_provided or autonomous . In spark_provided (architect‑led) mode, the user supplies the initial problem spark. In autonomous (collaborative brainstorm) mode, the protocol runs the Autonomous Spark Generation phase (I‑1) to propose a spark based on a high‑level domain interest.  
•  
run_id: short UUID (e.g. gcp‑a17e ).  
•  
workdir: ./gcp_run_<run_id>/ (virtual).  
•  
hard rules: Follow phases in order, emit every artifact with the exact filename, run every gate and render the gate card UX each time.  
•  
observability: Emit OpenTelemetry GenAI spans/metrics for every model/tool call; attach exception events on errors.  
•  
context: No external context is required—this protocol is self‑contained.  
Gate Card UX
Status: ? Pass / ?? Needs‑human / ? Fail
Why: <1–2 lines; include key numbers>
Next: Continue | Fix & retry | Waive (role‑gated)
Artifact: <path/to/file_or_folder>
Use the above template after every gate or runner.
1
Modes of operation
GCP V50 now supports two complementary ways to begin an inventive process:
1.  
Architect‑led mode (spark_provided) – The user provides a clear problem spark (e.g., “design a low‑latency scheduler for mobile devices”). The protocol begins at I‑0 Initialization, validates the provided spark and proceeds through C‑0 Ambiguity‑to‑Brief and the subsequent phases.
2.  
Collaborative brainstorm mode (autonomous) – The user supplies only a high‑level domain or goal (e.g., “sustainable agriculture”). The protocol runs the I‑1 Autonomous Spark Generation phase to autonomously identify a high‑value problem, perform a worth‑it analysis and present a spark and brief for human acceptance. If the user accepts, the protocol continues from I‑0; otherwise, the runner iterates or aborts.
The rest of this document details both the autonomous spark generation phase and the existing phases of GCP V50.
1. Governance & Standards Map
•  
NIST AI RMF & Generative AI Profile – lifecycle backbone with Govern/Map/Measure/Manage
controls.  
•  
ISO/IEC 42001 AIMS – AI management system manual (scope, RACI, CAPA loop, supplier oversight).  
•  
EU AI Act (Annex IV) – technical documentation generator and conformity assessment hooks.  •  
OWASP LLM Top‑10 & MITRE ATLAS – threat models and red‑team guidance.  
•  
FinOps & Sustainability – software carbon intensity (SCI), cost forecasting, energy/carbon reporting. •  
SPDX 3.0 SBOM, CycloneDX ML‑BOM, SLSA/in‑toto, Sigstore Rekor – supply‑chain provenance.  •  
C2PA 2.x – content credentials for media outputs.  
•  
Privacy & DP – NIST SP 800‑226 (DP evaluation), SP 800‑188 (de‑identification), HIPAA (if PHI).  
Include a cross‑walk document at docs/compliance/nist_rmf_mapping.md and an ISO 42001 manual at docs/aims/ISO42001_manual.md .
2. Universal File Layout
All runs must adhere to the following layout (add additional files only under permitted folders):
/gcp_run_<run_id>/
 MANIFEST.json
 Gate_Signals.json
 Evidence_Index.jsonl
 ClaimGraph.json
 PBOM.json
 SBOM.spdx.json
 MLBOM.cdx.json
 provenance/
 slsa_provenance.json
2
 in_toto_statement.json
 rekor_proofs/*.json
 observability/otel_traces/*.json  docs/
 aims/ISO42001_manual.md
 compliance/nist_rmf_mapping.md  eu/annex_iv/*
 governance/RACI.md
 cards/model_card.md
 cards/data_card.md
 cards/system_card.md
 C2PA/*.manifest.json
 risk_register.yaml
 MRM_CARD.md
 Data_Rights_Card.md
 HCB.yaml
 ENSEMBLE_LEDGER.md
 rehydration/rehydration_matrix.csv  release/IDENTIFIERS.md
 Makefile
 INDEX.md
 scoring/creative_scoring_config.json  schemas/
 PBOM.schema.json
 Gate_Signals.schema.json
 creative/
 Scan_Sources.json
 Patent_Landscape.md
 Morphological_Matrix.csv
 TRIZ_Contradictions.md
 SCAMPER_Prompts.md
 Analogy_Maps.md
 Blends.md
 Idea_Ledger.jsonl
 Candidate_Set.csv
 concepts/*
 research/
 landscape.md
 claims.tsv
 corpus/*
 derisk_plan.md
 design/
 spec.md
 api/*
 types/*
 otel.md
 test_matrix.md
 eval/
3
 eval_report.md
 data_sets/*
 security/
 findings.md
 atlas_map.md
 mitigations.md
 provenance/
 ro_crate/*
 finops/
 plan.md
 sci.json
 forecast.csv
 attribution.md
 compliance/
 eu_ai_act/*
 privacy/*
 aims/*
 release/
 README.md
 CHANGELOG.md
 ro_crate/*
 HITL/
 manifest.json
 waiver_log.jsonl
A chat‑only environment can emit artifacts verbatim using the wrapper:  
BEGIN ARTIFACT: <relative/path>
<file content>
END ARTIFACT
3. Core Schemas
MANIFEST.json
Minimal metadata describing the run:  
{
"run_id": "uuid",
"mode": "auto|full|manual",
"created_utc": "ISO-8601",
"artifacts": [
"Gate_Signals.json", "Evidence_Index.jsonl", "ClaimGraph.json", "PBOM.json", "SBOM.spdx.json", "MLBOM.cdx.json"
4
]
}
PBOM.json (Prompt Bill of Materials)
Captures system/policy prompts, memory configs, retrieval rules, tool contracts and hashes. See schemas/ PBOM.schema.json for validation.
Gate_Signals.json
Stores gate statuses ( pass , needs-human , fail ), reasons, artifact references and optional waiver objects. See schemas/Gate_Signals.schema.json .
A waiver has fields: role (ComplianceOwner|EngineeringDirector|SafetyLead), reason ,  timestamp_utc .
4. Phase Map (I‑1 → PM‑12)
GCP V50 reintegrates the rich 16‑phase lifecycle of v49 while adding a pre‑run initialization. Each phase defines Goal, Inputs, LLM MUST DO, Artifacts, Gate(s) and Exit. Adopt the following notation:
•  
? denotes at least / at most (e.g. ≥2 methods).  
•  
OTel span names are formatted as gcp.pX.<phase_name> .
I‑1 Autonomous Spark Generation
When used. This phase runs only when startup_mode=autonomous . It autonomously proposes a problem spark based on a high‑level domain interest. If startup_mode=spark_provided , skip this phase and start at I‑0.
Goal. Discover and validate a high‑value problem statement (“spark”) when the user has not provided one. Deliver a concise spark, an engineered brief and a worth‑it analysis for human acceptance.
Inputs. 1. domain_interest : a high‑level domain string (e.g., “sustainable agriculture”, “aerospace”). 2. constraints : optional list of user constraints (e.g., “must be open‑source”, “no personal data”). 3. registry/REGISTRY.json : list of available cartridges and runners.
LLM MUST DO. 1. Opportunity Scan – perform a broad sweep of scientific literature, industry news, technical blogs and patent databases relevant to the domain_interest . Identify emerging trends, unmet challenges and recent breakthroughs. Document findings in
spark_generation/Opportunity_Scan.md with metadata (source, date, relevance). 2. Capability Mapping – cross‑reference opportunities against available cartridges and runners. Prioritise problems where the system has strong domain support (e.g., choose a problem in life sciences only if the LifeSci cartridge exists). Document candidate opportunities and matching capabilities. 3. Worth‑It Analysis – for the top 2–3 candidates, perform a lightweight expected‑value analysis (impact, feasibility, time/cost, risk) and record in spark_generation/Candidate_Analysis.md . Use heuristics derived from the GCP V49 “Worth‑It” model. Flag any candidates that conflict with user constraints. 4. Spark Selection & Prompt
5
Engineering – select the best candidate based on the analysis. Draft a one‑sentence spark. Invoke the logic of C‑0 Ambiguity‑to‑Brief internally: answer the Heilmeier questions for this spark, choose measurable targets and produce brief.md and heilmeier.md under spark_generation/ . This produces a ready‑to‑run brief just as if the user had supplied the spark directly. 5. Proposal & Gate – present a proposal to the user with: the chosen spark, a summary of the opportunity and worth‑it analysis, and the engineered prompt. Await human review at the Spark_Acceptance gate. User may Accept, Request Revision (provide feedback to refine or refocus) or Reject. On accept, copy brief.md and
heilmeier.md to the root of the run ( brief.md , heilmeier.md ); on revision, re‑execute step 4 with new constraints; on reject, re‑execute from step 1 or abort.
Artifacts. *spark_generation/Opportunity_Scan.md – a survey of the domain landscape.* spark_generation/Candidate_Analysis.md – expected value models for candidate problems. *spark_generation/brief.md , spark_generation/heilmeier.md – engineered brief and Heilmeier responses. If accepted, duplicates saved to run root.
Gate – Spark_Acceptance. A mandatory human gate. Status options: pass (user accepts the spark and brief), needs‑revision (user requests adjustments), fail (user rejects). Pass transitions to I‑0; needs‑revision loops back to step 4; fail loops back to step 1 or aborts the run.
Exit. If accepted, proceed to I‑0 Initialization. Otherwise, iterate or terminate.
I‑0 Initialization
Goal. Remove friction before the run begins. When the user types Init GCP , the system auto‑intakes prior messages and attachments, proposes configuration and only asks for missing fields. Inputs. Auto‑derived or user‑confirmed:* spark – the problem statement, either provided by the user (architect‑led mode) or generated by I‑1 (autonomous mode). If startup_mode=autonomous , the spark and brief are taken from spark_generation/brief.md and spark_generation/heilmeier.md . *
mode – auto|full|manual execution mode.* risk – risk level ( r0 … r3 ). *runners – auto or list.* cartridges – discovered via registry. *consent – allow reading uploads.* telemetry – on/off. *tooling – offline|online.* budgets – time, steps, cost. *outputs – RO‑Crate, SBOM/ML‑BOM, C2PA, PDFs, zips.* compliance flags. Contract. Pass when spark, mode, risk, consent and cartridge resolution
are set. Needs‑human when missing; fail if consent is denied or contradictory flags are set. UX. Present a proposed settings table and allow accept or edit field=value . Validation. spark non‑empty; mode ∈ {auto, full, manual}; risk ∈ {r0…r3}; budgets numeric;
consent explicit.
Early Execution Sequence. 1. RUNNER_DATARIGHTS – set license, consent, retention, provenance
defaults.
2. RUNNER_CARTRIDGES_PARSE_PACK – discover and register cartridges into registry/REGISTRY.json .
3. RUNNER_PLANNER – emit plan/sequence.json mapping phases → runner calls. 4. RUNNER_MEMORY – configure safe persistence.
5. Proceed to C‑0.
6
C‑0 Ambiguity‑to‑Brief (Heilmeier)
Goal. Convert a vague prompt into a crisp, testable brief.
Inputs. Raw user prompt.
LLM MUST DO.
1. Answer all 8 Heilmeier questions.
2. Choose one target sub‑domain (e.g., “desktop OS scheduler”).
3. Define ≥1 measurable target (e.g., “reduce p99 latency by 20 % at iso‑energy”). 4. Emit brief.md and heilmeier.md .
5. Start span c0.heilmeier ; on error, add exception event. Artifacts. brief.md , heilmeier.md . Gate – AmbiguityToBrief. Pass if 8/8 answered and metrics defined; needs‑human for vague answers; fail if missing.
Templates. Provide Markdown scaffolds for brief.md and heilmeier.md .
C‑1 Creative Discovery & Domain Harvest
Goal. Produce novel candidate “alloys” through structured divergent/convergent discovery. Inputs. brief.md , heilmeier.md .
LLM MUST DO. 1. Rapid domain scan – query open materials/model/data sources (e.g., Materials Project, OQMD, AFLOW, NIST   JARVIS‑DFT, Papers   with   Code) and record structured hits to creative/ Scan_Sources.json .
2. Patent landscaping – run Google Patents (Advanced) and WIPO PATENTSCOPE; record CPC/IPC clusters, queries, assignees and 10–20 key hits to creative/Patent_Landscape.md .
3. Creative brief – restate tensions/contradictions.
4. Ideation methods (≥3, at least 2 non‑overlapping):
- SCAMPER – 5 serious ideas per letter; save prompts and best outputs to SCAMPER_Prompts.md . - TRIZ contradictions & inventive principles – map 3–7 contradictions to principles; save patterns to TRIZ_Contradictions.md .
- Morphological analysis – decompose dimensions/options; persist grid to Morphological_Matrix.csv .
- Analogies – propose 10 remote‑domain analogies; log mappings to Analogy_Maps.md . - Conceptual blending – create 5 double‑scope blends; save to Blends.md .
5. Idea ledger & scoring – record each idea to Idea_Ledger.jsonl with fields: ID, sketch, methods used, supporting hits, novelty notes, risks, next experiments. Use /scoring/ creative_scoring_config.json to compute scores (Novelty, Feasibility, Risk, Impact, Data   Rights, Sustainability); output top‑N to Candidate_Set.csv .
6. Update evidence & claims – link each candidate to citations in Evidence_Index.jsonl and hypotheses in ClaimGraph.json .
Artifacts. All files under creative/* plus updates to evidence and claims.
Gate – Creative_Discovery. Pass if ≥3 independent data sources + 1 patent portal scanned, ≥2 ideation methods used, ≥20 raw ideas and ≥10 candidates scored and linked; else needs‑human/fail. Templates/Prompts. Include ready‑to‑run prompts for SCAMPER, TRIZ, morphological matrices, analogies and blending.
7
R‑2 Domain Research & Signals Consolidation
Goal. Ground concepts in evidence and derisk weak paths.
LLM MUST DO. 1. Produce research/landscape.md summarising players, SOTA baselines and benchmarks.
2. Extract claims to verify into research/claims.tsv (claim, source, confidence, test). 3. Build mini‑corpus in research/corpus/ (papers/specs/docs).
4. Create research/derisk_plan.md mapping each risk to a test or analysis.
5. OTel span r2.research ; record metrics (sources_n, claims_n). Gate – ResearchGrounding. Pass if corpus curated, claims enumerable with tests and derisk plan present; needs‑human if critical sources missing; fail if no claims/tests linkage.
D‑3 System Design (Spec + API) and V‑4 Formal Specification & Verification
Goal. Create a precise, buildable spec and verify functional correctness.
LLM MUST DO. 1. Author design/spec.md (goals, non‑goals, architecture, invariants). 2. Emit design/api/*.md and skeletal reference types ( design/types/*.ts|.py ). 3. Define telemetry plan design/otel.md (model spans, agent spans, GenAI events, PII handling). 4. Emit test matrix design/test_matrix.md and acceptance criteria.
5. Span d3.design ; attach metrics (api_endpoints_n, invariants_n).  
Formal verification (if algorithmic/distributed).
- Use TLA+ for concurrency/distributed/state machines; emit verify/spec.tla , verify/MC.cfg ; run TLC; save tlc_log.txt .
- Use Lean 4 or Coq for functional proofs; emit verify/spec.lean or .v ; run proofs; save logs. - Emit verify/checklists.md mapping invariants to ACM/NeurIPS requirements. Gate – DesignReady (spec & API coherent) and Algorithm_Spec_Verification (no invariant violations or incomplete proofs).
Needs‑human if missing invariants or ambiguous interfaces; fail if spec cannot be traced to brief/metrics or proofs incomplete.
P‑5 Prototype & Tooling
Goal. Build a minimal reference implementation with unit and property tests.
LLM MUST DO. Implement skeleton code, tool contracts ( tools/contracts/*.json ), metamorphic tests and fuzz harness; emit OTel spans on tool/model calls; compute coverage.
Gate – SemConv (spans present & well‑formed) and ToolContractsFuzz (coverage ≥0.90).
E‑6 Evaluation & Safety
Goal. Demonstrate performance, reliability and safety.
LLM MUST DO. 1. Generate eval/plan.md with metrics, baselines and HELM‑style testing. 2. Prepare evaluation datasets and Data Cards; run experiments; write eval/eval_report.md ; update Model Card.
3. Compute HCB; update HCB.yaml and MRM_CARD.md .
4. Build red‑team suite mapped to OWASP   LLM   Top‑10 and MITRE   ATLAS; produce security/ 8
findings.md and security/atlas_map.md . Gates. HCB within budget; MRM seeded; ToolContractsFuzz coverage; ThreatModelReady (ATLAS coverage).
G‑7 Governance & Compliance
Goal. Ensure auditability and readiness against prevailing regulations and internal policies. LLM MUST DO. 1. Fill EU AI Act Annex IV technical docs in docs/eu/annex_iv/ . 2. Map controls to ISO 42001 and NIST RMF; fill docs/compliance/nist_rmf_mapping.md . 3. Produce privacy packs: privacy/deid.md , privacy/dp_eval.md (ε, δ, composition, threat model), privacy/hipaa_deid.md (if PHI), privacy/risks.tsv .
4. Emit SSDF mapping compliance/ssdf.md linking secure SDLC practices.
5. Build obligations matrix compliance/obligations_matrix.csv (requirements × control × evidence × owner × frequency).
Gate – ComplianceReady. Pass when manuals present, privacy/DP evaluation valid, obligations mapped and no unmitigated risks; needs‑human when missing data; fail if DP parameters invalid or obligations incomplete.
S‑8 Supply‑Chain & Provenance
Goal. Create verifiable lineage for software, models and datasets.
LLM MUST DO. 1. Generate SPDX   3.0 SBOM ( SBOM.spdx.json ) and CycloneDX   ML‑BOM ( MLBOM.cdx.json ) including SWHIDs for source artifacts.
2. Create SLSA provenance and in‑toto attestation ( provenance/slsa_provenance.json ,  provenance/in_toto_statement.json ).
3. Upload attestation to Sigstore Rekor; save proofs ( provenance/rekor_proofs/attest.proof.json ). 4. Attach C2PA 2.x manifests to media outputs; store in C2PA/ .
5. Emit RO‑Crate package in provenance/ro_crate/ .
Gate – SupplyChainProvenance. Pass if BOMs, SLSA/in‑toto, Rekor proofs and C2PA manifests present; needs‑human/fail otherwise.
F‑9 FinOps & Sustainability
Goal. Make cost and carbon first‑class design constraints.
LLM MUST DO. 1. Create FinOps plan finops/plan.md (scopes, cost KPIs, forecast). 2. Compute SCI score finops/sci.json with assumptions and measurement methodology. 3. Emit cost attribution finops/attribution.md with budgets and alerts; produce finops/ forecast.csv .
Gate – CostCarbonReady. Pass if SCI computed and cost dashboards configured; needs‑human if unknown factors; fail if budgets missing.
O‑10 Orchestration & Dynamic Budget Management
Goal. Dynamically manage the execution of the plan based on real‑time resource budgets (time, cost, compute) and propose adaptations when constraints are at risk.
LLM MUST DO. 1. Pre‑flight Check – before executing the next runner in plan/sequence.json , check the estimated cost and time against remaining budgets in finops/forecast.csv and finops/
9
plan.md . Use historical metrics and heuristic models to predict runner consumption. 2. Dynamic Adaptation – if a budget is at risk of being exceeded, propose one or more adaptations to the human operator. Examples: reduce the number of simulation runs in evaluation to lower cost; skip optional calibration phases to save time; downsample data or decrease model size. Document each suggestion with its impact on metrics (accuracy, confidence, carbon).
3. Human Approval – present the proposed adaptations at a BudgetAdaptation gate ( needs‑human ). Await user decision: accept a suggestion, modify budgets, or proceed without changes. Log the decision. 4. Execute & Monitor – upon approval, execute the next runner and monitor actual resource consumption. If consumption diverges significantly from estimates, generate an exception event and update heuristics. 5. Update Forecast – after the runner completes, deduct the actual cost/time/carbon from the remaining budget and update finops/forecast.csv . Produce an observability/Orchestrator_Log.jsonl
recording decisions, adaptations and consumption metrics.
Artifacts. observability/Orchestrator_Log.jsonl , updated finops/forecast.csv and Gate_Signals.json (BudgetAdaptation gate).
Gate   – BudgetAdaptation. Always needs‑human when an adaptation is proposed. Pass if the user approves or modifies budgets; fail if budgets cannot be met and no adaptation is acceptable.
Exit. Proceed to the next runner in the plan. Invoke this phase before every runner (except CAPA and HITL consult) in auto/full modes.
D‑10 Delivery & Publication
Goal. Ship human‑friendly deliverables and ensure reproducibility.
LLM MUST DO. 1. Write release/README.md (overview) and release/CHANGELOG.md (changes). 2. Create executive_brief.pdf , tech_whitepaper.pdf , api_reference.md and update all model/data/system cards.
3. Build reproducibility archive: generate RO‑Crate v1.2 under release/ro_crate/ containing artifacts, BOMs and proofs; compute rehydration/rehydration_matrix.csv and rehydration score. 4. Assign persistent identifiers (DOI via Zenodo/DataCite) and include release/IDENTIFIERS.md . 5. Prepare CITATION.cff and SWHIDs.
Gate – ShipIt. Pass if all upstream gates green or waived; needs‑human for outstanding issues; fail if provenance incomplete.
D‑11 Acceptance Review & Exit Wizard
Goal. Render a gate status table with links; collect waivers; finish packaging.
LLM MUST DO. 1. Assemble a table summarising each gate status, reasons, artifacts and waivers. 2. Collect waiver approvals (role, reason, timestamp) into HITL/waiver_log.jsonl . 3. Finalize packaging: zip run directory; include verification script for Rekor proofs and file hashes. 4. Emit final INDEX.md with artifact map, trace IDs and reproduction instructions. Gate – ExitReady. Pass if all gates green/waived and packaging complete.  
10
PM‑12 Post‑Market Monitoring & Continuous Improvement
Goal. Equip the human operator with a structured playbook to monitor the deployed invention, triage feedback and plan future iterations. This post‑market phase ensures that the system learns from real‑world usage and feeds insights back into the CAPA and planning loops.
LLM MUST DO. 1. Identify Monitoring Channels – Based on the invention type and deployment footprint, identify relevant channels to monitor: GitHub issue trackers, support email aliases, community forums, social media keywords, uptime dashboards, telemetry endpoints and review sites. Record the list and rationale. 2. Define Key Metrics – Specify what to monitor: bug report frequency, severity and recurrence; common feature request themes; performance and reliability thresholds; user sentiment and NPS scores; compliance incidents. Define thresholds that trigger corrective actions. 3. Generate Monitoring Playbook – Create post_market/Monitoring_Playbook.md containing: - A schedule for checks (e.g., weekly review
of GitHub issues; daily sentiment scraping). - Step‑by‑step instructions or code snippets for scripts that gather and summarise data from each channel. Use pseudocode or CLI commands (e.g., GitHub API queries, simple Python scripts). - Clear definitions of critical vs. non‑critical issues. Define triage logic: when to open a CAPA loop (critical bug), when to schedule a minor patch (non‑critical), and when to trigger a new GCP run (major V2 feature request). Represent this as a decision tree diagram or table. 4. Define Triage Logic & Escalation – Populate post_market/Triage_Rules.md with the decision tree described above.
Include guidelines on how to engage users, manage expectations, and involve the engineering/compliance team. Link to the CAPA process and RUNNER_CAPA. 5. Gate & Distribution – Set gate PostMarketPlaybook. Pass if the playbook and triage rules are comprehensive, actionable and aligned with regulatory obligations; needs‑human if incomplete; fail if key monitoring channels or metrics are missing. Deliver the playbook to the human operator and record acknowledgement.
Artifacts. *post_market/Monitoring_Playbook.md – a detailed monitoring guide.* post_market/ Triage_Rules.md – structured decision tree for triage and escalation. * Updated Gate_Signals.json (PostMarketPlaybook gate).
Exit. Once the playbook is delivered and acknowledged, the GCP run is concluded. Future iterations are initiated manually by the operator using the triage logic.
5. Observability & Tool Contracts
•  
Emit GenAI spans for every model/tool call. Include attributes: gen_ai.operation ,  llm.provider , llm.model , llm.request.tokens , llm.response.tokens , gcp.phase ,  gate.name , policy.decision . Add exception events on errors.
•  
Tool contracts are JSON files with fields: name , version , inputs , outputs ,  preconditions , postconditions , security_controls (mapped to OWASP LLM Top‑10),  failure_modes , rate_limits .
6. Friendly Gate Examples
•  
Creative Discovery – Pass: 3 DBs + 1 patent portal scanned; 72 raw ideas → 14 candidates scored. See  creative/Candidate_Set.csv .
11
•  
Data Rights – Fail: Consent lineage missing for dataset “crowd_voices_v2”. Check  Data_Rights_Card.md or choose Needs‑human.
•  
Supply‑Chain – Pass: SBOM & ML‑BOM present; SLSA + in‑toto attestations verified in Rekor (see  provenance/rekor_proofs/* ).
7. Notes for Materials/Alloys (Optional)
For materials/alloys problems, seed domain scans from Materials Project, OQMD, AFLOW, JARVIS‑DFT and HEA/MPEA literature; ground novelty with patent landscaping (CPC   C22C). For HEA strategies, consult Yeh 2004 and Cantor 2004. Track field momentum (e.g., AI‑assisted discovery like GNoME) but do not rely solely on hype.
8. HITL Consult Runner & Collaboration
In addition to formal go/no‑go gates, some tasks require nuanced human judgement (e.g., evaluating aesthetics, ethical trade‑offs or ambiguous design choices). To support this, any runner may invoke RUNNER_HITL_CONSULT as a subroutine.
Purpose. To solicit and integrate qualitative human feedback during a complex task. This differs from the needs‑human gate because it invites open‑ended consultation rather than a binary decision.
Inputs. *consult_prompt : The specific question or prompt for the human (e.g., “Rank these three UI designs from most to least intuitive” or “How should we balance privacy vs. personalization in this recommendation engine?”).* context_artifacts : List of file paths to artifacts the human should review (e.g., design mockups, ethical impact assessments, test reports). *expected_format : The format of the response (free‑text, ranking, multiple choice, JSON, etc.).
LLM MUST DO. 1. Package Context – Gather the specified context artifacts. Provide a concise summary for each artifact to guide the human, preserving links for full review. 2. Present Prompt – Present the consult prompt clearly, along with instructions on the expected response format, and provide the context summaries and links. Prompt the human to respond via the chat interface. 3. Ingest Response – Capture the human’s response. If the response is free‑text, perform semantic parsing to extract key points (e.g., ranking order, rationale). If structured, validate against the expected schema. 4. Generate Actionable Output – Translate the human feedback into machine‑readable instructions usable by the calling runner. For example, produce a JSON object capturing rankings or design constraints. Save this to HITL/ Human_Feedback.json or an appropriate path under the calling domain (e.g., creative/ Human_Feedback.json ). 5. Log Exchange – Append an entry to HITL/Consult_Log.jsonl recording the prompt, context artifacts, human response (redacted if sensitive), parsed output and timestamp. Respect data rights and privacy. 6. Gate – Set Consult_Complete gate. Pass if the human’s response is received and parsed; needs‑human if clarification is required; fail if no response or parsing fails.
Artifacts.* HITL/Consult_Log.jsonl – log of consultations. * HITL/Human_Feedback.json (or domain‑specific path) – structured feedback for downstream use.
Usage. Call this runner whenever subjective judgement or ethical deliberation is needed. It does not advance the phase map; rather, it returns control to the calling runner with enriched guidance.
12
This concludes the GCP V50 protocol. Use the Master Runners Codex to execute each phase as a runner with clear inputs, steps, gates and outputs.
13
