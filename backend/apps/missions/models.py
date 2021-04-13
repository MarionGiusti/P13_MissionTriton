from django.db import models
# from geoposition.fields import GeopositionField

# from apps.users.models import User

class Mission(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    ship_name = models.CharField(max_length=200, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    # user = models.ManyToMany(User)

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
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    #rajouter date
    # position = GeopositionField()
    def __str__(self):
        return f'{self.mission.name} {self.date}'