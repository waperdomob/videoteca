from rest_framework import generics
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


class idiomaListAPIView(generics.ListAPIView):
    serializer_class = IdiomaSerializer

    def get_queryset(self):
        queryset = Idioma.objects.all()
        return queryset


class tipoVideoListAPIView(generics.ListAPIView):
    serializer_class = tipoVideoSerializer

    def get_queryset(self):
        queryset = tipoVideo.objects.all()
        return queryset
