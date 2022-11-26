from django.db import models

# Create your models here.

ESPACIO_CHOICES = (
        ('POT', 'Potrero'),
        ('COR', 'Corral')
    )

class Fincas(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    domicilio = models.CharField(max_length=80, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    pais = models.CharField(max_length=15, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    delegacion = models.CharField(max_length=15, blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'eng_fincas'
        verbose_name = 'Finca'
        verbose_name_plural = 'Fincas'

    def __str__(self):
        return self.nombre


class EspacioFisico(models.Model):

    # Base
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=3, choices=ESPACIO_CHOICES)
    finca = models.ForeignKey(Fincas, on_delete=models.CASCADE, db_column="id_fincas")
    activo = models.BooleanField(default=True)

    # Especifico Potrero
    hectareas = models.CharField(max_length=80, blank=True, null=True)
    follaje = models.CharField(max_length=20, blank=True, null=True)
    

    class Meta:
        db_table = 'eng_espacio_fisico'
        verbose_name = 'Potrero'
        verbose_name_plural = 'Potreros'

    def __str__(self):
        return self.nombre