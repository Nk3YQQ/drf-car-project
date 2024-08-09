from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UsersSerializer, UsersRegistrationSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    """ Создание пользователя """

    serializer_class = UsersRegistrationSerializer


class UserListAPIView(generics.ListAPIView):
    """ Чтение всех пользователей """

    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Чтение одного пользователя """

    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Обновление пользователя """

    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление пользователя """

    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
