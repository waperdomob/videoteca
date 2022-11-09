from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from apps.users.api.serializers.User_serializers import CustomTokenOptainPairSerializer, CustomUserSerializer
from apps.users.models import User



class login(TokenObtainPairView):
    serializer_class = CustomTokenOptainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username','')
        password = request.data.get('password','')

        user = authenticate(
            username = username,
            password = password
        )
        if user:
            login_serializer = self.serializer_class(data= request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'access_token': login_serializer.validated_data.get('access'),
                    'refresh_token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message':'Inicio de sesión exitoso!'
                }, status=status.HTTP_200_OK) 
            return Response({'error':'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

class logout(GenericAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    """ def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user',0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST) """

