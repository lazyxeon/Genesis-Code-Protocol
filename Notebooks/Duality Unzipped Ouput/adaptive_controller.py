class AdaptiveController:
    def __init__(self, buf_ms=20, parity=0.03, lte_cap_mb_day=200):
        self.b = float(buf_ms)
        self.p = float(parity)
        self.lte_cap_mb_day = lte_cap_mb_day
        self.j_fast = 0.0
        self.j_slow = 0.0
        self.alpha_fast = 0.2
        self.alpha_slow = 0.05

    def update_jitter(self, jitter_sample_ms):
        self.j_fast = (1-self.alpha_fast)*self.j_fast + self.alpha_fast*abs(jitter_sample_ms)
        self.j_slow = (1-self.alpha_slow)*self.j_slow + self.alpha_slow*abs(jitter_sample_ms)

    def step(self, loss_in_last_20, gap_ms, cpu_pct):
        target_b = self.b
        if self.j_fast > 12: target_b += 2
        elif self.j_fast < 6: target_b -= 1
        target_b = max(15, min(30, target_b))
        delta_b = target_b - self.b
        delta_b = max(min(delta_b, 2), -1)
        self.b = round(self.b + delta_b, 3)

        target_p = self.p
        if loss_in_last_20 >= 2 or self.j_fast > 10: target_p += 0.01
        elif loss_in_last_20 == 0 and self.j_slow < 6: target_p -= 0.01
        target_p = max(0.0, min(0.10, target_p))
        dp = target_p - self.p
        dp = max(min(dp, 0.01), -0.01)
        self.p = round(self.p + dp, 4)

        if cpu_pct > 80:
            self.p = max(0.0, self.p - 0.02)
            self.b = max(15.0, self.b - 2.0)

        lte_active = gap_ms >= 120
        return {"buffer_ms": self.b, "parity": self.p, "lte_active": lte_active}
