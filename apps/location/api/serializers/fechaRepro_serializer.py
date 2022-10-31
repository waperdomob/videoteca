from apps.location.models import  fechaRepro
from rest_framework import serializers

from apps.videos.api.serializers.general_serializers import HistorialUserSerializer, HistorialVideoSerializer

class fechaReproSerializer(serializers.ModelSerializer):
    hist_user = HistorialUserSerializer
    hist_video = HistorialVideoSerializer
    class Meta:
        model= fechaRepro
        fields= "__all__"