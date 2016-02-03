from django.conf.urls import include, url
from backend import views
from backend import views_profile

urlpatterns = [
    url(r'^register/', views.user_register),
    url(r'^verify/(?P<token>\w+)/$', views.email_confirm),
    url(r'^user/', views.login_check),
    url(r'^login/', views.user_login),
    url(r'^logout/', views.user_logout),
    url(r'^emailverified/', views.email_check),
    url(r'^events/status/', views.events_check),
    url(r'^events/register/(?P<eventid>[0-9]+)/$', views.register_single),
    url(r'^events/unregister/(?P<eventid>[0-9]+)/$', views_profile.unregister_single),
    url(r'^events/team/register/(?P<eventid>[0-9]+)/$', views.register_team),
    url(r'^events/team/unregister/(?P<teamid>[0-9]+)/$', views_profile.unregister_team),
    url(r'^events/team/delete/(?P<teamid>[0-9]+)/$', views_profile.delete_team),
    url(r'^profile/update/$', views_profile.update_profile),
    url(r'^profile/$', views_profile.summary),
    url(r'^participant/(?P<participantid>[0-9]+)/$', views.participant_summary),
    url(r'^pay/$', views_profile.instamojo_payment),
    url(r'^thank_you/$', views_profile.apirequest_fee),
    url(r'^getupdatedata/$', views.getupdatedata),
]
