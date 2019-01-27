"""
A very basic Gallery App Model that has an image and its description with date
"""
from django.contrib.auth import get_user_model
from datetime import datetime
from django.db import models
from stdimage import StdImageField
from django.conf import settings

User = get_user_model()

class ImageCategory(models.Model):
    """Category class to categorize the images"""

    category = models.CharField(max_length=100)

    class Meta:

        verbose_name = "Image Category"
        verbose_name_plural = "Image Categories"

    def __str__(self):
        return str(self.category)

class Gallery(models.Model):
    """ Main Class of Gallery that has a tag with descriptions and date"""

    tag = models.ForeignKey(ImageCategory, default=0, on_delete=models.CASCADE)
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)
    image = StdImageField(upload_to='images/', variations={'thumbnail': (786, 1048, True)}, blank=True)
    label = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=500, blank=True)
    date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='pic_liked')
   
    class Meta:

        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return "Image: " + str(self.tag)
