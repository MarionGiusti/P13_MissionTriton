from rest_framework import viewsets
from rest_framework.response import Response

from users.permissions import (
    IsMissionOwnerOrReadOnly,
    IsMissionMemberOrReadOnly)
from users.models import MissionUser
from .serializers import (
    MissionSerializer,
    TimeLineSerializer,
    ShipPositionSerializer)
from .models import Mission, TimeLine, ShipPosition

class MissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows missions to be viewed or edited.
    """
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = (IsMissionOwnerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        data = request.data
        new_mission = Mission.objects.create(
            name=data["name"], ship_name=data["ship_name"],
            description=None, start_date=data["start_date"],
            end_date=data["end_date"])
        new_missionuser = MissionUser.objects.create(
            mission=new_mission, user=request.user)
        new_mission.save()
        new_missionuser.save()
        serializer = MissionSerializer(new_mission)
        return Response(serializer.data)

class TimeLineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows timelines to be viewed or edited.
    """
    queryset = TimeLine.objects.all()
    serializer_class = TimeLineSerializer
    permission_classes = (IsMissionMemberOrReadOnly,)

    def create(self, request, *args, **kwargs):
        data = request.data
        mission = Mission.objects.get(id = data["missionId"])
        if data["form"]["end_date"]:
            end_date = data["form"]["end_date"]
        else:
            end_date = None

        if data["form"]["description"]:
            description = data["form"]["description"]
        else:
            description = ""

        new_timeline = TimeLine.objects.create(
            mission=mission, name=data["form"]["name"],
            description=description, start_date=data["form"]["start_date"],
            end_date=end_date, color=data["form"]["color"])
        self.check_object_permissions(request, new_timeline)
        new_timeline.save()
        serializer = TimeLineSerializer(new_timeline)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset= self.get_queryset().order_by('-start_date')
        mission_id = request.GET.get('missionid')
        if mission_id:
            queryset = queryset.filter(
                mission_id = mission_id).order_by('-start_date')
        serializer = TimeLineSerializer(queryset, many=True)
        return Response(serializer.data)

class ShipPositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shippositions to be viewed or edited.
    """
    queryset = ShipPosition.objects.all()
    serializer_class = ShipPositionSerializer
    permission_classes = (IsMissionMemberOrReadOnly,)

    def create(self, request, *args, **kwargs):
        data = request.data
        mission = Mission.objects.get(id = data["mission"])
        new_shippos = ShipPosition(
            mission=mission, latitude=data["form"]["latitude"],
            longitude=data["form"]["longitude"],
            date_time=data["form"]["date_time"])
        self.check_object_permissions(request, new_shippos)
        new_shippos.save()
        new_shippos.save()
        serializer = ShipPositionSerializer(new_shippos)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset= self.get_queryset()
        mission_id = request.GET.get('missionid')
        if mission_id:
            queryset = queryset.filter(
                mission__id = mission_id).order_by('-date_time')
        serializer = ShipPositionSerializer(queryset, many=True)
        return Response(serializer.data)
