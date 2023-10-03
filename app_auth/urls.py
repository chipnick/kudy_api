from django.urls import path

from app_auth.views import SignUpView, LoginView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
]
