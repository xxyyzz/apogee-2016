from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from registrations.models import *
from django.template import Context
from django.http import HttpResponse

def home(request) :
	return render(request, "portal/index.html")

# Create your views here.
