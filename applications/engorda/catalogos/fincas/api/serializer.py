from rest_framework import serializers
from applications.engorda.catalogos.fincas.models import Fincas, EspacioFisico
class FincasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fincas
        fields = '__all__'
        

class PotrerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspacioFisico
        fields = '__all__'


class CorralesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspacioFisico
        fields = '__all__'