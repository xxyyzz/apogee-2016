from cover import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^preintro/$', views.preIntro),
    url(r'^intro/$', views.intro),
    url(r'^sponsors/$', views.spons),
    url(r'^$', views.main),
    ]
