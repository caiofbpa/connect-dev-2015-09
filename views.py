from django.shortcuts import render_to_response
from core.caixa import CaixaEletronico
from mysql import GatewayMySQL


def home(request):
    valor = request.GET.get('valor')
    if valor:
        valor = int(valor)
    else:
        valor = 0

    gateway = GatewayMySQL()
    caixa = CaixaEletronico(gateway)
    notas = caixa.sacar(valor)

    return render_to_response('home.html', {'notas': notas, 'valor': valor})
