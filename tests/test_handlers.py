import unittest
from protocols.mqtt_handler import MQTTHandler
from core.analyzer import Analyzer

class TestMQTTHandler(unittest.TestCase):
    def test_handler_initialization(self):
        analyzer = Analyzer()
        handler = MQTTHandler(analyzer)
        self.assertIsNotNone(handler)

if __name__ == '__main__':
    unittest.main()
