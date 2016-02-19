from django.shortcuts import render, redirect, resolve_url
from registrations.models import *
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.core.mail import send_mass_mail

def controls_check(user):
    if user.id:
        if user.is_superuser or user.email == 'controls@bits-apogee.org':
            return True
        else:
            return False
    else:
        return False

def pep_check(user):
    if user.id:
        if user.is_superuser or user.email == 'pep@bits-apogee.org':
            return True
        else:
            return False
    else:
        return False

def user_logout(request):
    logout(request)
    return redirect('cms:user_login')

def login_url(request):
    return reverse_lazy('cms:user_login')

# Create your views here.
def user_login(request, errors=None):
    context = {
        'errors': errors,
    }
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and user.is_staff:
                login(request, user)
                return render(request, 'cms/login.html', context)
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                return render(request, 'cms/login.html', context.update({"status": 0}))
        else:
            # Return an 'invalid login' error message.
            return render(request, 'cms/login.html', context.update({"status": 0}))
    return render(request, 'cms/login.html', context)

@user_passes_test(pep_check, login_url=reverse_lazy('cms:user_login', kwargs={'errors': "1"}), redirect_field_name=None)
def paper_home(request, status='0', category='0'):
    if request.POST:
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
        if "round3" in request.POST:
            for paperid in request.POST.getlist("qualifiers"):
                paper = Paper.objects.get(id=paperid)
                paper.status = "3"
                paper.save()
    if status == None or status == '0':
        papers = Paper.objects.all()
    else:
        papers = Paper.objects.filter(status=status)
    if category == None or category == '0':
        papers = papers
    else:
        papers = papers.filter(category__id=category)
    categories = Category.objects.filter(Q(model='Paper') | Q(model='Both'))
    context = {
    'papers': papers,
    'status': status,
    'category': category,
    'categories': categories,
    }
    return render(request, 'cms/paper_home.html', context)

@user_passes_test(controls_check, login_url=reverse_lazy('cms:user_login', kwargs={'errors': "1"}), redirect_field_name=None)
def project_home(request, status='0', category='0'):
    if request.POST:
        if "round1" in request.POST:
            for projectid in request.POST.getlist("qualifiers"):
                project = Project.objects.get(id=projectid)
                project.status = "1"
                project.save()
        if "round2" in request.POST:
            for projectid in request.POST.getlist("qualifiers"):
                project = Project.objects.get(id=projectid)
                project.status = "2"
                project.save()
        if "round3" in request.POST:
            for projectid in request.POST.getlist("qualifiers"):
                project = Project.objects.get(id=projectid)
                project.status = "3"
                project.save()
    if status == None or status == '0':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(status=status)
    if category == None or category == '0':
        projects = projects
    else:
        projects = projects.filter(category__id=category)
    categories = Category.objects.filter(Q(model='Project') | Q(model='Both'))
    context = {
    'projects': projects,
    'status': status,
    'category': category,
    'categories': categories,
    }
    return render(request, 'cms/project_home.html', context)

def project_email(request, projectid):
    project = Project.objects.get(id=projectid)
    context = {
    'project': project,
    }
    if request.POST:
        if "send" in request.POST:
            content = request.POST['content']
            recipientids = request.POST.getlist('recipientids')
            datatuple = ()
            for memberid in recipientids:
                participant = Participant.objects.get(id=memberid)
                subject = 'APOGEE 2016 Project Update'
                message = content.replace('Participant', participant.name)
                sender = 'BITS APOGEE 2016'
                recipient = participant.email
                subtuple = (subject, message, sender, [recipient])
                datatuple = (subtuple,) + datatuple
            status = send_mass_mail(datatuple)
            context.update({'status': status})
    return render(request, 'cms/project_email.html', context)