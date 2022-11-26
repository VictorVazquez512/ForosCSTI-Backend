"""GanaderoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from applications.engorda.catalogos.almacenes.api.routers import router_almacenes
from applications.engorda.catalogos.articulos.api.routers import router_articulos
from applications.engorda.catalogos.clasificacion.api.routers import router_clasificacion
from applications.engorda.catalogos.clientes.api.routers import router_clientes
from applications.engorda.catalogos.empresas.api.routers import router_empresas
from applications.engorda.catalogos.fincas.api.routers import router_fincas
from applications.engorda.catalogos.proveedores.api.routers import router_proveedores
from applications.engorda.catalogos.raza.api.routers import router_raza

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('applications.users.api.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # API
    # path('api/', include('applications.engorda.catalogos.almacenes.urls')),
    # path('api/', include('applications.engorda.catalogos.articulos.urls')),
    # path('api/', include('applications.engorda.catalogos.clasificacion.urls')),
    # path('api/', include('applications.engorda.catalogos.empresas.urls')),
    # path('api/', include('applications.engorda.catalogos.clientes.urls')),
    # path('api/', include('applications.engorda.catalogos.fincas.urls')),
    # path('api/', include('applications.engorda.catalogos.proveedores.urls')),
    # path('api/', include('applications.engorda.catalogos.raza.urls')),
    path('api/', include(router_almacenes.urls)),
    path('api/', include(router_articulos.urls)),
    path('api/', include(router_clasificacion.urls)),
    path('api/', include(router_clientes.urls)),
    path('api/', include(router_empresas.urls)),
    path('api/', include(router_fincas.urls)),
    path('api/', include(router_proveedores.urls)),
    path('api/', include(router_raza.urls)),
]
