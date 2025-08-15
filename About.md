# About

**Genesis Code Protocol (GCP)** is an **AI-native, checkpoint-gated invention protocol** that guides capable LLMs to produce **auditable, field-test-ready outputs** a dev or research team can validate and deploy. It operationalizes: **ideate → simulate → validate → productize → assure**, with realistic constraints, statistics, and post-release evaluation. :contentReference[oaicite:5]{index=5}

## Why GCP

- **Evidence over vibes**: Worth-It models (EVM), Worth-It Score (WIS), Brier-scored forecasts, tail metrics.  
- **Reality first**: serviceability, compliance, TCO, and training considered **before** scale.  
- **Safety, privacy, security, licensing**: first-class deliverables with SBOM/signing & provenance.  
- **Explicit checkpoints**: clear user options; resumable runs with deterministic gates. :contentReference[oaicite:6]{index=6}

## What GCP Is / Is Not

- **Is:** A single protocol + prompts any major LLM can follow to produce **auditable artifacts** and a **release pack**.  
- **Is:** A rigorous, gate-driven process that can justifiably **stop early** with a **No-Go**.  
- **Is not:** A crawler into your repos/services; stays within the LLM’s allowed tools.  
- **Is not:** A substitute for domain expertise, legal review, or real-world field validation. :contentReference[oaicite:7]{index=7}

## Current Version

**V49** (successor to V48). Key additions: full **Gate Decision Card** in Auto Mode, **Runner System** (optional), **Alias Resolver**, **C7.Repro**, **11.3 IP & Disclosure**, **Evidence TTL defaults**. :contentReference[oaicite:8]{index=8}

## Modes & Checkpoints

- **Full Run Mode**: pause at every checkpoint; summarize context; present options; wait for command.  
- **Auto Mode**: proceeds automatically but **prints the full Gate Decision Card before acting**.  
Universal commands:

proceed 1
branch Phase <n>
return C#.#
end & export

Mode/verbosity
switch to Full Run | switch to Auto
set auto_gate_verbosity = full|brief
set auto_gate_preview = on|off

markdown
Copy
Edit

:contentReference[oaicite:9]{index=9}

## Risk-Tiered Rigor

- **R1**: N≥15, seeds≥5, integrity-lite  
- **R2**: N≥30, seeds≥10, full integrity, SBOM/signing  
- **R3**: N≥50, seeds≥20, FMEA/STPA/GSN/DPIA/HIL, CE on by default :contentReference[oaicite:10]{index=10}

## Phases & Gates (V49)

Pre-Execution: **−0.8 TRIZ/ARIZ**, **−0.5A C-K**, **−1 Worth-It** → C−0.5  
Core: 0..15 with **2.5 Futures/Morph**, **4.A Red-Team**, **6.5 War Game**, **C7.Repro**, **13.5 Devastation**, **14.5 Adversary Shadowing**. :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12}

## Runners (Optional Enhancers) + Alias Map

Attach only when helpful. Aliases are human-friendly and case/space tolerant.  
**Code, Physical, Theory, OT, Mobility, LifeSci, AgMRV, FinTech** with auto-seeded templates (e.g., ADRs, test matrices, AUTOSAR specs, VMP/URS/FS, PLC contracts, safety ledgers). Examples: `medical-ai` → `[Code, LifeSci]`; `industrial-robotics` → `[OT, Mobility]`. :contentReference[oaicite:13]{index=13} :contentReference[oaicite:14]{index=14}

## Reproducibility & Evidence TTL

**C7.Repro** adds standardized repro files; **Evidence TTL** defaults: R1=180d, R2=90d, R3=30–60d, managed in `15_ce/PLAN.md`. :contentReference[oaicite:15]{index=15}

## Quickstart (LLM-Only)

Upload the protocol file and run:

Initiate GCP and Run Spark: <your idea>.
Mode: <Full Run | Auto>. Risk Tier: <R1 | R2 | R3>.
Objective: <success>. Constraints: <hard/soft>.
Deliverables: <code/docs/field kit/etc>.
attach runner <...> # optional

pgsql
Copy
Edit

You can switch modes at any time with `switch to auto mode` / `switch to full run mode`. :contentReference[oaicite:16]{index=16}
