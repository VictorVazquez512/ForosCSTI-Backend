from django.urls import path
from rest_framework import routers
from applications.engorda.catalogos.clasificacion.api.viewsets import ClasificacionViewSet

router_clasificacion = routers.DefaultRouter()
router_clasificacion.register(prefix='clasificacion', basename='clasificacion', viewset=ClasificacionViewSet)
