from django.urls import path, include
# from django.conf.urls import include
from rest_framework import routers

from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    path('',include(router.urls)),
]