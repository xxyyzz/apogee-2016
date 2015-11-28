from django.conf.urls import include, url
from cms import views, utilities
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^paperxlsx/$', utilities.paper_stats_xlsx),
    url(r'^projectxlsx/$', utilities.project_stats_xlsx),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^login/(?P<errors>\d)/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^papers/$', views.paper_home, name='paper_home'),
    url(r'^projects/$', views.project_home, name='project_home'),
    # url(r'^papers/$', RedirectView.as_view(url=reverse_lazy('paper_home'))),
    url(r'^papers/(?P<status>\d+)/(?P<category>\d+)/$', views.paper_home, name='paper_home'),
    url(r'^projects/(?P<status>\d+)/(?P<category>\d+)/$', views.project_home, name='project_home'),
    url(r'^projects/email/(?P<projectid>\d+)/$', views.project_email, name='project_email'),
    # url(r'^papers/initial/$', views.paper_initial, name='paper_initial'),
    url(r'^projects/$', views.project_home, name='project_home'),
    url(r'^', views.user_login, name='user_login'),
]