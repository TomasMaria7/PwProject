
from . import views
from django.urls import path

app_name = 'portfolio'

urlpatterns = [
    path('', views.pagina_inicial, name="pagina_inicial"),
    path('sobre/', views.sobre, name='sobre'),
    path('projetos/', views.projetos, name='projetos'),
    path('contato/', views.contato, name='contato'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


]