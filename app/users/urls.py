from app.users.api_endpoints.loginRequest import LoginRequestAPIView
from app.users.api_endpoints.loginVerify import LoginVerifyAPIView
from app.users.api_endpoints.registerentry import RegisterEntryAPIView
from app.users.api_endpoints.registerverify import RegisterVerifyAPIView
from app.users.api_endpoints.completeLesson import CompleteLessonAPIView
from django.urls import path

urlpatterns = [
    # login
    path("login-request/", LoginRequestAPIView.as_view(), name='login-request'),
    path("login-verify/", LoginVerifyAPIView.as_view(), name="login-verify"),

    # register
    path("register-entry/", RegisterEntryAPIView.as_view(), name="register-entry"),
    path("register-verify/", RegisterVerifyAPIView.as_view(), name="register-verify"),

    path("complete-lesson/", CompleteLessonAPIView.as_view(), name='complete-lesson')

]
