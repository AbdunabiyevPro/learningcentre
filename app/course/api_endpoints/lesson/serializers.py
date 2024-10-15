from django.db.models import Avg
from rest_framework import serializers
from app.course.models import Course, Module, Lesson, CourseReview



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("title", "file", "_type", "body", )

