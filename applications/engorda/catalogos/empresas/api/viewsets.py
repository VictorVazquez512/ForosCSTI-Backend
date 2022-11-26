from rest_framework import viewsets
from applications.engorda.catalogos.empresas.models import Empresas
from applications.engorda.catalogos.empresas.api.serializer import EmpresasSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre_razon', 'codigo', 'activo']