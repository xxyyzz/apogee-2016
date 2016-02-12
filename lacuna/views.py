from django.shortcuts import render
from lacuna.models import *
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'lacuna/index.html')

@csrf_exempt
def user_login(request):
    fbid = request.POST['fbid']
    name = request.POST['name']
    try:
        lacuna = Lacuna.objects.get(fbid=fbid)
    except:
        lacuna = Lacuna.objects.create(fbid=fbid, name=name, start_time=datetime.now())
    response = {
        'status' : 1,
    }
    return JsonResponse(response)

@csrf_exempt
def status(request):
    fbid = request.POST['fbid']
    lacuna = Lacuna.objects.get(fbid=fbid)
    score = lacuna.score
    response = {
        'fbid' : lacuna.fbid,
        'name' : lacuna.name,
        'score' : lacuna.score,
        'dvm_level' : lacuna.current_dvm_level,
        'informals_level' : lacuna.current_informals_level,
    }
    return JsonResponse(response)

@csrf_exempt
def dvm_level_get(request):
    fbid = request.POST['fbid']
    level = request.POST['level']
    level = int(level)
    lacuna = Lacuna.objects.get(fbid=fbid)
    if lacuna.current_dvm_level <= level:
        leveldata = Level.objects.get(level=level, dept='DVM')
        response = {
            'status' : 1,
            'content' : leveldata.content
        }
    else:
        response = {
            'status' : 0,
            'message' : 'Bad Request',
        }
    return JsonResponse(response)


@csrf_exempt
def dvm1verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    error = False
    for row in sol:
        for value in row:
            if value != 0:
                error = True
    if error == False:
        part = Lacuna.objects.get(fbid=fbid)
        part.current_dvm_level = 2
        part.dvm_1_time = part.start_time - datetime.now()
