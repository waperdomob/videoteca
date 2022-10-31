from apps.videos.models import Categoria, Idioma, historial_Video, tipoVideo
from apps.users.models import historial_user
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

class HistorialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= historial_user
        fields = "__all__"

class HistorialVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model= historial_Video
        fields = "__all__"
