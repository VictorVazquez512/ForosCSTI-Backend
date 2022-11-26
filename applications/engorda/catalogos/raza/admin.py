from django.contrib import admin
from .models import Raza, Tamano, Tipo

# Register your models here.

class RazaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo')

class TamanoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo')

class TipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo')


admin.site.register(Raza, RazaAdmin)
admin.site.register(Tamano, TamanoAdmin)
admin.site.register(Tipo, TipoAdmin)