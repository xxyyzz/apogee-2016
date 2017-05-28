from pcradmin import views
from registrations.views import *
from cms import utilities
from django.conf.urls import url, include
from pcradmin.apogeepcr import *
urlpatterns = [
    url(r'^$', views.dashboard2),

    url(r'^ambassadors/$', views.ambassadors_list),
    url(r'^app_amb/$', views.app_amb),
    url(r'^amb_act/$', views.amb_act),
    url(r'^amb_xlsx/$', views.ambassador_approved_xlsx),
    url(r'^mail_approved/$', views.mail_approved),
    url(r'^initreg/$', views.initial_registration),
    url(r'^part_list/$', views.part_list),
    url(r'^part_list_xlsx/$', views.lev_partlist),    
    url(r'^part_list/(?P<part_id>\d+)/$', views.part_details),
    url(r'^participantxlsx/$', utilities.participant_stats_xlsx),
    url(r'^part_act/$', views.part_act),

    url(r'^vpdf/(?P<gl_id>\d+)/$', view_pdf, name='view and generate pdf'),


    url(r'^mail_selected/$', views.mail_selected_amb),

    url(r'^dhiti_xlsx/$', views.dhiti_xlsx),
    url(r'^reng_xlsx/$', views.RENG_xlsx),
    url(r'^innover_xlsx/$', views.innover_xlsx),
    # url(r'^username/save/(?P<user_id>\d+)/$', views.username_save),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^sendconfirmationmails/$', send_mail),
    url(r'^sendmails/$', send_mail_full),
    # url(r'^$', views.home),
    # url(r'^college/select/$', views.college_select),
    # # url(r'^username/set/(?P<user_id>\d+)/$', views.username_set),
    # url(r'^college/plist/$', views.init_list),
    # url(r'^college/set/(?P<user_id>\d+)/$', views.view_Crep),
    # url(r'^college/save/(?P<user_id>\d+)/$', views.Crep_save),
    # url(r'^clg_list/$', views.std_list_college),
    # url(r'^clg_list/stdview_clg/$', views.stdview_college),
    # url(r'^clg_list/stdview_clg/collegelist/$', college_list),
    # url(r'^clg_list/change_req/$', views.change_req),
    # url(r'^college/crep_email/(?P<user_id>\d+)/$', views.crep_email),

    # url(r'^changelimit/$', views.change_team_limits),
    # url(r'^change_team_limit/$', views.change_team_limit_list),
    # url(r'^limit_changed/$', views.change_limits),
    # url(r'^sportlimit/select/$', views.sportlimit_select, name='sportlimits'),
    # url(r'^sportlimit/change/$', views.sportlimit_change),
    # url(r'^sportlimit/save/$', views.sportlimit_save),
    # url(r'^email/select/$', views.email_select),
    # url(r'^email/compose/$', views.email_compose),
    # url(r'^email/statchange/$', views.email_statchange, name='statchange'),
    # url(r'^email/send/$', views.email_send),
    # url(r'^status/select/$', views.status_select),
    # url(r'^status/set/$', views.status_set),
    # url(r'^status/save/$', views.status_save),
    url(r'^logout/$', views.pcr_logout),
    # # url(r'^sports_limits_changed/$', views.save_sports_limits),
    # # url(r'^setstatus/$', views.set_status),
    # # url(r'^showstatus/$', views.save_status),
    # url(r'^emailsend/$', views.send_mail),

    # # url(r'^compose/$', views.compose),
    # url(r'^listuser/$', views.user_list),
    # url(r'^participantlist/$', views.participant_list),
    # url(r'^users/$', views.search_user),
    # url(r'^participants/$', views.search_plist),
    # url(r'^pconfirm/$', views.pconfirm),
    # url(r'^pedit$', views.pedit),


    # url(r'^stats/paid_list$', views.paid_list, name='paid'),
    # url(r'^stats/paid_list/paid_act$', views.paid_act, name='paid_act'),
    url(r'^stats/$', views.eventwise_stats, name='stats'),
    url(r'^stats/(?P<event_id>\d+)/$', views.event_part),

    url(r'^total_stats/$', views.total_stats, name='stats'),
    url(r'^ambassadorxlsx/$', utilities.ambassador_stats_xlsx),

    # url(r'^stats/$', views.stats_eventwise, name='stats'),
    # url(r'^stats/eventwise/$', views.stats_eventwise, name='stats_eventwise'),
    # url(r'^stats/collegewise/$', views.stats_collegewise, name='stats_collegewise'),
    # url(r'^stats/(?P<collegeid>\d+)/(?P<eventid>\d+)/$', views.stats_college_event, name='stats_college_event'),
    # url(r'^stats/college/(?P<collegeid>\d+)/$', views.stats_college, name='stats_college'),
    # url(r'^stats/event/(?P<eventid>\d+)/$', views.stats_event, name='stats_event'),
    # url(r'^stats/unstandardised/$', views.stats_unstandardised, name='stats_unstandardised'),

    # url(r'^loginas/warning/$', views.loginas_warning),
    # url(r'^loginas/select/$', views.loginas_select),
    # url(r'^loginas/user/(?P<userid>\d+)/$', views.loginas_login),
    # # url(r'^gausstest/$', views.gausstest),
    # url(r'^pdf/select/$', views.pdf_select, name='customise_events'),
    # url(r'^pdf/edit/(?P<userid>\d+)/$', views.pdf_edit),
    # url(r'^pdf/save/(?P<userid>\d+)/$', views.pdf_save, name='pdf_save'),
    # url(r'^excelrep/$', views.gauss_xlsx),
    # url(r'^excelrep2/$', views.controlz_xlsx),
    # url(r'^(?P<pagename>\w+)/', views.pathfinder),
    ]
