# Requirements for Running GCP (Genesis Code Protocol) – V50 Flagship Edition

This document outlines the requirements for running **GCP V50**, the flagship AI‑native edition of the Genesis Code Protocol.  As with earlier releases, GCP is a text‑based framework executed by a large language model (LLM).  The model reads the protocol document (e.g. `GCP V50.md` from this repository), orchestrates each phase, handles recursion and tool calls, and produces artifacts at each gate.  V50 introduces a new *Autonomous Spark Generation* phase ahead of the Worth‑It check, unifies manual and auto modes, extends the phase count to 15 (archival/export), and expands governance and compliance mapping.  The sections below describe the capabilities you need in an LLM, optional dependencies for simulations and benchmarking, and how to run the protocol.

## Core Requirements

### LLM Capabilities
To run GCP V50 you need an LLM that can:

* **Handle complex reasoning and tool‑calling** – The model must support structured phase progression, recursion, tree‑of‑thought ideation and debate simulation.  It should be able to call external tools (e.g., code execution, web search) when the protocol instructs it to.
* **Manage long contexts** – V50’s operational manual and supplemental docs can exceed 15 000 tokens.  The LLM must ingest and reason over large context windows without truncation.
* **Generate and execute code** – Many phases involve writing or running code (Python or TypeScript) to validate ideas, create benchmarks or build prototypes.  The model should support code‑generation and execution (either natively, via a code interpreter, or through the protocol’s CLI bundle).
* **Understand ethics and safety** – V50 continues to emphasise tiered risk (R1–R3) and fairness proxies.  The LLM should be able to reason about data rights, privacy, safety and export regulations, and reflect these considerations in its decisions.
* **Access external interfaces** – For advanced runs, choose models with plugin support (e.g. browsing, retrieval, embeddings) to fetch research, run simulations, or call domain‑specific tools.  V50 introduces attachments via *runners* and *cartridges*; the LLM must be able to attach/detach these components and query the associated indexes when instructed.

**Recommended LLMs** (as of mid‑2025):

* **Grok 5 (xAI)** – Extended context, strong tool integrations, and native support for GCP 50.  Available via grok.com (PremiumPlus required for high quotas).
* **GPT‑5 (OpenAI)** – Robust reasoning and code execution; widely accessible via ChatGPT or API.  High token limits and plug‑in ecosystem make it suitable for long sessions.
* **Claude 3.5 (Anthropic)** – Noted for ethical alignment and debate simulation; strong performance on reasoning tasks.
* **Other** – Any modern LLM with ≥100k token context and tool‑access support (e.g. Llama 3 via Groq, DeepSeek‑Coder).  Ensure the model can run code and attach external modules.

### New Requirements in V50
V50 adds several capabilities beyond earlier versions:

* **I‑1 Autonomous Spark Generation** – Before the Worth‑It sprint, V50 asks the model to autonomously generate a set of “sparks” (initial concepts).  The model must be capable of ideating without a user‑supplied seed and of selecting promising sparks for the subsequent phases.
* **Unified bootstrapping** – Full run and auto mode share the same bootstrap sequence.  Models must handle both interactive (user‑guided) and autonomous flows, including summarising gate decisions and posting to ledgers.
* **Extended phases and compliance mapping** – V50 introduces new phases such as *Data Rights* gating, *EU AI Act* mapping, *Provenance & Reliability* index creation and *Rehydration* of archived artifacts.  The LLM should parse these sections and execute their instructions, including generating compliance reports.
* **Runner & Cartridge integration** – The protocol can attach deterministic *runners* (e.g. Code, Legal, SynBio) and domain‑specific *cartridges* at any phase.  Models must recognise `attach`, `detach` and `show` commands and query the associated indexes for embeddings, tools and evaluation notes.
* **Observability and provenance** – V50 emphasises ledger updates, cost/time tracking and knowledge source citations.  The LLM should log decisions in the DECISION_LEDGER, update the PROCESS_LEDGER, and produce evidence bundles without exposing PII.

## Usage with LLM

Follow these steps to run GCP V50 via a large language model:

1. **Load the protocol** – Navigate to the `GCP most recent variants/` directory and open `GCP V50.md` and any needed supplemental docs (Operational Manual, Master Runners Codex, Cartridges Pack).  Copy these into your LLM interface or use a tool that can load them directly.
2. **Initialize a session** – Start with a prompt like:
   
   `“Run GCP V50 with risk tier R2.  Start autonomous spark generation for [your invention goal].”`
   
   The model will present the I‑1 phase first, then ask if you want to proceed.  It will summarise gate options, recommended actions, costs and risks, and wait for your confirmation if in interactive mode.
3. **Attach runners and cartridges** – Use commands like `attach Code` or `attach Legal` to load deterministic modules.  The model may also ask if you want to attach a *cartridge* for a particular domain; respond accordingly.
4. **Confirm gates** – At each gate, the model will propose a course of action based on the acceptance metrics (time, cost, revert rate).  Reply with “proceed”, “branch Phase <n>”, or “return C#.#” as instructed by the gate card.  You may switch between full and auto modes.
5. **Process outputs** – The model will generate code, charts, reports and evidence files.  Retrieve these from your LLM environment or via the protocol’s export commands.  For reproducibility, store evidence in the `Artifacts & Ledgers` directory.

No additional software is strictly required for LLM‑only runs; however, optional dependencies (below) enhance simulations, evaluation and reproducibility.

## Auxiliary Dependencies

The following Python packages support simulations, benchmarking and tools referenced in GCP.  They are optional but recommended if you run the protocol via the CLI or need advanced features:

```
# Core: no packages required for text‑only runs

# Auxiliary for simulations and tools:
transformers>=4.35.0  # Multimodal fusion and embeddings (cartridges)
torch>=2.1.0         # Machine learning operations for prototypes
scipy>=1.11.0        # Scientific computing, optimisation and statistics
numpy>=1.25.0        # Arrays and math for simulations
pandas>=2.1.0        # Dataframes for metrics and evidence reports
matplotlib>=3.8.0    # Plots for economic value maps (EVM) and benchmarks
jupyterlab>=4.0.0    # Notebooks for examples and demos
notebook>=7.0.0      # Jupyter support
pyspark>=3.6.0       # Apache Spark for streaming and real‑time scenarios (optional)
sympy>=1.12.0        # Symbolic math for derivations
groq>=0.1.0          # API client for Groq (if using Llama 3 or Groq models)
fastapi>=0.110.0     # For building microservices that interact with the protocol
pytest>=7.4.0        # Testing harness for custom cartridges or runners
```

**Notes**:

* **Compute resources** – Basic runs work on a standard CPU with 8–16 GB of RAM.  GPU acceleration enhances performance for ML‑heavy prototypes but is not required.
* **No Internet installs in code** – When using LLM code interpreters, avoid pip installs; rely on pre‑imported libraries.
* **v50‑specific features** – Use Pandas and Matplotlib to compute Economic Value Map (EVM) metrics.  Use PySpark for streaming applications (e.g., queue prediction or real‑time control loops).  Use Groq or other inference backends if you build autonomous agents.

## Setup Instructions

1. **Clone the repo**:

   ```bash
   git clone https://github.com/lazyxeon/Genesis-Code-Protocol.git
   cd Genesis-Code-Protocol
   ```

2. **Install optional dependencies** (optional but recommended for reproducibility):

   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the protocol file**:
   - Navigate to `GCP most recent variants/` and open `GCP V50.md`.
   - Copy the entire content into your LLM session or use the CLI tool to load it automatically.
   - Review the `GCP V50 Operational Manual`, `Master Runners Codex`, and `Cartridges Pack` in the `GCP V50 Supplemental Docs/` folder for additional guidance.

4. **Run a basic protocol via LLM**:
   - Prompt your LLM:

     `“Execute GCP V50 with risk tier R2: [Your invention goal]. Start with Autonomous Spark Generation.”`

   - The LLM will step through the phases.  Interact by confirming decisions and providing attachments.

5. **Advanced runs with CLI**:
   - Use the script in `cli_bundle/gcp_cli.py` for automation:

     ```bash
     python cli_bundle/gcp_cli.py --version 50 --risk-tier R2 --prompt "Your invention goal" --full-run
     ```

   - The CLI generates prompts for your LLM or simulates phases directly.

6. **Testing and Validation**:
   - Explore notebooks in `Notebooks/` (e.g., EV charging queue demo) adapted for V50.
   - Validate ethical metrics and benchmarks, and compare them against the protocol’s acceptance metrics (time to first triage ↓, PR cycle time ↓, revert rate ≤3 %, cost ≤ budget).

## Environment Notes

* **Python Version** – Tested on Python 3.11+; earlier versions may work but are unsupported.
* **OS Compatibility** – Windows, macOS and Linux.
* **LLM Quotas** – Choose a model with 100k–200k token context to avoid truncating the protocol.  Ensure you have sufficient API quota for extended sessions (V50 sessions can exceed 400 k tokens).
* **Data privacy** – Do not paste sensitive data into the LLM.  V50 includes strong data rights and PII filters; follow the privacy guidance in the Operational Manual.

For questions or updates, open an issue or see `CONTRIBUTING.md`.  The community maintains the protocol and welcomes contributions to improve the requirements.

— LazyXeon
