from rest_framework import viewsets
from applications.engorda.catalogos.clasificacion.models import SubClasificacionArticulos
from applications.engorda.catalogos.clasificacion.api.serializer import ClasificacionSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ClasificacionViewSet(viewsets.ModelViewSet):
    queryset = SubClasificacionArticulos.objects.all()
    serializer_class = ClasificacionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo', 'clasificacion']