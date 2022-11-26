from django.contrib import admin
from django.urls import path, include

app_name = 'contabilidad'

urlpatterns = [
    path('contabilidad/', include('applications.contabilidad.catalogos.urls', namespace='catalogos')),
]