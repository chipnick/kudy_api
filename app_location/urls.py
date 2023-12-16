from django.urls import path
from .views import *

urlpatterns = [
    path('set_my_location', SetMyLocation.as_view(), name='set_my_location')
]
