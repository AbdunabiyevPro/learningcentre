from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path




urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include("app.users.urls")),
    path('api/v1/', include("app.course.urls"))
]
