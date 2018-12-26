from django.conf.urls import url
from .views import register, user_login, user_logout, user_info

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^profile/$', user_info, name='profile')
]