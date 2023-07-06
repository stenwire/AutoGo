from rest_framework.permissions import BasePermission


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_superuser
        if request.method == "PUT":
            return request.user.is_superuser
        if request.method == "DELETE":
            return request.user.is_superuser
        return True


class ProtectAllMethods(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_superuser
        if request.method == "POST":
            return request.user.is_superuser
        if request.method == "PUT":
            return request.user.is_superuser
        if request.method == "DELETE":
            return request.user.is_superuser
        return True
