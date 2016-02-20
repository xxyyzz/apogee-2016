from Event.models import *
from backend.models import *
from ems.models import *
teams = Team.objects.all()
events = Event.objects.all()
parts = Participant.objects.all()

# clean teams
for team in teams:
    leader = team.leader
    if leader in team.members.all():
        print "Changed Team ID: " + str(team.id)
        team.members.remove(leader)

# teams for individual registration
count = 0
for part in parts:
    for event in part.events.filter(is_team=False):
        try:
            team = Team.objects.get(leader=part, event=event, members=None)
        except:
            team = Team.objects.create(leader=part, event=event)
            count += 1
            print "New Single Team ID " + str(team.id)
            print count

# Two levels for each event
for event in events:
    try:
        registered = Level.objects.get(name="Registered", event=event, is_protected=True)
    except:
        registered = Level.objects.create(name="Registered", event=event, position=2, is_protected=True)
        print "New Registered Level for " + event.name + " ID " + str(registered.id)
    for team in teams:
        if team.event == event:
            print "Add Team " + str(team.id)
            registered.teams.add(team)
    winner = Level.objects.get_or_create(name="Winners", event=event, position=1, is_protected=True)
    print "New Winner Level for " + event.name+  " ? " + str(winner[1]) + " ID " + str(winner[0].id)

try:
    college = College.objects.get(name="BITS Pilani")
except:
    college = College.objects.create(name="BITS Pilani")

for part in parts:
    if part.aadhaar is not None:
        part.aadhaar = part.aadhaar.upper()
        part.name = part.name.title()
        part.save()
        print "Part " + part.aadhaar + " changed."

import bitsians
for sid, name in bitsians.BITSIANS:
    email = sid.lower() + "@pilani.bits-pilani.ac.in"
    try:
        part = Participant.objects.get(aadhaar__icontains=sid)
        part.is_bitsian = True
        part.name = name
        part.email_id = email
        part.college = college
        part.save()
        print "Match found! " + sid + " changed"
    except:
        try:
            from django.db import IntegrityError
            part = Participant.objects.get(email_id=email)
            part.aadhaar = sid
            part.is_bitsian = True
            part.name = name
            part.email_id = email
            part.college = college
            part.save()
            print "Match found! " + email + " changed"
        except:
            phone = 9999999999
            part = Participant.objects.create(is_bitsian=True, aadhaar=sid, name=name, college=college, email_id=email)
            print sid + " created"
