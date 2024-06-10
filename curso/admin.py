from django.contrib import admin
from django.utils.html import format_html

from .models import Curso
from .models import Area_Cientifica
from .models import Disciplina
from .models import Projeto
from .models import Linguagem_Programacao
from .models import Docente

admin.site.register(Curso)
admin.site.register(Area_Cientifica)
admin.site.register(Disciplina)
admin.site.register(Projeto)
admin.site.register(Linguagem_Programacao)
admin.site.register(Docente)


# Register your models here.
