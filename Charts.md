# Charts & Graphs (V49, GitHub-safe)

This page visualizes the V49 flow, gates, and runner-seeded templates.  
If a diagram ever fails to render, confirm the fence is exactly ```mermaid on its own line, with no indentation. Also keep labels ASCII-only. :contentReference[oaicite:2]{index=2}

## Phase Map (V49)

```mermaid
flowchart TB
  %% Use ASCII-only labels; no unicode arrows/dashes
  A["Pre-Execution - TRIZ ARIZ -0.8"] --> B["Pre-Execution - C-K Drift -0.5A"]
  B --> C["Pre-Execution - Worth-It Sprint -1 -> C-0.5"]

  C --> D0["0 Opportunity and Mode / Runner Handshake -> C0.1"]
  D0 --> D1["1 Context and Precedents -> C1.1"]
  D1 --> D2["2 Influence Harvesting -> C2.1"]
  D2 --> D25["2.5 Futures and Morph Space -> C2.5"]
  D25 --> D3["3 Constraints and Envelope -> C3.1"]
  D3 --> D4["4 Hypotheses and Branch Tree -> C4.1"]
  D4 --> D4A["4.A Red-Team Attack -> C4.A"]
  D4A --> D5["5 Conceptual Modeling and Architecture -> C5.1"]
  D5 --> D6["6 Simulation and Functional Modeling -> C6.1"]
  D6 --> D65["6.5 Multi-Agent War Game -> C6.5"]
  D65 --> D7["7 Iterative Refinement -> C7.1"]
  D7 --> D9["9 Validation and Benchmarking -> C7 and C7.Sigma and C7.Repro"]
  D9 --> D10["10 Simplicity C8.4 then Optimization C8.5"]
  D10 --> D11["11 Productization plus 11.3 IP and Disclosure -> C6.9"]
  D11 --> D12["12 Documentation and Handoff -> C12.1"]
  D12 --> D135["13.5 Devastation Protocol -> C13.5"]
  D135 --> D13["13 Deployment Readiness and Safety Case -> C9"]
  D13 --> D14["14 Continuous Evaluation -> C14.1"]
  D14 --> D145["14.5 Continuous Adversary Shadowing -> C14.5"]
  D145 --> D15["15 Archival, Export, Postmortem -> C15.1"]
Universal Gate Decision Card (Auto Mode UX)
mermaid
Copy
Edit
flowchart TB
  S["Auto Mode enabled"] --> A["Print Gate Decision Card"]
  A --> B{"User override?"}
  B -- "Yes" --> C["Execute user choice and log to DECISION_LEDGER"]
  B -- "No"  --> D["Execute AI recommendation and log to DECISION_LEDGER"]
  C --> E["Advance to next checkpoint"]
  D --> E
Runner System and Alias Examples
mermaid
Copy
Edit
flowchart TB
  R["Runner System (optional)"]
  R --> RC["Code"]
  R --> RP["Physical"]
  R --> RT["Theory"]
  R --> ROT["OT"]
  R --> RM["Mobility"]
  R --> RL["LifeSci"]
  R --> RA["AgMRV"]
  R --> RF["FinTech"]

  subgraph Examples
    X1["Alias: medical-ai => [Code, LifeSci]"]
    X2["Alias: industrial-robotics => [OT, Mobility]"]
  end

  RC -.-> X1
  RL -.-> X1
  ROT -.-> X2
  RM -.-> X2
Evidence TTL (Continuous Evaluation cadence)
Risk Tier	Default TTL	Notes
R1	180 days	Evidence refresh plan tracked in 15_ce/PLAN.md
R2	90 days	CE on for critical artifacts
R3	30–60 days	Highest rigor; security and safety prioritized
