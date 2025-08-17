# About — GCP V49 Flagship

**What it is.** A single spec an advanced LLM can follow to produce **auditable, benchmarked, policy-gated invention packages** with **provenance** and a verifiable **Exit Wizard** export.

## Core Principles (LLM-native)
1) **Policy-as-Code gates** (OPA/Rego-style patterns).  
2) **Observability from birth** (traces/metrics/logs).  
3) **Evidence over vibes** (Evidence Index + Claim Graph).  
4) **Adversarial & metamorphic testing**.  
5) **Formal constraints** where applicable.  
6) **Novelty vs SOTA** with thresholds.  
7) **Supply-chain & provenance** (SBOM/AI-BOM, signatures).  
8) **Rehydration proof** (rebuild + re-run slice).  
9) **Modular orchestration** (Runners & Cartridges).  
10) **Export with guarantees** (Exit Wizard).

## What GCP Is / Is Not
- **Is:** A single, auditable protocol any major LLM can run to emit **release-grade artifacts**.  
- **Is:** Gate-driven; can **stop early** with a **No-Go**.  
- **Is not:** A repo crawler or production deployer.  
- **Is not:** A substitute for expertise, legal review, or field validation.

## Modes & Universal Commands
```text
Full-Run: pause at every gate; present options; wait for command
Auto: proceeds automatically but prints Gate Decision Card first
proceed 1 | branch Phase <n> | return C#.# | end & export
switch to Full Run | switch to Auto
set auto_gate_verbosity = full|brief
set auto_gate_preview = on|off
```

---

## Interfaces (stable in V49)
Runner API: name, biases, policy overrides, timebox.

Cartridge API: domain knowledge, metrics, legal, risks, metamorphic relations, policies.

## Roles (internal council)
Planner • Researcher • Engineer • Adversary • Auditor • Operator • Scribe.

## Risk-Tiered Rigor
Tier	Reps/Seeds	Notes
R1	≥15 / ≥5	Integrity-lite
R2	≥30 / ≥10	Full integrity; SBOM/signing
R3	≥50 / ≥20	FMEA/STPA/GSN/DPIA/HIL; CE default

## Reproducibility & Evidence TTL
C7.Repro templates included.

TTL: R1=180d, R2=90d, R3=30–60d (managed in 15_ce/PLAN.md).

## Artifact Model (repo mode)
```text
agents/ memory/ tools/ novelty/ redteam/ metamorphic/ observability/
Policies/ SLOs/ SBOM/ provenance/ Evidence_Log/ Rehydration_Test/
Audit_Package/ XW/ INDEX.md MANIFEST.json Gate_Signals.json
When file I/O isn’t available, emit artifacts inline:
BEGIN ARTIFACT:<path> ... END ARTIFACT.
```

Rehydration & Exit
A Rehydration Test rebuilds the environment and re-runs checks; the Exit Wizard (XW) packages a signed, transparent export (ZIP or PDF/A) with provenance receipts.
