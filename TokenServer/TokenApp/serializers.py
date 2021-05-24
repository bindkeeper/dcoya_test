from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "password", "jwt")

    password = serializers.CharField(style={'input_type': 'password'})

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data["username"], password=validated_data["password"])
        return user


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username",)

