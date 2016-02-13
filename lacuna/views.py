from django.shortcuts import render
from lacuna.models import *
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
import json

# Create your views here.
@staff_member_required
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
        'score' : part.progress,
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
            'html_file' : levelobj.html_file,
            'css_file' : levelobj.css_file,
            'js_file' : levelobj.js_file,
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

def verify_final(request, error):
    PROGRESS = [3,6,11,16,23,31,40,50,61,73,86,100]
    fbid = request.POST['fbid']
    level = request.POST['level']
    level = int(level)
    if error == False:
        part = Participant.objects.get(fbid=fbid)
        if part.current_dvm_level == level:
            part.current_dvm_level = level+1
            delta = timezone.now() - part.start_time
            td = delta - timedelta(microseconds=delta.microseconds)
            # part['dvm_%s_time' % str(level)] = td
            part.start_time = timezone.now()
            part.progress = PROGRESS[level-1]
            part.save()
            attr = 'dvm_%s_time' % str(level)
            setattr(part, attr, td)
            part.save()
        response = {
            'status' : 1,
        }
    else:
        response = {
            'status' : 0,
        }
    return JsonResponse(response)


@csrf_exempt
def dvm1verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    level = request.POST['level']
    level = int(level)
    error = False
    for value in sol:
        if value != 0:
            error = True
    return verify_final(request, error)

@csrf_exempt
def dvm2verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    level = request.POST['level']
    level = int(level)
    error = False
    for i in range(0, int(len(sol)/2)):
        for j in range(0, int(len(sol[i])/2)):
            a = 2*i
            b = 2*j
            if sol[a][b]!=0 and ((a!=0 and sol[a-1][b]!=0 and (sol[a][b] != sol[a-1][b] or sol[a][b+1] != sol[a-1][b+1])) or (b!=0 and sol[a][b-1]!=0 and (sol[a][b] != sol[a][b-1] or sol[a+1][b] != sol[a+1][b-1]))):
                error = True;
    return verify_final(request, error)
