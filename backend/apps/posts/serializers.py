from rest_framework import serializers

from .models import Post, Picture
from apps.users.serializers import MissionUserSerializer
from apps.missions.serializers import MissionSerializer

class PostSerializer(serializers.ModelSerializer):
    mission = MissionSerializer(many=False, read_only=True)
    user = MissionUserSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "mission",
            "title",
            "content",
            "date",
            "created_at",
            "updated_at",
            "post_image",
            "video_url",
            "category",
        )


class PictureSerializer(serializers.ModelSerializer):
    mission = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Picture
        fields = (
            "id",
            "mission",
            "picture",
            "title",
            "created_at",
        )
