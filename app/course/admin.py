from django.contrib import admin
from app.course import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "get_custom_price", "is_started")
    search_fields = ("title",)
    list_filter = ("is_started",)

    def get_custom_price(self, obj):
        if obj:
            return f"$ {obj.price}"
        return None

    get_custom_price.short_description = "Price"


@admin.register(models.Module)
class ModulAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "course")
    search_fields = ("title",)
    list_filter = ("course",)
    autocomplete_fields = ("course",)


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "_type", "module")
    search_fields = ("title",)
    list_filter = ("module", "module__course")
    autocomplete_fields = ("module",)



@admin.register(models.CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ("comment", "rating")
