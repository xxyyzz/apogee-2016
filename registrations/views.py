from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from registrations.models import *
from django.template import Context
from django.http import HttpResponse, JsonResponse
from registrations.models import *
import string, random, os
from apogee16.settings import *
from django.template.defaultfilters import slugify


def home(request) :
	return render(request, "portal/index.html")

def papersInstructions(request) :
	return render(request, "portal/partials/papers_main.html")

def papersForm(request) :
	context = {};
	a = Category.objects.filter(model__in= {'Paper', 'Both'})
	context['categories'] = list(a)
	return render(request, "portal/partials/papers_form.html",context)

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

def projectsStatus(request) : 
	return HttpResponse("h1 !")

def checkForm(request) :
	return render(request, "portal/partials/check_form.html")

def checkStatus(request) :
	data = request.POST
	return render(request, "portal/check_status.html")


# Create your views here.
