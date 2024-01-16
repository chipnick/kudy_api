from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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
