from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Moderators').exists()


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user