from django.db import models
from applications.users.models import User

# Create your models here.

class Foros(models.Model):
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=250, default="", blank=True, null=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, db_column="id_usuario", default=1)

    class Meta:
        db_table = 'foros'
        verbose_name = 'Foro'
        verbose_name_plural = 'Foro'

    def __str__(self):
        return self.codigo + " | " + self.nombre


class Comentarios(models.Model):
    descripcion = models.CharField(max_length=250)
    foro = models.ForeignKey(Foros, on_delete=models.CASCADE, db_column="id_foro")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column="id_usuario")

    class Meta:
        db_table = 'comentarios'
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'