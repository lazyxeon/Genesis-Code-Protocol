# Genesis Code Protocol (GCP)

<!-- BADGES: core repo -->
[![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen)](./Documents/LICENSE.md)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
[![Stars](https://img.shields.io/github/stars/lazyxeon/Genesis-Code-Protocol?style=flat)](https://github.com/lazyxeon/Genesis-Code-Protocol/stargazers)
[![Forks](https://img.shields.io/github/forks/lazyxeon/Genesis-Code-Protocol?style=flat)](https://github.com/lazyxeon/Genesis-Code-Protocol/network/members)
[![Issues](https://img.shields.io/github/issues/lazyxeon/Genesis-Code-Protocol)](https://github.com/lazyxeon/Genesis-Code-Protocol/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/lazyxeon/Genesis-Code-Protocol)](https://github.com/lazyxeon/Genesis-Code-Protocol/pulls)
[![Last Commit](https://img.shields.io/github/last-commit/lazyxeon/Genesis-Code-Protocol)](https://github.com/lazyxeon/Genesis-Code-Protocol/commits/main)
[![Code Size](https://img.shields.io/github/languages/code-size/lazyxeon/Genesis-Code-Protocol)](https://github.com/lazyxeon/Genesis-Code-Protocol)
[![Contributors](https://img.shields.io/github/contributors/lazyxeon/Genesis-Code-Protocol)](https://github.com/lazyxeon/Genesis-Code-Protocol/graphs/contributors)

<!-- BADGES: automation / CI (links go to the workflow runs) -->
[![Python CI](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/Python-CI.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/Python-CI.yml)
[![Security Scan](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/security-scan.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/security-scan.yml)
[![Repo Tree Sync](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/update-repo-structure.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/update-repo-structure.yml)
[![Top-Level ToC](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/update-toc-file.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/update-toc-file.yml)
[![Changelog](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/generate-changelog.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/generate-changelog.yml)
[![Notebooks](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/validate-notebooks.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/validate-notebooks.yml)
[![Docker Build](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/docker-build.yml/badge.svg?branch=main)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/docker-build.yml)

<!-- BADGES: quality/style (optional; leave even if not fully wired—links go to tools) -->
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Type Checking: mypy](https://img.shields.io/badge/type%20checking-mypy-2A6DB2)](https://mypy.readthedocs.io/)
[![Tests: pytest](https://img.shields.io/badge/tests-pytest-0A9EDC)](https://docs.pytest.org/)



> **Formerly:** GRCP (Genesis Recursive Code Protocol)  
> **Status:** Active • **License:** MIT • **Language:** Python 3.10+

The **Genesis Code Protocol (GCP)** is an AI-native, recursively structured invention framework that enables modern LLMs to **discover, design, simulate, validate, and operate** novel algorithms, tools, and systems. It combines multi-phase progression, dual-scientist debate, rigorous gates with statistical evidence, safety/privacy/security governance, and post-release **continuous assurance**.

GCP is **LLM-agnostic** (ChatGPT, Claude, Grok, etc.) and integrates with common tooling (CLI, notebooks, Spark/Delta, Torch/SciPy/Transformers).

---

## Table of Contents

- [Why GCP](#why-gcp)
- [What’s New (V46, V46.5, V47)](#whats-new-v46-v465-v47)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
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
- **Risk tiering (R1/R2/R3)** (R3 adds FMEA, STPA, GSN, DPIA, HIL).  
- **Phase 10: Continuous Evaluation:** canary → shadow → drift → auto-rollback; evidence TTL + re-verify.  
- **Security depth:** SAST/DAST/secret scans, CVE gates; **SemVer + compat tests**; **SPDX** license compliance.

### V47 — *Worth-It Realism Edition*
- **Phase −1:** *Problem Discovery & Worth-It Sprint* → **Gate C−0.5** “Should we even try?”  
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
<details>
```bash
git clone https://github.com/lazyxeon/Genesis-Code-Protocol.git
cd Genesis-Code-Protocol
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
````</details>

---

## Usage
<details>
CLI
 
```bash
# Ironclad (V46)
python "CLI Bundle/gcp_cli.py" --version 46 --prompt "Invent a real-time anomaly detector for time series"

# Continuous Assurance (V46.5)
python "CLI Bundle/gcp_cli.py" --version 46.5 --prompt "Design, verify, and operate an LLM retrieval service"

# Worth-It Realism (V47)
python "CLI Bundle/gcp_cli.py" --version 47 --prompt "Should we even build X? Evaluate + pick smallest effective intervention"

``` 


**Common flags:**
`--version {45.6D,46,46.5,47}` • `--prompt "…"` • `--risk {R1,R2,R3}` • `--output_dir ./runs/<name>` • `--notebook`

### Notebooks

Open `Notebooks/` for quickstarts and full runs.</details>

---

## How It Works (Phases & Gates)

**Core (all editions)**

1. Init/Intake → goals, constraints, artifacts
2. Design/Build → prototypes, harnesses, profilers
3. Adversarial → metamorphic/property/fuzz/misuse testing
4. Benchmarks → replication, tails, significance (**C7**, **C7.Sigma**)
5. Simplicity/Optimization → **C8.4** then **C8.5** (*before* productization)
6. Productize → APIs/CLIs/configs/telemetry; surface freeze + compatibility tests
7. Release → **C9** signed checkpoint with SBOM, runbooks, field-test kit
8. Operate → Phase 10 CE (canary/shadow/drift/rollback), evidence TTL, re-verify

**Edition-specific adds:**
• **V46:** re-ordered gates; Perf Pareto; reproducible builds
• **V46.5:** risk tiering; CE loop; security & licensing depth; SemVer + compat
• **V47:** Phase −1 → **C−0.5** worth-it gate; Four-Fit; Minimal-Intervention; **C6.9**; decision forecasts + Brier

---

## Risk-Tiered Lanes (V46.5+)

| Tier   | When                        | Evidence & Rigor                                |
| ------ | --------------------------- | ----------------------------------------------- |
| **R1** | Low risk/impact             | N≥15 reps; seeds ≥5; integrity lite             |
| **R2** | Moderate                    | N≥30; seeds ≥10; full integrity                 |
| **R3** | Regulated / safety-critical | N≥50; seeds ≥20; FMEA / STPA / GSN / DPIA / HIL |

---

## Safety • Privacy • Security • Compliance

* **Safety:** misuse tests; R3 adds FMEA, STPA, Assurance Case (GSN).
* **Privacy:** DPIA (where applicable); retention/erasure; consent tracing; re-id checks.
* **Security:** SBOM, signatures/attestations, reproducible builds; SAST/DAST/secret scans; CVE gates (dual-signed exceptions).
* **Licensing:** SPDX scan; block non-commercial/incompatible copyleft in prod; attribution bundle.

---

## Version Matrix

| Edition    | Focus                                      | New Gates/Phases                                 | Security/Compliance                    | Operations                   |
| ---------- | ------------------------------------------ | ------------------------------------------------ | -------------------------------------- | ---------------------------- |
| **v45.6D** | Agentic multimodal, enterprise scaffolding | —                                                | SBOM/signing introduced                | Runbooks, field kits         |
| **V46**    | Field-test hardening                       | **C8.4 before C8; C8.5 before C8; tighter C7**   | Repro builds, attestations             | Perf Pareto, cost/energy     |
| **V46.5**  | Continuous assurance                       | **Phase 10 CE; risk tiering**                    | SAST/DAST/secrets, SPDX, SemVer/compat | Canary/shadow/drift/rollback |
| **V47**    | Worth-it selection                         | **Phase −1 + C−0.5; C6.9; Minimal-Intervention** | DPIA formalization; No-Go outcome      | Decision forecasts + Brier   |

---

## Example End-to-End (V47 + Spark)

distilled the full V47 run into an end-to-end, runnable example with commands, artifacts, KPIs, and gates.



# End-to-End Example (V47): EV Fast-Charging — Predict → Route → (Soft) Reserve
<details>
**Edition:** GCP **V47 — Worth-It Realism**
**Track:** Spark + Delta Lake • Kafka (ingest) • FastAPI (serve)
**Scope:** California pilot corridors (I-5 / I-80)
**Provenance:** Summarized from the “GCP V47 Known EV issue Full Run” document&#x20;

---

## 1) Problem & Goal (Phase −1: Worth-It)

**Pain:** Public DC fast charging (DCFC) suffers long queues and failed sessions during peaks → time loss, anxiety, lower EV satisfaction/adoption.
**Goal:** Cut **p95 wait** and **failed attempts** by predicting per-site wait/failure risk, then **advising routes** and optionally **holding soft time windows** across nearby sites.

**Baselines considered**

* **Do-Nothing:** “just go to nearest” (status quo)
* **Non-Tech:** marshal queues + signage/alerts
* **Tech (PRR):** Predict → Route → (Soft) Reserve

**Gate C−0.5 — Should we even try?**
Worth-It Score ≈ **0.76** → **PASS** (R2 pilot). Rationale: credible pain; CA data mandates enable real-time substrate; expected value positive even under conservative uptake.&#x20;

---

## 2) System at a Glance

**Ingest → Lakehouse → Models → Serving → CE (Phase 10)**

* **Data**: Station metadata (AFDC), real-time availability (network/OCPP), traffic, weather, events.
* **Spark Structured Streaming** to **Delta Lake**: bronze (raw) → silver (normalized) → gold (features/labels, predictions).
* **Models**: Day-one baseline = **historical quantiles blended with M/M/c queueing prior**; iterative upgrades (GBDT/CatBoost on Spark).
* **Serving**: **FastAPI** `/predict`, `/route`, `/hold` (soft reservations with bounded overbooking).
* **Ops**: Canary metrics + **auto-rollback** to advisory-only; dashboards for error, fairness deltas, utilization.&#x20;

---

## 3) KPIs, Targets, and Gates

* **Primary KPI:** p95 wait (minutes/arrival) — **target ≤ 10 min** at pilot sites during peak windows (90-day avg).
* **Secondary:** failed attempts %, reroute burden, fairness deltas (rural/low-income), prediction error tails.
* **Falsification (V47):** if p95 wait not improved by **≥30%** vs matched baseline corridors in **≤60 days** → **STOP / pivot to Minimal-Intervention**.
* **Risk tier:** **R2** (moderate). **Phase 10** CE on from day one.&#x20;

---

## 4) Data Inputs (pilot)

* **AFDC Station Locator** (IDs, operator, location, ports, max kW, connector mix).
* **Network status / OCPP** (per-port states, faults, price if available).
* **Traffic / Weather / Events** mapped to nearest stations.
* **(Optional)** anonymized app pings for ground-truth waits.&#x20;

---

## 5) Delta Tables (DDL sketch)

```sql
-- Bronze
CREATE TABLE bronze.ocpp_status_raw (
  ingest_ts TIMESTAMP, payload STRING, source STRING, kafka_offset BIGINT
) USING DELTA;

-- Silver
CREATE TABLE silver.port_status (
  obs_ts TIMESTAMP, station_id STRING, port_id STRING, connector_type STRING,
  status STRING, error_code STRING, power_kw DOUBLE, price_cents_kwh DOUBLE, source STRING
) USING DELTA;

-- Gold (features → predictions)
CREATE TABLE gold.site_timeslice_features (
  ts_5m TIMESTAMP, station_id STRING,
  busy_ports INT, total_ports INT, faults INT, last_change_secs INT,
  arrivals_5m INT, departures_5m INT, traffic_speed DOUBLE,
  weather_bucket STRING, event_flag INT, util_15m DOUBLE,
  prior_wait_p50 DOUBLE, prior_wait_p95 DOUBLE, label_wait_minutes DOUBLE
) USING DELTA;

CREATE TABLE gold.predictions (
  ts_5m TIMESTAMP, station_id STRING,
  y_wait_min DOUBLE, y_wait_lo DOUBLE, y_wait_hi DOUBLE,
  fail_prob DOUBLE, model_version STRING
) USING DELTA;
```

> Bronze streams from Kafka; silver normalizes OCPP/vendor JSON; gold builds features/labels and writes predictions.&#x20;

---

## 6) Spark Jobs (skeletons)

**Bronze ingest (OCPP)**

```python
# ocpp_ingest.py
df = (spark.readStream.format("kafka")
      .option("kafka.bootstrap.servers", "<broker>")
      .option("subscribe", "ocpp_status_raw")
      .option("startingOffsets", "latest").load())
bronze = df.selectExpr("timestamp as ingest_ts","CAST(value AS STRING) payload",
                       "CAST(topic AS STRING) source","offset as kafka_offset")
(bronze.writeStream.format("delta")
 .option("checkpointLocation","s3://…/chk/bronze/ocpp")
 .outputMode("append").start("s3://…/delta/bronze/ocpp_status_raw"))
```

**Silver normalize**

```python
# status_unify.py (parse payload → silver.port_status)
# expect fields: stationId, connectorId, status, errorCode, timestamp, powerKW, priceCentsKwh
```

**Gold features & labels**

```python
# features_labels.py (rollups to 5-min windows, joins traffic/weather/events)
# computes busy_ports/total_ports/faults/arrivals/departures/etc. → gold.site_timeslice_features
```

**Predictions**

```python
# predict_baseline.py (quantiles + M/M/c prior → y_wait_min/lo/hi, fail_prob) → gold.predictions
```

All four can run on Spark 3.5+ with Delta 3+.&#x20;

---

## 7) Day-One Baseline (robust & transparent)

* **Quantile table** by station × hour-of-week (p50/p80/p95).
* **Queueing prior (M/M/c)** from current load (arrivals/departures/ports).
* **Blend** (e.g., 70/30) for **y\_wait\_min**, with **y\_wait\_lo/hi** bounds; **fail\_prob** via simple fault features.
* Conservative behavior near saturation to avoid “confidently wrong” spikes.&#x20;

---

## 8) Minimal Serving API (FastAPI)

```python
# app.py (sketch)
@app.get("/predict")  # ?station_id=...
def predict(station_id: str):  # returns y_wait_min/lo/hi + fail_prob + ts
    ...
@app.get("/route")   # advisory routing (v0); soft holds in v1
def route(...): ...
@app.post("/hold")   # soft time-window reservation with bounded overbooking
def hold(...): ...
```

Latency target: **< 2s P95** per query. Soft holds are optional; advisory-only is the **Minimal-Intervention** fallback.&#x20;

---

## 9) A/B Design & Canary Rollback

**Experiment arms (corridor-paired):**

* **Control:** nearest-charger maps
* **Treatment A:** advisory with predicted waits
* **Treatment B:** advisory + soft holds (bounded overbooking)

**Canaries (auto-rollback):**

* Prediction error: **MAE > 5 min** or **p95 error > 12 min** → revert to advisory-only
* Reservation uptake: **< 15%** w/o benefit → disable holds
* Feed freshness: **> 60s** sustained gap → switch to cached/historical baseline&#x20;

---

## 10) Fairness • Privacy • Compliance

* **Fairness:** publish regional improvements; block expansion if any protected slice regresses **> 0.5%**.
* **Privacy:** station-level + aggregates only; no PII.
* **Compliance:** SBOM, SPDX, signatures/attestations at **C9**; abide by CA real-time data & uptime rules.&#x20;

---

## 11) Ops & Costs (pilot order-of-magnitude)

* **Cluster:** 1 driver (8 vCPU/32 GB), 6 workers (16 vCPU/64 GB), autoscale 3–10.
* **Storage:** Delta in object store; 30-day hot, 180-day warm.
* **90-day budget:** target **< \$100k** (compute + storage + APIs).&#x20;

---

## 12) Quickstart (commands)

```bash
# 1) Set Spark/Delta runtime and env (cloud of your choice)
export KAFKA_BOOTSTRAP=<broker>
export DELTA_ROOT=s3://your-bucket/delta
export CHK_ROOT=s3://your-bucket/chk

# 2) Create tables (adjust storage URIs)
spark-sql -f sql/ddl_delta_e2e.sql

# 3) Start streams (bronze → silver → gold)
spark-submit jobs/ocpp_ingest.py
spark-submit jobs/status_unify.py
spark-submit jobs/features_labels.py
spark-submit jobs/predict_baseline.py

# 4) Serve API (FastAPI) reading gold.predictions
uvicorn app:app --host 0.0.0.0 --port 8080
```

---

## 13) Minimal Folder Scaffold (suggested)

```text
Examples/EV_PRR_V47/
├─ sql/
│  └─ ddl_delta_e2e.sql
├─ jobs/
│  ├─ ocpp_ingest.py
│  ├─ status_unify.py
│  ├─ features_labels.py
│  └─ predict_baseline.py
├─ app.py
└─ README.md   ← this file
```

---

## 14) Gates Recap (this example)

* **C−0.5 (Worth-It):** **PASS** (R2 pilot)
* **C0 (Eligibility):** **PASS** (Domain Profile, Four-Fit, assumptions, budgets)
* **C6.9 (Field Realism & Adoption):** Checked pre-scale (serviceability, compliance, TCO, training)
* **C7 / C7.Sigma:** Stats/replication/tails for model promotions
* **C9:** Release with SBOM & signing; **Phase 10** Continuous Evaluation active&#x20;

---

## 15) Next 48 Hours

1. Secure CA network feeds (real-time availability), confirm AFDC API keys.
2. Stand up bronze/silver streams; verify station cross-refs.
3. Ship `/predict` baseline; wire advisory routing in app (feature flag).
4. Launch A/B on two corridors; enable canaries + auto-rollback.
5. Premortem & red-team pass before enabling soft holds.&#x20;

---

> **Note:** This example is intentionally conservative and **Minimal-Intervention** friendly. If predictions don’t deliver measurable benefit fast, the system stays at advisory-only while non-tech ops (signage/alerts) carry near-term relief.&#x20;
</details>



---

## Repository Structure

<details> **Auto-generated:** The section below is kept in sync by a workflow.
> Do not edit between the markers.

<!-- BEGIN REPO TREE -->
```text
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
  - AI ChatGPT Critical Analysis GCP V45.6D.md
  - AI ChatGPT Critical Analysis GCP V46.md
  - AI ChatGPT Critical Analysis V47 Full Run EV issue.md
  - AI Claude Critical Analysis GCP V45.6d.md
  - AI Claude Critical Analysis GCP V46.md
  - AI Claude Critical Analysis V47 full run EV issue.md
  - AI Grok Critical Analysis GCP V45.6D.md
  - AI Grok Critical Analysis GCP V46 .md
  - AI Grok Critical Analysis V47 Full Run EV issue.md
  - Citation.CFF
  - Feature Requests.md
  - Issue Template.md
  - Pull Request Template.md
  - Requirements.md
  - Security.md
  - Setup.py
  - releases.md
  - security\_report.md
- **GRCP most recent variants/**
  - Changelog.md
  - Complete Master List All Revisions Full.md
  - V09.md
  - V11.md
  - V12.md
  - V20.md
  - V22.md
  - V23.md
  - V30.md
  - V33.md
  - V34.md
  - V35.md
  - V36.md
  - V38.md
  - V39.md
  - V40.md
  - V41.md
  - V42.md
  - V43.7.md
  - V43.md
  - V44.1.md
  - V44.7.md
  - V44.8.md
  - V44.9D.md
  - V44.9b.md
  - V45.1.md
  - V45.2.md
  - V45.3.md
  - V45.4A.md
  - V45.5.md
  - V45.6.md
  - V45.md
  - V46.5.md
  - V46.md
  - V47.md
- **Notebooks/**
  - **Full Runs/**
    - Known EV issue Full Run, GCPv47.md
    - Latch Full run.md
    - Quantum Mechanics Full Run.md
    - Solar Energy Full Run.md
  -  A Complete Full runs\_ Full Inventions Master List(no order).md
  - Adaptive QoS Allocator.ipynb
  - Alloy Perceptual Loss.py
  - Alloyscript.py
  - Audio Processing, v45.6.md
  - Example Explanation.md
  - JACCO.ipynb
  - Latch Latent capability Harnesser.md
  - MOSAIC.ipynb
- **Scripts/**
  - generate\_changelog.py
  - generate\_repo\_toc.py
  - update\_repo\_structure.py
- **docker/**
  - .dockerignore
  - Dockerfile
  - requirements.txt
- About.md
- CHANGELOG.md
- Charts.md
- Code of Conduct.md
- Contributing.md
- GCP Current Version(47).md
- LICENSE.md
- README.md
- Table Of Contents.md
```
<!-- END REPO TREE --> </details> 

---

## Contributing

See `Documents/Contributing.md`. Please also read our `CODE_OF_CONDUCT.md`.

---

## Security Policy

Please use GitHub’s **Private vulnerability reporting** (Security → Advisories → “Report a vulnerability”).
We do not accept vulnerability details via email or public issues. See `SECURITY.md` for details.

---

## License & Disclaimer

**MIT** — see `Documents/LICENSE.md`.
GCP is a research-grade protocol. Results depend on model capability, tools, and data access. Follow applicable laws and ethical guidelines. Safety/privacy/compliance packs are provided; adapt to your domain and jurisdiction.

---

## Changelog (highlights)

* **V47:** Worth-It Realism Edition (Phase −1, **C−0.5**, Minimal-Intervention, **C6.9**, forecasts/Brier)
* **V46.5:** Continuous Assurance (risk-tiering, **Phase 10 CE**, security depth, SPDX, SemVer/compat)
* **V46:** Ironclad Field-Test (reordered gates, stat-rigor, Perf-Pareto, reproducible builds)
* **v45.6D:** Agentic multimodal expansion, CLI bundle, enterprise docs & notebooks

```
