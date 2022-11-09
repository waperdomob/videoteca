from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.users.api.serializers.general_serializers import *

class gustosUserViewset(viewsets.ModelViewSet):
    serializer_class = gustosUserSerializer

    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    def create(self, request, *args, **kwargs):
        serializer = gustosUserSerializer2(data=request.data)
        if serializer.is_valid():
            gusto_by_user = gustosUsuario.objects.all().filter(usuario=serializer.validated_data.get('usuario')).filter(categoria=serializer.validated_data.get('categoria'))            
            if gusto_by_user:
                print(gusto_by_user)
                return Response(
                    {"error": "Ya tiene registrada la preferencia seleccionada!"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                serializer.save()
            return Response(
                    {"message": "Preferencia agregada con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )
        return Response(
            {"error": "No ha seleccionado una opción correcta!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def list(self, request):        
        gustoUsers_serializer = self.serializer_class(self.get_queryset())
        data =  gustoUsers_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def list_by_user(self, request, pk=None):
        gusto_by_user = self.serializer_class(self.get_queryset().filter(usuario=request.data['user_id']), many=True)
        data =  gusto_by_user.data
        if data:
            return Response(data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No exiten preferencias para el usuario!"},
            status=status.HTTP_404_NOT_FOUND,
        )

    def retrieve(self, request, pk=None):
        gusto = self.get_queryset(pk)
        if gusto:
            gusto_serializer = self.serializer_class(gusto)
            return Response(gusto_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe una Preferencia con estos datos!"},
            status=status.HTTP_404_NOT_FOUND,
        )
    
    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Preferencia actualizada con exito!"}, status=status.HTTP_200_OK)
