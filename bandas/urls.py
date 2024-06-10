from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('registro/', views.registro_view, name="registro"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('', views.bandas_view, name='bandas'),
    path('albuns', views.albuns_view, name='albuns'),
    path('musicas', views.musicas_view, name='musicas'),
    path('banda/<str:banda_nome>/', views.banda_detalhes_view, name='banda_detalhes'),
    path('album/<str:album_nome>/', views.album_detalhes_view, name='album_detalhes'),
    path('musica/<str:musica_nome>/', views.musica_detalhes_view, name='musica_detalhes'),
    path('nova-banda/', views.nova_banda_view, name='nova_banda'),
    path('remover-banda/<str:banda_nome>/', views.remover_banda, name='remover_banda'),
    path('editar-banda/<str:nome_banda>/', views.editar_banda_view, name='editar_banda'),
    path('novo-album/', views.novo_album_view, name='novo_album'),
    path('remover-album/<str:banda_nome>/<str:album_nome>/', views.remover_album, name='remover_album'),
    path('editar-album/<str:banda_nome>/<str:album_nome>/', views.editar_album_view, name='editar_album'),
    path('nova-musica/<str:banda_nome>/<str:album_nome>/', views.nova_musica_view, name='nova_musica'),
    path('remover-musica/<str:banda_nome>/<str:album_nome>/<str:musica_nome>/', views.remover_musica, name='remover_musica'),
    path('editar-musica/<str:banda_nome>/<str:album_nome>/<str:musica_nome>/', views.editar_musica_view, name='editar_musica'),
    path('recuperar-senha/', views.recuperar_senha, name='recuperar_senha'),
]