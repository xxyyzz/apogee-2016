from django.conf.urls import include, url
from cms import views, utilities

urlpatterns = [
    url(r'^paperxlsx/$', utilities.paper_stats_xlsx),
    url(r'^projectxlsx/$', utilities.project_stats_xlsx),
    url(r'^papers/$', views.paper_home, name='paper_home'),
    url(r'^papers/(?:(?P<status>\d)/)$', views.paper_home, name='paper_home'),
    # url(r'^papers/initial/$', views.paper_initial, name='paper_initial'),
    url(r'^projects/$', views.project_home, name='project_home'),
]