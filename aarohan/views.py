from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse, JsonResponse
import string, random, os
from apogee16.settings import *


def website(request) :
	return render(request, "aarohan/index.html")

def soft09(request) :
	return render(request, "aarohan/soft09.html")

def soft10(request) :
	return render(request, "aarohan/soft10.html")

def soft11(request) :
	return render(request, "aarohan/soft11.html")

def soft12(request) :
	return render(request, "aarohan/soft12.html")