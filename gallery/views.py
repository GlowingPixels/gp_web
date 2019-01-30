"""A basic view for the Gallery App"""
from django.db.models import Count
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import Gallery, ImageCategory
from .forms import ImageCreateForm

def gallery(req, category=None):
    """
    Default view that renders all the images
    in a category
    """
    if(category != None):
        category_obj = ImageCategory.objects.filter(category=category)
        images = Gallery.objects.annotate(like_count=Count('likes')).order_by('-like_count').filter(category__in=category_obj)[:20]
    else:
        images = Gallery.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:20]

    context = {
            'images': images,
            'category': category,
        }
    return render(req, 'gallery/homepage.html', context=context)

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
        image.save()
        return HttpResponse("Unliked")
    else:
        image.likes.add(user)
        image.save()
        return HttpResponse("Liked")

@login_required
def has_liked(request, id):

    user = request.user
    image = Gallery.objects.get(id=id)
    if user.pic_liked.filter(id=image.id).exists():
        return HttpResponse("True")
    else:
        return HttpResponse("False")
