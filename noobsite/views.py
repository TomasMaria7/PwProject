from django.shortcuts import render

# project/views.py

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def nome_view(request):
    return HttpResponse("Olá sou o Tomás")

def cobra_view(request):
    return HttpResponse("Sou o numero a22206963")


