import django_filters.rest_framework as filters

from cars.models import Car


class CarFilter(filters.FilterSet):
    """Фильтрация для машин"""

    mileage_min = filters.NumberFilter(field_name="mileage", lookup_expr="gte")
    mileage_max = filters.NumberFilter(field_name="mileage", lookup_expr="lte")
    price_min = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Car
        fields = (
            "brand",
            "model",
            "year",
            "fuel_type",
            "transmission",
            "mileage_min",
            "mileage_max",
            "price_min",
            "price_max",
        )
