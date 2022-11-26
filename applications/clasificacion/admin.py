from django.contrib import admin
from .models import SubClasificacionArticulos

# Register your models here.

class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo')

admin.site.register(SubClasificacionArticulos, ClasificacionAdmin)
