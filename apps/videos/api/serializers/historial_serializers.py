from apps.videos.models import historial_Video
from apps.users.models import historial_user
from apps.users.api.serializers.User_serializers import CustomUserSerializer

from rest_framework import serializers

class HistorialUserSerializer(serializers.ModelSerializer): 
    usuario = CustomUserSerializer(read_only=True)
    class Meta:
        model= historial_user
        fields = "__all__"

class HistorialVideoSerializer(serializers.ModelSerializer):
    usuario = CustomUserSerializer(read_only=True)
    class Meta:
        model= historial_Video
        fields = "__all__"
