"""A basic view for the Gallery App"""

from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Gallery, ImageCategory
from .forms import ImageCreateForm
from django.contrib.auth.decorators import login_required

def gallery(req, category=None):
    """
    Default view that renders all the images
    in a category
    """

    if(category!=None):
        tag = ImageCategory.objects.filter(category=category)
        images = Gallery.objects.filter(tag__in=tag)
    else:
        images = Gallery.objects.all()

    context = {
            'images': images,
            'category': category,
            }
    return render(req, 'gallery/homepage.html', context=context)
  
    

def gallery360(req, category):
    """
    A generic view Function that renders the 360 images
    """
    image360 = {'images': Gallery.objects.filter(is_360=True).filter(tag=category)}

    return render(req, 'gallery/gallery360.html', image360)

@login_required
def create_image(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.contributor = request.user
            instance.save()
            return redirect('gallery:homepage')
    else:
        form = ImageCreateForm()
        return render(request, 'gallery/imagecreate.html', {'form': form})

@login_required
def add_likes(request, id):
    
    user = request.user
    image = Gallery.objects.get(id=id)
    if user.pic_liked.filter(id=image.id).exists():
        image.likes.remove(user)
    else:
        image.likes.add(user)
    image.save()
    return HttpResponse("Liked")


def has_liked(request, id):
    print("Im callde")
    user = request.user
    image = Gallery.objects.get(id=id)
    if user.pic_liked.filter(id=image.id).exists():
        return HttpResponse("True")
    else:
        return HttpResponse("False")
