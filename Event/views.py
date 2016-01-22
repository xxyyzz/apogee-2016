from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from Event.models import *
from backend.models import *
from django.views.decorators.csrf import csrf_exempt
import json
import html2text as gaussx
# Create your views here.
@csrf_exempt
def geteventdata(request,event_id):
	try:
	    eventid = event_id
	except :
	    raise Http404
	try :
	    event=Event.objects.get(pk=eventid)
	except ObjectDoesNotExist:
	    raise Http404
	# if request.GET:
	# 	eventid = request.GET['id']
	# 	try :
	# 		event=Event.objects.get(pk=eventid)
	# 	except ObjectDoesNotExist:
	# 		raise Http404
	resp = {}

	# resp['category']=unicode(event.category.name)
	# resp['content']=str(unicode(event.content))
	resp['eventname']=event.name
	resp['eventcategory']=str(unicode(event.category.name))
	resp['eventshortdescription']=unicode(event.short_description)

	resp['contact']=   str(  unicode(event.org.phone ) )
	resp['is_kernel']= str(unicode(event.is_kernel))
	resp['register']=    str(unicode(event.register) )

	# resp['eventdescription']=unicode(event.description)
	resp['tabs'] = [{k.heading.name : k.content} for k in event.tab_set.all()]
	resp['img']= str(unicode( event.img ))
	return JsonResponse(resp)

@csrf_exempt
def summary(request):
	response = []
	categories = EventCategory.objects.all()
	categories = [x for x in categories if x.name != "Other"]
	for category in categories:
		container = {}
		container['category'] = category.name
		eventlist = {}
		events = [
					{
						'id':event.id,
						'name':event.name,
						'short_desc':event.short_description,
						'tags':[tag.name for tag in event.tags.all()] + (['kernel'] if event.is_kernel else []),
					}
						for event in category.event_set.all()
				]
		container['events'] = events
		response.append(container)
	return JsonResponse(response, safe=False)
