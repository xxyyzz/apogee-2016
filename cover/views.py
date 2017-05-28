from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse, JsonResponse
import string, random, os
from apogee16.settings import *
from django.views.decorators.csrf import ensure_csrf_cookie


def preIntro(request) :
	return render(request, "pre/index.html")

def intro(request) :
	return render(request, "intro/index.html")

def spons(request):
	return render(request,"main/sponsors.html")

def wallpaper(request) :
	return render(request, "main/wallpaper.html")

@ensure_csrf_cookie
def main(request) :
	return render(request, "main/index.html")
