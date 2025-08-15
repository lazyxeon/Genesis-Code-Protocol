# Charts & Graphs (V49)

This page visualizes the **V49** flow, gates, and runner-seeded templates.

## Phase Map (V49)

```mermaid
flowchart LR
  subgraph Pre-Execution
    A[-0.8 TRIZ/ARIZ] --> B[-0.5A C-K Drift]
    B --> C[-1 Worth-It Sprint]
  end

  subgraph Core Execution
    C --> D0[0 Opportunity & Mode / Runner Handshake]
    D0 --> D1[1 Context & Precedents]
    D1 --> D2[2 Influence Harvesting]
    D2 --> D25[2.5 Futures & Morph Space]
    D25 --> D3[3 Constraints & Envelope]
    D3 --> D4[4 Hypotheses & Branch Tree]
    D4 --> D4A[4.A Red-Team Attack]
    D4A --> D5[5 Conceptual Modeling & Architecture]
    D5 --> D6[6 Simulation & Functional Modeling]
    D6 --> D65[6.5 Multi-Agent War Game]
    D65 --> D7[7 Iterative Refinement]
    D7 --> D9[9 Validation & Benchmarking]
    D9 --> D10[10 Simplicity (C8.4) → Optimization (C8.5)]
    D10 --> D11[11 Productization (+11.3 IP & Disclosure)]
    D11 --> D12[12 Documentation & Handoff]
    D12 --> D135[13.5 Devastation Protocol]
    D135 --> D13[13 Deployment Readiness & Safety Case]
    D13 --> D14[14 Continuous Evaluation]
    D14 --> D145[14.5 Continuous Adversary Shadowing]
    D145 --> D15[15 Archival, Export, Postmortem]
  end
Checkpoints: C−0.8, C−0.5A, C−0.5, C0.1, C1.1, C2.1, C2.5, C3.1, C4.1, C4.A, C5.1, C6.1, C6.5, C7, C7.Sigma, C7.Repro, C8.1, C8.4, C8.5, C6.9, C12.1, C13.5, C9, C14.1, C14.5, C15.1. 
 

Universal Gate Decision Card (UX)
mermaid
Copy
Edit
sequenceDiagram
  participant User
  participant GCP(V49)
  User->>GCP(V49): Mode: Auto
  GCP(V49)-->>User: Print Gate Decision Card (4 options + rationale, rec, confidence, cost/time, risk)
  Note over GCP(V49): auto_gate_preview=on (default)
  GCP(V49)->>GCP(V49): Select recommendation (unless overridden)
  GCP(V49)-->>User: Log decision in DECISION_LEDGER.md
Auto Mode now prints the full card before acting, then proceeds (configurable verbosity). 

Runner Alias Map
mermaid
Copy
Edit
flowchart TB
  R[Runner System] --> Code
  R --> Physical
  R --> Theory
  R --> OT
  R --> Mobility
  R --> LifeSci
  R --> AgMRV
  R --> FinTech

  subgraph Aliases (samples)
    Code -->|"code, dev, ml, ai, agent, sdk, cli, api"| Code
    Physical -->|"hardware, mechanical, electrical, embedded_hw"| Physical
    OT -->|"industrial, utilities, plc, scada, dcs, 61131, 62443, nerc"| OT
    Mobility -->|"auto, autosar, ecu, do178c, do254, robotics, odd"| Mobility
    LifeSci -->|"pharma, gxp, gamp, 21cfr11, annex11, 62304, 14971"| LifeSci
    AgMRV -->|"ag, agriculture, mrv, field, trials, soil, carbon"| AgMRV
    FinTech -->|"finance, payments, pci, sox, aml, kyc, sanctions"| FinTech
  end
Examples: medical-ai ⇒ [Code, LifeSci]; industrial-robotics ⇒ [OT, Mobility]. 

Auto-Seeded Templates by Runner (selected)
mermaid
Copy
Edit
flowchart LR
  Base[Base V49.1 (No Runner)] --> Repro[06_evidence/replication/{REPRO_PROTOCOL.md,REPRO_RESULTS.csv,ENV_LOCKFILE.yml}]
  Code -->|on attach| ADR[01_code/ARCHITECTURE_DECISIONS/ADR-0001.md]
  Code --> Errors[11_product/api/ERROR_TAXONOMY.md]
  Code --> Tests[04_benchmarks/results/TEST_MATRIX.csv]
  OT --> Zones[OT/NETWORK_ZONES_CONDUITS.md]
  OT --> Safety[OT/SAFETY_SIF_REGISTER.md]
  Mobility --> ODD[ODD_SPEC.md]
  Mobility --> Coverage[STRUCTURAL_COVERAGE_REPORT.md]
  LifeSci --> VMP[VALIDATION_MASTER_PLAN.md]
  Physical --> CAE[06_evidence/stats/CAE_SUMMARY.md]
Full per-runner file lists are in the Master Runner templates. 

Evidence TTL (CE Refresh Cadence)
mermaid
Copy
Edit
gantt
  title Evidence TTL by Risk Tier
  dateFormat  YYYY-MM-DD
  section R1
  Re-verify (every 180d) :a1, 2025-01-01, 180d
  section R2
  Re-verify (every 90d)  :a2, 2025-01-01, 90d
  section R3
  Re-verify (30–60d)     :a3, 2025-01-01, 45d
Managed in 15_ce/PLAN.md. 
