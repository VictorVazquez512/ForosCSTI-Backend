from django.contrib import admin
from .models import Almacenes

# Register your models here.

class AlmacenesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo')

admin.site.register(Almacenes, AlmacenesAdmin)
