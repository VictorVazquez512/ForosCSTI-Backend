from django.db import models

# Create your models here.

class Proveedores(models.Model):
    codigo = models.CharField(max_length=4)
    fechaAlta = models.DateField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    curp = models.CharField(max_length=20, blank=True, null=True)
    domicilio = models.CharField(max_length=80, blank=True, null=True)
    delegacion = models.CharField(max_length=15, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    pais = models.CharField(max_length=15, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    cuentaBancaria = models.CharField(max_length=18, blank=True, null=True)
    nacionalidad = models.CharField(max_length=15, blank=True, null=True)
    moneda = models.CharField(max_length=10, blank=True, null=True)
    operacion = models.CharField(max_length=10, blank=True, null=True)
    cuentaSat = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)


    class Meta:
        db_table = 'eng_proveedores'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre