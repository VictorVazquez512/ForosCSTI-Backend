from rest_framework import serializers
from applications.foros.models import Foros, Comentarios

class ForoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Foros
        fields = ('titulo', 'descripcion', 'creador')


class ComentariosSerializer(serializers.ModelSerializer):

    foro = ForoSerializer()
    
    class Meta:
        model = Comentarios
        fields = ('descripcion', 'foro', 'usuario')
