from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app_location.serializers import SetUserLocation
from app_users.models import User
from django.utils import timezone
from math import radians, sin, cos, sqrt, atan2, floor


def haversine_distance_meters(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6371000 * c
    return distance


class SetMyLocation(generics.GenericAPIView):
    serializer_class = SetUserLocation
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = SetUserLocation(data=request.data)
        print(request.headers)
        if serializer.is_valid():
            distance_m = haversine_distance_meters(request.user.longitude, request.user.latitude, request.data['longitude'], request.data['latitude'])
            self.request.user.longitude = request.data['longitude']
            self.request.user.latitude = request.data['latitude']
            self.request.user.last_position = timezone.now()
            self.request.user.speed = floor(distance_m/6)
            self.request.user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


