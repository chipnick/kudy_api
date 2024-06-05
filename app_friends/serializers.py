from rest_framework import serializers

from app_users.models import User


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", 'full_name', 'email', 'longitude', 'latitude', 'profile_pic', 'is_online', 'last_online', 'last_position', 'speed']


class SetOnlineStatusSerializer(serializers.Serializer):
    status = serializers.BooleanField()
