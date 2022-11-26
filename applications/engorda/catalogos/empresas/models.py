from django.db import models

# Create your models here.

class Empresas(models.Model):
    codigo = models.CharField(max_length=5)
    nombre_razon = models.CharField(max_length=50, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    curp = models.CharField(max_length=20, blank=True, null=True)
    imss = models.CharField(max_length=20, blank=True, null=True)
    domicilio = models.CharField(max_length=80, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    pais = models.CharField(max_length=15, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    delegacion = models.CharField(max_length=15, blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'eng_empresas'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre_razon