from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, PictureViewSet

router = routers.DefaultRouter()
router.register(r'gallery', PictureViewSet)
router.register(r'', PostViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
