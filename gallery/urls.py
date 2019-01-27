"""Urls patterns of the Gallery App"""
from . import views
from django.urls import path

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery, name='homepage'),
    path('add/image', views.create_image , name='addImage'),
    path('<str:category>/', views.gallery, name='gallery'),
    path('like/<int:id>/', views.add_likes, name="like"), #hardcoded urlpattern implemented html id
    path("like/<int:id>/check/", views.has_liked, name="check_like") #exclusively for ajax check of user liked images
]