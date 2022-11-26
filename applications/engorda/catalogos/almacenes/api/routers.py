from django.urls import path
from rest_framework import routers
from applications.engorda.catalogos.almacenes.api.viewsets import AlmacenesViewSet

router_almacenes = routers.DefaultRouter()
router_almacenes.register(prefix='almacenes', basename='almacenes', viewset=AlmacenesViewSet)
