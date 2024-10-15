from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from app.course.api_endpoints.coursecomment.serializers import CourseReviewSerializer
from app.course.models import CourseReview

class CourseListAPIView(CreateAPIView):
    serializer_class = CourseReviewSerializer
    queryset = CourseReview.objects.all()

    def post(self, request, *args, **kwargs):
        data = CourseReviewSerializer(request.data)
        return Response({"message": "Course comment added successfully."})
