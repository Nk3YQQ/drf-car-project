from django.contrib import admin

from cars.models import Car


@admin.register(Car)
class CarAdminModel(admin.ModelAdmin):
    """Модель для админки машины"""

    list_display = ("brand", "model", "year", "owner")
    list_per_page = 20
