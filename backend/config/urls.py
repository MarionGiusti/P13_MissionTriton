from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('api/users/', include('apps.users.urls')),
    path('api-token-auth/', views.obtain_auth_token),
]
