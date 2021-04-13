from django.db import models

from apps.users.models import MissionUser
from apps.missions.models import Mission


class Post(models.Model):
    mission_user = models.ForeignKey(MissionUser, related_name="posts", on_delete=models.PROTECT)
    mission = models.ForeignKey(Mission, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, null=False)
    content = models.TextField()
    date = models.DateField(null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    post_image = models.ImageField(upload_to="post_pics", 
            null=True, 
            blank=True) 
            # width_field="width_field", 
            # height_field="height_field")
    # height_field = models.IntegerField(default=0)
    # width_field = models.IntegerField(default=0)
    video_url = models.URLField(null=True, blank=True)
    CATEGORY_STATUS = (
        (0, 'Actu'),
        (1, 'Mediation'),
        (2, 'A_bord')
    )
    category = models.IntegerField(choices=CATEGORY_STATUS)
