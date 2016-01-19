from django.conf.urls import include, url
from backend import views

urlpatterns = [
    url(r'^register/', views.user_register),
    url(r'^verify/(?P<token>\w+)/$', views.email_confirm),
    url(r'^user/', views.login_check),
    url(r'^login/', views.user_login),
    url(r'^emailverified/', views.email_check),
]
