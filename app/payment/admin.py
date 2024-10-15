from django.contrib import admin
from app.payment.models import Order
from app.payment.models import Subscription

admin.site.register(Order)
admin.site.register(Subscription)