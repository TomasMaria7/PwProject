from django.db import models


class Regiao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return  self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Praia(models.Model):
    nome = models.CharField(max_length=100)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)
    servicos = models.ManyToManyField('Servico')
    foto = models.ImageField()

    def __str__(self):
        return  self.nome



