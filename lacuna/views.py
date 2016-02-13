from django.shortcuts import render
from lacuna.models import *
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
    return render(request, 'lacuna/index.html')

@csrf_exempt
def user_login(request):
    fbid = request.POST['fbid']
    name = request.POST['name']
    try:
        part = Participant.objects.get(fbid=fbid)
    except:
        part = Participant.objects.create(fbid=fbid, name=name, start_time=timezone.now())
    response = {
        'status' : 1,
    }
    return JsonResponse(response)

@csrf_exempt
def status(request):
    fbid = request.POST['fbid']
    part = Participant.objects.get(fbid=fbid)
    response = {
        'fbid' : part.fbid,
        'name' : part.name,
        'score' : part.score,
        'dvm_level' : part.current_dvm_level,
        'informals_stats' : part.informals_stats,
    }
    return JsonResponse(response)

@csrf_exempt
def dvm_level_get(request):
    fbid = request.POST['fbid']
    level = request.POST['level']
    level = int(level)
    part = Participant.objects.get(fbid=fbid)
    if level <= part.current_dvm_level:
        levelobj = Level.objects.get(level=level, dept='DVM')
        response = {
            'status' : 1,
            'content' : levelobj.content
        }
    else:
        response = {
            'status' : 0,
            'message' : 'Bad Request',
        }
    return JsonResponse(response)

@csrf_exempt
def informals_level_verify(request):
    fbid = request.POST['fbid']
    level = request.POST['level']
    level = int(level)
    sol = request.POST['sol']
    levelobj = Level.objects.get(level=level)
    if sol == levelobj.answer:
        part = Participant.objects.get(fbid=fbid)
        stats = list(part.informals_stats)
        stats[level-1] = '2'
        stats = ''.join(stats)
        part.informals_stats = stats
        part.save()
        response = {
            'status' : 1,
        }
    else:
        response = {
            'status' : 0,
        }
    return JsonResponse(response)

def time_taken(ref_time):
    delta = timezone.now() - ref_time
    td = delta - timedelta(microseconds=delta.microseconds)
    return td

@csrf_exempt
def dvm1verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    error = False
    for value in sol:
        if value != 0:
            error = True
    if error == False:
        part = Participant.objects.get(fbid=fbid)
        if part.current_dvm_level == 1:
            part.current_dvm_level = 2
            part.dvm_1_time = time_taken(part.start_time)
            part.save()
        response = {
            'status' : 1,
        }
    else:
        response = {
            'status' : 0,
        }
    return JsonResponse(response)
