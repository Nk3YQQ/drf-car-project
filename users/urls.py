from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (CurrentUserAPIView, UserDestroyAPIView, UserRegistrationAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    # Auth
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("registration/", UserRegistrationAPIView.as_view(), name="registration"),
    path("login/", TokenObtainPairView.as_view(), name="login"),

    # User
    path("me/", CurrentUserAPIView.as_view(), name="current_user"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("<int:pk>/edit/", UserUpdateAPIView.as_view(), name="user_edit"),
    path("<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_delete"),
]
