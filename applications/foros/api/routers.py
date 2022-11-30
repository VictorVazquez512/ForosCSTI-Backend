from django.urls import path
from rest_framework import routers
from applications.foros.api.viewsets import ForosViewSet, ComentariosViewSet

router_foros = routers.DefaultRouter()
router_foros.register(prefix='foro', basename='foro', viewset=ForosViewSet)

router_comentarios = routers.DefaultRouter()
router_comentarios.register(prefix='comentario', basename='comentario', viewset=ComentariosViewSet)
