from django.contrib import admin
from .models import Foros, Comentarios

# Register your models here.

class ForosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion')

admin.site.register(Foros, ForosAdmin)


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'foro', 'usuario')

admin.site.register(Comentarios, ComentariosAdmin)
