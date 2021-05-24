from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from django.conf.urls.static import static
from users.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('rest_framework.urls', namespace='rest_framework')),
    path('api/users/', include('users.urls')),
    path('api/missions/', include('missions.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/schedules/', include('schedules.urls')),
    path('api/api-token-auth/', CustomAuthToken.as_view()),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

] + static(settings.STATIC_URL) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
