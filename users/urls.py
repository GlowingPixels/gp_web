from django.urls import path
from .views import user_signup, user_login, user_logout, user_info

urlpatterns = [
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_info, name='profile')
]