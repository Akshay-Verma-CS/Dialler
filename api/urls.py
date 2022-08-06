from django.urls import path
from .views import RegisterUserAPIView, UserDetailAPI

urlpatterns = [
    path("get-details",UserDetailAPI.as_view()),
    path("register",RegisterUserAPIView.as_view()),
]