from rest_framework import serializers

class CompleteLessonSerializer(serializers.Serializer):
    lesson_id = serializers.IntegerField()
