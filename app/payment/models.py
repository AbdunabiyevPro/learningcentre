from django.db import models
from django.contrib.auth import get_user_model
from app.course.models import Course
from app.users.models import Subscription


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        CANCELED = "canceled", "Canceled"

    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name="orders")
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="orders")
    status = models.CharField(choices=OrderStatus.choices, max_length=16, default=OrderStatus.PENDING)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Buyurtma# {self.pk}"

    def handle_subscription(self):
        is_active = self.status == Order.OrderStatus.APPROVED

        Subscription.objects.update_or_create(
            user=self.user,
            course=self.course,
            defaults={
                "is_active": is_active
            }
        )

    def save(self, *args, **kwargs):
        if self.pk:
            self.handle_subscription()
        return super().save(*args, **kwargs)
