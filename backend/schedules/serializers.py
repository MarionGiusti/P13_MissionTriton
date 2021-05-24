from rest_framework import serializers

from .models import Schedule
from users.serializers import MissionUserSerializer
from missions.serializers import MissionSerializer

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
