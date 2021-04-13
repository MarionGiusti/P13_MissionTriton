from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from .serializers import MissionSerializer, TimeLineSerializer, ShipPositionSerializer
from .models import Mission, TimeLine, ShipPosition

class MissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = (AllowAny,)

class TimeLineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TimeLine.objects.all()
    serializer_class = TimeLineSerializer
    permission_classes = (AllowAny,)

class ShipPositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShipPosition.objects.all()
    serializer_class = ShipPositionSerializer
    permission_classes = (AllowAny,)