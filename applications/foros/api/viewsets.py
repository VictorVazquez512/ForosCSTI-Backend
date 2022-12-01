from rest_framework import viewsets
from applications.foros.api.serializer import ForoSerializer, ComentariosSerializer
from applications.foros.models import Foros, Comentarios
from django_filters.rest_framework import DjangoFilterBackend

class ForosViewSet(viewsets.ModelViewSet):
    queryset = Foros.objects.all()
    serializer_class = ForoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo', 'clasificacion']


class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo', 'clasificacion']