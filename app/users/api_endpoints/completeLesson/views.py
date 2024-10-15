from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import CompleteLessonSerializer
from rest_framework.permissions import IsAuthenticated
from app.course.models import Lesson
from rest_framework.exceptions import ValidationError
from app.users.models import Subscription

class CompleteLessonAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CompleteLessonSerializer(data=self.request.data)
        serializer.is_valid()
        data = serializer.data
        lesson_id = data.get("lesson_id")

        try:
            lesson = Lesson.objects.get(id=lesson_id)
        except Lesson.DoesNotExists:
            raise ValidationError(
                {
                    "detail": "Lesson not found", "code": "lesson_not_found"
                }
            )
        has_access = Subscription.objects.filter(course=lesson.module.course, user=self.request.user, is_active=True).exists()

        if not has_access:
            raise ValidationError(
                {
                    "detail": "User hasn't got access to this course", "code": "access_denied"
                }
            )

        return Response({
            "detail": "Successfully completed lesson", "code": "completed_lesson"
        }, status=201
        )








