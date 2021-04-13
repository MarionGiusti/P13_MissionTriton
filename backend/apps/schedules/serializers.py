from rest_framework import serializers

from .models import Schedule
from apps.users.serializers import MissionUserSerializer
from apps.missions.serializers import MissionSerializer

class ScheduleSerializer(serializers.ModelSerializer):
    mission = MissionSerializer(many=False, read_only=True)
    user = MissionUserSerializer(many=False, read_only=True)

    class Meta:
        model = Schedule
        fields = (
            "id",
            "user",
            "mission",
            "title",
            "details",
            "start_date",
            "end_date",
            "color",
        )
