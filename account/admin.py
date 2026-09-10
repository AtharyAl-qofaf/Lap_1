from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_doctor', 'is_patient', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('معلومات إضافية', {'fields': ('is_doctor', 'is_patient', 'phone')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'image')
    search_fields = ('user__username', 'phone')

from django.apps import apps

Notification = apps.get_model('account', 'Notification')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user',)