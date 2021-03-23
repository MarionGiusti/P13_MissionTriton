from rest_framework import serializers

from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        	"id",
        	"username", 
        	"first_name", 
        	"last_name", 
        	"email",
        	"password",
            
        	)
        extra_kwargs = {"password":{"write_only":True,"required":True}}

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "user",
            "profile_pic",
            "linkedin_profile"
        )