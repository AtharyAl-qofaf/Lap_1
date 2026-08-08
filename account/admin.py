from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_doctor', 'is_patient', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('معلومات إضافية', {'fields': ('is_doctor', 'is_patient', 'phone')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)