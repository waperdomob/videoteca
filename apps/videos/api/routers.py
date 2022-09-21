from rest_framework.routers import DefaultRouter

from apps.videos.api.viewsets.general_views import *
from apps.videos.api.viewsets.video_views import VideoViewSet

router = DefaultRouter()

router.register(r'videos',VideoViewSet, basename = 'videos')
router.register(r'idiomas',idiomaViewset, basename = 'idiomas')
router.register(r'tipos_de_Video',tipoVideoViewset, basename = 'tipos_de_Video')


urlpatterns = router.urls