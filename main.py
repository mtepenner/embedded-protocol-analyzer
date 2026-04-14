import argparse
from core.sniffer import Sniffer
from utils.logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Embedded Protocol Analyzer")
    parser.add_argument("-i", "--interface", help="Network interface to sniff on", default="eth0")
    parser.add_argument("-f", "--file", help="PCAP file to analyze offline")
    args = parser.parse_args()

    logger = setup_logger()
    logger.info("Starting Embedded Protocol Analyzer...")

    sniffer = Sniffer(interface=args.interface, pcap_file=args.file)
    sniffer.start()

if __name__ == "__main__":
    main()
