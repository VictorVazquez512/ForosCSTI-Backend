from django.contrib import admin
from .models import Fincas, EspacioFisico

# Register your models here.

class FincasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo')

class EspaciosFisicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo')

admin.site.register(Fincas, FincasAdmin)
admin.site.register(EspacioFisico, EspaciosFisicosAdmin)