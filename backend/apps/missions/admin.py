from django.contrib import admin

from .models import Mission, TimeLine, ShipPosition

admin.site.register(Mission)

@admin.register(TimeLine)
class TimeLineAdmin(admin.ModelAdmin):
    list_filter = ['mission']

@admin.register(ShipPosition)
class ShipPositionAdmin(admin.ModelAdmin):
    list_filter = ['mission']