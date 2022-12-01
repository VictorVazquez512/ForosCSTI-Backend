from django.contrib import admin
from .models import User

# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')

admin.site.register(User, UsuariosAdmin)