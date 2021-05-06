from django.contrib.auth import get_user_model
from django.db import models

# from apps.users.models import MissionUser
from apps.users.models import CustomUser
from apps.missions.models import Mission

class Schedule(models.Model):
    # mission_user = models.ForeignKey(MissionUser, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="scheduleuser")

    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True, null=False)
    details = models.TextField(default="", blank=True)
    start = models.DateField(null=False)
    end = models.DateField(null=False)
    color = models.CharField(max_length=7, default="#D33A3A", null=True)
    
    def __str__(self):
    	return f'{self.user} {self.name}'
        # return f'{self.mission_user} {self.name}'