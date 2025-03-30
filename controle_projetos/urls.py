from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Painel de administração
    path('', include('projetos.urls')),  # Página inicial e URLs de 'projetos'
]
