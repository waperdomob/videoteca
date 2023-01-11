from apps.location.models import  fechaRepro
from rest_framework import serializers

from apps.videos.api.serializers.historial_serializers import HistorialUserSerializer, HistorialVideoSerializer

class fechaReproSerializer(serializers.ModelSerializer):
    class Meta:
        model= fechaRepro
        fields= "__all__"