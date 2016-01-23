from django.http import JsonResponse, HttpResponse

def staff_check(request):
	if request.user.is_staff:
		response = {
			'status' : 0,
			'message' : 'You are logged in as staff. Only registered users can access this section',
		}
		return HttpResponse(response)
