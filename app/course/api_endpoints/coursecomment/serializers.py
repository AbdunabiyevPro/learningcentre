from rest_framework import serializers
from app.course.models import CourseReview



class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = ('course', 'comment', 'rating')

    def create(self, validated_data):
        context = self.context
        validated_data['user_id'] = context.get("request").user.id
        return super().create(validated_data)
