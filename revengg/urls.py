from revengg import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^create/$', views.create),
    url(r'^update/$', views.update),
    url(r'^$', views.software),


]
