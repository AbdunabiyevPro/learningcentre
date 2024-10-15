from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterVerifySerializer
from app.users.models import User
from django.core.cache import cache
from django.core.validators import ValidationError
from app.users.utils import generate_random_6digits, get_tokens_for_user


class RegisterVerifyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterVerifySerializer(data=request.data)

        if serializer.is_valid():
            phone_number = serializer.data.get("phone_number")
            code = serializer.data.get("code")

            if User.objects.filter(phone_number=phone_number, is_verified=True).exists():
                raise ValidationError({"success": False, "errors": "Phone_number is already taken"})

            if not User.objects.filter(phone_number=phone_number, is_verified=False).exists():
                raise ValidationError({"success": False, "errors": "Can't find not verified number"})

            cache.set(f"otp_register_{phone_number}", code, 60)
            cache_key = f"otp_register{phone_number}"
            cached_key = cache.get(cache_key)

            if cached_key is  None:
                return Response({"success": False, "message": "Your OTP is expired please try again"}, status=400)


            if cached_key != code:
                return Response({"success": False, "message": "wrong OTP"}, status=400)

            user = User.objects.get(phone_number=phone_number, is_verified=False)
            user.is_verified = True
            user.save()
            tokens = get_tokens_for_user(user)

            return Response(tokens)
        return Response({"success": False, "errors": serializer.errors})
