from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=300, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=300, blank=True)
