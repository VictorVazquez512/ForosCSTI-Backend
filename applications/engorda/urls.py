from django.contrib import admin
from django.urls import path, include

app_name = 'engorda'

urlpatterns = [
    path('engorda/', include('applications.engorda.catalogos.urls', namespace='catalogos')),
]