from protocols.mqtt_handler import MQTTHandler
from protocols.modbus_handler import ModbusHandler
from core.analyzer import Analyzer

class ProtocolParser:
    def __init__(self):
        self.analyzer = Analyzer()
        self.handlers = {
            1883: MQTTHandler(self.analyzer),
            502: ModbusHandler(self.analyzer)
        }

    def parse(self, packet):
        if packet.haslayer('TCP'):
            src_port = packet['TCP'].sport
            dst_port = packet['TCP'].dport

            if src_port in self.handlers:
                self.handlers[src_port].process(packet)
            elif dst_port in self.handlers:
                self.handlers[dst_port].process(packet)
