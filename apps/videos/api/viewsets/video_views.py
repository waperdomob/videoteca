from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    DjangoModelPermissionsOrAnonReadOnly,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

from datetime import timedelta

from apps.videos.api.serializers.video_serializers import (
    VideoSerializer,
    VideoSerializer2,
)
from apps.videos.funciones.vimeoAPI import cons_vim_api
from apps.videos.models import Video


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer2
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk == None:
            return (
                model.objects.filter(state=True)
                .prefetch_related("languages")
                .prefetch_related("categorias")
            )
        else:
            return (
                model.objects.filter(state=True)
                .filter(id=pk)
                .prefetch_related("languages")
                .prefetch_related("categorias")
                .first()
            )

    def list(self, request):
        video_serializer = self.serializer_class(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "videos": video_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def listPeliculas(self, request):
        video_serializer = self.serializer_class(self.get_queryset().filter(tipe_of_video_id = 1), many=True)
        data = {
            "total": self.get_queryset().count(),
            "videos": video_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def listSeries(self, request):
        video_serializer = self.serializer_class(self.get_queryset().filter(tipe_of_video_id = 2), many=True)
        data = {
            "total": self.get_queryset().count(),
            "videos": video_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        parser_classes = [MultiPartParser, FormParser]
        serializer = VideoSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer)
            videoVimeo = cons_vim_api(serializer.validated_data["code_esp"])
            duracion = timedelta(seconds=videoVimeo["duration"])
            serializer.save(
                url_vimeo_esp=videoVimeo["player_embed_url"],
                duration=duracion,
                state=True,
            )
            return Response(
                {"message": "Video agregado con exito!"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        video = self.get_queryset(pk)
        if video:
            video_serializer = self.serializer_class(video)
            return Response(video_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un video con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, pk=None):
        parser_classes = [MultiPartParser, FormParser]
        if self.get_queryset(pk):
            video_serializer = VideoSerializer(self.get_queryset(pk), data=request.data)
            if video_serializer.is_valid():
                videoVimeo = cons_vim_api(video_serializer.validated_data["code_esp"])
                duracion = timedelta(seconds=videoVimeo["duration"])
                video_serializer.save(
                    url_vimeo_esp=videoVimeo["player_embed_url"],
                    duration=duracion,
                    state=True,
                )
                return Response(video_serializer.data, status=status.HTTP_200_OK)
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        video = self.get_queryset().filter(id=pk).first()
        if video:
            video.state = False
            video.save()
            return Response(
                {"message": "Video eliminado correctamente!"}, status=status.HTTP_200_OK
            )
        return Response(
            {"error": "No existe un video con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

class VideoListAPIView(generics.ListAPIView):
    serializer_class = VideoSerializer
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        queryset = model.objects.filter(state=True)
        return queryset

class VideoCreateAPIView(generics.CreateAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Video agregado con exito!"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self, pk=None):
        if pk == None:
            queryset = Video.objects.filter(state=True)
            return queryset
        else:
            queryset = Video.objects.filter(state=True).filter(id=pk).first()
            print(queryset)
            return queryset

class VideoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, pk=None):
        if pk == None:
            return Video.objects.filter(state=True)
        else:
            return Video.objects.filter(state=True).filter(id=pk).first()

    def delete(self, request, pk):
        video = self.get_queryset().filter(id=pk).first()
        if video:
            video.state = False
            video.save()
            return Response(
                {"message": "Video eliminado correctamente!"}, status=status.HTTP_200_OK
            )
        return Response(
            {"error": "No existe un video con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            video_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(video_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un video con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            video_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data
            )
            if video_serializer.is_valid():
                video_serializer.save()
                return Response(video_serializer.data, status=status.HTTP_200_OK)
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
