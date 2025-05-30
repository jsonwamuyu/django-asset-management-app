from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermissions):
    """
    Custom permission to only allow admins to edit objects.
    All users can read.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'admin':
            return True
        return request.method in permissions.SAFE_METHODS
    
class IsAdminOrAssignedOnly(permissions.BasePermissions):
    """
    Custom permission to allow admins full access and staff to view only their assigned assets.
    """

    def has_asset_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        return obj.assigned_to == request.user