from rest_framework import serializers

from .models import Mission, TimeLine, ShipPosition
from apps.users.serializers import MissionUserSerializer

class MissionSerializer(serializers.ModelSerializer):
    missionusers = MissionUserSerializer(many=True, read_only=True)
    # missionusers = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Mission
        fields = (
            "id",
            "name", 
            "ship_name", 
            "start_date", 
            "end_date",
            "missionusers"
            )

class TimeLineSerializer(serializers.ModelSerializer):
    # mission = MissionSerializer(many=False, read_only=True)
    mission_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    class Meta:
        model = TimeLine
        fields = (
            "id",
            "mission_id",
            "name",
            "description",
            "start_date",
            "end_date",
        )

class ShipPositionSerializer(serializers.ModelSerializer):
    mission = MissionSerializer(many=False, read_only=True)

    class Meta:
        model = ShipPosition
        fields = (
            "id",
            "mission",
            "latitude",
            "longitude",
        )
