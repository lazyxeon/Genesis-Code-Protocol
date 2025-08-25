GCP V50 Cartridges Pack – Domain Knowledge Modules (Version 2.0)
Release: TBD (2025)

Cartridges provide modular domain knowledge and retrieval stacks for the Genesis Code Protocol.  Each cartridge bundles embeddings, indexes, lexicons, evaluation hooks, tools and governance notes for a specific domain.  Cartridges are deterministic and versioned; they can be discovered and validated via the Cartridges Parse Pack runner.  This document specifies the v2.0 cartridge schema and describes the built‑in domain cartridges included with GCP V50.
0. Concept and usage
Cartridges encapsulate everything needed for an LLM to perform high‑quality retrieval, reasoning and generation in a domain.  They include:

Manifest (CARTRIDGE.json) – metadata and configuration (schema below).  Cartridges must be signed using the Exotics meta‑cartridge key.
Vectorisation stack – embedding model(s) and index configuration (e.g., Milvus HNSW or FAISS IVF) for retrieval.
Lexicons & data anchors – vocabularies, ontologies and anchor terms/phrases to guide search and classification.
Evaluation hooks – metrics and thresholds to monitor retrieval quality (e.g., MRR, recall), hallucination rate and provenance coverage.
Tool bundles – optional domain‑specific tools with JSON contracts (e.g., patent search API, simulation engine).
Governance & licensing notes – terms of use, licensing and sustainability hints.

Cartridges are stored under cartridges/<domain>/ and registered in registry/REGISTRY.json.  The RUNNER_CARTRIDGES_PARSE_PACK validates the manifest and populates the registry.  Cartridges declare which runners they support (e.g., RUNNER_CREATIVE_DISCOVERY, RUNNER_RESEARCH) and may be required to proceed in those phases.
1. Universal Cartridge Schema (v2.0)
Each cartridge must include a top‑level CARTRIDGE.json conforming to the following schema (simplified here; see schemas/CARTRIDGE_v2.schema.json for validation):

{

  "name": "quantum_materials",

  "version": "2.0.1",

  "domain": "Quantum Materials",

  "description": "Embeddings, lexicons and tools for discovery and reasoning about quantum materials, superconductors and topological phases.",

  "supported_runners": ["RUNNER_CREATIVE_DISCOVERY", "RUNNER_RESEARCH", "RUNNER_SYSTEM_DESIGN"],

  "embedding_models": [

    {

      "id": "bge-large-quantum",

      "provider": "huggingface",

      "model": "BAAI/bge-large-en-v1.5",

      "dimension": 1024,

      "languages": ["en"],

      "domain_specialisation": "quantum materials"

    }

  ],

  "index": {

    "type": "milvus",

    "metric": "cosine",

    "params": {"efConstruction": 200, "M": 16},

    "fallback": {"type": "faiss", "metric": "dot", "params": {"nlist": 1024}}

  },

  "chunking": {

    "max_tokens": 512,

    "overlap": 64,

    "deduplicate": true

  },

  "lexicons": ["data/ontology.owl", "data/terms.csv"],

  "evaluation": {

    "retrieval_mrr_threshold": 0.35,

    "hallucination_rate_threshold": 0.05,

    "provenance_coverage_threshold": 0.95

  },

  "tools": [

    {

      "name": "wipo_patents",

      "version": "1.0.0",

      "contract": "tools/wipo_patents_contract.json",

      "description": "Search WIPO PATENTSCOPE for relevant patents."

    }

  ],

  "governance": {

    "license": "CC‑BY‑4.0",

    "provenance": "Derived from open quantum materials databases and academic papers.",

    "sustainability": {

      "sci_factor": 0.10,

      "notes": "Embedding model uses GPU; approximate energy consumption documented in README."

    }

  },

  "signature": "BASE64_SIGNATURE"

}
Field descriptions
name: unique slug identifying the cartridge.
version: SemVer string for the cartridge.  Bump minor for backward‑compatible changes, major for breaking changes.
domain: human‑readable domain name.
description: summary of domain scope.
supported_runners: list of runners that may use this cartridge.  Only those runners should import the cartridge’s resources.
embedding_models: array of embedding model configurations.  Each entry must specify provider, model name, dimension and language/domain specialisation.
index: index configuration with type (milvus, faiss, elastic, etc.), metric and parameters.  A fallback index may be specified.
chunking: rules for splitting text into embeddings (max tokens, overlap, deduplication).
lexicons: list of vocabulary or ontology files packaged with the cartridge.
evaluation: thresholds for retrieval quality, hallucination rate and provenance coverage.  Runners use these to decide if candidate retrieval is sufficient.
tools: optional domain‑specific tools with contract files; these must adhere to the tool contract schema in the Master Runners Codex.
governance: licensing and provenance notes; sustainability hints (SCI factor per use; energy/carbon estimates).
signature: base64 signature of the manifest; verified by the Exotics meta‑cartridge.
2. Built‑in domain cartridges
GCP V50 includes a curated set of cartridges covering core domains.  Each cartridge directory contains the CARTRIDGE.json, lexicons, index files and tools.  Summaries of built‑in cartridges are provided below.  Users may add their own cartridges by following the schema and signing them.
2.1 Code
Domain. General programming languages, software engineering patterns, algorithms and systems design.

Embedding model: bge-large-code (dimension 1024) optimised for code and docstrings.
Index: Milvus HNSW (M=16, efConstruction=200) with FAISS fallback.
Lexicons: Programming language glossaries, API documentation, design pattern catalogues.
Tools: github_search (contract for searching code repositories), code_simulator (simulate code execution), static_analyser.
Evaluation thresholds: MRR ≥ 0.40, hallucination rate ≤ 3 %, provenance coverage ≥ 95 %.
Governance: MIT‑licensed; derived from open‑source repositories; SCI factor 0.05 per 1k embeddings.
2.2 Energy & Power Systems
Domain. Electric power grids, renewable energy, battery technology, smart grids.

Embedding model: bge-large-energy (trained on IEEE power systems literature).
Index: Milvus with metric=IP and FAISS fallback.
Lexicons: Standard IEEE power engineering terms, NREL datasets.
Tools: pv_simulator, grid_stability_checker, nrel_data_api.
Evaluation thresholds: MRR ≥ 0.33, hallucination rate ≤ 5 %, provenance coverage ≥ 90 %.
Governance: CC‑BY‑4.0; data from DOE and NREL; SCI factor 0.08.
2.3 Legal & Regulatory
Domain. Laws, regulations, case law and compliance frameworks (e.g., GDPR, HIPAA, EU AI Act, ISO 42001).

Embedding model: bge-large-legal (multi‑lingual legal text embeddings).
Index: ElasticSearch with BM25 metric and FAISS fallback for dense retrieval.
Lexicons: Black’s Law Dictionary, compliance glossaries, acronym lists.
Tools: govt_regulations_api (search EU/US regulations), case_search (judicial opinions search), dp_risk_assessor.
Evaluation thresholds: MRR ≥ 0.30, hallucination rate ≤ 4 %, provenance coverage ≥ 98 %.
Governance: Data under various licenses; usage restricted to non‑legal advice; SCI factor 0.06.
2.4 Life Sciences & Healthcare
Domain. Biology, medicine, genomics, drug discovery, healthcare guidelines.

Embedding model: bge-large-bio (trained on PubMed and biomedical corpora).
Index: Milvus with cosine metric.
Lexicons: Gene Ontology, MeSH terms, SNOMED CT.
Tools: ncbi_entrez search, drug_interaction_checker, clinical_trials_api.
Evaluation thresholds: MRR ≥ 0.38, hallucination rate ≤ 5 %, provenance coverage ≥ 95 %.  Additional DP evaluation required for PHI.
Governance: Data governed by NIH/NLM policies; HIPAA compliance guidance; SCI factor 0.09.
2.5 Agriculture & Food Systems
Domain. Crop science, soil health, farming practices, food supply chains.

Embedding model: bge-large-agri (trained on agronomy literature and FAO reports).
Index: Milvus with metric=cosine.
Lexicons: Crop species taxonomy, soil nutrients, weather patterns.
Tools: usda_crop_api, soil_nutrient_analyser, supply_chain_tracker.
Evaluation thresholds: MRR ≥ 0.32, hallucination rate ≤ 6 %, provenance coverage ≥ 90 %.
Governance: Data from USDA and FAO; SCI factor 0.07; ensure ethical considerations for GMOs and pesticide use.
2.6 Quantum Materials & Advanced Physics
Domain. Quantum materials, superconductivity, topological phases, quantum computing architectures.

Embedding model: bge-large-quantum (as shown in schema example).
Index: Milvus HNSW; high dimensional (1024).  Fallback FAISS.
Lexicons: Crystal structures, topological invariants, quantum numbers.
Tools: materials_project_api, ab_initio_simulator, topological_classifier.
Evaluation thresholds: MRR ≥ 0.35, hallucination rate ≤ 5 %, provenance coverage ≥ 95 %.
Governance: Derived from Materials Project, OQMD; license CC‑BY‑NC‑4.0; SCI factor 0.12.
2.7 Advanced Robotics & Autonomous Systems
Domain. Robotics design, control theory, autonomous vehicles, drones.

Embedding model: bge-large-robotics (trained on robotics papers and ROS documentation).
Index: Milvus; fallback FAISS.
Lexicons: Control theory terms, ROS message types, actuators and sensors vocabulary.
Tools: ros_simulator, path_planner, control_stability_checker.
Evaluation thresholds: MRR ≥ 0.34, hallucination rate ≤ 5 %, provenance coverage ≥ 93 %.
Governance: Data from ROS, arXiv; open‑source; SCI factor 0.10.
2.8 Climate Adaptation & Sustainability
Domain. Climate science, adaptation strategies, carbon accounting, sustainability frameworks.

Embedding model: bge-large-climate (climate reports, IPCC docs, sustainability research).
Index: ElasticSearch with dense retrieval fallback.
Lexicons: IPCC terms, greenhouse gases, adaptation techniques.
Tools: ipcc_search, carbon_accounting_tool, climate_risk_assessor.
Evaluation thresholds: MRR ≥ 0.31, hallucination rate ≤ 5 %, provenance coverage ≥ 92 %.
Governance: CC‑BY‑SA; emphasises sustainable practices; SCI factor 0.07.
2.9 Synthetic Biology & Biodesign
Domain. Genetic circuits, gene editing, metabolic engineering, synthetic ecosystems.

Embedding model: bge-large-synbio (trained on synthetic biology literature).
Index: Milvus; fallback FAISS.
Lexicons: Gene regulatory networks, metabolic pathways, safety terms.
Tools: genetic_design_tool, metabolic_pathway_simulator, biosafety_checker.
Evaluation thresholds: MRR ≥ 0.33, hallucination rate ≤ 6 %, provenance coverage ≥ 90 %.  Additional biosafety review required.
Governance: Data from iGEM, JBEI; license CC‑BY‑NC; SCI factor 0.11.  Contains high‑risk content; requires Safety Lead approval.
2.10 FinTech & Regulation
Domain. Financial technologies, blockchain, payments, securities, regulatory compliance (SEC, FINRA).

Embedding model: bge-large-fintech (trained on financial regulations, fintech white papers, crypto protocols).
Index: ElasticSearch + Milvus fallback.
Lexicons: Financial instruments, regulatory agencies, compliance checks.
Tools: sec_filings_search, payment_system_simulator, risk_assessment_tool.
Evaluation thresholds: MRR ≥ 0.30, hallucination rate ≤ 4 %, provenance coverage ≥ 96 %.
Governance: Data licensed from EDGAR, BIS; usage restricted for financial advice; SCI factor 0.09.
3. Meta‑cartridge and security
The Exotics Meta‑Cartridge validates and signs all other cartridges.  Its responsibilities include:

Schema validation – verifying that CARTRIDGE.json conforms to v2.0 schema.
Signature verification – ensuring each cartridge manifest is signed with a recognised key.  Untrusted cartridges are flagged.
Compatibility check – verifying that embedding models and tools meet security and licensing requirements.
Registration – recording validated cartridges in registry/REGISTRY.json with trust levels (e.g., trusted, community, unverified).
Licensing enforcement – ensuring that the license terms in the governance section are compatible with the project’s use case.
4. Registry and discovery
Cartridges are indexed in registry/REGISTRY.json generated by RUNNER_CARTRIDGES_PARSE_PACK.  Each entry includes:

{

  "name": "code",

  "version": "2.0.0",

  "domain": "Code",

  "path": "cartridges/code/",

  "signature_status": "verified|unverified|expired",

  "supported_runners": ["RUNNER_CREATIVE_DISCOVERY", "RUNNER_RESEARCH", "RUNNER_SYSTEM_DESIGN"],

  "trust_level": "trusted|community|unverified"

}

Runners use the registry to resolve which cartridges to load.  A simple CLI can be implemented to manage cartridges (illustrative only):

$ cartridge.list

Name            Version  Trust    Supported Runners

code            2.0.0    trusted  creative, research, design

energy_power    2.0.0    trusted  creative, research, design

legal           2.0.0    community creative, research, compliance

...

$ cartridge.validate path/to/CARTRIDGE.json

Validating schema… OK

Verifying signature… OK

MRR threshold >= 0.30… OK

Registered as trusted.

$ cartridge.register path/to/CARTRIDGE.json

Registered quantum_materials v2.0.1 as community (signature unverified).

$ cartridge.verify_signature quantum_materials

Signature verified by Exotics key.  Trust level upgraded to trusted.
5. Evaluation and FinOps integration
Cartridges define default thresholds for retrieval quality and hallucination rate.  Runners compare their performance to these thresholds and, if necessary, adjust retrieval parameters or switch embedding models/indexes.  Additionally, cartridges provide sustainability hints:

"governance": {

  "sci_factor": 0.08,

  "notes": "Embedding model inference uses ~0.5 kWh per 1000 queries; choose CPU inference when possible."

}

The FinOps runner can sum the SCI factors from all loaded cartridges and compute expected carbon emissions.  Cartridges may also include cost guidance (e.g., API usage fees) to help budgeting.
6. Authoring new cartridges
Third parties can author cartridges for new domains.  To contribute:

Create a directory cartridges/<your_domain>/ with embeddings, index, lexicons and a CARTRIDGE.json manifest conforming to the v2.0 schema.
Include tool contracts in tools/ for any domain‑specific APIs; ensure they follow the tool contract schema in the Master Runners Codex.
Define evaluation thresholds (MRR, hallucination rate, provenance coverage) based on benchmarking against representative tasks.
Document provenance and licensing in the governance section; declare SCI factors.
Sign the CARTRIDGE.json with your private key.  Submit the cartridge to the registry maintainers or publish it to a trusted registry.  Include signature verification instructions.
Provide a short README.md describing the domain, usage examples and tool instructions.
Safety and ethics
Cartridge authors must ensure that content does not violate ethical guidelines (e.g., no harmful biological agents without containment, no illegal or unethical instructions).  High‑risk domains (e.g., synthetic biology, firearms) require an explicit safety review and may only be loaded with Safety Lead approval.



This Cartridges Pack v2.0 enables GCP V50 to ingest rich domain knowledge across a spectrum of disciplines.  Together with the Master Runners Codex, cartridges empower LLMs to perform sophisticated discovery, retrieval and reasoning tasks while maintaining quality, provenance and compliance.

