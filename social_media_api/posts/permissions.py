from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Allows access only to the owner for unsafe methods (PUT/PATCH/DELETE).
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS (always allowed)
        if request.method in SAFE_METHODS:
            return True

        # Only allow modification if user is the author
        return obj.author == request.user
