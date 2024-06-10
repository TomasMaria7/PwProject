from django.shortcuts import render
from praias.models import Praia

def praias_view(request):
    praias_por_regiao = {}
    praias = Praia.objects.select_related('regiao').all()
    for praia in praias:
        if praia.regiao.nome not in praias_por_regiao:
            praias_por_regiao[praia.regiao.nome] = []
        praias_por_regiao[praia.regiao.nome].append(praia)
    context = {'praias_por_regiao': praias_por_regiao}
    return render(request, 'praias/praias.html', context)

def praia_view(request, praia_nome):
    praia = Praia.objects.get(nome=praia_nome)
    context = {'praia': praia}
    return render(request, 'praias/praia.html', context)

