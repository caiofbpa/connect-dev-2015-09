from unittest import TestCase
from core.caixa import CaixaEletronico


class CaixaEletronicoTests(TestCase):
    def test_sacar(self):
        gateway = GatewayDuble()
        gateway.salvar_notas([5, 2, 1])
        caixa = CaixaEletronico(gateway)
        self.assertEquals(caixa.sacar(1), {1: 1})
        self.assertEquals(caixa.sacar(2), {2: 1})
        self.assertEquals(caixa.sacar(3), {2: 1, 1: 1})
        self.assertEquals(caixa.sacar(4), {2: 2})
        self.assertEquals(caixa.sacar(5), {5: 1})

    def test_sacar_desordenado(self):
        gateway = GatewayDuble()
        gateway.salvar_notas([2, 5, 1])
        caixa = CaixaEletronico(gateway)
        self.assertEquals(caixa.sacar(1), {1: 1})
        self.assertEquals(caixa.sacar(2), {2: 1})
        self.assertEquals(caixa.sacar(3), {2: 1, 1: 1})
        self.assertEquals(caixa.sacar(4), {2: 2})
        self.assertEquals(caixa.sacar(5), {5: 1})


class GatewayContractTests(TestCase):
    def setUp(self):
        self.gateway = GatewayDuble()

    def test_vazio(self):
        self.gateway.salvar_notas([])
        self.assertEquals([], self.gateway.obter_notas())

    def test_uma_nota(self):
        self.gateway.salvar_notas([1])
        self.assertEquals([1], self.gateway.obter_notas())

    def test_duas_notas(self):
        self.gateway.salvar_notas([1, 2])
        self.assertEquals([1, 2], self.gateway.obter_notas())


class GatewayDuble(object):
    def salvar_notas(self, notas):
        self.notas = notas

    def obter_notas(self):
        return self.notas
