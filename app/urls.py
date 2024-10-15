from django.urls import path, include

urlpatterns = [
    path("users/", include("users.urls")),
    path("courses/", include("app.course.urls")),
    path("payment/", include("apps.payment.urls"))
]
