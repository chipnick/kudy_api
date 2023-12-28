from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app_friends.serializers import FriendSerializer
from app_location.serializers import SetUserLocation
from app_users.models import User
from helpers.helpers import base64UrlDecode, base64UrlEncode


class FriendClass(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def get(self, request, args, kwargs):
        return Response(FriendSerializer(instance=self.request.user.friends, many=True).data, status=status.HTTP_200_OK)

    def delete(self, request, args, kwargs):
        token = self.request.query_params.get("token")
        if token:
            friend = User.friends.filter(id=int(base64UrlDecode(token.encode('utf-8')).decode('utf-8')))
            self.request.user.friends.remove(friend)
            self.request.user.save()
            friend.friends.remove(self.request.user)
            friend.friends.save()
            return Response(FriendSerializer(instance=self.request.user.friends, many=True).data,
                            status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetFriendUrl(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        token = base64UrlEncode(f"{request.user.id}".encode('utf-8')).decode('utf-8')
        return Response(f"{token}")


class AddFriend(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        token = self.request.query_params.get("token")
        if token:
            friend = User.objects.filter(id=base64UrlDecode(token.encode('utf-8')).decode('utf-8')).first()
            self.request.user.friends.add(friend)
            self.request.user.save()
            friend.friends.add(self.request.user)
            friend.save()
            self.request.user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

