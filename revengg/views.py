from django.shortcuts import render
from lacuna.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def software(request):
    return render(request, 'revengg/index.html')

# @csrf_exempt
# def user_login(request):
#     name = request.POST['name']
#     email = request.POST['email']
#     phone = request.POST['phone']
#     try:
#         part = Participant.objects.get(email=email)
#     except:
#         part = Participant.objects.create(email=email, name=name, phone=phone)
#     response = {
#         'status' : 1,
#     }
#     return JsonResponse(response)

