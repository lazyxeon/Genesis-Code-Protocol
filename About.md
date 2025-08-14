# About

**Genesis Code Protocol (GCP)** is an AI-native, checkpoint-gated invention protocol.
It guides capable LLMs to produce field-test-ready outputs that a dev team can validate and deploy.
The protocol teaches an LLM how to **ideate → simulate → validate → productize → assure** with realistic
constraints, statistical evidence, and continuous evaluation after release.

## Why GCP

* Evidence over vibes: expected value models, worth-it scoring, Brier-scored forecasts, and tail metrics.
* Reality first: serviceability, compliance, TCO, and training are considered before scale.
* Safety, privacy, security, and licensing are first-class deliverables.
* Explicit checkpoints with clear user choices and seamless resume at any step.

## What GCP Is (and Is Not)

* **Is:** A single document and prompt set any LLM can follow to produce auditable artifacts and a release pack.
* **Is:** A rigorous process with gates that can stop a run early with a justified **No-Go** when needed.
* **Is not:** A library that reaches into your repos or services; it stays within the LLM’s allowed tools.
* **Is not:** A substitute for domain expertise, legal review, or real-world field validation.

## Modes and Checkpoints

GCP supports two execution modes.

* **Full Run Mode:** The model halts at each checkpoint, shows context, lists options, and waits for your choice.
* **Auto Mode:** The model advances on its own and pauses only at gates that require human input.

At each checkpoint you can respond with short commands:

proceed 1
branch Phase 7
return C8.4
end & export

## Phases and Gates (V47.2)

* Phase −1: Worth-It discovery sprint → C−0.5 (“Should we even try?”)
* Phase 0–4: Opportunity, context, constraints, and hypothesis branching
* Phase 5–8: Architecture, simulation, refinement, and system integration
* Phase 9: Validation and benchmarking → C7 / C7.Sigma
* Phase 10: C8.4 (Simplicity) then C8.5 (Optimization)
* Phase 11: Productization and packaging → C6.9 (Field realism and adoption)
* Phase 12–13: Docs, safety case, and signed release → C9
* Phase 14–15: Continuous evaluation, archival, and postmortem

## Risk-Tiered Rigor

* **R1:** Low risk. N ≥ 15, seeds ≥ 5, integrity-lite.
* **R2:** Moderate risk. N ≥ 30, seeds ≥ 10, full integrity, SBOM and signing.
* **R3:** High or regulated. N ≥ 50, seeds ≥ 20, FMEA/STPA/GSN/DPIA/HIL, CE on by default.

## Quickstart (LLM-Only)

Upload the protocol file to your LLM chat and run:

Initiate GCP and Run Spark: your idea.
Mode: Full Run | Auto.
Risk Tier: R1 | R2 | R3.
Objective: success criteria.
Constraints: hard/soft.
Deliverables: code/docs/field kit/etc.

You can switch modes at any time:

switch to auto mode
switch to full run mode

## Learn More

* README: repository overview and status
* Wiki: phases, gates, modes, artifacts, and methods guide
