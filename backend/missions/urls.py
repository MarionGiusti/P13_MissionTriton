from django.urls import path, include
from rest_framework import routers

from .views import (
	MissionViewSet, 
	TimeLineViewSet, 
	ShipPositionViewSet
)

router = routers.DefaultRouter()
router.register(r'timelines', TimeLineViewSet)
router.register(r'shippositions', ShipPositionViewSet)
router.register(r'', MissionViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
