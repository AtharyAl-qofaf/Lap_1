from django.conf import settings
from django.db import models


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile",
        verbose_name="حساب الطبيب",
    )
    specialty = models.CharField(
        max_length=150,
        verbose_name="التخصص الطبي",
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0,
        verbose_name="التقييم",
    )
    reviews_count = models.PositiveIntegerField(
        default=0,
        verbose_name="عدد التقييمات",
    )
    experience_years = models.PositiveIntegerField(
        default=0,
        verbose_name="سنوات الخبرة",
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="العمر",
    )
    degree = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="المؤهل العلمي",
    )
    schedule = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="مواعيد الدوام",
    )
    location = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="موقع العيادة",
    )
    available = models.BooleanField(
        default=True,
        verbose_name="متاح للحجز",
    )
    services = models.ManyToManyField(
        "services.Service",
        blank=True,
        related_name="doctors",
        verbose_name="الخدمات التي يقدمها الطبيب",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة",
    )

    @property
    def name(self):
        full_name = self.user.get_full_name().strip()
        return full_name or self.user.username

    def __str__(self):
        return self.name