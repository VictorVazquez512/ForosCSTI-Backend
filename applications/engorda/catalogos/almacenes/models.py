from django.db import models
from applications.base.models import BaseModel
from applications.engorda.catalogos.articulos.models import Articulos
from simple_history.models import HistoricalRecords

# Create your models here.

class Almacenes(models.Model):

    GENDER_CHOICES = (
        ('INS', 'Insumos'),
        ('MED', 'Medicamentos')
    )

    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=3, choices=GENDER_CHOICES)
    activo = models.BooleanField(default=True)
    articulos = models.ManyToManyField(Articulos)

    class Meta:
        db_table = 'eng_almacenes'
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'

    def __str__(self):
        return self.nombre
