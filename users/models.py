from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator, MaxLengthValidator

MAX_VAL = 10**16
MIN_VAL = 10**9

#Model Class for more feature
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.IntegerField(validators=[MinValueValidator(MIN_VAL), MaxValueValidator(MAX_VAL)],
        blank=True, help_text="Optional Example: XXXXXXXXXX")
    profile_pic = models.ImageField(upload_to="users/profile_pic", blank=True)


    def __str__(self):
        return self.user.first_name + " Username: " + self.user.username
