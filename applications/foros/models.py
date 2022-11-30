from django.db import models
from applications.usuarios.models import User

# Create your models here.

class Foros(models.Model):
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=250, default="", blank=True, null=True)

    class Meta:
        db_table = 'eng_subclasificacion_articulos'
        verbose_name = 'SubClasificacion Articulos'
        verbose_name_plural = 'SubClasificaciones Articulos'

    def __str__(self):
        return self.codigo + " | " + self.nombre


class Comentarios(models.Model):
    descripcion = models.CharField(max_length=250)
    foro = models.ForeignKey(Foros, on_delete=models.CASCADE, db_column="id_foro")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column="id_usuario")