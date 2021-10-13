from django.contrib import admin

from .models import Avaliacao,Curso

@admin.register(Curso)
class detCurso(admin.ModelAdmin):
    list_display = ("titulo", "url", "create", "update", "active")

@admin.register(Avaliacao)
class detAvaliacao(admin.ModelAdmin):
    list_display = ("curso", "nome", "nota", "comentarios", "email", "update")
