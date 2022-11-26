from django.contrib import admin
from .models import Clientes

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreCliente', 'activo')

admin.site.register(Clientes, ClientesAdmin)