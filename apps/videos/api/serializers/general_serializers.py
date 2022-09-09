from apps.videos.models import Idioma,tipoVideo

from rest_framework import serializers

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Idioma
        fields = '__all__'

class tipoVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoVideo
        fields = '__all__'