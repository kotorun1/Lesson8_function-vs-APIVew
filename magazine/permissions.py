from rest_framework.permissions import BasePermission


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in ('GET', 'HEAD', 'OPTIONS') or request.user and request.user.is_staff)

class IsClientReadOnlyOrAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and
                    request.method in ('GET', 'HEAD', 'OPTIONS')
                    or request.user and request.user.is_staff )
