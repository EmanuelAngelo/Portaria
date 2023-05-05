from django.contrib import admin
from .models import Visitante, Apartamento, Sucesso

@admin.register(Apartamento)
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'bloco_apt',)
    list_filter = ('numero', 'bloco_apt',)

@admin.register(Visitante)
class VisitanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'uber', 'data_visita', 'apartamentos')
    list_filter = ('nome', 'cpf', 'apartamentos')

@admin.register(Sucesso)
class SucessoAdmin(admin.ModelAdmin):
    list_display = ('mensagem',)