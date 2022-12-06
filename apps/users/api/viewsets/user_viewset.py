from django.shortcuts import get_object_or_404
import os
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.api.serializers.User_serializers import (
    CustomUserSerializer, UserSerializer, UserListSerializer, UpdateUserSerializer,
    PasswordSerializer
)

class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects\
                            .filter(is_active=True)\
                            .values('id', 'username','email','name')
        return self.queryset

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        """Metodo para actualizar la contraseña

        Args.
            request (password): Nueva contraseña
            pk (id, optional): id del usuario al que se le va actualizar la contraseña. Defaults to None.

        Returns.
            Response: Mensaje de exito o error y estado de la petición.
        """        
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({
                'message': 'Contraseña actualizada correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la información enviada',
            'errors': password_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """Metodo para listar a todos los usuario

        Args.
            request (_type_): No data

        Returns.
            Response: Data de todos los usuarios y estado de la petición
        """        
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Metodo para la creación de un nuevo usuario

        Args.
            request (json): Data con los datos para el registro del usuario

        Returns.
            Response: Mensaje y estado de la petición
        """        
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario registrado correctamente.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Hay errores en el registro',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Metodo para ver los detalles del usuario

        Args.
            request (_type_): No data
            pk (id, optional): Id del usuario a consultar. Defaults to None.

        Returns.
            Response: Data del usuario y estado de la petición.
        """        
        user = self.get_object(pk)
        user_serializer = CustomUserSerializer(user)
        if user:
            return Response(user_serializer.data,status=status.HTTP_200_OK)
        return Response({'message':'No existe un usuario con ese id'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Metodo para actualizar al usuario

        Args.
            request (json): Datos a actualizar del usuario
            pk (id, optional): Id del usuario que se va a actualizar. Defaults to None.

        Returns.
            Response: Mensaje de exito o error, estado de la petición.
        """        
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self, request, pk=None):
        """Metodo para actualizar la imagen del usuario

        Args.
            request (json): Data para actualizar al usuario
            pk (id, optional): Id del usuario a actualizar. Defaults to None.

        Returns.
            Response: Mensaje de exito o error, estado de la petición.
        """        
        user = self.get_object(pk)
        user_serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():
            if user.image:
                os.remove(user.image.path)
            user_serializer.save()
            return Response({
                'message': 'Imagen de perfil actualizada correctamente'
            },status=status.HTTP_200_OK)
        return Response({
                'Error': 'Hubo un error al actualizar los datos'
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Metodo para "Eliminar" un usuario. La eliminación es lógica, por lo que solo se cambia el estado del usuario a False

        Args.
            request (_type_): No data
            pk (id, optional): Id del usuario a eliminar. Defaults to None.

        Returns.
            Response: Mensaje de exito o error, estado de la petición.
        """        
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'Usuario eliminado correctamente'
            })
        return Response({
            'message': 'No existe el usuario que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)