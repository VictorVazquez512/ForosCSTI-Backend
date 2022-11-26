from rest_framework import viewsets
from applications.engorda.catalogos.raza.models import Raza, Tamano, Tipo
from applications.engorda.catalogos.raza.api.serializer import RazaSerializer, TamanoSerializer, TipoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo']
    
class TamanoViewSet(viewsets.ModelViewSet):
    queryset = Tamano.objects.all()
    serializer_class = TamanoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo']

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo']