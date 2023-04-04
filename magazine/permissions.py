from rest_framework.permissions import BasePermission


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in ('GET', 'HEAD', 'OPTIONS') or request.user and request.user.is_staff)

class IsClientOrAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and
                    request.method in ('GET', 'HEAD', 'OPTIONS')
                    or request.user and request.user.is_staff )

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user and request.user.is_staff