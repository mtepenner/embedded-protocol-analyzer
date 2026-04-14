from scapy.all import sniff, rdpcap
from core.parser import ProtocolParser
import logging

class Sniffer:
    def __init__(self, interface=None, pcap_file=None):
        self.interface = interface
        self.pcap_file = pcap_file
        self.parser = ProtocolParser()
        self.logger = logging.getLogger("Analyzer")

    def start(self):
        if self.pcap_file:
            self.logger.info(f"Analyzing PCAP file: {self.pcap_file}")
            packets = rdpcap(self.pcap_file)
            for pkt in packets:
                self.parser.parse(pkt)
        else:
            self.logger.info(f"Sniffing live traffic on interface: {self.interface}")
            sniff(iface=self.interface, prn=self.parser.parse, store=0)
