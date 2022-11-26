from django.urls import path
from rest_framework import routers
from applications.engorda.catalogos.empresas.api.viewsets import EmpresasViewSet

router_empresas = routers.DefaultRouter()
router_empresas.register(prefix='empresas', basename='empresas', viewset=EmpresasViewSet)
