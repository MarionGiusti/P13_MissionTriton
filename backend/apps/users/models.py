from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import AbstractUser 
from django.db import models


# class User(AbstractUser):
#     profile_pic = models.ImageField(upload_to="profile_pics", default="profile.png", null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profile_pics", default="profile.png", null=True)
    linkedin_profile = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.update_or_create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)