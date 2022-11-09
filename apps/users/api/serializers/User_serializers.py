from apps.users.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenOptainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','name','is_superuser','image')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def validate(self, data):
        if data['username'] != data['email']:
            raise serializers.ValidationError('username y email tienen que ser el mismo')
        return data
    
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name')

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password':'Debe ingresar ambas contraseñas iguales'}
            )
        return data

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'name': instance['name'],
            'email': instance['email']
        }

