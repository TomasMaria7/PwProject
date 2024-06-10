from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),
    path('curso/<str:curso_nome>/', views.detalhes_curso, name='detalhes_curso'),
    path('disciplina/<str:disciplina_nome>/', views.detalhes_disciplina, name='detalhes_disciplina'),
    path('projeto/<str:projeto_nome>/', views.detalhes_projeto, name='detalhes_projeto'),
    path('adicionar/', views.adicionar_curso, name='adicionar_curso'),
    path('curso/remover/<str:nome_curso>/', views.remover_curso, name='remover_curso'),
    path('curso/editar/<str:nome_curso>/', views.editar_curso, name='editar_curso'),
    path('curso/<str:curso_nome>/adicionar_disciplina/', views.adicionar_disciplina, name='adicionar_disciplina'),
    path('curso/<str:curso_nome>/remover_disciplina/<str:disciplina_nome>/', views.remover_disciplina, name='remover_disciplina'),
    path('editar_disciplina/<str:disciplina_nome>/', views.editar_disciplina, name='editar_disciplina'),
    path('<str:disciplina_nome>/adicionar-projeto/', views.adicionar_projeto, name='adicionar_projeto'),
    path('<str:disciplina_nome>/remover-projeto/<str:projeto_nome>/', views.remover_projeto, name='remover_projeto'),
    path('<str:disciplina_nome>/editar-projeto/<str:projeto_nome>/', views.editar_projeto, name='editar_projeto'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]