from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from datetime import timedelta

from apps.notifications.api.serializers.notification_serializer import tipoNotificacionSerializer

class tipoNotificacionViewSet(viewsets.ModelViewSet):
    serializer_class=tipoNotificacionSerializer

    def get_queryset(self, pk=None):    
        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    #def create(self, request, *args, **kwargs):
    #    serializer = tipoNotificacionSerializer(data=request.data)
    #    if serializer.is_valid():
    #        #print(serializer.data)
    #        serializer.save()
    #        return Response(
    #                {"message": "tipoNotificacion agregado con exito!","data":serializer.data}, status=status.HTTP_200_OK
    #            )

    #def list(self, request):
    #    ubicacion_serializer = self.serializer_class(self.get_queryset(), many=True)
    #    data =  ubicacion_serializer.data
    #    return Response(data, status=status.HTTP_200_OK)
