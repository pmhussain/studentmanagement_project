from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    designation = models.CharField(max_length=500, blank=True, null =True)
    mobileno = models.CharField(max_length=30, blank=True, null =True)
    profile_pic = models.ImageField(default='img_avatar.png', blank=True)
