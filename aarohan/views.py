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

def results(request):
	if request.POST:
		roll_no= int(request.POST['roll_no'])
		try:
			res_ob= Results.objects.get(roll_no=roll_no)
		except:
			return HttpResponse('Error: Not Found')
		return render(request,'../../pcradmin/templates/pcradmin/res_details.html',{'res':res_ob})
	return render(request,'../../pcradmin/templates/pcradmin/aarohan_results.html')
