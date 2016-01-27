from backend.utilities import staff_check
from django.views.decorators.http import require_POST
from backend.models import *
from Event.models import *
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
import hmac
import hashlib

@staff_check
def summary(request):
	staff_check(request)
	user = request.user
	member = request.user.participant
	if member.email_verified:
		response = {
			'status' : 1,
			'id' : member.id,
			'aadhaar' : member.aadhaar,
			'name' : member.name,
			'gender' : member.gender,
			'college' : member.college.name,
			'city' : member.city,
			'phone' : member.phone_one,
			'alt_phone' : member.phone_two,
			'email' : member.email_id,
			'email_verified' : member.email_verified,
			'social_link' : member.social_link,
			'single_events' : [
				{
					'name' : event.name,
					'id' : event.id,
				}
				for event in member.events.filter(is_team=False)
			],
			'team_events' : [
			{
				'event_id' : team.event.id,
				'event_name' : team.event.name,
				'event_max_members' : team.event.max_participants,
				'team_id' : team.id,
				'team_name' : team.name,
				'team_leader' : {
					'id' : team.leader.id,
					'name' : team.leader.name,
				},
				'team_members' : [
					{
						'id' : member.id,
						'name' : member.name,
					}
						for member in team.members.all()
				]
			}
				for team in member.team_set.all()
			],
			'fee_paid' : member.fee_paid,
			'teams' : [team.name for team in member.teams.all()],
			'address' : member.address,
			'bank_ifsc' : member.bank_ifsc,
			'bank_account_no' : member.bank_account_no,
			'bank_name' : member.bank_name,
			'pcr_approval' : member.pcr_approval,
		}
	else:
		response = {
			'status' : 0,
			'message' : 'Please verify your email to access this section'
		}
	return JsonResponse(response)

@staff_check
@require_POST
def unregister_single(request, eventid):
	try:
		event = Event.objects.get(id=eventid)
		member = request.user.participant
		member.events.remove(event)
		member.save()
		response = {
			'status' : 1,
		}
		return JsonResponse(response)
	except:
		response = {
			'status' : 0,
		}
		return JsonResponse(response)

@staff_check
@require_POST
def unregister_team(request, teamid):
	try:
		team = Team.objects.get(id=teamid)
		member = request.user.participant
		team.members.remove(member)
		team.save()
		member.events.remove(team.event)
		member.save()
		response = {
			'status' : 1,
		}
		return JsonResponse(response)
	except:
		response = {
			'status' : 0,
		}
		return JsonResponse(response)

@staff_check
@require_POST
def update_team(request, teamid):
	# try:
	data = request.POST
	memberids = data.getlist('memberid')
	name = data['name']
	event = Event.objects.get(id=eventid)
	# leader = request.user.participant
	team = Team.objects.get(id=teamid)
	team.name = name
	team.save()
	teaam.members.clear()
	# team.leader = leader
	response = {
		'status' : 1,
		'message' : 'Team ' + name + ' successfully registered.',
		'added' : [],
		'not_added' : [],
	}
	for memberid in memberids:
		try:
			member = Participant.objects.get(id=memberid)
			member.events.add(event)
			member.save()
			team.members.add(member)
			team.save()
			response['added'].append(member.name)
		except:
			response['not_added'].append(memberid)
	# except:
	# 	response = {
	# 		'status' : 0,
	# 		'message' : 'Whoopsie! Looks like an error occured. Please try again later.'
	# 	}
	return JsonResponse(response)

@staff_check
@require_POST
def delete_team(request, teamid):
	try:
		team = Team.objects.get(id=teamid)
		for member in team.members.all():
			member.events.remove(team.event)
		team.leader.events.remove(team.event)
		team.delete()
		response = {
			'status' : 1,
		}
		return JsonResponse(response)
	except:
		response = {
			'status' : 1,
		}
		return JsonResponse(response)

@staff_check
@require_POST
def update_profile(request):
	data = request.POST
	# city = data['city'] if 'city' in data else None
	member = request.user.participant
	member.bank_ifsc = data['bank_ifsc']
	member.address = data['address']
	member.bank_account_no = data['bank_account_no']
	member.bank_name = data['bank_name']
	member.save()
	response = {
		'status' : 1,
	}
	return JsonResponse(response)

@staff_check
def instamojo_payment(request):
	part_ob = request.user.participant
	if part_ob.email_verified:
		pid = part_ob.id
		salt='3688fa4859dd4812882c001d951fcae6'
		message = str(pid)
		mac_calculated = hmac.new(
     		str(salt),
    		message,
    		hashlib.sha1,
    		).hexdigest()
	#b = 'https://www.instamojo.com/bitsoasis/registration-ticket/'+'?intent=buy&data_Field_88249='+names+'&data_amount='+str(a*250)+'&data_readonly=data_amount&data_readonly=data_Field_88249&data_sign='+mac_calculated
		instalink = 'https://www.instamojo.com/bitsapogee/apogee-registration-fee/'+'?data_Field_94287='+message+'&data_readonly=data_Field_94287&data_sign='+mac_calculated
		return HttpResponseRedirect(instalink)


@staff_check
def apirequest_fee(request):
	import requests
	#payid=str(request.GET['payment_id'] )
	headers = {'X-Api-Key': '58430d59e907bd9061be3f38597757d6',
    	       'X-Auth-Token': '1fed57f6ea0de2abac9b85508fcdc4c1'}
	r = requests.get('https://www.instamojo.com/api/1.1/payments/',
                	 headers=headers)
	json_ob = r.json()
	# dec_json = json.loads(json_ob)
	payments = json_ob['payments'][0]
	custom_fields_ = payments['custom_fields']
	linktitle = payments['link_title']
	paymentid = payments['payment_id']
	field2 = custom_fields_['Field_94287']
	pid = field2['value']
	part = Participant.objects.get(id = int(pid))
	part.fee_paid=True
	part.save()

	#name= payments['buyer_name'  ]
	#kunal='kunal sharma'
	response={
	#'name':name,
	#'kunal':kunal,
	'paymentid' :paymentid,
	'linktitle' : linktitle,
	'status':1,
	}
	return JsonResponse(response)
