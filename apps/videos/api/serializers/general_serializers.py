from apps.videos.models import Categoria, Idioma, historial_Video, tipoVideo
from apps.users.models import historial_user
from apps.users.api.serializers.User_serializers import CustomUserSerializer
#from apps.videos.api.serializers.video_serializers import VideoSerializer2

from rest_framework import serializers


class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = "__all__"


class IdiomaSerializerV(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = "__all__"


class tipoVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoVideo
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class CategoriaSerializerV(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


