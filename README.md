# Genesis Code Protocol (GCP) — V49 Flagship

[![License: MIT](https://img.shields.io/github/license/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](./LICENSE.md)
[![Release](https://img.shields.io/github/v/release/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/releases/latest)
[![Stars](https://img.shields.io/github/stars/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/stargazers)
[![Issues](https://img.shields.io/github/issues/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/issues)
[![PRs](https://img.shields.io/github/issues-pr/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/pulls)
[![Last Commit](https://img.shields.io/github/last-commit/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/commits/main)
[![Code Size](https://img.shields.io/github/languages/code-size/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol)
[![Contributors](https://img.shields.io/github/contributors/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/graphs/contributors)

[![CI: Python](https://img.shields.io/github/actions/workflow/status/lazyxeon/Genesis-Code-Protocol/Python-CI.yml?branch=main&label=CI%3A%20Python&logo=githubactions&style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/Python-CI.yml)
[![Security Scan](https://img.shields.io/github/actions/workflow/status/lazyxeon/Genesis-Code-Protocol/security-scan.yml?branch=main&label=Security%20Scan&logo=githubactions&style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/security-scan.yml)
[![Repo Tree Sync](https://img.shields.io/github/actions/workflow/status/lazyxeon/Genesis-Code-Protocol/update-repo-structure.yml?branch=main&label=Repo%20Tree%20Sync&logo=githubactions&style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/update-repo-structure.yml)
[![Top-Level ToC](https://img.shields.io/github/actions/workflow/status/lazyxeon/Genesis-Code-Protocol/update-toc-file.yml?branch=main&label=Top%20Level%20ToC&logo=githubactions&style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/update-toc-file.yml)
[![Changelog](https://img.shields.io/github/actions/workflow/status/lazyxeon/Genesis-Code-Protocol/generate-changelog.yml?branch=main&label=Changelog&logo=githubactions&style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/generate-changelog.yml)
[![Notebooks](https://img.shields.io/github/actions/workflow/status/lazyxeon/Genesis-Code-Protocol/validate-notebooks.yml?branch=main&label=Notebooks&logo=githubactions&style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/validate-notebooks.yml)
[![Docker Build](https://img.shields.io/github/actions/workflow/status/lazyxeon/Genesis-Code-Protocol/docker-build.yml?branch=main&label=Docker%20Build&logo=githubactions&style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/docker-build.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/lazyxeon/Genesis-Code-Protocol/badge?style=for-the-badge)](https://scorecard.dev/viewer/?uri=github.com/lazyxeon/Genesis-Code-Protocol)

> **GCP V49 Flagship** — an **AI-native, checkpoint-gated invention protocol**. A capable LLM can run it end-to-end to turn a Spark into a **signed, auditable Invention Package** with evidence, provenance, and a verifiable **Exit Wizard** export. Humans may intervene at **Human-Required** gates.

**Quick nav:** [What’s New](#whats-new) • [Quick Start](#quick-start) • [Phase Map](#phase-map--gates) • [Runners](#runners--cartridges-optional) • [Auto Repo Tree](#auto-generated-repository-tree) • [Security](#security--provenance) • [License](#license)

---

## What’s New
- **Phases −1..16** (incl. **XW Exit Wizard**) retained; additive updates only.
- **Runner / Cartridge APIs** stable (additive schema).
- **Rehydration Test** clarified; **Gate_Signals.json** unchanged.

---

# Important Updates
- **Grok4** and **Claude Opus 4** Struggle to run Flagship. **Claude** more so than **Grok**
- **ChatGPT5** Runs Flagship Seamlessly.
- **Gemini 2.5** Runs Flagship Very Well

---

## Quick Start

```text
Initiate GCP V49 for Spark: <your idea>.
Mode: <Full-Run | Auto>; Risk: <R1 | R2 | R3>.
Runner(s): <optional>; Cartridge(s): <optional>.
Objective: <clear success criteria>.
Constraints: <hard/soft>; License: MIT; No PII in logs.
Deliverables: <explicit artifacts>.
```

---

## Universal commands

```text
proceed 1
branch Phase <n>
return C#.#
end & export
switch to Full Run | switch to Auto
set auto_gate_verbosity = full|brief
set auto_gate_preview = on|off
```

---

## Phase Map & Gates
See Charts.md for GitHub-rendered Mermaid flowcharts (linear map + Gate Decision).

---

## Runners & Cartridges (optional)
Attach domain Runners and Cartridges when needed (e.g., Code, Hardware, LifeSci, AgMRV, Space, Deep-Sea, Exotics). They add micro-gates, artifacts, standards, adversarial/metamorphic tests, novelty thresholds, observability, supply-chain/provenance, rehydration, and export rules.
Reference: Master Runners Codex — Flagship Edition.

Attach example:
```text
attach runner code
attach cartridge <name>
```

---

# Artifacts & Ledgers (Flagship set)

### Evidence & Claims: 
Evidence_Index.jsonl, ClaimGraph.json, Source_Reliability.csv

### Reproducibility: 
REPRO_PROTOCOL.md, REPRO_RESULTS.csv, ENV_LOCKFILE.yml

### Provenance:
SBOM/AI-BOM, signatures, attestations

### Gate Signals: 
Gate_Signals.json (allow|deny|needs-human)

### Indexes:
INDEX.md, MANIFEST.json

### Export:
XW/ (ZIP/PDF-A with receipts)

---

# 📚 GCP Wiki

Home: overview, quickstart, phases/gates, modes, checkpoint UX

👉 https://github.com/lazyxeon/Genesis-Code-Protocol/wiki

---
# Auto-Generated Repository Tree
   Full Overview of Repo Structure
<details> <summary>Expand Repo Tree</summary>

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
  - Pull Request Template.md
  - Requirements.md
  - Security.md
  - Setup.py
  - index.md
  - releases.md
  - security\_report.md
- **GCP Runners/**
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
- GCP Current Version(49 Flagship Edition). AI-Native Operational Manual.md
- LICENSE.md
- README.md
- SECURITY.md
- Table Of Contents.md
- mkdocs.yml
- requirements.txt
```
<!-- END REPO TREE -->
</details>

---

## Security & Provenance
OpenSSF Scorecard (action + badge).

SBOM / signing / provenance artifacts included in release bundles.

## Security policy: see SECURITY.md.

## Contributing
Use small PRs, conventional commits, and keep ledgers/indexes current. See Contributing.md and Code of Conduct.

## License
MIT — see LICENSE.md.

## Cite
Add CITATION.cff so others can cite the project correctly.
