import argparse, numpy as np, pandas as pd, os

def simulate_trace(duration_s=60, pps=200, seed=42,
                   jitter_sigma_ms=3.0, spike_sigma_ms=20.0, spike_prob=0.05,
                   outage_rate_per_min=4, outage_min_ms=150, outage_max_ms=400):
    rng = np.random.default_rng(seed)
    n = int(duration_s * pps)
    base_interval = 1.0 / pps
    jitter = rng.normal(0, jitter_sigma_ms/1000.0, n)
    spikes = rng.random(n) < spike_prob
    jitter[spikes] += rng.normal(0, spike_sigma_ms/1000.0, spikes.sum())
    send_times = np.arange(n) * base_interval
    arrival_times = send_times + jitter
    num_outages = rng.poisson(outage_rate_per_min * duration_s / 60.0)
    lost = np.zeros(n, dtype=bool)
    for _ in range(num_outages):
        start = rng.uniform(0, duration_s - (outage_max_ms/1000))
        length = rng.uniform(outage_min_ms/1000.0, outage_max_ms/1000.0)
        lost |= (arrival_times >= start) & (arrival_times <= start + length)
    arrival_times[lost] = np.nan
    return send_times, arrival_times, lost

def jitter_stats(times):
    valid = ~np.isnan(times)
    t = times[valid]
    if len(t) < 3:
        return {"p50_ms": float("nan"), "p95_ms": float("nan")}
    d = np.diff(t)
    jitter = np.abs(d - np.median(d))
    return {"p50_ms": float(np.percentile(jitter, 50)*1000), "p95_ms": float(np.percentile(jitter, 95)*1000)}

def apply_jitter_buffer(send_times, arrival_times, buffer_ms=25):
    buf = buffer_ms / 1000.0
    out = np.full_like(arrival_times, np.nan, dtype=float)
    scheduled = send_times + buf
    for i, a in enumerate(arrival_times):
        if not np.isnan(a):
            out[i] = max(a, scheduled[i])
    return out

def sliding_window_still_lost_after_fec(lost, window_packets=20, parity_rate=0.05):
    n = len(lost)
    k = int(np.ceil(parity_rate * window_packets))
    if k == 0:
        return lost.copy()
    still = lost.copy()
    for start in range(0, n, window_packets):
        end = min(n, start + window_packets)
        win = lost[start:end]
        loss_idx = np.where(win)[0]
        if loss_idx.size <= k:
            still[start:end] = False
        else:
            still[start:end] = False
            keep = loss_idx[k:]
            still[start + keep] = True
    return still

def long_gap_mask_from_original(lost, pps, threshold_ms=120):
    mask = np.zeros_like(lost)
    i = 0
    while i < len(lost):
        if lost[i]:
            j = i
            while j+1 < len(lost) and lost[j+1]:
                j += 1
            duration_ms = (j - i + 1)/pps * 1000.0
            if duration_ms >= threshold_ms:
                mask[i:j+1] = True
            i = j + 1
        else:
            i += 1
    return mask

def run_variant(send, arr, lost, variant, pps=200,
                buffer_ms=15, parity_rate=0.05, gap_ms=120, lte=True):
    if variant == "baseline":
        jit = jitter_stats(arr)
        return {
            "variant": variant,
            "jitter_p95_ms": jit["p95_ms"],
            "loss_pct": float(np.mean(np.isnan(arr))*100),
            "overhead_pct": 0.0,
            "added_latency_p95_ms": 0.0
        }

    out = apply_jitter_buffer(send, arr, buffer_ms=buffer_ms)
    still_after_fec = sliding_window_still_lost_after_fec(lost, window_packets=20, parity_rate=parity_rate)
    lte_recovery = np.zeros_like(lost)

    if variant in ("duality_dual",) and lte:
        long_gaps = long_gap_mask_from_original(lost, pps, threshold_ms=gap_ms)
        i = 0
        while i < len(long_gaps):
            if long_gaps[i]:
                j = i
                while j+1 < len(long_gaps) and long_gaps[j+1]:
                    j += 1
                if j > i:
                    lte_recovery[i+1:j+1] = True
                i = j + 1
            else:
                i += 1

    still_after = still_after_fec & ~lte_recovery
    recovered = lost & ~still_after
    out[recovered] = send[recovered] + buffer_ms/1000.0

    jit = jitter_stats(out)
    parity_overhead_pct = parity_rate * 100.0
    lte_overhead_pct = (float(lte_recovery.sum()) / len(lost) * 100.0) if variant == "duality_dual" else 0.0

    return {
        "variant": variant,
        "jitter_p95_ms": jit["p95_ms"],
        "loss_pct": float(still_after.mean()*100.0),
        "overhead_pct": float(parity_overhead_pct + lte_overhead_pct),
        "added_latency_p95_ms": float(buffer_ms)
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sweep", action="store_true")
    ap.add_argument("--out-details", default="04_benchmarks/results/S49_extended_details.csv")
    ap.add_argument("--out-summary", default="04_benchmarks/results/S49_extended_summary.csv")
    args = ap.parse_args()

    families = {
        "cable_ftth_evening": dict(jitter_sigma_ms=3.0, spike_sigma_ms=20.0, spike_prob=0.05,
                                   outage_rate_per_min=4, outage_min_ms=150, outage_max_ms=400),
        "rural_dsl_tails": dict(jitter_sigma_ms=7.0, spike_sigma_ms=35.0, spike_prob=0.08,
                                outage_rate_per_min=3, outage_min_ms=200, outage_max_ms=450),
        "wifi_contention": dict(jitter_sigma_ms=5.0, spike_sigma_ms=30.0, spike_prob=0.15,
                                outage_rate_per_min=2, outage_min_ms=100, outage_max_ms=220),
        "leo_satellite_like": dict(jitter_sigma_ms=6.0, spike_sigma_ms=60.0, spike_prob=0.07,
                                   outage_rate_per_min=1, outage_min_ms=300, outage_max_ms=600),
    }

    variants = [
        ("baseline", {"buffer_ms": 0, "parity_rate": 0.0, "lte": False}),
        ("duality_single", {"buffer_ms": 15, "parity_rate": 0.07, "lte": False}),
        ("duality_dual", {"buffer_ms": 15, "parity_rate": 0.05, "lte": True}),
    ]

    rows = []
    seeds = list(range(1, 21))
    for fam, params in families.items():
        for seed in seeds:
            send, arr, lost = simulate_trace(seed=seed, **params)
            for variant_name, cfg in variants:
                res = run_variant(send, arr, lost, variant_name,
                                  buffer_ms=cfg["buffer_ms"],
                                  parity_rate=cfg["parity_rate"],
                                  lte=cfg["lte"])
                res.update({"family": fam, "seed": seed})
                rows.append(res)

    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(args.out_details), exist_ok=True)
    df.to_csv(args.out_details, index=False)

    summary = df.groupby(["family", "variant"]).agg(
        jitter_p95_ms_mean=("jitter_p95_ms", "mean"),
        loss_pct_mean=("loss_pct", "mean"),
        overhead_pct_mean=("overhead_pct", "mean"),
        added_latency_p95_ms=("added_latency_p95_ms", "mean"),
    ).reset_index()
    summary["accept_latency"] = summary["added_latency_p95_ms"] <= 15.0
    summary["accept_overhead"] = summary["overhead_pct_mean"] <= 10.0
    summary["verdict"] = np.where(summary["accept_latency"] & summary["accept_overhead"], "PASS", "CHECK")
    summary.to_csv(args.out_summary, index=False)

if __name__ == "__main__":
    main()
