# Dataplane placeholders.
# Real implementation should wire QUIC/MP-QUIC sockets and optional MASQUE relays.
class Dataplane:
    def __init__(self):
        self.bytes_sent_lte = 0
        self.bytes_sent_primary = 0

    def send_parity(self, n_bytes: int, via_lte: bool=False):
        if via_lte:
            self.bytes_sent_lte += n_bytes
        else:
            self.bytes_sent_primary += n_bytes

    def stats(self):
        return {
            "bytes_sent_primary": self.bytes_sent_primary,
            "bytes_sent_lte": self.bytes_sent_lte,
        }
