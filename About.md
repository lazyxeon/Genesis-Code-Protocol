---

## `About.md`

```markdown
# About

**Genesis Code Protocol (GCP)** is an **AI-native, checkpoint-gated invention protocol** that guides capable LLMs to produce **auditable, field-test-ready outputs**. It operationalizes **ideate → simulate → validate → productize → assure** and is designed to render cleanly under GitHub-Flavored Markdown. :contentReference[oaicite:2]{index=2}

## Why GCP
- **Evidence over vibes**: Worth-It models (EVM), Worth-It Score (WIS), Brier-scored forecasts, tail metrics.
- **Reality first**: serviceability, compliance, TCO considered early.
- **Safety, privacy, security, licensing**: first-class deliverables with SBOM/signing & provenance.
- **Explicit checkpoints**: clear user options; resumable runs with deterministic gates.

## What GCP Is / Is Not
- **Is:** a single protocol any major LLM can follow to produce **auditable artifacts** and a **release pack**.  
- **Is:** a rigorous, gate-driven process that can justifiably **stop early** with a **No-Go**.  
- **Is not:** a crawler into your repos/services; it stays within allowed tools.  
- **Is not:** a substitute for domain expertise, legal review, or field validation.

## Current Version
**V49** (successor to V48). Additions: **Auto-Mode Gate Decision Card**, **Runner System**, **Alias Resolver**, **C7.Repro**, **11.3 IP & Disclosure**, **Evidence TTL defaults**.

## Modes & Checkpoints

**Modes**
```text
Full Run Mode  – pause at every checkpoint; present options; wait for command
Auto Mode      – proceeds automatically but prints the Gate Decision Card first
Universal commands

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
Risk-Tiered Rigor
Tier	Reps / Seeds	Notes
R1	N≥15 / ≥5	Integrity-lite
R2	N≥30 / ≥10	Full integrity; SBOM/signing
R3	N≥50 / ≥20	FMEA/STPA/GSN/DPIA/HIL; CE default

Reproducibility & Evidence TTL
C7.Repro adds standardized repro files.

Evidence TTL defaults: R1=180d, R2=90d, R3=30–60d (managed in 15_ce/PLAN.md).

Quickstart (LLM-only)
text
Copy
Edit
Initiate GCP and Run Spark: <your idea>.
Mode: <Full Run | Auto>. Risk Tier: <R1 | R2 | R3>.
Objective: <success>. Constraints: <hard/soft>.
Deliverables: <code/docs/field kit/etc>.
attach runner <...>  # optional
Related
Charts & Diagrams: see Charts.md — rendered with Mermaid on GitHub. 
GitHub Docs

README: project overview, badges, repo tree, and links.

Shields: badges use the for-the-badge style. 
shields.io
