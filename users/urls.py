from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = "users"

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
	path('profile/', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
]