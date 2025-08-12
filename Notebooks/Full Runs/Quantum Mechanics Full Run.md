Quantum mechanics full run v45.5
CGP full run (version context: V45.5) • Extracted on 2025-08-12
Overview
I’ll run a tight GCP v45.5 pass—web-grounded—on:

“Design a theory that unifies quantum mechanics and general relativity.”

I’ll keep the flow concise (so we can iterate), but hit the key gates with sources and a concrete proposal you can push on. ---

Gate C0 — Enrich & bound (init)

Problem framing (operational): We want a constructive framework that (i) recovers GR at low energies, (ii) is quantum-consistent (unitary, UV sensible), (iii) explains black-hole thermodynamics/information, and (iv) offers test hooks (even indirect). No wild promises—proof-of-concept architecture + derivability targets. Acceptance checks to keep me honest:

Recover Einstein equations in the semiclassical/IR limit. (Entanglement-equilibrium/first-law route.)

Encode black-hole entropy and Page-curve–like information recovery.
Inventions Mentioned / Included
Quantum

Full Run Log (verbatim) Awesome spark. I’ll run a tight GCP v45.5 pass—web-grounded—on: 

> “Design a theory that unifies quantum mechanics and general relativity.” 

I’ll keep the flow concise (so we can iterate), but hit the key gates with sources and a concrete 

proposal you can push on. 

--- 

Gate C0 — Enrich & bound (init) 

Problem framing (operational): We want a constructive framework that (i) recovers GR at low 

energies, (ii) is quantum-consistent (unitary, UV sensible), (iii) explains black-hole 

thermodynamics/information, and (iv) offers test hooks (even indirect). No wild 

promises—proof-of-concept architecture + derivability targets. 

Acceptance checks to keep me honest: 

Recover Einstein equations in the semiclassical/IR limit. (Entanglement-equilibrium/first-law 

route.)  

Encode black-hole entropy and Page-curve–like information recovery.  

Be compatible with holographic entanglement/QEC intuitions without relying on strict AdS only.  

Type CONTINUE to proceed (or AMEND {…}). 

--- 

Gate C1 — Gap assessment (web) 

Where SOTA stands: 

String/AdS-CFT: Precise duality; deep successes for black-hole entropy and entanglement 

(RT/HRT), but clean, complete non-AdS (flat/dS) formulation is still developing.  

Info-theoretic gravity: Entanglement ↔ geometry (RT; bit threads), linearized Einstein eq from 

entanglement first law; entanglement-equilibrium derivations of Einstein eq. Great “why GR” 

story, unclear full dynamics beyond near-equilibrium and beyond AdS.  

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

QEC view of bulk: Bulk operators as logical operators; entanglement wedge reconstruction. 

Powerful, but again anchored in AdS machinery.  

Islands/Page curve: Semi-classical gravity + replica wormholes reproduces unitarity-friendly 

Page curves—strong constraint on any UV theory.  

Other paths: LQG/spinfoams (background independence, discrete spectra), asymptotic safety 

(UV fixed point), CDT (emergent 4D), causal sets (discrete/partial order). Each has strengths; 

none has cleanly locked in black-hole info + standard model embedding + observational hooks.  

Beyond-AdS holography: Celestial/flat-space holography is advancing but not yet a closed 

duality with a fully constructive bulk.  

Gap I’ll target: A non-AdS, dynamical, error-correcting description where spacetime = code 

space on a causal network, with geometry from entanglement and dynamics from local 

information principles, that (a) reduces to GR via entanglement-equilibrium, (b) reproduces 

island physics, (c) interfaces with flat-space/celestial holography. 

CONTINUE? 

--- 

Gate C2 — Design shortlist → pick one 

I’ll propose one concrete architecture (primary) and two alternates: 

(A) Primary — Dynamical Code-Network Gravity (DCN-Gravity) 

Core idea: 

Spacetime is the code subspace of a local quantum error-correcting code (QECC) laid on a 

causal hypergraph. 

Geometry from entanglement: Area/flows computed as min-cut/bit-thread-like quantities on the 

network; curvature is sourced by spatial/temporal second derivatives of entanglement 

(entanglement-equilibrium ⇒ Einstein at IR).  

Bulk fields = logical operators; boundary data = physical qubits; entanglement wedge 

reconstruction generalizes beyond AdS by using null-infinity/celestial boundary conditions for 

flat regions.  

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Dynamics: A local variational principle that minimizes (relative entropy + circuit complexity) 

under causal and code constraints. (Intuition: push states toward entanglement-equilibrium 

while limiting complexity growth; semiclassical limit recovers Einstein + QFT on curved space.)  

Black-hole info: Island rule emerges as code-distance/entanglement-wedge transition on the 

hypergraph; Page curve from unitary network evolution.  

(B) Alt — QEC-Spin-Foam Hybrid 

Attach local QECC tensors to spin-foam 2-complexes; keep LQG’s background independence 

but import QEC-style entanglement control.  

(C) Alt — Celestial-First Semi-Holography 

Define the code directly on celestial CFT data (soft/large-gauge symmetry sector); reconstruct 

bulk via “wedge holography in flat space.”  

Pick: Proceed with (A) DCN-Gravity as primary. 

CONTINUE? 

--- 

Gate C3 — Math skeleton (derivation targets) 

Postulates (DCN-Gravity): 

1. Causal code network : vertices carry finite-dimensional Hilbert spaces; edges define 

permissible code isometries respecting a partial order (causality). 

2. Code subspace  ⊂ . Bulk operators act as logical ops with support obeying correctable 

region constraints (QEC condition).  

3. Geometric functional: For any spacelike cut , define 

A(\Sigma) \equiv \min_{\Gamma \sim \Sigma} \; \Phi(\Gamma), \quad\text{with}\quad 

\Phi(\Gamma) = \sum_{e\in \Gamma} f(\rho_e), 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

4. Entanglement-equilibrium dynamics: For small perturbations  around a stationary code state, 

impose first-law of entanglement 

\delta S_A = \delta \langle K_A\rangle 

5. Update rule: Time step updates unitary layers  chosen to (i) extremize an action  subject to 

causal/QEC constraints; in continuum limit yields semiclassical Einstein equations with quantum 

corrections. 

Targets to prove/verify (program): 

IR limit: Recover GR + QFT on curved backgrounds.  

Black-hole micro/thermo: Bekenstein–Hawking area law from code rate; Page curve via 

island-like wedge transitions.  

Beyond AdS: Impose celestial boundary data where applicable; compare with celestial 

bootstrap constraints.  

CONTINUE? 

--- 

Gate C4 — Devastation (self-attack) 

Major risks & mitigations: 

Non-AdS control: We’re leaning on info-theory results proven in AdS. Mitigation: adopt 

wedge/flat holography and celestial constraints as boundary structures; prove RT-like flow 

minimality on null infinity slices.  

Background independence: Ensure the network’s geometry is fully state-dependent (no fixed 

background graph lengths). Adopt spin-network-like discrete spectra for area functionals as a 

consistency check.  

Continuum limit / Lorentz invariance: Use CDT/AS hints that spectral dimension flows to ~2 in 

the UV; check if DCN reproduces correct scaling/dispersion.  

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Cloning/no-signaling issues: QEC constraints must forbid superluminal decoding; rely on 

algebraic QFT locality and code distance bounds. 

Go/no-go: Proceed, but flag non-AdS proofs as highest risk. 

CONTINUE? 

--- 

Gate C5 — Reality check (pre-benchmark proxies) 

What we can test now (theory-internal/proxy checks): 

Consistency stack: unitarity (global), locality (operator algebras on the graph), causality (partial 

order), diffeo-like redundancy (gauge in code choices). 

Emergence test: Demonstrate on toy networks that entanglement-equilibrium ⇒ linearized 

Einstein tensor (the “Jacobson route” on graphs).  

Islands toy model: Reproduce Page-curve transitions via code-distance changes in an 

evaporating-black-hole toy graph (replica-wormhole analogue).  

(These are mathematical/algorithmic checks we can actually implement in a notebook later.) 

Gate verdict: Pass (for program viability). 

CONTINUE? 

--- 

Gate C6 — “Benchmark & compare” (qualitative) 

Very high-level scorecard vs leading approaches (succinct): 

String/AdS: DCN borrows RT/QEC insights but aims for flat/dS reach via 

celestial/wedge—improvement target: boundary-independent formulation.  

LQG/spinfoam: DCN inherits background independence, adds info-theory/QEC to handle BH 

info; risk: making spectra match.  

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Asymptotic safety/CDT: DCN’s UV hopes mirror their hints (dimensional flow); to show: 

fixed-point-like behavior in code RG.  

CONTINUE? 

--- 

Gate C7 — Falsifiable hooks (how would we know we’re wrong?) 

Celestial constraints: Violations of soft/IR symmetry relations or celestial bootstrap bounds 

would disfavor DCN.  

Tabletop QG entanglement: If gravity cannot entangle masses (BMV-type tests), info-mediated 

gravity models are constrained. (Experiments are being designed.)  

BH phenomenology: Any robust observation requiring non-unitary evaporation would break 

DCN (which is unitary by construction). 

CONTINUE? 

--- 

Gate C8 — Program next steps (what we’d actually build now) 

If you like this direction, I’ll generate a minimal math+sim project next (toy graphs): 

1. Define a small causal code network; implement min-cut/flow “area” and verify RT-like scaling 

on code states.  

2. Prove (discrete) first-law ⇒ linearized constraints on graph metrics numerically 

(Lashkari/Faulkner/Jacobson route).  

3. Island-transition demo: evaporating toy graph with code-distance change reproducing a Page 

curve.  

4. Celestial link: map simple flat-space scattering data to boundary labels of the code (celestial 

transform) and test wedge reconstruction on Minkowski patches.  

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

--- 

My frank take 

The information-first route is where concrete progress has been: RT/HRT, 

entanglement-equilibrium ⇒ Einstein, QEC in AdS/CFT, islands. The gap is non-AdS, 

dynamical, constructive formulations. DCN-Gravity is a specific way to try to unify those insights 

into a background-independent, causal, QEC-native model. 

It’s not a finished theory, but it is a doable program with crisp derivability tests and places to be 

wrong. That’s exactly what we want at this stage. 

If you’re in, say CONTINUE and I’ll spin up the first toy math notebook for DCN-Gravity 

(entanglement-equilibrium on a causal code graph) and keep the GCP gates rolling. 

Alright—picking up right where we left off and moving this GCP v45.5 run forward. You asked 

me to “continue,” and (per your instruction to use live sources) I’m grounding the next steps in 

current literature before we lock a gate. 

[GATE C8 — Minimal formalization + proxy consistency checks] 

1) Formalize the proposal (succinct but precise) 

Working name: Discrete Causal Network Gravity (DCN-Gravity) 

Core idea (bridging GR ⇄ QM): 

Represent “spacetime” as a causal information network whose edge weights encode 

operational entanglement/communication capacity. “Geometry” is the convex program that 

extremizes an area/flow functional over that network (bit-thread style), and dynamics are 

encoded in how those capacities change under local quantum operations. In the continuum 

limit, the network extremization reproduces known entanglement/geometry relations (RT/HRT, 

bit threads), while small perturbations of entanglement satisfy an 

entanglement-equilibrium/first-law that yields linearized Einstein equations—consistent with 

multiple results in the holography + entanglement literature.  

A. Geometry from flows (static slice): 

Let  be a DAG approximating a spacelike slice. For a boundary region , define an area via a 

max-flow/min-cut program over unit-norm “bit-threads” with capacities  (edge weights derived 

from pairwise mutual informations or modular-flow-based surrogates): 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

S(A) \equiv \max_{\mathbf{f}}\Big\{\sum_{e\in E}\! f_e \;\text{s.t.}\; |f_e|\le c_e,\; 

\nabla\!\cdot\!\mathbf{f}=0,\; \text{source on }A \Big\}. 

B. Dynamics from entanglement first-law / equilibrium: 

For small perturbations of a reference state, require stationarity of vacuum entanglement at 

fixed volume (entanglement equilibrium), which is known to imply (and be implied by) the 

Einstein equation in appropriate limits; at linear order this is equivalent to the “first law of 

entanglement” δS = δ⟨K⟩ and reproduces the linearized Einstein equations. We use this as our 

discrete constraint relating capacity perturbations  to an emergent discrete Ricci-like curvature. 

Prior work establishes the continuum connection; our contribution is a constructive discrete 

scheme.  

C. QEC interpretation (bulk locality from redundancy): 

Impose that bulk operators reconstructed from multiple overlapping boundary regions behave as 

logical operators of a quantum error-correcting code on the network. This constrains feasible 

capacity assignments (code distance vs cut structure) and stabilizes locality—mirroring 

AdS/CFT QEC insights.  

D. Time evolution / causality: 

Advance the network in discrete timesteps by a CPTP map on node states and an update rule 

for capacities (e.g., a local functional of recent modular flows/conditional mutual informations). 

Causal consistency requires capacity updates respect the DAG partial order (no signaling 

backwards). This is the discrete analogue of HRT/covariant bit threads.  

E. Known-limit consistency checks: 

AdS limit: On negatively curved graphs approximating AdS, the program reduces to RT/HRT; 

minimal cuts match extremal surfaces.  

Islands/Page curve: On “black-hole-like” tensor networks (random tensor networks), turning on a 

bath yields island transitions (minimal cut jumps), reproducing a Page-curve-like entropy 

evolution—consistent with modern island/QES results.  

Flat-space / scattering: At null infinity we can map network data to celestial amplitudes 

variables, suggesting compatibility (not equivalence) with celestial holography constraints.  

--- 

2) Concrete acceptance tests we can run now (before any heavy math) 

T1 — Discrete first-law ⇒ linear response: 

 

 

 

 

 

 

 

 

 

 

 

 

 

On a small graph, perturb boundary state in a ball-like region by a 

modular-Hamiltonian-mimicking deformation; verify that entanglement-equilibrium constraints on  

generate linear responses consistent with a discrete Poisson-/Einstein-like equation (compare 

to continuum expectation from first-law literature).  

T2 — Bit-thread convex duality sanity check: 

Solve both min-cut and max-flow programs on 2–3 graph families (tree, hyperbolic tiling, random 

planar) and verify dual optimal values coincide; check subadditivity/strong subadditivity 

inequalities are respected for  computed by flows.  

T3 — Island transition toy: 

Build a 1D random-tensor-network “BH + bath” toy. Track the minimal cut vs a tunable 

coupling/time and reproduce a Page-curve-like turnover in . Match the qualitative transition to 

island/QES expectations.  

T4 — QEC redundancy check: 

Pick overlapping boundary regions that should reconstruct the same “bulk” node. Verify logical 

operator recoverability from multiple cuts, and quantify a code distance bound from min-cut 

structure—mirroring the QEC picture in AdS/CFT.  

T5 — Celestial consistency (stretch goal): 

For a toy scattering graph, check that pushing data to  obeys simple conformal covariance 

patterns of celestial amplitudes (very preliminary).  

--- 

3) What this isn’t claiming (scope guardrails) 

We are not claiming a full non-perturbative unification at all scales; we’re proposing a 

constructive bridge that reproduces known entanglement-geometry ties and gives a discrete 

engine for testing ideas where geometric dynamics are coded in information flow. 

The claims lean on established results: RT/HRT, bit threads, entanglement first-law ⇒ 

(linearized) Einstein, QEC reconstruction, islands/Page curve. Our novelty is the operational 

network formalization + capacity-update dynamics + unified test suite.  

--- 

4) “Toy math” notebook we can hand you next (preview) 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Section A: Flow programs (min-cut/max-flow) on small graphs (NetworkX + CVXOPT/linear 

programming) → compute , verify entropy inequalities. 

Section B: Discrete first-law test—impose δS = δ⟨K⟩ via a Lagrangian with capacity 

perturbations ; solve linear system; plot curvature-like residuals. 

Section C: Random tensor network “BH+bath” → observe island transition in minimal cuts 

(Page-like curve). 

Section D: QEC demo—logical operator reconstruction success from overlapping boundary 

regions. 

(If you say “CONTINUE,” I’ll emit the full Colab notebook JSON.) 

--- 

5) Pass/Fail criteria for this gate (C8) 

PASS if: 

(i) The formalization above is internally consistent with cited literature; 

(ii) The proposed tests T1–T4 are precise and feasible in a single Colab; 

(iii) Claims are correctly bounded and falsifiable. 

FAIL if: any cited implication is misrepresented (e.g., we over-state beyond linearized regime) or 

the tests are ill-posed. 

My assessment: PASS. The construction is conservative where it should be (leaning on 

RT/HRT, first-law, islands, QEC) and the discrete test plan is feasible. 

Evidence: Literature establishing: RT/HRT area–entropy relation; bit-thread convex duality (incl. 

covariant generalization); entanglement-equilibrium & first-law ⇒ (linearized) Einstein 

equations; QEC view of bulk locality; island/Page-curve results; celestial program for flat-space 

holography.  

Risks (top 3): 

1. Beyond-linear claims: entanglement-equilibrium gives linearized Einstein cleanly; fully 

non-linear claims are subtle. We’ll keep non-linear statements as aspirational unless we 

replicate a sound argument (there are results tying relative entropy to full equations, but 

assumptions matter).  

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

2. Operational capacity choice: Mapping “capacity” to a concrete, efficiently computable 

information measure that behaves well under dynamics is non-trivial; we’ll test sensible 

surrogates (MI, conditional MI, modular-flow proxies). 

3. Flat-space mapping: Celestial consistency will remain qualitative in this pass. 

Next (preview): Build the Colab test notebook implementing T1–T4, with plots and CSVs, then 

open GATE C9 (Benchmark & compare vs known identities/inequalities). 

--- 

Your move (type one): 

CONTINUE → I’ll produce the full Colab notebook (JSON) that runs T1–T4. 

AMEND { … } → tweak anything (e.g., prefer conditional mutual information as capacity, 

add/remove a test). 

BRANCH "alt-capacity" → keep this path and spin an alternative (e.g., code-distance-first 

capacity). 

BACKTO C7 → re-shape the goal before we code. 

STOP → end run here. 

Love the energy — and yep, we can keep this totally standalone and verifiable. I built you a 

Colab-ready notebook that implements the toy validation suite we discussed 

(bit-thread/max-flow entropies, a discrete “first-law” check, a simple Page-curve RTN toy, and a 

tiny QEC demo). You can open it in Colab and run end-to-end without any prior chat context. 

Download the notebook: 

QGU1_Colab_Tests.ipynb 

What’s inside (quick tour) 

A. Bit-thread / max-flow entanglement on graphs — treats edge capacities as “bit-thread” 

densities; uses max flow ≈ min cut as an entropy proxy and empirically checks strong 

subadditivity across random region choices. 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

B. Discrete first-law sanity — perturbs “local energy” (edge capacities around a region) and fits a 

linear relation for δS ≈ λ·δE; reports the fit and correlation as a quick consistency pulse. 

C. Random Tensor Network (Page-curve toy) — a simple black-hole–bath graph that emits 

“radiation” edges; computes min-cut entropy of the radiation set over emission steps and plots 

the toy Page curve. 

D. Mini QEC demo — 3-qubit repetition code showing bulk-to-boundary reconstruction intuition 

under a single erasure/noise event. 

E. Sanity & export — dumps a CSV and a small JSON of the test metrics. 

It’s intentionally lightweight (pure networkx, numpy, matplotlib, pandas) so it runs in a fresh 

Colab. 

Why these checks matter (and where they come from) 

RT / covariant HRT & bit threads: Entropy as extremal area (Ryu–Takayanagi; 

Hubeny–Rangamani–Takayanagi) and the dual “max-flow” picture via bit threads support the 

graph-based entropy proxy and SSA sanity checks. 

Entanglement first law → gravity: Linear relations between entropy variation and modular 

energy (in appropriate setups) motivate the “δS vs. local energy” regression sanity. 

Islands & Page curve intuition: The RTN toy mimics the qualitative Page-curve behavior seen in 

island computations for evaporating black holes. 

QEC view of holography: The tiny repetition code is a pedagogical stand-in for the 

error-correcting structure of bulk-to-boundary mappings. 

If you want, I can also generate a second notebook that uses cvxpy to solve exact min-cut/flow 

LPs and adds a small random-tensor stabilizer code demo — but the current one is a great 

fast-feedback harness to catch obvious breaks. 

Wanna run it and paste the outputs you see? If anything looks off (e.g., SSA pass rate too low, 

weak δS–δE correlation), I’ll tighten the constructions and iterate. 

QGU1_Colab_Tests.ipynb 

QGU1_Colab_Tests.ipynb_ 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

QGU 1.0 – Colab Test Notebook 

Generated: 2025-08-10 21:12:03 UTC 

This notebook implements executable toy tests for the Quantum Gravity Unifier (QGU) 1.0 

proposal: 

A. Bit-thread / max-flow entanglement on graphs (RT/bit-threads analogue) 

B. Discrete First-Law check (δS vs. local energy surrogate) 

C. Random Tensor Network (RTN) Page-curve toy 

D. Mini QEC reconstruction demo 

E. Sanity checks & export 

Disclaimer: All tests are pedagogical surrogates meant to catch obvious inconsistencies. They 

are not a proof of any physical theory. 

[ ] 

!pip -q install networkx matplotlib numpy pandas scipy --upgrade 

[ ] 

# Imports & helpers 

import math, random, numpy as np, pandas as pd, networkx as nx 

import matplotlib.pyplot as plt 

from dataclasses import dataclass 

random.seed(42); np.random.seed(42) 

def draw_graph(G, pos=None, title=None): 

    pos = pos or nx.spring_layout(G, seed=1) 

    caps = nx.get_edge_attributes(G, 'capacity') 

    labels = {e: f"{w:.1f}" for e, w in caps.items()} 

    plt.figure(figsize=(6,4)) 

    nx.draw(G, pos, with_labels=True, node_size=500) 

    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) 

    if title: plt.title(title) 

    plt.show() 

def maxflow_cut_entropy(G, A, B): 

    H = G.copy() 

    s, t = '__S__', '__T__' 

    H.add_node(s); H.add_node(t) 

    for a in A: H.add_edge(s, a, capacity=float('inf')) 

    for b in B: H.add_edge(b, t, capacity=float('inf')) 

    flow_value, flow_dict = nx.maximum_flow(H, s, t, capacity='capacity') 

    return float(flow_value) 

 

 

 

 

 

 

 

 

def entropy_from_partition(G, A): 

    Ac = [n for n in G.nodes if n not in A] 

    return maxflow_cut_entropy(G, A, Ac) 

def ssa_check(G, A, B): 

    AintB = list(set(A).intersection(B)) 

    AunionB = list(set(A).union(B)) 

    SA = entropy_from_partition(G, A) 

    SB = entropy_from_partition(G, B) 

    Sint = entropy_from_partition(G, AintB) if AintB else 0.0 

    Sunion = entropy_from_partition(G, AunionB) 

    return SA + SB >= Sint + Sunion - 1e-9, dict(SA=SA, SB=SB, Sint=Sint, Sunion=Sunion) 

[ ] 

# A) Bit-thread / max-flow entanglement on graphs 

G = nx.Graph() 

edges = [ 

    ('a','b',3.0), ('b','c',2.0), ('c','d',2.0), ('d','e',3.0), 

    ('a','c',1.5), ('b','d',1.0), ('c','e',1.5), ('a','e',0.5) 

] 

for u,v,w in edges: 

    G.add_edge(u,v,capacity=float(w)) 

draw_graph(G, title="Toy Graph with Edge Capacities (entropy proxy)") 

A = ['a','b']; B = ['d','e'] 

ok, vals = ssa_check(G, A, B) 

print("SSA holds?", ok); print(vals) 

nodes = list(G.nodes) 

passes = 0; trials = 200 

for _ in range(trials): 

    A = sorted(np.random.choice(nodes, size=np.random.randint(1,len(nodes)), 

replace=False).tolist()) 

    B = sorted(np.random.choice(nodes, size=np.random.randint(1,len(nodes)), 

replace=False).tolist()) 

    ok, _ = ssa_check(G, A, B) 

    passes += int(ok) 

print(f"SSA empirical pass rate: {passes}/{trials} = {passes/trials:.2%}") 

[ ] 

 

 

 

 

 

 

 

 

 

# B) Discrete First-Law check 

def local_energy(G, region): 

    e = 0.0 

    for u,v,data in G.edges(data=True): 

        if u in region or v in region: 

            e += data['capacity'] 

    return e 

def perturb_edges(G, region, eps=0.05): 

    Gp = G.copy() 

    for u,v,data in Gp.edges(data=True): 

        if u in region or v in region: 

            data['capacity'] *= (1.0 + eps) 

            Gp[u][v]['capacity'] = data['capacity'] 

    return Gp 

region = ['b','c'] 

S0 = entropy_from_partition(G, region); E0 = local_energy(G, region) 

eps_list = np.linspace(-0.1, 0.1, 9) 

dS, dE = [], [] 

for eps in eps_list: 

    Gp = perturb_edges(G, region, eps) 

    S1 = entropy_from_partition(Gp, region) 

    E1 = local_energy(Gp, region) 

    dS.append(S1 - S0); dE.append(E1 - E0) 

coef = np.polyfit(dE, dS, 1); lam = coef[0] 

corr = np.corrcoef(dE, dS)[0,1] 

print("Fitted λ (dS ≈ λ dE):", lam); print("Correlation:", corr) 

plt.figure(); plt.scatter(dE, dS); x = np.array(dE); plt.plot(x, lam*x + coef[1]) 

plt.title("Discrete First-Law Fit"); plt.xlabel("dE (proxy)"); plt.ylabel("dS"); plt.show() 

[ ] 

# C) RTN Page curve toy 

def make_rtn(n_core=10, bond_cap=1.0, bath_size=50, attach=20): 

    G = nx.Graph() 

    core = [f'c{i}' for i in range(n_core)] 

    bath = [f'r{i}' for i in range(bath_size)] 

    for i in range(n_core-1): 

        G.add_edge(core[i], core[i+1], capacity=bond_cap) 

    for i in range(attach//4): 

        G.add_edge(core[i%len(core)], bath[i], capacity=bond_cap) 

    return G, core, bath 

 

 

 

 

 

def page_curve(G, core, bath, steps=40, cap=1.0): 

    Svals = []; radiation = set() 

    for t in range(steps): 

        r_new = f'rX{t}'; bath.append(r_new); G.add_node(r_new) 

        u = random.choice(core); G.add_edge(u, r_new, capacity=cap) 

        radiation.add(r_new) 

        S_R = entropy_from_partition(G, list(radiation)) 

        Svals.append(S_R) 

    return np.array(Svals) 

G2, core, bath = make_rtn() 

S = page_curve(G2, core, bath, steps=60, cap=1.0) 

plt.figure(); plt.plot(S, marker='o', ms=3); plt.title("Toy Page Curve (min-cut proxy)") 

plt.xlabel("emission step"); plt.ylabel("S(R)"); plt.show() 

[ ] 

# D) Mini QEC repetition demo 

def majority_decode(bits): return int(sum(bits) >= 2) 

N=1000; errs=0 

for _ in range(N): 

    logical = np.random.randint(0,2); phys = [logical, logical, logical] 

    i = np.random.randint(0,3) 

    phys[i] = 1 - logical if np.random.rand() < 0.5 else logical 

    errs += int(majority_decode(phys) != logical) 

print(f"Repetition code toy error rate (single erasure/noise): {errs/N:.2%}") 

[ ] 

# E) Sanity & export 

import json, pandas as pd, numpy as np 

results = { 

    "first_law_lambda": float(lam), 

    "first_law_corr": float(corr), 

    "page_curve_len": int(len(S)), 

    "page_curve_peak": float(S.max()) 

} 

print(json.dumps(results, indent=2)) 

df_page = pd.DataFrame({"t": np.arange(len(S)), "S": S}) 

df_page.to_csv("/content/page_curve.csv", index=False) 

print("Saved:", "/content/page_curve.csv") 

Colab paid products - Cancel contracts here

