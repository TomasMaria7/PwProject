from django.shortcuts import render, redirect
from curso.models import Curso, Disciplina, Projeto
from .forms import CursoForm, DisciplinaForm, ProjetoForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def lista_cursos(request):
    cursos = Curso.objects.all()
    context = {'cursos': cursos}
    return render(request, 'curso/lista_cursos.html', context)

def detalhes_curso(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplinas = curso.disciplinas.all()
    context = {'curso': curso, 'disciplinas': disciplinas}
    return render(request, 'curso/detalhes_curso.html', context)

def detalhes_disciplina(request, disciplina_nome):
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    projetos = Projeto.objects.filter(disciplina=disciplina)
    context = {'disciplina': disciplina, 'projetos': projetos}
    return render(request, 'curso/detalhes_disciplina.html', context)

def detalhes_projeto(request, projeto_nome):
    projeto = Projeto.objects.get(nome=projeto_nome)
    context = {'projeto': projeto}
    return render(request, 'curso/detalhes_projeto.html', context)


def adicionar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'curso/adicionar_curso.html', {'form': form})

def remover_curso(request, nome_curso):
    curso = Curso.objects.get(nome=nome_curso)
    curso.delete()
    return redirect('curso:lista_cursos')

def editar_curso(request, nome_curso):
    curso = Curso.objects.get(nome=nome_curso)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso:detalhes_curso', curso_nome=nome_curso)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso/editar_curso.html', {'form': form})


def adicionar_disciplina(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.save()
            curso.disciplinas.add(disciplina)
            return redirect('curso:detalhes_curso', curso_nome=curso_nome)
    else:
        form = DisciplinaForm()
    return render(request, 'curso/adicionar_disciplina.html', {'form': form, 'curso': curso})


def remover_disciplina(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    curso.disciplinas.remove(disciplina)
    return redirect('curso:detalhes_curso', curso_nome=curso_nome)

def editar_disciplina(request, disciplina_nome):
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:detalhes_disciplina', disciplina_nome=disciplina.nome)
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'curso/editar_disciplina.html', {'form': form, 'disciplina': disciplina})


def adicionar_projeto(request, disciplina_nome):
    disciplina = Disciplina.objects.get(nome=disciplina_nome)

    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.disciplina = disciplina
            projeto.save()
            return redirect('curso:detalhes_disciplina', disciplina_nome=disciplina_nome)
    else:
        form = ProjetoForm()
    return render(request, 'curso/adicionar_projeto.html', {'form': form, 'disciplina_nome': disciplina_nome})


def remover_projeto(request, disciplina_nome, projeto_nome):
    projeto = Projeto.objects.get(nome=projeto_nome)
    projeto.delete()
    return redirect('curso:detalhes_disciplina', disciplina_nome=disciplina_nome)


def editar_projeto(request, disciplina_nome, projeto_nome):
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    projeto = Projeto.objects.get(nome=projeto_nome)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('curso:detalhes_projeto', projeto_nome=projeto_nome)
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'curso/editar_projeto.html', {'form': form, 'disciplina_nome': disciplina_nome, 'projeto_nome': projeto_nome})


def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('curso:lista_cursos')
    else:
        form = UserForm()
    return render(request, 'curso/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('curso:lista_cursos')
    else:
        form = AuthenticationForm()
    return render(request, 'curso/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('curso:lista_cursos')





