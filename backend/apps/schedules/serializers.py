from rest_framework import serializers

from .models import Schedule
from apps.users.serializers import MissionUserSerializer
from apps.missions.serializers import MissionSerializer

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = (
            "id",
            "user",
            "mission",
            "name",
            "details",
            "start",
            "end",
            "color",
        )
