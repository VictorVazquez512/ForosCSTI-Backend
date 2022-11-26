from django.urls import path
from rest_framework import routers
from applications.engorda.catalogos.proveedores.api.viewsets import ProveedoresViewSet

router_proveedores = routers.DefaultRouter()
router_proveedores.register(prefix='proveedores', basename='proveedores', viewset=ProveedoresViewSet)