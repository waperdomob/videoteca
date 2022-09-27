from rest_framework import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser

from apps.videos.models import Idioma, Video, tipoVideo
from apps.videos.api.serializers.general_serializers import IdiomaSerializer, IdiomaSerializerV,tipoVideoSerializer

class VideoSerializer(serializers.ModelSerializer):
    #languages = IdiomaSerializer(source='get_lenguages_video', many=True)
    languages = IdiomaSerializerV(many=True, queryset= Idioma.objects.all())
    #languages = IdiomaSerializer(many=True, read_only=True)
    #languages = IdiomaSerializerV
    tipe_of_video = tipoVideoSerializer
    class Meta:
        model=Video
        fields = [
                'id', 'code_esp', 'code_engl','title_espanol', 'title_english', 'title_cap_esp', 'title_cap_english', 'description_esp', 'description_english', 'duration', 'featured_image', 'min_image','repro_counter', 'score', 'tipe_of_video', 'languages','state','url_vimeo_esp','url_vimeo_eng'
                ]
    #def to_representation(self,instance):
    #        return {
    #            'id': instance.id,
    #            'code':instance.code,
    #            'title_espanol': instance.title_espanol,
    #            'title_english': instance.title_english,
    #            'title_cap_esp': instance.title_cap_esp,
    #            'title_cap_english': instance.title_cap_english,
    #            'description_esp': instance.description_esp,
    #            'description_english': instance.description_english,
    #            'duration': instance.duration,
    #            'repro_counter': instance.repro_counter,
    #            'score': instance.score,
    #            'tipe_of_video': instance.tipe_of_video.tipe_video if instance.tipe_of_video is not None else '',
    #            'languages': instance.languages
    #        }
    
    def create(self, validated_data):
        idioms = validated_data.pop('languages')#se obtiene una lista con los idiomas seleccionados
        instance = Video.objects.create(**validated_data) #se crea el objeto del formulario json para Video
        for i in idioms:
            instance.languages.add(i.id) #se guarda la relacion m2m
        return instance