# Genesis Code Protocol (GCP) — V49 Flagship

[![License: MIT](https://img.shields.io/github/license/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](./LICENSE.md)
[![Release](https://img.shields.io/github/v/release/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/releases/latest)
![Status](https://img.shields.io/badge/status-ACTIVE-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white&style=for-the-badge)
[![Stars](https://img.shields.io/github/stars/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/stargazers)
[![Forks](https://img.shields.io/github/forks/lazyxeon/Genesis-Code-Protocol?style=for-the-badge)](https://github.com/lazyxeon/Genesis-Code-Protocol/network/members)
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

> **GCP V49 Flagship** is an **AI-native, checkpoint-gated invention protocol** that a capable LLM can run end-to-end to turn a *Spark* into a **signed, auditable Invention Package** with evidence, provenance, and a verifiable export. Humans may intervene at “Human-Required” gates; the protocol assumes autonomous execution. See **[About](./About.md)** and **[Charts](./Charts.md)**.  *(Rev: 2025-08-17)*

**Quick nav:** [What’s New](#whats-new) • [Quick Start](#quick-start) • [Phase Map](#phase-map) • [Runners](#runners-optional) • [Repo Structure](#repo-structure) • [Contributing](#contributing) • [License](#license)

---

## What’s New
- **Phases −1..16 preserved**; **Gate_Signals.json** schema stable.  
- **Runner / Cartridge APIs** unchanged; additions are additive-only.  
- **Rehydration Test** + **Exit Wizard (XW)** export path clarified.  :contentReference[oaicite:5]{index=5}

---

## Quick Start
Paste this into chat to start a run (Flagship bootstrap, simplified):

Initiate GCP V49 for Spark: <your idea>.
Mode: <Full-Run | Auto>; Risk: <R1 | R2 | R3>.
Runner: <optional>; Cartridges: <optional>.
Constraints: license=MIT; no PII in logs.
Objective: <clear success criteria>.
Deliverables: <explicit artifacts>.

markdown
Copy
Edit

**Universal commands**
proceed 1
branch Phase <n>
return C#.#
end & export
switch to Full Run | switch to Auto
set auto_gate_verbosity = full|brief
set auto_gate_preview = on|off

yaml
Copy
Edit
(See Flagship sections **0–3, 14** for the full bootstrap, roles, and phases overview.) :contentReference[oaicite:6]{index=6}

---

## Phase Map
See **[Charts.md](./Charts.md)** for the GitHub-rendered Mermaid diagrams (Flowchart only). :contentReference[oaicite:7]{index=7}

---

## Runners (optional)
Attach domain-specific **Runners** when needed (e.g., Code, Hardware, LifeSci, AgMRV, Space, Deep-Sea, Exotics). Runners add micro-gates, artifacts, standards, and role packs; they inherit the Flagship rubric (observability, SBOM/provenance, adversarial/metamorphic tests, novelty scoring, rehydration). :contentReference[oaicite:8]{index=8}

Attach example:
attach runner code

yaml
Copy
Edit
Runner schemas and examples live in the **Master Runners Codex — Flagship Edition**. :contentReference[oaicite:9]{index=9}

---

## Repo Structure
Top-level (repo mode):

agents/ memory/ tools/ novelty/ redteam/ metamorphic/ observability/
Policies/ SLOs/ SBOM/ provenance/ Evidence_Log/ Rehydration_Test/
Audit_Package/ XW/ INDEX.md MANIFEST.json Gate_Signals.json

yaml
Copy
Edit
When file I/O isn’t available, artifacts are emitted inline with `BEGIN ARTIFACT:<path> ... END ARTIFACT`. :contentReference[oaicite:10]{index=10}

---

## Contributing
Use small PRs, conventional commits, and keep ledgers/indexes current. Additions must respect gates and the Flagship rubric. :contentReference[oaicite:11]{index=11}

## License
MIT — see **[LICENSE.md](./LICENSE.md)**.
