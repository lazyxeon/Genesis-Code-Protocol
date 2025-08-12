Genesis Code Protocol (GCP)

License: MIT • Language: Python 3.10+ • Status: Active development (Aug 2025)

The Genesis Code Protocol (GCP)—formerly GRCP—is an AI-native invention framework that lets modern LLMs autonomously discover, design, simulate, validate, and harden novel algorithms, tools, and systems. It combines recursive phases, dual-scientist debate, rigorous gates, statistical benchmarking, safety/privacy governance, and automated post-release monitoring. GCP is model-agnostic (ChatGPT, Claude, Grok, etc.) and tool-friendly (CLI + notebooks + integrations).

This README adds the V46, V46.5, and V47 editions alongside the previously documented v45.6D.


---

✨ Why GCP

From idea → field test: A single protocol takes you from hypothesis to signed, reproducible release artifacts.

Evidence over vibes: Statistical significance, tail metrics, seed sweeps, fairness deltas, SBOM/signing/provenance.

Safety + compliance built-in: DPIA, threat models, attack trees, assurance cases (GSN), license/SPDX.

Operate in the real world: Canary, shadow, drift detection, auto-rollback, evidence TTL & re-verification.

Worth it or stop (V47): “Do-Nothing” and Non-Tech baselines, expected value modeling, problem red-team, and No-Go memoranda.



---

🚀 What’s New (since v45.6D)

V46 — Ironclad Field-Test Edition

Reordered gates to prevent late-stage API churn: Simplicity (8.4) and Optimization (8.5) occur before productization.

Statistical benchmarking mandatory (N≥30, 95% CI, Mann-Whitney on medians, p50/p95/p99).

Perf Pareto across time/memory/energy/cost; cost/energy first-class metrics.

Supply-chain integrity: SBOM, pinned deps, signatures/attestations, reproducible builds.

Field-test kit: runbooks, failure-injection, rollback, acceptance checklists.


V46.5 — Ironclad+ Continuous Assurance Edition

Risk-tiered lanes (R1/R2/R3) to right-size rigor (R3 adds FMEA, STPA, GSN, DPIA, HIL).

Phase 10: Continuous Evaluation — canary → shadow → drift → auto-rollback; evidence TTL + re-verify triggers.

Security depth: SAST/DAST/secret scanning, CVE policy, attack trees.

SemVer + compatibility tests; license/SPDX compliance; operator training and usability checks.


V47 — Worth-It Realism Edition

Phase −1: Problem Discovery & Worth-It Sprint (new gate C−0.5 “Should we even try?”).
Includes Do-Nothing and Non-Tech baselines, Expected-Value modeling with sensitivity, Causal sketch, Problem Red-Team, Premortem, Ethics/Externalities.

Four-Fit at Phase 0: Problem–User, Problem–World, Solution–Problem, Capability–Solution.

Minimal-Intervention Track (choose the smallest thing that works) & No-Go memo as a first-class outcome.

Gate C6.9 Field Realism & Adoption (serviceability, compliance, training, TCO) before scale-out.

Decision forecasts with Brier scoring to calibrate future bets.


> Full gate lineup in “How It Works” below.




---

🧩 Key Features (all editions)

Recursive multi-phase workflow with mandatory gates and artifacts per phase.

Dual-scientist simulation (debate + peer audit) and adversarial testing (metamorphic/property/fuzz).

Autonomous orchestration via CLI and notebooks; supports parallel branches with AMEND/BRANCH governance.

Tooling ecosystem: Torch/SciPy/Transformers, Spark/Delta, profiling suites (perf/VTune/Nsight), fairness evaluators.



---

📦 Installation

git clone https://github.com/lazyxeon/Genesis-Recursive-Code-Protocol-.git
cd Genesis-Recursive-Code-Protocol-
python -m venv .venv && source .venv/bin/activate  # or your preferred env
pip install -r requirements.txt

> Python 3.10+ recommended. Aux packages (e.g., transformers>=4.30, torch>=2.0, scipy>=1.10) power simulations and notebooks.




---

🖥️ Usage Overview

Run a protocol edition from the CLI

# Example: run Ironclad (V46)
python CLI\ Bundle/gcp_cli.py --version 46 --prompt "Invent a real-time anomaly detector for time series"

# Continuous Assurance (V46.5)
python CLI\ Bundle/gcp_cli.py --version 46.5 --prompt "Design, verify, and operate an LLM-based retrieval service"

# Worth-It Realism (V47)
python CLI\ Bundle/gcp_cli.py --version 47 --prompt "Should we even build X? Evaluate + pick smallest effective intervention"

CLI flags (common):

--version {45.6D,46,46.5,47}

--prompt "…", --risk {R1,R2,R3}, --output_dir ./runs/<name>

--notebook to launch the matching example notebook.


Notebook runs

Open Notebooks/ and start with:

GCP_V46_Quickstart.ipynb

GCP_V46_5_CE.ipynb (Phase 10 demos)

GCP_V47_WorthIt_Sprint.ipynb (Phase −1, EV modeling, red-team flows)



---

🔧 CLI Tooling

gcp_cli.py — main orchestrator

full_run.py — executes a complete invention cycle

phase*.py — phase-focused utilities (e.g., benchmarking, safety pack)

audit_utils.py, prompt_utils.py — evidence capture, debate prompts, red-team templates


See CLI Bundle/CLI_Readme.md for all switches/output formats.


---

🧠 How It Works (Phases & Gates)

Shared Core (all editions):

1. Init/Intake → define goals, constraints, artifacts.


2. Design/Build → prototypes, harnesses, profilers.


3. Adversarial → metamorphic/property/fuzz/misuse testing.


4. Benchmarks → replication, tails, statistics (C7, C7.Sigma).


5. Simplicity/Optimization → C8.4 then C8.5 (before productization).


6. Productize → APIs/CLIs/configs/telemetry; surface freeze + compatibility.


7. Release → signed checkpoint with SBOM, runbooks, field-test kit.


8. Operate → CE loop (canary/shadow/drift/rollback), evidence TTL, re-verify.



Edition-specific gates:

V46

C8.4 Simplicity (KISS/YAGNI, dep trim, API audit)

C8.5 Optimization (stat-sig perf/cost/energy; Perf Pareto)

C9 Release (SBOM/signing/provenance; field-test kit)


V46.5

Risk tiering (R1/R2/R3) with escalating evidence

Phase 10 Continuous Evaluation: canary → shadow → drift → auto-rollback

Security depth (SAST/DAST/secrets/CVE gates), SemVer + compat tests, SPDX


V47

Phase −1 Problem Discovery & Worth-It Sprint → Gate C−0.5 “Should we even try?”

Do-Nothing & Non-Tech baselines, EV modeling, causal sketch, Problem Red-Team, Premortem, Ethics.


Phase 0 adds Four-Fit and falsification criteria.

Phase 2 adds Minimal-Intervention Track (pivot if it ties/beats EV).

Gate C6.9 Field Realism & Adoption (serviceability, compliance, training, TCO).

Forecasts + Brier scoring for decision calibration.



> All editions enforce AMEND/BRANCH rules, dual-signing for threshold reductions, and append-only Run Ledger events.




---

🧮 Risk-Tiered Lanes (V46.5+)

R1 (low risk): N≥15 reps; seed sweep ≥5; integrity lite.

R2 (moderate): N≥30; seeds ≥10; full integrity.

R3 (regulated/safety-critical): N≥50; seeds ≥20; FMEA, STPA, Assurance Case (GSN), DPIA, attack trees, HIL.



---

🛡️ Safety, Privacy, Security & Compliance

Safety: misuse tests; for R3 → FMEA, STPA, Assurance Case (GSN).

Privacy: DPIA where applicable; retention/erasure; consent tracing; re-identification checks (k/l/t when relevant).

Security: SBOM, signatures/attestations, repro builds; SAST/DAST/secret scans; CVE policy with dual-signed exceptions.

Licensing: SPDX scan; block non-commercial/incompatible copyleft in prod; attribution bundle.



---

📊 Example End-to-End (V47 + Spark): EV Fast-Charging PRR

Problem: Long waits and failed sessions at public DC fast chargers.

Phase −1 proved value vs Do-Nothing and Non-Tech and passed C−0.5; CA’s real-time data mandate enables a clean pilot.

Solution: Predict → Route → (Soft) Reserve with Spark Structured Streaming + Delta:

Ingest OCPP/network feeds + AFDC metadata + traffic/weather/events.

Predict per-site wait + failure risk; advisory routing first; soft holds with bounded overbooking.

Canaries: prediction error, feed freshness, reservation uptake; auto-rollback to advisory-only.

Fairness: slice deltas; constraints prevent starving rural/low-income regions.


Gates: C2 (powered diff-in-diff A/B), C3 (labeling state machine), C7/C7.Sigma (stats), C6.9 (adoption/serviceability/compliance/TCO), C9 (release), C10 (CE on).


> See Notebooks/EV_PRR_V47_Spark.ipynb (provided in this repo’s notebooks) for a runnable skeleton.




---

📁 Repository Structure

Genesis-Recursive-Code-Protocol-/
├─ CLI Bundle/
│  ├─ gcp_cli.py, full_run.py, phase*.py, audit_utils.py, prompt_utils.py
│  └─ CLI_Readme.md
├─ Documents/
│  ├─ Requirements.md, Contributing.md, LICENSE.md, README.md (this file)
│  ├─ Critical Analyses/ (V45.6D+ audits)
│  └─ Safety-Privacy/ (DPIA templates, GSN examples, FMEA/STPA guides)
├─ GRCP most recent variants/
│  ├─ V09.md … V45.6D.md
│  ├─ V46.md, V46.5.md, V47.md     ← **NEW** editions
│  └─ Changelog.md
├─ Notebooks/
│  ├─ GCP_V46_Quickstart.ipynb
│  ├─ GCP_V46_5_CE.ipynb
│  ├─ GCP_V47_WorthIt_Sprint.ipynb
│  └─ EV_PRR_V47_Spark.ipynb
└─ Examples/
   ├─ AlloyScript specs & demos
   └─ End-to-end invention runs (QoS allocators, retrieval, etc.)


---

🧭 Version Matrix (at a glance)

Edition	Purpose Focus	New Gates/Phases	Security/Compliance	Operations

v45.6D	Agentic multimodal, enterprise scaffolding	—	SBOM/signing introd.	Runbooks, field kits
V46	Field-test hardening	C8.4 before C8; C8.5 before C8; tighter C7	Repro builds, attestations	Perf Pareto, cost/energy
V46.5	Continuous assurance	Phase 10 CE; risk tiering	SAST/DAST/secrets, SPDX, SemVer/compat	Canary/shadow/drift/rollback
V47	Worth-it problem selection	Phase −1 + Gate C−0.5; C6.9; Minimal-Intervention	DPIA formalization; No-Go as outcome	Decision forecasting + Brier



---

🧪 Quickstart Prompts

V46:
“Run GCP V46 to design a real-time anomaly detector and package a field-test kit with perf/cost/energy Pareto.”

V46.5:
“Run GCP V46.5 for a retrieval pipeline with Phase 10 CE: configure canary, shadow, drift, and auto-rollback.”

V47:
“Run GCP V47 to determine if we should build a multi-agent scheduler at all; compare Do-Nothing/Non-Tech, then pick the smallest effective intervention.”



---

🤝 Contributing

1. Fork & branch (feat/<topic>).


2. Follow Python best practices (black/ruff/pytest).


3. For protocol changes, open a proposal issue; include gate impacts and artifact diffs.


4. PRs must pass CI (tests + SAST/DAST/secret scans for code assets) and include updated docs/notebooks if relevant.



See Contributing.md for full guidelines.


---

📝 License & Disclaimer

MIT License — see LICENSE.
GCP is a research-grade protocol. Results depend on model capability, tools, and data access. Follow all applicable laws and ethical guidelines. Safety/privacy/compliance packs are provided; adapt them to your domain and jurisdiction.


---

Changelog (highlights)

V47 (Aug 2025): Worth-It Realism Edition (Phase −1, C−0.5, Minimal-Intervention, C6.9, forecasts/Brier).

V46.5: Continuous Assurance Edition (risk-tiering, Phase 10 CE, security depth, SPDX, SemVer/compat).

V46: Ironclad Field-Test Edition (reordered gates, stat-rigor, Perf-Pareto, reproducible builds, field-test kits).

v45.6D: Agentic multimodal expansion, CLI bundle, enterprise docs and notebooks.



