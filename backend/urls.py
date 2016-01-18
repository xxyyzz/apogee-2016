from django.conf.urls import include, url
from registration import views
from registration.game import *

urlpatterns = [
    url(r'^register/', views.register),
]
