from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['nome', 'titulo', 'autor', 'foto', 'idade', 'texto']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'foto']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'texto']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')