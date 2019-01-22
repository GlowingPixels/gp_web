from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

app_name = "users"

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('settings/', login_required(views.Settings.as_view()), name='settings'),
	path('profile/', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    path("user/<str:fellow_username>/", views.fellow_user, name="fellow_user"),
    path("search/", views.search_user, name="search_user"),
]
