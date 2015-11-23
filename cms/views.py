from django.shortcuts import render

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
def paper_home(request):
    return render(request, 'cms/paper_home.html')
def project_home(request):
    return render(request, 'cms/paper_home.html')