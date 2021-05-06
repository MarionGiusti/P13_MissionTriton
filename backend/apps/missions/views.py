from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import MissionSerializer, TimeLineSerializer, ShipPositionSerializer
from .models import Mission, TimeLine, ShipPosition

class MissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class TimeLineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TimeLine.objects.all()
    serializer_class = TimeLineSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        print("TRALALA", request.data)
        data = request.data
        mission = Mission.objects.get(id = data["missionId"])

        if (data["form"]["end_date"]):
            end_date = data["form"]["end_date"]
            # new_task = Schedule.objects.create(user=user, mission=mission, name=data["name"], details=data["details"], start=data["start"], end=data["end"], color=data["color"])
        else:
            end_date = None

        if (data["form"]["description"]):
            description = data["form"]["description"]
            # new_task = Schedule.objects.create(user=user, mission=mission, name=data["name"], details=data["details"], start=data["start"], end=data["end"], color=data["color"])
        else:
            description = ""


        new_timeline = TimeLine.objects.create(mission=mission, name=data["form"]["name"], description=description, start_date=data["form"]["start_date"], end_date=end_date, color=data["form"]["color"])
        print("new timeline:", new_timeline)
        new_timeline.save()
        serializer = TimeLineSerializer(new_timeline)
        return Response(serializer.data)

    def list(self, request):
        # print("HALLOOOOOOO")
        queryset= self.get_queryset().order_by('-start_date')
        mission_id = request.GET.get('missionid')        
        
        if mission_id:
            queryset = queryset.filter(mission_id = mission_id).order_by('-start_date')
        
        serializer = TimeLineSerializer(queryset, many=True)
        # print("serializer.data:", serializer.data)
        return Response(serializer.data)

class ShipPositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShipPosition.objects.all()
    serializer_class = ShipPositionSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        print("TRALALA", request.data)
        data = request.data
        mission = Mission.objects.get(id = data["mission"])
        new_shippos = ShipPosition.objects.create(mission=mission, latitude=data["form"]["latitude"], longitude=data["form"]["longitude"], date_time=data["form"]["date_time"])
        print("new shippos:", new_shippos)
        new_shippos.save()
        serializer = ShipPositionSerializer(new_shippos)
        return Response(serializer.data)

    def list(self, request):
        queryset= self.get_queryset()
        mission_id = request.GET.get('missionid')        
        if mission_id:
            queryset = queryset.filter(mission__id = mission_id).order_by('-date_time')
        serializer = ShipPositionSerializer(queryset, many=True)
        # print("serializer.data:", serializer.data)
        return Response(serializer.data)