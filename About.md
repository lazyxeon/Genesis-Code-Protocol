About

Genesis Code Protocol (GCP) is an AI-native, checkpoint-gated invention protocol. Upload the single protocol document to a capable LLM and run a session to produce field-test-ready outputs that a dev team can validate and deploy.

GCP teaches an LLM how to think and build: ideate → simulate → validate → productize → assure. It emphasizes worth-it realism, statistical evidence, supply-chain integrity, and continuous evaluation after release.

Why GCP

Evidence over vibes: expected-value modeling, worth-it scoring, Brier-scored forecasts, medians and tails (p50/p95/p99), and replication across seeds.

Reality first: serviceability, compliance, TCO, and training are considered before scale.

Safety, privacy, security, and licensing are first-class deliverables.

Explicit checkpoints with clear user choices and seamless resume at any step.

What GCP Is (and Is Not)

Is: A single document and prompt library any LLM can execute in chat to produce auditable artifacts, ledgers, and a release package.

Is: A rigorous process with gates that can stop a run early with a justified No-Go when the expected value is not there.

Is not: A library that automatically reaches into your repo or services; it stays within the LLM’s capabilities and your provided tools.

Is not: A substitute for domain expertise, legal review, or real-world validation.

Modes and Checkpoints

GCP supports two execution modes:

Full Run Mode: The model halts at every checkpoint. It prints a brief context recap, lists next moves, and waits for your choice (Proceed, Branch, Return, End & Export).

Auto Mode: The model advances by itself and only stops at critical gates or when a step requires your input. All decisions are logged to a Decision Ledger.

At each checkpoint you can respond with short commands:

proceed 1
branch Phase 7
return C8.4
end & export

Phases and Gates (V47.2)

Phase −1: Worth-It Discovery Sprint → C−0.5 (“Should we even try?”)

Phase 0–4: Opportunity, context, constraints, and hypothesis branching

Phase 5–8: Architecture, simulation, refinement, and system integration

Phase 9: Validation and benchmarking → C7 / C7.Sigma

Phase 10: C8.4 (Simplicity) then C8.5 (Optimization)

Phase 11: Productization and packaging → C6.9 (Field realism & adoption)

Phase 12–13: Documentation, safety case, and signed release → C9

Phase 14–15: Continuous evaluation, archival, and postmortem

Risk-Tiered Rigor

R1: Low risk. N ≥ 15, ≥ 5 seeds, integrity-lite.

R2: Moderate risk. N ≥ 30, ≥ 10 seeds, full integrity, SBOM/signing.

R3: High/regulated. N ≥ 50, ≥ 20 seeds, FMEA/STPA/GSN/DPIA/HIL, CE on by default.

Artifacts and Ledgers

Run, Decision, Assumption, Evidence, Benchmark, Optimization, Risk & Safety, and Compliance ledgers are produced across phases.

File naming uses a short Run ID and phase markers, for example: S42_9_Benchmark_Ledger.md, S42_13_Safety_Case.md, and S42_FinalPackage.zip.

Security, Privacy, and Licensing

SBOM (SPDX or CycloneDX), signatures/attestations, SAST/DAST/secret scans, and CVE gates.

DPIA where applicable, data minimization, retention/erasure, and re-identification checks.

SPDX license identifiers; avoid incompatible copyleft in production; attribution bundles included.

Quickstart (LLM-Only)

Upload the protocol file to your LLM chat and run:

Initiate GCP and Run Spark: <your idea>.
Mode: <Full Run | Auto>.
Risk Tier: <R1 | R2 | R3>.
Objective: <success criteria>.
Constraints: <hard/soft>.
Deliverables: <code/docs/field kit/etc>.


You can switch modes at any time:

switch to auto mode
switch to full run mode

Learn More

README: Repository overview and status

Wiki: Phases, gates, modes, artifacts, and the full methods guide

Docs site (optional): Versioned documentation if enabled with MkDocs

Citation

If you use GCP, please cite the repository and the specific release you adopted. See the root CITATION.cff (also shown via GitHub’s “Cite this repository” button).
