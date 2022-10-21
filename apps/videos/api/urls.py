from django.urls import path

from apps.videos.api.viewsets.video_views import  VideoListAPIView, VideoRetrieveAPIView

urlpatterns = [

    path('videos/retrieve/<int:pk>', VideoRetrieveAPIView.as_view(), name = 'video-detail'),
    path('videos/List', VideoListAPIView.as_view(), name = 'videos_list'),
    #path('videos/peliculas', VideoListPeliculasApiView.as_view(), name='videos_peliculas'),
    #path('videos/series', VideoListSeriesApiView.as_view(), name='videos_series'),

    #path('idiomas/', idiomaListAPIView.as_view(), name = 'idiomas'),
    #path('tipos_de_Video/', tipoVideoListAPIView.as_view(), name = 'tipos_de_Video'),
    #path('videos/create', VideoCreateAPIView.as_view(), name = 'videos-create'),
    #path('videos/retrieveUpDel/<int:pk>', VideoRetrieveUpdateDestroyAPIView.as_view(), name = 'video-detail_update_destroy'),

]