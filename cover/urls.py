from cover import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.preIntro),
    ]
