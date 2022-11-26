from rest_framework import viewsets
from applications.engorda.catalogos.clientes.models import Clientes
from applications.engorda.catalogos.clientes.api.serializer import ClientesSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombreCliente', 'codigo', 'activo']