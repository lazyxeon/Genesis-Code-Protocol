# Placeholder flow classifier.
# TODO: Implement process/port allowlists and per-app routing policies.
from dataclasses import dataclass

@dataclass
class FlowPolicy:
    allow: bool = True
    realtime: bool = True

def classify_flow(proto: str, port: int, process_name: str|None=None) -> FlowPolicy:
    realtime_ports = {3478, 3479, 5004, 5005, 27015, 27036}
    if proto.upper() in {"UDP", "QUIC"} and (port in realtime_ports):
        return FlowPolicy(allow=True, realtime=True)
    return FlowPolicy(allow=True, realtime=False)
