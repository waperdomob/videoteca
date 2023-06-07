from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.parsers import MultiPartParser, FormParser


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

class commentaryViewset(viewsets.ModelViewSet):
    serializer_class = commentarySerializer

    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk == None:
            return model.objects.all()
        else:
            return model.objects.get(id=pk)

    def create(self, request, *args, **kwargs):
        serializer = commentarySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                    {"message": "Comentario agregado con exito!","data":serializer.data}, status=status.HTTP_200_OK
                )
        return Response(
            {"error": "Ocurrió un problema!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def list(self, request):        
        commentary_serializer = self.serializer_class(self.get_queryset(), many=True)
        data =  commentary_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def list_by_video(self, request, pk=None):
        
        commentaries_by_video = self.serializer_class(self.get_queryset().filter(video=request.data['video_id']).order_by('-created_date'), many=True)
        data =  commentaries_by_video.data
        if data:
            return Response(data, status=status.HTTP_200_OK)
        else :
            return Response(
                {"error": "No existe un comentario con estos datos!"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def retrieve(self, request, pk=None):
        commentary = self.get_queryset(pk)
        if commentary:
            commentary_serializer = self.serializer_class(commentary)
            return Response(commentary_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un comentario con estos datos!"},
            status=status.HTTP_404_NOT_FOUND,
        )
    
    def partial_update(self, request, pk=None):
        parser_classes = [MultiPartParser, FormParser]
        if self.get_queryset(pk):
            commentary_serializer = commentarySerializer2(self.get_queryset(pk), data=request.data,partial=True)
            if commentary_serializer.is_valid():
                commentary_serializer.save()
                return Response({"message": "Comentario actualizado con exito!"}, status=status.HTTP_200_OK)
            return Response(commentary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)