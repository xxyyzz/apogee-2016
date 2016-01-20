from django.shortcuts import render
from backend.models import *
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@csrf_exempt
def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
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
		# city = request.POST['city']
		email_id = request.POST['email_id']
		college = request.POST['college']
		phone_one = int(request.POST['phone_one'])
		# phone_two = request.POST['phone_two']
		# social_link = request.POST['social_link']
		# events = request.POST.getlist('events[]')
		try:
			# city = request.POST['city']
			college = request.POST['college']
		except :
			response = {}
			response['status'] = 0
			response['message'] = "Enter a valid college. Please Refresh the page to enter valid details"
			return JsonResponse(response)

		# try :
		# 	phone_two = int(phone_two)
		# except :
		# 	phone_two = None

		try:
			model_college = College.objects.get(name=college)
		except:
			model_college = College.objects.create(name=college, is_displayed=False)

		registered_members = Participant.objects.all()
		registered_emails = [x.email_id for x in registered_members]
		if email_id in registered_emails: #check for already registered emails....no need to check if valid as we are using email field on fronted side
			response = {}
			response['status'] = 0
			response['message'] = "This email is already registered! Please Refresh the page to register with another email."
			return JsonResponse(response)
		member = Participant()
		member.name = name
		member.gender = gender
		# member.city = city
		member.email_id = email_id
		member.college = model_college
		member.phone_one = phone_one
		# member.phone_two = phone_two
		# member.social_link = social_link
		member.save()
		token_url = email_generate_token(member)

		body = unicode(u'''
Hello %s !

You have been successfully registered for APOGEE 16.
To continue, please visit %s to verify your email.

Thanks,
The Department of Visual Media
BITS Pilani
		''' ) % (name, token_url)
		send_to = email_id
		# try:
		email = EmailMessage('Registration for APOGEE 16', body, 'noreply@bits-apogee.org', [send_to])
		# email.attach_file('/home/dvm/taruntest/oasisattach/Rules Booklet Oasis 2014.pdf')
		email.send()
		# except:
		# 	return HttpResponse('error')
		# 	pass
		status = {}
		status['status'] = 1
		status['message'] = "Successfully Registered!"
		return JsonResponse(status)
	else:
		status = {}
		status['status'] = 0
		status['message'] = "No POST Data 	Received."
		return JsonResponse(status)

def email_generate_token(member):
	import uuid
	token = uuid.uuid4().hex
	registered_tokens = [member.email_token for member in Participant.objects.all()]
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
	user = User.objects.create_user(member.email_id, member.email_id, password)
	member.user = user
	member.save()
	return user
def mail_password(member, password):
	body = unicode(u'''
Hello %s !

Thanks for verifying your email.
Your login details are:
Username: %s
Password: %s
Visit http://bits-apogee.org/ to login.

Thanks,
The Department of Visual Media
BITS Pilani

P.S. The password is auto generated. We do not intend to offend you in any manner.
	''' ) % (member.name, member.email_id, password)
	send_to = member.email_id
	# try:
	email = EmailMessage('Registration for APOGEE 16', body, 'APOGEE, BITS Pilani', [send_to])
	# email.attach_file('/home/dvm/taruntest/oasisattach/Rules Booklet Oasis 2014.pdf')
	email.send()
def email_confirm(request, token):
	member = email_authenticate_token(token)
	if member:
		password = generate_password(member)
		user = create_user(member, password)
		email = user.email
		mail_password(member, password)
		context = {
			'email' : email,
			'password' : password,
		}
	else:
		context = {
			'email' : "No Such Token",
			'password' : "No Such Token",
		}
	return render(request, 'main/email_verified.html', context)

def login_check(request):
	if request.user.is_active:
		try:
			firstname = request.user.participant.name.split(' ', 1)[0],
		except ObjectDoesNotExist:
			firstname = None,
		context = {
			'status' : 1,
			'email' : request.user.email,
			'loggedin' : True,
			'firstname' : firstname,
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
