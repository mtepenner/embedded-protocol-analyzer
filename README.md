# Embedded Protocol Analyzer 🕵️‍♂️📡

A Python-based network protocol analyzer specifically designed for embedded systems and IoT environments. This tool monitors network traffic, parses industrial and IoT protocols (MQTT, Modbus TCP), and detects potential security anomalies using signature-based rules.

## 📑 Table of Contents
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration & Rules](#-configuration--rules)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Features
* **Live Traffic Sniffing:** Capture and analyze packets in real-time from a specified network interface.
* **Offline PCAP Analysis:** Ingest and parse pre-recorded `.pcap` files for forensic analysis.
* **Protocol Support:** Dedicated handlers for IoT and industrial protocols:
  * **MQTT (Port 1883):** Analyzes generic payloads and detects exposed, unencrypted credentials.
  * **Modbus TCP (Port 502):** Inspects payloads for suspicious or unauthorized function codes.
* **Signature-Based Detection:** Compares packet payloads against a customizable JSON signature file to flag malicious strings (e.g., SQL injection, shell commands) and default passwords.
* **Logging & Exporting:** Comprehensive logging system with CSV export capabilities for detected alerts.

## 🛠️ Technologies Used
* **Python 3.x**
* **Scapy:** For robust packet manipulation and sniffing.
* **PyYAML:** For parsing configuration files.

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mtepenner/embedded-protocol-analyzer.git
   cd embedded-protocol-analyzer
   ````

2.  **Set up a virtual environment (Optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *Note: Packet sniffing with Scapy may require elevated (root/administrator) privileges depending on your operating system.*

## 💻 Usage

Run the tool using the `main.py` entry point. You can choose to analyze live traffic or read from a `.pcap` file.

**Analyze Live Traffic:**

```bash
# Requires root privileges on Unix-based systems
sudo python main.py -i eth0
```

**Analyze Offline PCAP File:**

```bash
python main.py -f traffic_capture.pcap
```

**Command-line Arguments:**

  * `-i`, `--interface`: Network interface to sniff on (default: `eth0`).
  * `-f`, `--file`: Path to a PCAP file for offline analysis.

## 📝 Configuration & Rules

The analyzer's behavior and detection capabilities can be customized without altering the code.

### Signatures (`rules/signatures.json`)

Add or modify detection rules in this file. It currently supports:

  * `generic_malicious_strings`: Byte strings to flag in payloads (e.g., `DROP TABLE`, `/bin/sh`).
  * `default_passwords`: Common default credentials to watch for.
  * `suspicious_modbus_functions`: Modbus function codes that should trigger an alert (e.g., `90`, `43`).

### Configuration (`rules/config.yaml`)

Control network filtering and logging output levels:

```yaml
network:
  default_interface: eth0
  bpf_filter: "tcp port 1883 or tcp port 502"
logging:
  level: INFO
  file: "data/logs/analyzer.log"
```

## 📂 Project Structure

```text
embedded-protocol-analyzer/
├── core/
│   ├── analyzer.py       # Detection logic and signature matching
│   ├── parser.py         # Packet routing to protocol handlers
│   └── sniffer.py        # Scapy ingestion (live or pcap)
├── protocols/
│   ├── base_protocol.py  # Base class for handlers
│   ├── modbus_handler.py # Modbus TCP parsing
│   └── mqtt_handler.py   # MQTT parsing
├── rules/
│   ├── config.yaml       # App configuration
│   └── signatures.json   # Threat detection signatures
├── utils/
│   ├── export.py         # CSV export utility
│   └── logger.py         # Logging configuration
├── main.py               # Application entry point
└── requirements.txt      # Python dependencies
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\!

1.  Fork the project.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE]
