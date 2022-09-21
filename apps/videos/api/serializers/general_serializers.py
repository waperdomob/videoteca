from apps.videos.models import Idioma,tipoVideo

from rest_framework import serializers


class IdiomaSerializer( serializers.ModelSerializer):
    class Meta:
        model  = Idioma
        fields = '__all__'

class IdiomaSerializerV(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model  = Idioma
        fields = '__all__'

        #events = serializers.SerializerMethodField()
#
    #def get_events(self, obj):
    #    events_qs = Idioma.objects.filter(artists__in=[obj.id])
    #    events = IdiomaSerializerV(
    #        events_qs, many=True, context=self.context).data
    #    return events

class tipoVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoVideo
        fields = '__all__'