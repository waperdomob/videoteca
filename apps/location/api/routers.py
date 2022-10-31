from rest_framework.routers import DefaultRouter

from apps.location.api.viewsets.ubicacion_view import ubicacionViewSet
from apps.location.api.viewsets.fechaRepro_view import fechaReproViewset

router = DefaultRouter()

router.register(r'ubicaciones',ubicacionViewSet, basename = 'ubicaciones')
router.register(r'fechaReprods',fechaReproViewset, basename='fechaReprods')

urlpatterns = router.urls