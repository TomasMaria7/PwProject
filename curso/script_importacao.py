from curso.models import *
import json

Curso.objects.all().delete()
Area_Cientifica.objects.all().delete()
Disciplina.objects.all().delete()
Projeto.objects.all().delete()
Linguagem_Programacao.objects.all().delete()
Docente.objects.all().delete()

def importar_curso(ficheiro_json):
    with open('curso/json/lei.json') as f:
        dados = json.load(f)

    curso_dados = dados['curso']
    curso = Curso.objects.create(
        nome=curso_dados['nome'],
        apresentacao=curso_dados['apresentacao'],
        objetivos=curso_dados['objetivos'],
        competencias=curso_dados['competencias']
    )


    areas_cientificas_dados = dados['areas_cientificas']
    for area_dados in areas_cientificas_dados:
        Area_Cientifica.objects.create(
            nome=area_dados['nome']
        )


    disciplinas_dados = dados['disciplinas']
    for disciplina_dados in disciplinas_dados:
        area_cientifica = Area_Cientifica.objects.get(nome=disciplina_dados['area_cientifica'])
        disciplina = Disciplina.objects.create(
            nome=disciplina_dados['nome'],
            ano=disciplina_dados['ano'],
            semestre=disciplina_dados['semestre'],
            ects=disciplina_dados['ects'],
            code=disciplina_dados['code'],
            area_cientifica=area_cientifica
        )

        projetos_dados = disciplina_dados['projetos']
        for projeto_dados in projetos_dados:
            projeto = Projeto.objects.create(
                nome=projeto_dados['nome'],
                descricao=projeto_dados['descricao'],
                conceitos=projeto_dados['conceitos'],
                tecnologias=projeto_dados['tecnologias'],
                foto=projeto_dados['foto'],
                video=projeto_dados.get('video'),
                gitLink=projeto_dados.get('gitLink'),
                disciplina=disciplina
            )
            linguagens_dados = projeto_dados['linguagens']
            for linguagem_dados in linguagens_dados:
                linguagem, _ = Linguagem_Programacao.objects.get_or_create(
                    nome=linguagem_dados['nome']
                )
                projeto.linguagens.add(linguagem)


    docentes_dados = dados['docentes']
    for docente_dado in docentes_dados:
        docente = Docente.objects.create(
            nome=docente_dado['nome']
        )
        disciplinas_dados = docente_dado['disciplinas']
        for disciplina_nome in disciplinas_dados:
            disciplina = Disciplina.objects.get(nome=disciplina_nome)
            docente.disciplina.add(disciplina)

