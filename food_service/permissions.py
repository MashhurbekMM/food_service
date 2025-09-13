from rest_framework.permissions import BasePermission


class isOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        owner = obj.owner
        if owner == request.user:
            return True
        
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    

class CustomIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
