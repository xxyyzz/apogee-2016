from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse, JsonResponse
import string, random, os
from apogee16.settings import *


def website(request) :
	return render(request, "aic2016/index.html")
