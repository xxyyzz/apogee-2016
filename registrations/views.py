from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from registrations.models import *
from django.template import Context
from django.http import HttpResponse

def home(request) :
	return render(request, "portal/index.html")

def papersInstructions(request) :
	return render(request, "portal/partials/papers_main.html")

def papersForm(request) :
	return render(request, "portal/papers_form.html")

def projectsInstructions(request) :
	return render(request, "portal/partials/projects_main.html")

def projectsForm(request) :
	return render(request, "portal/projects_form.html")


# Create your views here.
