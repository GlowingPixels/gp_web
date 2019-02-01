"""Urls patterns of the Gallery App"""
from . import views
from django.urls import path

app_name = 'gallery'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add/image', views.create_image , name='addImage'),
    path('<str:category>/', views.category_images, name='category'),
    path('like/<int:id>/', views.add_likes, name="like"), #hardcoded urlpattern implemented html id
    path("like/<int:id>/check/", views.has_liked, name="check_like") #exclusively for ajax check of user liked images
]