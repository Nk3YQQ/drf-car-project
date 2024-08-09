from django.urls import path

from cars.apps import CarConfig
from cars.views import CarCreateAPIView, CarListAPIView, CarRetrieveAPIView, CarUpdateAPIView, CarDestroyAPIView

app_name = CarConfig.name

urlpatterns = [
    path('create/', CarCreateAPIView.as_view(), name='car_create'),
    path('', CarListAPIView.as_view(), name='car_list'),
    path('<int:pk>/', CarRetrieveAPIView.as_view(), name='car_retrieve'),
    path('<int:pk>/edit/', CarUpdateAPIView.as_view(), name='car_update'),
    path('<int:pk>/delete/', CarDestroyAPIView.as_view(), name='car_destroy')
]
