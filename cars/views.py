from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from cars.models import Car
from cars.paginators import Paginator
from cars.serializers import CarSerializer
from cars.services import get_params
from users.permissions import IsOwner


class CarCreateAPIView(generics.CreateAPIView):
    """ Контроллер для создания машины """

    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CarListAPIView(generics.ListAPIView):
    """ Контроллер для чтения списка машин """

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = Paginator

    def get_queryset(self):
        queryset = super().get_queryset()

        query_params = self.request.query_params

        return get_params(queryset, query_params)


class CarRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер для чтения машины """

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated]


class CarUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер для обновления машины """

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class CarDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления машины """

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
