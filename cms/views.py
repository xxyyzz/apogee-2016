from django.shortcuts import render
from registrations.models import *

# Create your views here.
def login(request):
    if request.POST:
        from django.contrib.auth import authenticate, login
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and user.is_staff:
                login(request, user)
                return HttpResponse('yay')
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                return render(request, 'cms/paper_home.html', {"status": 0})
        else:
            # Return an 'invalid login' error message.
            return render(request, 'cms/paper_home.html', {"status": 0})
    return render(request, 'cms/paper_home.html')
# def paper_home(request):
#     papers = Paper.objects.all()
#     context = {
#     'papers': papers,
#     }
#     return render(request, 'cms/paper_home.html', context)
def paper_home(request, status=None):
    if request.POST:
        if "initial" in request.POST:
            for paperid in request.POST.getlist("qualifiers"):
                paper = Paper.objects.get(id=paperid)
                paper.status = "0"
                paper.save()
        if "round1" in request.POST:
            for paperid in request.POST.getlist("qualifiers"):
                paper = Paper.objects.get(id=paperid)
                paper.status = "1"
                paper.save()
        if "round2" in request.POST:
            for paperid in request.POST.getlist("qualifiers"):
                paper = Paper.objects.get(id=paperid)
                paper.status = "2"
                paper.save()
    if status == None:
        papers = Paper.objects.all()
    if status == '0':
        papers = Paper.objects.filter(status='0')
    if status == '1':
        papers = Paper.objects.filter(status='1')
    if status == '2':
        papers = Paper.objects.filter(status='2')
    context = {
    'papers': papers,
    'status': status,
    }
    return render(request, 'cms/paper_home.html', context)
def project_home(request):
    return render(request, 'cms/paper_home.html')