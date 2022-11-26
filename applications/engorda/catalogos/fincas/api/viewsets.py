from rest_framework import viewsets
from applications.engorda.catalogos.fincas.models import Fincas, EspacioFisico
from applications.engorda.catalogos.fincas.api.serializer import FincasSerializer, PotrerosSerializer, CorralesSerializer
from django_filters.rest_framework import DjangoFilterBackend

class FincasViewSet(viewsets.ModelViewSet):
    queryset = Fincas.objects.all()
    serializer_class = FincasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo']
    

class PotrerosViewSet(viewsets.ModelViewSet):
    queryset = EspacioFisico.objects.all()
    serializer_class = PotrerosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo']


class CorralesViewSet(viewsets.ModelViewSet):
    queryset = EspacioFisico.objects.all()
    serializer_class = CorralesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'codigo', 'activo']