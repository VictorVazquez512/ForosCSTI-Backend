from rest_framework import serializers
from applications.engorda.catalogos.empresas.models import Empresas

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'
        