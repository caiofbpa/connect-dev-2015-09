class CaixaEletronico(object):
    def __init__(self, gateway):
        self.gateway = gateway

    def sacar(self, valor):
        resultado = {}
        notas = self.gateway.obter_notas()
        for nota in sorted(notas, reverse=True):
            while valor >= nota:
                resultado[nota] = resultado.get(nota, 0) + 1
                valor -= nota
        return resultado
