from django.shortcuts import render
from backend.models import *
from django.http import JsonResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@csrf_exempt
def register(request):
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
			College.objects.get(name=college)
		except:
			College.objects.create(name=college, is_displayed=False)

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
		member.college = college
		member.phone_one = phone_one
		# member.phone_two = phone_two
		# member.social_link = social_link
		member.save()

		body = unicode(u'''

		''' )
		# send_to = email_id
		# try:
		# 	email = EmailMessage('Application for BITS Oasis 2015', body, 'invitation@bits-oasis.org', [send_to])
			#poster attachment
			# email.attach_file('/home/dvm/oasis/oasis2015/attachments/Oasis 2015 Communique.docx')
			#email.attach_file('/home/dvm/taruntest/oasisattach/Oasis 2014 Posters.pdf')
			#email.attach_file('/home/dvm/taruntest/oasisattach/Rules Booklet Oasis 2014.pdf')
			# email.send()
		# except:
		# 	return HttpResponse('error')
			# pass
		status = {}
		status['status'] = 1
		status['message'] = "Successfully Registered!"
		return JsonResponse(status)
	else:
		status = {}
		status['status'] = 0
		status['message'] = "No POST Data Received."

def email_generate_token(member):
	import uuid
	token = uuid.uuid4().hex
	member.email_token = token
	member.save()
def email_confirm(request, token):
	try:
		member = Participant.objects.get(email_token=token)
		member.email_verified = True
		member.save()
		return HttpResponse("Email Verified")
	except ObjectDoesNotExist:
		return HttpResponse("No such token")
