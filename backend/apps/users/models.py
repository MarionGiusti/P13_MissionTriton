"""
Define models CustomUser and MissionUser
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.missions.models import Mission

class CustomUser(AbstractUser):
    """ Class CustomUser to custom user model """
    profile_image = models.ImageField(upload_to="profile_pics", default="profile.png", null=True)
    profile_background_image = models.ImageField(
        upload_to="profile_background_pics", default="jakob-owens-turtle-unsplash.jpg", null=True)
    linkedin_link = models.URLField(null=True, blank=True)
    researchgate_link = models.URLField(null=True, blank=True)
    missions = models.ManyToManyField(Mission, through='MissionUser')

class MissionUser(models.Model):
    """ Class MissionUser for each user member of a mission """
    user = models.ForeignKey(
        get_user_model(), null=False, on_delete=models.CASCADE, related_name="missionusers")
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="missionusers")
    job = models.CharField(max_length=150, default="", blank=True)
    team_lab = models.CharField(max_length=200, default="", blank=True)
    description = models.TextField(default="", blank=True)

    class Meta:
        unique_together = ['user', 'mission']
        ordering = ['mission']

    def __str__(self):
        """Method to change the object name in QuerySet """
        return f'{self.user.username} {self.mission.name}'
