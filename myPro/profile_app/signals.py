# profile_app/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from connect_app.models import UserMd
from .models import Profile

@receiver(post_save, sender=UserMd)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, full_name=instance.full_name)
