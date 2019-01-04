"""Urls patterns of the Gallery App"""
from . import views
from django.urls import path

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery, name='homepage'),
    path('create/image', views.create_image , name='createImage'),
    path('<str:category>/', views.gallery, name='gallery'),
    path('<str:category>/image360/', views.gallery360, name='gallery360'),
]