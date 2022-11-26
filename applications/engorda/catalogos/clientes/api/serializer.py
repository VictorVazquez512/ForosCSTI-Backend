from rest_framework import serializers
from applications.engorda.catalogos.clientes.models import Clientes

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
        