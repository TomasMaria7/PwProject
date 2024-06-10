from django.urls import path
from .views import praias_view, praia_view

app_name = 'praias'

urlpatterns = [
    path('', praias_view, name='praias'),
    path('praia/<str:praia_nome>/', praia_view, name='praia'),
]
