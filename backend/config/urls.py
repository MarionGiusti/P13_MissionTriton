from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from django.conf.urls.static import static
from apps.users.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('api/users/', include('apps.users.urls')),
    path('api/missions/', include('apps.missions.urls')),
    path('api/posts/', include('apps.posts.urls')),
    path('api/schedules/', include('apps.schedules.urls')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

] + static(settings.STATIC_URL) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
