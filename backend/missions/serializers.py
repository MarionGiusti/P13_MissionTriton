from rest_framework import serializers

from .models import Mission, TimeLine, ShipPosition
from users.serializers import MissionUserSerializer

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = (
            "id",
            "name", 
            "ship_name", 
            "start_date", 
            "end_date",
            "description"
            )
 
class TimeLineSerializer(serializers.ModelSerializer):
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
            "color"
        )

class ShipPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipPosition
        fields = (
            "id",
            "mission",
            "latitude",
            "longitude",
            "date_time",
        )
