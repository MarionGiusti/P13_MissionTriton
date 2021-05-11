from rest_framework import serializers

from .models import CustomUser, MissionUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
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
        )
        extra_kwargs = {"password":{"write_only":True,"required":True}}
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
