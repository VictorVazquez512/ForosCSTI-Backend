from rest_framework import serializers
from applications.engorda.catalogos.almacenes.models import Almacenes

class AlmacenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacenes
        fields = '__all__'
        
