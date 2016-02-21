# encoding=utf8
from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from Event.models import *
from backend.models import *
from django.views.decorators.csrf import csrf_exempt
import json
from html2text import html2text as gaussx
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
						for event in category.event_set.filter(is_displayed=True)
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


	overview_ob  =Heading.objects.get(name='Overview')
	rules_ob  =Heading.objects.get(name='Rules')
	eligibility_ob  =Heading.objects.get(name='Eligibility')
	guidelines_ob  =Heading.objects.get(name='Guidelines')
	judging_ob  =Heading.objects.get(name='Judging Criteria')
	prob_ob  =Heading.objects.get(name='Problem Statements')
	resources_ob  =Heading.objects.get(name='Resources')
	sampleq_ob  =Heading.objects.get(name='Sample Questions')
	specifications_ob  =Heading.objects.get(name='Specifications')
	materials_ob  =Heading.objects.get(name='Materials')
	regdetails_ob  =Heading.objects.get(name='Registration Details')
	faqs_ob  =Heading.objects.get(name='FAQs')
	sponsors_ob  =Heading.objects.get(name='Sponsors')

	for k in krn_events:
		itemdict= {}
		itemdict["UniqueId"] = str(k.name)
		itemdict['Title'] = itemdict['UniqueId']
		itemdict['ImagePath'] = "Assets/"+ str(k.name.replace(" ","").lower() ) + ".png"
		try:
			itemdict['Overview'] = str(   gaussx( str((Tab.objects.get(event=k, heading= overview_ob) ).content ) )   )
		except:
			itemdict['Overview'] = ""
		try:
			itemdict['Rules'] = str(   gaussx( str((Tab.objects.get(event=k, heading= rules_ob ) ).content) )   )
		except:
			itemdict['Rules'] = ""

		try:			
			itemdict['Eligibility'] = str(   gaussx((Tab.objects.get(event=k, heading= eligibility_ob) ).content )   )
		except:
			itemdict['Eligibility'] = ""

		try:			
			itemdict['Guidelines'] = str(   gaussx((Tab.objects.get(event=k, heading= guidelines_ob ) ).content )   )
		except:
			itemdict['Guidelines'] = ""

		try:			
			itemdict['Judging Criteria'] =str(    gaussx((Tab.objects.get(event=k, heading= judging_ob) ).content )   )
		except:
			itemdict['Judging Criteria'] =""

		try:			
			itemdict['Problem Statements'] = str(    gaussx((Tab.objects.get(event=k, heading= prob_ob)  ).content )  )
		except:
			itemdict['Problem Statements'] = ""


		try:			
			itemdict['Resources'] = str(   gaussx((Tab.objects.get(event=k, heading=resources_ob) ).content )   )
		except:
			itemdict['Resources'] = ""

		try:
			itemdict['Sample Questions'] =str( gaussx((Tab.objects.get(event=k, heading= sampleq_ob) ).content )   )
		except:
			itemdict['Sample Questions'] =""

		try:			
			itemdict['Specifications'] = str(  gaussx((Tab.objects.get(event=k, heading= specifications_ob) ).content )   )
		except:
			itemdict['Specifications'] = ""

		try:			
			itemdict['Materials'] = str(   gaussx((Tab.objects.get(event=k, heading= materials_ob) ).content )   )
		except:
			itemdict['Materials'] = ""

		try:			
			itemdict['Registration Details'] = str(   gaussx((Tab.objects.get(event=k, heading= regdetails_ob) ).content )   )
		except:
			itemdict['Registration Details'] = ""

		try:			
			itemdict['FAQs'] = str(   gaussx((Tab.objects.get(event=k, heading= faqs_ob) ).content )   )
		except:
			itemdict['FAQs'] = ""

		try:			
			itemdict['Sponsors'] = str(   gaussx((Tab.objects.get(event=k, heading= sponsors_ob) ).content )   )
		except:
			itemdict['Sponsors'] = ""

		try:			
			itemdict['Contacts'] = str(   (Organization.objects.get(event=k) ).phone   )
		except:
			itemdict['Contacts'] = str(   (Organization.objects.get(event=k) ).phone   )



		tempx['SubItems'].append(itemdict)

	temp['Items'].append(tempx)

	for z in eve_cat:
		tempx={}
		tempx['UniqueId'] = str(z.name)
		tempx['Title'] = tempx['UniqueId']
		tempx['SubItems'] = []
		for e_ob in Event.objects.filter(category=z,is_displayed=True):
			itemdict= {}
			itemdict["UniqueId"] = (str(e_ob.name).replace(' ','') + str(e_ob.id)).encode('ascii','ignore')
			itemdict['Title'] = itemdict['UniqueId']
			itemdict['ImagePath'] = "Assets/"+ str(e_ob.name.replace(" ","").lower() ) + ".png"
			try:
				itemdict['Overview'] = str(   gaussx((Tab.objects.get(event=k, heading= overview_ob) ).content )   )
			except:
				itemdict['Overview'] = ""
			try:
				itemdict['Rules'] = str(   gaussx((Tab.objects.get(event=k, heading= rules_ob ) ).content )   )
			except:
				itemdict['Rules'] = ""

			try:			
				itemdict['Eligibility'] = str(   gaussx((Tab.objects.get(event=k, heading= eligibility_ob) ).content )   )
			except:
				itemdict['Eligibility'] = ""

			try:			
				itemdict['Guidelines'] = str(   gaussx((Tab.objects.get(event=k, heading= guidelines_ob ) ).content )   )
			except:
				itemdict['Guidelines'] = ""

			try:			
				itemdict['Judging Criteria'] =str(    gaussx((Tab.objects.get(event=k, heading= judging_ob) ).content )   )
			except:
				itemdict['Judging Criteria'] =""

			try:			
				itemdict['Problem Statements'] = str(    gaussx((Tab.objects.get(event=k, heading= prob_ob)  ).content )  )
			except:
				itemdict['Problem Statements'] = ""


			try:			
				itemdict['Resources'] = str(   gaussx((Tab.objects.get(event=k, heading=resources_ob) ).content )   )
			except:
				itemdict['Resources'] = ""

			try:
				itemdict['Sample Questions'] =str( gaussx((Tab.objects.get(event=k, heading= sampleq_ob) ).content )   )
			except:
				itemdict['Sample Questions'] =""

			try:			
				itemdict['Specifications'] = str(  gaussx((Tab.objects.get(event=k, heading= specifications_ob) ).content )   )
			except:
				itemdict['Specifications'] = ""

			try:			
				itemdict['Materials'] = str(   gaussx((Tab.objects.get(event=k, heading= materials_ob) ).content )   )
			except:
				itemdict['Materials'] = ""

			try:			
				itemdict['Registration Details'] = str(   gaussx((Tab.objects.get(event=k, heading= regdetails_ob) ).content )   )
			except:
				itemdict['Registration Details'] = ""

			try:			
				itemdict['FAQs'] = str(   gaussx((Tab.objects.get(event=k, heading= faqs_ob) ).content )   )
			except:
				itemdict['FAQs'] = ""

			try:			
				itemdict['Sponsors'] = str(   gaussx((Tab.objects.get(event=k, heading= sponsors_ob) ).content )   )
			except:
				itemdict['Sponsors'] = ""

			try:			
				itemdict['Contacts'] = str(   (Organization.objects.get(event=k) ).phone   )
			except:
				itemdict['Contacts'] = str(   (Organization.objects.get(event=k) ).phone   )
			
			tempx['SubItems'].append(itemdict)
		temp['Items'].append(tempx)

	resp['Groups'].append(temp)

	



#############################################################################################
############### events end here : apart from events,(notable speakers n all) ################
#############################################################################################





	resp['Groups'].append(temp)

	return HttpResponse(json.dumps(resp), content_type="application/json")