from rest_framework import viewsets
from applications.engorda.catalogos.articulos.models import Articulos
from applications.engorda.catalogos.articulos.api.serializer import ArticulosSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ArticulosViewSet(viewsets.ModelViewSet):
    queryset = Articulos.objects.all()
    serializer_class = ArticulosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo']