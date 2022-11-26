from django.db import models

# Create your models here.

class Raza(models.Model):

    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=40)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'eng_raza_cabeza'
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'

    def __str__(self):
        return self.nombre


class Tamano(models.Model):

    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=40)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'eng_tamano_cabeza'
        verbose_name = 'Tamaño'
        verbose_name_plural = 'Tamaños'

    def __str__(self):
        return self.nombre


class Tipo(models.Model):

    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=40)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'eng_tipo_cabeza'
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.nombre