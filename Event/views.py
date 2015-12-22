# from django.http import HttpResponse, Http404, JsonResponse
# from django.core.exceptions import ObjectDoesNotExist
# from events.models import Event, Category, Notification
# from django.views.decorators.csrf import csrf_exempt
# import json
# import html2text as gaussx
# # Create your views here.
# @csrf_exempt
# def geteventdata(request, event_id):
#     try:
#         eventid = event_id
#     except :
#         raise Http404
#     try :
#         event=Event.objects.get(pk=eventid)
#     except ObjectDoesNotExist:
#         raise Http404
#     resp = {}
    
#     # resp['category']=unicode(event.category.name)
#     resp['content']=str(unicode(event.content))
#     resp['eventname']=str(unicode(event.name))
#     resp['eventcategory']=str(unicode(event.category.name))
#     resp['date']=    str( unicode( event.date ))
#     resp['time']=   str(  unicode(event.time ) )
#     resp['eventcontent']= str(unicode(event.content))
#     resp['venue']=    str  (unicode(event.venue) )
#     resp['eventdescription']=unicode(event.description)
#     resp['eventshortdescription']=unicode(event.short_description)
#     return JsonResponse(resp)

# @csrf_exempt
# def summary(request):
#     response = []
#     categories = Category.objects.all()
#     categories = [x for x in categories if x.name != "Other"]
#     for category in categories:
#         container = {}
#         container['category'] = category.name
#         eventlist = {}
#         events = [{'id':event.id, 'name':event.name, 'is_kernel':event.is_kernel} for event in category.event_set.all()]
#         container['events'] = events
#         response.append(container)
#     return JsonResponse(response, safe=False)

# @csrf_exempt
# def getcategoryevents(request):
#     if request.GET:
#         data=request.GET
#         name=data['category']
#         try:
#             c=Category.objects.get(name=name)
#         except :
#             raise Http404
#         eset= Event.objects.filter(category = c)
#         resp={}
#         resp['Events']=[]
#         for e in eset :
#             dic={}
#             dic['eventid']=int(e.id)
#             dic['eventname']=str(unicode(e.name))
#             dic['eventcategory']=str(unicode(e.category.name))
#             dic['date']=    str( unicode( e.date ))
#             dic['time']=   str(  unicode(e.time ) )
#             dic['eventcontent']= str(unicode(e.content))
#             dic['venue']=    str  (unicode(e.venue) )
#             if e.icon:
#                 dic['eventicon']=str(e.icon.url)
#             else :
#                 dic['eventicon']=''
#             dic['eventdescription']=unicode(e.description)
#             dic['eventshortdescription']=unicode(e.short_description)
#             resp['Events'].append(dic)
#         # json = simplejson.dumps(resp)
#         # return HttpResponse(json, mimetype='application/json')
#         return HttpResponse(json.dumps(resp), content_type="application/json")
#     else:
#         raise Http404
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

