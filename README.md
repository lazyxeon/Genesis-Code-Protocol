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

**Quick nav:** [What’s New](#whats-new) • [Quick Start](#quick-start) • [Phase Map](#phase-map--gates) • [Runners](#runners--cartridges-optional) • [Auto ToC](#auto-generated-table-of-contents) • [Auto Repo Tree](#auto-generated-repository-tree) • [Security](#security--provenance) • [License](#license)

---

## What’s New
- **Phases −1..16** (incl. **XW Exit Wizard**) retained; additive updates only.
- **Runner / Cartridge APIs** stable (additive schema).
- **Rehydration Test** clarified; **Gate_Signals.json** unchanged.

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

text
Copy
Edit
proceed 1
branch Phase <n>
return C#.#
end & export
switch to Full Run | switch to Auto
set auto_gate_verbosity = full|brief
set auto_gate_preview = on|off

---

## Phase Map & Gates
See Charts.md for GitHub-rendered Mermaid flowcharts (linear map + Gate Decision).

Runners & Cartridges (optional)
Attach domain Runners and Cartridges when needed (e.g., Code, Hardware, LifeSci, AgMRV, Space, Deep-Sea, Exotics). They add micro-gates, artifacts, standards, adversarial/metamorphic tests, novelty thresholds, observability, supply-chain/provenance, rehydration, and export rules.
Reference: Master Runners Codex — Flagship Edition.

Attach example:
```text
attach runner code
attach cartridge <name>
```

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

# 📚 GCP Wiki

Home: overview, quickstart, phases/gates, modes, checkpoint UX

👉 https://github.com/lazyxeon/Genesis-Code-Protocol/wiki

---
# Auto-Generated Repository Tree
   Full Overview of Repo Structure
<details> <summary>Expand Repo Tree</summary>

<!-- BEGIN REPO TREE -->

<!-- END REPO TREE -->
</details>

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
