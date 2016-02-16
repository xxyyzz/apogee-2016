from django.conf.urls import patterns, url
from ems.views import *
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', user_login, name='user_login'),
    url(r'^logout/$', user_logout, name='user_logout'),
    url(r'^uploadlist/$', upload_list, name='upload_list'),
    url(r'^chooseLeader/$', choose_leader, name='choose_leader'),
    url(r'^genTeam/$', genTeam, name='genTeam'),
    url(r'^addbitsian/$', bitsian_add, name='add_bitsian'),
    url(r'^participantdetails/(?P<partid>\d+)/$', participant_details, name="participant_details"),
    url(r'^participantdetails/$', participant_details_home, name="participant_home"),
    url(r'^events/$', events_select, name="events_select"),
    url(r'^events/(?P<eventid>\d+)/levels/$', events_levels, name="events_levels"),
    url(r'^events/(?P<eventid>\d+)/home/$', events_home, name="events_home"),
    url(r'^teamdetails/(?P<teamid>\d+)/$', team_details, name="team_details"),
    url(r'^teamdetails/$', team_details_home, name="team_home"),
	url(r'^getparticipantlist/$', getParticipantList, name='getParticipantList'),
]
