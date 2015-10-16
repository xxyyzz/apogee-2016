from django.shortcuts import get_object_or_404, render_to_response, redirect
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
	assoc = data['association']
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
	model_assoc = Association.objects.get(name=assoc)

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
				response['title'] = entry.name
				response['category'] = entry.category.name
				response['stub'] = entry.stub
				response['address'] = entry.address
				response['author'] = {}
				response['author']['name'] = entry.author.name
				response['author']['phone'] = entry.author.phone
				response['author']['email'] = entry.author.email
				response['author']['college'] = entry.author.college.name
				response['co-author'] = {}
				response['abstract'] = entry.abstract.file
				if entry.co_author != None :
					response['co-author']['name'] = entry.co_author.name
					response['co-author']['phone'] = entry.co_author.phone
					response['co-author']['email'] = entry.co_author.email
					response['co-author']['college'] = entry.co_author.college
				
				return render(request, "portal/partials/check_result_paper.html", response)

			except :
				print 'invalid ref'

		elif cat == 'project' :
			entry = Project.objects.get(stub=ref)
			try : 
				response['title'] = entry.name
				response['category'] = entry.category.name
				response['stub'] = entry.stub
				response['assoc'] = entry.assoc.name
				response['abstract'] = entry.abstract.file
				response['tl'] = {}
				response['tl']['name'] = entry.leader.name
				response['tl']['phone'] = entry.leader.phone
				response['tl']['email'] = entry.leader.email
				response['tl']['college'] = entry.leader.college.name
				response['members'] = []

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
				print 'invalid ref'

	except : 
		print 'quit'
		response["status"] = 0
		response["text"] = "Invalid Input"

	#return HttpResponse(request.POST)


def campusAmbassadorMain(request) : 
	return render(request, "portal/campusAmbassadorMain.html")

def campusAmbassadorForm(request) : 
	return render(request, "portal/campusAmbassadorForm.html")


# Create your views here.
