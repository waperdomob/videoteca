from apps.location.models import direccionIP
from rest_framework import serializers



class ubicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model= direccionIP
        fields = "__all__"
