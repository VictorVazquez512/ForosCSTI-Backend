from django.contrib import admin
from .models import Articulos

# Register your models here.

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo')

admin.site.register(Articulos, ArticulosAdmin)