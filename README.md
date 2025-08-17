Genesis Code Protocol (GCP) — V49 (Flagship
Edition)
<!-- Badges -->
License: MIT
Release
Status
Python
Stars
Forks
Issues
PRs
Last Commit
Code Size
Contributors
CI: Python
1
Security Scan
Repo Tree Sync
Top‑Level ToC
Changelog
Notebooks
Docker Build
Code Style: Black
pre‑commit
Type Checking: mypy
Tests: pytest
Docs
OpenSSF Scorecard
PRs Welcome
Code of Conduct
Discussions
2
GCP: Genesis Code Protocol
Status: Active • License: MIT • Language: Python 3.10+
Edition: V49 (Flagship Edition)
GCP is an AI‑native invention protocol that teaches an LLM how to think and build: ideate → simulate →
validate → productize → assure. In the Flagship Edition the core V49 protocol is extended with a rigorous
multi‑agent rubric, policy‑as‑code gates, memory architecture, novelty/SOTA benchmarking, adversarial
and metamorphic testing, observability, supply‑chain provenance, and rehydration/export guarantees. The
protocol runs autonomously in chat or repository mode, producing auditable artifacts and a signed,
reproducible release pack. See About for the rationale and safety posture.
What’s New — Flagship Edition
Multi‑Agent Council: Seven specialized roles — Planner, Researcher, Engineer, Adversary,
Auditor, Operator and Scribe — collaborate via an agent_graph.json to decompose the Spark,
curate the evidence index and claim graph, build prototypes, run adversarial tests, enforce policies,
maintain SLOs and continuously update the index & manifest.
Flagship Rubric: Every phase must satisfy ten criteria: agent handoffs, tool orchestration plan,
memory architecture & retrieval rules, OPA/Rego gates with signed evidence, deterministic
acceptance tests (positive/negative/abuse), novelty vs SOTA thresholds, adversarial & metamorphic
testing, observability from birth, SBOM/AI‑BOM + provenance, and a closeout/rehydration plan with
verifiable export.
New Artifacts & Ledgers: Flagship adds structured directories for agents/ , memory/ , tools/ ,
novelty/ , redteam/ , metamorphic/ , observability/ , SBOM/ , provenance/ ,
Rehydration_Test/ and Evidence_Log/ , alongside existing ledgers such as 07_ledgers/
DECISION_LEDGER.md . Each runner seeds a tools catalog, failure matrix, novelty benchmarks,
metamorphic relations, adversarial corpus, observability plan, SBOM, provenance attestations and
rehydration scripts. An optional Cost_Carbon_Report.md estimates energy use and CO₂
emissions.
Policy‑as‑Code Gates: All decisions are enforced via Rego policies (OPA) with explicit allow/deny/
needs‑human outcomes. Auto mode prints the full Gate Decision Card before acting and logs
decisions to the DECISION_LEDGER.
Keep a Changelog
Conventional Commits
Semantic Versioning
•
•
•
•
3
Novelty & Benchmarking: Runs now measure novelty scores against SOTA baselines (e.g., HELM/
MMLU‑Pro/GAIA/SWE‑Bench) and require novelty ≥ threshold; deterministic acceptance tests
include metamorphic/property‑based relations and adversarial prompts.
Observability & Provenance: Telemetry traces, metrics and logs are planned up front; supply‑chain
artifacts such as SBOMs and signed provenance attestations are mandatory.
Rehydration Proof: Each run produces scripts and evidence enabling third parties to reconstruct the
result; a run is incomplete unless the audit package can be rehydrated.
What’s New — V49 (baseline)
Gate Decision Card (Auto Mode) — FIXED: Auto Mode now prints the full Gate Decision Card
(options, rationale, recommendation) before acting; verbosity is configurable.
Runner System: Optional domain packs (Code, Physical, Theory, OT, Mobility, LifeSci, AgMRV,
FinTech) add extra roles, artifacts and micro‑gates. Aliases (e.g., industrial-robotics ⇒ [OT,
Mobility] ) make attachment intuitive.
Alias System: Human‑friendly synonyms map to runner names.
Reproducibility Gate: Adds C7.Repro with ENV_LOCKFILE.yml , REPRO_PROTOCOL.md and
REPRO_RESULTS.csv .
11.3 IP & Disclosure: Explicit IP/export/safe‑use review before packaging.
Evidence TTL Defaults: CE refresh cadence (R1=180d, R2=90d, R3=30–60d) defined in 15_ce/
PLAN.md .
Manifest & Ledgers: Expanded artifact conventions and auto‑seeded templates.
Quick Start (LLM‑Only)
Upload the Flagship protocol file ( GCP V49 Flagship Edition.md ) to your LLM.
Prompt:
Initiate GCP and Run Spark: <YOUR_SPARK>.
Mode: <Auto|Full Run>.
Risk Tier: <R1|R2|R3>.
Objective: <Describe the invention goal>.
Constraints: <license=MIT; no PII in logs; max_passes_per_phase=2; evidence ≥2
independent sources per critical claim>.
Deliverables: <Specify high‑level outputs>.
# optional runner(s)
attach runner <code|physical|theory|ot|mobility|lifesci|agMRV|fintech>
At each ⛔ checkpoint, reply with proceed 1 , branch Phase <N> , return C#.# , or end & export .
Switch modes at any time with switch to auto mode or switch to full run mode . Auto mode
prints the full decision card before acting.
•
•
•
•
•
•
•
•
•
•
1.
2.
4
Phase Map & Gates (V49)
See Charts & Graphs for a visual phase map, a table of checkpoints and the universal gate decision card.
Flagship edition preserves the phase numbering (−1 through 15) but requires each phase to satisfy the
Flagship rubric.
Risk‑Tiered Lanes (R1–R3)
Tier Typical Use Rigor
R1
Low risk / low
impact N≥15 reps; ≥5 seeds; integrity‑lite
R2 Moderate N≥30; ≥10 seeds; full integrity; SBOM/signing
R3 High/regulated N≥50; ≥20 seeds; FMEA/STPA/GSN/DPIA/HIL; continuous evaluation on
by default
Runner System (Optional)
Attach only what you need. Aliases are case‑insensitive; spaces/underscores/hyphens are ignored. Each
runner seeds an agent graph, memory configuration, policy module, tools catalog and other artifacts.
Micro‑gates cover metamorphic invariants, novelty, adversarial abuse, observability, supply‑chain and
rehydration tests.
Runner Purpose (short) Example aliases
Code SW/ML/Agents/SDK/CLI/API code, dev, ml, ai, agent, sdk, cli, api
Physical Hardware/Mechatronics/EE/ME/Embedded hardware, mechanical, electrical,
embedded_hw
Theory Axioms, conjectures, formal proofs theory, math, formal, proof
OT
Industrial/Utilities PLC‑SCADA‑DCS,
standards
industrial, utilities, plc, scada, dcs, 61131,
62443, nerc
Mobility Auto/Aero/Robot ECUs & safety auto, autosar, ecu, do178c, do254, robotics
LifeSci GxP/CSV/CSA; 21 CFR Part 11; IEC 62304;
ISO 14971
pharma, gxp, gamp, 21cfr11, annex11,
62304, 14971
AgMRV Agriculture & environmental MRV ag, agriculture, mrv, field, trials, soil, carbon
FinTech PCI/SOX/AML/KYC/sanctions; model risk
SR 11‑7
finance, payments, pci, sox, aml, kyc,
sanctions
5
Alias bundles (examples): medical-ai ⇒ [Code, LifeSci] ; industrial-robotics ⇒ [OT,
Mobility] .
Links & Further Reading
Flagship Specification: GCP V49 Flagship Edition.md
Master Runners Codex — Flagship Edition: Master Runners Codex
Charts & Graphs: Charts.md
About: About.md
•
•
•
•
6
