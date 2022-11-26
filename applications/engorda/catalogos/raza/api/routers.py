from django.urls import path
from rest_framework import routers
from applications.engorda.catalogos.raza.api.viewsets import RazaViewSet, TamanoViewSet, TipoViewSet

router_raza = routers.SimpleRouter()
router_raza.register(prefix='raza', basename='raza', viewset=RazaViewSet)
router_raza.register(prefix='tamano', basename='tamano', viewset=TamanoViewSet)
router_raza.register(prefix='tipo', basename='tipo', viewset=TipoViewSet)
