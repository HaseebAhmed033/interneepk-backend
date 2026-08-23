from rest_framework import permissions

class IsAdminOrStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Reading (GET) is allowed for any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        # Writing (POST/PUT/DELETE) only allowed for admin/staff
        return request.user.is_authenticated and request.user.role in ['admin', 'staff']