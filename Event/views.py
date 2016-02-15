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



def windows_json(request):
	resp={}
	resp['Groups'] =[]
	krn_events= Event.objects.filter(is_kernel= True)
	eve_cat= EventCategory.objects.all()
	gen_events= Event.objects.filter(is_kernel= False)


	temp = {}
	temp['UniqueId'] = "Events"
	temp['Title'] = "Events"
	temp['Items'] = []


	tempx={}
	tempx['UniqueId'] = "Kernel Events"
	tempx['Title'] = "Kernel Events"
	tempx['ImagePath'] = "Assets/LightGray.png"
	tempx['SubItems'] = []
	for k in krn_events:
		itemdict= {}
		itemdict["UniqueId"] = str(k.name).replace(' ','') + str(k.id)
		itemdict['Title'] = itemdict['UniqueId']
		itemdict['ImagePath'] = "Assets/"+ str(k.name.replace(" ","").lower() ) + ".png"
		itemdict['Overview'] = str(k.short_description)
		itemdict['Rules'] = ""
		itemdict['Eligibility'] = ""
		itemdict['Guidlines'] = ""
		itemdict['Judging Criteria'] = ""
		itemdict['Problem Statements'] = ""
		itemdict['Resources'] = ""
		itemdict['Sample Questions'] = ""
		itemdict['Specifications'] = ""
		itemdict['Materials'] = ""
		itemdict['Registration Details'] = ""
		itemdict['FAQs'] = ""
		itemdict['Sponsors'] = ""
		itemdict['Contacts'] = ""
		tempx['SubItems'].append(itemdict)

	temp['Items'].append(tempx)

	for z in eve_cat:
		tempx={}
		tempx['UniqueId'] = str(z.name.replace(' ','')) + str(z.id)
		tempx['Title'] = tempx['UniqueId']
		tempx['SubItems'] = []
		for e_ob in Event.objects.filter(category=z):
			itemdict= {}
			itemdict["UniqueId"] = str(e_ob.name).replace(' ','') + str(e_ob.id)
			itemdict['Title'] = itemdict['UniqueId']
			itemdict['ImagePath'] = "Assets/"+ str(e_ob.name.replace(" ","").lower() ) + ".png"
			itemdict['Overview'] = str(e_ob.short_description)
			itemdict['Rules'] = ""
			itemdict['Eligibility'] = ""
			itemdict['Guidlines'] = ""
			itemdict['Judging Criteria'] = ""
			itemdict['Problem Statements'] = ""
			itemdict['Resources'] = ""
			itemdict['Sample Questions'] = ""
			itemdict['Specifications'] = ""
			itemdict['Materials'] = ""
			itemdict['Registration Details'] = ""
			itemdict['FAQs'] = ""
			itemdict['Sponsors'] = ""
			itemdict['Contacts'] = ""
			tempx['SubItems'].append(itemdict)
		temp['Items'].append(tempx)

	resp['Groups'].append(temp)

	return HttpResponse(json.dumps(resp), content_type="application/json")    	