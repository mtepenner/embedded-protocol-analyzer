import json
import logging

class Analyzer:
    def __init__(self):
        self.logger = logging.getLogger("Analyzer")
        with open("rules/signatures.json", "r") as f:
            self.signatures = json.load(f)

    def analyze_payload(self, protocol, payload):
        for sig in self.signatures.get("generic_malicious_strings", []):
            if sig.encode() in payload:
                self.logger.warning(f"[{protocol}] Malicious payload detected: {sig}")

    def analyze_credentials(self, protocol, username, password):
        if username == "admin" and password in self.signatures.get("default_passwords", []):
            self.logger.warning(f"[{protocol}] Default credentials used: {username}/{password}")
        else:
            self.logger.info(f"[{protocol}] Unencrypted credentials found: {username}/<hidden>")

    def analyze_modbus_anomaly(self, function_code):
        if function_code in self.signatures.get("suspicious_modbus_functions", []):
            self.logger.warning(f"[Modbus] Suspicious Function Code detected: {function_code}")
