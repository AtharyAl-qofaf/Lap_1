from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'doctor_name', 'available_time', 'created_at']

admin.site.register(Service, ServiceAdmin)