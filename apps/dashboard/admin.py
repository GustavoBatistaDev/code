from django.contrib import admin
from .models import AlertaDeCrise, Anotacao, Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('status',)


@admin.register(Anotacao)
class AnotacaoAdmin(admin.ModelAdmin):
    list_display = ('avaliacao', 'anotacao', 'tipo')


@admin.register(AlertaDeCrise)
class AlertaDeCriseAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'inicio', 'fim')
