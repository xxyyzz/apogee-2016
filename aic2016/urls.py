from aic2016 import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.website),
    url(r'^submit/$', views.problemstatement_add),
    ]
