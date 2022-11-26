from django.contrib import admin
from django.urls import path, include

app_name = 'catalogos'

urlpatterns = [
    path('catalogos/', include('applications.engorda.catalogos.empresas.urls', namespace='empresas')),
]