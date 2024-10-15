from app.course.models import Course
from rest_framework.generics import RetrieveAPIView
from .serializers import LessonSerializer
from app.course.models import Lesson
from rest_framework.permissions import IsAuthenticated
from app.course.permissions import IsSubscribed


class LessonDetailAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsSubscribed]
