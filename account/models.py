from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="رقم الهاتف")
    is_doctor = models.BooleanField(default=False, verbose_name="هل هو طبيب؟")
    is_patient = models.BooleanField(default=True, verbose_name="هل هو مريض؟")

    def __str__(self):
        return self.username