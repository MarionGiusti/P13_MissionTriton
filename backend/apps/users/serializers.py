from rest_framework import serializers

from .models import CustomUser, MissionUser

class UserSerializer(serializers.ModelSerializer):
    # missionusers = serializers.StringRelatedField(many=True)

    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_image",
            "profile_background_image",
            "linkedin_link",
            "researchgate_link",
            "missions",
            # "missionusers"
        )
        extra_kwargs = {"password":{"write_only":True,"required":True}}
        # depth show details of missions
        depth = 1

class MissionUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MissionUser
        fields = (
            "id",
            "user",
            "mission",
            "job",
            "team_lab",
            "description"
        )
        # depth show details of user and mission foreign key
        # depth = 1
