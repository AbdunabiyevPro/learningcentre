from rest_framework import serializers
from app.users.models import User


class UserLoginRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number",)
