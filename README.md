# Genesis Code Protocol (GCP) — V50 Flagship

> **GCP V50 Flagship** — the next‑generation AI‑native invention protocol. This release supersedes the V49 Flagship edition, integrating autonomous spark generation and refined governance & compliance frameworks. A capable LLM can follow these steps to transform a vague "spark" into a reproducible, auditable invention package with provenance and a verifiable exit wizard.

<!-- PR Mentor badges -->
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


[![LLM Reviewer: optional](https://img.shields.io/badge/LLM%20Reviewer-optional-lightgrey)](docs/llm-reviewer.md)
[![Danger JS](https://img.shields.io/badge/Danger%20JS-enabled-blue?logo=npm)](https://danger.systems/js/)
[![reviewdog](https://img.shields.io/badge/reviewdog-enabled-blue)](https://github.com/reviewdog/reviewdog)
[![Semgrep CI](https://img.shields.io/badge/Semgrep-ci--ready-blue)](https://semgrep.dev/docs/deployment/add-semgrep-to-ci)
[![Ruff](https://img.shields.io/badge/Ruff-linting-blue)](https://docs.astral.sh/ruff/)

Quick nav: [What’s New](#whats-new) • [Quick Start](#quick-start) • [Phase Map](#phase-map) • [Runners & Cartridges](#runners--cartridges) • [Artifacts](#artifacts--ledgers) • [Security](#security--provenance) • [License](#license)

---

## What’s New

- **Autonomous spark generation** (*I‑1*): V50 introduces an optional I‑1 phase for collaborative brainstorming. When no problem spark is provided, the protocol generates a high‑value problem based on a domain interest and returns a brief for user approval. Architect‑led (*spark_provided*) flows remain supported.
- **Unified bootstrap**: The bootstrap phase clarifies `mode`, `startup_mode`, `run_id` and `workdir` parameters. Hard rules enforce phase order and gate cards.
- **Governance & compliance mapping**: V50 maps directly to NIST AI RMF, ISO/IEC 42001, the EU AI Act and FinOps/Sustainability standards.
- **Extended runners & phases**: Additional runners support privacy & DP evaluation, MITRE ATLAS threat modelling, FinOps, SBOM & ML‑BOM generation, C2PA credentials and EU AI Act technical documentation.
- **Backward compatibility**: All additions are additive; existing V49 runners and cartridges remain valid and forward‑compatible.

## Important Updates

- Large models (e.g. ChatGPT5 and Gemini 2.5) run V50 seamlessly; earlier models may struggle as gating complexity increases.
- Data rights, privacy budgets and SBOM/AI‑BOM generation are mandatory for R2+ risk tiers.

---

## Quick Start

```
Initiate GCP V50 for Spark: <your idea> or leave empty to use autonomous brainstorming.
Mode: <auto | full | manual> ; Startup: <spark_provided | autonomous> ; Risk: <r1 | r2 | r3>
Cartridges: <optional domain packs> ; Runners: <optional>
Objective: <clear success criteria> ; Constraints: <hard/soft> ; License: MIT ; No PII in logs.
Deliverables: <explicit artifacts>.
```

Universal commands remain unchanged from V49: `proceed 1`, `branch Phase <n>`, `return C#.#`, `end & export`, `switch to Full Run`, `switch to Auto`, `set auto_gate_verbosity=full|brief`, `set auto_gate_preview=on|off`.

---

## Phase Map

See **Charts.md** for a visual phase map and gate decision flow. In summary, V50 adds an initial **I‑1 Autonomous Spark Generation** phase ahead of the C‑0 ambiguity‑to‑brief phase and retains phases up to 15 Archival/Export with minor refinements.

---

## Runners & Cartridges

Attach domain **Runners** (e.g., Code, Hardware, LifeSci) and **Cartridges** (e.g., Code, Legal, SynBio) when needed. Runners implement deterministic modules with defined inputs, steps, gates and telemetry. Cartridges provide embeddings, indexes, lexicons, tools and governance notes for a domain. They extend retrieval and reasoning capabilities but are optional.

For detailed definitions and specifications, see the **GCP V50** supplemental documents:

- **Master Runners Codex** — the library of standard runners, including contracts, steps, gates and telemetry: [GCP V50 Master Runners Codex](GCP%20Runners/GCP%20V50%20Supplemental%20Docs/GCP%20V50%20Master%20Runners%20Codex.md)
- **Cartridges Pack** — modular domain knowledge packages with schemas, lexicons, index configurations and tool contracts: [GCP V50 Cartridges Pack](GCP%20Runners/GCP%20V50%20Supplemental%20Docs/GCP%20V50%20Cartridges%20Pack.md)

These links provide the full runner and cartridge specifications for V50.

---

## Artifacts & Ledgers

- **Evidence & Claims:** `Evidence_Index.jsonl`, `ClaimGraph.json`, `Source_Reliability.csv`
- **Reproducibility:** `REPRO_PROTOCOL.md`, `REPRO_RESULTS.csv`, `ENV_LOCKFILE.yml`
- **Provenance:** SBOM/ML‑BOM, signatures, attestations
- **Gate signals:** `Gate_Signals.json` (allow | deny | needs‑human)
- **Indexes:** `INDEX.md`, `MANIFEST.json`
- **Export:** `XW/` (ZIP/PDF‑A package with receipts)

---

## Security & Provenance

See `SECURITY.md` for the security policy and supply‑chain controls. V50 continues to publish SBOMs and C2PA manifests to guarantee provenance and reproducibility.

---

## Docs

- **About** → [About.md](./About.md)  
- **Charts & Graphs** → [Charts.md](./Charts.md)  
- **Changelog** → [CHANGELOG.md](./CHANGELOG.md)

---

## Version Matrix (Historic Highlights)

See **CHANGELOG** for details: v45.6D → V46 → V46.5 → V47 → V47.1 → V47.2 → **V48** → **V49**.

---

## License

MIT — see `LICENSE.md`.

---

## About

See `About.md` for core principles and additional context.

---

📚 GCP Wiki

Home: overview, quickstart, phases/gates, modes, checkpoint UX

👉 https://github.com/lazyxeon/Genesis-Code-Protocol/wiki

---

# **Repository Structure**

Overview Of Entire Repo, Auto Generated by Workflow.
 
<details><!-- BEGIN REPO TREE -->
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
  - A Documents Readme.md
  - AI ChatGPT Critical Analysis Flagship GCP V49.md
  - AI ChatGPT Critical Analysis GCP V45.6D.md
  - AI ChatGPT Critical Analysis GCP V46.md
  - AI ChatGPT Critical Analysis V47 Full Run EV issue.md
  - AI Claude Critical Analysis Flagship GCP V49.md
  - AI Claude Critical Analysis GCP V45.6d.md
  - AI Claude Critical Analysis GCP V46.md
  - AI Claude Critical Analysis V47 full run EV issue.md
  - AI Grok Critical Analysis Flagship GCPV49.md
  - AI Grok Critical Analysis GCP V45.6D.md
  - AI Grok Critical Analysis GCP V46 .md
  - AI Grok Critical Analysis V47 Full Run EV issue.md
  - Feature Requests.md
  - Issue Template.md
  - Operations Manual.md
  - Pull Request Template.md
  - Requirements.md
  - Security.md
  - Setup.py
  - Theoretical Soundness Analysis.md
  - index.md
  - releases.md
  - security\_report.md
- **GCP Runners/**
  - **GCP V50 Supplemental Docs/**
    - GCP V50 Cartridges Pack.md
    - GCP V50 Master Runners Codex.md
  - A V49.0 Master Runners Codex: Flagship Edition.md
  - Agriculture & Environmental MVR Runner.md
  - Archaeology\_History Runner.md
  - Code Runner.md
  - Culinary Cartridge.md
  - Cybersecurity Runner.md
  - Deep Sea Runner.md
  - Education Runner.md
  - Energy\_Power Runner.md
  - Entertainment Cartridge.md
  - Exotics Runner.md
  - Finance & FinTech Runner.md
  - Humanitarian\_Disaster Relief Cartridge.md
  - Industrial & Utilities OT Runner.md
  - Infrastructure Runner.md
  - Legal Cartridge.md
  - Life Sciences Runner.md
  - Physical Runner.md
  - Political Systems Runner.md
  - Public Programs\_Policy Runner.md
  - Spaceflight\_Aerospace Runner.md
  - Sports\_Athletics Cartridge.md
  - Theology Runner.md
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
  - V49.1 Flagship Edition.md
  - V50.md
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
    - **Flagship Full Runs/**
    - A FR Readme.md
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
  - A Notebook Readme.md
  - Adaptive QoS Allocator.ipynb
  - Alloy Perceptual Loss.py
  - Alloyscript.py
  - Audio Processing.md
  - JACCO.ipynb
  - Latch LCH.md
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
- GCP Current Version(V50 Flagship Edition).md
- LICENSE.md
- README.md
- SECURITY.md
- Table Of Contents.md
- mkdocs.yml
- requirements.txt
```
<!-- END REPO TREE --></details>
