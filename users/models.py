from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage import StdImageField

class CustomUser(AbstractUser):

    profile_pic = models.ImageField(upload_to="profile_pic/", blank=True, default="profile.jpg")
    cover_pic = models.ImageField(upload_to="cover_pic/", blank=True, default="cover.jpg")
    facebook_link = models.URLField(max_length=200, blank=True)
    instagram_link = models.URLField(max_length=200, blank=True)
    
