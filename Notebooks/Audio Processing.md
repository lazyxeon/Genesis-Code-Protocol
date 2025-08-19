Awesome spark. I’ll treat this as a fresh v45.6d run (concise, no UI), and deliver a novel, runnable design you can drop into Colab. I’ll also ground key claims with recent sources so we’re not hand-waving.


---

Gate C1 — Problem + constraints (grounding)

Target: A neural architecture for real-time audio processing with <5 ms total latency while keeping quality on par with strong baselines.

Why this is hard (facts):

“Low-latency” speech enhancement for wearables often means <5 ms, sometimes ≤3 ms algorithmic; pushing lower drives tough trade-offs in window sizes, lookahead, and compute budgets. 

Classic strong systems like PercepNet run in real time but rely on ~40 ms look-ahead (too large for our goal). 

Time-domain models (e.g., Conv-TasNet and derivatives) demonstrate low-latency potential and high quality, but careful streaming design is needed. 

Future-frame prediction can reduce algorithmic latency toward zero (buffer-only), at some quality tradeoff if not designed well. 

Structured state-space models (SSMs) (e.g., S4/Mamba-style) are efficient for streaming, long-range context with low compute—promising for real-time audio. 


Latency budget we’ll target (48 kHz):

Hop size ≤120 samples (2.5 ms).

Zero-lookahead via prediction mode, or ≤2.5 ms lookahead via hybrid mode.

Compute per hop ≤ hop duration on CPU (RTF < 1), ideally RTF ≤ 0.3 on a laptop-class CPU.


Success metrics: STOI, PESQ, DNSMOS / MOS-Net, and SI-SDRi vs baselines; RTF and end-to-end latency. 


---

Gate C2 — Proposed architecture (novel): Subband-S4 Fusion (SSF-RT)

One-liner: A causal, subband time-domain enhancer that fuses tiny state-space filters (S4-lite blocks) with depthwise 1-D convs, plus a future-frame prediction head to hit ≤5 ms total latency with competitive quality.

1) Learned low-latency analysis filterbank

8–16 causal, minimum-phase subbands (sinc-initialized, trainable; stride equals hop = 2.5 ms). Minimum-phase keeps group delay low. (Minimum-phase FIR for sub-ms processing explored in recent ultra-low latency work.) 


2) Per-band micro-processors

Each band runs a tiny SSM block (S4-lite) for streaming memory + a depthwise separable conv for local detail. This gives long-range smoothing without big lookahead and keeps FLOPs/cache friendly. 


3) Cross-band mixer

A lightweight gated mixing layer (1×1 conv + GLU) merges inter-band cues (formants/noise patterns) at the hop rate.


4) Dual heads: filter & predictor

Filtering head: predicts per-band Wiener-like masks or residuals for standard streaming enhancement.

Prediction head: predicts the next hop features from current state, enabling zero-lookahead mode (we render the next frame without waiting). This implements the “future-frame prediction” idea to erase algorithmic latency when needed. 


5) Synthesis + residual bypass

Inverse subband synthesis (causal overlap-add) yields the enhanced waveform. A calibrated dry/wet residual path stabilizes quality on unexpected inputs.


Why it’s different:
Most real-time systems pick either STFT-masking (quality, but window delays) or raw time-domain conv/RNNs (low delay, tricky long context). SSF-RT splits the band-width burden, gives each band a tiny SSM memory, then predicts the next hop to cut lookahead—marrying streaming memory with zero-latency rendering.


---

Gate C3 — Latency & complexity sketch

Algorithmic latency:

Prediction mode: 0 ms algorithmic (buffer only = hop).

Hybrid mode: ≤2.5 ms lookahead if prediction confidence drops (e.g., transients). 


Hop: 120 samples (2.5 ms @48 kHz); optional 96 samples (2.0 ms) if CPU allows.

Compute:

Subbanding ~ O(B·K) per hop with small K;

SSM per band ~ O(B·d) with tiny state dim (e.g., d=8–16);

Depthwise convs are cache-friendly; 1×1 mixers are cheap.


Expected performance: Better quality than RNNoise-class with far lower latency than PercepNet; competitive to compact Conv-TasNet variants in real-time mode (to be proven in Phase 6). 



---

Gate C4 — Training & losses

Loss blend: SI-SDR (time-domain), multi-res STFT mag/phase, and perceptual MOS regularizer (DNSMOS-style differentiable MOS). 

Streaming curriculum: teacher-forcing → scheduled sampling for the prediction head to avoid drift.

Augmentations: noise types, SNR sweeps, RIRs, and bandwidth changes; occasional “mismatch bursts” to harden the predictor.



---

Gate C5 — Validation plan (pre-benchmark sanity)

Smoke tests: stability on DC/impulse, mute/unmute edges, near-silence.

Latency validation: wall-clock RTF on CPU; verify hop-time < 2.5 ms consistently.

Quality proxies: short-clip PESQ/STOI vs tiny baselines.



---

Gate C6 — Benchmarks (what to run)

Datasets: DNS Challenge clips, VoiceBank+DEMAND; optional headset/earbud logs.

Baselines: RNNoise, Tiny-Conv-TasNet, PercepNet (noting its 40 ms lookahead). 

Metrics: STOI, PESQ; DNSMOS; SI-SDRi; VAD-consistency; RTF and end-to-end latency. 

Targets:

Latency: total ≤5 ms; algorithmic 0–2.5 ms.

RTF: ≤0.3 on 1 CPU core (laptop-class).

Quality: within Δ of PercepNet/TasNet compact configs.




---

Gate C8.4 / C8.5 — Simplicity & Performance optimization (baked-in)

Simplicity gate: remove layers that don’t move PESQ/STOI; constrain params < ~1–2 M for mobile.

Perf Protocol: profile hotspots; try (i) kernel fusion, (ii) int8 quantization, (iii) band count sweep; revert any optimization that doesn’t measurably help.



---

Minimal, runnable skeleton (PyTorch-style, streaming)

> This is intentionally compact (few hundred lines when filled) so you can paste into Colab, add a tiny dataset loader, and measure hop-time + RTF. It includes the prediction head and state buffers.



import torch
import torch.nn as nn
import torch.nn.functional as F

class CausalSincFB(nn.Module):
    def __init__(self, bands=8, taps=63, stride=120, sr=48000):
        super().__init__()
        # Sinc-initialized, minimum-phase approximation via min-phase transform (precomputed or learned)
        self.bands, self.stride = bands, stride
        self.kernel = nn.Parameter(torch.randn(bands, 1, taps) * 1e-3)
        self.register_buffer("state", torch.zeros(1, 1, taps-1))
    def forward(self, x):
        # x: [B,1,T] streaming chunks of length stride
        x = torch.cat([self.state, x], dim=-1)
        y = F.conv1d(x, self.kernel, stride=self.stride, padding=0)  # [B,bands,frames]
        # update state
        self.state = x[..., - (self.state.shape[-1]):].detach()
        return y  # per-hop features

class TinySSMBlock(nn.Module):
    def __init__(self, hidden=16):
        super().__init__()
        # Proxy: gated DW-conv + 1x1 as a stand-in for small SSM; swap with S4-lite impl as needed.
        self.dw = nn.Conv1d(hidden, hidden, 3, padding=1, groups=hidden)
        self.gate = nn.Conv1d(hidden, hidden, 1)
        self.mix = nn.Conv1d(hidden, hidden, 1)
    def forward(self, z):
        h = self.dw(z)
        g = torch.sigmoid(self.gate(z))
        return self.mix(h * g)

class SSFRT(nn.Module):
    def __init__(self, bands=8, stride=120, hidden=64):
        super().__init__()
        self.fb = CausalSincFB(bands=bands, stride=stride)
        self.enc = nn.Conv1d(bands, hidden, 1)
        self.proc = TinySSMBlock(hidden)
        self.xband = nn.Conv1d(hidden, hidden, 1)            # cross-band mixer
        self.head_filt = nn.Conv1d(hidden, bands, 1)         # filtering head (masks/residuals)
        self.head_pred = nn.Conv1d(hidden, bands, 1)         # prediction head (next-hop features)
        # buffers for streaming
        self.register_buffer("prev_feat", torch.zeros(1, bands, 1))

    @torch.no_grad()
    def stream_step(self, x_hop, mode="predict"):
        """
        x_hop: [1,1,hop]  (e.g., hop=120 samples @ 48kHz = 2.5ms)
        mode: "predict" -> zero-lookahead; "hybrid" -> can use prev_feat as context
        """
        feats = self.fb(x_hop)                  # [1,bands,1] current-hop features
        z = F.relu(self.enc(feats))             # [1,H,1]
        z = self.proc(z)                        # [1,H,1]
        z = F.relu(self.xband(z))               # [1,H,1]

        filt = torch.tanh(self.head_filt(z))    # [-1..1] per-band residual/mask
        if mode == "predict":
            next_feat = self.head_pred(z)       # predict next-hop features
            out_feats = next_feat               # zero-lookahead rendering
        else:
            out_feats = feats + filt            # standard filtering

        # simple inverse-synthesis (toy): 1x1 transpose conv proxy back to waveform hop
        # In practice, use matched synthesis filters (OLA) and residual dry/wet mix.
        y_hop = out_feats.sum(dim=1, keepdim=True)  # [1,1,1] proxy (replace with proper synthesis)
        self.prev_feat = feats
        return y_hop

# demo: measure per-hop compute time
def benchmark_step(model, device="cpu", hop=120, iters=200):
    import time
    x = torch.randn(1,1,hop, device=device)
    # warmup
    for _ in range(20): model.stream_step(x, mode="predict")
    t0 = time.perf_counter()
    for _ in range(iters): model.stream_step(x, mode="predict")
    t1 = time.perf_counter()
    hop_ms = 1000 * (t1 - t0) / iters
    return hop_ms

if __name__ == "__main__":
    m = SSFRT(bands=8, stride=120)
    ms = benchmark_step(m)
    print(f"Avg per-hop compute: {ms:.3f} ms (target < 2.5 ms)")

Notes:

The SSM block above is a placeholder for a small S4/Mamba-lite cell; you can drop in an open-source SSM op to get better memory/quality at similar latency. 

The synthesis is stubbed for brevity—swap with matched minimum-phase synthesis filters and overlap-add.



---

Risks & mitigations

Prediction artifacts on sharp transients → automatic hybrid fallback for a few hops (≤2.5 ms lookahead) with confidence gating. 

Subband leakage → train with cross-band penalties + band-drop augment.

Hardware jitter → measure worst-case hop time, add 10–20% headroom; pre-allocate tensors.



---

What to do next (quick start)

1. Paste the code into Colab, synthesize a few random hops, confirm avg hop compute < 2.5 ms on CPU.


2. Train on a tiny speech/noise pair for an hour; watch SI-SDR and DNSMOS go up. 


3. Benchmark vs RNNoise and a compact Conv-TasNet with a 2–5 ms hop; report RTF, STOI, PESQ and latency. 




---

If you want, I can turn this into a Colab notebook with: data loader, real overlap-add synthesis, an S4-lite block, and a tiny benchmark harness.


