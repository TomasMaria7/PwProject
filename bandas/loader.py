from bandas.models import *

from django.db.models import Count

import json

Banda.objects.all().delete()
Album.objects.all().delete()
Musicas.objects.all().delete()

with open('bandas/json/bandas.json') as f:
        bandas = json.load(f)

        for banda in bandas:
            Banda.objects.create(
                nome = banda['nome'],
                idade = banda['ano_criacao'],
                nacionalidade = banda['nacionalidade']
                )


with open('bandas/json/discos.json') as f:
    discos = json.load(f)

    for disco in discos:
        banda = Banda.objects.get(nome=disco['banda'])

        album = Album.objects.create(
            nome=disco['titulo'],
            ano=disco['ano_lancamento'],
            banda=banda
        )

        for musica in disco['musicas']:
            Musicas.objects.create(
                nome=musica['titulo'],
                ano=album.ano,
                duracao=musica['duracao'],
                album=album
            )


print('Nome das bandas, ordenadas alfabeticamente:')

#Listar o nome das bandas, ordenadas alfabeticamente
bandas = Banda.objects.all().order_by('nome')
for banda in bandas:
    print(banda.nome)

print('')
print('')
print('Nome dos álbuns de uma banda, ordenados cronologicamente:')

#Listar o nome dos álbuns de uma banda, ordenados cronologicamente
banda_nome = 'Metallica'
albuns = Album.objects.filter(banda__nome=banda_nome).order_by('ano')
for album in albuns:
    print(album.nome)

print('')
print('')
print('Álbuns que  lançados entre 1970 e 1980:')

#Apresentar todos os álbuns que foram lançados entre dois anos à sua escolha
ano_inicial = 1970
ano_final = 1980
albuns = Album.objects.filter(ano__range=(ano_inicial, ano_final))
for album in albuns:
    print(album.nome)

print('')
print('')
print('Álbuns com músicas que durem mais de 5 minutos:')

#Listar os álbuns com músicas que durem mais de 5 minutos
albuns = Album.objects.filter(musicas__duracao__gt=5)
for album in albuns:
    print(album.nome)

print('')
print('')
print('Listar todas as músicas que tenham uma determinada palavra no título:')

#Listar todas as músicas que tenham uma determinada palavra no título
palavra_chave = 'to'
musicas = Musicas.objects.filter(nome__icontains=palavra_chave)
for musica in musicas:
    print(musica.nome)

print('')
print('')


#Contar o número de álbuns lançados por uma banda específica
banda_nome = 'Queen'
quantidade_albuns = Album.objects.filter(banda__nome=banda_nome).count()
print(f"A banda {banda_nome} lançou {quantidade_albuns} álbuns.")


print('')
print('')

#Encontrar a banda mais antiga no banco de dados
banda_mais_antiga = Banda.objects.order_by('idade').first()
print(f"A banda mais antiga é {banda_mais_antiga.nome}, criada em {banda_mais_antiga.idade}.")

print('')
print('')
print('Bandas que têm pelo menos um álbum lançado nos anos 90:')

#Listar todas as bandas que têm pelo menos um álbum lançado nos anos 90
bandas = Banda.objects.filter(album__ano__range=(1990, 1999)).distinct()
for banda in bandas:
    print(banda.nome)


print('')
print('')

#Encontrar todas as bandas que foram criadas antes de um determinado ano
ano_limite = 1980
bandas_antigas = Banda.objects.filter(idade__lt=ano_limite)
for banda in bandas_antigas:
    print(f"A banda '{banda.nome}' foi criada antes de {ano_limite}.")

print('')
print('')

#Encontrar todas as bandas que têm mais de 2 álbuns registrados no sistema
bandas_com_muitos_albuns = Banda.objects.annotate(num_albuns=Count('album')).filter(num_albuns__gt=2)
for banda in bandas_com_muitos_albuns:
    print(f"A banda '{banda.nome}' tem mais de 2 álbuns registrados.")



