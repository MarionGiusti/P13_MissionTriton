from rest_framework import serializers

from .models import CustomUser, MissionUser

class UserSerializer(serializers.ModelSerializer):
    # profile_image_url = serializers.SerializerMethodField()
    # def get_profile_image_url(self, obj):
    #     request = self.context.get('request')
    #     profile_image_url = obj.profile_image.url
    #     return request.build_absolute_uri(profile_image_url)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            # "profile_image_url",
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
