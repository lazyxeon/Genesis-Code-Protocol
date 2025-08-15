# Requirements for Running GCP (Genesis Code Protocol)

This document outlines the core requirements for running the GCP, with a focus on v48. GCP is primarily an LLM-interpreted framework, meaning the protocol logic is executed by pasting or feeding the protocol content (e.g., from `GCP V48.md`) into a capable large language model (LLM). The LLM handles orchestration, phase progression, recursion, and invention generation.

However, to support auxiliary tools, simulations, benchmarking, and real-time features (e.g., Apache Spark integration in v48 for streaming applications like EV charging optimization), additional dependencies are recommended. These are optional for basic runs but essential for full functionality, such as code execution, data processing, and continuous assurance.

## Core Requirements

### LLM Capabilities
GCP v48 requires an LLM with:
- **Strong Reasoning and Tool-Calling**: Supports structured phase progression, Tree-of-Thought (ToT) ideation, debate simulation, and recursion. Models like Grok 4, GPT-5 (or equivalent), Claude 3.5, or similar are ideal.
- **Long Context Handling**: Processes large protocol documents (~10k+ tokens) without truncation.
- **Code Generation and Execution**: Capable of writing, simulating, and validating code (e.g., Python for benchmarks).
- **Ethical and Safety Awareness**: Handles ontological proxies, fairness deltas, and risk-tiered execution natively.
- **API or Interface Access**: For advanced runs, use LLMs with tool integration (e.g., web search, code interpreter) to enhance discovery and validation phases.

**Recommended LLMs**:
- **Grok 4 (xAI)**: Optimized for GCP due to native tool support and reasoning depth. Access via grok.com or X apps (PremiumPlus required for full quotas).
- **GPT-5 (OpenAI)**: Excellent for orchestration; use via ChatGPT or API.
- **Claude 3.5 (Anthropic)**: Strong in ethical alignment and debate simulation.
- **Other**: Any LLM supporting tool access (e.g., Llama 3 via Groq or Hugging Face).

**Usage with LLM**:
1. Load the protocol file (e.g., `GCP V48.md`) into your LLM interface.
2. Start with a prompt like: "Run GCP v48 with risk tier R2: [Your invention goal, e.g., 'Invent a real-time EV charging queue optimizer']. Assess worth-it and proceed phase-by-phase."
3. Confirm progress (e.g., reply "Y" at gates) and handle outputs (e.g., generated code, benchmarks).
4. For realism features: Include EVM assessments and non-tech alternatives in prompts.

No additional software is strictly required for LLM-only runs, but for reproducibility and simulations, see below.

## Auxiliary Dependencies

These Python packages support simulations, benchmarking, data processing, and tools referenced in GCP (e.g., for v48's Spark integration, ethical audits, or invention validation). Install via `pip install -r requirements.txt` in the repo root.

### requirements.txt Content
```
# Core for LLM interpretation: None required (protocol is text-based)

# Auxiliary for simulations, tools, and v48 features:
transformers>=4.30.0  # For multimodal fusion (v11+) and NLP tasks
torch>=2.0.0  # ML operations, tensors (e.g., agentic layers)
scipy>=1.10.0  # Scientific computing, stats for benchmarks
numpy>=1.23.0  # Arrays, math for simulations
pandas>=1.5.0  # Data handling, CSVs for reports
matplotlib>=3.6.0  # Plots for metrics (e.g., EVM charts)
jupyterlab>=3.6.0  # Notebooks for demos
notebook>=6.5.0  # Jupyter support
pyspark>=3.5.0  # Apache Spark for real-time/streaming (v48 EV runs)
sympy>=1.12.0  # Symbolic math for derivations
networkx>=3.3  # Graphs for ToT and topology
rdkit>=2023.9.1  # Chemistry simulations (domain-specific)
biopython>=1.83  # Biology tools (if needed)
astropy>=6.1.0  # Physics/astronomy simulations
pygame>=2.6.0  # Game dev prototypes
```

**Notes**:
- **CPU/GPU**: Basic runs work on CPU (>=1.14 recommended for compatibility). GPU acceleration (e.g., CUDA for Torch) enhances ML-heavy inventions.
- **No Internet/Installs in Code**: When using code interpreters in LLMs, avoid pip installs; rely on pre-imported libs.
- **v48-Specific**: For realism (e.g., EVM calculations), use Pandas/Matplotlib. Spark for streaming features like queue prediction.

## Setup Instructions

1. **Clone the Repo**:
   ```
   git clone https://github.com/lazyxeon/Genesis-Code-Protocol-.git
   cd Genesis-Code-Protocol-
   ```

2. **Install Dependencies** (optional but recommended):
   ```
   pip install -r requirements.txt
   ```

3. **Prepare Protocol File**:
   - Navigate to `GCP most recent variants/` and select `GCP V48.md`.
   - Copy the content into your LLM (e.g., Grok chat).

4. **Run a Basic Protocol**:
   - Prompt your LLM: "Execute GCP v48: [Prompt]. Start with Phase -1 worth-it assessment."
   - Interact as needed (e.g., confirm gates).

5. **Advanced Runs with CLI**:
   - Use `CLI Bundle/gcp_cli.py` for automation:
     ```
     python CLI\ Bundle/gcp_cli.py --version 48 --risk-tier R2 --prompt "Your invention goal" --full-run
     ```
   - This generates prompts for LLM pasting or simulates phases.

6. **Testing & Validation**:
   - Run notebooks in `Notebooks/` for examples (e.g., EV charging demo).
   - Verify ethical metrics and benchmarks match protocol outputs.

## Environment Notes

- **Python Version**: 3.10+ (tested up to 3.12.3).
- **OS Compatibility**: Windows, macOS, Linux.
- **Compute Resources**: Basic: 4GB RAM, standard CPU. Advanced (e.g., Spark): 16GB+ RAM, multi-core.
- **LLM Quotas**: Use models with high token limits (e.g., Grok 4 for 128k+ context).

If dependencies change (e.g., for new variants), update via PR. For questions, see CONTRIBUTING.md.

— LazyXeon
