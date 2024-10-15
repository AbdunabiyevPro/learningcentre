from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.course.api_endpoints.coursDetail.serializers import CourseDetailSerializer, ModulSerializer, LessonSerializer
from app.course.models import Course, Module, Lesson, CourseReview


class CourseDetailAPIView(generics.ListAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
