from rest_framework import permissions

class isOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object editing permission.
    """
    def has_object_permission(self, request, view, obj):
        """
        We'll always allow GET, HEAD or OPTIONS.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user.profile