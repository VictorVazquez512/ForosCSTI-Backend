from rest_framework import viewsets
from applications.engorda.catalogos.almacenes.models import Almacenes
from applications.engorda.catalogos.almacenes.api.serializer import AlmacenesSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AlmacenesViewSet(viewsets.ModelViewSet):
    queryset = Almacenes.objects.all()
    serializer_class = AlmacenesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo']
    