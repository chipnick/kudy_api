from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from app_auth.serializers import SignUpSerializer, LoginSerializer
from app_users.models import User
from app_users.serializers import UserSerializer


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(email=request.data['email']).first()
            if user:
                return Response({
                    'status': 'error',
                    'message': 'User with this email already exist.'
                }, status=status.HTTP_400_BAD_REQUEST)
            user = User(
                full_name=request.data['full_name'],
                email=request.data['email'],
            )
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({
                'status': 'success',
                'data': {
                    'user': UserSerializer(instance=user).data,
                    'token': token
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(email=request.data['email']).first()
            if user:
                if not check_password(request.data['password'], user.password):
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    "user": UserSerializer(instance=user, many=False).data,
                    "token": token.key,
                }, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
