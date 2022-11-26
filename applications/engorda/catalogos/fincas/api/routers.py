from django.urls import path
from rest_framework import routers
from applications.engorda.catalogos.fincas.api.viewsets import FincasViewSet, PotrerosViewSet, CorralesViewSet

router_fincas = routers.DefaultRouter()
router_fincas.register(prefix='fincas', basename='fincas', viewset=FincasViewSet)
router_fincas.register(prefix='potreros', basename='potreros', viewset=PotrerosViewSet)
router_fincas.register(prefix='corrales', basename='corrales', viewset=CorralesViewSet)
