from django.contrib import admin
from .models import DoctorProfile


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "specialty",
        "rating",
        "experience_years",
        "available",
    )
    list_filter = (
        "available",
        "specialty",
    )
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "specialty",
    )
    filter_horizontal = ("services",)