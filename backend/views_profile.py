from backend.utilities import staff_check
from django.http import JsonResponse

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
				'id' : event.id,
				'name' : event.name,
				'details' : [
					{
						'id' : team.id,
						'name' : team.name,
						'leader' : {
							'id' : team.leader.id,
							'name' : team.leader.name,
						},
						'members' : [
							{
								'id' : member.id,
								'name' : member.name,
							}
								for member in team.members.all()
						]
					}
						for team in member.team_set.filter(event=event)
				]
			}
				for event in member.events.filter(is_team=True)
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

# @staff_check
# def delete_event(request):
# 	member = request.user.participant
# 	member.events.
