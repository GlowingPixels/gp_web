"""Urls patterns of the Gallery App"""
from . import views
from django.urls import path


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<str:category>/', views.gallery, name='gallery'),
    path('<str:category>/image360/', views.gallery360, name='gallery360'),
]