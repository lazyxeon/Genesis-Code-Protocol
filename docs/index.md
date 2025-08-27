# About — GCP V50 Flagship

**What it is.** A single protocol an advanced LLM can follow to produce **auditable, benchmarked, policy‑gated invention packages** with **provenance** and a verifiable **Exit Wizard** export. V50 builds on the V49 Flagship edition with autonomous spark generation, refined governance and compliance mapping, and an expanded library of runners and cartridges.

## Core Principles (LLM‑native)

1. **Policy‑as‑Code gates** (Rego/OPA‑style patterns).
2. **Observability from birth** (traces/metrics/logs).
3. **Evidence over vibes:** Evidence Index & Claim Graph.
4. **Adversarial & metamorphic testing**.
5. **Formal constraints** (SMT/proof assistants).
6. **Novelty vs SOTA** with thresholds.
7. **Supply‑chain & provenance** (SBOM/AI‑BOM, signatures).
8. **Rehydration proof** (rebuild & re‑run).
9. **Modular orchestration** (Runners & Cartridges).
10. **Export with guarantees** (Exit Wizard).

## What GCP Is / Is Not

- **Is:** a deterministic, auditable protocol any major LLM can run to emit release‑grade artifacts.
- **Is:** gate‑driven; can **stop early** at No‑Go points.
- **Is not:** a repo crawler or production deployer.
- **Is not:** a substitute for domain expertise, legal review or field validation.

## Modes & Startup

GCP V50 supports two modes of operation:

- **Architect‑led (spark_provided):** you supply a well‑defined problem spark; the protocol starts at I‑0 initialization and proceeds through the phases.
- **Collaborative brainstorm (autonomous):** you supply only a high‑level domain; the **I‑1 Autonomous Spark Generation** phase proposes a spark based on the domain, performs a worth‑it analysis and presents a brief for acceptance.

Operational modes (`auto`, `full`, `manual`) control gate progression. Universal commands (`proceed`, `branch`, `return`, `end & export`, etc.) remain unchanged from V49.

## Interfaces (stable in V50)

- **Runner API:** deterministic modules with inputs, steps, artifacts, gates and telemetry as defined in the Master Runners Codex.
- **Cartridge API:** domain knowledge modules with embeddings, indexes, lexicons, tools and governance notes.

## Roles (internal council)

Planner • Researcher • Engineer • Adversary • Auditor • Operator • Scribe.

## Risk‑Tiered Rigor

| Tier | Reps/Seeds | Notes |
|---|---|---|
| **R1** | ≥15 / ≥5 | Integrity‑lite |
| **R2** | ≥30 / ≥10 | Full integrity; SBOM/signing |
| **R3** | ≥50 / ≥20 | Includes FMEA/STPA/GSN/DPIA/HIL; CE default |

Reproducibility & Evidence TTL: C7.Repro templates included. TTL: R1 = 180 days, R2 = 90 days, R3 = 30–60 days.

## Artifact Model

Artifacts are stored in run directories or emitted inline. Key folders include:

```text
agents/  memory/  tools/  novelty/  redteam/  metamorphic/  observability/
policies/  SLOs/  SBOM/  provenance/  Evidence_Log/  Rehydration_Test/
Audit_Package/  XW/  INDEX.md  MANIFEST.json  Gate_Signals.json
```

When file I/O is unavailable, emit artifacts inline using:

```text
BEGIN ARTIFACT:

END ARTIFACT
```

Rehydration tests rebuild the environment and re‑run checks; the Exit Wizard packages a signed, transparent export.
