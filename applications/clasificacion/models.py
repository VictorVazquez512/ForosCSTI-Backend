from django.db import models

# Create your models here.

class SubClasificacionArticulos(models.Model):

    GENDER_CHOICES = (
        ('INS', 'Insumos'),
        ('MED', 'Medicamentos')
    )

    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=40)
    clasificacion = models.CharField(max_length=15, choices=GENDER_CHOICES)
    activo = models.BooleanField(default=True)


    class Meta:
        db_table = 'eng_subclasificacion_articulos'
        verbose_name = 'SubClasificacion Articulos'
        verbose_name_plural = 'SubClasificaciones Articulos'

    def __str__(self):
        return self.codigo + " | " + self.nombre