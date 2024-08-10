from django.db import models


class Car(models.Model):
    """Модель для машины"""

    FUEL_CHOICE = [
        ("бензин", "Бензин"),
        ("дизель", "Дизель"),
        ("электричество", "Электричество"),
        ("гибрид", "Гибрид"),
    ]

    TRANSMISSION_CHOICE = [
        ("механическая", "Механическая"),
        ("автоматическая", "Автоматическая"),
        ("вариатор", "Вариатор"),
        ("робот", "Робот"),
    ]

    brand = models.CharField(max_length=100, verbose_name="Бренд")
    model = models.CharField(max_length=100, verbose_name="Марка")
    year = models.IntegerField(verbose_name="Год выпуска")
    fuel_type = models.CharField(max_length=30, verbose_name="Тип топлива")
    transmission = models.CharField(max_length=30, verbose_name="Тип КПП")
    mileage = models.PositiveIntegerField(verbose_name="Пробег")
    price = models.PositiveIntegerField(verbose_name="Цена")

    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name="Владелец")

    def __str__(self):
        return f"{self.brand} {self.model} - {self.owner}"

    class Meta:
        verbose_name = "машина"
        verbose_name_plural = "машины"
