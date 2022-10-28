from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from datetime import timedelta

from apps.location.api.serializers.ubicacion_serializer import ubicacionSerializer

class ubicacionViewSet(viewsets.ModelViewSet):
    serializer_class=ubicacionSerializer

    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    def create(self, request, *args, **kwargs):
        serializer = ubicacionSerializer(data=request.data)
        if serializer.is_valid():
            #print(serializer.data)
            serializer.save()
            return Response(
                    {"message": "ubicación agregada con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )

    def list(self, request):

        ubicacion_serializer = self.serializer_class(self.get_queryset(), many=True)
        data =  ubicacion_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def list_by_historial(self, request, pk=None):
        ubicacion_by_historial = self.get_queryset().filter(historial_user_id=request.data['histUser_id'])
        data =  ubicacion_by_historial.values()
        return Response(data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "ubicación actualizada con exito!"}, status=status.HTTP_200_OK)