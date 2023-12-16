from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app_location.serializers import SetUserLocation
from app_users.models import User


class SetMyLocation(generics.GenericAPIView):
    serializer_class = SetUserLocation
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = SetUserLocation(data=request.data)
        if serializer.is_valid():
            self.request.user.x = request.data['x']
            self.request.user.y = request.data['y']
            self.request.user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


