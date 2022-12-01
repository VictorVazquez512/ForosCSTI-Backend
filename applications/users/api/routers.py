from rest_framework.routers import DefaultRouter

from applications.users.api.api import UserViewSet

router_users = DefaultRouter()

router_users.register('', UserViewSet, basename="users")

urlpatterns = router_users.urls