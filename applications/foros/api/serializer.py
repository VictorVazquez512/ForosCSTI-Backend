from rest_framework import serializers
from applications.foros.models import Foros, Comentarios

class ForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foros
        fields = '__all__'

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'
