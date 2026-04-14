from protocols.base_protocol import BaseProtocolHandler
from scapy.all import raw

class ModbusHandler(BaseProtocolHandler):
    def process(self, packet):
        try:
            payload = raw(packet['TCP'].payload)
            if len(payload) > 7:
                # Modbus TCP ADU header is 7 bytes; Function code is the 8th byte
                function_code = payload[7]
                self.analyzer.analyze_modbus_anomaly(function_code)
        except Exception:
            pass
