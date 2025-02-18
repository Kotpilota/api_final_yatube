from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Allows read access to all but restricts modifications to the author."""

    def has_object_permission(self, request, view, obj):
        """Check if the request should be permitted.

        Args:
            request (Request): The incoming HTTP request.
            view (View): The view being accessed.
            obj (Model): The object being accessed.

        Returns:
            bool: True if the method is safe or the user is the author.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
