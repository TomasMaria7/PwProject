from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm

def pagina_inicial(request):
    return render(request, 'portfolio/pagina_inicial.html')


def sobre(request):
    return render(request, 'portfolio/sobre.html')

def projetos(request):
    return render(request, 'portfolio/projetos.html')

def contato(request):
    return render(request, 'portfolio/contato.html')

def registro_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('portfolio:pagina_inicial')
    else:
        form = UserForm()
    return render(request, 'portfolio/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('portfolio:pagina_inicial')
            else:
                messages.error(request, 'Credenciais inválidas')
    else:
        form = AuthenticationForm()
    return render(request, 'portfolio/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('portfolio:pagina_inicial')