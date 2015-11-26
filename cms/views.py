from django.shortcuts import render, redirect, resolve_url
from registrations.models import *
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse, reverse_lazy

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
        if user.is_superuser or user.email == 'controls@bits-apogee.org':
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
def user_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and user.is_staff:
                login(request, user)
                return  redirect('cms:paper_home')
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                return render(request, 'cms/login.html', {"status": 0})
        else:
            # Return an 'invalid login' error message.
            return render(request, 'cms/login.html', {"status": 0})
    return render(request, 'cms/login.html')

@user_passes_test(pep_check, login_url=reverse_lazy('cms:user_login'), redirect_field_name=None)
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
    categories = Category.objects.all()
    context = {
    'papers': papers,
    'status': status,
    'category': category,
    'categories': categories,
    }
    return render(request, 'cms/paper_home.html', context)
def project_home(request):
    return render(request, 'cms/paper_home.html')