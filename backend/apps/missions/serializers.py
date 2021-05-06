from rest_framework import serializers

from .models import Mission, TimeLine, ShipPosition
from apps.users.serializers import MissionUserSerializer

# class MissionSerializer(serializers.ModelSerializer):
#     # missionusers = MissionUserSerializer(many=True)
#     missionusers = MissionUserSerializer(many=True, read_only=True)
#     # missionusers = serializers.StringRelatedField(many=True, read_only=True)

#     # missionusers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     # ship_positions = serializers.SlugRelatedField(
#     #     many=True,
#     #     read_only=True,
#     #     slug_field="full_position")

#     class Meta:
#         model = Mission
#         fields = (
#             "id",
#             "name", 
#             "ship_name", 
#             "start_date", 
#             "end_date",
#             "missionusers",
#             # "ship_positions",
#             )

#         depth = 1 

class MissionSerializer(serializers.ModelSerializer):
    # missionusers = MissionUserSerializer(many=True)
    # missionusers = MissionUserSerializer(many=True, read_only=True)
    # missionusers = serializers.StringRelatedField(many=True, read_only=True)

    # missionusers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # ship_positions = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field="full_position")

    class Meta:
        model = Mission
        fields = (
            "id",
            "name", 
            "ship_name", 
            "start_date", 
            "end_date",
            "description"
            # "missionusers",
            # "ship_positions",
            )

        # depth = 1 
        
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
            "color"
        )

class ShipPositionSerializer(serializers.ModelSerializer):
    # mission = MissionSerializer(many=False, read_only=True)
    # mission_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = ShipPosition
        fields = (
            "id",
            "mission",
            "latitude",
            "longitude",
            "date_time",
        )
