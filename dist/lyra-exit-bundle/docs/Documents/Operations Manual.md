# GCP Current Version (50 Flagship Edition) — AI‑Native Operational Manual

**Revision:** 2025‑08‑25

**Design target:** LLM‑native, autonomous invention engine requiring minimal human intervention. This manual supersedes the V49 edition and should be treated as the definitive reference for V50 runs.

## 0) Purpose & Scope

GCP V50 defines a single specification an advanced LLM can follow to turn a spark — an invention goal — into a rigorously tested, benchmarked, policy‑gated invention package with evidence, provenance and a verifiable export. It operates purely in chat (emitting artifacts inline) or in a repository (writing files and running CI). Humans may spectate or intervene, but the protocol assumes autonomous LLM execution.

## 1) Modes of Operation

- **Architect‑led (spark_provided):** You supply a clear spark (e.g., “design a low‑latency scheduler for mobile devices”). The protocol begins at I‑0 initialization, validates the provided spark and proceeds through the phases.
- **Collaborative brainstorm (autonomous):** You supply only a high‑level domain or goal. The **I‑1 Autonomous Spark Generation** phase proposes a spark based on the domain, performs a worth‑it analysis and presents a brief for acceptance.

Operational modes `auto`, `full` and `manual` control gate progression (automatic vs human‑paused).

## 2) Bootstrap Configuration

To start a run, the LLM must set:

- `mode`: auto, full or manual.
- `startup_mode`: spark_provided or autonomous.
- `run_id`: short UUID (e.g., gcp‑a17e).
- `workdir`: `./gcp_run_<run_id>/`.

**Hard rules:** follow phases in order; emit every artifact with the exact filename; run every gate and render the gate card UX each time. Emit OpenTelemetry spans for every model/tool call.

## 3) Core Principles & Rubric

Retain the ten core principles described in `About.md`. In addition, V50 emphasises:

- **Governance & standards mapping:** NIST AI RMF, ISO/IEC 42001, EU AI Act, FinOps and sustainability frameworks.
- **Privacy & DP evaluation:** Dedicated runners enforce NIST SP 800‑226 de‑identification guidelines and HIPAA compliance.
- **Provenance & supply chain:** SPDX 3.0 SBOM, CycloneDX ML‑BOM, SLSA/in‑toto, Sigstore Rekor and C2PA manifests.

All phases must satisfy the flagship rubric: multi‑agent handoffs, tool orchestration plan, memory & retrieval rules, policy gates, deterministic acceptance tests, novelty accounting, adversarial tests, observability, provenance and rehydration plan.

## 4) Interfaces & Roles

- **Runner API:** Deterministic modules with inputs, steps, artifacts, gates and telemetry as defined in the Master Runners Codex.
- **Cartridge API:** Domain modules with embeddings, indexes, lexicons, tools and governance notes.
- **Internal roles:** Planner, Researcher, Engineer, Adversary, Auditor, Operator and Scribe.

## 5) Phases & Runners

V50 phases include:

- **I‑1 Autonomous Spark Generation (optional):** Generate and validate a spark when none is provided.
- **I‑0 Initialization:** Data rights, cartridges parsing, planning and memory setup.
- **C‑0 Ambiguity → Brief** and **C‑1 Creative Discovery**.
- **R‑2 Research**.
- **D‑3 System Design**.
- **D‑4 Algorithm Specification & Verification**.
- **D‑5 Prototyping**.
- **E‑7 Evaluation & Safety** (including DP evaluation and MITRE ATLAS threat modelling).
- **G‑13 Governance**.
- **Delivery & Export:** SBOM/ML‑BOM, C2PA credentials, RO‑Crate packaging, EU AI Act technical documentation, rehydration tests and archival.

Refer to the Master Runners Codex for detailed contracts of each runner.

## 6) Artifact Model & Inline Emission

Artifacts are stored under the run directory (e.g., `agents/`, `memory/`, `tools/`, `novelty/`, `redteam/`, `metamorphic/`, `observability/`, `policies/`, `SLOs/`, `SBOM/`, `provenance/`, `Evidence_Log/`, `Rehydration_Test/`, `Audit_Package/`, `XW/`, `INDEX.md`, `MANIFEST.json`, `Gate_Signals.json`). When file I/O is unavailable, emit artifacts inline using:

```
BEGIN ARTIFACT:<virtual_path>
<content>
END ARTIFACT
```

The Scribe must keep `INDEX.md` and `MANIFEST.json` up to date. Rehydration tests rebuild the environment and re‑run checks; the Exit Wizard packages a signed, transparent export.

## 7) Running the Protocol

Paste the bootstrap instruction into the LLM:

```
SYSTEM — GCP V50 BOOTSTRAP (Flagship Edition)
You are executing GCP V50 autonomously. Follow phases –1..15 (including I‑1), rubrics and gates exactly. Emit every artifact at the specified path. If files aren’t supported, inline artifacts. Never skip a gate. If blocked, output a Gate_Signals entry with status=needs‑human and a minimal unblock plan. Prefer formal proofs, tests and policies over assertions. Keep `INDEX.md` and `MANIFEST.json` current.
RUN CONFIG
Spark: <your spark or blank for autonomous>
Runner: <Auto|Assisted|Research‑Heavy|Code‑First|…>  # optional
Cartridges: <[domain packs] or none>               # optional
Constraints: license=MIT; no PII in logs; max_passes_per_phase=2 unless red‑flagged; evidence ≥2 independent sources per critical claim.
BEGIN EXECUTION AT PHASE –1.
```

---

This manual is intentionally high level; refer to the Master Runners Codex and Cartridges Pack for full schemas and runner details.
