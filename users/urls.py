from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (UserRegistrationAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView,
                         UserDestroyAPIView)

app_name = UsersConfig.name

urlpatterns = [
    # User
    path('register/', UserRegistrationAPIView.as_view(), name='registration'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('', UserListAPIView.as_view(), name='user_list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('edit/<int:pk>/', UserUpdateAPIView.as_view(), name='user_edit'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

    # Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
