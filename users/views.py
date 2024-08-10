from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsUser
from users.serializers import UsersRegistrationSerializer, UsersSerializer


@extend_schema_view(create=extend_schema(description="Register a new user"))
class UserRegistrationAPIView(generics.CreateAPIView):
    """Создание пользователя"""

    serializer_class = UsersRegistrationSerializer


@extend_schema_view(retrieve=extend_schema(description="Read a current user"))
class CurrentUserAPIView(generics.RetrieveAPIView):
    """Чтение текущего пользователя"""

    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


@extend_schema_view(retrieve=extend_schema(description="Retrieve a specific user by id"))
class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Чтение одного пользователя"""

    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    update=extend_schema(description="Update an existing user, if current user is owner of this account"),
    particular_update=extend_schema(description="Particular update user, if current user is account's owner"),
)
class UserUpdateAPIView(generics.UpdateAPIView):
    """Обновление пользователя"""

    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


@extend_schema_view(
    destroy=extend_schema(description="Delete an existing user, if current user is owner of this account"),
)
class UserDestroyAPIView(generics.DestroyAPIView):
    """Удаление пользователя"""

    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUser]
