from django.urls import path
from applications.users.api.api import user_api_view, user_detail_api_view

urlpatterns = [
    path('usuarios/', user_api_view, name = 'usuario_api'),
    path('usuarios/<int:pk>', user_detail_api_view, name = 'usuario_detail'),
]