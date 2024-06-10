from django import forms
from .models import Banda, Album, Musicas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = '__all__'
        help_texts = {
            'nome': 'Insira o nome da banda.',
            'idade': 'Insira o ano de criação da banda.',
            'nacionalidade': 'Insira a nacionalidade da banda (opcional).',
            'foto': 'Selecione uma imagem para representar a banda.'
        }

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musicas
        fields = ['nome', 'ano', 'duracao', 'link', 'letra', 'bibliografia']
        help_texts = {
            'nome': 'Insira o nome da música.',
            'ano': 'Insira o ano de lançamento da música.',
            'duracao': 'Insira a duração da música em minutos.',
            'link': 'Insira o link da música (opcional).',
            'letra': 'Insira a letra da música (opcional).',
            'bibliografia': 'Insira uma breve bibliografia sobre a música (opcional).'
        }


class RemoverBandaForm(forms.Form):
    banda_id = forms.IntegerField(widget=forms.HiddenInput())


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nome', 'banda', 'ano', 'capa', 'descricao']
        help_texts = {
            'nome': 'Insira o nome do álbum.',
            'banda': 'Selecione a banda associada ao álbum.',
            'ano': 'Insira o ano de lançamento do álbum.',
            'capa': 'Selecione uma imagem para a capa do álbum.',
            'descricao': 'Insira uma descrição para o álbum (opcional).'
        }



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')




