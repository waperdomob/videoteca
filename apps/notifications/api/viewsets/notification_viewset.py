from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from datetime import timedelta

from apps.notifications.api.serializers.notification_serializer import NotificactionSerializer

class notificationViewSet(viewsets.ModelViewSet):
    serializer_class=NotificactionSerializer

    def get_queryset(self, pk=None):
        """Obtiene los objetos del modelo notificación

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
        """Metodo para la creación de una notificación
        Args.
            request (json): Data con los datos para crear la notificación.

        Returns.
            Response: Mensaje, data del objeto creado y estado de la petición.
        """
        serializer = NotificactionSerializer(data=request.data)
        if serializer.is_valid():
            #print(serializer.data)
            serializer.save()
            return Response(
                    {"message": "Notificación agregada con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )

    def list(self, request):
        """Metodo para listar todos los objetos del modelo 

        Args.
            request (json): No data.

        Returns.
            Response: Data y estado de la petición.
        """
        ubicacion_serializer = self.serializer_class(self.get_queryset(), many=True)
        data =  ubicacion_serializer.data
        return Response(data, status=status.HTTP_200_OK)

