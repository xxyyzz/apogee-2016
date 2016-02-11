"""apogee16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portal/', include('registrations.urls', namespace='registrations')),
    url(r'^', include('cover.urls', namespace='cover')),
    url(r'^pcradmin/', include('pcradmin.urls', namespace='pcradmin')),
    url(r'^manage/', include('cms.urls', namespace='cms')),
    url(r'^aic/', include('aic2016.urls', namespace='aic2016')),
    url(r'^iot/', include('iot.urls', namespace='iot')),
    url(r'^aarohan/', include('aarohan.urls', namespace='aarohan')),
    url(r'^dhiti/', include('dhiti.urls', namespace='dhiti')),
    url(r'^youthcon/', include('youthcon.urls', namespace='youthcon')),
    url(r'^events/', include('Event.urls', namespace='Event')),
    url(r'^api/', include('backend.urls', namespace='api')),
    url(r'^', include('regsoft.urls', namespace='regsoft')),
    
]
