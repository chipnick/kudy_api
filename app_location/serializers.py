from rest_framework import serializers

from app_users.models import User


class SetUserLocation(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['x', 'y']
