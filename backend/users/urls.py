from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, MissionUserViewSet

router = routers.DefaultRouter()
router.register(r'missionusers', MissionUserViewSet)
router.register(r'', UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
