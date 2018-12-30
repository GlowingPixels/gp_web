from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField


class UserProfile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = StdImageField(upload_to='profile_pic/',
                                variations={
                                     'thumbnail': (150, 150, True)
                                     },
                                blank=True)    
    def __str__(self):
        return self.user.first_name + " Username: " + self.user.username
