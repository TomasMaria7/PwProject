from django.shortcuts import render, redirect
from bandas.models import Banda, Album, Musicas
from .forms import BandaForm, RemoverBandaForm, AlbumForm, MusicaForm,UserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password

def bandas_view(request):
    bandas = Banda.objects.all().order_by('nome')
    context = {'bandas': bandas}
    return render(request, "bandas/bandas.html", context)

def albuns_view(request):
    albuns = Album.objects.all().order_by('nome')
    context = {'albuns': albuns}
    return render(request, "bandas/albuns.html", context)

def musicas_view(request):
    musicas = Musicas.objects.all().order_by('nome')
    context = {'musicas': musicas}
    return render(request, "bandas/musicas.html", context)

def banda_detalhes_view(request, banda_nome):
    if banda_nome.lower() == "ac-dc":
        banda = Banda.objects.get(nome="AC DC")
    else:
        banda_nome = banda_nome.replace('-', ' ').title()
        banda = Banda.objects.get(nome = banda_nome)

    albuns = Album.objects.filter(banda=banda)
    context = {'banda': banda, 'albuns': albuns}
    return render(request, "bandas/banda_detalhes.html", context)

def album_detalhes_view(request, album_nome):
    album = Album.objects.get(nome=album_nome)
    musicas = Musicas.objects.filter(album=album)
    context = {'album': album, 'musicas': musicas}
    return render(request, "bandas/album_detalhes.html", context)

def musica_detalhes_view(request, musica_nome):
    musica = Musicas.objects.get(nome=musica_nome)
    context = {'musica': musica}
    return render(request, "bandas/musica_detalhes.html", context)


def nova_banda_view(request):
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas')
    else:
        form = BandaForm()

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)

def remover_banda(request, banda_nome):
    try:
        banda = Banda.objects.get(nome=banda_nome)
    except Banda.DoesNotExist:
        banda = None

    if request.method == 'POST' and banda:
        banda.delete()
        return HttpResponseRedirect(reverse('bandas:bandas'))

    return render(request, 'bandas/remover_banda.html', {'banda': banda})

def editar_banda_view(request, nome_banda):
    try:
        banda = Banda.objects.get(nome=nome_banda.replace('-', ' '))
    except Banda.DoesNotExist:
        banda = None

    if request.method == 'POST' and banda:
        form = BandaForm(request.POST, instance=banda)
        if form.is_valid():
            form.save()

            return redirect('bandas:bandas')
    else:
        form = BandaForm(instance=banda)

    context = {'form': form}
    return render(request, 'bandas/editar_banda.html', context)


def novo_album_view(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            nome_banda = album.banda.nome
            album.save()
            return redirect('bandas:banda_detalhes', banda_nome=nome_banda)
    else:
        form = AlbumForm()

    context = {'form': form}
    return render(request, 'bandas/novo_album.html', context)


def remover_album(request, banda_nome, album_nome):
    album = Album.objects.get(nome=album_nome)
    banda = Banda.objects.get(nome=banda_nome)
    album.delete()
    return redirect('bandas:banda_detalhes', banda_nome=banda_nome)

def editar_album_view(request, banda_nome, album_nome):
    banda = Banda.objects.get(nome=banda_nome)
    album = Album.objects.get(nome=album_nome)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:banda_detalhes', banda_nome=banda_nome)
    else:
        form = AlbumForm(instance=album)
    context = {'form': form, 'banda': banda, 'album': album}
    return render(request, 'bandas/editar_album.html', context)


def nova_musica_view(request, banda_nome, album_nome):
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            musica = form.save(commit=False)
            album = Album.objects.get(nome=album_nome)
            musica.album = album
            musica.save()
            return redirect('bandas:album_detalhes', album_nome=album_nome)
    else:
        form = MusicaForm()

    context = {'form': form}
    return render(request, 'bandas/nova_musica.html', context)


def remover_musica(request, banda_nome, album_nome, musica_nome):
    musica = Musicas.objects.get(nome=musica_nome)

    musica.delete()
    return redirect('bandas:album_detalhes', album_nome=album_nome)


def editar_musica_view(request, banda_nome, album_nome, musica_nome):
    try:
        banda = Banda.objects.get(nome=banda_nome)
        album = Album.objects.get(nome=album_nome, banda=banda)
        musica = Musicas.objects.get(album=album, nome=musica_nome)
    except (Banda.DoesNotExist, Album.DoesNotExist, Musicas.DoesNotExist):
        return HttpResponseNotFound("Banda, álbum ou música não encontrados.")

    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:musica_detalhes', musica_nome=musica.nome)
    else:
        form = MusicaForm(instance=musica)

    context = {'form': form, 'musica': musica}
    return render(request, 'bandas/editar_musica.html', context)

def registro_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('bandas:bandas')
    else:
        form = UserForm()
    return render(request, 'bandas/registro.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bandas:bandas')
            else:
                messages.error(request, 'Credenciais inválidas')
    else:
        form = AuthenticationForm()
    return render(request, 'bandas/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('bandas:bandas')


def recuperar_senha(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        nova_senha = request.POST.get('nova_senha')

        try:
            user = User.objects.get(username=username)
            user.password = make_password(nova_senha)
            user.save()
            return render(request, 'bandas/bandas.html')
        except User.DoesNotExist:
            return render(request, 'bandas/registro.html')

    return render(request, 'bandas/recuperar_senha.html')

