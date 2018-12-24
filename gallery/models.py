
"""
A very basic Gallery App Model that has an image and its description with date
"""
from datetime import datetime
from django.db import models
from stdimage import StdImageField


class ImageCategory(models.Model):
    """Category class to categorize the images"""

    category = models.CharField(max_length=100)

    class Meta:

        verbose_name = "Image Category"
        verbose_name_plural = "Image Categories"

    def __str__(self):
        return "Image Category: {}".format(str(self.category))

class Gallery(models.Model):
    """ Main Class of Gallery that has a tag with descriptions and date"""

    tag = models.ForeignKey(ImageCategory, default=0, on_delete=models.CASCADE)
    contributor = models.CharField(max_length=100, default="Anonymous")
    image = StdImageField(upload_to='gallery/image/', variations={'thumbnail':(1280, 720, True)}, blank=True)
    label = models.CharField(max_length=100, default="Image")
    descriptions = models.CharField(max_length=500, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_360 = models.BooleanField(default=False)
    image_360Link = models.URLField(max_length=500, blank=True)

    class Meta:

        verbose_name = "Image"
        verbose_name_plural = "Image Gallery"

    def __str__(self):
        return "Image"+str(self.tag)
