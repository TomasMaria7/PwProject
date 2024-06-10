from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('previsao/<str:cidade_id>/', views.tempo_5_dias, name='tempo_5_dias'),
    path('api/', views.pagina_api, name='pagina_api'),
    path('api/lista_de_cidades/', views.lista_de_cidades, name='api_lista_de_cidades'),
    path('api/previsao_hoje/<str:cidade_id>/', views.previsao_hoje, name='api_previsao_hoje'),
    path('api/previsao_proximos_5_dias/<str:cidade_id>/', views.previsao_proximos_5_dias, name='api_previsao_proximos_5_dias'),
]