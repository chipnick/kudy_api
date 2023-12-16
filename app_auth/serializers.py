from rest_framework import serializers

from app_users.models import User


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password']


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']
