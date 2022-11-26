from django.db import models

# Create your models here.

class Clientes(models.Model):
    fechaAlta = models.DateField(blank=True, null=True)
    codigo = models.CharField(max_length=5)
    nombreCliente = models.CharField(max_length=50, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    curp = models.CharField(max_length=20, blank=True, null=True)
    clasificacion = models.CharField(max_length=20, blank=True, null=True)
    domicilio = models.CharField(max_length=80, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    pais = models.CharField(max_length=15, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    delegacion = models.CharField(max_length=15, blank=True, null=True)
    nacionalidad = models.CharField(max_length=15, blank=True, null=True)
    moneda = models.CharField(max_length=10, blank=True, null=True)
    operacion = models.CharField(max_length=10, blank=True, null=True)
    claveSat = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'eng_clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombreCliente