"""
Define signal between Mission and MissionUser
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Mission
from apps.users.models import MissionUser
from django.contrib.auth import get_user_model


@receiver(post_save, sender=Mission)
def create_missionuser(sender, instance=None, created=False, **kwargs):
    if created:
        MissionUser.objects.create(user=get_user_model(), mission=instance)
