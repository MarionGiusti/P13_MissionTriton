from django.db import models

from apps.users.models import MissionUser
from apps.missions.models import Mission

class Schedule(models.Model):
    mission_user = models.ForeignKey(MissionUser, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, null=False)
    details = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    