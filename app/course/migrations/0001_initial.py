# Generated by Django 4.2.16 on 2024-09-30 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Kurs nomi")),
                ("description", models.TextField(verbose_name="Izoh")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Narxi"
                    ),
                ),
                (
                    "is_started",
                    models.BooleanField(
                        default=False, verbose_name="Kurs boshlanganmi ? "
                    ),
                ),
                ("cover", models.ImageField(upload_to="covers/")),
            ],
            options={
                "verbose_name": "Kurs",
                "verbose_name_plural": "Kurslar",
            },
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Modul nomi")),
                ("description", models.TextField(verbose_name="Izoh")),
                ("duration", models.DateField(verbose_name="Davomiyligi")),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
            ],
            options={
                "verbose_name": "Modul",
                "verbose_name_plural": "Modullar",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Dars nomi")),
                ("file", models.FileField(blank=True, null=True, upload_to="media")),
                (
                    "_type",
                    models.CharField(
                        choices=[
                            ("video", "Video"),
                            ("audio", "Audio"),
                            ("document", "Document"),
                        ],
                        default="document",
                        max_length=255,
                        verbose_name="Dars turi",
                    ),
                ),
                ("body", models.TextField(blank=True, null=True)),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lesson",
                        to="course.module",
                    ),
                ),
            ],
            options={
                "verbose_name": ("Dars",),
                "verbose_name_plural": "Darslar",
            },
        ),
        migrations.CreateModel(
            name="CurseReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                        ],
                        default="5",
                        max_length=6,
                    ),
                ),
                ("comment", models.TextField()),
                ("is_confirmed", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Kurs izohi",
                "verbose_name_plural": "Kurs izohlari",
            },
        ),
    ]
