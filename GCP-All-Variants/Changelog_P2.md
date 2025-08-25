# Changelog

All notable changes to this project are documented here. Earlier history (v9 → v45.6D) was compiled previously and is summarized below.

> Style: “curated, chronologically ordered list of notable changes per version.”  
> For full context and repo history, see README and Wiki.

---

## [V50] – Flagship AI‑Native Release

### Added
- **Autonomous Spark Generation (I‑1)**: a new brainstorming phase that proposes a spark from a domain interest when none is provided, performing a worth‑it analysis before proceeding【573040816040038†L0-L14】.
- **Unified bootstrap & startup modes**: new parameters `mode`, `startup_mode`, `run_id`, and `workdir` with a strict early execution sequence; improved gate card UX including `auto_gate_preview` and verbosity controls【244666351008357†L55-L58】.
- **Governance & compliance mapping**: built‑in support for NIST AI RMF, ISO/IEC 42001, EU AI Act, FinOps and sustainability frameworks; dedicated DP evaluation and MITRE ATLAS threat modelling runners【244666351008357†L62-L68】.
- **Extended phases & runners**: added phases for Data Rights, Cartridges parsing, Planning, Memory, Research, System Design, Algorithm Verification, Prototyping, Evaluation & Safety, Governance, FinOps/Sustainability, SBOM/ML‑BOM, C2PA, EU AI Act tech docs, Rehydration, Delivery & Export; see the Master Runners Codex for contracts and ordering【573040816040038†L115-L149】.
- **Master Runners Codex & Cartridges Pack**: new supplemental documents defining deterministic runner contracts and modular domain cartridges (v2.0 schema with manifest, vectorisation stack, lexicons, evaluation hooks, tool bundles and governance notes)【573040816040038†L0-L14】【283978148441638†L0-L14】.
- **Observability & provenance**: mandatory OpenTelemetry spans for every model or tool call; expanded artifact model including privacy cards, threat models, SBOM/ML‑BOM, C2PA manifests, DP reports, evidence & claim ledgers; Data rights and privacy budgets enforced for R2+ risk tiers【573040816040038†L60-L68】.

### Changed
- **Backwards compatibility**: All changes are additive; V49 runners and cartridges remain valid and forward‑compatible. Runners are optional enhancers, but Cartridges provide domain‑specific retrieval and evaluation.

### Notes
- V50 emphasises autonomous, chat‑native execution; the LLM must follow the defined phase sequence exactly and consult the Master Runners Codex and Cartridges Pack for detailed schemas and domain packs.

Refs: GCP V50 Manual, Master Runners Codex & Cartridges Pack.

---

## [V49.0] – Protocol First, Runners Optional

### Added
- **Gate Decision Card (Auto Mode)** now **prints fully before acting**: 4 options + short descriptions, AI recommendation, confidence, cost/time, and risk; logged in DECISION_LEDGER. Verbosity commands added.  
- **Runner System** (optional): **Code, Physical, Theory, OT, Mobility, LifeSci, AgMRV, FinTech**. Attaching seeds domain files and micro-gates; `attach/detach/show` runner commands.
- **Alias Resolver**: case/space-insensitive synonyms; combo aliases like `industrial-robotics` → `[OT, Mobility]`, `medical-ai` → `[Code, LifeSci]`.
- **C7.Repro micro-gate**: standard repro protocol/results/env-lock files.
- **11.3 IP & Disclosure**: explicit review for IP/export/ethics before packaging.
- **Evidence TTL defaults**: R1=180d, R2=90d, R3=30–60d (defined in `15_ce/PLAN.md`).

### Changed
- Expanded manifest conventions and ledger set; clarified artifact naming and export packaging.

### Notes
- V49 runs perfectly **without** runners; runners are **optional enhancers**.  
  (See Charts.md for visuals and Master Runner templates for file seeds.)

Refs: Protocol V49 docs & Runner Templates. :contentReference[oaicite:23]{index=23} :contentReference[oaicite:24]{index=24}

---

## [V48] – Pre-Execution Reasoning & Adversarial Rigor

### Added
- **Pre-execution**: **−0.8 TRIZ/ARIZ** and **−0.5A C‑K Drift** before **−1 Worth-It**.  
- **Exploration**: **2.5 Futures & Morph Space**.  
- **Adversarial**: **4.A Red-Team**, **6.5 Multi-Agent War Game**, **13.5 Devastation**; **14.5 Adversary Shadowing** post-deploy.
- **Artifacts**: CONTRADICTION_LEDGER, C_K_LEDGER, MORPH_FUTURES_LEDGER, ADVERSARY_LEDGER.
- **Checkpoint UX**: Full Run vs Auto Mode, resumable at every gate.

Refs: V48 About/README. :contentReference[oaicite:25]{index=25} :contentReference[oaicite:26]{index=26}

---

## [V47.2] – Dual-Mode + Renumbered Flow

### Added
- **Full Run** (stop at each gate) and **Auto Mode** (conditional stops).  
- Universal checkpoint banner; graph-enhanced reasoning (optional).  
- Renumbered flow from C−0.5 Worth-It to CE (Phase 14).  
(Repo README historically reflected this version.) :contentReference[oaicite:27]{index=27}

---

## [V47.1] – Checkpoint-Gate UX

- Deterministic branching; explicit stop/summary/options at each gate. :contentReference[oaicite:28]{index=28}

## [V47] – Worth-It Realism

- Phase −1 Worth-It Sprint + C−0.5; Minimal-Intervention principle; C6.9; forecasts/Brier. :contentReference[oaicite:29]{index=29}

## [V46.5] – Continuous Assurance

- Phase 14 CE loop; risk tiers; SPDX/SAST/DAST; SemVer/compat. :contentReference[oaicite:30]{index=30}

## [V46] – Field-Test Hardening

- C8.4 Simplicity before C8.5 Optimization; tightened C7. :contentReference[oaicite:31]{index=31}

---

## [v45.6D and earlier] – Summary

- Agentic multimodal scaffolding; SBOM/signing intro; enterprise docs.  
For the detailed v9 → v45.6D entries, see the prior compiled changelog material. :contentReference[oaicite:32]{index=32}
