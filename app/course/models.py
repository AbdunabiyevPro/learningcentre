from django.db import models
from django.contrib.auth import get_user_model


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kurs nomi")
    description = models.TextField(verbose_name="Izoh")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Narxi")
    is_started = models.BooleanField("Kurs boshlanganmi ? ", default=False)
    cover = models.ImageField(upload_to="covers/")


    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField("Modul nomi", max_length=255)
    description = models.TextField(verbose_name="Izoh")
    duration = models.DateField("Davomiyligi")
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Modul"
        verbose_name_plural = "Modullar"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    class LessonTypes(models.TextChoices):
        VIDEO = "video", "Video"
        AUDIO = "audio", "Audio"
        DOCUMENT = "document", "Document"

    title = models.CharField(max_length=255, verbose_name="Dars nomi")
    file = models.FileField(upload_to="media", null=True, blank=True)
    _type = models.CharField(
        max_length=255,
        verbose_name="Dars turi",
        choices=LessonTypes.choices,
        default=LessonTypes.DOCUMENT
    )
    body = models.TextField(null=True, blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lesson")

    class Meta:
        verbose_name = "Dars",
        verbose_name_plural = "Darslar"

    def __str__(self):
        return self.title


class CourseReview(models.Model):
    class Ratings(models.TextChoices):
        R1 = "1", "1"
        R2 = "2", "2"
        R3 = "3", "3"
        R4 = "4", "4"
        R5 = "5", "5"

    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.CharField(choices=Ratings.choices, default=Ratings.R5, max_length=6)
    comment = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Kurs izohi"
        verbose_name_plural = "Kurs izohlari"


    def __str__(self):
        return self.comment




