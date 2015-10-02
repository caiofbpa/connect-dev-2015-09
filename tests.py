from core.tests import GatewayContractTests
from mysql import GatewayMySQL


class GatewayMySQLTests(GatewayContractTests):
    def setUp(self):
        self.gateway = GatewayMySQL()
