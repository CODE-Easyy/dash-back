from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = 'Your access level must be minimum \'Администратор\'.'
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)


class IsSuperAdmin(BasePermission):
    message = 'Your access level must be \'Супер Администратор\'.'
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_super_admin)

class SelfOrSuperAdmin(BasePermission):
    message = 'It is not your account or your access level less than \'Супер Администратор\'.'
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user == obj)