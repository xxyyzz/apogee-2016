from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from registrations.models import *
from django.template import Context
from django.http import HttpResponse
from registrations.models import *

def home(request) :
	return render(request, "portal/index.html")

def papersInstructions(request) :
	return render(request, "portal/partials/papers_main.html")

def papersForm(request) :
	context = {};
	a = Category.objects.filter(model__in= {'Paper', 'Both'})
	context['categories'] = list(a)
	return render(request, "portal/partials/papers_form.html",context)

def projectsInstructions(request) :
	return render(request, "portal/partials/projects_main.html")

def projectsForm(request) :
	context = {};
	a = Category.objects.filter(model__in= {'Project', 'Both'})
	context['categories'] = list(a)
	b = Association.objects.all()
	context['assocs'] = list(b)
	return render(request, "portal/partials/projects_form.html", context)

def checkForm(request) :
	return render(request, "portal/partials/check_form.html")

def checkStatus(request) :
	return render(request, "portal/check_status.html")


# Create your views here.
