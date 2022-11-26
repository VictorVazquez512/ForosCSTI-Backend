from django.db import models
from applications.engorda.catalogos.fincas.models import *
from applications.engorda.catalogos.raza.models import *

# Create your models here.

class Lotes(models.Model):
    loteFisico = models.CharField(max_length=5)
    loteSistema = models.CharField(max_length=15)
    anio = models.DateField()

    class Meta:
        db_table = 'eng_lotes'
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'
        constraints = [
            models.UniqueConstraint(fields=['loteFisico', 'anio'], 
            name='Combinacion unica loteFisico-anio')
        ]

    def __str__(self):
        return self.loteFisico


class Cabezas(models.Model):
    
    arete = models.CharField(max_length=15, unique=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    lote = models.ForeignKey(Lotes, on_delete=models.CASCADE, db_column="id_fincas")
    espaciosFisicos = models.ManyToManyField(
        EspacioFisico,
        through='CabezaEspacio',
        through_fields=('cabeza', 'espacioFisico'),
    )
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, db_column="id_fincas")
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, db_column="id_fincas")
    tamano = models.ForeignKey(Tamano, on_delete=models.CASCADE, db_column="id_fincas")
    observacion_1 = models.CharField(max_length=50, null=True, null=True)
    observacion_2 = models.CharField(max_length=50, null=True, null=True)

    class Meta:
        db_table = 'eng_cabezas'
        verbose_name = 'Cabeza'
        verbose_name_plural = 'Cabezas'
        

    def __str__(self):
        return self.arete


class CabezaEspacio(models.Model):
    cabeza = models.ForeignKey(Cabezas, on_delete=models.CASCADE, db_column="id_cabeza")
    espacioFisico = models.ForeignKey(EspacioFisico, on_delete=models.CASCADE, db_column="id_espacio_fisico")
    activo = models.BooleanField()
    fecha = models.DateField()

    class Meta:
        db_table = 'eng_cabeza_espacio'
        verbose_name = 'CabezaEspacio'
        verbose_name_plural = 'CabezasEspacios'
        