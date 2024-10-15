from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.payment.models import Order



class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("course", )

    def create(self, validated_data):
        context = self.context
        user = context.get('request').user

        if Order.objects.filter(course_id=validated_data['course'], user=user).exists():
            raise ValidationError({
                "detail": "user is already sent request for this course",
                "success": False
            })

        validated_data['user_id'] = user.pk
        return super().create(validated_data)