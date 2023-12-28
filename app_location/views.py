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
        print(request.headers)
        if serializer.is_valid():
            self.request.user.longitude = request.data['longitude']
            self.request.user.latitude = request.data['latitude']
            self.request.user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


