from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """Проверка на пользователя"""

    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверка на владельца или использование только безопасных методов"""

    def has_permission(self, request, view):
        return request.user.is_authenticated if request.method == "POST" else True

    def has_object_permission(self, request, view, obj):
        return True if request.method in permissions.SAFE_METHODS else obj.owner == request.user
