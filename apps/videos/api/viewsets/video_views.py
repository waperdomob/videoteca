from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

from datetime import timedelta
import os

from apps.videos.api.serializers.video_serializers import (
    VideoSerializer,
    VideoSerializer2,
)
from apps.videos.funciones.vimeoAPI import cons_vim_api
from apps.videos.models import Video


class VideoViewSet(viewsets.ModelViewSet):
    
    serializer_class = VideoSerializer2
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self, pk=None):
        """Obtiene el objeto del modelo Video consultado

        Args.
            pk (id, optional): Id del video en la base de datos. Defaults to None.

        Returns.
            object: Ojeto del modelo Video correspondiente al pk ingresado, si no hay pk se retornan todos los que tengan state = True
        """        
        model = self.get_serializer().Meta.model
        if pk == None:
            return (
                model.objects.filter(state=True).order_by('-upload_date')
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
        """Metodo para obtener la lista completa de videos registrados en la base de datos

        Args.
            request (_type_): No data

        Returns.
            Response: Respuesta con la data y el estado de la respuesta (200 OK)
        """
        video_serializer = self.serializer_class(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "videos": video_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def listPeliculas(self, request):
        """Metodo para obtener la lista completa de videos clasificados como peliculas(Videos unicos, no serie) registrados en la base de datos

        Args.
            request (_type_): No data

        Returns.
            Response: Respuesta con la data y el estado de la respuesta (200 OK)
        """
        video_serializer = self.serializer_class(self.get_queryset().filter(tipe_of_video_id = 1), many=True)
        data = {
            "total": self.get_queryset().count(),
            "videos": video_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def listSeries(self, request):
        """Metodo para obtener la lista completa de videos clasificados como series registrados en la base de datos

        Args.
            request (_type_): No data

        Returns.
            Response: Respuesta con la data y el estado de la respuesta (200 OK)
        """
        video_serializer = self.serializer_class(self.get_queryset().filter(tipe_of_video_id = 2), many=True)
        data = {
            "total": self.get_queryset().count(),
            "videos": video_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def listCasos(self, request):
        """Metodo para obtener la lista completa de videos clasificados como casos registrados en la base de datos

        Args.
            request (_type_): No data

        Returns.
            Response: Respuesta con la data y el estado de la respuesta (200 OK)
        """
        video_serializer = self.serializer_class(self.get_queryset().filter(tipe_of_video_id = 3), many=True)
        data = {
            "total": self.get_queryset().count(),
            "videos": video_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """Metodo para registrar un nuevo video

        Args.
            request (json): Datos enviados desde el frontend para el registro de un nuevo video

        Returns.
            Response: Respuesta con mensaje de exito o error al momento de registrar el video.
        """
        parser_classes = [MultiPartParser, FormParser]
        serializer = VideoSerializer(data=request.data)

        if serializer.is_valid():
            videoVimeo = cons_vim_api(serializer.validated_data["code_esp"])
            created_time = videoVimeo["created_time"]
            duracion = timedelta(seconds=videoVimeo["duration"])
            consulta = Video.objects.filter(code_esp = serializer.validated_data["code_esp"] ).exists()
            if consulta:
                return Response(
                    {"ERROR": "¡Ya existe un video con este código!"}, status=status.HTTP_409_CONFLICT
                )
            serializer.save(
                duration=duracion,
                create_date=created_time,
                state=True,
            )
            return Response(
                {"message": "Video agregado con exito!"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Metodo para ver el detalle de un vídeo

        Args.
            request (_type_): No data
            pk (id , optional): Id del vídeo a consultar. Defaults to None.

        Returns.
            Response: Data del vídeo consultado o mensaje de error si no se encuentra el vídeo y estado de la respuesta(200 Ok o 400 Bad_request)
        """        
        video = self.get_queryset(pk)
        if video:
            video_serializer = self.serializer_class(video)
            return Response(video_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un video con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, pk=None):
        """Metodo para actualizar un registro(Vídeo)

        Args.
            request (json): Data con la información para actualizar.
            pk (id, optional): Id del vídeo a actualizar. Defaults to None.

        Returns.
            Response: Mensaje de exito o error al hacer la petición, junto con el status de la petición.
        """        
        parser_classes = [MultiPartParser, FormParser]
        video = self.get_queryset(pk)
        if self.get_queryset(pk):
            video_serializer = VideoSerializer(self.get_queryset(pk), data=request.data)
            if video_serializer.is_valid():
                if video_serializer.validated_data.get('featured_image'):
                    if video.featured_image:
                        os.remove(video.featured_image.path)
                if video_serializer.validated_data.get('min_image'):
                    if video.featured_image:
                        os.remove(video.min_image.path)
                videoVimeo = cons_vim_api(video_serializer.validated_data["code_esp"])
                duracion = timedelta(seconds=videoVimeo["duration"])
                video_serializer.save(
                    url_vimeo_esp=videoVimeo["player_embed_url"],
                    duration=duracion,
                    state=True,
                )
                return Response({"message": "Video actualizado con exito!"}, status=status.HTTP_200_OK)
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """Metodo para la actualización parcial de un vídeo.

        Args.
            request (json): Datos a actualizar
            pk (id, optional): Id del vídeo a actualizar. Defaults to None.

        Returns.
            Response: Mensaje y estatus de la petición.
        """        
        parser_classes = [MultiPartParser, FormParser]
        if self.get_queryset(pk):
            video_serializer = VideoSerializer(self.get_queryset(pk), data=request.data,partial=True)
            if video_serializer.is_valid():
                video_serializer.save()
                return Response({"message": "video actualizado con exito!"}, status=status.HTTP_200_OK)
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        """Metodo para la eliminación de un vídeo. Esta eliminación es lógica, solo se cambia el estado del video a False

        Args.
            request (): No data
            pk (id): Id del video a eliminar.

        Returns.
            Response: Mensaje y estado de la petición.
        """        
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

