from rest_framework import serializers

from .models import Post, Picture
from users.serializers import MissionUserSerializer
from missions.serializers import MissionSerializer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "mission_user",
            "mission",
            "title",
            "content",
            "created_at",
            "updated_at",
            "post_image",
            "video_url",
            "category",
        )

class PictureSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField()
    class Meta:
        model = Picture
        fields = (
            "id",
            "mission",
            "picture",
            "created_at",
        )
