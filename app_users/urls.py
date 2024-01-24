from django.urls import path
from .views import *

urlpatterns = [
    path('', UserView.as_view(), name='set_my_location'),
    path('set_online/', SetOnlineStatus.as_view()),
]
