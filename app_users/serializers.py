from rest_framework import serializers

from app_users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['full_name', 'email', 'longitude', 'latitude', 'friends', 'profile_pic']


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['full_name', 'email', 'profile_pic']
