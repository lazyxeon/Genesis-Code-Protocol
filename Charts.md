# Charts & Graphs

---

## 1) Phase Map (V49, linear view)

[Pre-Exec: TRIZ/ARIZ -0.8]
|
v
[Pre-Exec: C-K Drift -0.5A]
|
v
[Pre-Exec: Worth-It Sprint -1 => C-0.5]
|
v
[0 Opportunity & Mode / Runner Handshake => C0.1]
|
v
[1 Context & Precedents => C1.1]
|
v
[2 Influence Harvesting => C2.1]
|
v
[2.5 Futures & Morph Space => C2.5]
|
v
[3 Constraints & Envelope => C3.1]
|
v
[4 Hypotheses & Branch Tree => C4.1]
|
v
[4.A Red-Team Attack => C4.A]
|
v
[5 Conceptual Modeling & Architecture => C5.1]
|
v
[6 Simulation & Functional Modeling => C6.1]
|
v
[6.5 Multi-Agent War Game => C6.5]
|
v
[7 Iterative Refinement => C7.1]
|
v
[9 Validation & Benchmarking => C7 / C7.Sigma / C7.Repro]
|
v
[10 Simplicity (C8.4) then Optimization (C8.5)]
|
v
[11 Productization + 11.3 IP & Disclosure => C6.9]
|
v
[12 Documentation & Handoff => C12.1]
|
v
[13.5 Devastation Protocol => C13.5]
|
v
[13 Deployment Readiness & Safety Case => C9]
|
v
[14 Continuous Evaluation => C14.1]
|
v
[14.5 Continuous Adversary Shadowing => C14.5]
|
v
[15 Archival, Export, Postmortem => C15.1]

ruby
Copy
Edit

### Checkpoints quick index

| Code   | Name                                             |
|-------:|--------------------------------------------------|
| C-0.8  | TRIZ/ARIZ pre-execution                          |
| C-0.5A | C-K drift check                                  |
| C-0.5  | Worth-It decision                                |
| C0.1   | Opportunity & Mode / Runner handshake            |
| C1.1   | Context & Precedents                             |
| C2.1   | Influence harvesting                             |
| C2.5   | Futures & Morph space                            |
| C3.1   | Constraints & Envelope                           |
| C4.1   | Hypotheses & Branch tree                         |
| C4.A   | Red-Team attack                                  |
| C5.1   | Conceptual modeling & architecture               |
| C6.1   | Simulation & functional modeling                 |
| C6.5   | Multi-Agent War Game                             |
| C7     | Validation (core)                                |
| C7.Sigma | Statistical sufficiency                        |
| C7.Repro | Reproducibility gate                           |
| C8.4   | Simplicity                                       |
| C8.5   | Optimization                                     |
| C6.9   | Productization packaging                         |
| C12.1  | Documentation & Handoff                          |
| C13.5  | Devastation protocol                             |
| C9     | Deployment readiness & safety case               |
| C14.1  | Continuous Evaluation                            |
| C14.5  | Continuous Adversary Shadowing                   |
| C15.1  | Archival / Export / Postmortem                   |

## Phase Map
![Phase Map](./images/gcp_v49_phase_map.png)

---

## 2) Universal Gate Decision Card (Auto-Mode UX)

[Auto Mode ON]
|
v
[Print Gate Decision Card]
|
v
[User override?] -- yes --> [Execute user choice] --> [Log to DECISION_LEDGER] --> [Next checkpoint]

-- no --> [Execute AI recommendation] --> [Log to DECISION_LEDGER] --> [Next checkpoint]

pgsql
Copy
Edit

**Gate Decision Card (fields)**

| Field            | Meaning                                                                 |
|------------------|-------------------------------------------------------------------------|
| Options          | `Proceed` / `Branch Phase N` / `Return C#.#` / `End & export`           |
| Descriptions     | 1-line plain-English summaries for each option                          |
| AI Recommendation| Model’s pick + short why                                                |
| Confidence       | 0–1 or Low/Med/High                                                     |
| Cost/Time        | Rough order-of-magnitude estimate                                       |
| Risk             | Key downside(s) or blocker(s)                                           |

**Auto-mode knobs** (as protocol commands)

switch to Full Run | switch to Auto
set auto_gate_verbosity = full|brief
set auto_gate_preview = on|off

yaml
Copy
Edit

## Universal Gate Decision Card (Auto Mode UX)
![Gate UX](./images/gcp_v49_gate_ux.png)

---

## 3) Runner System & Alias Map (reference)

Attach only what you need. Aliases are case/space tolerant.

| Runner  | Purpose (short)                                  | Example aliases (samples)                                 |
|---------|--------------------------------------------------|------------------------------------------------------------|
| Code    | SW/ML/Agents/SDK/CLI/API                         | code, dev, ml, ai, agent, sdk, cli, api                    |
| Physical| Hardware/Mechatronics/EE/ME/Embedded             | hardware, mechanical, electrical, embedded\_hw            |
| Theory  | Axioms, conjectures, formal proofs               | theory, math, formal, proof                                |
| OT      | Industrial/Utilities PLC-SCADA-DCS, standards    | industrial, utilities, plc, scada, dcs, 61131, 62443, nerc |
| Mobility| Auto/Aero/Robot ECUs & safety                    | auto, autosar, ecu, do178c, do254, robotics, odd           |
| LifeSci | GxP/CSV/CSA; 21 CFR Part 11; IEC 62304; ISO 14971| pharma, gxp, gamp, 21cfr11, annex11, 62304, 14971          |
| AgMRV   | Agriculture & environmental MRV                  | ag, agriculture, mrv, field, trials, soil, carbon          |
| FinTech | PCI/SOX/AML/KYC/sanctions; model risk SR 11-7    | finance, payments, pci, sox, aml, kyc, sanctions           |

**Alias bundles (examples)**  
- `medical-ai` ⇒ `[Code, LifeSci]`  
- `industrial-robotics` ⇒ `[OT, Mobility]`

## Runner System & Alias Examples
![Runners](./images/gcp_v49_runners.png)

---

## 4) Auto-seeded templates by Runner (selected)

Base (no runner)
└─ 06_evidence/replication/
├─ REPRO_PROTOCOL.md
├─ REPRO_RESULTS.csv
└─ ENV_LOCKFILE.yml

Copy
Edit
Code
├─ 01_code/ARCHITECTURE_DECISIONS/ADR-0001.md
├─ 04_benchmarks/results/TEST_MATRIX.csv
└─ 11_product/api/ERROR_TAXONOMY.md

Copy
Edit
OT
├─ OT/NETWORK_ZONES_CONDUITS.md
└─ OT/SAFETY_SIF_REGISTER.md

Copy
Edit
Mobility
├─ ODD_SPEC.md
└─ STRUCTURAL_COVERAGE_REPORT.md

Copy
Edit
LifeSci
└─ VALIDATION_MASTER_PLAN.md

Copy
Edit
Physical
└─ 06_evidence/stats/CAE_SUMMARY.md

yaml
Copy
Edit

## Auto-seeded Templates by Runner (selected)
![Templates](./images/gcp_v49_templates_tree.png)

---

## 5) Evidence TTL (Continuous Evaluation cadence)

| Risk Tier | Default TTL | Notes                                     |
|-----------|-------------|-------------------------------------------|
| R1        | 180 days    | Refresh plan tracked in `15_ce/PLAN.md`   |
| R2        | 90 days     | CE on for critical artifacts              |
| R3        | 30–60 days  | Highest rigor; safety/security prioritized|

ASCII timeline (illustrative):

R1: |====180d====|====180d====|====180d====|
R2: |==90d==|==90d==|==90d==|==90d==|==90d==|
R3: |=45d=|=45d=|=45d=|=45d=|=45d=|=45d=| (30–60d window; shown mid at 45d)

yaml
Copy
Edit

## Evidence TTL (Continuous Evaluation cadence)
![Evidence TTL](./images/gcp_v49_evidence_ttl.png)

---

## 6) Packaging & Ledgers (snapshot)

| Category     | Examples (not exhaustive)                                                                      |
|--------------|-------------------------------------------------------------------------------------------------|
| Ledgers      | RUN, DECISION, ASSUMPTION, EVIDENCE, BENCHMARK, OPTIMIZATION, RISK\_SAFETY, COMPLIANCE, CONTRADICTION, C\_K, MORPH\_FUTURES, ADVERSARY |
| Naming       | `RunID_Phase.Subphase_Artifact_Short.ext`                                                      |
| Repro (base) | `REPRO_PROTOCOL.md`, `REPRO_RESULTS.csv`, `ENV_LOCKFILE.yml`                                   |
| Export       | Release pack + SBOM/signing + docs    

## Packaging & Ledgers (snapshot)
![Ledgers](./images/gcp_v49_ledgers_table.png)

---
