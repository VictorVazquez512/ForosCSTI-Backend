from django.contrib import admin
from .models import Proveedores

# Register your models here.

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo')

admin.site.register(Proveedores, ProveedoresAdmin)