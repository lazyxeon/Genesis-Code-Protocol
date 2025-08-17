# Genesis Code Protocol (GCP) — V49

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

> **GCP** is an **AI-native, checkpoint-gated invention protocol**. It guides capable LLMs to produce **auditable, field-test-ready** outputs by operationalizing **ideate → simulate → validate → productize → assure**. Runs in chat; CLI/notebooks/CI are optional accelerators. See **[About](./About.md)**.  
*(Format conforms to GitHub-Flavored Markdown & GitHub README guidance.)*

**Quick nav:** [What’s New](#whats-new--v49) • [Quick Start](#quick-start) • [Runners](#runner-system-optional) • [Phase Map](#phase-map--gates-v49) • [Charts](./Charts.md) • [Contributing](#contributing) • [Security](#security) • [License](#license)

---

## What’s New — V49
- **Auto-Mode Gate Decision Card** prints full options + short descriptions + AI recommendation (configurable verbosity).
- **Runner System** (Code, Physical, Theory, OT, Mobility, LifeSci, AgMRV, FinTech) adds role packs, artifacts, micro-gates.
- **Alias System** for human-friendly runner names.
- **C7.Repro** with `REPRO_PROTOCOL.md`, `REPRO_RESULTS.csv`, `ENV_LOCKFILE.yml`.
- **11.3 IP & Disclosure** added pre-packaging.
- **Evidence TTL defaults** by risk tier (managed in `15_ce/PLAN.md`).

---

## Quick Start
```text
Initiate GCP and Run Spark: <your idea>.
Mode: <Full Run | Auto>.
Risk Tier: <R1 | R2 | R3>.
Objective: <success criteria>.
Constraints: <hard/soft>.
Deliverables: <code/docs/field kit/etc>.
# Optional:
attach runner <Code|Physical|Theory|OT|Mobility|LifeSci|AgMRV|FinTech>
```
---
Universal commands

proceed 1
branch Phase <n>
return C#.#
end & export
# Mode/verbosity
switch to Full Run | switch to Auto
set auto_gate_verbosity = full|brief
set auto_gate_preview = on|off
Phase Map & Gates (V49)
See Charts & Diagrams for the full mermaid diagrams.

Pre-Execution

−0.8 TRIZ/ARIZ → C−0.8

−0.5A C-K Drift → C−0.5A

−1 Worth-It Sprint → C−0.5

Core
0 → C0.1 • 1 → C1.1 • 2 → C2.1 • 2.5 → C2.5 • 3 → C3.1 • 4 → C4.1 • 4.A → C4.A • 5 → C5.1 • 6 → C6.1 • 6.5 → C6.5 • 7 → C7.1 • 9 → C7 / C7.Sigma / C7.Repro • 10 → C8.4 → C8.5 • 11 (+11.3) → C6.9 • 12 → C12.1 • 13.5 → C13.5 • 13 → C9 • 14 → C14.1 • 14.5 → C14.5 • 15 → C15.1

Risk-Tiered Lanes
Tier	Typical use	Rigor
R1	Low risk	N≥15; seeds≥5; integrity-lite
R2	Moderate	N≥30; seeds≥10; full integrity; SBOM/signing
R3	High/regulated	N≥50; seeds≥20; FMEA/STPA/GSN/DPIA/HIL; CE default

Runner System (Optional)
Attach only what you need. Aliases are case/space tolerant.

Code (code, dev, ml, ai, agent, sdk, cli, api)

Physical (hardware, mechanical, electrical, embedded_hw)

Theory (theory, math, formal, proof)

OT (industrial, utilities, plc, scada, dcs, 61131, 62443, nerc)

Mobility (auto, aero, robot, autosar, do-178c/254)

LifeSci (vmp, urs, fs, csv)

AgMRV (agriculture, mrv)

FinTech (fintech, trading, risk)

Repo Structure (top-level)
<details>

├─ About.md
├─ Charts.md
├─ README.md
├─ CHANGELOG.md
├─ SECURITY.md
├─ Table Of Contents.md
├─ GCP-All-Variants/
├─ GCP Runners/
├─ Notebooks/
├─ Scripts/
├─ docker/
└─ .github/workflows/
</details>

Contributing
See Contributing. Use conventional commits and keep ledgers updated.

Security
See Security Policy to report vulnerabilities.

License
MIT — see LICENSE.md.
