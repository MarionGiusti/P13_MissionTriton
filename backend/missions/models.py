"""
Define model Mission, Timeline and ShipPosition
"""
from django.utils import timezone
from django.db import models

class Mission(models.Model):
    """ Class Mission to define each mission """
    name = models.CharField(max_length=100, unique=True, null=False)
    ship_name = models.CharField(max_length=200, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """Method to change the object name in QuerySet """
        return self.name

class TimeLine(models.Model):
    """ Class Timeline to define an event in the timeline """
    mission = models.ForeignKey(Mission, related_name="timelines", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(default='', blank=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=7, default="#B6885D", null=True)

    def __str__(self):
        """Method to change the object name in QuerySet """
        return f'{self.mission.name} {self.name}'

class ShipPosition(models.Model):
    """ Class ShipPosition to define the coordinates of the ship during the mission """
    mission = models.ForeignKey(Mission, related_name="ship_positions", on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=False, unique=True, default=timezone.now)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    # name = models.CharField(max_length=200, null=True)
    # description = models.TextField(null= True, blank=True)

    def __str__(self):
        """Method to change the object name in QuerySet """
        return f'{self.mission.name} {self.date_time}'

    @property
    def full_position(self):
        return str(self.date_time) + ", " + str(self.latitude) + ", " + str(self.longitude)
