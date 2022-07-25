from rest_framework import permissions
from .models import Note


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin/staff to edit book objects.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
        # does this work???


class IsPublic(permissions.BasePermission):
    pass
    # def has_permission(self, request, view):
    #     if 
    #         return True
    #     else:
    #         return request.user.is_staff
