from rest_framework import permissions


class IsAdminOrAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
