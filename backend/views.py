from django.shortcuts import render
from backend.models import *
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from Event.models import Event, EventCategory

# Create your views here.
@csrf_exempt
def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				context = {
					'status' : 1,
					'firstname' : user.participant.name.split(' ', 1)[0],
				}
				return JsonResponse(context)
			else:
				context = {
					'status' : 0,
					'message' : 'Your account is frozen.'
				}
				return JsonResponse(context)
		else:
			context = {
				'status' : 0,
				'message' : 'Invalid username or password'
			}
			return JsonResponse(context)
	else:
		context = {
			'status' : 0,
			'message' : 'Invalid request format.'
		}
		return JsonResponse(context)

@csrf_exempt
def user_register(request):
	if request.POST:
		name = request.POST['name']
		gender = request.POST['gender']
		email_id = request.POST['email_id']
		college = request.POST['college']
		phone_one = int(request.POST['phone_one'])
		college = request.POST['college']

		try:
			model_college = College.objects.get(name=college)
		except:
			model_college = College.objects.create(name=college, is_displayed=False)

		response = {}
		registered_members = Participant.objects.all()
		registered_emails = [x.email_id for x in registered_members]
		if email_id in registered_emails: #check for already registered emails....no need to check if valid as we are using email field on fronted side
			member = Participant.objects.get(email_id=email_id)
			response['message'] = "This email has already been registered."
		else:
			member = Participant()
			member.name = name
			member.gender = gender
			member.email_id = email_id
			member.college = model_college
			member.phone_one = phone_one
			member.save()
			response['message'] = "Registration Successful!"
		token_url = email_generate_token(member)

		body = unicode(u'''
Hello %s !

You have successfully registered for APOGEE 16.

Just need to verify that this is your email address.
Gotta keep the internet safe from spambots and all that.
Is this you?

Please visit %s to verify your email.
We'll give you your login credentials there.
See ya!

Thanks,
Department of Visual Media
BITS Pilani
		''' ) % (member.name, token_url)
		send_to = member.email_id
		email = EmailMessage('Registration for APOGEE 16', body, 'noreply@bits-apogee.org', [send_to])
		email.send()
		response['status'] = 1
		response['message'] += "<br>An automated email has been sent to your registered email address.<br>Please confirm the activation link in the mail to continue."
		return JsonResponse(response)
	else:
		response = {}
		response['status'] = 0
		response['message'] = "No POST Data Received."
		return JsonResponse(response)

### Helper Functions
def email_generate_token(member):
	import uuid
	token = uuid.uuid4().hex
	registered_tokens = [participant.email_token for participant in Participant.objects.all()]
	while token in registered_tokens:
		token = uuid.uuid4().hex
	member.email_token = token
	member.save()
	token_url = 'http://bits-apogee.org/2016/api/verify/' + token + '/'
	return token_url
def email_authenticate_token(token):
	try:
		member = Participant.objects.get(email_token=token)
		member.email_verified = True
		member.email_token = None
		member.save()
		return member
	except ObjectDoesNotExist:
		return False
def generate_password(member):
    from xkcdpass import xkcd_password as xp
    wordfile = xp.locate_wordfile()
    mywords = xp.generate_wordlist(wordfile=wordfile, min_length=8, max_length=10)
    password = xp.generate_xkcdpassword(mywords, numwords=2, delimiter='').lower().translate(None, ' -_')
    return(password)
def create_user(member, password):
	name = str(member.name).lower()
	username = name.translate(None, ' ?.!/;:-_') + str(member.id)
	try:
		user = User.objects.get(email=member.email_id)
		user.set_password(password)
		user.save()
	except:
		user = User.objects.create_user(username=username, email=member.email_id, password=password)
	member.user = user
	member.save()
	return user
def mail_password(member, user, password):
	body = unicode(u'''
Hello %s !

Thanks for verifying your email.
Your login details are:
User ID: %s
Username: %s
Password: %s
Visit http://bits-apogee.org/ to login.

Thanks,
Department of Visual Media
BITS Pilani

P.S. The password is auto generated. We do not intend to offend you in any manner.
	''' ) % (member.name, member.id, user.username, password)
	send_to = member.email_id
	# try:
	email = EmailMessage('Registration for APOGEE 16', body, 'APOGEE, BITS Pilani', [send_to])
	# email.attach_file('/home/dvm/taruntest/oasisattach/Rules Booklet Oasis 2014.pdf')
	email.send()
### End helper functions

def email_confirm(request, token):
	member = email_authenticate_token(token)
	if member:
		password = generate_password(member)
		user = create_user(member, password)
		username = user.username
		mail_password(member, user, password)
		context = {
			'status' : 1,
			'username' : username,
			'password' : password,
		}
	else:
		context = {
			'status' : 0,
			'email' : "Invalid Token",
			'password' : "Invalid Token",
		}
	return render(request, 'main/email_verified.html', context)

def login_check(request):
	if request.user.is_authenticated():
		try:
			firstname = request.user.participant.name.split(' ', 1)[0],
		except ObjectDoesNotExist:
			firstname = None,
		context = {
			'status' : 1,
			'id' : request.user.participant.id if hasattr(request.user, 'participant') else None,
			'email' : request.user.email,
			'loggedin' : True,
			'firstname' : firstname,
			'name' : request.user.participant.name if hasattr(request.user, 'participant') else None,
		}
		return JsonResponse(context)
	else:
		context = {
			'status' : 0,
			'loggedin' : False,
		}
		return JsonResponse(context)

def email_check(request):
	context = {
		'email' : "No Such Token",
		'password' : "No Such Token",
	}
	return render(request, 'main/email_verified.html', context)

def user_logout(request):
	logout(request)
	return login_check(request)

def events_check(request):
	loggedin = request.user.is_authenticated()
	response = {
		'loggedin' : loggedin,
		'data' : [],
	}
	categories = EventCategory.objects.all()
	events = Event.objects.all()
	try:
		registered = True if event in request.user.participant.events.all() else False
	except:
		registered = False
	for category in categories:
		container = {}
		container['category'] = category.name
		container['events'] = []
		eventlist = {}
		for event in category.event_set.all():
			try:
				registered = True if event in request.user.participant.events.all() else False
			except:
				registered = False
			eventdata = {
					'id':event.id,
					'reg_enabled' : event.register,
					'registered' : registered,
					'team_event' : event.is_team,
					'max_members' : event.max_participants,
				}
			container['events'].append(eventdata)
		response['data'].append(container)
	return JsonResponse(response)


def register_single(request, eventid):
	event = Event.objects.get(id=eventid)
	participant = request.user.participant
	try:
		participant.events.add(event)
		participant.save()
		response = {
			'status' : 1,
			'message' : 'Successfully Registered!'
		}
	except:
		response = {
			'status' : 0,
			'message' : 'Registration Failed!'
		}
	return JsonResponse(response)

def register_team(request, eventid):
	# try:
	data = request.POST
	memberids = data.getlist('memberid')
	name = data['name']
	event = Event.objects.get(id=eventid)
	leader = request.user.participant
	team = Team.objects.create(name=name, event=event, leader=leader)
	team.name = name
	team.leader = leader
	team.save()
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

def participant_summary(request, participantid):
	try:
		participant = Participant.objects.get(id=participantid)
		response = {
			'name' : participant.name,
			'id' : participant.id,
			'college': participant.college.name,
			'status' : 1,
		}
	except:
		response = {
			'status' : 0,
			'message' : 'No such participant',
		}
	return JsonResponse(response)

