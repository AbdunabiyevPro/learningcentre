from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterVerifySerializer(serializers.ModelSerializer):
    code = serializers.CharField()
    full_name = serializers.CharField()
