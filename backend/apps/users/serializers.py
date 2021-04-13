from rest_framework import serializers

from .models import CustomUser, MissionUser

class UserSerializer(serializers.ModelSerializer):
    # missionusers = MissionUserSerializer(many=True, read_only=True)
    missionusers = serializers.StringRelatedField(many=True)

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
            "linkedin_link",
            "researchgate_link",
            "missionusers"
        )
        extra_kwargs = {"password":{"write_only":True,"required":True}}

class MissionUserSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(many=False, read_only=True)
    # mission_id = MissionSerializer(many=False, read_only=True)
    # user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # mission_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

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

# class DataSerializer(serializers.ModelSerializer):
#     size = serializers.SerializerMethodField()
#     name = serializers.SerializerMethodField()
#     filetype = serializers.SerializerMethodField()
#     since_added = serializers.SerializerMethodField()
#         class Meta:
#             model = Data
#             fields = ('file_id', 'file', 'since_added', 'size', 'name', 'filetype')
            
#             def get_size(self, obj):
#                 file_size = ''
#                 if obj.file and hasattr(obj.file, 'size'):
#                     file_size = obj.file.size
#                 return file_size
            
#             def get_name(self, obj):
#                 file_name = ''
#                 if obj.file and hasattr(obj.file, 'name'):
#                     file_name = obj.file.name
#                 return file_name
            
#             def get_filetype(self, obj):
#               filename = obj.file.name
#               return filename.split('.')[-1]
          
#           def get_since_added(self, obj):
#                 date_added = obj.date_created
#                 return date_added