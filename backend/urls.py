from django.conf.urls import include, url
from backend import views

urlpatterns = [
    url(r'^register/', views.register),
    url(r'^verify/(?P<token>\w+)/$', views.email_confirm),
]
