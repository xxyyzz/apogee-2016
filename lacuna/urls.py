from django.conf.urls import patterns, url
from lacuna.views import *
urlpatterns = [
    url(r'^$', home),
    url(r'^status/$', status),
    url(r'^login/$', user_login),
    url(r'^dvm/getlevel/$', dvm_level_get),
    url(r'^informals/verifylevel/$', informals_level_verify),
    url(r'^dvm/filterpuzzle/$', dvm1verify),
    url(r'^dvm/colourmatch/$', dvm2verify),
]
