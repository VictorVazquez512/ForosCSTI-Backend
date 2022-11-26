from rest_framework import serializers
from applications.engorda.catalogos.clasificacion.models import SubClasificacionArticulos

class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubClasificacionArticulos
        fields = '__all__'
