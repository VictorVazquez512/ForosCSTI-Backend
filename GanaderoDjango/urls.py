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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from applications.foros.api.routers import router_foros, router_comentarios
from applications.users.api.routers import urlpatterns
from applications.users.views import Login, Logout

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
    path('users/', include(urlpatterns)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('logout/', Logout.as_view(), name='logout'),
    path('login/', Login.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # API
    # path('api/', include('applications.engorda.catalogos.almacenes.urls')),
    # path('api/', include('applications.engorda.catalogos.articulos.urls')),
    # path('api/', include('applications.engorda.catalogos.clasificacion.urls')),
    # path('api/', include('applications.engorda.catalogos.empresas.urls')),
    # path('api/', include('applications.engorda.catalogos.clientes.urls')),
    # path('api/', include('applications.engorda.catalogos.fincas.urls')),
    # path('api/', include('applications.engorda.catalogos.proveedores.urls')),
    # path('api/', include('applications.engorda.catalogos.raza.urls')),
    path('api/', include(router_foros.urls)),
    path('api/', include(router_comentarios.urls)),
]
