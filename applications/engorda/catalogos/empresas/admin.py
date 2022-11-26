from django.contrib import admin
from .models import Empresas

# Register your models here.

class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_razon', 'activo')

admin.site.register(Empresas, EmpresasAdmin)