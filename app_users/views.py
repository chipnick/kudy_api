from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app_friends.serializers import SetOnlineStatusSerializer
from .serializers import *
from app_users.models import User


class UserView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(instance=self.request.user, many=False).data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)


class SetOnlineStatus(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = SetOnlineStatusSerializer

    def post(self, request, *args, **kwargs):
        serializer = SetOnlineStatusSerializer(data=request.data)
        if serializer.is_valid():
            self.request.user.is_online = request.data['is_online']
            self.request.user.save()
            return Response(UserSerializer(instance=self.request.user, many=False).data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)