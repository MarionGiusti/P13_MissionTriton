from rest_framework import permissions
from apps.users.models import MissionUser
from apps.missions.models import Mission

class IsUserOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow self user to edit their objects.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

class IsMissionUserOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners
    of missionuser profile to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class IsMissionOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow member of the same mission
    to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            missionuser = MissionUser.objects.get(
            	mission=obj.id, user=request.user.id)
            return obj == missionuser.mission
        except MissionUser.DoesNotExist:
            return None

class IsMissionMemberOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow members of the same mission
    to edit object related to this mission.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            missionuser = MissionUser.objects.get(
            	mission=obj.mission, user=request.user.id)
            return obj.mission == missionuser.mission
        except MissionUser.DoesNotExist:
            return None

class IsScheduleOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners or share owners
    of schedule event to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return False
        try:
            if obj.mission is None:
                return obj.user == request.user
            else:
                missionuser = MissionUser.objects.get(
                	mission=obj.mission, user=request.user.id)
                return obj.mission == missionuser.mission
        except MissionUser.DoesNotExist:
            return None
