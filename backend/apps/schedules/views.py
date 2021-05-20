from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Q

from apps.users.permissions import IsScheduleOwner
from apps.users.models import CustomUser
from apps.missions.models import Mission
from .serializers import ScheduleSerializer
from .models import Schedule

class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsScheduleOwner,)

    def create(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id = request.user.id)
        data = request.data
        if data["mission"]:
            mission = Mission.objects.get(name= data["mission"])
        else:
            mission = None
        new_task = Schedule.objects.create(
            user=user, mission=mission, name=data["name"],
            details=data["details"], start=data["start"],
            end=data["end"], color=data["color"])
        new_task.save()
        serializer = ScheduleSerializer(new_task)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
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
        return Response(serializer.data)
