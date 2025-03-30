from django.urls import path
from . import views

app_name = 'projetos'

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial (index)
    path('lista/', views.lista_projetos, name='lista_projetos'),  # Página de lista de projetos
    path('adicionar/', views.adicionar_projeto, name='adicionar_projeto'),  # Página de adicionar projeto
    path('<int:pk>/', views.detalhes_projeto, name='detalhes_projeto'),  # Detalhes do projeto
]
