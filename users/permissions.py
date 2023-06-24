from rest_framework.permissions import BasePermission


class IsOwnBook(BasePermission):
    """
    Allows users if they are Author for this book
    """

    def has_object_permission(self, request, view, obj):
        if obj.author.id == request.user.id:
            return True
        return False

