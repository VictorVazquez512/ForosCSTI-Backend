from rest_framework import serializers
from applications.foros.models import Foros, Comentarios
from applications.users.api.serializer import UserSerializer

class ForoSerializer(serializers.ModelSerializer):

    creador = UserSerializer()

    class Meta:
        model = Foros
        fields = ('titulo', 'descripcion', 'creador')


class ComentariosSerializer(serializers.ModelSerializer):

    foro = ForoSerializer()
    usuario = UserSerializer()

    class Meta:
        model = Comentarios
        fields = ('descripcion', 'foro', 'usuario')
