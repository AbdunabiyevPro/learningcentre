from rest_framework import serializers


class UserLoginVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.IntegerField()
