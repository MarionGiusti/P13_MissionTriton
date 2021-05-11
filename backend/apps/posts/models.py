"""
Define model Post and Picture
"""
from django.db import models

from apps.users.models import MissionUser
from apps.missions.models import Mission


class Post(models.Model):
    """ Class Post with 3 categories """
    mission_user = models.ForeignKey(MissionUser, related_name="posts", on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(upload_to="post_pics", blank=True, null=True)
    video_url = models.URLField(null=True, blank=True)
    CATEGORY_STATUS = (
        ('Actu', 'Actu'),
        ('Med', 'Médiation'),
        ('Onboard', 'À bord')
    )
    category = models.CharField(max_length=20, choices=CATEGORY_STATUS)

    def __str__(self):
        """Method to change the object name in QuerySet """
        return f'{self.mission} {self.category}: {self.title} / {self.created_at}'

class Picture(models.Model):
    """ Class Picture for each picture of the gallery """
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="missions_pics", null=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        """Method to change the object name in QuerySet """
        return f'{self.mission} : {self.picture}'
