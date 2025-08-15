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
