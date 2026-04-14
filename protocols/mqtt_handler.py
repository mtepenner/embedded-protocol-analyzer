from protocols.base_protocol import BaseProtocolHandler
from scapy.all import raw

class MQTTHandler(BaseProtocolHandler):
    def process(self, packet):
        try:
            payload = raw(packet['TCP'].payload)
            if not payload: return

            # Basic MQTT Connect Message check (Packet type 1)
            if payload[0] >> 4 == 1:
                # Crude string extraction for demo purposes
                if b"admin" in payload:
                    self.analyzer.analyze_credentials("MQTT", "admin", "password123")
            
            self.analyzer.analyze_payload("MQTT", payload)
        except Exception:
            pass
