import django_filters.rest_framework as filters
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from cars.filters import CarFilter
from cars.models import Car
from cars.paginators import Paginator
from cars.serializers import CarOwnerSerializer, CarSerializer
from users.permissions import IsOwnerOrReadOnly


@extend_schema_view(
    list=extend_schema(description="Retrieve a list of cars"),
    retrieve=extend_schema(description="Retrieve a specific car by id"),
    create=extend_schema(description="Create a new car object"),
    update=extend_schema(description="Update an existing car"),
    particular_update=extend_schema(description="Particular update an existing car"),
    destroy=extend_schema(description="Delete an existing car"),
)
class CarViewSet(ModelViewSet):
    """Вьюсет для машины"""

    serializer_class = CarSerializer
    queryset = Car.objects.all().order_by("id")
    pagination_class = Paginator
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CarFilter

    def get_serializer_class(self):
        if self.action in ("create", "list"):
            serializer_class = CarSerializer

        else:
            serializer_class = CarOwnerSerializer

        return serializer_class

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
