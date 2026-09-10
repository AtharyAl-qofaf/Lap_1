from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from .emails import send_welcome_email

@receiver(post_save, sender='account.CustomUser')
def create_welcome_notification_and_email(sender, instance, created, **kwargs):
    if created:
        Notification = apps.get_model('account', 'Notification')
        Notification.objects.create(
            user=instance,
            message=f"أهلاً بك {instance.username}! تم إنشاء حسابك بنجاح."
        )
        if instance.email:
            send_welcome_email(instance.email, instance.username)