from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    """ Модель для админки пользователя """

    list_display = ('first_name', 'last_name', 'email')
    list_per_page = 20
