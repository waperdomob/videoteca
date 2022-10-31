from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.location.api.serializers.fechaRepro_serializer import *

class fechaReproViewset(viewsets.ModelViewSet):
    serializer_class = fechaReproSerializer

    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                    {"message": "Fecha agregada con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )

    def list(self, request):
        
        serializer = self.serializer_class(self.get_queryset(), many=True)
        data =  serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def list_by_user(self, request, pk=None):
        historial_by_user = self.get_queryset().filter(usuario_id=request.data['user_id'])
        data =  historial_by_user.values()
        return Response(data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Fecha actualizada con exito!"}, status=status.HTTP_200_OK)