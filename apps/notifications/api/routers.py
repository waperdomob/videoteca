from rest_framework.routers import DefaultRouter

from apps.notifications.api.viewsets.tipoNotificacion_viewset import tipoNotificacionViewSet
from apps.notifications.api.viewsets.notification_viewset import notificationViewSet

router = DefaultRouter()

router.register(r'tipoNotificacion',tipoNotificacionViewSet, basename = 'tipoNotificacion')
router.register(r'notificacion',notificationViewSet, basename='notificacion')

urlpatterns = router.urls