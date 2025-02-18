from rest_framework.pagination import LimitOffsetPagination


class DynamicLimitOffsetPagination(LimitOffsetPagination):
    """Custom pagination that enable limit-offset only when parameters exist"""

    def paginate_queryset(self, queryset, request, view=None):
        """Paginate the queryset only if `limit` or `offset` are provided.

        Args:
            queryset (QuerySet): The original queryset.
            request (Request): The incoming HTTP request.
            view (View, optional): The associated view. Defaults to None.

        Returns:
            list | None: The paginated queryset or None if no pagination.
        """
        if not (request.query_params.get('limit')
                or request.query_params.get('offset')):
            return None
        return super().paginate_queryset(queryset, request, view)
