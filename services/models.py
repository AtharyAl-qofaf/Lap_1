from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الخدمة")
    description = models.TextField(verbose_name="وصف الخدمة")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    doctor_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="الطبيب المختص")
    available_time = models.CharField(max_length=100, blank=True, null=True, verbose_name="أوقات العمل")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    def __str__(self):
        return self.name