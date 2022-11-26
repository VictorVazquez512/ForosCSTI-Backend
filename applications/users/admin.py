from django.contrib import admin
from .models import User

# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'last_name', 'is_active', 'is_staff')

admin.site.register(User, UsuariosAdmin)