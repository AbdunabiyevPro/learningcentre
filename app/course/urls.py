from django.urls import path

from app.course.api_endpoints.coursDetail.views import CourseDetailAPIView
from app.course.api_endpoints.coursecomment.views import CourseListAPIView
from app.course.api_endpoints.lesson.views import LessonDetailAPIView

urlpatterns = [
    path("course-detail/", CourseDetailAPIView.as_view(), name="course-detail"),
    path("lesson/<int:pk>/detail/", LessonDetailAPIView.as_view(), name="lesson-detail"),
    path("course-comment/", CourseListAPIView.as_view(), name="course-list")
]
