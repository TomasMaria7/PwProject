from django.contrib import admin
from django.utils.html import format_html
from .models import Autor
from .models import Noticia
from .models import Comentario

admin.site.register(Autor)
admin.site.register(Noticia)
admin.site.register(Comentario)


# Register your models here.
