from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('noticia/<str:nome_noticia>/', views.detalhes_noticia, name='detalhes_noticia'),
    path('autor/<str:nome_autor>/', views.detalhes_autor, name='detalhes_autor'),
    path('adicionar-noticia/', views.adicionar_noticia, name='adicionar_noticia'),
    path('adicionar-autor/', views.adicionar_autor, name='adicionar_autor'),
    path('remover-noticia/<int:id_noticia>/', views.remover_noticia, name='remover_noticia'),
    path('editar-noticia/<str:nome_noticia>/', views.editar_noticia, name='editar_noticia'),
    path('adicionar-comentario/<str:nome_noticia>/', views.adicionar_comentario, name='adicionar_comentario'),
    path('remover-comentario/<int:id_comentario>/', views.remover_comentario, name='remover_comentario'),
    path('editar-comentario/<int:id_comentario>/', views.editar_comentario, name='editar_comentario'),
    path('editar-autor/<int:id_autor>/', views.editar_autor, name='editar_autor'),
    path('remover-autor/<int:autor_id>/', views.remover_autor, name='remover_autor'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),

]