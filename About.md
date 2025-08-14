# About

---

**Genesis Code Protocol (GCP)** is an AI-native, checkpoint-gated invention protocol.  
It guides capable LLMs to produce field-test-ready outputs that a dev team can validate and deploy.  
The protocol teaches an LLM how to **ideate → simulate → validate → productize → assure** with realistic constraints, statistical evidence, and continuous evaluation after release.

## Current Version

**V48** — evolutionary enhancement over V47.2 with **pre-execution reasoning (TRIZ/ARIZ; C-K)**, **Futures & Morph Space**, expanded adversarial rigor (**Red-Team 4.A; War-Game 6.5; Devastation 13.5**), and **Continuous Adversary Shadowing (14.5)**. New ledgers and packaging manifest are included.

## Why GCP

- **Evidence over vibes:** expected value models (EVM), Worth-It Score (WIS), Brier-scored forecasts, tail metrics.
- **Reality first:** serviceability, compliance, TCO, and training are considered before scale.
- **Safety, privacy, security, licensing** are first-class deliverables.
- **Explicit checkpoints** with clear user choices and seamless resume at any step.

## What GCP Is (and Is Not)

- **Is:** A single document + prompts any LLM can follow to produce auditable artifacts and a release pack.
- **Is:** A rigorous process with gates that can stop a run early with a justified **No-Go** when needed.
- **Is not:** A library that reaches into your repos or services; it stays within the LLM’s allowed tools.
- **Is not:** A substitute for domain expertise, legal review, or real-world field validation.

## Modes and Checkpoints

GCP supports two execution modes.

- **Full Run Mode:** The model halts at each checkpoint, shows context, lists options, and waits for your choice.
- **Auto Mode:** The model advances on its own and pauses only at gates that require human input.

At each checkpoint you can respond with short commands:

proceed 1
branch Phase 7
return C8.4
end & export

markdown
Copy
Edit

## Phases and Gates (V48)

**Pre-Execution**

- **Phase −0.8:** Contradiction Resolution (TRIZ/ARIZ) → **C−0.8**
- **Phase −0.5A:** Concept–Knowledge Drift (C-K) → **C−0.5A**
- **Phase −1:** Worth-It Discovery Sprint → **C−0.5**

**Core Execution**

- **0:** Opportunity & Mode → **C0.1**
- **1:** Context & Precedents → **C1.1**
- **2:** Influence Harvesting → **C2.1**
- **2.5:** Futures & Morph Space → **C2.5**
- **3:** Constraints & Envelope → **C3.1**
- **4:** Hypotheses & Branch Tree → **C4.1**
- **4.A:** Red-Team Hypotheses → **C4.A**
- **5:** Conceptual Modeling & Architecture → **C5.1**
- **6:** Simulation & Functional Modeling → **C6.1**
- **6.5:** Multi-Agent War Game → **C6.5**
- **7:** Iterative Refinement → **C7.1**
- **8:** Integration & Assembly → **C8.1**
- **9:** Validation & Benchmarking → **C7 / C7.Sigma**
- **10:** Simplicity **C8.4** → Optimization **C8.5**
- **11:** Productization & Packaging → **C6.9**
- **12:** Documentation & Handoff → **C12.1**
- **13:** Deployment Readiness & Safety Case → **C9** *(requires **C13.5** PASS)*
- **13.5:** Devastation Protocol → **C13.5**
- **14:** Continuous Evaluation → **C14.1**
- **14.5:** Continuous Adversary Shadowing → **C14.5**
- **15:** Archival, Export, Postmortem → **C15.1**

## Risk-Tiered Rigor

- **R1:** Low risk. N ≥ 15, seeds ≥ 5, integrity-lite.
- **R2:** Moderate risk. N ≥ 30, seeds ≥ 10, full integrity, SBOM/signing.
- **R3:** High or regulated. N ≥ 50, seeds ≥ 20, FMEA/STPA/GSN/DPIA/HIL, CE on by default.

## Quickstart (LLM-Only)

Upload the protocol file to your LLM chat and run:

Initiate GCP and Run Spark: <your idea>.
Mode: <Full Run | Auto>.
Risk Tier: <R1 | R2 | R3>.
Objective: <success criteria>.
Constraints: <hard/soft>.
Deliverables: <code/docs/field kit/etc>.

cpp
Copy
Edit

You can switch modes at any time:

switch to auto mode
switch to full run mode

markdown
Copy
Edit

## Learn More

- **README:** repository overview and status
- **Wiki:** phases, gates, modes, artifacts, and methods guide
