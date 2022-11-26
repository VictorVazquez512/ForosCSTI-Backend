from django.urls import path
from rest_framework import routers
from applications.engorda.catalogos.clientes.api.viewsets import ClientesViewSet

router_clientes = routers.DefaultRouter()
router_clientes.register(prefix='clientes', basename='clientes', viewset=ClientesViewSet)
