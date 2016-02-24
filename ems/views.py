from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from ems.models import Score, Level, Judge, Label
from Event.models import Event
from backend.models import Participant, Team
from django.contrib.auth.models import User

# Create your views here.
EMSADMINS = [
# have access to all events
    'admin',
    'controlsadmin',
]



def home(request):
    if request.user.is_authenticated() and request.user.is_staff:
        return redirect('ems:events_select')
    else:
        return redirect('ems:user_login')

def user_login(request, errors=None):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and user.is_staff:
                login(request, user)
                return redirect('ems:home')
    return render(request, 'ems/login.html')

def user_logout(request):
    logout(request)
    return redirect('ems:user_login')

@staff_member_required
def bitsian_add(request):
    if request.POST:
        long_id = request.POST['long_id'].upper()
        short_id = request.POST['short_id']
        gender = request.POST['gender'].upper()
        name = request.POST['name'].upper()
        import re
        verify = re.match(r'\d{4}.{4}\d{3}P', long_id)
        if verify:
            try:
                bitsian = Bitsian.objects.get(long_id=long_id)
                context = {
                    'status' : 0,
                    'bitsian' : bitsian,
                }
                return render(request, 'ems/bitsian_add.html', context)
            except ObjectDoesNotExist:
                bitsian = Bitsian()
                bitsian.long_id = long_id
                bitsian.short_id = short_id
                bitsian.name = name
                bitsian.gender = gender[0]
                bitsian.college = 'BITS Pilani'
                bitsian.save()
                context = {
                    'status' : 1,
                    'bitsian' : bitsian,
                }
                return render(request, 'ems/bitsian_add.html', context)
        else:
            context = {
                'status' : 0,
                'wrongid' : long_id,
            }
            return render(request, 'ems/bitsian_add.html', context)

    else:
        return render(request, 'ems/bitsian_add.html')


@staff_member_required
def team_details_home(request):
    if request.POST:
        teamid = request.POST['code']
        return redirect('ems:team_details', teamid)
    else:
        return render(request, 'ems/team_home.html')

@staff_member_required
def team_details(request, teamid):
    if request.POST:
        team = Team.objects.get(id=teamid)
        if request.POST['position'] == '':
            team.position = None
        else:
            team.position = request.POST['position']
        team.name_cheque = request.POST['name_cheque']
        team.address = request.POST['address']
        team.category = request.POST['category']
        team.save()
        if 'add' in request.POST:
            id_list = [sg_id for sg_id in filter(lambda a: a != '', request.POST.get('idlist', '').replace(",","").split(" "))]
            outside_list = [x for x in id_list if len(x) < 5]
            bitsian_short_list = [x for x in id_list if len(x) >= 5 and len(x) < 11]
            bitsian_long_list = [x for x in id_list if len(x) >= 11]

            try:
                reg_objs = InitialRegistration.objects.filter(id__in = outside_list)
                for r in reg_objs:
                    team.members.add(r)
            except:
                context['error_message'] = "Error Generating Team"
                return redirect('ems:main')
            try:
                bitsian_short_objs =  Bitsian.objects.filter(short_id__in = bitsian_short_list)
                bitsian_long_objs = Bitsian.objects.filter(long_id__in = bitsian_long_list)
                bitsians = bitsian_long_objs | bitsian_short_objs
                for r in bitsians:
                    team.bitsian_members.add(r)
            except:
                context['error_message'] = "Error Generating Team"
                return redirect('ems:main')
            team.save()
        if 'delete-outstation' in request.POST:
            memberid = request.POST['delete-outstation']
            member = InitialRegistration.objects.get(id=memberid)
            team.members.remove(member)
            team.save()
        if 'delete-bitsian' in request.POST:
            memberid = request.POST['delete-bitsian']
            member = Bitsian.objects.get(id=memberid)
            team.bitsian_members.remove(member)
            team.save()

    try:
        team = Team.objects.get(id=teamid)
    except:
        return render(request, 'ems/team_home.html', {'status' : 0})
    context = {
        'team' : team,
    }
    return render(request, 'ems/team_details.html', context)

@staff_member_required
def participant_details_home(request):
    if request.POST:
        partid = request.POST['code']
        return redirect('ems:participant_details', partid)
    else:
        return render(request, 'ems/participant_home.html')

@staff_member_required
def participant_details(request, partid):
    try:
        participant = InitialRegistration.objects.get(id=partid)
    except:
        return render(request, 'ems/participant_home.html', {'status' : 0})
    context = {
        'participant' : participant,
    }
    return render(request, 'ems/participant_details.html', context)

@staff_member_required
def events_select(request):
    if request.method == 'POST':
        eventid = request.POST['event']
        return redirect('ems:events_home', eventid)
    if request.user.username in EMSADMINS:
        events = Event.objects.order_by('name')
    else:
        events = [x for x in request.user.organization.event_set.order_by('name')]
    context = {
        'events' : events,
    }
    return render(request, 'ems/events_select.html', context)

@csrf_exempt
def events_home(request, eventid):
    if not request.user.is_staff:
        return redirect('ems:user_login')
    event = Event.objects.get(id=eventid)
    levels = Level.objects.filter(event=event)
    emsadmin = True if request.user.username in EMSADMINS else False
    if request.POST:
        if "promote" in request.POST:
            position = int(request.POST['promote'])
            teams = request.POST.getlist('teams')
            try:
                curr_level = Level.objects.get(event=event, position=position)
            except:
                return HttpResponse("Error: Duplicate levels with rank %s. <br> Please Ensure correct them from the 'Manage Levels' pane." % str(position))
            try:
                next_level = Level.objects.get(event=event, position=position-1)
            except:
                return HttpResponse("Error: Cannot find level with rank %s. <br> Please Ensure Level Rankings are in continuous order, starting from 1. Correct them from the 'Manage Levels' pane." % str(position-1))
            for teamid in teams:
                team = Team.objects.get(id=teamid)
                next_level.teams.add(team)
        if "demote" in request.POST:
            position = int(request.POST['demote'])
            teams = request.POST.getlist('teams')
            try:
                curr_level = Level.objects.get(event=event, position=position)
            except:
                return HttpResponse("Error: Duplicate levels with rank %s. <br> Please Ensure correct them from the 'Manage Levels' pane." % str(position))
            try:
                prev_level = Level.objects.get(event=event, position=position+1)
            except:
                return HttpResponse("Error: Cannot find Level with rank %s. <br> Please Ensure Level Rankings are in continuous order, starting from 1. Correct them from the 'Manage Levels' pane." % str(position+1))
            for teamid in teams:
                team = Team.objects.get(id=teamid)
                curr_level.teams.remove(team)
                if team not in prev_level.teams.all():
                    prev_level.teams.add(team)
        if "add-finalists" in request.POST:
            teamids = request.POST.getlist('registered')
            for teamid in teamids:
                Team.objects.filter(id=teamid).update(is_finalist=True)
        if "remove-finalists" in request.POST:
            teamids = request.POST.getlist('finalists')
            for teamid in teamids:
                Team.objects.filter(id=teamid).update(is_finalist=False)
        if "add-winners" in request.POST:
            teamids = request.POST.getlist('registered')
            for teamid in teamids:
                Team.objects.filter(id=teamid).update(is_winner=True)
        if "remove-winners" in request.POST:
            teamids = request.POST.getlist('winners')
            for teamid in teamids:
                Team.objects.filter(id=teamid).update(is_winner=False)
        if "delete-team" in request.POST:
            teamid = request.POST['delete-team']
            Team.objects.get(id=teamid).delete()
    context = {
        'event' : event,
        'levels' : levels,
        'emsadmin' : emsadmin,
    }
    if emsadmin:
        return render(request, 'ems/events_home_admin.html', context)
    else:
        return render(request, 'ems/events_home.html', context)

def events_levels(request, eventid):
    event = Event.objects.get(id=eventid)
    levels = Level.objects.filter(event=event)
    emsadmin = True if request.user.username in EMSADMINS else False
    if request.method == 'POST':
        if 'delete-level' in request.POST:
            levelid = request.POST['delete-level']
            level = Level.objects.get(id=levelid)
            level.teams.clear()
            level.delete()
        if 'delete-judge' in request.POST:
            judgeid = request.POST['delete-judge']
            judge = Judge.objects.get(id=judgeid)
            judge.level_set.clear()
            judge.user.delete()
            judge.delete()
        if 'delete-label' in request.POST:
            labelid = request.POST['delete-label']
            label = Label.objects.get(id=labelid)
            label.delete()
    context = {
        'event' : event,
        'levels' : levels,
        'emsadmin' : emsadmin,
    }
    return render(request, 'ems/events_levels.html', context)

def events_levels_add(request, eventid):
    event = Event.objects.get(id=eventid)
    levels = Level.objects.filter(event=event)
    emsadmin = True if request.user.username in EMSADMINS else False
    if request.method == 'POST':
        if 'add' in request.POST:
            name = request.POST['name']
            position = int(request.POST['position'])
            level = Level.objects.create(name=name, position=position, event=event)
            if 'judgesheet' in request.POST:
                labelid = request.POST['label']
                label = Label.objects.get(id=labelid)
                level.label = label
                level.save()
                judges = request.POST.getlist('judge')
                for judgeid in judges:
                    judge = Judge.objects.get(id=judgeid)
                    level.judges.add(judge)
        return redirect('ems:events_levels', event.id)
    context = {
        'event' : event,
        'levels' : levels,
        'emsadmin' : emsadmin,
    }
    return render(request, 'ems/events_levels_add.html', context)

def events_labels_add(request, eventid):
    event = Event.objects.get(id=eventid)
    levels = Level.objects.filter(event=event)
    emsadmin = True if request.user.username in EMSADMINS else False
    if request.method == 'POST':
        if 'add' in request.POST:
            names = request.POST.getlist("name")
            maxvalues = request.POST.getlist("max")
            label = Label(event=event)
            for i, name in enumerate(names):
                attr = "var" + str(i+1) + "name"
                setattr(label, attr, name)
            for i, maxvalue in enumerate(maxvalues):
                attr = "var" + str(i+1) + "max"
                setattr(label, attr, maxvalue)
            label.save()
        return redirect('ems:events_levels', event.id)
    context = {
        'event' : event,
        'levels' : levels,
        'emsadmin' : emsadmin,
    }
    return render(request, 'ems/events_labels_add.html', context)

def events_judges_add(request, eventid):
    event = Event.objects.get(id=eventid)
    levels = Level.objects.filter(event=event)
    emsadmin = True if request.user.username in EMSADMINS else False
    if request.method == 'POST':
        if 'add' in request.POST:
            name = request.POST['name']
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.create_user(username=username, password=password)
            except:
                return HttpResponse("Please use a different username. Press the back button to continue")
            judge = Judge.objects.create(name=name, event=event, user=user)
            judge.user = user
            judge.save()
            return redirect('ems:events_levels', event.id)
    context = {
        'event' : event,
        'levels' : levels,
        'emsadmin' : emsadmin,
    }
    return render(request, 'ems/events_judges_add.html', context)


def events_levels_edit(request, eventid, levelid):
    emsadmin = True if request.user.username in EMSADMINS else False
    event = Event.objects.get(id=eventid)
    level = Level.objects.get(id=levelid)
    if 'save' in request.POST:
        name = request.POST['name']
        position = int(request.POST['position'])
        level.name = name
        level.position = position
        level.label = None
        level.save()
        level.judges.clear()
        if 'judgesheet' in request.POST:
            labelid = request.POST['label']
            label = Label.objects.get(id=labelid)
            level.label = label
            level.save()
            judges = request.POST.getlist('judge')
            for judgeid in judges:
                judge = Judge.objects.get(id=judgeid)
                level.judges.add(judge)
        return redirect('ems:events_levels', event.id)
    if 'delete' in request.POST:
        level.delete()
        return redirect('ems:events_home', event.id)
    context = {
        'event' : event,
        'level' : level,
        'emsadmin' : emsadmin,
    }
    return render(request, 'ems/events_levels_edit.html', context)

def events_judge_home(request, eventid):
    event = Event.objects.get(id=eventid)
    context = {
        'event' : event,
    }
    return render(request, 'ems/events_judge_home.html', context)

def events_judge_login(request, eventid, levelid, judgeid):
    event = Event.objects.get(id=eventid)
    judge = Judge.objects.get(id=judgeid)
    level = Level.objects.get(id=levelid)
    context = {
        'event' : event,
        'level' : level,
        'judge' : judge,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and user == judge.user:
                login(request, user)
                return redirect('ems:events_levels_judge', event.id, level.id, judge.id)
            else:
                context['status'] = 0
    return render(request, 'ems/login.html', context)

def events_levels_judge(request, eventid, levelid, judgeid):
    event = Event.objects.get(id=eventid)
    level = Level.objects.get(id=levelid)
    judge = Judge.objects.get(id=judgeid)
    emsadmin = True if request.user.username in EMSADMINS else False
    if not emsadmin and request.user != judge.user:
        return redirect('ems:events_judge_login', event.id, level.id, judge.id)
    if request.method == 'POST':
        if 'leave' in request.POST:
            # print "leave"
            for team in level.teams.all():
                try:
                    score = Score.objects.get(level=level, team=team, judge=judge)
                    if not score.is_frozen:
                        score.delete()
                        score = Score.objects.create(level=level, team=team, judge=judge)
                        score.is_frozen = True
                        score.save()
                except:
                    score = Score.objects.create(level=level, team=team, judge=judge)
                    score.is_frozen = True
                    score.save()
        elif "save" or "freeze" in request.POST:
            # print "save"
            for team in level.teams.all():
                scores = request.POST.getlist(str(team.id))
                try:
                    score = Score.objects.get(level=level, team=team, judge=judge)
                except:
                    score = Score.objects.create(level=level, team=team, judge=judge)
                for i, val in enumerate(scores):
                    attr = 'var' + str(i+1)
                    setattr(score, attr, val)
                comments = request.POST['comment-'+str(team.id)]
                score.comments = comments
                if "freeze" in request.POST:
                    score.is_frozen = True
                score.save()
    teams = []
    for team in level.teams.all():
        try:
            score = Score.objects.get(level=level, team=team, judge=judge)
            team.score = score
            total = 0
            for x in range(1, 11):
                attr = 'var' + str(x)
                try:
                    val = getattr(score, attr)
                    total += val
                except:
                    pass
            team.score.total = total
        except:
            # print "pass"
            pass
        teams.append(team)
    context = {
        'event' : event,
        'level' : level,
        'judge' : judge,
        'teams' : teams,
        'emsadmin' : emsadmin,
    }
    return render(request, 'ems/events_judge_edit.html', context)

def events_participants(request, eventid):
    event = Event.objects.get(id=eventid)
    emsadmin = True if request.user.username in EMSADMINS else False
    if event.is_team:
        return redirect('ems:events_teams', event.id)
    teams = Team.objects.filter(event=event)
    if request.method == 'POST':
        if 'delete-team' in request.POST:
            teamid = request.POST['delete-team']
            team = Team.objects.get(id=teamid)
            team.delete()
    context = {
        'event' : event,
        'teams' : teams,
        'emsadmin' : emsadmin,
    }
    return render(request, 'ems/events_participants.html', context)

def events_participants_add(request, eventid):
    event = Event.objects.get(id=eventid)
    emsadmin = True if request.user.username in EMSADMINS else False
    parts = []
    if request.method == 'POST':
        if 'fetch' in request.POST:
            partid = request.POST['aadhaar']
            partids = partid.split()
            for partid in partids:
                try:
                    part = Participant.objects.get(aadhaar__icontains=partid)
                    parts.append(part)
                except:
                    pass
                try:
                    part = Participant.objects.get(id__icontains=partid)
                    parts.append(part)
                except:
                    pass
        if 'add' in request.POST:
            partids = request.POST.getlist('part')
            for partid in partids:
                part = Participant.objects.get(id=partid)
                try:
                    team = Team.objects.get(leader=part, event=event, members=None)
                except:
                    team = Team.objects.create(leader=part, event=event)
                    registered = Level.objects.get(name="Registered", event=event)
                    team.levels.add(registered)
            return redirect('ems:events_participants', event.id)
    context = {
        'event' : event,
        'parts' : parts,
        'emsadmin' : emsadmin,
    }
    return render(request, 'ems/events_participants_add.html', context)

def events_teams(request, eventid):
    event = Event.objects.get(id=eventid)
    emsadmin = True if request.user.username in EMSADMINS else False
    if not event.is_team:
        return redirect('ems:events_participants', event.id)
    teams = Team.objects.filter(event=event)
    if request.method == 'POST':
        if 'delete-team' in request.POST:
            teamid = request.POST['delete-team']
            team = Team.objects.get(id=teamid)
            team.delete()
    context = {
        'event' : event,
        'teams' : teams,
        'emsadmin' : emsadmin,
    }
    return render(request, 'ems/events_teams.html', context)

def events_teams_add(request, eventid):
    event = Event.objects.get(id=eventid)
    parts = []
    select = []
    errors = []
    if request.method == 'POST':
        if 'fetch' in request.POST:
            partid = request.POST['aadhaar']
            if ";" in partid:
                existingteams = Team.objects.filter(event=event)
                newteams = partid.split(";")
                for newteam in newteams:
                    team_parts = []
                    team_partids = newteam.split()
                    for team_partid in team_partids:
                        try:
                            part = Participant.objects.get(aadhaar__icontains=team_partid)
                            team_parts.append(part)
                        except:
                            pass
                        try:
                            part = Participant.objects.get(id__icontains=team_partid)
                            team_parts.append(part)
                        except:
                            pass
                    if team_parts:
                        for part in parts:
                            for existingteam in existingteams:
                                if part in existingteam.members.all():
                                    error = part.name+" is already a part of "+team.leader.name+"'s Team."
                                    errors.append(error)
                                if part == existingteam.leader:
                                    error = part.name+" already have their own team."
                                    errors.append(error)
                            if errors:
                                return HttpResponse(error)
                        leader = team_parts[0]
                        team = Team.objects.create(leader=leader, event=event)
                        members = team_parts[1:]
                        for member in members:
                            team.members.add(member)
                        registered = Level.objects.get(name="Registered", event=event)
                        team.levels.add(registered)
                return redirect('ems:events_participants', event.id)

            else:
                partids = partid.split()
                for partid in partids:
                    try:
                        part = Participant.objects.get(aadhaar__icontains=partid)
                        parts.append(part)
                    except:
                        pass
                    try:
                        part = Participant.objects.get(id__icontains=partid)
                        parts.append(part)
                    except:
                        pass
        if 'next' in request.POST:
            teams = event.team_set.all()
            partids = request.POST.getlist('part')
            for partid in partids:
                part = Participant.objects.get(id=partid)
                for team in teams:
                    if part in team.members.all():
                        error = part.name+" is already a part of "+team.leader.name+"'s Team."
                        errors.append(error)
                    if part == team.leader:
                        error = part.name+" already have their own team."
                        errors.append(error)
            if not errors:
                for partid in partids:
                    part = Participant.objects.get(id=partid)
                    select.append(part)
        if "add" in request.POST:
            teams = event.team_set.all()
            partids = request.POST.getlist('part')
            leaderid = request.POST['leader']
            name = request.POST['name']
            comments = request.POST['comments']
            leader = Participant.objects.get(id=leaderid)
            team = Team.objects.create(leader=leader, event=event, name=name, comments=comments)
            for partid in partids:
                if partid != leaderid:
                    part = Participant.objects.get(id=partid)
                    team.members.add(part)
            registered = Level.objects.get(name="Registered", event=event)
            team.levels.add(registered)
            return redirect('ems:events_participants', event.id)
    context = {
        'event' : event,
        'parts' : parts,
        'select' : select,
        'errors' : errors,
    }
    return render(request, 'ems/events_teams_add.html', context)

def events_teams_edit(request, eventid, teamid):
    event = Event.objects.get(id=eventid)
    team = Team.objects.get(id=teamid)
    if request.method == 'POST':
        if 'save' in request.POST:
            comments = request.POST['comments']
            team.comments = comments
            team.save()
    context = {
        'event' : event,
        'team' : team,
    }
    return render(request, 'ems/events_teams_edit.html', context)


# @staff_member_required
# def upload_list(request):
#     events = [x for x in Event.objects.order_by('name') if x.category.name != "Other"]
#     context = {
#         'events' : events,
#     }
#     return render(request, "ems/upload_list.html", context)
#
# @csrf_exempt
# @staff_member_required
# def choose_leader(request):
#     if request.method == "POST":
#         context = RequestContext(request)
#
#         id_list = [sg_id for sg_id in filter(lambda a: a != '', request.POST.get('id_list', '').replace(",","").split(" "))]
#         outside_list = [x for x in id_list if len(x) < 5]
#         bitsian_short_list = [x for x in id_list if len(x) >= 5 and len(x) < 11]
#         bitsian_long_list = [x for x in id_list if len(x) >= 11]
#         outsiders = InitialRegistration.objects.filter(id__in = outside_list)
#         bitsian_short_objs =  Bitsian.objects.filter(short_id__in = bitsian_short_list)
#         bitsian_long_objs = Bitsian.objects.filter(long_id__in = bitsian_long_list)
#         bitsians = bitsian_long_objs | bitsian_short_objs
#         context = RequestContext(request)
#         context['outsiders'] = outsiders
#         context['bitsians'] = bitsians
#         context['event_name'] = request.POST['event_name']
#         context['id_list'] = request.POST.get('id_list', '')
#         # context['names'] = [r.name for r in reg_objs]
#         # context['colleges'] = [r.college for r in reg_objs]
#         # context['phones'] = [r.phone_one for r in reg_objs]
#
#         return render(request, "ems/chooseLeader.html", context)
#     else:
#         return redirect('ems:main')
#
# @csrf_exempt
# @staff_member_required
# def genTeam(request):
#     if request.method == "POST":
#         leader_id = request.POST['leader_id']
#         try:
#             leader_obj = InitialRegistration.objects.get(id=leader_id)
#         except:
#             leader_obj = Bitsian.objects.get(long_id=leader_id)
#         event_obj = Event.objects.get(name=request.POST['event_name'])
#         college_obj = College.objects.get(name=leader_obj.college)
#         team_obj = Team()
#         team_obj.event = event_obj
#         try:
#             team_obj.leader = leader_obj
#             team_obj.bitsian_leader = None
#         except:
#             team_obj.bitsian_leader = leader_obj
#             team_obj.leader = None
#         team_obj.address = request.POST['address']
#         team_obj.name_cheque = request.POST['name_cheque']
#         team_obj.college = college_obj
#         try:
#             team_obj.position = int(request.POST['position'])
#         except:
#             team_obj.position = None
#         category = request.POST['category']
#         if category == '':
#             team_obj.category = None
#         else:
#             team_obj.category = request.POST['category']
#         if 'generate' in request.POST:
#             team_obj.is_winner=False
#         if 'generate-winner' in request.POST:
#             team_obj.is_winner=True
#         team_obj.save()
#         context = {}
#
#         id_list = [sg_id for sg_id in filter(lambda a: a != '', request.POST.get('id_list','').replace(",","").split(" "))]
#         outside_list = [x for x in id_list if len(x) < 5]
#         bitsian_short_list = [x for x in id_list if len(x) >= 5 and len(x) < 11]
#         bitsian_long_list = [x for x in id_list if len(x) >= 11]
#
#         try:
#             reg_objs = InitialRegistration.objects.filter(id__in = outside_list)
#             for r in reg_objs:
#                 team_obj.members.add(r)
#         except:
#             context['error_message'] = "Error Generating Team"
#             return redirect('ems:main')
#         try:
#             bitsian_short_objs =  Bitsian.objects.filter(short_id__in = bitsian_short_list)
#             bitsian_long_objs = Bitsian.objects.filter(long_id__in = bitsian_long_list)
#             bitsians = bitsian_long_objs | bitsian_short_objs
#             for r in bitsians:
#                 team_obj.bitsian_members.add(r)
#         except:
#             context['error_message'] = "Error Generating Team"
#             return redirect('ems:main')
#
#         team_obj.save()
#
#         context['error_message'] = "Team Generated Successfully"
#
#         return redirect('ems:main')
#     else:
#         return redirect('ems:main')

# @csrf_exempt
# @staff_member_required
# def getParticipantList(request):
#     pass
#     id_list = [sg_id for sg_id in filter(lambda a: a != '', request.POST.get('id_list', '').replace(",","").split(" "))]

#     outside_list = [x for x in id_list if len(x) < 5]
#     bitsian_short_list = [x for x in id_list if len(x) >= 5 and len(x) < 11]
#     bitsian_long_list = [x for x in id_list if len(x) >= 11]
#     outsiders = InitialRegistration.objects.filter(id__in = outside_list)
#     bitsian_short_objs =  Bitsian.objects.filter(short_id__in = bitsian_short_list)
#     bitsian_long_objs = Bitsian.objects.filter(long_id__in = bitsian_long_list)
#     bitsians = bitsian_long_objs | bitsian_short_objs

#     context = {}
#     context['ids'] = [r.id for r in outsiders] + [r.long_id for r in bitsians]
#     context['names'] = [r.name for r in outsiders] + [r.name for r in bitsians]
#     context['colleges'] = [r.college for r in outsiders] + [r.college for r in bitsians]
#     context['phones'] = [r.phone_one for r in outsiders] + [None for r in bitsians]
#     print context
#     return JsonResponse(context, safe=False)
