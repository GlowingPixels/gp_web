from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage import StdImageField

class CustomUser(AbstractUser):

    profile_pic = StdImageField(upload_to="profile_pic/", variations={'cover': (800, 200, True)}, blank=True)
    