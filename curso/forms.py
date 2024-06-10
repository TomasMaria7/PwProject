from django import forms
from curso.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'apresentacao', 'objetivos', 'competencias']

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'ano', 'semestre', 'ects', 'code', 'area_cientifica', 'conteudos']

class ProjetoForm(forms.ModelForm):
    linguagens = forms.ModelMultipleChoiceField(queryset=Linguagem_Programacao.objects.all())

    class Meta:
        model = Projeto
        fields = '__all__'


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')