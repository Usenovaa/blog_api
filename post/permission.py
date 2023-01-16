from rest_framework.permissions import\
    BasePermission


class IsAdminAuthPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
                request.user.is_active
             or request.user.is_staff)
