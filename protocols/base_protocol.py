class BaseProtocolHandler:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def process(self, packet):
        raise NotImplementedError("Protocol handlers must implement the process method.")
