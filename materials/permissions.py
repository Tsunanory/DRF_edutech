from rest_framework.permissions import BasePermission


class IsOwnerOrModerator(BasePermission):
    def has_object_permission(self, request, view, obj):
        is_moderator = request.user and request.user.groups.filter(name='Moderators').exists()
        is_owner = obj.owner == request.user
        return is_moderator or is_owner


class NotModerator(BasePermission):
    def has_permission(self, request, view):
        return not (request.user and request.user.groups.filter(name='Moderators').exists())


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

