{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Adaptive QoS Traffic Manager\n",
        "**Fairness-Based Dynamic Bandwidth Allocator for Starlink**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# AdaptiveQoS: Predictive Fairness-Based Traffic Manager for Starlink\n",
        "\n",
        "\"\"\"\n",
        "This module dynamically allocates bandwidth among Starlink users based on service tier, \n",
        "latency conditions, and a predictive 24-hour demand model. It integrates an alloy-style\n",
        "fairness function that boosts emergency and underserved connections without degrading \n",
        "overall throughput.\n",
        "\"\"\"\n",
        "\n",
        "import math\n",
        "import numpy as np\n",
        "from typing import List, Dict\n",
        "from dataclasses import dataclass\n",
        "\n",
        "@dataclass\n",
        "class UserNode:\n",
        "    user_id: str\n",
        "    service_tier: float  # 1.0 = premium, 0.5 = standard, 0.2 = low-tier\n",
        "    qos_score: float     # From past performance history\n",
        "    current_latency_ms: float\n",
        "    emergency_flag: bool\n",
        "\n",
        "class AdaptiveQoSAllocator:\n",
        "    def __init__(self, total_bandwidth_mbps: float):\n",
        "        self.total_bw = total_bandwidth_mbps\n",
        "        self.alpha = 1.2  # Emergency multiplier\n",
        "        self.beta = 0.8   # Latency penalty coefficient\n",
        "        self.gamma = 0.6  # QoS weight\n",
        "\n",
        "    def _predict_demand_modifier(self, hour):\n",
        "        return 1.0 + 0.4 * math.cos(2 * math.pi * (hour - 18) / 24)\n",
        "\n",
        "    def _user_alloy_score(self, user: UserNode, hour):\n",
        "        base = user.service_tier\n",
        "        latency_penalty = math.exp(-self.beta * user.current_latency_ms / 100)\n",
        "        qos_boost = math.exp(self.gamma * user.qos_score)\n",
        "        demand_mod = self._predict_demand_modifier(hour)\n",
        "        emergency = self.alpha if user.emergency_flag else 1.0\n",
        "        return base * latency_penalty * qos_boost * demand_mod * emergency\n",
        "\n",
        "    def allocate(self, users: List[UserNode], hour: int) -> Dict[str, float]:\n",
        "        scores = {user.user_id: self._user_alloy_score(user, hour) for user in users}\n",
        "        total_score = sum(scores.values())\n",
        "        return {uid: (score / total_score) * self.total_bw for uid, score in scores.items()}\n",
        "\n",
        "# Example simulation\n",
        "if __name__ == \"__main__\":\n",
        "    users = [\n",
        "        UserNode(\"u1\", 1.0, 0.8, 30, False),\n",
        "        UserNode(\"u2\", 0.5, 0.5, 120, True),\n",
        "        UserNode(\"u3\", 0.2, 0.2, 200, False),\n",
        "        UserNode(\"u4\", 0.5, 0.9, 40, False),\n",
        "        UserNode(\"u5\", 0.2, 0.6, 90, True)\n",
        "    ]\n",
        "\n",
        "    allocator = AdaptiveQoSAllocator(total_bandwidth_mbps=100.0)\n",
        "    for hour in range(0, 24, 6):\n",
        "        print(f\"\\nHour: {hour:02d}:00\")\n",
        "        allocs = allocator.allocate(users, hour)\n",
        "        for uid, mbps in allocs.items():\n",
        "            print(f\"  {uid}: {mbps:.2f} Mbps\")"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.10.12"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 4
}
