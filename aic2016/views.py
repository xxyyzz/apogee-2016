from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse, JsonResponse
import string, random, os
from apogee16.settings import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from aic2016.models import *
from django.template.defaultfilters import slugify


def website(request) :
	return render(request, "aic2016/index.html")

@csrf_exempt
def problemstatement_add(request) :
	data = request.POST
	gl_name = data['gl_name']
	gl_phone = data['gl_phone']
	gl_email = data['gl_email']
	gl_college = data['gl_college']
	gl_yos = data['gl_yos']

	member = {}
	for x in range(1,4):
		member[x] = {}
		try:
			key = 'mem-%s-name' % x
			member[x]['name'] = data[key]
		except KeyError:
			member[x]['name'] = None
		try:
			key = 'mem-%s-email' % x
			member[x]['email'] = data[key]
		except KeyError:
			member[x]['phone'] = None
		try:
			key = 'mem-%s-phone' % x
			member[x]['phone'] = data[key]
		except KeyError:
			member[x]['email'] = None
		try:
			key = 'mem-%s-college' % x
			member[x]['college'] = data[key]
		except KeyError:
			member[x]['college'] = None
		try:
			key = 'mem-%s-yos' % x
			member[x]['yos'] = data[key]
		except KeyError:
			member[x]['yos'] = None

	# return HttpResponse(member[3]['email'])

	# college = data['college']
	# category = data['category']
	# try:
	# 	assoc = data['association']
	# except:
	# 	assoc = None
	problem_statement = data['problem_statement']
	solution = request.FILES['0']


	try:
		model_leader = Participant.objects.get(email=gl_email)
	except:
		model_leader = Participant.objects.create(name=gl_name, phone=gl_phone, email=gl_email, college=gl_college, yos=gl_yos)

	# model_category = Category.objects.get(name=category)
	# try:
	# 	model_assoc = Association.objects.get(name=assoc)
	# except:
	# 	model_assoc = None

	model_member = {}
	for x in range(1,4):
		if member[x]['email'] != None:
			try:
				model_member[x] = Participant.objects.get(email=member[x]['email'])
			except:
				model_member[x] = Participant.objects.create(name=member[x]['name'], phone=member[x]['phone'], email=member[x]['email'], college=member[x]['college'], yos=member[x]['yos'])
		else:
			model_member[x] = None

	solution.name = slugify(str(model_leader.id)+'-'+gl_college+'-'+gl_name)+'.zip'

	slugified_category = slugify(category)
	category_directory = os.path.join(MEDIA_ROOT, 'projects/', slugified_category)
	if not os.path.exists(category_directory):
		os.makedirs(category_directory)

	model_project = AicSubmission.objects.create(leader=model_leader, solution=solution, problem_statement=problem_statement)

	for x in range(1,4):
		if model_member[x] != None:
			model_project.members.add(model_member[x])
	model_project.save()

	response = 1

	return JsonResponse(response, safe=False)
