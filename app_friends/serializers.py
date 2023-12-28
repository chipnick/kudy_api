from rest_framework import serializers

from app_users.models import User


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['full_name', 'email', 'longitude', 'latitude']
