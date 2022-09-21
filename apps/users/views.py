from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.api.serializers import CustomUserSerializer

# Create your views here.


class userToken(APIView):
    def get(self, request, *args, **kwars):
        username = request.GET.get("username")
        try:
            user_token = Token.objects.get(
                user=CustomUserSerializer.Meta.model.objects.filter(
                    username=username
                ).first()
            )
            print(user_token)
            return Response({"token": user_token.key})
        except:
            return Response(
                {"error": "Credenciales enviadas incorrectas!"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if login_serializer.is_valid():
            user = login_serializer.validated_data["user"]
            if user.is_active:
                user_serializer = CustomUserSerializer(user)
                token, created = Token.objects.get_or_create(user=user)
                if created:
                    return Response(
                        {
                            "token": token.key,
                            "user": user_serializer.data,
                            "message": "Inicio de sesión exitoso!",
                        },
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    """all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()

                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({'token':token.key, 'user':user_serializer.data,'message': 'Inicio de sesión exitoso!'},status=status.HTTP_201_CREATED)"""

                    return Response(
                        {"Message": "Ya hay una sesión activa con este usuario"},
                        status=status.HTTP_409_CONFLICT,
                    )
            else:
                return Response(
                    {"error": "Este usuario no puede iniciar sesión"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"error": "Nombre de usuario y/o contraseña incorrectos."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({"mensaje": "Hola desde Response"}, status=status.HTTP_200_OK)


class logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = request.POST["token"]
            token = Token.objects.filter(key=token).first()
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get("_auth_user_id")):
                            session.delete()
                token.delete()
                session_message = "Sesiones de usuario eliminadas."
                token_message = "Token eliminado."

                return Response(
                    {
                        "token_message": token_message,
                        "session_message": session_message,
                    },
                    status=status.HTTP_200_OK,
                )

            return Response(
                {"error": "No se ha encontrado un usuario con estas credenciales."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except:
            return Response(
                {"error": "No se ha encontrado un token en la petición."},
                status=status.HTTP_409_CONFLICT,
            )
