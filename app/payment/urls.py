from app.payment.api_endpoints.create_order.views import CreateOrderAPIView
from django.urls import path


urlpatterns = [
    path("create-order/", CreateOrderAPIView.as_view(), name="create-order"),
]