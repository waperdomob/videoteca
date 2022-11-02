
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.videos.models import Idioma, tipoVideo, Categoria
from apps.videos.api.serializers.general_serializers import *


class categoriaViewset(viewsets.ModelViewSet):

    serializer_class = CategoriaSerializer

    def get_queryset(self):
        queryset = Categoria.objects.all()
        return queryset


class idiomaViewset(viewsets.ModelViewSet):
    """Clase para el control del modelo Idioma

    Parameters.
        viewsets (ModelViewSet)---> provee por default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.

    Returns:
        queryset: Retorna un objeto del modelo Idioma
    """

    serializer_class = IdiomaSerializer

    def get_queryset(self):
        queryset = Idioma.objects.all()
        return queryset


class tipoVideoViewset(viewsets.ModelViewSet):
    serializer_class = tipoVideoSerializer

    def get_queryset(self):
        queryset = tipoVideo.objects.all()
        return queryset


class historialUserViewset(viewsets.ModelViewSet):
    serializer_class = HistorialUserSerializer

    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    def create(self, request, *args, **kwargs):
        serializer = HistorialUserSerializer(data=request.data)
        if serializer.is_valid():
            #print(serializer.data)
            serializer.save()
            return Response(
                    {"message": "historial agregado con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )

    def list(self, request):
        
        historialUsers_serializer = self.serializer_class(self.get_queryset(), many=True)
        data =  historialUsers_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def list_by_user(self, request, pk=None):
        historial_by_user = self.get_queryset().filter(usuario_id=request.data['user_id'])
        data =  historial_by_user.values()
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        historial = self.get_queryset(pk)
        if historial:
            historial_serializer = self.serializer_class(historial)
            return Response(historial_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un historial con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "historial actualizado con exito!"}, status=status.HTTP_200_OK)

class historialVideoViewset(viewsets.ModelViewSet):
    serializer_class = HistorialVideoSerializer

    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    def create(self, request, *args, **kwargs):
        serializer = HistorialVideoSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(
                    {"message": "historial agregado con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )

    def list(self, request):
        
        historialUsers_serializer = self.serializer_class(self.get_queryset(), many=True)
        data =  historialUsers_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def list_by_video(self, request, pk=None):
        historial_by_video = self.get_queryset().filter(video_id=request.data['video_id'])
        data =  historial_by_video.values()
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        historial = self.get_queryset(pk)
        if historial:
            historial_serializer = self.serializer_class(historial)
            return Response(historial_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un historial con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "historial actualizado con exito!"}, status=status.HTTP_200_OK)