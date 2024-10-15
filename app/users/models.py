from django.db import models
from django.contrib.auth.models import AbstractUser

from app.course.models import Course, Lesson
from app.users.validators import PhoneNumberValidator
from app.users.managers import CustomUserManager


class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = "admin", "Admin"
        STUDENT = "student", "Student"
        GUEST = "guest", "Guest"

    first_name = None
    last_name = None
    user_name = None

    full_name = models.CharField("Full name", max_length=255)
    role = models.CharField(max_length=16, choices=UserType.choices)
    avatar = models.ImageField(null=True, blank=True)

    phone_number_validator = PhoneNumberValidator()

    phone_number = models.CharField(
        "PhoneNumber",
        validators=[phone_number_validator],
        max_length=255,
        unique=True)

    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="subscriptions")
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("course", "user")


class IsUserCompleteLesson(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
