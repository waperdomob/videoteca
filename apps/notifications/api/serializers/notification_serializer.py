from apps.notifications.models import  tipoNotificacion, Notificaction
from rest_framework import serializers


class tipoNotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model= tipoNotificacion
        fields= "__all__"

class NotificactionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notificaction
        fields= "__all__"