from rest_framework.routers import DefaultRouter

from apps.users.api.viewsets.user_viewset import UserViewSet
from apps.users.api.viewsets.general_views import gustosUserViewset

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'gustos_by_users', gustosUserViewset, basename="gustos_by_users")

urlpatterns = router.urls