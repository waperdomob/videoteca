
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.videos.models import Idioma, tipoVideo, Categoria
from apps.videos.api.serializers.general_serializers import *
from apps.videos.api.serializers.historial_serializers import *

import json
class categoriaViewset(viewsets.ModelViewSet):
    """Clase para el control del modelo Categoria

    Parameters.
        viewsets (ModelViewSet)---> provee por default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.

    Returns:
        queryset: Retorna un objeto del modelo Categoria
    """    
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
    """Clase para el control del modelo tipoVideo

    Parameters.
        viewsets (ModelViewSet)---> provee por default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.

    Returns:
        queryset: Retorna un objeto del modelo tipoVideo
    """    
    serializer_class = tipoVideoSerializer

    def get_queryset(self):
        queryset = tipoVideo.objects.all()
        return queryset


class historialUserViewset(viewsets.ModelViewSet):
    
    serializer_class = HistorialUserSerializer

    def get_queryset(self, pk=None):
        """Obtiene el objeto del modelo historial_user consultado

        Args.
            pk (id, optional): Id del historial_user en la base de datos. Defaults to None.

        Returns.
            object: Ojeto del modelo historial_user correspondiente al pk ingresado, si no hay pk se retornan todos.
        """
        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    def create(self, request, *args, **kwargs):
        """Metodo para registrar un nuevo historial_user

        Args.
            request (json): Data enviada desde el frontend para registrar un nuevo historial_user

        Returns.
            Response: Mensaje, data del objeto creado y estado de la petición.
        """
        serializer = HistorialUserSerializer3(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(
                    {"message": "historial agregado con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )

    def list(self, request):
        """Metodo para listar todos los historial_user

        Args.
            request (_type_): No data

        Returns.
            Response: Data de todos los historial_user y estado de la petición.
        """
        historialUsers_serializer = self.serializer_class(self.get_queryset(), many=True)
        data =  historialUsers_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def list_4_comments(self, request):
        """Metodo para listar todos los historial_user filtrando comentarios activos

        Args.
            request (_type_): No data

        Returns.
            Response: Data de todos los historial_user y estado de la petición.
        """
        historialUsers_serializer = self.serializer_class(self.get_queryset().filter(approved_by_m=True).filter(commentary__isnull=False).order_by('-id'), many=True)
        data =  historialUsers_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def list_by_user(self, request, pk=None):
        """Metodo para consultar todos los historiales por usuario específico

        Args.
            request (json): Data enviada desde el frontend con el id del usuario para realizar la consulta.
            pk (id, optional): Id del historial_user. Defaults to None.

        Returns.
            Response: Data todos los historiales buscados y estado de la petición.
        """        
        historial_by_user = self.serializer_class(self.get_queryset().filter(usuario_id=request.data['user_id']), many=True)
        data =  historial_by_user.data
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Metodo para consultar un historial en específico.

        Args.
            request (_type_): No data.
            pk (Id, optional): Id del historial_user a consultar. Defaults to None.

        Returns.
            Response: Data del historial_user consultado y estado del a petición, mensaje de error si no hay Data.
        """
        historial = self.get_queryset(pk)
        if historial:
            historial_serializer = self.serializer_class(historial)
            return Response(historial_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un historial con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def partial_update(self, request, pk=None):
        """Metodo para la actualización parcial de un historial_user

        Args.
            request (json): Datos a actualizar del historial_user
            pk (id, optional): Id del historial_user a actualizar. Defaults to None.

        Returns.
            Response: Mensaje y estado de la petición.
        """
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "historial actualizado con exito!"}, status=status.HTTP_200_OK)

class historialVideoViewset(viewsets.ModelViewSet):
    serializer_class = HistorialVideoSerializer

    def get_queryset(self, pk=None):
        """Obtiene el objeto del modelo historial_Video consultado

        Args.
            pk (id, optional): Id del historial_Video en la base de datos. Defaults to None.

        Returns.
            object: Ojeto del modelo historial_Video correspondiente al pk ingresado, si no hay pk se retornan todos.
        """
        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    def create(self, request, *args, **kwargs):
        """Metodo para registrar un nuevo historial_Video

        Args.
            request (json): Data enviada desde el frontend para registrar un nuevo historial_Video

        Returns.
            Response: Mensaje, data del objeto creado y estado de la petición.
        """
        serializer = HistorialVideoSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(
                    {"message": "historial agregado con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )

    def list(self, request):
        """Metodo para listar todos los historial_Video

        Args.
            request (_type_): No data

        Returns.
            Response: Data de todos los historial_Video y estado de la petición.
        """
        historialUsers_serializer = self.serializer_class(self.get_queryset(), many=True)
        data =  historialUsers_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def list_by_video(self, request, pk=None):
        """Metodo para consultar todos los historiales por video específico

        Args.
            request (json): Data enviada desde el frontend con el id del video para realizar la consulta.
            pk (id, optional): Id del historial_video. Defaults to None.

        Returns.
            Response: Data todos los historiales buscados y estado de la petición.
        """
        historial_by_video = self.get_queryset().filter(video_id=request.data['video_id'])
        data =  historial_by_video.values()
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Metodo para consultar un historial en específico.

        Parameters.
            request (_type_): No data.
            pk (Id, optional): Id del historial_Video a consultar. Defaults to None.

        Returns.
            Response: Data del historial_Video consultado y estado del a petición, mensaje de error si no hay Data.
        """
        historial = self.get_queryset(pk)
        if historial:
            historial_serializer = self.serializer_class(historial)
            return Response(historial_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un historial con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def partial_update(self, request, pk=None):
        """Metodo para la actualización parcial de un historial_Video

        Args.
            request (json): Datos a actualizar del historial_Video
            pk (id, optional): Id del historial_Video a actualizar. Defaults to None.

        Returns.
            Response: Mensaje y estado de la petición.
        """
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "historial actualizado con exito!"}, status=status.HTTP_200_OK)