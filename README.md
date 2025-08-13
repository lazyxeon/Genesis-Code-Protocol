# Genesis Code Protocol (GCP)

<!-- Badges -->
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Stars](https://img.shields.io/github/stars/lazyxeon/Genesis-Code-Protocol?style=flat)
![Forks](https://img.shields.io/github/forks/lazyxeon/Genesis-Code-Protocol?style=flat)
![Last Commit](https://img.shields.io/github/last-commit/lazyxeon/Genesis-Code-Protocol)
![CI](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/Python-CI.yml/badge.svg)
![Security Scan](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/security-scan.yml/badge.svg)

> **Formerly:** GRCP (Genesis Recursive Code Protocol)  
> **Status:** Active (Aug 2025) • **License:** MIT • **Language:** Python 3.10+

The **Genesis Code Protocol (GCP)** is an AI-native, recursively structured invention framework that enables modern LLMs to **discover, design, simulate, validate, and operate** novel algorithms, tools, and systems. It blends multi-phase progression, dual-scientist debate, rigorous gates with statistical evidence, safety/privacy/security governance, and post-release **continuous assurance**.

GCP is **LLM-agnostic** (ChatGPT, Claude, Grok, etc.) and integrates with common tooling (CLI, notebooks, Spark/Delta, Torch/SciPy/Transformers).

---

## Table of Contents
- [Why GCP](#why-gcp)
- [What’s New (V46, V46.5, V47)](#whats-new-v46-v465-v47)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
  - [CLI](#cli)
  - [Notebooks](#notebooks)
- [How It Works (Phases & Gates)](#how-it-works-phases--gates)
- [Risk-Tiered Lanes (V46.5+)](#risk-tiered-lanes-v465)
- [Safety • Privacy • Security • Compliance](#safety--privacy--security--compliance)
- [Version Matrix](#version-matrix)
- [Example End-to-End (V47 + Spark)](#example-end-to-end-v47--spark)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)
- [Security Policy](#security-policy)
- [License & Disclaimer](#license--disclaimer)
- [Changelog (highlights)](#changelog-highlights)

---

## Why GCP
- **Idea → field test:** one protocol produces **signed, reproducible** releases with runbooks and field-test kits.  
- **Evidence over vibes:** statistical significance, tail metrics, seed sweeps, fairness deltas, SBOM/signing/provenance.  
- **Operate in reality:** canary, shadow, drift detection, **auto-rollback**, evidence TTL & re-verification.  
- **Worth-it by design (V47):** **Do-Nothing** & **Non-Tech** baselines, expected value modeling, problem red-team, **No-Go** memoranda.

---

## What’s New (V46, V46.5, V47)

### V46 — *Ironclad Field-Test Edition*
- **Gate order:** **Simplicity (8.4)** & **Optimization (8.5)** run *before* productization.  
- **Statistical rigor:** N≥30, 95% CI, Mann-Whitney on medians, p50/p95/p99.  
- **Perf Pareto:** time/memory/energy/cost; cost & energy first-class metrics.  
- **Supply-chain integrity:** SBOM, pinned deps, signatures/attestations, reproducible builds.  
- **Field-test kit:** runbooks, failure-injection, rollback, acceptance checklists.

### V46.5 — *Ironclad+ Continuous Assurance Edition*
- **Risk tiering (R1/R2/R3)** with evidence scaling (R3 adds FMEA, STPA, GSN, DPIA, HIL).  
- **Phase 10: Continuous Evaluation:** canary → shadow → drift → auto-rollback; evidence TTL + re-verify.  
- **Security depth:** SAST/DAST/secret scans, CVE gates; **SemVer + compat tests**; **SPDX** license compliance.  
- **Operator readiness:** usability checks, training drills, dashboards.

### V47 — *Worth-It Realism Edition*
- **Phase −1:** *Problem Discovery & Worth-It Sprint* → **Gate C−0.5** *“Should we even try?”*  
- **Four-Fit at Phase 0:** Problem–User, Problem–World, Solution–Problem, Capability–Solution.  
- **Minimal-Intervention Track:** pick the **smallest effective** intervention; **No-Go** is a valid outcome.  
- **Gate C6.9:** Field realism & adoption (serviceability, compliance, training, TCO).  
- **Decision forecasts + Brier scoring** for calibration.

---

## Key Features
- **Recursive, gated workflow** with required **artifacts** per phase.  
- **Dual-scientist** simulated debate & **peer audit**; **adversarial testing** (metamorphic/property/fuzz/misuse).  
- **Autonomous orchestration** (CLI + notebooks), parallel branches with AMEND/BRANCH governance.  
- **Tooling ecosystem:** Torch/SciPy/Transformers, Spark/Delta, profilers (perf/VTune/Nsight), fairness evaluators.

---

## Installation
```bash
git clone https://github.com/lazyxeon/Genesis-Code-Protocol.git
cd Genesis-Code-Protocol
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
Usage
CLI
bash
Copy
Edit
# Ironclad (V46)
python "CLI Bundle/gcp_cli.py" --version 46 --prompt "Invent a real-time anomaly detector for time series"

# Continuous Assurance (V46.5)
python "CLI Bundle/gcp_cli.py" --version 46.5 --prompt "Design, verify, and operate an LLM retrieval service"

# Worth-It Realism (V47)
python "CLI Bundle/gcp_cli.py" --version 47 --prompt "Should we even build X? Evaluate + pick smallest effective intervention"
Common flags:
--version {45.6D,46,46.5,47} • --prompt "…" • --risk {R1,R2,R3} • --output_dir ./runs/<name> • --notebook

Notebooks
See Notebooks/:

GCP_V46_Quickstart.ipynb

GCP_V46_5_CE.ipynb

GCP_V47_WorthIt_Sprint.ipynb

EV_PRR_V47_Spark.ipynb

How It Works (Phases & Gates)
Core (all editions)

Init/Intake → goals, constraints, artifacts

Design/Build → prototypes, harnesses, profilers

Adversarial → metamorphic/property/fuzz/misuse testing

Benchmarks → replication, tails, significance (C7, C7.Sigma)

Simplicity/Optimization → C8.4 then C8.5 (before productization)

Productize → APIs/CLIs/configs/telemetry; surface freeze + compatibility tests

Release → C9 signed checkpoint with SBOM, runbooks, field-test kit

Operate → Phase 10 CE (canary/shadow/drift/rollback), evidence TTL, re-verify

Edition-specific adds:
• V46: re-ordered gates; Perf Pareto; reproducible builds
• V46.5: risk tiering; CE loop; security & licensing depth; SemVer + compat
• V47: Phase −1 → C−0.5 worth-it gate; Four-Fit; Minimal-Intervention; C6.9; decision forecasts + Brier

Risk-Tiered Lanes (V46.5+)
Tier	When	Evidence & Rigor
R1	Low risk/impact	N≥15 reps; seeds ≥5; integrity lite
R2	Moderate	N≥30; seeds ≥10; full integrity
R3	Regulated / safety-critical	N≥50; seeds ≥20; FMEA / STPA / GSN / DPIA / attack trees / HIL

Safety • Privacy • Security • Compliance
Safety: misuse tests; R3 adds FMEA, STPA, Assurance Case (GSN).

Privacy: DPIA where applicable; retention/erasure; consent tracing; re-id checks when relevant.

Security: SBOM, signatures/attestations, reproducible builds; SAST/DAST/secret scans; CVE gates (dual-signed exceptions).

Licensing: SPDX scan; block non-commercial/incompatible copyleft in prod; attribution bundle.

Version Matrix
Edition	Focus	New Gates/Phases	Security/Compliance	Operations
v45.6D	Agentic multimodal, enterprise scaffolding	—	SBOM/signing introduced	Runbooks, field kits
V46	Field-test hardening	C8.4 before C8; C8.5 before C8; tighter C7	Repro builds, attestations	Perf Pareto, cost/energy
V46.5	Continuous assurance	Phase 10 CE; risk tiering	SAST/DAST/secrets, SPDX, SemVer/compat	Canary/shadow/drift/rollback
V47	Worth-it selection	Phase −1 + C−0.5; C6.9; Minimal-Intervention	DPIA formalization; No-Go outcome	Decision forecasts + Brier

Example End-to-End (V47 + Spark)
Problem: long waits & failed sessions at public DC fast chargers.

Phase −1: proved value vs Do-Nothing & Non-Tech; passed C−0.5 (pilot in California).

Solution: Predict → Route → (Soft) Reserve with Spark Structured Streaming + Delta.

Ingest OCPP/network feeds + AFDC metadata + traffic/weather/events.

Predict per-site wait + failure risk; start advisory routing; optionally enable soft holds.

Canaries: prediction error, feed freshness, reservation uptake → auto-rollback to advisory-only.

Fairness: slice deltas; constraints prevent starving rural/low-income regions.

## Repository Structure (auto-generated)

> **Note:** The tree below is kept in sync automatically by a workflow.  
> Do not edit between the markers.

<!-- BEGIN REPO TREE -->


<!-- END REPO TREE -->


Contributing
See CONTRIBUTING.md. Please also read our Code of Conduct.

Security Policy
Please use GitHub’s Private vulnerability reporting (Security → Advisories → “Report a vulnerability”). We do not accept vulnerability details via email or public issues. See SECURITY.md for details.

License & Disclaimer
MIT — see LICENSE.md.
GCP is a research-grade protocol. Results depend on model capability, tools, and data access. Follow applicable laws and ethical guidelines. Safety/privacy/compliance packs are provided; adapt to your domain and jurisdiction.

Changelog (highlights)
V47 (Aug 2025): Worth-It Realism Edition (Phase −1, C−0.5, Minimal-Intervention, C6.9, forecasts/Brier)

V46.5: Continuous Assurance (risk-tiering, Phase 10 CE, security depth, SPDX, SemVer/compat)

V46: Ironclad Field-Test (reordered gates, stat-rigor, Perf-Pareto, reproducible builds, field-test kits)

v45.6D: Agentic multimodal expansion, CLI bundle, enterprise docs & notebooks

pgsql
Copy
Edit

> The CI badges above use GitHub’s file-based badge URL (`actions/workflows/<file>/badge.svg`), which is the current recommended pattern. :contentReference[oaicite:5]{index=5}
