from django.urls import path, include
# from django.conf.urls import include
from rest_framework import routers

from .views import (
	MissionViewSet, 
	TimeLineViewSet, 
	ShipPositionViewSet
)

router = routers.DefaultRouter()
router.register(r'timeline', TimeLineViewSet)
router.register(r'shipposition', ShipPositionViewSet)
router.register(r'', MissionViewSet)

urlpatterns = [
    path('',include(router.urls)),
]