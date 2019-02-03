"""
A very basic Gallery App Model that has an image and its description with date
"""
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from datetime import datetime
from django.db import models
from stdimage import StdImageField
from django.conf import settings
from .compress import compress

User = get_user_model()

class ImageCategory(models.Model):
    """Category class to categorize the images"""

    category = models.CharField(max_length=100)
    representative_image = StdImageField(upload_to='category_images/', variations={'thumbnail': (786, 1048, True)}, blank=True)

    class Meta:

        verbose_name = "Image Category"
        verbose_name_plural = "Image Categories"

    def save(self, *args, **kwargs):
        representative_image = compress(self.representative_image)
        self.representative_image = representative_image
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.category)

class SubCategory(models.Model):

    parent =  models.ForeignKey(ImageCategory, on_delete=models.CASCADE, related_name='subcategory_list')
    name = models.CharField(max_length=100)

    class Meta:

        verbose_name = "Sub-Category"
        verbose_name_plural = "Sub-Categories"
    
    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    """
    A collection of all tags of an image
    """
    name = models.CharField(max_length=25)

    class Meta:
    
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return str(self.name)


class Image(models.Model):
    """ 
    Main Class of Gallery
    """
    slug = models.SlugField(max_length=50, unique=True, blank=True, help_text="THIS is field is AUTO-GENERATED keep it empty")
    category = models.ForeignKey(ImageCategory, on_delete=models.SET_DEFAULT, default=0)
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)
    image = StdImageField(upload_to='images/', variations={'thumbnail': (786, 1048, True)}, blank=True)
    label = models.CharField(max_length=100, help_text="Name of the image must be related to image attributes")
    tags = models.ManyToManyField(Tag, blank=True, related_name='images')
    date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='pic_liked')
   
    class Meta:

        verbose_name = "Image"
        verbose_name_plural = "Images"


    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super(Image, self).save(*args, **kwargs)    

    def __str__(self):
        return "Image: " + str(self.category)


