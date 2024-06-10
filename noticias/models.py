from django.db import models
import datetime

class Autor(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Autor')
    foto = models.ImageField(verbose_name='Foto do Autor')

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Noticia')
    titulo = models.CharField(max_length=100, verbose_name='Titulo', default='')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='noticias', verbose_name='Autor da Noticia', default='Nome do Autor Padrão')
    foto = models.ImageField(verbose_name='Capa da Noticia')
    idade = models.IntegerField(verbose_name='Ano da Noticia')
    texto = models.CharField(max_length=10000, verbose_name='Corpo da Noticia')
    data_postagem = models.DateTimeField(auto_now_add=True, verbose_name='Data de Postagem')  # Adicionado com valor padrão

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    autor = models.CharField(max_length=100, verbose_name='Nome')
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios', verbose_name='Noticia')
    texto = models.CharField(max_length=500, verbose_name='Texto do Comentário')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data do Comentário')

    def __str__(self):
        return f'Comentário por {self.autor} em {self.noticia}'
