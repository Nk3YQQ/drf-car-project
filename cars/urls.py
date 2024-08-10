from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cars.apps import CarConfig
from cars.views import CarViewSet

app_name = CarConfig.name

router = DefaultRouter()
router.register(r"cars", CarViewSet, basename="car")

urlpatterns = [path("", include(router.urls))]
