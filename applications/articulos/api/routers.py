from django.urls import path
from rest_framework import routers
from applications.engorda.catalogos.articulos.api.viewsets import ArticulosViewSet

router_articulos = routers.DefaultRouter()
router_articulos.register(prefix='articulos', basename='articulos', viewset=ArticulosViewSet)

