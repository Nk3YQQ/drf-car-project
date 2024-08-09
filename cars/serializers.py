from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    """ Сериализатор для машины """

    class Meta:
        model = Car
        exclude = ['owner']
