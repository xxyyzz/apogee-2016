# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from registrations.models import *
from Event.models import *
from backend.models import *
# from events.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import Context
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth import login, logout
from django.contrib import auth
from django.db.models import F
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect

import difflib

from django.core.mail.backends.smtp import EmailBackend
cabackend = EmailBackend(
    host='smtp.mailgun.org',
    port=587,
    username='noreply@mg.bits-apogee.org',
    password='donotreplybc',
    use_tls=True,
    fail_silently=False,
)


def initial_registration(request):
	init_reg = InitialRegistration.objects.all()
	return render(request,'pcradmin/init_reg.html', {'init_reg' : init_reg })




@staff_member_required
def dashboard2(request):
	return HttpResponseRedirect('./dashboard/')

@staff_member_required
def dashboard(request):
	return render(request, 'pcradmin/dashboard.html')

def pcr_logout(request):
	logout(request)
	return redirect('http://bits-apogee.org/2016/pcradmin/dashboard/')



def part_list(request):
	part_obs = Participant.objects.all()
	# amb_list=[]
	# collegelist = [x.name for x in College.objects.filter(is_displayed=True)]
	return render(request, 'pcradmin/part_list.html', {'part_list' : part_obs})



def part_act(request):
	part_obs = Participant.objects.all()


	body = unicode(u''' ''')


	part_ids = request.POST.getlist('part_list')
	if part_ids:
		no_select=0
	else:
		return render(request,'pcradmin/part_list.html',{'part_list' : part_obs, 'no_select' : 1})

	if request.POST.get('approval', False):
		val = request.POST['approval']
		val =int(val)
		if val == 2:
			send_to= []
			for i in part_ids:
				aid = int(i)
				try:
					part= Participant.objects.get(id=aid)
				except:
					return HttpResponse('Error : Call Satwik 9928823099')
				if part.pcr_approval == True:
					continue
				part.pcr_approval= True
				part.save()
				send_to.append( str( part.email_id) )

			# try:
			# 	email = EmailMessage("PCR Approval", body, 'no-reply@bits-apogee.org', send_to, connection=cabackend)
			# #poster attachment
			# # email.attach_file('/home/dvm/oasis/oasis2015/attachments/Oasis 2015 Communique.docx')
			# #email.attach_file('/home/dvm/taruntest/oasisattach/Oasis 2014 Posters.pdf')
			# #email.attach_file('/home/dvm/taruntest/oasisattach/Rules Booklet Oasis 2014.pdf')
			# 	email.send()
			# 	return render(request, 'pcradmin/showmailsent.html')
			# except:
			# 	return HttpResponse(' Email Error: Call Satwik 9928823099 ')

		elif val == 1:
			for i in part_ids:
				aid = int(i)
				try:
					part= Participant.objects.get(id=aid)
				except:
					return HttpResponse('Error : Call Satwik 9928823099')
				part.pcr_approval= False
				part.save()
		else:
			return HttpResponse('Error: Decision Value didnt match;   Call Satwik 9928823099  :    ' + str(part_ids) + ' | ' + str(val))


		return HttpResponseRedirect('../part_list/')

	# elif request.POST['mail']:
	# 	id_str = ','.join(part_ids)
	# 	mailbody = 'Default mail body'
	# 	gauss_check= 0
	# 	context = {
	# 	'mailbody' :mailbody,
	# 	'id_str' : id_str,
	# 	}
	# 	return render(request, 'pcradmin/mail_selected_amb.html', context)















def ambassadors_list(request):
	amb_obs = CampusAmbassador.objects.all()
	# amb_list=[]
	# collegelist = [x.name for x in College.objects.filter(is_displayed=True)]
	return render(request, 'pcradmin/list_ambassadors.html', {'amb_list' : amb_obs})

def app_amb(request):
	amb_obs = CampusAmbassador.objects.filter(pcr_approved=True)
	# amb_list=[]
	# collegelist = [x.name for x in College.objects.filter(is_displayed=True)]
	return render(request, 'pcradmin/approved_amb.html', {'amb_list' : amb_obs})

def amb_act(request):
	amb_obs = CampusAmbassador.objects.all()


	body = unicode(u'''Hello,

Greetings from Team APOGEE- BITS Pilani!

APOGEE is the annual technical festival of BITS Pilani. For its promotion in other colleges, we have joined hands with the internship platform YOUTH4WORK to recruit Marketing Interns. As a part of the process, you were called and told the about the work (in a broader fashion).

This is to inform you that you have been selected as a Marketing Intern for APOGEE 2016. You are now a part of APOGEE and YOUTH4WORK family and we expect you to work towards making it a grand success. However, there will be a great influx of responsibilities on your shoulders. We expect you to put in sincere efforts from your side. You will be in touch with one of our members via phone and email periodically.


Incentives:

1. Marketing Intern Certificate by Youth4work for 2 months is a valuable deliverable by a renowned internship platform. This recognition will specially be helpful for people looking to sit for placements in the future.

2. Based on your performance and how much participation you are able to bring, your registration fee may be waivered upto an extent/completely.

3. For Exceptional performances, be ready for goodies by Youth4work and APOGEE!


The following are expected from you promptly:

1. Please Pre-register and help your friends pre-register on https://www.bits-apogee.org/ .

2. Please reply to pcr@bits-apogee.org with the e-mail address and contact numbers of the NSS head in your college along with the Mechanical, Computer Science and Electrical departments’ (if any) student representatives.

3. You are expected to share the posts uploaded on the APOGEE Facebook page https://www.facebook.com/bitsapogee ; it will be monitored by one of our members.

4. Please subscribe on Youth4Work (website) if you haven’t till now (otherwise you will be not be a recognized Intern).

5. From announcing in classrooms and sending out mails to meeting various heads of participating teams, do all that which ensures participation in the events (whose posters will be sent out to you). Any other idea from you will always be received with a great pleasure.


To begin with, we require you to like the APOGEE Facebook page to keep yourself updated and also pre-register yourself on the APOGEE website www.bits-apogee.org. From now onwards, you will be regularly updated with your responsibilities via email. Do let us know if you have any suggestions specifically for your college that might help all of us spread the word about APOGEE and ensure healthy participation in a better way.

We wish you a grand success in this endeavor. Let's make APOGEE a grand success together.


Good Luck! ''')


	amb_ids = request.POST.getlist('amb_list')
	if amb_ids:
		no_select=0
	else:
		return render(request,'pcradmin/list_ambassadors.html',{'amb_list' : amb_obs, 'no_select' : 1})

	if request.POST.get('approval', False):
		val = request.POST['approval']
		val =int(val)
		if val == 2:
			send_to= []
			for i in amb_ids:
				aid = int(i)
				try:
					amb= CampusAmbassador.objects.get(id=aid)
				except:
					return HttpResponse('Error : Call Satwik 9928823099')
				if amb.pcr_approved == True:
					continue
				amb.pcr_approved= True
				amb.save()
				send_to.append( str( amb.email) )

			try:
				email = EmailMessage("Campus Ambassador Approval", body, 'no-reply@bits-apogee.org', send_to, connection=cabackend)
			#poster attachment
			# email.attach_file('/home/dvm/oasis/oasis2015/attachments/Oasis 2015 Communique.docx')
			#email.attach_file('/home/dvm/taruntest/oasisattach/Oasis 2014 Posters.pdf')
			#email.attach_file('/home/dvm/taruntest/oasisattach/Rules Booklet Oasis 2014.pdf')
				email.send()
				return render(request, 'pcradmin/showmailsent.html')
			except:
				return HttpResponse(' Email Error: Call Satwik 9928823099 ')

		elif val == 1:
			for i in amb_ids:
				aid = int(i)
				try:
					amb= CampusAmbassador.objects.get(id=aid)
				except:
					return HttpResponse('Error : Call Satwik 9928823099')
				amb.pcr_approved= False
				amb.save()
		else:
			return HttpResponse('Error: Decision Value didnt match;   Call Satwik 9928823099  :    ' + str(amb_ids) + ' | ' + str(val))


		return HttpResponseRedirect('../ambassadors/')

	elif request.POST['mail']:
		id_str = ','.join(amb_ids)
		mailbody = 'Default mail body'
		gauss_check= 0
		context = {
		'mailbody' :mailbody,
		'id_str' : id_str,
		}
		return render(request, 'pcradmin/mail_selected_amb.html', context)




def mail_selected_amb(request):
	id_str = request.POST.get('id_str', False)
	amb_ids = id_str.split(',')
	body = str( request.POST.get('body' , '') )

	send_to= []
	for k in amb_ids:
		aid = int(k)
		amb = CampusAmbassador.objects.get(id= aid)
		send_to.append( str( amb.email) )

	# try:
	email = EmailMessage(subject="Campus Ambassador", body=body, from_email='no-reply@bits-apogee.org', to=send_to, connection=cabackend)
	#poster attachment
	# email.attach_file('/home/dvm/oasis/oasis2015/attachments/Oasis 2015 Communique.docx')
	#email.attach_file('/home/dvm/taruntest/oasisattach/Oasis 2014 Posters.pdf')
	#email.attach_file('/home/dvm/taruntest/oasisattach/Rules Booklet Oasis 2014.pdf')
	email.send()
	return render(request, 'pcradmin/showmailsent.html')
	# except:
	# 	return HttpResponse('Mail to selected Ambassadors Error : Contact Satwik 9928823099')


def mail_approved(request):
	amb_list = CampusAmbassador.objects.filter(pcr_approved=True)
	if request.POST:
		body = str(request.POST['body'])
		send_to = []
		for amb in amb_list:
			send_to=[]
			send_to.append( str(amb.email) )
			try:
				email = EmailMessage("Campus Ambassador", body, 'no-reply@bits-apogee.org', send_to, connection=cabackend)
				email.send()
			#poster attachment
			# email.attach_file('/home/dvm/oasis/oasis2015/attachments/Oasis 2015 Communique.docx')
			#email.attach_file('/home/dvm/taruntest/oasisattach/Oasis 2014 Posters.pdf')
			#email.attach_file('/home/dvm/taruntest/oasisattach/Rules Booklet Oasis 2014.pdf')
			except:
				return HttpResponse('Mail Error : Contact Satwik 9928823099')
		return render(request, 'pcradmin/showmailsent.html')

	else:
		mailbody = 'Default mail body'
		gauss_check= 0
		if CampusAmbassador.objects.filter(pcr_approved=True):
			gauss_check= 1
		context = {
		'mailbody' :mailbody,
		'gauss_check' : gauss_check
		}
		return render(request, 'pcradmin/mail_amb.html', context)



def stats_ambassadors(request):
	total_amb = CampusAmbassador.objects.all().count()
	app_amb = CampusAmbassador.objects.filter(pcr_approved=True).count()
	amb_stats = str(total_amb)+ " | " +str(app_amb)
	context= {
	'amb_stats' : amb_stats,
	}
	return render(request,'pcradmin/amb_stats.html', context)






def deepgetattr(obj, attr, default = None):
    """
    Get a named attribute from an object; multi_getattr(x, 'a.b.c.d') is
    equivalent to x.a.b.c.d. When a default argument is given, it is
    returned when any attribute in the chain doesn't exist; without
    it, an exception is raised when a missing attribute is encountered.

    """
    attributes = attr.split(".")
    for i in attributes:
        try:
            obj = getattr(obj, i)
        except AttributeError:
            if default:
                return default
            else:
                raise
    return obj





def ambassador_approved_xlsx(request):
	from django.http import HttpResponse, HttpResponseRedirect
	import xlsxwriter
	from registrations.models import CampusAmbassador
	# if request.POST:
	try:
	    import cStringIO as StringIO
	except ImportError:
	    import StringIO
	a_list = []


	entries = CampusAmbassador.objects.filter(pcr_approved=True)

	for p in entries:
	    a_list.append({'obj': p})
	data = sorted(a_list, key=lambda k: k['obj'].id)
	output = StringIO.StringIO()
	workbook = xlsxwriter.Workbook(output)
	worksheet = workbook.add_worksheet('new-spreadsheet')
	date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})
	worksheet.write(0, 0, "Generated:")
	from time import gmtime, strftime
	generated = strftime("%d-%m-%Y %H:%M:%S UTC", gmtime())
	worksheet.write(0, 1, generated)

	worksheet.write(1, 0, "ID")
	worksheet.write(1, 1, "Name")
	worksheet.write(1, 2, "College")
	worksheet.write(1, 3, "Degree")
	worksheet.write(1, 4, "Year")
	worksheet.write(1, 5, "Phone")
	worksheet.write(1, 6, "Email")
	worksheet.write(1, 7, "Description")
	worksheet.write(1, 8, "Root Mail")
	worksheet.write(1, 9, "PCR Approved")

	for i, row in enumerate(data):
	    """for each object in the date list, attribute1 & attribute2
	    are written to the first & second column respectively,
	    for the relevant row. The 3rd arg is a failure message if
	    there is no data available"""

	    worksheet.write(i+2, 0, deepgetattr(row['obj'], 'id', 'NA'))
	    worksheet.write(i+2, 1, deepgetattr(row['obj'], 'name', 'NA'))
	    worksheet.write(i+2, 2, deepgetattr(row['obj'], 'college.name', 'NA'))
	    worksheet.write(i+2, 3, deepgetattr(row['obj'], 'degree', 'NA'))
	    worksheet.write(i+2, 4, deepgetattr(row['obj'], 'year', 'NA'))
	    worksheet.write(i+2, 5, deepgetattr(row['obj'], 'phone', 'NA'))
	    worksheet.write(i+2, 6, deepgetattr(row['obj'], 'email', 'NA'))
	    worksheet.write(i+2, 7, deepgetattr(row['obj'], 'ambassador_quality', 'NA'))
	    worksheet.write(i+2, 8, deepgetattr(row['obj'], 'root_mail', 'NA'))
	    worksheet.write(i+2, 9, deepgetattr(row['obj'], 'pcr_approved', 'NA'))

	workbook.close()
	filename = 'ExcelReport.xlsx'
	output.seek(0)
	response = HttpResponse(output.read(), content_type="application/ms-excel")
	response['Content-Disposition'] = 'attachment; filename=%s' % filename
	return response
	# amb_obs = CampusAmbassador.objects.all()
	# return render(request, 'pcradmin/xlsx_ambassadors.html', {'amb_list' : amb_obs})



@staff_member_required
def stats_event(request):
	events = [x for x in Event.objects.order_by('name') if x.category.name != "Other"]
	college = College.objects.all()
	eventwise = []
	for event in events:
		entry = {}
		entry['id'] = event.id
		entry['name'] = event.name
		entry['category'] = str(event.category.name) 
		entry['males'] = str(event.participant_set.filter(gender='M', college=college).count())+' | '+str(event.participant_set.filter(gender='M', pcr_approval=True).count())
		entry['females'] = str(event.participant_set.filter(gender='F').count())+' | '+str(event.participant_set.filter(gender='F', pcr_approval=True).count())
		entry['total'] = str(event.participant_set.filter(college=college).count())+' | '+str(event.participant_set.filter(pcr_approval=True).count())
		for key, value in entry.iteritems():
			if type(value) is str:
				if value == '0 | 0 | 0':
					entry[key] = value.replace('0 | 0 | 0', '---')
		eventwise.append(entry)
	total = {}
	total['males'] = str(Participant.objects.filter(gender='M').count())+' | '+str(Participant.objects.filter(gender='M', pcr_approval=True).count())
	total['females'] = str(Participant.objects.filter(gender='F').count())+' | '+str(Participant.objects.filter(gender='F', pcr_approval=True).count())
	total['total'] = str(Participant.objects.all().count())+' | '+str(Participant.objects.filter(pcr_approval=True).count())

	total_amb = CampusAmbassador.objects.all().count()
	app_amb = CampusAmbassador.objects.filter(pcr_approved=True).count()
	amb_stats = str(total_amb)+ " | " +str(app_amb)
	# context= {
	# 'amb_stats' : amb_stats,
	# }


	context = {
		# 'college' : college,
		'eventwise' : eventwise,
		'total' : total,
		'amb_stats' : amb_stats,

	}
	return render(request, 'pcradmin/apogee_stats.html', context)
################################################################





















# ### old code below

# # Create your views here.
# def home(request):
# 	return redirect('dashboard/',)
# @staff_member_required
# def pathfinder(request, pagename):
# 	users = User.objects.all()
# 	return render(request, 'pcradmin/'+pagename+'.html', {'users' : users})


# # @staff_member_required
# # def username_select(request):
# # 	users = initialregistration.objects.all()
# # 	context = {
# # 		'users' : users
# # 	}
# # 	return render(request, 'pcradmin/username_select.html', context)

# @staff_member_required
# def init_list(request):
# 	if request.method == 'POST':
# 		clg = str(request.POST['college'])

# 		users = InitialRegistration.objects.filter(college=clg)
# 		context = {
# 			'users' : users

# 		}
# 		return render(request, 'pcradmin/init_select.html', context)

# @staff_member_required
# def college_select(request):
# 	college_ob = College.objects.filter(is_displayed = True)
# 	clist = [x.name for x in college_ob]
# 	initreg = InitialRegistration.objects.all()
# 	clg_list = []
# 	for t in clist:
# 		if InitialRegistration.objects.filter(college = t):
# 			k = InitialRegistration.objects.filter(college = t)[0]

# 			if k.college_rep:
# 				clg_list.append((k.college, 'Selected' ))
# 			else:
# 				clg_list.append((k.college, 'Not Selected'))

# 	context = {
# 		'clg_list' : clg_list
# 	}
# 	return render(request, 'pcradmin/college_select.html', context)



# @staff_member_required
# def view_Crep(request, user_id):
# 	user = InitialRegistration.objects.get(pk=user_id)

# 	context = {
# 		'user' : user
# 	}
# 	return render(request, 'pcradmin/view_crep.html', context)



# @staff_member_required
# def Crep_save(request, user_id):
# 	crep = InitialRegistration.objects.get(pk=user_id)

# 	if request.method == "POST":
# 		if request.POST.get('set_rep', False):
# 			college = crep.college

# 			if crep.college_rep:
# 				user_ob = crep.college_rep.user





# 			# if crep.college_rep == None:
# 			if (User.objects.filter(email = crep.email_id) ):
# 				newuser = User.objects.get(email = crep.email_id)
# 				new_userp = UserProfile.objects.get(user = newuser)
# 			else:
# 				newuser = User.objects.create_user(crep.email_id, crep.email_id, crep.phone_one)
# 				crep_id = crep.id
# 				new_userp = UserProfile.objects.create(user= newuser, details_id = crep_id)


# 			newuser.save()
# 			new_userp.save()
# 			crep.college_rep = new_userp
# 			crep.save()


# 			members = InitialRegistration.objects.filter(college = college)
# 			for k in members:
# 				k.college_rep = crep.college_rep
# 				k.save()


# 			username =crep.email_id
# 			password= crep.phone_one
# 			body = unicode(u'''
# You have been selected as the college representative for your college.
# Your username is : %s
# Your password is : %s
# To view the information brochure of Oasis '15 click here: http://bits-oasis.org/2015/details/
# 		''' ) % (username, password)



# 			context = {
# 				'user' : crep,
# 				'mailbody' : body,
# 			}
# 			return render(request, 'pcradmin/crep_show.html', context)




# 		if request.POST.get('mail', False):
# 			username =crep.email_id
# 			password= crep.phone_one

# 			body = ''
# 			if request.POST.get('body', False):
# 				body = request.POST['body']
# 			else:
# 				body = unicode(u'''.
# 	You have been selected as the college representative for your college.
# 	Your username is : %s
# 	Your password is : %s
# 	To view the information brochure of Oasis '15 click here: http://bits-oasis.org/2015/details/
# 			''' ) % (username, password)


# 		send_to = username
# 		try:
# 			email = EmailMessage("College representative confirmation, Oasis'15", body, 'invitation@bits-oasis.org', [send_to])
# 			#poster attachment
# 			# email.attach_file('/home/dvm/oasis/oasis2015/attachments/Oasis 2015 Communique.docx')
# 			#email.attach_file('/home/dvm/taruntest/oasisattach/Oasis 2014 Posters.pdf')
# 			#email.attach_file('/home/dvm/taruntest/oasisattach/Rules Booklet Oasis 2014.pdf')
# 			email.send()
# 			return render(request, 'pcradmin/showmailsent.html')
# 		except:
# 			return HttpResponse('error')



# def crep_email(request,user_id):
# 	crep= InitialRegistration.objects.get(id =user_id)
# 	if crep.college_rep:
# 		username =crep.email_id
# 		password= crep.phone_one
# 		body = unicode(u'''
# You have been selected as the college representative for your college.
# Your username is : %s
# Your password is : %s
# To view the information brochure of Oasis '15 click here: http://bits-oasis.org/2015/details/
# 		''' ) % (username, password)

# 		context = {
# 			'user' : crep,
# 			'mailbody' : body,
# 		}
# 		return render(request, 'pcradmin/crep_email.html', context)
# 	else:
# 		return render(request, 'pcradmin/crep_email.html')







# @staff_member_required
# def std_list_college(request):
# 	dispcollege_ob = College.objects.filter(is_displayed = True)

# 	tocollege_ob = College.objects.filter(is_displayed = False)

# 	clg_list = []
# 	clist = [x.name for x in tocollege_ob]
# 	for k in tocollege_ob:
# 		no_rpart = InitialRegistration.objects.filter(college = k.name).count()
# 		if no_rpart == 0:
# 			continue
# 		clg_list.append( (k, no_rpart) )
# 	# initreg = InitialRegistration.objects.all()

# 	context = {
# 		'clg_list' : clg_list
# 	}
# 	return render(request, 'pcradmin/list_college.html', context)



# def stdview_college(request):
# 	dispcollege_ob = College.objects.filter(is_displayed=True)
# 	if request.method == 'POST':
# 		clg = request.POST['college']
# 		dispcollege_name = [str(x.name) for x in dispcollege_ob]
# 		clg_name = str(clg)
# 		pos_list = []
# 		pos_list = difflib.get_close_matches(clg_name, dispcollege_name)
# 		if len( clg_name.split(',')) == 2:
# 			clgstr1 = clg_name.split(',')[0].strip()
# 			newstr=''
# 			for k in clgstr1.split(' '):
# 				if k.upper() != 'OF' and k.upper() != 'AND':
# 					newstr= newstr + str(k[0].upper())
# 			newstr = newstr + str(clg_name.split(',')[1])
# 			newmatches = difflib.get_close_matches(newstr, dispcollege_name)
# 			pos_list = pos_list + newmatches


# 		context = {
# 			'clg_name' : clg_name,
# 			'pos_list' : pos_list,
# 			'clg_list' : dispcollege_ob
# 		}
# 	return render(request, 'pcradmin/stdview_college.html', context)



# def change_req(request):
# 	if request.method == "POST":
# 		if request.POST.get('newcollege', False):
# 			newclg = request.POST['newcollege']
# 			clgob = College.objects.get(name = newclg)
# 			clgob.is_displayed = True
# 			clgob.save()
# 			context = {
# 			'status' : 2
# 			}
# 			return render(request, 'pcradmin/changed_college.html', context)
# 		old_clg = request.POST['oldcollege']
# 		new_clg = request.POST['userSchool']
# 		init_ob = InitialRegistration.objects.filter(college = old_clg)
# 		if College.objects.filter(name = new_clg, is_displayed= True):
# 			init_ob_euler = InitialRegistration.objects.filter(college = new_clg)
# 			for k in init_ob:
# 				k.college = new_clg
# 				if init_ob_euler:
# 					if init_ob_euler[0].college_rep:
# 						k.college_rep = init_ob_euler[0].college_rep
# 				k.save()

# 		else:
# 			clg_create = College(name = new_clg, is_displayed=True)
# 			clg_create.save()
# 			for k in init_ob:
# 				k.college = new_clg
# 				k.save()

# 		context = {
# 			'status' : 1,
# 			'clg_name' : new_clg
# 		}
# 		return render(request, 'pcradmin/changed_college.html', context)




# ####stats views  #####



# @staff_member_required
# def stats_eventwise(request):
# 	events = [x for x in Event.objects.order_by('name') if x.category.name != "Other"]
# 	users = InitialRegistration.objects.all()
# 	colleges_init = College.objects.filter(is_displayed= True)
# 	colleges= []
# 	## SPORTWISE COUNTS
# 	eventwise = []
# 	for event in events:
# 		entry = {}
# 		entry['id'] = event.id
# 		entry['name'] = event.name
# 		entry['category'] = str(event.category.name)
# 		entry['males'] = str(event.initialregistration_set.filter(gender='M').count())+' | '+str(event.initialregistration_set.filter(gender='M', gl_approval=True).count())+' | '+str(event.initialregistration_set.filter(gender='M', pcr_approval=True).count())
# 		entry['females'] = str(event.initialregistration_set.filter(gender='F').count())+' | '+str(event.initialregistration_set.filter(gender='F', gl_approval=True).count())+' | '+str(event.initialregistration_set.filter(gender='F', pcr_approval=True).count())
# 		entry['total'] = str(event.initialregistration_set.all().count())+' | '+str(event.initialregistration_set.filter(gl_approval=True).count())+' | '+str(event.initialregistration_set.filter(pcr_approval=True).count())+' | '+str(event.initialregistration_set.filter(pcr_approval=True, confirmed_events__gte=1).distinct().count())
# 		for key, value in entry.iteritems():
# 			if type(value) is str:
# 				if value == '0 | 0 | 0':
# 					entry[key] = value.replace('0 | 0 | 0', '---')
# 		eventwise.append(entry)
# 	total = {}
# 	total['males'] = str(InitialRegistration.objects.filter(gender='M').count())+' | '+str(InitialRegistration.objects.filter(gender='M', gl_approval=True).count())+' | '+str(InitialRegistration.objects.filter(gender='M', pcr_approval=True).count())
# 	total['females'] = str(InitialRegistration.objects.filter(gender='F').count())+' | '+str(InitialRegistration.objects.filter(gender='F', gl_approval=True).count())+' | '+str(InitialRegistration.objects.filter(gender='F', pcr_approval=True).count())
# 	total['total'] = str(InitialRegistration.objects.all().count())+' | '+str(InitialRegistration.objects.filter(gl_approval=True).count())+' | '+str(InitialRegistration.objects.filter(pcr_approval=True).count())+' | '+str(InitialRegistration.objects.filter(pcr_approval=True, confirmed_events__gte=1).distinct().count())

# 	for gauss in colleges_init:
# 		if InitialRegistration.objects.filter(college = gauss).count() != 0:
# 			colleges.append(gauss)
# 	# COLLEGEWISE COUNTS
# 	# collegewise = []
# 	# for college in colleges:
# 	# 	entry = {}
# 	# 	clgname = college.name
# 	# 	entry['collegeid'] = college.id
# 	# 	entry['college'] = college.name

# 	# 	entry['males'] = str(InitialRegistration.objects.filter(gender= 'M', college=college).count() )
# 	# 	entry['females'] = str(InitialRegistration.objects.filter(gender= 'F', college=college).count() )
# 	# 	if InitialRegistration.objects.filter(college=college)[0].college_rep:
# 	# 		entry['college_rep'] = 'Selected'
# 	# 	else:
# 	# 		entry['college_rep'] = 'Not Selected'
# 	# 	entry['total'] = str(InitialRegistration.objects.filter(college=college).count() )
# 	# 	if entry['total'] != '0':
# 	# 		for key, value in entry.iteritems():
# 	# 			if type(value) is str:
# 	# 				if value == '0':
# 	# 					entry[key] = value.replace('0', '-')
# 	# 		collegewise.append(entry)
# 	flist= []                                # no of female participants under unstandardized colleges
# 	mlist= []                                # male ^
# 	un_college = [g.name for g in College.objects.filter(is_displayed= False)]
# 	for k in InitialRegistration.objects.all():
# 		result = [k.college == z for z in un_college ]
# 		if True in result:
# 			if k.gender == 'F':
# 				flist.append(k)
# 			else:
# 				mlist.append(k)
# 	un_stdF= len(flist)
# 	un_stdM= len(mlist)
# 	un_std = un_stdM + un_stdF

# 	paidlist = InitialRegistration.objects.filter(reg_paid= True).count()
# 	paidlistm = InitialRegistration.objects.filter(reg_paid= True, gender='M').count()
# 	paidlistf= InitialRegistration.objects.filter(reg_paid= True, gender="F").count()


# 	context = {
# 		'eventwise' : eventwise,
# 		# 'collegewise' : collegewise,
# 		'total' : total,
# 		'un_stdf' : un_stdF,
# 		'un_stdm' : un_stdM,
# 		'un_std': un_std,
# 		'paid' : paidlist,
# 		'paidm' : paidlistm,
# 		'paidf' : paidlistf,
# 	}

# 	return render(request, 'pcradmin/stats.html', context)

# @staff_member_required
# def stats_collegewise(request):
# 	events = Event.objects.order_by('name')
# 	users = InitialRegistration.objects.all()
# 	colleges_init = College.objects.filter(is_displayed= True)
# 	colleges= []
# 	## SPORTWISE COUNTS
# 	# eventwise = []
# 	# for event in events:
# 	# 	entry = {}
# 	# 	entry['id'] = event.id
# 	# 	entry['name'] = event.name
# 	# 	entry['category'] = str(event.category.name)
# 	# 	entry['males'] = str(event.initialregistration_set.filter(gender='M').count())
# 	# 	entry['females'] = str(event.initialregistration_set.filter(gender='F').count())
# 	# 	entry['total'] = str(event.initialregistration_set.all().count())
# 	# 	for key, value in entry.iteritems():
# 	# 		if type(value) is str:
# 	# 			if value == '0 | 0 | 0':
# 	# 				entry[key] = value.replace('0 | 0 | 0', '---')
# 	# 	eventwise.append(entry)
# 	# total = {}
# 	# total['males'] = str(InitialRegistration.objects.filter(gender='M').count())
# 	# total['females'] = str(InitialRegistration.objects.filter(gender='F').count())
# 	# total['total'] = str(InitialRegistration.objects.all().count())

# 	for gauss in colleges_init:
# 		if InitialRegistration.objects.filter(college = gauss).count() != 0:
# 			colleges.append(gauss)
# 	# COLLEGEWISE COUNTS
# 	collegewise = []
# 	for college in colleges:
# 		entry = {}
# 		clgname = college.name
# 		entry['collegeid'] = college.id
# 		entry['college'] = college.name
# 		entry['males'] = str(InitialRegistration.objects.filter(gender='M', college=college).count())+' | '+str(InitialRegistration.objects.filter(gender='M', gl_approval=True, college=college).count())+' | '+str(InitialRegistration.objects.filter(gender='M', pcr_approval=True, college=college).count())+' | '+str(InitialRegistration.objects.filter(gender='M', gl_approval=True, college=college, reg_paid=True).count())+' | '+str(InitialRegistration.objects.filter(gender='M',pcr_approval=True, college=college, confirmed_events__gte=1).distinct().count())
# 		entry['females'] = str(InitialRegistration.objects.filter(gender='F', college=college).count())+' | '+str(InitialRegistration.objects.filter(gender='F', gl_approval=True, college=college).count())+' | '+str(InitialRegistration.objects.filter(gender='F', pcr_approval=True, college=college).count())+' | '+str(InitialRegistration.objects.filter(gender='F',gl_approval=True, college=college, reg_paid=True).count())+' | '+str(InitialRegistration.objects.filter(gender='F',pcr_approval=True, college=college, confirmed_events__gte=1).distinct().count())
# 		if InitialRegistration.objects.filter(college=college)[0].college_rep:
# 			entry['college_rep'] = 'Selected'
# 		else:
# 			entry['college_rep'] = 'Not Selected'
# 		entry['total'] = str(InitialRegistration.objects.filter(college=college).count())+' | '+str(InitialRegistration.objects.filter(gl_approval=True, college=college).count())+' | '+str(InitialRegistration.objects.filter(pcr_approval=True, college=college).count())+' | '+str(InitialRegistration.objects.filter(gl_approval=True, college=college, reg_paid=True).count())+' | '+str(InitialRegistration.objects.filter(pcr_approval=True, college=college, confirmed_events__gte=1).distinct().count())
# 		if entry['total'] != '0 | 0 | 0':
# 			for key, value in entry.iteritems():
# 				if type(value) is str:
# 					if value == '0 | 0 | 0':
# 						entry[key] = value.replace('0 | 0 | 0', '---')
# 			collegewise.append(entry)

# 	context = {
# 		# 'eventwise' : eventwise,
# 		'collegewise' : collegewise,
# 		# 'total' : total,
# 	}

# 	return render(request, 'pcradmin/stats.html', context)

# @staff_member_required
# def stats_college(request, collegeid):
# 	events = [x for x in Event.objects.order_by('name') if x.category.name != "Other"]
# 	college = College.objects.get(id= collegeid)
# 	eventwise = []
# 	for event in events:
# 		entry = {}
# 		entry['id'] = event.id
# 		entry['name'] = event.name
# 		entry['category'] = str(event.category.name)
# 		entry['males'] = str(event.initialregistration_set.filter(gender='M', college=college).count())+' | '+str(event.initialregistration_set.filter(gender='M', gl_approval=True, college=college).count())+' | '+str(event.initialregistration_set.filter(gender='M', pcr_approval=True, college=college).count())
# 		entry['females'] = str(event.initialregistration_set.filter(gender='F', college=college).count())+' | '+str(event.initialregistration_set.filter(gender='F', gl_approval=True, college=college).count())+' | '+str(event.initialregistration_set.filter(gender='F', pcr_approval=True, college=college).count())
# 		entry['total'] = str(event.initialregistration_set.filter(college=college).count())+' | '+str(event.initialregistration_set.filter(gl_approval=True, college=college).count())+' | '+str(event.initialregistration_set.filter(pcr_approval=True, college=college).count())
# 		for key, value in entry.iteritems():
# 			if type(value) is str:
# 				if value == '0 | 0 | 0':
# 					entry[key] = value.replace('0 | 0 | 0', '---')
# 		eventwise.append(entry)
# 	total = {}
# 	total['males'] = str(InitialRegistration.objects.filter(gender='M', college=college).count())+' | '+str(InitialRegistration.objects.filter(gender='M', gl_approval=True, college=college).count())+' | '+str(InitialRegistration.objects.filter(gender='M', pcr_approval=True, college=college).count())
# 	total['females'] = str(InitialRegistration.objects.filter(gender='F', college=college).count())+' | '+str(InitialRegistration.objects.filter(gender='F', gl_approval=True, college=college).count())+' | '+str(InitialRegistration.objects.filter(gender='F', pcr_approval=True, college=college).count())
# 	total['total'] = str(InitialRegistration.objects.filter(college=college).count())+' | '+str(InitialRegistration.objects.filter(gl_approval=True, college=college).count())+' | '+str(InitialRegistration.objects.filter(pcr_approval=True, college=college).count())

# 	context = {
# 		'college' : college,
# 		'eventwise' : eventwise,
# 		'total' : total,
# 	}
# 	return render(request, 'pcradmin/stats_college.html', context)

# def stats_event(request, eventid):
# 	init_collegelist = College.objects.filter(is_displayed= True)
# 	event = Event.objects.get(id=eventid)
# 	collegewise = []
# 	collegelist = []
# 	for k in init_collegelist:
# 		if InitialRegistration.objects.filter(college = k).count() != 0:
# 			collegelist.append(k)
# 	for college in collegelist:
# 		entry = {}
# 		entry['id'] = college.id
# 		entry['name'] = college.name
# 		entry['males'] = str(InitialRegistration.objects.filter(gender= 'M', college=college, events=eventid).count() )
# 		entry['females'] = str(InitialRegistration.objects.filter(gender= 'F', college=college, events=eventid).count() )
# 		entry['total'] = str(InitialRegistration.objects.filter(college=college, events= eventid).count() )

# 		entry['males'] = str(InitialRegistration.objects.filter(gender='M', college=college, events=event).count())+' | '+str(InitialRegistration.objects.filter(gender='M', gl_approval=True, college=college, events=event).count())+' | '+str(InitialRegistration.objects.filter(gender='M', pcr_approval=True, college=college, events=event).count())
# 		entry['females'] = str(InitialRegistration.objects.filter(gender='F', college=college, events=event).count())+' | '+str(InitialRegistration.objects.filter(gender='F', gl_approval=True, college=college, events=event).count())+' | '+str(InitialRegistration.objects.filter(gender='F', pcr_approval=True, college=college, events=event).count())
# 		entry['total'] = str(InitialRegistration.objects.filter(college=college, events=event).count())+' | '+str(InitialRegistration.objects.filter(gl_approval=True, college=college, events=event).count())+' | '+str(InitialRegistration.objects.filter(pcr_approval=True, college=college, events=event).count())

# 		if InitialRegistration.objects.filter(college=college)[0].college_rep:
# 			entry['college_rep'] = 'Selected'
# 		else:
# 			entry['college_rep'] = 'Not Selected'
# 		if entry['total'] != '0 | 0 | 0':
# 			for key, value in entry.iteritems():
# 				if type(value) is str:
# 					if value == '0 | 0 | 0':
# 						entry[key] = value.replace('0 | 0 | 0', '---')
# 			collegewise.append(entry)
# 	context = {
# 		'event' : event,
# 		'collegewise' : collegewise,
# 		# 'total' : total,
# 	}
# 	return render(request, 'pcradmin/stats_event.html', context)

# def stats_college_event(request, collegeid=None, eventid=None):
# 	if request.POST:
# 		pcr_request = request.POST['request']
# 		partids = request.POST.getlist('partid')
# 		if pcr_request == 'approve':
# 			for key in partids:
# 				InitialRegistration.objects.filter(id=key).update(pcr_approval=True)
# 		elif pcr_request == 'deny':
# 			for key in partids:
# 				InitialRegistration.objects.filter(id=key).update(pcr_approval=False)
# 	college = College.objects.get(id=collegeid)
# 	event = Event.objects.get(id=eventid)
# 	participants = InitialRegistration.objects.filter(college=college, events=event)
# 	context = {
# 		'college' : college,
# 		'event' : event,
# 		'participants' : participants,
# 		# 'total' : total,
# 	}
# 	return render(request, 'pcradmin/stats_participants.html', context)

# def stats_unstandardised(request):
# 	participants = []
# 	unstd_colleges = College.objects.filter(is_displayed=False)
# 	for college in unstd_colleges:
# 		participants.extend(InitialRegistration.objects.filter(college=college.name))
# 	context = {
# 	'participants' : participants,
# 	}
# 	return render(request, 'pcradmin/stats_unstandardised.html', context)

# ####stats views end#####























# def paid_list(request):
# 	paidlist = InitialRegistration.objects.filter(reg_paid= True)
# 	context = {
# 	'plist' : paidlist,
# 	}
# 	return render(request, 'pcradmin/paid_list.html', context)




# def paid_act(request):
# 	if request.POST:
# 		pcr_request = request.POST['request']
# 		partids = request.POST.getlist('partid')
# 		if pcr_request == 'approve':
# 			for key in partids:
# 				InitialRegistration.objects.filter(id=key).update(pcr_approval=True)
# 		elif pcr_request == 'deny':
# 			for key in partids:
# 				InitialRegistration.objects.filter(id=key).update(pcr_approval=False)

# 	return HttpResponseRedirect('../')







# # def email_select(request):
# # 	users = User.objects.all()
# # 	return render(request, 'pcradmin/email_select_t.html', {'users' : users})













































# # @staff_member_required
# # def username_set(request, user_id):
# # 	user = InitialRegistration.objects.get(pk=user_id)
# # 	context = {
# # 		'user' : user
# # 	}
# # 	return render(request, 'pcradmin/username_set.html', context)

# # @staff_member_required
# # def username_save(request, user_id):
# # 	user = InitialRegistration.objects.get(pk=user_id)
# # 	if request.method == "POST":
# # 		shortlisted = request.POST['shortlisted']
# # 		if shortlisted == "True":
# # 			user.shortlisted = True
# # 			if user.user == None:
# # 				newuser = User.objects.create_user(user.email_id, user.email_id, user.phone_one)
# # 				user.user = newuser
# # 			user.save()
# # 		if shortlisted == "False":
# # 			user.shortlisted = False
# # 			if user.user != None:
# # 				newuser = user.user
# # 				newuser.delete()
# # 				user.user = None
# # 			user.save()
# # 		if shortlisted == "None":
# # 			user.shortlisted = None
# # 			user.save()
# # 		if shortlisted == "Freeze":
# # 			user.user.is_active = False
# # 			user.shortlisted = False
# # 			user.user.save()
# # 			user.save()
# # 		if shortlisted == "Activate":
# # 			user.user.is_active = True
# # 			user.shortlisted = True
# # 			user.user.save()
# # 			user.save()
# # 	context = {
# # 		'user' : user
# # 	}
# # 	return render(request, 'pcradmin/username_show.html', context)

# @staff_member_required
# def change_team_limit_list(request):
# 	u_list = UserProfile.objects.order_by('college')[0:]
# 	return render(request, 'pcradmin/change_team_limit_list.html', {'u_list':u_list})

# @staff_member_required
# def change_team_limits(request):
# 	if request.method == 'POST':
# 		uid = request.POST.get('uid', False)
# 		#fna = request.POST['fna']
# 		#lna = request.POST['lna']
# 		e_list = EventNew.objects.order_by('name')[0:]
# 		message = ""
# 		return render(request, 'pcradmin/changelimit.html', {'uid':uid, 'e_list':e_list, 'message':message})

# @staff_member_required
# def change_limits(request):
# 	if request.method == 'POST':
# 		userid = request.POST['userid']
# 		climit = request.POST['limit']
# 		eventid = request.POST['eventid']
# 		p = EventLimits()
# 		p.event = EventNew.objects.get(id=int(eventid))
# 		p.leader = UserProfile.objects.get(id=int(userid))

# 		p.limit = climit
# 		p.save()
# 		return render(request, 'pcradmin/limit_changed.html')

# @staff_member_required
# def sportlimit_select(request):
# 	events = EventNew.objects.order_by('name')
# 	return render(request, 'pcradmin/sport_select.html', {'events':events})
# def sportlimit_change(request):
# 	if request.method == 'POST':
# 		eventid = request.POST['event']
# 		event = EventNew.objects.get(id=eventid)
# 		return render(request, 'pcradmin/sport_change.html', {'event':event})
# def sportlimit_save(request):
# 	if request.method == 'POST':
# 		eventid = request.POST['event']
# 		min_limit = request.POST['min_limit']
# 		max_limit = request.POST['max_limit']
# 		event = EventNew.objects.get(id=eventid)
# 		event.min_limit = min_limit
# 		event.max_limit = max_limit
# 		event.save()
# 		return render(request, 'pcradmin/sport_save.html', {'event':event})
# @staff_member_required
# def email_select(request):
# 	users = User.objects.all()
# 	return render(request, 'pcradmin/email_select.html', {'users' : users})
# @staff_member_required
# def email_compose(request):
# 	if request.method == 'POST':
# 		email = request.POST['email']
# 		subject = request.POST['subject']
# 		body = request.POST['body']
# 		context = {
# 			'to' : email,
# 			'subject' : subject,
# 			'body' : body,
# 		}
# 		return render(request, 'pcradmin/email_compose.html', context)
# @staff_member_required
# def email_statchange(request):
# 	if request.method == 'POST':
# 		to = request.POST['email']
# 		status = request.POST['status']
# 		if status == 'active':
# 			subject = "Account Activated"
# 		elif status == 'inactive':
# 			subject = "Account Frozen"
# 		body = "Dear User, Your account status has been changed, and is now "+status+"."
# 		context = {
# 			'to' : to,
# 			'subject' : subject,
# 			'body' : body,
# 		}
# 		return render(request, 'pcradmin/email_compose.html', context)
# @staff_member_required
# def email_send(request):
# 	if request.method == 'POST':
# 		sub = request.POST['sub']
# 		body = request.POST['body']
# 		send_to = request.POST['mailadd']
# 		email = EmailMessage(sub, body, 'register@bits-bosm.org', [send_to])
# 		email.send()
# 		return render(request, "pcradmin/email_sent.html", {'email':send_to})
# def status_select(request):
# 	users = User.objects.filter(is_superuser= False)
# 	return render(request, 'pcradmin/status_select.html', {'users' : users})
# @staff_member_required
# def status_set(request):
# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		user = User.objects.get(username=username)
# 		email = user.email
# 		status = user.is_active
# 		return render(request, 'pcradmin/status_set.html',{'uname': username, 'email' : email, 'stat' : status})

# @staff_member_required
# def save_sports_limits(request):
# 	if request.method == 'POST':
# 		slimit = request.POST['limit']
# 		eventid = request.POST['eventid']
# 		p = EventNew.objects.get(id=int(eventid))
# 		p.max_limit = slimit
# 		p.save()
# 		return render(request, 'pcradmin/sportslimitchanged.html')


# @staff_member_required
# def status_save(request):
# 	if request.method == 'POST':
# 		stat = request.POST['status']
# 		user_name = request.POST['uname']

# 		gauss= User.objects.all()
# 		tstat=2
# 		if stat == '0':
# 			for obj in gauss:
# 				if obj.username == user_name:
# 					obj.is_active =  False
# 					email_add = obj.email
# 					obj.save()
# 					return render(request, 'pcradmin/status_show.html', {'status' : 'inactive', 'status_bin': 0, 'username' : user_name, 'email' : email_add})
# 		if stat == '1':
# 			for obj in gauss:
# 				if obj.username == user_name:
# 					obj.is_active =  True
# 					email_add = obj.email
# 					obj.save()
# 					return render(request, 'pcradmin/status_show.html', {'status' : 'active', 'status_bin': 1,'username' : user_name, 'email' : email_add})
# 		return render(request, 'pcradmin/showstatus.html')






# # def pcr_login(request):

# 	# context = RequestContext(request)

# 	# if request.method == 'POST':
# 		# #return render(request, 'pcradmin/changelimit.html')
# 		# username = request.POST['username']
# 		# password = request.POST['password']
# 		# user = authenticate(username=username, password=password)
# 		# if user:
# 			# if user.is_active:
# 				# if user.is_staff:
# 					# login(request, user)
# 					# return HttpResponseRedirect('../dashboard/')
# 				# else:
# 					# context = {'error_heading' : "Access Denied", 'error_message' : 'You are not a PCr Member. <br> Return back <a href="/">home</a>'}
# 					# return render(request, 'pcradmin/error.html', context)
# 			# else:
# 				# context = {'error_heading' : "Account Frozen", 'error_message' :  'No changes can be made now <br> Return back <a href="/">home</a>'}
# 				# return render(request, 'pcradmin/error.html', context)

# 		# else:
# 			# context = {'error_heading' : "Invalid Login Credentials", 'error_message' :  'Please <a href=".">try again</a>'}
# 			# return render(request, 'pcradmin/error.html', context)
# 	# else:
# 		# return render(request, 'pcradmin/login.html')

# @staff_member_required
# def user_list(request):
# 	uobjects= User.objects.all()
# 	prt = Participant.objects.all()
# 	users=[]
# 	for i in uobjects:
# 		for p in prt:
# 			if p.gleader.username == i.username:
# 				users.append(i)
# 				break

# 	return render(request, 'pcradmin/listuser.html', {'user' : users, 'participant' : prt})

# # def participant_list(request):
# # 	if request.method == 'POST':
# # 		user_name= request.POST['uname']
# # 		plist= []
# # 		uid = User.objects.get(username = user_name)
# # 		#plist.append(uid)

# # 		p_objlist = Participant.objects.filter(coach = False)
# # 		for k in p_objlist:
# # 			if k.gleader.id == uid.id:
# # 				plist.append(k)

# # 		return render(request, 'pcradmin/participantlist.html', {'plist': plist, 'uname' : user_name})

# @staff_member_required
# def participant_list(request):
# 	if request.method == 'POST':
# 		if 'save' in request.POST:
# 				try:
# 					key = request.POST['id']
# 				except ValueError:
# 					return
# 				coach = request.POST['coach']
# 				if coach == "True":
# 					coach = True
# 				elif coach == "False":
# 					coach = False
# 				email = request.POST['email']
# 				uname = request.POST['uname']
# 				events = request.POST.getlist('events')
# 				name = request.POST['name']
# 				phone = request.POST['phone']
# 				sex = request.POST['sex']

# 				check=1
# 				if coach == True:
# 					check = 1
# 				if check == 1:
# 					participant = Participant.objects.get(pk=key)
# 					participant.name = name
# 					participant.gender = sex
# 					participant.phone = phone
# 					participant.email_id = email
# 					participant.coach = coach
# 					participant.events.clear()
# 					for key in events:
# 						event = EventNew.objects.get(pk=key)
# 						participant.events.add(event)
# 					participant.save()
# 					plist= []
# 					user_name = request.POST['uname']
# 					uid = User.objects.get(username = user_name)
# 					#plist.append(uid)

# 					p_objlist = Participant.objects.filter(coach = False)
# 					for k in p_objlist:
# 						if k.gleader.id == uid.id:
# 							plist.append(k)

# 					clist=[]
# 					c_objlist = Participant.objects.filter(coach = True)
# 					for k in c_objlist:
# 						if k.gleader.id == uid.id:
# 							clist.append(k)
# 					return render(request,'pcradmin/participantlist.html', {'plist': plist, 'uname' : uname, 'clist' : clist})
# 					#return redirect('registration:edit')
# 				else:
# 					user_name= request.POST['uname']
# 					participant = Participant.objects.get(pk=key)
# 					participant.name = name
# 					participant.gender = sex
# 					participant.phone = phone
# 					participant.email_id = email
# 					participant.coach = coach
# 					participant.events.clear()
# 					for key in events:
# 						event = EventNew.objects.get(pk=key)
# 						participant.events.add(event)
# 					participant.save()
# 					plist= []
# 					uid = User.objects.get(username = user_name)
# 					#plist.append(uid)

# 					p_objlist = Participant.objects.filter(coach = False)
# 					for k in p_objlist:
# 						if k.gleader.id == uid.id:
# 							plist.append(k)

# 					clist=[]
# 					c_objlist = Participant.objects.filter(coach = True)
# 					for k in c_objlist:
# 						if k.gleader.id == uid.id:
# 							clist.append(k)
# 					return render(request,'pcradmin/participantlist.html', {'plist': plist, 'uname' : uname, 'clist' : clist})

# 		user_name= request.POST['uname']
# 		plist= []
# 		uid = User.objects.get(username = user_name)
# 		#plist.append(uid)

# 		p_objlist = Participant.objects.filter(coach = False)
# 		for k in p_objlist:
# 			if k.gleader.id == uid.id:
# 				plist.append(k)

# 		eventobjects = EventNew.objects.all()
# 		eventlist = [x.name for x in eventobjects]
# 		clist=[]
# 		c_objlist = Participant.objects.filter(coach = True)
# 		for k in c_objlist:
# 			if k.gleader.id == uid.id:
# 				clist.append(k)
# 		return render(request, 'pcradmin/participantlist.html', {'plist': plist, 'uname' : user_name, 'eventlist': eventlist, 'clist' : clist})
# 	else:
# 		return render(request, 'pcradmin/dashboard.html')

# @staff_member_required
# def search_user(request):
# 	if request.method == 'POST':
# 		query = request.POST['query']

# 		uprofile = UserProfile.objects.all()
# 		result= []
# 		flag=0
# 		for k in uprofile:
# 			flag=0
# 			for z in Participant.objects.all():
# 				if z.gleader == k.user:
# 					flag=1
# 					break
# 			if flag == 1:
# 				if query.upper() in k.firstname.upper() or query.upper() in k.lastname.upper() or query.upper() in k.college.upper() or query.upper() in k.user.username.upper() or query.upper() in k.user.email.upper():
# 					result.append(k)

# 		return render(request, 'pcradmin/users.html', {'result' : result})

# @staff_member_required
# def search_plist(request):
# 	if request.method == 'POST' and 'query' in request.POST:
# 		qry = request.POST['query']
# 		uid= request.POST['plist']
# 		uname = request.POST['uname']
# 		gender= request.POST['gender']
# 		p_list = Participant.objects.all()
# 		klist= []
# 		for z in p_list:
# 			if z.gleader.username == uname:
# 				klist.append(z)

# 		plist = []
# 		for k in klist:
# 			events = k.events.all()
# 			if gender == 'B':
# 				for z in events:
# 					if qry.upper() in z.name.upper():
# 						plist.append(k)
# 				if qry.upper() in k.name.upper() or qry.upper() in k.email_id.upper():
# 					plist.append(k)
# 			elif k.gender == gender:
# 				for z in events:
# 					if qry.upper() in z.name.upper():
# 						plist.append(k)
# 				if qry.upper() in k.name.upper() or qry.upper() in k.email_id.upper():
# 					plist.append(k)

# 		return render(request, 'pcradmin/participants.html', {'plist' : plist, 'uname' : uname})
# 	else:
# 		uname = request.POST['uname']
# 		gender = request.POST['gender']
# 		user_gauss = User.objects.filter(username= uname)[0]
# 		event_q = request.POST['event_search']
# 		p_list = Participant.objects.filter(gleader=user_gauss)
# 		# klist= []
# 		# for z in p_list:
# 		# 	if z.gleader.username == uname:
# 		# 		klist.append(z)

# 		plist = []
# 		for k in p_list:
# 			eventss = k.events.all()
# 			for x in eventss:
# 				if gender == 'B':
# 					if event_q in x.name:
# 						plist.append(k)
# 				elif k.gender in gender:
# 					if event_q in x.name:
# 						plist.append(k)


# 		return render(request, 'pcradmin/participants.html', {'plist' : plist, 'uname' : uname})





# @staff_member_required
# def pconfirm(request):
# 	if request.method == 'POST':
# 		#pidlist = request.POST['key']
# 		plist=[]
# 		test = request.POST['key']
# 		uname = request.POST['uname']

# 		if test == 'confirm':
# 			for k in Participant.objects.all():
# 				for z in request.POST:
# 					if z != 'key' and z != 'uname' :
# 						if str(k.id) == str(z):
# 							k.confirmation = True
# 							k.save()
# 							plist.append(k)

# 		if test == 'unconfirm':
# 			for k in Participant.objects.all():
# 				for z in request.POST:
# 					if z != 'key'and z != 'uname':
# 						if str(k.id) == str(z):
# 							k.confirmation = False
# 							k.save()
# 							plist.append(k)
# 		return render(request, 'pcradmin/confirmed.html', {'plist' : plist, 'uname' : uname})


# @staff_member_required
# def stats_view_old(request):
# 	events = EventNew.objects.order_by('name')
# 	users = User.objects.all()


# 	## SPORTWISE COUNTS
# 	sportwise = []
# 	for event in events:
# 		entry = {}
# 		entry['id'] = event.id
# 		entry['name'] = event.name
# 		entry['males'] = str(event.participant_set.filter(gender='M', confirmation=True, coach=False).count()) + ' | ' + str(event.participant_set.filter(gender='M', coach=False).count())
# 		entry['females'] = str(event.participant_set.filter(gender='F', confirmation=True, coach=False).count()) + ' | ' + str(event.participant_set.filter(gender='F', coach=False).count())
# 		entry['coaches'] = str(event.participant_set.filter(confirmation=True, coach=True).count()) + ' | ' + str(event.participant_set.filter(coach=True).count())
# 		entry['total'] = str(event.participant_set.filter(confirmation=True).count()) + ' | ' + str(event.participant_set.all().count())
# 		for key, value in entry.iteritems():
# 			if type(value) is str:
# 				entry[key] = value.replace('0 | 0', '--')
# 		sportwise.append(entry)
# 	total = {}
# 	total['males'] = str(Participant.objects.filter(gender='M', confirmation=True, coach=False).count()) + ' | ' + str(Participant.objects.filter(gender='M', coach=False).count())
# 	total['females'] = str(Participant.objects.filter(gender='F', confirmation=True, coach=False).count()) + ' | ' + str(Participant.objects.filter(gender='F', coach=False).count())
# 	total['coaches'] = str(Participant.objects.filter(coach=True, confirmation=True).count()) + ' | ' + str(Participant.objects.filter(coach=True).count())
# 	total['total'] = str(Participant.objects.filter(confirmation=True).count()) + ' | ' + str(Participant.objects.all().count())

# 	# COLLEGEWISE COUNTS
# 	collegewise = []
# 	for user in users:
# 		entry = {}
# 		entry['userid'] = user.id
# 		try:
# 			entry['college'] = user.userprofile_set.all()[0].college
# 		except IndexError:
# 			entry['college'] = '<none>'
# 		entry['males'] = str(user.participant_set.filter(gender='M', confirmation=True, coach=False).count()) + ' | ' + str(user.participant_set.filter(gender='M', coach=False).count())
# 		entry['females'] = str(user.participant_set.filter(gender='F', confirmation=True, coach=False).count()) + ' | ' + str(user.participant_set.filter(gender='F', coach=False).count())
# 		entry['coaches'] = str(user.participant_set.filter(confirmation=True, coach=True).count()) + ' | ' + str(user.participant_set.filter(coach=True).count())
# 		entry['total'] = str(user.participant_set.filter(confirmation=True).count()) + ' | ' + str(user.participant_set.all().count())
# 		if entry['total'] != '0 | 0':
# 			for key, value in entry.iteritems():
# 				if type(value) is str:
# 					entry[key] = value.replace('0 | 0', '--')
# 			collegewise.append(entry)

# 	context = {
# 		'sportwise' : sportwise,
# 		'collegewise' : collegewise,
# 		'total' : total,
# 	}

# 	return render(request, 'pcradmin/stats.html', context)

# @staff_member_required
# def stats_college_old(request, userid):
# 	events = EventNew.objects.order_by('name')
# 	college = User.objects.get(id=userid).userprofile_set.all()[0].college
# 	sportwise = []
# 	for event in events:
# 		entry = {}
# 		entry['id'] = event.id
# 		entry['name'] = event.name
# 		entry['males'] = str(event.participant_set.filter(gleader=userid, gender='M', confirmation=True, coach=False).count()) + ' | ' + str(event.participant_set.filter(gleader=userid, gender='M', coach=False).count())
# 		entry['females'] = str(event.participant_set.filter(gleader=userid, gender='F', confirmation=True, coach=False).count()) + ' | ' + str(event.participant_set.filter(gleader=userid, gender='F', coach=False).count())
# 		entry['coaches'] = str(event.participant_set.filter(gleader=userid, confirmation=True, coach=True).count()) + ' | ' + str(event.participant_set.filter(gleader=userid, coach=True).count())
# 		entry['total'] = str(event.participant_set.filter(gleader=userid, confirmation=True).count()) + ' | ' + str(event.participant_set.filter(gleader=userid).count())
# 		for key, value in entry.iteritems():
# 			if type(value) is str:
# 				entry[key] = value.replace('0 | 0', '--')
# 		sportwise.append(entry)
# 	total = {}
# 	total['males'] = str(Participant.objects.filter(gleader=userid, gender='M', confirmation=True, coach=False).count()) + ' | ' + str(Participant.objects.filter(gleader=userid, gender='M', coach=False).count())
# 	total['females'] = str(Participant.objects.filter(gleader=userid, gender='F', confirmation=True, coach=False).count()) + ' | ' + str(Participant.objects.filter(gleader=userid, gender='F', coach=False).count())
# 	total['coaches'] = str(Participant.objects.filter(gleader=userid, coach=True, confirmation=True).count()) + ' | ' + str(Participant.objects.filter(gleader=userid, coach=True).count())
# 	total['total'] = str(Participant.objects.filter(gleader=userid, confirmation=True).count()) + ' | ' + str(Participant.objects.filter(gleader=userid).count())
# 	context = {
# 		'name' : college,
# 		'sportwise' : sportwise,
# 		'total' : total,
# 	}
# 	return render(request, 'pcradmin/stats.html', context)

# def stats_event_old(request, eventid):
# 	users = User.objects.all()
# 	event = EventNew.objects.get(id=eventid).name
# 	collegewise = []
# 	for user in users:
# 		entry = {}
# 		entry['userid'] = user.id
# 		try:
# 			entry['college'] = user.userprofile_set.all()[0].college
# 		except IndexError:
# 			entry['college'] = '<none>'
# 		entry['males'] = str(user.participant_set.filter(gender='M', confirmation=True, coach=False, events=eventid).count()) + ' | ' + str(user.participant_set.filter(gender='M', coach=False, events=eventid).count())
# 		entry['females'] = str(user.participant_set.filter(gender='F', confirmation=True, coach=False, events=eventid).count()) + ' | ' + str(user.participant_set.filter(gender='F', coach=False, events=eventid).count())
# 		entry['coaches'] = str(user.participant_set.filter(confirmation=True, coach=True, events=eventid).count()) + ' | ' + str(user.participant_set.filter(coach=True, events=eventid).count())
# 		entry['total'] = str(user.participant_set.filter(confirmation=True, events=eventid).count()) + ' | ' + str(user.participant_set.filter(events=eventid).count())
# 		if entry['total'] != '0 | 0':
# 			for key, value in entry.iteritems():
# 				if type(value) is str:
# 					entry[key] = value.replace('0 | 0', '--')
# 			collegewise.append(entry)
# 	context = {
# 		'name' : event,
# 		'collegewise' : collegewise,
# 		# 'total' : total,
# 	}
# 	return render(request, 'pcradmin/stats.html', context)




# @staff_member_required
# def loginas_warning(request):
# 	return render(request, 'pcradmin/loginas_warning.html')

# @staff_member_required
# def loginas_select(request):
# 	users = User.objects.all()
# 	return render(request, 'pcradmin/loginas_select.html', {'users':users})

# # @user_passes_test(lambda u: u.is_superuser)
# @staff_member_required
# def loginas_login(request, userid):
# 	user = User.objects.get(id=userid)
# 	user.backend = 'django.contrib.auth.backends.ModelBackend'
# 	login(request, user)
# 	return redirect('registration:dashboard')

# def user_logout(request):
# 	logout(request)
# 	return redirect('registration:login')


# @staff_member_required
# def pedit(request):
# 	if request.method == 'POST':
# 		if 'edit' in request.POST:
# 			key = request.POST['pid']
# 			participant = Participant.objects.get(pk=key)
# 			# userprofile = request.user.userprofile_set.all()[0]
# 			events = EventNew.objects.order_by('name')
# 			context = {
# 				# 'name' : userprofile,
# 				# 'college' : userprofile.college,
# 				'participant': participant,
# 				'events' : events,
# 			}
# 			return render(request, 'pcradmin/participant_edit_detail.html', context)
# 		if 'save' in request.POST:
# 			try:
# 				key = request.POST['id']
# 			except ValueError:
# 				return
# 			coach = request.POST['coach']
# 			if coach == "True":
# 				coach = True
# 			elif coach == "False":
# 				coach = False
# 			email = request.POST['email']
# 			uname = request.POST['uname']
# 			events = request.POST.getlist('events')
# 			name = request.POST['name']
# 			phone = request.POST['phone']
# 			sex = request.POST['sex']
# 			check = check_limits(request)
# 			if coach == True:
# 				check = 1
# 			if check == 1:
# 				participant = Participant.objects.get(pk=key)
# 				participant.name = name
# 				participant.gender = sex
# 				participant.phone = phone
# 				participant.email_id = email
# 				participant.coach = coach
# 				participant.events.clear()
# 				for key in events:
# 					event = EventNew.objects.get(pk=key)
# 					participant.events.add(event)
# 				participant.save()
# 				eventobjects= EventNew.objects.all()
# 				eventlist = [ x.name for x in eventobjects]

# 				return render(request,'pcradmin/participantlist.html', {'uname' : uname, 'eventlist' : eventlist})
# 				#return redirect('registration:edit')
# 			else:
# 				eventobjects = EventNew.objects.all()
# 				eventlist = [x.name for x in eventobjects]
# 				return render(request, 'pcradmin/participantlist.html', {'uname' : uname, 'eventlist' : eventlist})
# 	else:
# 		return render('pcradmin/dashboard.html')

# @staff_member_required
# def check_limits(request):
# 	return 1
# 	# if 'id' in request.POST:
# 	#     partid = request.POST['id']
# 	# events = request.POST.getlist('events')
# 	# userid = request.user.id
# 	# # default = request.user.userprofile_set.all()[0].default_limits
# 	# error = []
# 	# userprofile = str(request.user.userprofile_set.all()[0].id)
# 	# for key in events:
# 	#     event = EventNew.objects.get(pk=key)
# 	#     already = event.participant_set.filter(gleader=userid, coach=False)
# 	#     current = len(already)
# 	#     try:
# 	#         limit = EventLimits.objects.get(event=key, leader=userprofile)
# 	#         max_limit = limit.limit
# 	#     except EventLimits.DoesNotExist:
# 	#         max_limit = event.max_limit
# 	#     try :
# 	#         check = Participant.objects.get(pk=partid)
# 	#         if check in already:
# 	#             max_limit = max_limit + 1
# 	#     except:
# 	#         pass
# 	#     if current >= max_limit:
# 	#         error.append('Only '+str(max_limit)+' participants can be registered for '+event.name+'!')
# 	# if len(error) > 0:
# 	#     return error
# 	# else:
# 	#     return 1


# def gauss_xlsx(request):
# 	from django.http import HttpResponse, HttpResponseRedirect
# 	import xlsxwriter

# 	try:
# 		import cStringIO as StringIO
# 	except ImportError:
# 		import StringIO
# 	a_list = []






# 	# data = sorted(a_list, key=lambda k: k.college)
# 	# data.sort(key=lambda x: x.name.lower())
# 	output = StringIO.StringIO()
# 	workbook = xlsxwriter.Workbook(output)
# 	worksheet = workbook.add_worksheet('new-spreadsheet')
# 	# date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

# 	eventlist = Event.objects.all()
# 	init_ob = InitialRegistration.objects.all()
# 	clglist = [t.name for t in College.objects.filter(is_displayed= True)]
# 	# clglist = sorted(clglist, key=lambda k: k.lower)
# 	plist = []


# 	worksheet.set_column (0,0, 30)
# 	worksheet.write(0, 0, "College Name")

# 	colno =1
# 	for event in eventlist:
# 		worksheet.write(0, colno , event.name)
# 		colno = colno+1

# 	colno = 1
# 	rowno = 1

# 	for clg in clglist:
# 		colno =1
# 		# plist= []
# 		# plist = InitialRegistration.objects.filter(college = clg)
# 		if  InitialRegistration.objects.filter(college=clg):
# 			worksheet.write(rowno, 0 , clg)

# 			for event in eventlist:
# 				fermat = str(event.initialregistration_set.filter(college = clg, gender= 'M').count()) + '|' +  str(event.initialregistration_set.filter(college = clg, gender='F').count() ) #+ '|' + str(event.initialregistration_set.filter(college = clg, pcr_approval= True).count() )
# 				worksheet.set_column (rowno, colno, 16)
# 				worksheet.write(rowno, colno, fermat)
# 				colno+=1

# 			rowno+=1



# 	# for row in data:
# 	#     """for each object in the date list, attribute1 & attribute2
# 	#     are written to the first & second column respectively,
# 	#     for the relevant row. The 3rd arg is a failure message if
# 	#     there is no data available"""
# 		# worksheet.write(i, 0, i+1)
# 		# worksheet.write(i, 1, getattr(row['obj'], 'name', 'attribute1 not available'))
# 		# worksheet.write(i, 2, getattr(row['obj'], 'gender', 'attribute2 not available'))
# 		# worksheet.write(i, 3, getattr(row['obj'], 'phone', 'attribute1 not available'))
# 		# worksheet.write(i, 4, getattr(row['obj'], 'event', 'attribute1 not available'))
# 		# worksheet.write(i, 5, getattr(row['obj'], 'college', 'attribute1 not available'))

# 	workbook.close()
# 	filename = 'ExcelReport.xlsx'
# 	output.seek(0)
# 	response = HttpResponse(output.read(), content_type="application/ms-excel")
# 	response['Content-Disposition'] = 'attachment; filename=%s' % filename
# 	return response







# def gausstest(request):
# 	return render(request,'pcradmin/gausstest.html')

# def pdf_select(request):
# 	users = UserProfile.objects.all()
# 	context = {
# 		'users' : users,
# 		# 'name' : request.user.userprofile.details.name,
# 		# 'college' : request.user.userprofile.details.college,
# 	}
# 	return render(request, 'pcradmin/pdf_select.html', context)

# def pdf_edit(request, userid, saved=False):
# 	events = Event.objects.all()
# 	context = {
# 		# 'name' : userprofile,
# 		# 'college' : userprofile.college,
# 		# 'participants': participants,
# 		'events' : events
# 	}

# 	eventlist = [x for x in Event.objects.order_by('name') if x.category.name != "Other"]
# 	collegerep = UserProfile.objects.get(id=userid)
# 	participants = collegerep.initialregistration_set.filter(pcr_approval=True)
# 	firsttime = True
# 	# for member in participants:
# 	# 	if member.confirmed_events.count() > 0:
# 	# 		firsttime = False
# 	events = []
# 	for key in eventlist:
# 		event = {}
# 		event['name'] = key.name
# 		event['id'] = key.id

# 		# edited = key.initialregistration_confirmed_set.filter(college_rep=collegerep, pcr_approval=True)
# 		# if edited.count() == 0:
# 		# 	members = key.initialregistration_set.filter(college_rep=collegerep, pcr_approval=True)
# 		# elif edited.count() > 0:
# 		# 	members = key.initialregistration_confirmed_set.filter(college_rep=collegerep, pcr_approval=True)

# 		all_members = key.initialregistration_set.filter(college_rep=collegerep, pcr_approval=True)
# 		confirmed_members = key.initialregistration_confirmed_set.filter(college_rep=collegerep, pcr_approval=True)

# 		members = []
# 		# if firsttime:
# 		# 	for member in all_members:
# 		# 		member.checked = True
# 		# 		members.append(member)
# 		# if not firsttime:
# 		for member in all_members:
# 			if member in confirmed_members:
# 				member.checked = True
# 				members.append(member)
# 			else:
# 				member.checked = False
# 				members.append(member)
# 		event['count'] = len(members)
# 		event['members'] = members
# 		if event['count'] > 0:
# 			events.append(event)
# 	context = {
# 		'events' : events,
# 		'collegerep' : collegerep,
# 		'userid' : userid,
# 		'saved' : saved,
# 		# 'name' : request.user.userprofile.details.name,
# 		# 'college' : request.user.userprofile.details.college,
# 	}
# 	return render(request, 'pcradmin/pdf_edit.html', context)

# def pdf_save(request, userid):
# 	collegerep = UserProfile.objects.get(id=userid)
# 	participants = collegerep.initialregistration_set.filter(pcr_approval=True)
# 	for member in participants:
# 		member.confirmed_events.clear()
# 		member.save()
# 	data = {}
# 	for eventid in request.POST:
# 		data[eventid] = request.POST.getlist(eventid)
# 	# events = [x for x in data if x.isdigit == True]
# 	# return HttpResponse(events)
# 	for eventid, memberids in data.iteritems():
# 		try:
# 			event = Event.objects.get(id=eventid)
# 		except ValueError:
# 			continue
# 		for memberid in memberids:
# 			member = InitialRegistration.objects.get(id=memberid)
# 			member.confirmed_events.add(event)
# 			member.save()
# 	return pdf_edit(request, userid, True)
