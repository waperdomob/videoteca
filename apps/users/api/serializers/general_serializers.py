from rest_framework import serializers
from apps.users.api.serializers.User_serializers import CustomUserSerializer
from apps.users.models import gustosUsuario
from apps.videos.api.serializers.general_serializers import CategoriaSerializer

class gustosUserSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer
    usuario = CustomUserSerializer
    class Meta:
        model= gustosUsuario
        fields = "__all__"
        
    def to_representation(self,instance):
        
        return {
        'categoria':instance.categoria.categoria if instance.categoria is not None else '',
        'usuario': instance.usuario.name if instance.usuario is not None else '',
        }

class gustosUserSerializer2(serializers.ModelSerializer):
    class Meta:
        model= gustosUsuario
        fields = "__all__"
    
