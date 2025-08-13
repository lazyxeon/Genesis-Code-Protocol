# Genesis Code Protocol (GCP) — V47.2

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

<!-- CI / AUTOMATION BADGES (adjust workflow names to your repo) -->
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

> **Formerly:** GRCP (Genesis Recursive Code Protocol)  
> **Status:** Active • **License:** MIT • **Language:** Python 3.10+  
> **Edition:** **V47.2** (evolutionary enhancement over V47.1; no regressions)

**GCP** is an **AI-native invention protocol** that teaches an LLM **how to think and build**: ideate → simulate → validate → productize → assure. It’s a **single document** you can upload to any capable LLM (GPT-5, Claude, Grok, etc.). The model follows the protocol’s **phases, gates, and artifacts** to deliver a **field-test-ready** invention that a competent team can cross-validate and deploy.

---

## Why GCP

- **Evidence > vibes:** worth-it modeling (EV/WIS), Brier-scored forecasts, p50/p95/p99, real baselines.  
- **Reality-first:** serviceability, compliance, TCO, training — before scale.  
- **Secure supply chain:** SBOM, SPDX licensing, signatures/attestations.  
- **Continuous assurance:** canary → shadow → drift → auto-rollback (Phase 14).  
- **LLM-agnostic:** optimized prompts, artifacts, and checkpoints for conversational execution.

---

## What’s New — **V47.2** (over V47.1)

- **Dual Modes:**  
  - **Full Run Mode (FRM):** stop at *every* checkpoint; summarize, then present **Proceed / Branch / Return / End & Export** options; wait for user choice.  
  - **Auto Mode (AM):** AI selects the most logical branch automatically and **only stops** at **critical** decision gates or when flagged as manual.  
- **Strict Checkpoint UX:** universal banner with **Context Recap**, **Next Moves**, and **copy-paste commands**.  
- **Renumbered Phases for Flow:** logical map from Worth-It Sprint (C−0.5) → Docs/Handoff → Release (C9) → CE (Phase 14).  
- **Graph-Enhanced Reasoning (optional):** cluster/gap/centrality hooks without tool dependencies.  
- **No regressions:** all capabilities from **V47.1** preserved and expanded.

---

## Quick Start (LLM-Only)

1) **Upload:** `GCP V47.2 — AI-Native Operational Manual` to your LLM chat.  
2) **Prompt:**
```

Initiate GCP and Run Spark: <your idea>.
Mode: \<Full Run | Auto>.
Risk Tier: \<R1 | R2 | R3>.
Objective: <your success criteria>.
Constraints: \<hard/soft>.
Deliverables: \<code/docs/field kit/etc>.

```
3) **Follow Checkpoints:** At each ⛔ **CHECKPOINT**, choose:  
- `proceed 1`  •  `branch Phase <n>`  •  `return C#.#`  •  `end & export`  
4) **Export:** The protocol produces a complete artifact set + manifest for handoff.

> **Optional:** Use the included CLI/Notebooks in this repo as accelerators; the **protocol still runs fully in chat**.

---

## Phase Map & Gates

**Phase −1** Worth-It Sprint → **C−0.5** (“Should we even try?”)  
**0** Opportunity Scan & Mode Handshake  
**1** Context & Precedent Map  
**2** Influence Harvesting (Cross-Domain)  
**3** Constraints & Design Envelope  
**4** Hypotheses & Branch Tree  
**5** Conceptual Modeling & Architecture Draft  
**6** Simulation & Functional Modeling  
**7** Iterative Refinement & Convergence  
**8** Integration & System Assembly  
**9** Validation & Benchmarking → **C7 / C7.Sigma**  
**10** Simplicity then Optimization → **C8.4 → C8.5**  
**11** Productization & Packaging → **C6.9** (Field Realism & Adoption)  
**12** Documentation & Handoff Package  
**13** Deployment Readiness & Safety Case → **C9** (Signed Release)  
**14** Continuous Evaluation (canary/shadow/drift/TTL)  
**15** Archival, Export, Postmortem

> Gates are **hard stops** in FRM; **conditional stops** in AM.

---

## Checkpoint UX (Universal)

```

⛔ CHECKPOINT C#.# — <Name>

Context Recap:

* Progress since prior checkpoint
* Key artifacts (short filenames)
* Open assumptions / risks
* Outstanding decisions

Next Moves:

1. Proceed to \<Phase/Subphase> — <what happens next>
2. Branch to \<Phase/Subphase> — <alternate path>
3. Return to Checkpoint \<C#.#> — <why>
4. End run & export — <zip manifest name>

How to respond:

* proceed 1
* branch Phase <n>
* return C#.#
* end & export

\[Mode: Full Run | Auto]
\[Auto Mode Active: AI will choose option <x> unless overridden in next message]

````

---

## Risk-Tiered Lanes (R1–R3)

| Tier | Typical Use | Rigor |
| --- | --- | --- |
| **R1** | Low risk / low impact | N≥15 reps, ≥5 seeds, integrity-lite |
| **R2** | Moderate risk | N≥30, ≥10 seeds, full integrity |
| **R3** | High/regulated | N≥50, ≥20 seeds, FMEA/STPA/GSN/DPIA/HIL, CE on |

---

## Artifacts & Naming

- **Run ID:** `S123` (short alphanumeric)  
- **Files:** `RunID_Phase.Subphase_Artifact_Short.ext`  
  - Examples:  
    - `S123_3.2_Assumptions_Ledger.md`  
    - `S123_9_Benchmark_Ledger.md`  
    - `S123_10_Optimization_Ledger.md`  
- **Ledgers:** Run • Decision • Assumption • Evidence • Benchmark • Optimization • Risk/Safety • Compliance  
- **Final Export:** `RunID_FinalPackage.zip` (manifest listed if zipping isn’t available)

---

## Features (Selected)

- **Worth-It Realism:** Do-Nothing / Non-Tech baselines; EV/WIS; **No-Go** memos are valid outcomes.  
- **Four-Fit at the start:** Problem–User, Problem–World, Solution–Problem, Capability–Solution.  
- **Simplicity before speed:** **C8.4** (prune complexity) precedes **C8.5** (optimize).  
- **Security & Compliance:** SBOM + signatures; SPDX licensing; SAST/DAST/secrets; CVE gates; SemVer + compat tests.  
- **Fairness & Privacy:** slice deltas, re-id checks, DPIA where applicable.  
- **CE Loop:** canary → shadow → drift → TTL & re-verify → auto-rollback.

---

## Installation (Optional Tooling)

```bash
git clone https://github.com/lazyxeon/Genesis-Code-Protocol.git
cd Genesis-Code-Protocol
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
````

> **Note:** The protocol itself runs in chat. The repo’s CLI/Notebooks are accelerators.

---

## Usage

**LLM-Only (recommended)**

```text
Upload: GCP V47.2 — AI-Native Operational Manual.md
Prompt:
Initiate GCP and Run Spark: <your idea>.
Mode: <Full Run | Auto>.
Risk Tier: <R1 | R2 | R3>.
Objective: <success criteria>. Constraints: <hard/soft>.
Deliverables: <code/docs/field kit/etc>.
```

**CLI (optional)**

```bash
# Example: run a scaffolded flow (adjust to fit your env)
python "CLI Bundle/gcp_cli.py" --version 47.2 --prompt "Invent a streaming compression algorithm with field test"
```

---

## Version Matrix

| Edition    | Focus                                      | Key Additions                                                                            |
| ---------- | ------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **v45.6D** | Agentic multimodal, enterprise scaffolding | SBOM/signing intro; enterprise docs                                                      |
| **V46**    | Field-test hardening                       | **C8.4 before C8; C8.5 before C8;** tight C7                                             |
| **V46.5**  | Continuous assurance                       | **Phase 14 CE;** risk tiers; SPDX/SAST/DAST; SemVer/compat                               |
| **V47**    | Worth-It realism                           | **Phase −1 + C−0.5;** Minimal-Intervention; C6.9; forecasts/Brier                        |
| **V47.1**  | Checkpoint-Gate UX                         | Explicit stop/summary/options; deterministic branching                                   |
| **V47.2**  | Dual-mode + renumbered flow                | **FRM/AM** modes; universal checkpoint banners; graph-enhanced reasoning; no regressions |

---

## Safety • Privacy • Security • Compliance

* **Safety:** misuse/adversarial tests; hazards; red-team memos; dual-sign R3 exceptions.
* **Privacy:** data minimization, retention/erasure, DPIA where applicable, re-id checks.
* **Security:** SBOM, signatures/attestations, SAST/DAST/secrets, CVE gates, reproducible build notes.
* **Licensing:** SPDX identifiers; block incompatible copyleft in prod; attribution bundle.
* **Fairness:** slice metrics and guardrails; regressions ≤ 0.5% absolute (R2/R3) unless waivered with justification.

---

## Repository Structure (indicative)

```text
- CLI Bundle/
- Documents/
- GRCP most recent variants/
- Notebooks/
- Scripts/
- docker/
- GCP V47.2 — AI-Native Operational Manual.md
- README.md
- LICENSE.md
- SECURITY.md
- CODE_OF_CONDUCT.md
- CONTRIBUTING.md
```

> Keep this in sync via the included automation workflows.

---

## Contributing

Please see `CONTRIBUTING.md` and our `CODE_OF_CONDUCT.md` (Contributor Covenant). We use Conventional Commits + SemVer and welcome issues/PRs that include tests, docs, and security considerations.

---

## Security Policy

Use **GitHub’s Private Vulnerability Reporting** (Security → “Report a vulnerability”). We don’t accept sensitive vulnerability details via email or public issues. See `SECURITY.md` for triage/embargo timelines and keys.

---

## License & Disclaimer

**MIT** — see `Documents/LICENSE.md`.
GCP is a research-grade protocol. Outcomes depend on model capability, tools, and data access. Follow laws/ethics and your organization’s security & privacy standards.

---

## Changelog (highlights)

* **V47.2:** Dual modes (FRM/AM), strict checkpoint banners, renumbered flow, graph-enhanced reasoning, zero regressions from V47.1.
* **V47.1:** Checkpoint-Gate UX with explicit stop/summary/options.
* **V47.0:** Worth-It Realism (Phase −1, C−0.5, Minimal-Intervention, C6.9, forecasts/Brier).
* **V46.5:** Continuous Assurance (Phase 14 CE), risk tiers, SPDX/SAST/DAST, SemVer/compat.
* **V46:** Field-test hardening, reordered gates, rigorous stats, reproducible builds.

```
