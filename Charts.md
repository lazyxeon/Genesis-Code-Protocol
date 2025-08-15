# Charts & Graphs (V49, GitHub-safe)

This page shows a single Mermaid flowchart for the V49 phase map.  
Tip: The code fence must be exactly three backticks followed by `mermaid` on its own line, no indentation, and end with exactly three backticks on their own line.

## Phase Map (V49)

```mermaid
flowchart TB
  %% ASCII-only labels. No unicode arrows/dashes. Single diagram to avoid fence confusion.

  A0["Pre-Execution - TRIZ ARIZ -0.8"]
  A1["Pre-Execution - C-K Drift -0.5A"]
  A2["Pre-Execution - Worth-It Sprint -1 (C-0.5)"]

  B0["0 Opportunity and Mode / Runner Handshake (C0.1)"]
  B1["1 Context and Precedents (C1.1)"]
  B2["2 Influence Harvesting (C2.1)"]
  B25["2.5 Futures and Morph Space (C2.5)"]
  B3["3 Constraints and Envelope (C3.1)"]
  B4["4 Hypotheses and Branch Tree (C4.1)"]
  B4A["4.A Red-Team Attack (C4.A)"]
  B5["5 Conceptual Modeling and Architecture (C5.1)"]
  B6["6 Simulation and Functional Modeling (C6.1)"]
  B65["6.5 Multi-Agent War Game (C6.5)"]
  B7["7 Iterative Refinement (C7.1)"]
  B9["9 Validation and Benchmarking (C7 / C7.Sigma / C7.Repro)"]
  B10["10 Simplicity C8.4 then Optimization C8.5"]
  B11["11 Productization plus 11.3 IP and Disclosure (C6.9)"]
  B12["12 Documentation and Handoff (C12.1)"]
  B135["13.5 Devastation Protocol (C13.5)"]
  B13["13 Deployment Readiness and Safety Case (C9)"]
  B14["14 Continuous Evaluation (C14.1)"]
  B145["14.5 Continuous Adversary Shadowing (C14.5)"]
  B15["15 Archival Export Postmortem (C15.1)"]

  A0 --> A1 --> A2 --> B0 --> B1 --> B2 --> B25 --> B3 --> B4 --> B4A --> B5 --> B6 --> B65 --> B7 --> B9 --> B10 --> B11 --> B12 --> B135 --> B13 --> B14 --> B145 --> B15
Runner System (reference)
Code, Physical, Theory, OT, Mobility, LifeSci, AgMRV, FinTech.

Examples: medical-ai => [Code, LifeSci], industrial-robotics => [OT, Mobility].

Evidence TTL (reference)
Risk Tier	Default TTL	Notes
R1	180 days	Tracked in 15_ce/PLAN.md
R2	90 days	
R3	30–60 days	Highest rigor
