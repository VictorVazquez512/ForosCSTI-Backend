from django.db import models
from applications.engorda.catalogos.clasificacion.models import SubClasificacionArticulos

# Create your models here.

class Articulos(models.Model):

    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=40)
    subClasificacion = models.ForeignKey(SubClasificacionArticulos, on_delete=models.CASCADE, db_column="id_subClasificacion")
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'eng_articulos'
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
