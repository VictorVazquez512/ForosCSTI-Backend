from rest_framework import viewsets
from applications.engorda.catalogos.proveedores.models import Proveedores
from applications.engorda.catalogos.proveedores.api.serializer import ProveedoresSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo']