from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(verbose_name = 'Ano de Criação')
    nacionalidade =  models.CharField(max_length=100, verbose_name = 'Nacionalidade', default='Unknown')
    foto = models.ImageField()

    def __str__(self):
        return f'Banda: {self.nome}, Ano de Criação: {self.idade}, '

class Album(models.Model):
    nome = models.CharField(max_length=100, default = 'Album nome')
    capa = models.ImageField()
    ano = models.IntegerField()
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=1000, default = 'Descrição')

    def __str__(self):
        return f'Album: {self.banda.nome}, Álbum: {self.nome}, Ano: {self.ano}'

class Musicas(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    duracao = models.FloatField()
    link = models.URLField(null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    letra = models.TextField(default='', null=True, blank=True)
    bibliografia = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f'Música: {self.nome}, Duração: {self.duracao}, Álbum: {self.album.nome}, Banda: {self.album.banda.nome}'




# Create your models here.
