from django.db import models

from apps.users.models import MissionUser
from apps.missions.models import Mission


class Post(models.Model):
    mission_user = models.ForeignKey(MissionUser, related_name="posts", on_delete=models.PROTECT)
    mission = models.ForeignKey(Mission, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(upload_to="post_pics", blank=True, null=True) 
    # default="seashell.png"
            # width_field="width_field", 
            # height_field="height_field")
    # height_field = models.IntegerField(default=0)
    # width_field = models.IntegerField(default=0)
    video_url = models.URLField(null=True, blank=True)
    CATEGORY_STATUS = (
        # (0, 'Actu'),
        # (1, 'Médiation'),
        # (2, 'À bord')
        ('Actu', 'Actu'),
        ('Med', 'Médiation'),
        ('Onboard', 'À bord')
    )
    # category = models.IntegerField(choices=CATEGORY_STATUS)
    category = models.CharField(max_length=20, choices=CATEGORY_STATUS)

    def __str__(self):
        return f'{self.mission} {self.category}: {self.title} / {self.created_at}'

class Picture(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="missions_pics", null=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.mission} : {self.picture}'