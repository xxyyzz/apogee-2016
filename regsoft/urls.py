from django.conf.urls import patterns, url
from regsoft.views import *

urlpatterns = [
	url(r'^firewallzouter/scan/$', firewallzo_dashboard),
	url(r'^firewallzouter/scan/(?P<part_id>\d+)$', firewallzo_dashboard_two),
	url(r'^firewallzouter/confirm/$', firewallzo_confirm),
# 	url(r'^firewallzouter/confirm/(?P<crep_id>\d+)$', firewallzo_setgleader),
	url(r'^firewallzouter/edit/(?P<part_id>\d+)$', firewallzo_edit_part),
	url(r'^firewallzouter/pcodes/$', gcodelist),
# 	url(r'^firewallzouter/testx/$', testx),
	url(r'^firewallzouter/unconfirm/(?P<part_id>\d+)$', firewallzo_unconfirm),
# 	url(r'^firewallzouter/unconfirmed/(?P<crep_id>\d+)$', firewallzo_unconfirm),
	url(r'^firewallzouter/add/$', firewallzo_add),
# 	url(r'^firewallzouter/add_guest/$', firewallzo_add_guest),
	url(r'^firewallzouter/barcodelist/$', get_barcode),

# 	url(r'^common/search/$', common_search,  name="common_search"),

	url(r'^controlz/home/$', controlz_home),
	url(r'^controlz/home/(?P<part_id>\d+)$', controlz_dashboard),
# 	url(r'^controlz/stats/$', controlz_stats, name="controlz_stats"),
# 	url(r'^controlz/edit/(?P<part_id>\d+)$', controlz_edit_part),
# 	url(r'^controlz/bill_select/$', controlz_bill_select),
# 	url(r'^controlz/bill_delete/$', controlz_delete_bill),
# 	url(r'^controlz/bill_view/(?P<billid>\d+)/$', controlz_view_bill),
# 	url(r'^controlz/bill_details/(?P<gl_id>\d+)$', controlz_bill_details),
# 	url(r'^controlz/recnacc_bill_list/$', recnacc_bill_list),
# 	url(r'^controlz/recnacc_bill_print/(?P<gl_id>\d+)$', recnacc_bill_print),
# 	# url(r'^controlz/billdetails/(?P<bill_id>\d+)$', ),

# 	url(r'^controlz/bill_print/$', controlz_bill_print),
# 	url(r'^group_notify/$', recnacc_notify),



	url(r'^recnacc/home/$', recnacc_home),
	url(r'^recnacc/home/(?P<pid>\d+)$', recnacc_dashboard),
	url(r'^recnacc/allot/(?P<pid>\d+)$', recnacc_allot),
# 	url(r'^recnacc/faculty_allot/(?P<gl_id>\d+)$', recnacc_faculty_allot),
	url(r'^recnacc/deallocate/(?P<pid>\d+)$', recnacc_deallocate),
	url(r'^recnacc/checkout/(?P<pid>\d+)$', recnacc_checkout),
# 	#url(r'^recnacc/return_inventory/(?P<gl_id>\d+)$', recnacc_return_inventory),
# 	url(r'^recnacc/checkedout_select_gl/$', recnacc_checkedout_select_gl),
# 	url(r'^recnacc/checked_out_participants/(?P<gl_id>\d+)$', recnacc_checked_out_participants),
# 	url(r'^recnacc/checked_out_list/(?P<gl_id>\d+)$', recnacc_checked_out_participants_in),
# 	url(r'^recnacc/bhavan_inventory_list/$', recnacc_bhavan_inventory_list),
# 	url(r'^recnacc/room_availibility_list/$', recnacc_room_availibility_list),
# 	url(r'^recnacc/bhavan_gleader_list/$', recnacc_bhavan_gleader_list),
	url(r'^recnacc/room_list/$', recnacc_room_list),
	url(r'^recnacc/room_details/(?P<room_id>\d+)$', recnacc_room_details),
	

# 	url(r'^teams/$', mainScreen, name='main'),
# 	url(r'^teams/uploadlist/$', upload_list, name='upload_list'),
# 	url(r'^teams/chooseLeader/$', choose_leader, name='choose_leader'),
# 	url(r'^teams/genTeam/$', genTeam, name='genTeam'),
# 	url(r'^teams/addbitsian/$', bitsian_add, name='add_bitsian'),

# 	url(r'^teams/participantdetails/(?P<partid>\d+)/$', participant_details, name="participant_details"),
# 	url(r'^teams/participantdetails/$', participant_details_home, name="participant_home"),
# 	url(r'^teams/eventdetails/(?P<eventid>\d+)/$', event_details, name="event_details"),
# 	url(r'^teams/eventdetails/$', event_details_home, name="event_home"),
# 	url(r'^teams/teamdetails/(?P<teamid>\d+)/$', team_details, name="team_details"),
# 	url(r'^teams/teamdetails/$', team_details_home, name="team_home"),

# 	url(r'^teams/getparticipantlist/$', getParticipantList, name='getParticipantList'),

# 	url(r'^teams/selectEvent_delete/$', selectEvent_manageTeams, name='selectEvent_manageTeams'),
# 	url(r'^teams/selectTeam_delete/$', showTeams_manageTeams, name='showTeams_manageTeams'),
# 	url(r'^teams/deleteTeams/$', deleteTeam_manageTeams, name='deleteTeam_manageTeams'),

# 	url(r'^teams/show_teamList/$', eventlist_showTeams, name='eventlist_showTeams'),
# 	url(r'^teams/show_selectEvent/$', eventList_selectEvent, name='eventList_selectEvent'),
# 	url(r'^teams/singleTeam/(?P<team_id>\d+)/$', eventList_selectEvent, name='eventList_selectEvent'),
 
#  	url(r'^teams/finalist_selectEvent/$', finalist_selectEvent, name="finalist_selectEvent"),   
#  	url(r'^teams/finalist_showTeams/$', finalist_showTeams, name="finalist_showTeams"),   
#  	url(r'^teams/setFinalist/$', setFinalist, name="setFinalist"),   

#  	url(r'^teams/winner_selectEvent/$', winner_selectEvent, name="winner_selectEvent"),   
#  	url(r'^teams/winner_showTeams/$', winner_showTeams, name="winner_showTeams"),   
#  	url(r'^teams/setWinner/$', setWinner, name="setWinner"),   

]
