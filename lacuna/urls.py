from django.conf.urls import patterns, url
from lacuna import views
urlpatterns = [
    url(r'^status/$', status),
    url(r'^login/$', user_login),
    url(r'^filterpuzzle/$', dvm1verify),
]
