from rest_framework.routers import DefaultRouter

from apps.location.api.viewsets.ubicacion_view import ubicacionViewSet

router = DefaultRouter()

router.register(r'ubicaciones',ubicacionViewSet, basename = 'ubicaciones')

urlpatterns = router.urls