"""A basic view for the Gallery App"""
from django.shortcuts import render
from .models import Gallery


def gallery(req, category):
    """
    Default view that renders all the images
    in a category
    """

    images = {'images': Gallery.objects.filter(tag=category)}
  
    return render(req, 'gallery/gallery.html', images)

def gallery360(req, category):
    """
    A generic view Function that renders the 360 images
    """
    image360 = {'images': Gallery.objects.filter(is_360=True).filter(tag=category)}

    return render(req, 'gallery/gallery360.html', image360)
