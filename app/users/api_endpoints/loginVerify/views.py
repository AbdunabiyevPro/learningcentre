from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserLoginVerifySerializer
from app.users.models import User
from django.core.cache import cache
from app.users.utils import get_tokens_for_user


class LoginVerifyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginVerifySerializer(data=request.data)

        if serializer.is_valid():
            phone_number = serializer.data.get("phone_number")
            code = serializer.data.get("code")
            cache_key = f"otp_{phone_number}"
            cache_code = cache.get(cache_key)
            if cache_code is None:
                return Response({
                    "success": False, "errors": "Your OTP is expired"
                })
            if code != cache_code:
                return Response({
                    "success": False, "errors": "You have entered wrong OTP"
                })
            user = User.objects.get(phone_number=phone_number)
            token = get_tokens_for_user(user)

            return Response({"success": True, "message": "We have sent sms to verify your number"})
        return Response({"success": False, "errors": serializer.errors})
