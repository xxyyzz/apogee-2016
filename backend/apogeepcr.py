from django.http import HttpResponse
from registration.models import *
from barg import code128_image
from django.template import Context
from django.shortcuts import get_object_or_404, render_to_response, render
#import GifImagePlugin
import sys
from django.template import RequestContext
from django.template.loader import get_template
from django.views.static import serve
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail, EmailMessage
import pyPdf
import string
from random import randint
import shutil
import pdfkit
import os
from django.views.decorators.csrf import csrf_exempt
sys.path.append('/home/dvm/taruntest/')
sys.path.append('/home/dvm/taruntest/bosm2015/')


def gen_barcode(gl_id):
	gl_ida = '0'*(4-len(str(gl_id)))+str(gl_id)
	mixed = string.ascii_uppercase + string.ascii_lowercase
	count = 51
	encoded = ''
	for x in gl_ida:
		encoded = encoded + x
		encoded = encoded + mixed[randint(0,51)]
#	gl_ida = '6'
	#image='/home/dvm/taruntest/%s.gif' % str(gl_id)
	image='/home/dvm/bosm/public_html/taruntest/satwik_bosmcode/%s.gif' % str(gl_id)
	code128_image(encoded).save(image)
	return encoded


def write_pdf(gl_id,encoded):
	gl = UserProfile.objects.get(id=gl_id)
	gl_name = gl.details.name
	participant_list_temp = gl.initialregistration_set.filter(pcr_approval=True).order_by('name')
	participant_list = [x for x in participant_list_temp if x.confirmed_events.count() != 0]
	no_of_males = len([x for x in participant_list if str(x.gender) == 'M' or str(x.gender) == 'male'])
	no_of_females = len(participant_list)-no_of_males
	college = gl.details.college
	barcode_name = str(gl_id)+'.gif'
	plist_tab1 = []
	linear_list = []
	#linear_list = [((str(p.name ) + '    (' + str(p.gender)[0].upper() + ')'),str(p.events.all()[0].name)) for p in participant_list]
	for p in participant_list:
		x = str(p.name ) + '    (' + str(p.gender)[0].upper() + ')'
		if len(p.confirmed_events.all()):
			# y = ",".join([x.name for x in p.events.all()])
			# y= p.events.all()[0].name
			# if len(p.events.all()) < 5:
			y = ",".join([str(z.name) for z in p.confirmed_events.all()])
			# else:
				# y = ",".join([str(z.name) for z in p.events.all()[:5]]) + '...'
		elif p.is_faculty:
			y = 'Faculty in charge'
		else:
			y = ''
		linear_list.append((x,y))

	if len(linear_list)%2 != 0:
		linear_list.append(('',''))					#appending extra for symmetric table format

	glen = len(linear_list)

	# if len(linear_list)<=50:						#implies every detail can fit in one page
		#template = get_template('pisatest.html')
	first_half = linear_list[:len(linear_list)/2]
	second_half = linear_list[len(linear_list)/2:]
	plist_tab = []										#participant list for tabular format
	for x in range(0,len(first_half)):
		plist_tab.append((first_half[x],second_half[x]))
	context = Context({'encoded':encoded,'plist_tab':plist_tab,'barcode_name':barcode_name,'gl_name' : gl_name, "college" : college})
	# html = template.render(context)
	# #result = open('/home/dvm/taruntest/%s.pdf' %(str(gl_id)), 'wb')
	# #pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
	# #result.close()

	template = get_template('registration/singlepageoasis.html')
	html = template.render(context)
	text_file = open("/home/dvm/taruntest/apogee/output.html", "w")			#temporary only 
	# text_file = open("/home/gauss/DVM Github/oasis2015/output.html", "w")			#temporary only 
	text_file.write(html)
	text_file.close()
	pdfkit.from_file('/home/dvm/taruntest/apogee/output.html', '/home/dvm/taruntest/apogee/%s.pdf' %(str(gl_id)))


	'''
	participant_list_formatted_n = [str(p.name ) for p in participant_list]
	participant_list_formatted_e = [str(p.events.all()[0].name) for p in participant_list]
	template_list1_n = participant_list_formatted_n[len(participant_list_formatted_n)/2:]
	template_list1_e = participant_list_formatted_e[len(participant_list_formatted_e)/2:]
	template_list2_n = participant_list_formatted_n[:len(participant_list_formatted_n)/2]
	template_list2_e = participant_list_formatted_e[:len(participant_list_formatted_e)/2]
	'''
	
	return html


def myview(request):
	z = write_pdf(44)
	gen_barcode(44)
	return HttpResponse(z)

#@staff_member_required
def pcr_pdf2(request,gl_id):
	id_list = gl_id
	for x in id_list:
		encoded = gen_barcode(x)
		write_pdf_2(x,encoded)
	return HttpResponse('operations completed for id %s' % gl_id)

def pcr_pdf(request, gl_id):
	encoded = gen_barcode(gl_id)
	write_pdf(gl_id,encoded)
#	return HttpResponse('operations completed for id %s' % gl_id)
	return serve(request, os.path.basename('/home/dvm/taruntest/%s.pdf' % gl_id), os.path.dirname('/home/dvm/taruntest/%s.pdf' % gl_id))
def email_participant2(request):
	id_list = [15, 21, 34, 39, 44, 46, 53, 55, 60, 65, 94, 106, 119, 127, 130, 132, 139, 141, 147, 148, 150, 158, 164, 165, 170, 188, 189, 198, 234, 265, 267, 268, 270, 298, 299] #gl_id list here
	s = ''
	for x in id_list:
		our_user = UserProfile.objects.get(id=x)
		send_to = str(our_user.user.email)
		college = str(our_user.college.name)
		body = ''' body here '''
		attachment = '/home/dvm/taruntest/%s.pdf' % x
		a_name = 'BOSM'+str(randint(9901,99000))
		shutil.copy2(attachment, '/home/dvm/taruntest/%s.pdf' % a_name)
		email = EmailMessage('BITS BOSM Barcode', body, 'reachtarunhere@gmail.com', [send_to])
		email.attach_file('/home/dvm/taruntest/%s.pdf' % a_name)
		email.send()
		s += str(x)+' '
	return HttpResponse(s)







def email_participant(request,gl_id):
	our_user = UserProfile.objects.get(id=gl_id)
	send_to = str(our_user.user.email)
	college = str(our_user.details.college)
	inchaarge = str(our_user.details.name)
	if inchaarge is None:
		return HttpResponse("Please assign an incharge first")
#	participant_list = our_user.user.participant_set.all()
	# user_ob = our_user.UserProfile
	participant_list = InitialRegistration.objects.filter(pcr_approval= True, college_rep= our_user)
	no_of_males = len([x for x in participant_list if str(x.gender) == 'male' or str(x.gender) == 'M'])
	no_of_females = len(participant_list)-no_of_males
	body = '''
Hello!

It is our immense pleasure to confirm your college's participation at Oasis '15 - Around the World in 96 Hours. Kudos to your co-operation along the whole process - it was indeed an endeavour - an endeavour we hope is worth it and you have an Oasis you remember for years to come.

Please find attached the list of confirmed participants along with
their events, and note that only these participants will be allowed to
enter the campus.

College : %s
Total no. of boys :%s
Total no. of girls : %s
College Representative : %s

We require little bit of paper-work from your side regarding bona fide certificates. Check out http://bits-oasis.org/2015/registrationdetails
1. Follow the ID requirements in the link here. Follow these guidelines faithfully to ensure hassle free entry into campus, especially regarding the bona fide certificates.
[Please note that failure to will result in refusal of entry at the campus gate]
2. Peruse the Security and Safety Instructions in the link given. The guidelines will be strictly enforced and you are liable to be thrown out of the campus in case of non-compliance.
3. Peruse the Travel document in the link above. 
4. Peruse the Accommodation document in the link above.
5. You are automatically considered in the running for the titular event of the fest-Mr. and Ms. Oasis-if you are participating in any of the events showcasign art forms like music, dance etc. Taking place on the midnight of 31st October, it is your chance to stand out as the brightest in the midst of immense talent and to etch your name alongside that of this Oasis. Participants are selected on the basis of their college performances during their respective events. 


For any clarifications call your assigned BITS point-of-contact.

Good Luck. See you on campus!
-- 
Maheep Tripathi
StuCCAn (Head)
Dept. of Publications & Correspondence
Oasis '15-Around the World in 96 Hours 
BITS, Pilani

''' % (college,no_of_males,no_of_females,inchaarge+", "+str(our_user.details.phone_one))
	attachment = '/home/dvm/taruntest/apogee/%s.pdf' % gl_id
	a_name = 'Oasis'+str(randint(9901,99000))
	shutil.copy2(attachment, '/home/dvm/taruntest/apogee/%s.pdf' % a_name)
	email = EmailMessage('BITS Oasis', body, 'invitation@bits-oasis.org', [send_to])
	email.attach_file('/home/dvm/taruntest/apogee/%s.pdf' % a_name)
	# email.attach_file('/home/dvm/taruntest/apogee/BOSM_checklist.pdf')
	email.send()
	#send_mail('BOSM 2014 Registration', 'Here is the message.', 'reachtarunhere@gmail.com',[send_to], fail_silently=False)
	return HttpResponse('mail sent')

@staff_member_required
def generate_pdf(request, gl_id):
	our_participant = UserProfile.objects.get(id=gl_id)
	if not our_participant.barcode:
		encoded = gen_barcode(gl_id)
		our_participant.barcode = encoded
		our_participant.save()
	else:
		encoded = our_participant.barcode
	write_pdf(gl_id,encoded)
	return HttpResponse('generation sucessful')

@staff_member_required
def view_pdf(request, gl_id):
	#first generating
	our_participant = UserProfile.objects.get(id=gl_id)
	if not our_participant.barcode:
		encoded = gen_barcode(gl_id)
		our_participant.barcode = encoded
		our_participant.save()
	else:
		encoded = our_participant.barcode
	write_pdf(gl_id,encoded)
	return serve(request, os.path.basename('/home/dvm/taruntest/apogee/%s.pdf' % gl_id), os.path.dirname('/home/dvm/taruntest/apogee/%s.pdf' % gl_id))




@staff_member_required
def pcr_act(request):
	crep_ob = UserProfile.objects.all()
	crep_list=[]
	for k in crep_ob:
		if k.initialregistration_set.all().count():
			crep_list.append(k)
	# crep_list = []
	# for gl in big_list:
	# 	if gl.user and len(gl.user.participant_set.all()):
	# 		crep_list.append(gl)
	# crep_list = crep_list.order_by('-college')
	context = RequestContext(request)
	context_dict = {'crep_list':crep_list}
	return render_to_response('registration/pcractx.html', context_dict, context)










@csrf_exempt
def get_pdf(request):
	if request.user.is_authenticated():
		try:
			our_participant = request.user.participant_set.all()[0]
		except:
			return HttpResponse('Invalid user')
	gl_id = our_participant.id
	if not our_participant.barcode:
		encoded = gen_barcode(gl_id)
		our_participant.barcode = encoded
		our_participant.save()
	else:
		encoded = our_participant.barcode
	write_pdf(gl_id,encoded)
	return serve(request, os.path.basename('/home/dvm/taruntest/apogee/%s.pdf' % gl_id), os.path.dirname('/home/dvm/taruntest/apogee/%s.pdf' % gl_id))




def xlsx(request):
	from django.http import HttpResponse, HttpResponseRedirect  
	import xlsxwriter

	try:  
	    import cStringIO as StringIO
	except ImportError:  
	    import StringIO
	a_list = []

	from registration.models import Participant
	participants = Participant.objects.filter(controlzpay=True)

	for p in participants:
		p.college = p.gleader.userprofile_set.last().college
		elist = [event.name for event in p.events.all()]
		elist1=[]
		for t in elist:
			if 'BOYS' in t.upper():
				t = t.upper()
				t = t[:t.find(" (BOYS)")]
				elist1.append(t.title())
			elif 'GIRLS' in t.upper():
				t = t.upper()
				t = t[:t.find(" (GIRLS)")]
				elist1.append(t.title())
			else: 
				elist1.append(t)

		p.event = ",".join(elist1)
		a_list.append({'obj': p})
	data = sorted(a_list, key=lambda k: k['obj'].college)
	output = StringIO.StringIO()
	workbook = xlsxwriter.Workbook(output)
	worksheet = workbook.add_worksheet('new-spreadsheet')
	date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})
	for i, row in enumerate(data):
	    """for each object in the date list, attribute1 & attribute2
	    are written to the first & second column respectively,
	    for the relevant row. The 3rd arg is a failure message if
	    there is no data available"""

	    worksheet.write(i, 0, i+1)
	    worksheet.write(i, 1, getattr(row['obj'], 'name', 'attribute1 not available'))
	    worksheet.write(i, 2, getattr(row['obj'], 'gender', 'attribute2 not available'))
	    worksheet.write(i, 3, getattr(row['obj'], 'phone', 'attribute1 not available'))
	    worksheet.write(i, 4, getattr(row['obj'], 'event', 'attribute1 not available'))
	    worksheet.write(i, 5, getattr(row['obj'], 'college', 'attribute1 not available'))
	workbook.close()
	filename = 'ExcelReport.xlsx'
	output.seek(0)
	response = HttpResponse(output.read(), content_type="application/ms-excel")  
	response['Content-Disposition'] = 'attachment; filename=%s' % filename
	return response



