from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from registrations.models import *
from django.template import Context
from django.http import HttpResponse, JsonResponse
from registrations.models import *
import string, random, os
from apogee16.settings import *
from django.template.defaultfilters import slugify
from django.utils.datastructures import MultiValueDictKeyError
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


def renderUpdates(request) :
	return render(request, "portal/partials/updates.html")

def home(request) :
	return render(request, "portal/index.html")

def papersInstructions(request) :
	return render(request, "portal/partials/papers_main.html")

def papersForm(request) :
	context = {};
	a = Category.objects.filter(model__in= {'Paper', 'Both'})
	context['categories'] = list(a)
	return render(request, "portal/partials/papers_form.html",context)

@csrf_exempt
def papersStatus(request) :
	data = request.POST
	paper_name = data['paper-name']
	category = data['category']
	author_name = data['author-name']
	author_phone = data['author-phone']
	author_email = data['author-email']
	author_address = data['author-address']
	college = data['college']
	co_author_name = data['co-author-name']
	co_author_phone = data['co-author-phone']
	co_author_email = data['co-author-email']
	abstract = request.FILES['0']

	try:
		model_college = College.objects.get(name=college)
	except:
		model_college = College.objects.create(name=college)

	try:
		model_author = Participant.objects.get(email=author_email)
	except:
		model_author = Participant.objects.create(name=author_name, phone=author_phone, email=author_email, college=model_college)

	model_category = Category.objects.get(name=category)

	if co_author_name != "":
		try:
			model_co_author = Participant.objects.get(email=co_author_email)
		except:
			model_co_author = Participant.objects.create(name=co_author_name, phone=co_author_phone, email=co_author_email, college=model_college)
	else:
		model_co_author = None

	model_stub = stubGenerator()
	abstract.name = model_stub + '.pdf'

	slugified_category = slugify(category)
	category_directory = os.path.join(MEDIA_ROOT, 'papers/', slugified_category)
	if not os.path.exists(category_directory):
		os.makedirs(category_directory)

	Paper.objects.create(name=paper_name, address=author_address, author=model_author, co_author=model_co_author, category=model_category, stub=model_stub, abstract=abstract)

	response = {}
	response['status'] = 1
	response['stub'] = model_stub
	response['type'] = 'Project'

	return render(request, "portal/partials/papers_status.html", response)


def stubGenerator(size=8, chars=string.ascii_uppercase + string.digits):
		stub = ''.join(random.choice(chars) for _ in range(size))
		try:
			Project.objects.get(stub=stub)
		except:
			try:
				Paper.objects.get(stub=stub)
			except:
				return stub


def projectsInstructions(request) :
	return render(request, "portal/partials/projects_main.html")


def projectsForm(request) :
	context = {};
	a = Category.objects.filter(model__in= {'Project', 'Both'})
	context['categories'] = list(a)
	b = Association.objects.all()
	context['assocs'] = list(b)
	return render(request, "portal/partials/projects_form.html", context)


@csrf_exempt
def projectsStatus(request) :
	data = request.POST
	project_name = data['project-name']
	tl_name = data['tl-name']
	tl_phone = data['tl-phone']
	tl_email = data['tl-email']
	member = {}
	for x in range(1,6):
		member[x] = {}
		try:
			key = 'mem-%s-name' % x
			member[x]['name'] = data[key]
		except MultiValueDictKeyError:
			member[x]['name'] = None
		try:
			key = 'mem-%s-phone' % x
			member[x]['phone'] = data[key]
		except MultiValueDictKeyError:
			member[x]['phone'] = None
		try:
			key = 'mem-%s-email' % x
			member[x]['email'] = data[key]
		except MultiValueDictKeyError:
			member[x]['email'] = None


	# return HttpResponse(member[3]['email'])

	college = data['college']
	category = data['category']
	try:
		assoc = data['association']
	except:
		assoc = None
	abstract = request.FILES['0']


	try:
		model_college = College.objects.get(name=college)
	except:
		model_college = College.objects.create(name=college)

	try:
		model_leader = Participant.objects.get(email=tl_email)
	except:
		model_leader = Participant.objects.create(name=tl_name, phone=tl_phone, email=tl_email, college=model_college)

	model_category = Category.objects.get(name=category)
	try:
		model_assoc = Association.objects.get(name=assoc)
	except:
		model_assoc = None

	model_member = {}
	for x in range(1,6):
		if member[x]['email'] != None:
			try:
				model_member[x] = Participant.objects.get(email=member[x]['email'])
			except:
				model_member[x] = Participant.objects.create(name=member[x]['name'], phone=member[x]['phone'], email=member[x]['email'], college=model_college)
		else:
			model_member[x] = None

	model_stub = stubGenerator()
	abstract.name = model_stub + '.pdf'


	slugified_category = slugify(category)
	category_directory = os.path.join(MEDIA_ROOT, 'projects/', slugified_category)
	if not os.path.exists(category_directory):
		os.makedirs(category_directory)

	model_project = Project.objects.create(name=project_name, leader=model_leader, category=model_category, stub=model_stub, abstract=abstract, assoc=model_assoc)

	for x in range(1,6):
		if model_member[x] != None:
			model_project.members.add(model_member[x])
	model_project.save()

	response = {}
	response['status'] = 1
	response['stub'] = model_stub
	response['type'] = 'Project'

	return render(request, "portal/partials/projects_status.html", response)


def checkForm(request) :
	return render(request, "portal/partials/check_form.html")


@csrf_exempt
def checkStatus(request) :
	data = request.POST
	response = {}
	try :
		ref = data['ref']
		cat = data['cat']
		if cat == 'paper' :
			entry = Paper.objects.get(stub=ref)
			try :
				response['status'] = 1
				response['title'] = entry.name
				response['category'] = entry.category.name
				response['stub'] = entry.stub
				response['address'] = entry.address
				response['author'] = {}
				response['author']['name'] = entry.author.name
				response['author']['phone'] = entry.author.phone
				response['author']['email'] = entry.author.email
				response['author']['college'] = entry.author.college.name
				response['coauthor'] = {}
				response['round'] = entry.status
				#response['abstract'] = entry.abstract.file
				if entry.co_author != None :
					response['coauthor']['name'] = entry.co_author.name
					response['coauthor']['phone'] = entry.co_author.phone
					response['coauthor']['email'] = entry.co_author.email
					response['coauthor']['college'] = entry.co_author.college

				return render(request, "portal/partials/check_result_paper.html", response)

			except :
				response['status'] = 0
				return render(request, "portal/partials/check_result_paper.html", response)

		elif cat == 'project' :
			entry = Project.objects.get(stub=ref)
			try :
				response['status'] = 1
				response['title'] = entry.name
				response['category'] = entry.category.name
				response['stub'] = entry.stub
				response['assoc'] = entry.assoc.name
				#response['abstract'] = entry.abstract.file
				response['tl'] = {}
				response['tl']['name'] = entry.leader.name
				response['tl']['phone'] = entry.leader.phone
				response['tl']['email'] = entry.leader.email
				response['tl']['college'] = entry.leader.college.name
				response['members'] = []
				response['round'] = entry.status

				cursor = entry.members.all()

				for member in cursor :
					mem = {};
					mem['name'] = member.name
					mem['phone'] = member.phone
					mem['email'] = member.email
					mem['college'] = member.college.name
					response['members'].append(mem)

				return render(request, "portal/partials/check_result_project.html", response)

			except :
				response['status'] = 0
				return render(request, "portal/partials/check_result_project.html", response)


	except :
		print ('quit')
		response["status"] = 0
		response["text"] = "Invalid Input"
		return render(request, "portal/partials/check_result_project.html", response)




# CAMPUS AMBASSADOR VIEWS


def campusAmbassadorMain(request) :
	return render(request, "portal/campusAmbassadorMain.html")

@csrf_exempt
def campusAmbassadorStatus(request):
	data = request.POST
	name = data['fname']
	address = data['address']
	college = data['college']
	year = data['year']
	degree = data['degree']
	email = data['email']
	phone = data['phone']
	ambassador_quality = data['desc']
	root_mail = data['rmail']
	if root_mail == 0:
		root_mail = False
	elif root_mail == 1:
		root_mail = True

	try:
		model_college = College.objects.get(name=college)
	except:
		model_college = College.objects.create(name=college)

	response = {}

	try:
		CampusAmbassador.objects.create(name=name, address=address, college=model_college, year=year, degree=degree, email=email, phone=phone, ambassador_quality=ambassador_quality, root_mail=root_mail)
		response['status'] = 1


		body = """Dear Applicant,
Greetings from the Department for Publications and Correspondence -APOGEE, BITS Pilani. We are pleased to inform you that your registration for the Campus Ambassador Programme for APOGEE 2016 has been confirmed.

Please make sure you go through the following guidelines for better understanding of the programme:

i) Registration Guideline (Make sure you have completed these steps)
   a) Visit www.youth4work.com and register yourself (with the same email and phone number)
   b) Visit www.facebook.com/bitsapogee, like and follow the page for future updates


ii) Selection Procedure
   a) Selection will be carried out on a one-one telephonic conversation basis which will be held in last week of December or early January.
   b) Judgement will be based on your oratory skills, knowledge about APOGEE and your commitment to the Campus Ambassador Program.
   c) You will be informed about your selection on a later date via email.

iii) Post Selection Tasks
    a) If you are selected, you automatically get registered as a marketing intern with youth4work, working for APOGEE 2016.
    b) You will be working with a member from the organizing team who will assign you tasks and keep helping you out with various issues you may face during marketing and publicity of APOGEE in your institute.
    c) The final performance of the intern will be judged by how many people he/she can get for APOGEE-2016 from 25th Feb-28th          Feb,2016.

Please note that failing to meet the dedication required for a successful internship without righteous reasons can lead to cancellation of your internship anytime till APOGEE 2016.

You will be contacted shortly by our representatives for the telephonic conversation.

Thank you."""
		send_to = [str(email) ]
		# try:
		email = EmailMessage("Campus Ambassador Apogee 2016", body, 'noreply@bits-apogee.org', send_to)
			#poster attachment
			# email.attach_file('/home/dvm/oasis/oasis2015/attachments/Oasis 2015 Communique.docx')
			#email.attach_file('/home/dvm/taruntest/oasisattach/Oasis 2014 Posters.pdf')
			#email.attach_file('/home/dvm/taruntest/oasisattach/Rules Booklet Oasis 2014.pdf')
		email.send()
		# except:
		# response['status'] = 0
		# response['message'] = "Error"

	except IntegrityError:
		response['status'] = 0
		response['message'] = "Email already exists!"


	# return render(request, "portal/partials/projects_status.html", response)
	return JsonResponse(response)

@csrf_exempt
def add_initial_registration(request):
	data = request.POST
	name = data['pname']
	email = data['email']
	phone = data['phone']
	response = {}
	try:
		InitialRegistration.objects.create(name=name, email=email, phone=phone)
		response['status']=1

	except IntegrityError:
		response['status'] = 0
		response['message'] = "Email already exists!"

	return JsonResponse(response)

@csrf_exempt
def edit_paper(request):
	data = request.POST
	stub = data['ref']
	paper = request.FILES['0']
	paper.name = model_stub + '.pdf'
	entry = Paper.objects.get(stub=stub)
	entry.paper = paper
	entry.save()
	slugified_category = slugify(entry.category)
	category_directory = os.path.join(MEDIA_ROOT, 'papers-final/', slugified_category)
	if not os.path.exists(category_directory):
		os.makedirs(category_directory)
	response = {
		"paper" : entry,
	}
	return render(request, "portal/partials/check_edit_paper.html", response)


def edit_project(request):
	data = request.POST
	stub = data['ref']
	member = {}
	for x in range(1,6):
		member[x] = {}
		try:
			key = 'mem-%s-name' % x
			member[x]['name'] = data[key]
		except MultiValueDictKeyError:
			member[x]['name'] = None
		try:
			key = 'mem-%s-phone' % x
			member[x]['phone'] = data[key]
		except MultiValueDictKeyError:
			member[x]['phone'] = None
		try:
			key = 'mem-%s-email' % x
			member[x]['email'] = data[key]
		except MultiValueDictKeyError:
			member[x]['email'] = None
	entry = Project.objects.get(stub=stub)
	entry.members.clear()
	model_member = {}
	for x in range(1,6):
		if member[x]['email'] != None:
			try:
				model_member[x] = Participant.objects.get(email=member[x]['email'])
			except:
				model_member[x] = Participant.objects.create(name=member[x]['name'], phone=member[x]['phone'], email=member[x]['email'], college=model_college)
		else:
			model_member[x] = None
	for x in range(1,6):
		if model_member[x] != None:
			entry.members.add(model_member[x])
	entry.save()
	response = {
		"project" : entry,
	}
	return render(request, "portal/partials/check_edit_project.html", response)
