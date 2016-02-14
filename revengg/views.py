from django.shortcuts import render
from revengg.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
def software(request):
    return render(request, 'revengg/index.html')

@csrf_exempt
def create(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    try:
        Participant.objects.get(email=email)
    except:
        Participant.objects.create(name=name, email=email, phone=phone)
    return HttpResponse('1')

@csrf_exempt
def update(request):
    score = request.POST['name']
    email = request.POST['email']
    time = request.POST['phone']
    part = Participant.objects.get(email=email)
    part.time = time
    part.score = score
    part.save()
    return HttpResponse('1')
