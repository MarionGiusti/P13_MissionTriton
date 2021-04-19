# from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser 
from django.db import models

from apps.missions.models import Mission

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to="profile_pics", default="profile.png", null=True)
    profile_background_image = models.ImageField(upload_to="profile_background_pics", default="jakob-owens-turtle-unsplash.jpg", null=True)
    linkedin_link = models.URLField(null=True, blank=True)
    researchgate_link = models.URLField(null=True, blank=True)
    missions = models.ManyToManyField(Mission, through='MissionUser')


class MissionUser(models.Model):
    user = models.ForeignKey(get_user_model(), null=False, on_delete=models.PROTECT, related_name="missionusers")
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="missionusers")
    job = models.CharField(max_length=150, null=True, blank=True)
    team_lab = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ['user', 'mission']
        ordering = ['mission']

    def __str__(self):
        return f'{self.user.username} {self.mission.name}'

# class UserProfile(models.Model):
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
#     profile_pic = models.ImageField(upload_to="profile_pics", default="profile.png", null=True)
#     linkedin_profile = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}'

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.update_or_create(user=instance)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)