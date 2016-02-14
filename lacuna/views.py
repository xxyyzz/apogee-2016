from django.shortcuts import render
from lacuna.models import *
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
import json
# import yaml

# Create your views here.
# @staff_member_required
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
def storyline(request):
    level = request.POST['level']
    level = int(level)
    # story = Story.objects.all()
    story = Story.objects.get(level=level)
    content = story.content
    return JsonResponse(content, safe=False)

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
def informals_level_get(request):
    fbid = request.POST['fbid']
    level = request.POST['level']
    level = int(level)
    part = Participant.objects.get(fbid=fbid)
    even_level = part.current_dvm_level - part.current_dvm_level % 2
    if level <= even_level:
        levelobj = Level.objects.get(level=level, dept='INFORMALS')
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
    if sol.upper().replace(' ', '') == levelobj.answer.upper().replace(' ', ''):
        part = Participant.objects.get(fbid=fbid)
        stats = list(part.informals_stats)
        count = stats.count('0')
        count = 12 - count
        if stats[level-1] == '0':
            stats[level-1] = '2'
            stats = ''.join(stats)
            part.informals_stats = stats
            part.save()
            stats = list(part.informals_stats)
            count = stats.count('0')
            count = 12 - count
            part.informals_score = part.informals_score + count*50
            part.save()
        response = {
            'status' : 1,
        }
    else:
        response = {
            'status' : 0,
        }
    return JsonResponse(response)

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
            # part.save()
            attr = 'dvm_%s_time' % str(level)
            setattr(part, attr, td)
            part.save()
            total_time = timedelta(seconds=0)
            for i in range(1, 13):
                attr = 'dvm_%s_time' % str(i)
                addition = getattr(part, attr)
                if addition is not None:
                    total_time = total_time + addition
            part.total_time = total_time
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
    return verify_final(request, error)

@csrf_exempt
def dvm2verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    level = request.POST['level']
    level = int(level)
    error = True
    if sol.upper().replace(' ', '') == 'SAMYEMONASTERY':
        error = False
    return verify_final(request, error)

@csrf_exempt
def dvm3verify(request):
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
def dvm4verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    level = request.POST['level']
    level = int(level)
    error = True
    # remove spaces and convert to upper
    # if sol.upper().replace(' ', '') == '':
        # error = False
    return verify_final(request, error)

@csrf_exempt
def dvm5verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    level = request.POST['level']
    level = int(level)
    error = True
    # remove spaces and convert to upper
    # if sol.upper().replace(' ', '') == '':
        # error = False
    return verify_final(request, error)

@csrf_exempt
def dvm6verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    level = request.POST['level']
    level = int(level)
    error = True
    # remove spaces and convert to upper
    # if sol.upper().replace(' ', '') == '':
        # error = False
    return verify_final(request, error)

@csrf_exempt
def dvm7verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    level = request.POST['level']
    level = int(level)
    error = False
    temp = [0,0,0,0,0,0,0,0,0,0]
    for i in sol:
        for j in col:
            temp[i+6] += sol[i][j]
            temp[j+1] += sol[i][j]
        temp[0] += sol[i][i]
        temp[5] += sol[i][3-1]
    for i in temp:
        if i != 6:
            error = True
    return verify_final(request, error)

@csrf_exempt
def dvm8verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    level = request.POST['level']
    level = int(level)
    error = True
    # remove spaces and convert to upper
    # if sol.upper().replace(' ', '') == '':
        # error = False
    return verify_final(request, error)

@csrf_exempt
def dvm9verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    level = request.POST['level']
    level = int(level)
    error = True
    # remove spaces and convert to upper
    # if sol.upper().replace(' ', '') == '':
        # error = False
    return verify_final(request, error)

@csrf_exempt
def dvm10verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    level = request.POST['level']
    level = int(level)
    error = True
    # remove spaces and convert to upper
    # if sol.upper().replace(' ', '') == '':
        # error = False
    return verify_final(request, error)

@csrf_exempt
def dvm11verify(request):
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

@csrf_exempt
def dvm12verify(request):
    fbid = request.POST['fbid']
    sol = request.POST['sol']
    sol = json.loads(sol)
    level = request.POST['level']
    level = int(level)
    error = True
    # remove spaces and convert to upper
    # if sol.upper().replace(' ', '') == '':
        # error = False
    return verify_final(request, error)

def leaderboard(request):
    parts = Participant.objects.order_by('-progress', 'total_time')
    context = {
        'parts' : parts,
    }
    return render(request, 'lacuna/leaderboard.html', context)
