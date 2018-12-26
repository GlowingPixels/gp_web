"""A basic view for the Gallery App"""
from django.shortcuts import render
from .models import Gallery

def gallery(req, category=None):
    """
    Default view that renders all the images
    in a category
    """
    if(category):
        images = Gallery.objects.filter(tag=category)
        context = {
            'images': images,
            'category': category,
            }
        return render(req, 'category/category.html', context=context)
    else:
        context = {
            'images': Gallery.objects.all()
            }
        return render(req, 'homepage/homepage.html', context=context)
  
    

def gallery360(req, category):
    """
    A generic view Function that renders the 360 images
    """
    image360 = {'images': Gallery.objects.filter(is_360=True).filter(tag=category)}

    return render(req, 'gallery/gallery360.html', image360)
