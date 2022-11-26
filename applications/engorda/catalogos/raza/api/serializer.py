from rest_framework import serializers
from applications.engorda.catalogos.raza.models import Raza, Tamano, Tipo

class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = '__all__'

class TamanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamano
        fields = '__all__'

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'