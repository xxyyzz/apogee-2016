from cover import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^preintro/$', views.preIntro),
    url(r'^$', views.main),
    ]
