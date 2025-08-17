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
Overview
Genesis Code Protocol (GCP) is an AI‑native invention protocol that teaches a large language model how to
think and build: ideate → simulate → validate → productize → assure. The Flagship Edition layers a rigorous
rubric onto the baseline V49 protocol. It introduces multi‑agent orchestration, memory and claim‑graph
architecture, policy‑as‑code gates, novelty/SOTA benchmarking, adversarial and metamorphic testing,
observability from birth, supply‑chain provenance and rehydration/export guarantees. GCP runs
autonomously in chat or repository mode and produces auditable artifacts and a signed, reproducible
release pack.
What’s New — Flagship Edition
Multi‑Agent Council: Seven specialised roles — Planner, Researcher, Engineer, Adversary, Auditor,
Operator and Scribe — collaborate via an agent_graph.json . They decompose the Spark, curate
the evidence index and claim graph, build prototypes, run adversarial tests, enforce policies,
maintain SLOs and continuously update the index and manifest.
Flagship Rubric: Each phase must satisfy ten criteria: agent handoffs, tool orchestration plan,
memory architecture and retrieval rules, OPA/Rego gates with signed evidence, deterministic
acceptance tests (positive, negative and abuse), novelty vs SOTA thresholds, adversarial and
metamorphic testing, observability from birth, SBOM/AI‑BOM plus provenance, and a closeout/
rehydration plan with verifiable export.
New Artifacts and Ledgers: Flagship adds structured directories for agents, memory, tools, novelty,
redteam, metamorphic, observability, SBOM, provenance, Rehydration_Test and Evidence_Log in
addition to the existing ledgers. Each runner seeds a tools catalog, failure matrix, novelty
benchmarks, metamorphic relations, adversarial corpus, observability plan, SBOM, provenance
attestations and rehydration scripts. An optional Cost_Carbon_Report.md estimates energy use
and CO₂ emissions.
Policy‑as‑Code Gates: All decisions are enforced via Rego (OPA) policies with explicit allow/deny/
needs‑human outcomes. Auto mode prints the full Gate Decision Card before acting and logs
decisions to the DECISION_LEDGER.
Novelty & Benchmarking: Runs measure novelty scores against SOTA baselines (e.g., HELM,
MMLU‑Pro, GAIA, SWE‑Bench). Deterministic acceptance tests include metamorphic/property‑based
relations and adversarial prompts.
Observability & Provenance: Telemetry traces, metrics and logs are planned up front; supply‑chain
artifacts such as SBOMs and signed provenance attestations are mandatory.
Keep a Changelog
Conventional Commits
Semantic Versioning
•
•
•
•
•
•
3
Rehydration Proof: Each run produces scripts and evidence enabling third parties to reconstruct the
result; a run is incomplete unless the audit package can be rehydrated.
What’s New — V49 (baseline)
Gate Decision Card (Auto Mode): Auto Mode now prints the full Gate Decision Card (options,
rationale and recommendation) before acting; verbosity is configurable.
Runner System: Optional domain packs — Code, Physical, Theory, OT, Mobility, LifeSci, AgMRV and
FinTech — add extra roles, artifacts and micro‑gates. Aliases (e.g., industrial‑robotics maps to
[OT, Mobility] ) make attachment intuitive.
Alias System: Human‑friendly synonyms map to runner names.
Reproducibility Gate: Adds C7.Repro with ENV_LOCKFILE.yml , REPRO_PROTOCOL.md and
REPRO_RESULTS.csv .
11.3 IP & Disclosure: Explicit IP, export and safe‑use review before packaging.
Evidence TTL Defaults: CE refresh cadence (R1 = 180 days, R2 = 90 days, R3 = 30–60 days) defined in
15_ce/PLAN.md .
Manifest & Ledgers: Expanded artifact conventions and auto‑seeded templates.
Quick Start (LLM‑Only)
Upload the Flagship protocol file ( GCP V49 Flagship Edition.md ) to your LLM.
Prompt your LLM with the following template:
Initiate GCP and Run Spark: <YOUR_SPARK>.
Mode: <Auto|Full Run>.
Risk Tier: <R1|R2|R3>.
Objective: <Describe the invention goal>.
Constraints: <license=MIT; no PII in logs; max_passes_per_phase=2; evidence ≥2
independent sources per critical claim>.
Deliverables: <Specify high‑level outputs>.
# optional runner(s)
attach runner <code|physical|theory|ot|mobility|lifesci|agMRV|fintech>
At each ⛔ checkpoint, reply with proceed 1 , branch Phase <N> , return C#.# or end & export .
You can switch modes at any time with switch to auto mode or switch to full run mode . In
Auto Mode the full decision card is printed before acting.
Phase Map & Gates
The Flagship edition preserves the phase numbering (−1 through 15) of V49 but requires each phase to
satisfy the Flagship rubric. See Charts & Graphs for a visual phase map, a table of checkpoints and the
universal gate decision card.
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
Risk‑Tiered Lanes
Tier Typical Use Rigor
R1
Low risk / low
impact N ≥ 15 repetitions; ≥ 5 seeds; integrity‑lite
R2 Moderate N ≥ 30; ≥ 10 seeds; full integrity; SBOM/signing
R3 High/regulated N ≥ 50; ≥ 20 seeds; FMEA, STPA, GSN, DPIA, HIL; continuous evaluation
on by default
Runner System (Optional)
Attach only what you need. Aliases are case‑insensitive; spaces, underscores and hyphens are ignored. Each
runner seeds an agent graph, memory configuration, policy module, tools catalog and other artifacts.
Micro‑gates cover metamorphic invariants, novelty, adversarial abuse, observability, supply‑chain and
rehydration tests.
Runner Purpose (short) Example aliases
Code Software/ML/Agents/SDK/CLI/API code, dev, ml, ai, agent, sdk, cli, api
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
Alias bundles (examples): medical-ai ⇒ [Code, LifeSci] ; industrial-robotics ⇒ [OT,
Mobility] .
Links & Further Reading
Flagship Specification: GCP V49 Flagship Edition
Master Runners Codex — Flagship Edition: Master Runners Codex
Charts & Graphs: Charts.md
About: About.md
•
•
•
•
5
6


## Repository Structure

<!-- BEGIN REPO TREE -->
```text
- **.devcontainer/**
  - devcontainer.json
- **CLI Bundle/**
  - Readme.md
  - audit\_utils.py
  - full\_run.py
  - gcp\_cli.py
  - phase1.py
  - phase6.7.py
  - prompt\_utils.py
  - requirements.txt
- **Documents/**
  - **protocol/**
    - overview
  - AI ChatGPT Critical Analysis GCP V45.6D.md
  - AI ChatGPT Critical Analysis GCP V46.md
  - AI ChatGPT Critical Analysis V47 Full Run EV issue.md
  - AI Claude Critical Analysis GCP V45.6d.md
  - AI Claude Critical Analysis GCP V46.md
  - AI Claude Critical Analysis V47 full run EV issue.md
  - AI Grok Critical Analysis GCP V45.6D.md
  - AI Grok Critical Analysis GCP V46 .md
  - AI Grok Critical Analysis V47 Full Run EV issue.md
  - Feature Requests.md
  - Issue Template.md
  - Pull Request Template.md
  - Requirements.md
  - Security.md
  - Setup.py
  - index.md
  - releases.md
  - security\_report.md
- **GCP Runners/**
  - A V49.0 Master Runners Codex: Flagship Edition.md
  - Archaeology\_History Runner.md
  - Culinary Cartridge.md
  - Deep Sea Runner.md
  - Education Runner.md
  - Energy\_Power Runner.md
  - Entertainment Cartridge.md
  - Exotics Runner.md
  - Humanitarian\_Disaster Relief Cartridge.md
  - Infrastructure Runner.md
  - Legal Cartridge.md
  - Political Systems Runner.md
  - Public Programs\_Policy Runner.md
  - Spaceflight\_Aerospace Runner.md
  - Sports\_Athletics Cartridge.md
  - Theology Runner.md
  - V49.0 Agriculture & Environmental MVR Runner.md
  - V49.0 Code Runner.md
  - V49.0 Finance & FinTech Runner.md
  - V49.0 Industrial & Utilities OT Runner.md
  - V49.0 Life Sciences Runner.md
  - V49.0 Mobility & Autonomy Runner.md
  - V49.0 Physical Runner.md
  - V49.0 Theory Runner.md
- **GCP-All-Variants/**
  - Changelog.md
  - Changelog\_P2.md
  - GCP V49 Flagship Edition.md
  - V09.md
  - V11.md
  - V20.md
  - V22.md
  - V23.md
  - V30.md
  - V34.md
  - V35.md
  - V36.md
  - V40.md
  - V41.md
  - V42.md
  - V43.0.md
  - V43.6.md
  - V43.7.md
  - V44.1.md
  - V44.7.md
  - V44.8.md
  - V44.9b.md
  - V44.9d.md
  - V45.0.md
  - V45.1.md
  - V45.2.md
  - V45.3.md
  - V45.4A.md
  - V45.5.md
  - V45.6.md
  - V46.0.md
  - V46.5.md
  - V47.0.md
  - V47.1.md
  - V47.2.md
  - V48.0.md
  - V49.0.md
- **Notebooks/**
  - **Duality Unzipped Ouput/**
    - BENCHMARK\_LEDGER.md
    - DECISION\_LEDGER.md
    - ENV\_LOCKFILE.yml
    - Makefile
    - README.md
    - S49\_6\_Param\_Sweep.csv
    - S49\_extended\_details (1).csv
    - S49\_extended\_summary (1).csv
    - \_\_init\_\_.py
    - adaptive\_controller.py
    - api\_server.py
    - dataplane.py
    - default\_policy.yml
    - duality-agent.service
    - flow\_classifier.py
    - main.py
    - masque\_placeholder.py
    - openapi.yaml
    - policy.py
    - requirements.txt
    - setup\_duality.sh
    - sim\_duality.py
    - sqm\_duality.conf
  - **Full Runs/**
    - High Speed Internet Issue V49 Full Run.md
    - Known EV issue Full Run, GCPv47.md
    - Latch Full run.md
    - Quantum Mechanics Full Run.md
    - Solar Energy Full Run.md
    - V48 Full Run.md
  - **Modulift Unzipped Output/**
    - CMakeLists.txt
    - README\_MODULIFT\_v0.1.md
    - REFERENCES.md
    - S48\_-0.5A\_CK\_Drift.md
    - S48\_-0.8\_TRIZ\_Contradictions.md
    - S48\_-1\_WorthIt\_Report.md
    - S48\_10.0\_Simplicity\_Audit.md
    - S48\_10.5\_Optimization\_Ledger.md
    - S48\_1\_Context\_Dossier.md
    - S48\_2\_Influence\_Matrix.md
    - S48\_3\_Design\_Envelope.md
    - S48\_4\_BranchTree.md
    - S48\_5\_Architecture\_Blueprint.md
    - S48\_6\_FunctionalPlan.md
    - S48\_8.9\_RedTeam\_Findings.md
    - S48\_9\_Validation\_Template.md
    - bench\_build.ps1
    - bench\_build.sh
    - enable-named-modules.cmake
    - headers.cmake
    - hu-clang-gcc.cmake
    - hu-msvc.cmake
    - lib.cpp
    - main.cpp
    - math.hpp
    - modulift-bench.yml
    - modulift\_explain.py
    - modulift\_explain\_rules.json
    - util.hpp
  - A Example Explanation.md
  - Adaptive QoS Allocator.ipynb
  - Alloy Perceptual Loss.py
  - Alloyscript.py
  - Audio Processing, v45.6.md
  - JACCO.ipynb
  - Latch Latent capability Harnesser.md
  - MOSAIC.ipynb
- **Scripts/**
  - fix\_md\_spacing.py
  - generate\_changelog.py
  - generate\_repo\_toc.py
  - update\_repo\_structure.py
- **docker/**
  - .dockerignore
  - Dockerfile
  - requirements.txt
- .dockerignore
- About.md
- CHANGELOG.md
- CITATION.cff
- Charts.md
- Code of Conduct.md
- Contributing.md
- Dockerfile
- GCP Current Version(49 Flagship Edition). AI-Native Operational Manual.md
- LICENSE.md
- README.md
- SECURITY.md
- Table Of Contents.md
- mkdocs.yml
- requirements.txt
```
<!-- END REPO TREE -->
