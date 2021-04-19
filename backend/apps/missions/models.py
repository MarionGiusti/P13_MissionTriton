# from geoposition.fields import GeopositionField

from django.db import models

class Mission(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    ship_name = models.CharField(max_length=200, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return self.name

class TimeLine(models.Model):
    mission = models.ForeignKey(Mission, related_name="timelines", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True, null=False)
    description = models.TextField(default='', blank=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return f'{self.mission.name} {self.name}'

class ShipPosition(models.Model):
    mission = models.ForeignKey(Mission, related_name="ship_positions", on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=False, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    # position = GeopositionField()

    def __str__(self):
        return f'{self.mission.name} {self.date_time}'

    @property
    def full_position(self):
        return str(self.date_time) + ", " + str(self.latitude) + ", " + str(self.longitude)
