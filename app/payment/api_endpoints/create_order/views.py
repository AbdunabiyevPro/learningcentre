from rest_framework.generics import CreateAPIView
from app.payment.models import Order
from .serializers import OrderCreateSerializer
from rest_framework.permissions import IsAuthenticated

class CreateOrderAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated, ]