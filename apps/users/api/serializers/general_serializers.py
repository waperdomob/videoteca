from rest_framework import serializers
from apps.users.api.serializers.User_serializers import CustomUserSerializer
from apps.users.models import gustosUsuario, Commentary
from apps.videos.api.serializers.general_serializers import CategoriaSerializer
from apps.videos.api.serializers.historial_serializers import HistorialUserSerializer2
from apps.videos.api.serializers.video_serializers import VideoSerializer2

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
    
class commentarySerializer(serializers.ModelSerializer):
    historial_user = HistorialUserSerializer2(read_only=True)
    class Meta:
        model = Commentary
        fields= "__all__"

class commentarySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields= "__all__"