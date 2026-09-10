from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_yemeni_phone, validate_image_size

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="رقم الهاتف")
    is_doctor = models.BooleanField(default=False, verbose_name="هل هو طبيب؟")
    is_patient = models.BooleanField(default=True, verbose_name="هل هو مريض؟")

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, validators=[validate_yemeni_phone], blank=True, null=True)
    image = models.ImageField(upload_to='profiles/', validators=[validate_image_size], blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    class Notification(models.Model):
         user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"