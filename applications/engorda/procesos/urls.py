from django.contrib import admin
from django.urls import path, include

app_name = 'procesos'

urlpatterns = [
    path('procesos/', include('applications.engorda.catalogos.urls', namespace='catalogos')),
]