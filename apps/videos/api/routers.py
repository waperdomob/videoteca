from rest_framework.routers import DefaultRouter

from apps.videos.api.viewsets.general_views import *
from apps.videos.api.viewsets.video_views import VideoViewSet

router = DefaultRouter()

router.register(r'videos',VideoViewSet, basename = 'videos')
router.register(r'categorias',categoriaViewset, basename = 'categorias')
router.register(r'idiomas',idiomaViewset, basename = 'idiomas')
router.register(r'tipos_de_Video',tipoVideoViewset, basename = 'tipos_de_Video')
router.register(r'historialUser', historialUserViewset, basename='historialUser')
router.register(r'historialVideo', historialVideoViewset,basename='historialVideo')

urlpatterns = router.urls