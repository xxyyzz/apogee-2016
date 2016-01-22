from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from Event.models import *
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
	    event=events.objects.get(pk=eventid)
	except ObjectDoesNotExist:
	    raise Http404
	# if request.GET:
	# 	eventid = request.GET['id']
	# 	try :
	# 		event=events.objects.get(pk=eventid)
	# 	except ObjectDoesNotExist:
	# 		raise Http404       
	resp = {}
	
	# resp['category']=unicode(event.category.name)
	# resp['content']=str(unicode(event.content))
	resp['eventname']=str(unicode(event.name))
	resp['eventcategory']=str(unicode(event.category.name))
	resp['eventshortdescription']=unicode(event.short_description)
	resp['contact']=   str(  unicode(event.org.phone ) )
	resp['is_kernel']= str(unicode(event.is_kernel))
	resp['register']=    str(unicode(event.register) )
	# resp['eventdescription']=unicode(event.description)
	resp['tabs'] = [{k.heading.name : k.content} for k in event.tabs_set.all()]
	resp['img']=    str( unicode( event.img ))
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
		events = [{'id':event.id, 'name':event.name, 'short_desc':event.short_description} for event in category.events_set.all()]
		container['events'] = events
		response.append(container)
	return JsonResponse(response, safe=False)

# @csrf_exempt
# def getcategoryevents(request):
# 	if request.GET:
# 		data=request.GET
# 		name=data['category']
# 		try:
# 			c=Category.objects.get(name=name)
# 		except :
# 			raise Http404
# 		eset= Event.objects.filter(category = c)
# 		resp={}
# 		resp['Events']=[]
# 		for e in eset :
# 			dic={}
# 			dic['eventid']=int(e.id)
# 			dic['eventname']=str(unicode(e.name))
# 			dic['eventcategory']=str(unicode(e.category.name))
# 			dic['date']=    str( unicode( e.date ))
# 			dic['time']=   str(  unicode(e.time ) )
# 			dic['eventcontent']= str(unicode(e.content))
# 			dic['venue']=    str  (unicode(e.venue) )
# 			if e.icon:
# 				dic['eventicon']=str(e.icon.url)
# 			else :
# 				dic['eventicon']=''
# 			dic['eventdescription']=unicode(e.description)
# 			dic['eventshortdescription']=unicode(e.short_description)
# 			resp['Events'].append(dic)
# 		# json = simplejson.dumps(resp)
# 		# return HttpResponse(json, mimetype='application/json')
# 		return HttpResponse(json.dumps(resp), content_type="application/json")
# 	else:
# 		raise Http404
# @csrf_exempt
# def getnotificationdata(request):
#     try:
#         n =Notification.objects.all()
#     except :
#         raise Http404
#     resp={}
#     resp['Notifications']=[]
#     for notification in n :
#         dic={}
#         dic['content']=str(unicode(notification.content))
#         dic['type']=unicode(notification.types)
#         dic['link']=unicode(notification.link)
		
#         resp['Notifications'].append(dic)
#         # json = simplejson.dumps(resp)
#         # return HttpResponse(json, mimetype='application/json')
#     return HttpResponse(json.dumps(resp), content_type="application/json")

