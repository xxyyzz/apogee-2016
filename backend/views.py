from django.shortcuts import render
from backend.models import *
from django.http import JsonResponse
from django.shortcuts import render, render_to_response, redirect

# Create your views here.


def register(request):
	if request.POST:
		name = request.POST['userName']
		gender = request.POST['userGender']
		if gender == "male":
			gender = 'M'
		elif gender == "female":
			gender = 'F'
		city = request.POST['userLocation']
		email_id = request.POST['userEmail']
		college = request.POST['userSchool']
		phone_one = int(request.POST['userPhone'])
		phone_two = request.POST['userPhoneAlt']
		social_link = request.POST['link']
		# events = request.POST.getlist('events[]')
		try:
			city = request.POST['userLocation']
			college = request.POST['userSchool']
		except :
			response = {}
			response['status'] = 0
			response['message'] = "Enter a valid city and college. Please Refresh the page to enter valid details"
			return JsonResponse(response)

		try :
			phone_two = int(phone_two)
		except :
			phone_two = None

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
		member.city = city
		member.email_id = email_id
		member.college = college
		member.phone_one = phone_one
		member.phone_two = phone_two
		member.social_link = social_link
		member.save()
		for key in events:
			event = Event.objects.get(pk=key)
			member.events.add(event)

		# try:
		# 	college_rep = UserProfile.objects.get(details__college=college)
		# except:
		# 	member.college_rep = None
		# else:
		# 	member.college_rep = college_rep
		member.save()

		# if member.college_rep == None:
		# 	crdetails = "Your college representative has not been assigned. We will contact you to take up the post."
		# elif member.college_rep != None:
		# 	rep = member.college_rep.details
		# 	if rep.phone_two != None:
		# 		phone = str(rep.phone_one) + ", " + str(rep.phone_two)
		# 	elif rep.phone_two == None:
		# 		phone = str(rep.phone_one)
		# 	crdetails = """
		# 	Name: %s,
		# 	College: %s,
		# 	Email: %s,
		# 	Phone: %s,
		# 	""" % (rep.name, rep.college, rep.email_id, phone)

		body = unicode(u'''
For centuries now, the sands of the quaint hamlet of Pilani have lured many-a-traveller into their unyielding clutches, and once you experience it, so will Oasis. ­­In its 45th edition, the cultural fest of BITS Pilani has risen from the whim of a pile of sand to one of the biggest college gatherings in the country. For the un-worshipping youth, Oasis is our religion. Come celebrate it with us.

It gives us, the students of BITS Pilani, great pleasure to welcome you to take part in our annual cultural festival Oasis ’15-Around the World in 96 Hours, which is going to be held from 28th October to 1st November 2015.

To apply for participation, click http://bits-oasis.org/2015/participate/ if you haven't already. Read on to understand the application procedure.

Get ready to take the journey of a lifetime, with the theme 'Around The World In 96 Hours', and who knows, you may very well reach your destination, or better still, forget about it. With a myriad of events from Rocktaves to Oasis Quiz and performances by artists of worldwide renown, the fest promises to be bigger, better and much more memorable this time around.

Peruse the Oasis ’15 Rules Booklet, http://bits-oasis.org/2015/details/ for a comprehensive definition of all the events we have in store for you.

Visit our engaging website http://bits-oasis.org/ and follow us on Facebook http://facebook.com/oasis.bitspilani for regular updates.

Looking forward to seeing you at Oasis ’15.


Your college representative details: %s
		''' ) % crdetails
		send_to = email_id
		try:
			email = EmailMessage('Application for BITS Oasis 2015', body, 'invitation@bits-oasis.org', [send_to])
			#poster attachment
			# email.attach_file('/home/dvm/oasis/oasis2015/attachments/Oasis 2015 Communique.docx')
			#email.attach_file('/home/dvm/taruntest/oasisattach/Oasis 2014 Posters.pdf')
			#email.attach_file('/home/dvm/taruntest/oasisattach/Rules Booklet Oasis 2014.pdf')
			email.send()
		except:
			return HttpResponse('error')
			# pass
		status = {}
		status['status'] = 1
		status['message'] = "Successfully Registered!"
		if member.college_rep != None:
			rep = member.college_rep.details
			status['collegerep'] = 1
			status['name'] = rep.name
			status['college'] = rep.college
			if rep.phone_two != None:
				status['phone'] = str(rep.phone_one) + ", " + str(rep.phone_two)
			elif rep.phone_two == None:
				status['phone'] = str(rep.phone_one)
			status['email'] = rep.email_id
		elif member.college_rep == None:
			status['collegerep'] = 0
		return JsonResponse(status)
	# return render(request, 'initialregistration.html')
	return HttpResponseRedirect('/register.html')
