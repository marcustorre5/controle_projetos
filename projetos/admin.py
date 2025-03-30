from django.contrib import admin
from .models import Projeto

class ProjetoAdmin(admin.ModelAdmin):
    # Atualize list_display para incluir apenas os campos existentes no modelo Projeto
    list_display = ('nome', 'data_inicio', 'data_fim', 'descricao')  # Remova 'cliente' e 'status'
    
    # Atualize search_fields para pesquisar apenas pelos campos existentes
    search_fields = ('nome',)  # Remova 'cliente'

    # Atualize list_filter para filtrar apenas pelos campos existentes
    list_filter = ('data_inicio', 'data_fim')  # Remova 'status'

    # Ações personalizadas
    actions = ['marcar_como_revisao', 'marcar_como_finalizado', 'marcar_como_em_andamento']
    
    # Ação para marcar como "Revisão"
    def marcar_como_revisao(self, request, queryset):
        queryset.update(status='revisao')
        self.message_user(request, "Status alterado para 'Revisão'.")
    marcar_como_revisao.short_description = 'Marcar como Revisão'

    # Ação para marcar como "Finalizado"
    def marcar_como_finalizado(self, request, queryset):
        queryset.update(status='finalizado')
        self.message_user(request, "Status alterado para 'Finalizado'.")
    marcar_como_finalizado.short_description = 'Marcar como Finalizado'
    
    # Ação para marcar como "Em Andamento"
    def marcar_como_em_andamento(self, request, queryset):
        queryset.update(status='em_andamento')
        self.message_user(request, "Status alterado para 'Em Andamento'.")
    marcar_como_em_andamento.short_description = 'Marcar como Em Andamento'

admin.site.register(Projeto, ProjetoAdmin)
