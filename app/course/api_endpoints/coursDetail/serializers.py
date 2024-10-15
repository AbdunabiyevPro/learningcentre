from django.db.models import Avg
from rest_framework import serializers
from app.course.models import Course, Module, Lesson, CourseReview
from django.contrib.auth.models import AnonymousUser

from app.users.models import IsUserCompleteLesson


class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = ["rating", "comment", "is_confirmed"]


class LessonSerializer(serializers.ModelSerializer):
    is_completed = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ("id", "title", "is_completed")

    def get_is_completed(self, obj):
        user = self.context.get("user")
        if user.__class__ != AnonymousUser:
            return IsUserCompleteLesson.objects.filter(lesson=obj.module.course, user=user).exists()
        return None


class ModulSerializer(serializers.ModelSerializer):
    lesson = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ["title", "description", "duration", "course", "lesson"]

    def get_lesson(self, obj):
        return LessonSerializer(obj.lesson.all(), many=True, context=self.context).data


class CourseDetailSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    modules = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["id", "title", "description", "price", "rating", "modules"]

    def get_rating(self, obj):
        reviews = obj.reviews.filter(is_confirmed=True)
        if reviews.exists():
            return reviews.aggregate(Avg('rating'))['rating__avg']
        return None

    def get_modules(self, obj):
        user = self.context.get("request").user
        context = {"user": user}
        return ModulSerializer(obj.modules.all(), many=True, context=context).data
