from rest_framework.permissions import BasePermission
from app.users.models import Subscription

class IsSubscribed(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        course_id = request.parser_context.get('kwargs', {}).get("pk")
        return Subscription.objects.filter(
            user=user,
            course_id=course_id,
            is_active=True
        ).exists()
