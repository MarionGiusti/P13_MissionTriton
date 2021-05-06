from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from django.db.models import Q

from .serializers import ScheduleSerializer
from .models import Schedule
from apps.users.models import CustomUser
from apps.missions.models import Mission

from apps.users.permissions import IsOwner

class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (IsOwner,)

    def create(self, request, *args, **kwargs):
        print("TRALALA", request.data)
        user = CustomUser.objects.get(id = request.user.id)

        data = request.data
        if (data["mission"]):
            mission = Mission.objects.get(name= data["mission"])
            # new_task = Schedule.objects.create(user=user, mission=mission, name=data["name"], details=data["details"], start=data["start"], end=data["end"], color=data["color"])
        else:
            mission = None
            # new_task = Schedule.objects.create(user=user, name=data["name"], details=data["details"], start=data["start"], end=data["end"], color=data["color"])
        new_task = Schedule.objects.create(user=user, mission=mission, name=data["name"], details=data["details"], start=data["start"], end=data["end"], color=data["color"])
        print("new task:", new_task)
        new_task.save()
        serializer = ScheduleSerializer(new_task)
        return Response(serializer.data)

    # def list(self, request):
    #     # self.checkobjectpermission
    #     print("HULLOOOOOOO", request.user.id)
    #     queryset= self.get_queryset()
    #     # queryset = queryset.filter(mission_user__user = request.user.id)
    #     queryset = queryset.filter(user = request.user.id)
    #     serializer = ScheduleSerializer(queryset, many=True)
    #     print("serializer.data:", serializer.data)
    #     return Response(serializer.data)

    def list(self, request):
        print("HULLOOOOOOO", request.user.id)
        queryset= self.get_queryset()
        user = CustomUser.objects.get(id = request.user.id)
        missions_user = user.missions.all().values('id')

        missions_id = []
        for miss in missions_user:
            missions_id.append(miss['id'])

        queryset= queryset.filter(
            Q(user = request.user.id) |
            Q(mission__in = missions_id)
        )

        serializer = ScheduleSerializer(queryset, many=True)
        print("serializer.data:", serializer.data)
        return Response(serializer.data)
