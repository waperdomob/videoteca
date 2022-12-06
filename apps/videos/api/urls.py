from django.urls import path
from apps.videos.api.viewsets.video_views import   VideoRetrieveAPIView
urlpatterns = [
    path('videos/retrieve/<int:pk>', VideoRetrieveAPIView.as_view(), name = 'video-detail')
]