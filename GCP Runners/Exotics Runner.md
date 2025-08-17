6 Exotics Runner & Cartridges 
The Exotics runner is an umbrella for a set of high‑risk domains that each require their own micro‑gates and artefacts. Attaching runner exotics with a cartridge parameter (disaster, sports, culinary, legal or entertainment) loads the respective definitions described in Sections 5.7–5.11, along with their policies, metamorphic tests, novelty benchmarks and artefacts. The Exotics runner itself defines the base schema and refusal guards: 
runner: 
name: "Exotics" 
aliases: ["exotics"] 
risk_tier: "R2|R3" # depends on cartridge 
confidence_target: 0.95|0.975 # depends on cartridge 
roles: 
- Planner 
- Researcher 
- Inventor 
- Engineer 
59
- Adversary 
- Optimizer 
- Auditor 
- Productizer 
- Operator 
- Scribe 
refusal_policy: 
- "Refuse to attach an unknown cartridge." 
- "Refuse to bypass cartridge‑specific refusal rules." 
agent_graph: "agents/exotics_agent_graph.json" 
memory_config: "memory/exotics_memory_config.yml" 
policy_module: "Policies/exotics.rego" # dispatches to cartridge policies micro_gates: [] # All gates supplied by selected cartridge 
metrics: [] # Metrics supplied by selected cartridge 
tool_catalog: "tools/catalog.json" 
failure_matrix: "tools/failure_matrix.csv" 
kickoff: 
prompt_template: | 
attach runner exotics 
Initiate GCP V49 for Spark: <exotic use‑case> + <cartridge: disaster| sports|culinary|legal|entertainment> 
Mode: <Full‑Run|Auto> • Risk: <R2|R3> 
Context: domain scoping for the chosen cartridge 
Deliverables: cartridge micro‑gates & artefacts, metamorphic & adversarial  tests, novelty score, signed release 
When a cartridge is specified, the Exotics runner merges its own agent graph and memory config with that of the cartridge, then applies the cartridge’s refusal policy, micro‑gates, metrics and artefacts. The cartridges for Disaster, Sports, Culinary, Legal and Entertainment have been fully defined above in Sections 5.7–5.11 and need no further summarization here. 
7 Gate UX & Decision Cards 
The Flagship codex inherits the gate UX from GCP V49. At each gate (including micro‑gates defined in this codex), the LLM prints a Gate Decision Card with the check name, options to proceed, branch, return or end, a recommendation with rationale, confidence, cost/time and risk assessment. In Full‑Run mode, execution pauses for human input; in Auto mode, the LLM executes the recommended option unless the gate is marked Human‑Required. 
8 Rehydration & Exit 
Every runner includes a rehydration script and status report (e.g., Rehydration_Test/<runner>.sh ,  Rehydration_Test/<runner>_status.json ) that rebuilds the environment from the audit bundle, 
60
reruns core tests and verifies that key results are reproduced. Failure to pass rehydration marks the run as incomplete. The Exit Wizard packaging from GCP V49 applies equally here: the final export (ZIP or PDF/A) includes all artefacts, manifest, provenance receipts and transparency log entries, along with a rehydration badge, provenance badge and SBOM badge when applicable. 
9 References & Standards 
Throughout this codex, runners reference external standards and normative guidance. Citations include, but are not limited to: the Sphere Handbook for humanitarian response, WADA prohibited lists, FDA Food Code, ABA Model Rules, IGDA Ethics Code, PCI DSS, FERPA, OECD Deliberative principles, ISO and IEC standards for hardware, aerospace and power systems, NIST security and risk guidelines, IPCC MRV guidelines, and religious source canon collections. See each runner’s standards_refs for details. These references are not reproduced in full here; instead they act as signposts for the LLM to locate authoritative guidance during execution. 
10 Change Log vs Master Runner v49‑AI 
This Flagship edition retains the structure of the original Master Runner v49‑AI while integrating the full Flagship rubric. Key enhancements include: 
1.  
Agent orchestration — added agent_graph.json and explicit role hand‑offs to every runner. 
2.  
Memory & evidence — defined memory configs, claim graphs and evidence indexes with retention, 
redaction and retrieval policies. 
3.  
Policy‑as‑code — added Policies/<runner>.rego modules implementing refusal policies and 
micro‑gate conditions using OPA/Rego. 
4.  
Metamorphic & property‑based tests — inserted universal metamorphic gates and provided 
domain‑specific invariants and transforms. 
5.  
Novelty benchmarking — integrated novelty/sota_benchmarks.csv and novelty scoring with 
thresholds; required SOTA comparisons in gates. 
6.  
Adversarial testing — expanded redteam corpora and added adversarial gates to all runners. 7.  
Observability from birth — mandated OTEL plans and spans for every runner; added Observability micro‑gate. 
8.  
Supply‑chain & provenance — mandated SBOM, SLSA attestations and signature verification across all runners; added SupplyChain gate. 
9.  
Rehydration proof — added rehydration scripts and required pass status for completion; integrated 
with Exit Wizard badges. 
10.  
Energy/Cost reporting — optional carbon report added to runners with significant computational 
or material footprint. 
This codex is meant to be used alongside GCP   V49 Flagship. Together they form a comprehensive, automated invention framework with rigorous safety, compliance and novelty checks across multiple domains.  
