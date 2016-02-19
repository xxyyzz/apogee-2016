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
for part in parts:
    for event in part.events.filter(is_team=False):
        try:
            team = Team.objects.get(leader=part, event=event, members=None)
        except:
            team = Team.objects.create(leader=part, event=event)
            print "New Single Team ID " + str(team.id)

# Two levels for each event
for event in events:
    registered = Level.objects.get_or_create(name="Registered", event=event, position=2, is_protected=True)
    print "New Registered Level for " + event.name+  " ? " + str(registered[1]) + " ID " + str(registered[0].id)
    for team in teams:
        if team.event == event:
            print "Add Team " + str(team.id)
            registered[0].teams.add(team)
    winner = Level.objects.get_or_create(name="Winners", event=event, position=1, is_protected=True)
    print "New Winner Level for " + event.name+  " ? " + str(winner[1]) + " ID " + str(winner[0].id)
