from rest_framework import serializers
from applications.engorda.catalogos.articulos.models import Articulos

class ArticulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulos
        fields = '__all__'