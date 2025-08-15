# Genesis Code Protocol (GCP) — V49

<!-- CORE BADGES -->
[![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen)](./Documents/LICENSE.md)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
[![Stars](https://img.shields.io/github/stars/lazyxeon/Genesis-Code-Protocol?style=flat)](https://github.com/lazyxeon/Genesis-Code-Protocol/stargazers)
[![Forks](https://img.shields.io/github/forks/lazyxeon/Genesis-Code-Protocol?style=flat)](https://github.com/lazyxeon/Genesis-Code-Protocol/network/members)
[![Issues](https://img.shields.io/github/issues/lazyxeon/Genesis-Code-Protocol)](https://github.com/lazyxeon/Genesis-Code-Protocol/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/lazyxeon/Genesis-Code-Protocol)](https://github.com/lazyxeon/Genesis-Code-Protocol/pulls)
[![Last Commit](https://img.shields.io/github/last-commit/lazyxeon/Genesis-Code-Protocol)](https://github.com/lazyxeon/Genesis-Code-Protocol/commits/main)
[![Code Size](https://img.shields.io/github/languages/code-size/lazyxeon/Genesis-Code-Protocol)](https://github.com/lazyxeon/Genesis-Code-Protocol)
[![Contributors](https://img.shields.io/github/contributors/lazyxeon/Genesis-Code-Protocol)](https://github.com/lazyxeon/Genesis-Code-Protocol/graphs/contributors)

<!-- CI / AUTOMATION BADGES -->
[![Python CI](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/Python-CI.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/Python-CI.yml)
[![Security Scan](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/security-scan.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/security-scan.yml)
[![Repo Tree Sync](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/update-repo-structure.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/update-repo-structure.yml)
[![Top-Level ToC](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/update-toc-file.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/update-toc-file.yml)
[![Changelog](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/generate-changelog.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/generate-changelog.yml)
[![Notebooks](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/validate-notebooks.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/validate-notebooks.yml)
[![Docker Build](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/docker-build.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/docker-build.yml)

<!-- QUALITY / STYLE -->
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Type Checking: mypy](https://img.shields.io/badge/type%20checking-mypy-2A6DB2)](https://mypy.readthedocs.io/)
[![Tests: pytest](https://img.shields.io/badge/tests-pytest-0A9EDC)](https://docs.pytest.org/)
[![Docs](https://img.shields.io/badge/docs-mkdocs%20material-blue)](https://lazyxeon.github.io/Genesis-Code-Protocol/)
[![Container](https://img.shields.io/badge/ghcr-image-blue)](https://ghcr.io/lazyxeon/Genesis-Code-Protocol)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/lazyxeon/Genesis-Code-Protocol/badge)](https://scorecard.dev/viewer/?uri=github.com/lazyxeon/Genesis-Code-Protocol)
[![Release](https://img.shields.io/github/v/release/lazyxeon/Genesis-Code-Protocol)](https://github.com/lazyxeon/Genesis-Code-Protocol/releases/latest)

<!-- Tech stack badges -->
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white&style=for-the-badge)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white&style=for-the-badge)

[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-Structured%20Streaming-FDEE21?logo=apachespark&logoColor=black&style=for-the-badge)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Lakehouse-1F6FEB?style=for-the-badge)](https://delta.io/)

[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white&style=for-the-badge)
[![Dev Containers](https://img.shields.io/badge/Dev%20Containers-Ready-2B2F77?logo=visualstudiocode&logoColor=white&style=for-the-badge)](https://code.visualstudio.com/docs/devcontainers/tutorial)
[![Docs: MkDocs Material](https://img.shields.io/badge/Docs-MkDocs%20Material-000000?logo=mkdocs&logoColor=white&style=for-the-badge)](https://squidfunk.github.io/mkdocs-material/)

[![CI: GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white&style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions)
[![SBOM / SPDX](https://img.shields.io/badge/SBOM-SPDX-009639?logo=spdx&logoColor=white&style=for-the-badge)](https://spdx.dev/learn/overview/)
[![CITATION.cff](https://img.shields.io/badge/Citation-CITATION.cff-2962FF?style=for-the-badge)](./CITATION.cff)

<!-- Auto-updating language stats -->
[![Top language](https://img.shields.io/github/languages/top/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol)
[![Language count](https://img.shields.io/github/languages/count/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol)

> **Formerly:** GRCP (Genesis Recursive Code Protocol)  
> **Status:** Active • **License:** MIT • **Language:** Python 3.10+  
> **Edition:** **V49** (successor to V48; see CHANGELOG for deltas)

**GCP** is an **AI-native invention protocol** that teaches an LLM **how to think and build**: *ideate → simulate → validate → productize → assure*. It’s a **single protocol document** any capable LLM can follow to produce **auditable artifacts** and a **field-test-ready** release pack. GCP is **LLM-agnostic** and runs fully in chat; this repo adds optional accelerators (CLI, notebooks, CI).  
See **About** for the rationale and safety posture.

---

## What’s New — V49

- **Gate Decision Card (Auto Mode) — FIXED**: Auto Mode now **prints the full Gate Decision Card** (options + rationale + recommendation) **before acting**, then proceeds. Verbosity is configurable.  
  Commands: `switch to Full Run | switch to Auto | set auto_gate_verbosity = full|brief | set auto_gate_preview = on|off`.  
- **Runners (optional enhancers)**: Attach domain packs that add roles, artifacts, and micro-gates:
  **Code, Physical, Theory, OT, Mobility, LifeSci, AgMRV, FinTech**.  
  Commands: `attach runner <...> | detach runner <...> | show runner status`.  
- **Alias System**: Human-friendly synonyms (e.g., `attach runner industrial-robotics` → `[OT, Mobility]`).
- **Reproducibility Gate**: **C7.Repro** with `REPRO_PROTOCOL.md`, `REPRO_RESULTS.csv`, `ENV_LOCKFILE.yml`.
- **11.3 IP & Disclosure**: explicit IP/export/safe-use review before packaging.
- **Evidence TTL Defaults**: CE refresh cadence (R1=180d, R2=90d, R3=30–60d) defined in `15_ce/PLAN.md`.
- **Manifest + Ledgers**: Expanded artifact conventions and runner-seeded templates.

---

## Quick Start (LLM-Only)

1) **Upload** the protocol file (*GCP V49 — AI-Native Operational Manual*) to your LLM.  
2) **Prompt**:

Initiate GCP and Run Spark: <your idea>.
Mode: <Full Run | Auto>.
Risk Tier: <R1 | R2 | R3>.
Objective: <success criteria>.
Constraints: <hard/soft>.
Deliverables: <code/docs/field kit/etc>.

Optional runner(s)
attach runner <Code|Physical|Theory|OT|Mobility|LifeSci|AgMRV|FinTech>

sql
Copy
Edit

At each ⛔ checkpoint, reply with:

proceed 1
branch Phase <n>
return C#.#
end & export

markdown
Copy
Edit

Switch anytime: `switch to auto mode` or `switch to full run mode`.

---

## Phase Map & Gates (V49)

**Pre-Execution**  
- **−0.8** TRIZ/ARIZ *Contradiction Resolution* → **C−0.8**  
- **−0.5A** C-K *Concept–Knowledge Drift Check* → **C−0.5A**  
- **−1** Worth-It Discovery Sprint → **C−0.5**

**Core Execution**  
0 Opportunity & Mode / Runner Handshake → **C0.1**  
1 Context & Precedents → **C1.1**  
2 Influence Harvesting → **C2.1**  
2.5 Futures & Morph Space → **C2.5**  
3 Constraints & Envelope → **C3.1**  
4 Hypotheses & Branch Tree → **C4.1**  
4.A Red-Team Hypothesis Attack → **C4.A**  
5 Conceptual Modeling & Architecture → **C5.1**  
6 Simulation & Functional Modeling → **C6.1**  
6.5 Multi-Agent War Game → **C6.5**  
7 Iterative Refinement → **C7.1**  
9 Validation & Benchmarking → **C7 / C7.Sigma / C7.Repro**  
10 Simplicity (**C8.4**) → Optimization (**C8.5**)  
11 Productization & Packaging (+ **11.3 IP & Disclosure**) → **C6.9**  
12 Documentation & Handoff → **C12.1**  
13 Deployment Readiness & Safety Case → **C9** *(requires **C13.5** PASS)*  
13.5 Devastation Protocol → **C13.5**  
14 Continuous Evaluation → **C14.1**  
14.5 Continuous Adversary Shadowing → **C14.5**  
15 Archival, Export, Postmortem → **C15.1**

> **Universal Gate Decision Card (FRM & AM):** prints options (Proceed / Branch / Return / End & export) with short descriptions, **AI recommendation** + confidence, cost/time, and risk. *(AM now prints the full card before acting.)*

---

## Risk-Tiered Lanes (R1–R3)

| Tier | Typical Use | Rigor |
|---|---|---|
| R1 | Low risk / low impact | N≥15 reps; ≥5 seeds; integrity-lite |
| R2 | Moderate | N≥30; ≥10 seeds; full integrity; SBOM/signing |
| R3 | High/regulated | N≥50; ≥20 seeds; FMEA/STPA/GSN/DPIA/HIL; CE on by default |

---

## Artifacts & Packaging (V49)

- **Run ID:** `S49` (short alphanumeric)  
- **Naming:** `RunID_Phase.Subphase_Artifact_Short.ext`  
- **Primary ledgers:** RUN_LEDGER • DECISION_LEDGER • ASSUMPTION_LEDGER • EVIDENCE_LEDGER • BENCHMARK_LEDGER • OPTIMIZATION_LEDGER • RISK_SAFETY_LEDGER • COMPLIANCE_LEDGER • **CONTRADICTION_LEDGER** • **C_K_LEDGER** • **MORPH_FUTURES_LEDGER** • **ADVERSARY_LEDGER**  
- **Base repro templates (no runner):** `06_evidence/replication/` → **REPRO_PROTOCOL.md**, **REPRO_RESULTS.csv**, **ENV_LOCKFILE.yml**  
- **Runner attach = auto-seed** domain-specific templates (see **Charts & Graphs** for a visual and **CHANGELOG** for file lists).

---

## Runner System (Optional)

Attach only what you need. Aliases are case-insensitive; spaces/underscores/hyphens ignored.

- **Code** (aka: code, dev, ml, ai, agent, sdk, cli, api)  
- **Physical** (hardware/mechatronics; embedded_hw, mechanical, electrical)  
- **Theory** (axioms, conjectures, proofs)  
- **OT** (industrial/utilities; PLC/SCADA/DCS; 61131/62443/NERC)  
- **Mobility** (automotive/aerospace/robotics; AUTOSAR, DO-178C/254)  
- **LifeSci** (GAMP5 CSV/CSA; 21 CFR Part 11; IEC 62304; ISO 14971)  
- **AgMRV** (agriculture & environmental MRV; trials/QA/QC)  
- **FinTech** (PCI, SOX, AML/KYC/sanctions; model-risk SR 11-7)

Examples:  
`attach runner medical-ai` → `[Code, LifeSci]`  
`attach runner industrial-robotics` → `[OT, Mobility]`

---

## Docs

- **About** → [About.md](./About.md)  
- **Charts & Graphs** → [Charts.md](./Charts.md)  
- **Changelog** → [CHANGELOG.md](./CHANGELOG.md)

---

## Version Matrix (Historic Highlights)

See **CHANGELOG** for details: v45.6D → V46 → V46.5 → V47 → V47.1 → V47.2 → **V48** → **V49**.

📚 GCP Wiki

Home: overview, quickstart, phases/gates, modes, checkpoint UX

👉 https://github.com/lazyxeon/Genesis-Code-Protocol/wiki

## Repository Structure

Overview Of Entire Repo, Auto Generated by Workflow.
 
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
  - V49.0 Agriculture & Environmental MVR Runner.md
  - V49.0 Code Runner.md
  - V49.0 Finance & FinTech Runner.md
  - V49.0 Industrial & Utilities OT Runner.md
  - V49.0 Life Sciences Runner.md
  - V49.0 Master Runner.md
  - V49.0 Mobility & Autonomy Runner.md
  - V49.0 Physical Runner.md
  - V49.0 Theory Runner.md
- **GCP-All-Variants/**
  - Changelog.md
  - Changelog\_P2.md
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
- **Images/**
  - ledgers\_table.png
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
- GCP Current Version(49). AI-Native Operational Manual.md
- LICENSE.md
- README.md
- SECURITY.md
- Table Of Contents.md
- mkdocs.yml
- requirements.txt
```
<!-- END REPO TREE --></details>

