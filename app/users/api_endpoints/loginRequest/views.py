from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserLoginRequestSerializer
from app.users.models import User
from django.core.cache import cache
from app.users.utils import generate_random_6digits





class LoginRequestAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginRequestSerializer(data=request.data)

        if serializer.is_valid():
            phone_number = serializer.data.get("phone_number")
            cache_key = f"otp_{phone_number}"
            if cache.get(cache_key):
                return Response(
                    {"success": False, "errors": "we have already sent sms. Try again in 60s"}
                )
            phone_number = serializer.data.get("phone_number")
            if not User.objects.filter(phone_number=phone_number, is_verified=True).exists():
                return Response(
                    {"success": False, "errors": "Can't find user with this credanitsals"}
                )
            code = generate_random_6digits()
            cache_key = f"otp_{phone_number}"
            print(code, cache_key)
            cache.set(cache_key, code, 60)
            return Response({"success": True, "message": "We have sent sms to verify your number"})
        return Response({"success": False, "errors": serializer.errors})
