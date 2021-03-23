from django.urls import path, include
# from django.conf.urls import include
from rest_framework import routers

from .views import UserViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profile', UserProfileViewSet)
print(router.urls)
urlpatterns = [
    path('',include(router.urls)),
]