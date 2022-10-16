from django.contrib import admin
from .models import Pessoa
from import_export.admin import ExportActionMixin
from django.contrib.auth.models import User

class pessoaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['id', 'login', 'senha', 'data_de_nascimento']  

admin.site.register(Pessoa, pessoaAdmin)
