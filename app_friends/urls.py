from django.urls import path
from .views import *

urlpatterns = [
    path('', FriendClass.as_view(), name='friend'),
    path('add/', AddFriend.as_view(), name='add_friend'),
    path('get_url/', GetFriendUrl.as_view(), name='get_friend_url')
]
