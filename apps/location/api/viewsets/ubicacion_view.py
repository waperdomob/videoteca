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
        """Obtiene los objetos del modelo direccionIP

        Args.
            pk (id, optional): Id del objeto a buscar. Defaults to None.

        Returns.
            Object: Si hay un pk retorna un objeto en específico, caso contrario traera la lista de todos los objectos.
        """        
        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    def create(self, request, *args, **kwargs):
        """Metodo para la creación de una ubicación la cual es relación entre historial_user e historial_video

        Args.
            request (json): Data con los datos para crear la ubicación.

        Returns.
            Response: Mensaje, data del objeto creado y estado de la petición.
        """
        serializer = ubicacionSerializer(data=request.data)
        if serializer.is_valid():
            #print(serializer.data)
            serializer.save()
            return Response(
                    {"message": "ubicación agregada con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )

    def list(self, request):
        """Metodo para listar todos los objetos del modelo direccionIP

        Args.
            request (json): No data.

        Returns.
            Response: Data y estado de la petición.
        """
        ubicacion_serializer = self.serializer_class(self.get_queryset(), many=True)
        data =  ubicacion_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def list_by_historial(self, request, pk=None):
        """Metodo para listar todos los objetos del modelo direccionIP correspondientes a historial_user.

        Args.
            request (json): Data enviado desde el frontend con historial_user para realizar la consulta.

        Returns.
            Response: Data y estado de la petición.
        """
        ubicacion_by_historial = self.get_queryset().filter(historial_user_id=request.data['histUser_id'])
        data =  ubicacion_by_historial.values()
        return Response(data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        """Metodo para actualizar la ubicación

        Args.
            request (json): Data enviada desde el frontend para actualizar el objeto.
            pk (id, optional): id del objeto a actualizar. Defaults to None.

        Returns.
            Response: Mensaje y estado de la petición.
        """        
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "ubicación actualizada con exito!"}, status=status.HTTP_200_OK)