from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer
from app.users.models import User
from django.core.cache import cache
from django.core.validators import ValidationError
from app.users.utils import generate_random_6digits


class RegisterEntryAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            phone_number = serializer.data.get("phone_number")
            full_name = serializer.data.get("full_name")

            if User.objects.filter(phone_number=phone_number, is_verified=True).exists():
                raise ValidationError({"success": False, "errors": "Phone_number is already taken"})
            code = generate_random_6digits()
            cache.set(f"otp_register_{phone_number}", code, 60)
            cache_key = f"otp_register{phone_number}"

            if cache.get(cache_key) is not None:
                return Response({"success": False, "message": "We have already sent sms, try again in 60s"})

            User.objects.update_create(
                phone_number=phone_number,
                defaults={
                    "full_name":full_name
                }
            )

            cache.set(cache_key, code, 60)
            return Response({"success": True, "message": "We have sent sms to verify your number"})
        return Response({"success": False, "errors": serializer.errors})
