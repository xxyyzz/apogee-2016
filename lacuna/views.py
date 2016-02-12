from django.shortcuts import render
from lacuna.models import *
import json
import datetime

# Create your views here.
def home(request):
    return render(request, 'lacuna/index.html')

def user_login(request):
    fbid = request.POST['id']
    try:
        lacuna = Lacuna.models.get(fbid=fbid)
    except:
        lacuna = Lacuna.models.create(fbid=fbid, name=name, start_time=timezone.now)
    response = {
        'status' : 1,
    }
    return JsonResponse(response)

def status(request):
    fbid = request.POST['id']
    lacuna = Lacuna.models.get(fbid=fbid)
    score = lacuna.score
    response = {
        'fbid' : lacuna.fbid,
        'name' : lacuna.name,
        'score' : lacuna.score,
        'dvm_level' : lacuna.current_dvm_level,
        'informals_level' : lacuna.current_lacuna_level,
    }
    return JsonResponse(response)

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
        pass
