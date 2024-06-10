from django.shortcuts import render, redirect
from .models import *
from .forms import NoticiaForm, AutorForm, ComentarioForm, UserForm
from django.http import HttpResponseNotFound
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def pagina_inicial(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/pagina_inicial.html', {'noticias': noticias})

def detalhes_noticia(request, nome_noticia):
    noticia = Noticia.objects.get(nome=nome_noticia)
    comentarios = noticia.comentarios.all()
    return render(request, 'noticias/detalhes_noticia.html', {'noticia': noticia, 'comentarios': comentarios})

def detalhes_autor(request, nome_autor):
    autor = Autor.objects.get(nome=nome_autor)
    noticias = autor.noticias.all()
    return render(request, 'noticias/detalhes_autor.html', {'autor': autor, 'noticias': noticias})

def adicionar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('noticias:pagina_inicial')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/adicionar_noticia.html', {'form': form})

def adicionar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('noticias:pagina_inicial')
    else:
        form = AutorForm()
    return render(request, 'noticias/adicionar_autor.html', {'form': form})

def remover_noticia(request, id_noticia):
    noticia = Noticia.objects.get(id=id_noticia)
    if request.method == 'POST':
        noticia.comentarios.all().delete()
        noticia.delete()
        return redirect('noticias:pagina_inicial')
    else:
        return HttpResponseNotFound("Noticia não encontrada.")

def editar_noticia(request, nome_noticia):
    try:
        noticia = Noticia.objects.get(nome=nome_noticia)
    except Noticia.DoesNotExist:
        return HttpResponseNotFound("Notícia não encontrada.")

    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias:detalhes_noticia', nome_noticia=nome_noticia)
    else:
        form = NoticiaForm(instance=noticia)

    return render(request, 'noticias/editar_noticia.html', {'form': form})


def adicionar_comentario(request, nome_noticia):
    noticia = Noticia.objects.get(nome=nome_noticia)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = noticia
            comentario.save()
            return redirect('noticias:detalhes_noticia', nome_noticia=nome_noticia)
    else:
        form = ComentarioForm()

    return render(request, 'noticias/adicionar_comentario.html', {'form': form})


def remover_comentario(request, id_comentario):
    comentario = Comentario.objects.get(id=id_comentario)
    if request.method == 'POST':
        comentario.delete()
        return redirect('noticias:detalhes_noticia', nome_noticia=comentario.noticia.nome)
    else:
        return HttpResponseNotFound("Comentário não encontrado.")


def editar_comentario(request, id_comentario):
    comentario = Comentario.objects.get(id=id_comentario)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('noticias:detalhes_noticia', nome_noticia=comentario.noticia.nome)
    else:
        form = ComentarioForm(instance=comentario)

    return render(request, 'noticias/editar_comentario.html', {'form': form, 'comentario': comentario})


def editar_autor(request, id_autor):
    try:
        autor = Autor.objects.get(pk=id_autor)
    except Autor.DoesNotExist:
        return HttpResponseNotFound("Autor não encontrado.")

    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('noticias:detalhes_autor', nome_autor=autor.nome)
    else:
        form = AutorForm(instance=autor)

    return render(request, 'noticias/editar_autor.html', {'form': form})


def remover_autor(request, autor_id):
    autor = Autor.objects.get(pk=autor_id)
    if request.method == 'POST':
        autor.noticias.all().delete()
        autor.delete()
        return redirect('noticias:pagina_inicial')
    else:
        return HttpResponseNotFound("Autor não encontrado.")


def registro_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('noticias:pagina_inicial')
    else:
        form = UserForm()
    return render(request, 'noticias/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('noticias:pagina_inicial')
            else:
                messages.error(request, 'Credenciais inválidas')
    else:
        form = AuthenticationForm()
    return render(request, 'noticias/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('noticias:pagina_inicial')

