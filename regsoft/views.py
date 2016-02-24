from backend.models import *
from regsoft.models import *
# from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import string
from random import randint
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, render
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from Event.models import *
from django.db import IntegrityError
import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404





#####################################FIREWALLZ###########################################




@csrf_exempt
@staff_member_required
def firewallzo_board(request):
    if request.POST:
        try:
            pidlist= request.POST.getlist('pidlist',False) #taking alternative character because alphabets were random and had no meaning
            part_ob_list =[]
            plist2=[]
            for part in pidlist:
                part_ob = Participant.objects.get(id=int(part))
                if part_ob.firewallzo:
                    plist2.append(part_ob)
                else:
                    part_ob_list.append(part_ob)
            context={
            'plist' : part_ob_list,
            'plist2' : plist2,
            }
            return render(request, 'regsoft/table_apogee.html', context)            
        except:
            return HttpResponse('Error : Call Satwik : 9928823099')
    else:
        return HttpResponseRedirect('../barcodelist/')





@csrf_exempt
@staff_member_required
def firewallzo_dashboard(request):
    if request.POST:
        try:
            encoded = request.POST['code']
            decoded = int(encoded[0]+encoded[2]+encoded[4]+encoded[6]) #taking alternative character because alphabets were random and had no meaning

        except:
            if request.POST.get('crepid', False):
                decoded = int( request.POST['crepid'] )
            else:
                return render(request, 'regsoft/scan.html', {'status' : 0})
        return HttpResponseRedirect("../scan/" + str(decoded) )


        decoded = int(encoded[0]+encoded[2]+encoded[4]+encoded[6]) #taking alternative character because alphabets were random and had no meaning
        
        part = Participant.objects.filter(id = decoded)
        if part:
            part=  part[0]
            context = {
            'part' :part,
            }
            return render(request, 'regsoft/table.html', context)
        else:
            return render(request, 'regsoft/scan.html', {'status' : 0})


    return render(request, 'regsoft/scan.html')



@staff_member_required
def firewallzo_dashboard_two(request,part_id):

    decoded = part_id
    # decoded = int(encoded[0]+encoded[2]+encoded[4]+encoded[6]) #taking alternative character because alphabets were random and had no meaning    
    part = Participant.objects.filter(id = decoded)
    if part:
        part=  part[0]
        context = {
        'part' : part,

        }
        return render(request, 'regsoft/table.html', context)
    else:
        return render(request, 'regsoft/scan.html', {'status' : 0})


    return render(request, 'regsoft/scan.html')

def firewallzo_confirm(request):
    if request.POST:
        # pid = request.POST.get('confirm',False)
        pidlist = request.POST.getlist('pidlist',False)
        glid= int(request.POST.getlist('gleader')[0])
        grp_part_ob = Participant.objects.get(id= glid)
        grp_part_ob.firewallzo=True
        grp_part_ob.save()
        grp_ob= gleader(details=grp_part_ob, groupcode="")
        grp_ob.save()
        grp_id = grp_ob.id
        googol = "000000000"        
        num_part = googol[ : ( 4 - len(str(grp_id)) ) ] + str(grp_id)
        grpcode= "0"
        try:
            grpcode = str(grp_ob.details.name)[:3].upper() + num_part
        except:
            grpcode = "0"
        grp_ob.groupcode= grpcode
        grp_ob.save()
        plist=[]
        if pidlist:
            for pid in pidlist:
                pid = int(pid)
                p_ob= Participant.objects.get(id= int(pid))
                p_ob.firewallzo=True
                p_ob.grpleader= grp_ob
                p_ob.save()
                googol = "000000000"
                clg = p_ob.college.name
                num_part = googol[ : ( 4 - len(str(pid)) ) ] + str(pid)
                pcode= "0"
                try:
                    pcode = str(clg)[:3].upper() + num_part
                except:
                    pcode = "0"
                p_ob.aadhaar = pcode
                p_ob.save()
                plist.append(p_ob)
        else:
            return HttpResponse('Please select atleast 1 participant')            
        context={
        'plist2' : plist,
        }
        return render(request,'regsoft/table_apogee.html', context)


# def firewallzo_unconfirm(request, part_id):
#     p_ob = Participant.objects.get(id = int(part_id))
#     p_ob.firewallzo = False
#     p_ob.save()
#     return HttpResponseRedirect('../scan/' + str(p_ob.id) )



def firewallzo_edit_part(request, part_id):
    if request.POST:
        part_ob = Participant.objects.get(id = part_id)
        part_ob.name = str(request.POST['name'])
        part_ob.email_id = str(request.POST['email'])
        part_ob.phone_one = int(request.POST['phone'])
        part_ob.gender = str(request.POST['gender'])
        if request.POST.get('pcr_approval', False):
            part_ob.pcr_approval=True
        else:
            part_ob.pcr_approval = False

        part_ob.events.clear()
        if request.POST.get('events', False):
            for k in request.POST.getlist('events'):                                    
                event = Event.objects.get(pk=k)
                part_ob.events.add(event)
        part_ob.save()
        return HttpResponseRedirect('../barcodelist/' )


    part_ob = Participant.objects.get(id= part_id)
    elist = Event.objects.all()
    # crep = init_ob.college_rep
    return render(request, 'regsoft/fire_edit.html' , {'part' : part_ob, 'events' : elist})




def firewallzo_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        sex = request.POST['gender']
        phone_one = request.POST['phone']
        email = request.POST['email']
        col_id= int(request.POST['college'])
        events = request.POST.getlist('events')
        check = 1
        try:
            college= College.objects.get(id= col_id)
        except:
            college=None
        # check = check_limits(request)

        try:
            participant = Participant.objects.create(name=name, gender=sex, phone_one=phone_one, email_id=email, college=college,  pcr_approval = True)
        except IntegrityError:
        # errors = []
            errorsx = 'The email '+str(email)+' has already been registered. Try a different email.'
            events = [x for x in Event.objects.order_by('name') if x.category.name != "Other"]
            clg_list =  College.objects.all()
            context = {
                'clg_list' : clg_list ,
                'errors' : errorsx,
                'events' : events,
            }
            return render(request, 'regsoft/fire_add.html', context)
        # #### FireWallz bypass for bitsians
        # if str(user_pr.college) == 'BITS Pilani':
        #     participant.firewallz= True
        #     participant.confirmation= True
        for k in events:
            event = Event.objects.get(id=k)
            participant.events.add(event)
        participant.save()
        return HttpResponseRedirect('../scan/')
        
    # userprofile = request.user.userprofile_set.all()[0]
    events = [x for x in Event.objects.order_by('name') if x.category.name != "Other"]
    clg_list= College.objects.all()
    context = {
        'clg_list':clg_list,
        'events' : events,
    }
    return render(request, 'regsoft/fire_add.html', context)



def firewallzo_setgleader(request, crep_id):
  if request.POST:
      part_id = request.POST['pid']
      # pidlist = request.POST.getlist['pidlist']
      part = InitialRegistration.objects.get(id = part_id)
      crep = UserProfile.objects.get(id= crep_id )
      partid = part.id
      newgl = gleader(details = part, groupcode= '')
      newgl.save()
        
      googol = '000000000'
      glid = newgl.id 
      num_gl  = googol[ : (4 - len(str(glid)) ) ] + str(glid)
      grpcode = str(part.college)[:3] + num_gl
      newgl.groupcode = grpcode
      newgl.save()

      for pid in request.POST:
          if pid != 'pid' and pid != 'csrfmiddlewaretoken':
              pid = int(pid)
              part = InitialRegistration.objects.get(id =pid)
              part.grpleader = newgl
              part.save()


      return HttpResponseRedirect('../scan/' + str(crep.id))




















##### GROUP CODE LIST #####
def gcodelist(request):
    gl_list = gleader.objects.all()
    data=[]
    for k in gl_list:
        gcode= k.groupcode
        glname= k.details.name
        glid= k.id
        males = Participant.objects.filter(gender='M', grpleader=k).count()
        females = Participant.objects.filter(gender='F', grpleader=k).count()
        data.append( (glname,gcode,glid,males,females) )

    context = {
    'data' : data,
    }
    return render(request, 'regsoft/groupcodelist.html', context)


def unconfirm_list(request):
    gl_list = gleader.objects.all()
    data=[]
    for k in gl_list:
        gcode= k.groupcode
        glname= k.details.name
        glid= k.id
        males = Participant.objects.filter(gender='M', grpleader=k).count()
        females = Participant.objects.filter(gender='F', grpleader=k).count()
        data.append( (glname,gcode,glid,males,females) )
    context = {
    'data' : data,
    }
    return render(request, 'regsoft/fire_unconfirm_2.html', context)


def fire_unconfirm(request,glid):
    gl_ob= gleader.objects.get(id=int(glid))
    plist = Participant.objects.filter(grpleader=gl_ob)
    for k in plist:
        k.firewallzo= False
        k.grpleader= None
        k.save()
    gl_ob.details= None
    gl_ob.save()
    gl_ob.delete()
    return HttpResponseRedirect('../')



def grp_details(request,gl_id):
    gl_ob = gleader.objects.get(id=int(gl_id))
    plist = Participant.objects.filter(grpleader=gl_ob)
    context = {
    'gl_ob' : gl_ob,
    'plist' : plist,
    }
    return render(request, 'regsoft/grp_details.html', context)

# def testx(request):
#   return render(request, 'regsoft/testx.html')


##############################################CONTROLZ #########################################


@csrf_exempt
def controlz_home(request):
    if request.POST:
        try:
            encoded = str( request.POST['code'] )
            decoded = int(encoded[-4:]) #taking alternative character because alphabets were random and had no meaning

        except:
            return render(request, 'regsoft/controlz_home.html', {'status' : 0})
        return HttpResponseRedirect("../home/" + str(decoded) )

    return render(request, "regsoft/controlz_home.html")

def controlz_stats(request):
    passed_controls = Participant.objects.filter(controlz=True).count()
    passed_offline = Participant.objects.filter(controlz=True, fee_paid= False ).count()
    passed_online = Participant.objects.filter(controlz=True, fee_paid=True).count()
    all_bills = Bill.objects.all()
    amount_total = 0
    for bill in all_bills:
        amount_total += bill.amount
    context = {
        'passed_controls' : passed_controls,
        'passed_offline' : passed_offline,
        'passed_online' : passed_online,
        'amount_total' : amount_total,
    }

    return render(request, "regsoft/controlz_stats.html", context)

def controlz_dashboard(request,gl_id):
    gl_ob = gleader.objects.filter(id = gl_id)
    if gl_ob:
        gl_ob = gl_ob[0]
        plist = gl_ob.participant_set.filter(controlz =False)
        plist_two = gl_ob.participant_set.filter(controlz =True)
        maleno = Participant.objects.filter(grpleader = gl_ob, gender= 'M', controlz= False).count()
        femaleno = Participant.objects.filter(grpleader = gl_ob, gender= 'F', controlz= False).count()
        maleno_two = Participant.objects.filter(grpleader = gl_ob, gender= 'M', controlz= True).count()
        femaleno_two = Participant.objects.filter(grpleader = gl_ob, gender= 'F', controlz= True).count()

        context ={
        'gl' : gl_ob, 
        'plist' : plist,
        'plist_two' : plist_two,
        'maleno' : maleno,
        'femaleno' : femaleno,
        'maleno_two' : maleno_two,
        'femaleno_two' : femaleno_two,


        }
        return render(request, 'regsoft/controlz_dashboard.html', context)

    else:
        return render(request, 'regsoft/controlz_home.html', {'status' : 0})




def controlz_edit_part(request, part_id):
    if request.POST:
        init_ob = Participant.objects.get(id = part_id)
        init_ob.name = str(request.POST['name'])
        init_ob.email_id = str(request.POST['email'])
        init_ob.phone_one = int(request.POST['phone'])
        init_ob.gender = str(request.POST['gender'])

        init_ob.events.clear()
        if request.POST.get('events', False):
            for k in request.POST.getlist('events'):                                    
                event = Event.objects.get(pk=k)
                init_ob.events.add(event)
        init_ob.save()

        gl = init_ob.grpleader
        return HttpResponseRedirect('../home/' + str(gl.id) )


    init_ob = Participant.objects.get(id= part_id)
    elist = Event.objects.all()
    gl = init_ob.grpleader
    return render(request, 'regsoft/controlz_edit.html' , {'part' : init_ob, 'events' : elist, 'gl' : gl})



def controlz_bill_select(request):
    if request.POST:
        pidlist = request.POST.getlist('part')
        plist= []
        onlinepaid=0
        for k in pidlist:
            k= int(k)
            part = Participant.objects.get(id=k)
            plist.append(part)
            if part.fee_paid == True:
                onlinepaid+=1

        totalamt= onlinepaid*0
        

        gl = plist[0].grpleader
        total = len(plist) 
        totalamt += (total - onlinepaid) * 900
        pcount = (total - onlinepaid)
        context ={
        'gl' : gl, 
        'plist' : plist,
        'total' : total,
        'totalamt' : totalamt,
        'onlinepaid' : onlinepaid,
        'pcount' : pcount,
        }

        return render(request, 'regsoft/controlz_bill_amt.html', context)


def controlz_bill_details(request,gl_id):
    if request.POST:
        pidlist= str(request.POST['pidlist'])
        gl_id = gl_id
        gl= gleader.objects.get(id=gl_id)
        college = gl.details.college
        femaleno =0
        maleno  =0
        pidlistx = pidlist.split(',')
        pidlist = pidlist.split(',')
        onlinepaid = 0
        for k in pidlist:
            if k != '' :
                k=int(k)
                part = Participant.objects.get(id =k)
                part.controlz = True
                if part.gender == 'M':
                    maleno+=1
                else:
                    femaleno+=1
                if part.fee_paid:
                    onlinepaid+=1
                part.save()

        ddno = request.POST.get('ddno' ,  False)
        n1000 = int(request.POST.get('n_1000',0) )
        n500 = int(request.POST.get('n_500',      0) )
        n100 = int(request.POST.get('n_100',      0) )
        n50 = int(request.POST.get('n_50',        0) )
        n20 = int(request.POST.get('n_20',        0) )
        n10 = int(request.POST.get('n_10' ,      0) )


        # totalamt = 1000*n1000 + 500*n500 + 100*n100 + 50*n50 + 20*n20 + 10*n10


        balance = 0
        given=0
        if n1000 < 0:
            balance += -(n1000) * 1000
        else:
            given+= n1000 * 1000


        if n500 < 0:
            balance += -(n500) * 500
        else:
            given+= n500 * 500


        if n100 < 0:
            balance += -(n100) * 100
        else:
            given+= n100 * 100


        if n50 < 0:
            balance += -(n50) * 50
        else:
            given+= n50 * 50


        if n20 < 0:
            balance += -(n20) * 20 
        else:
            given+= n20 * 20     

        if n10 < 0:
            balance += -(n10) * 10 
        else:
            given+= n10 * 10                                                     
            



        total = request.POST.get('total', 0)
        if total == '':
            total = 0   
        if ddno:
            newbill = Bill(gleader = gl_id, amount= total, given=given, balance=balance, draft_number= ddno)
        else:
            newbill = Bill(gleader = gl_id, amount= total, given=given, balance=balance)
            ddno= 'None'

        newbill.save()

        test = []
        for k in pidlistx:
            if k != '' :
                k=int(k)
                part = Participant.objects.get(id =k)
                part.bill_id = int(newbill.id)
                test.append({part.name, newbill.id})
                part.save()

                
        newbill.notes_1000 = int(n1000)
        newbill.notes_500 = int(n500)
        newbill.notes_100 = int(n100)
        newbill.notes_50 = int(n50)
        newbill.notes_20 = int(n20)
        newbill.notes_10 = int(n10)
        newbill.save()



        # return HttpResponse(test)
    context={
        'gl' : gl,
        'college' : college,
        'given' : given,
        'balance' : balance, 
        'total' : total,
        'maleno' : maleno,
        'femaleno' : femaleno,
        'bill_id' : newbill.id,
        'totalpart' : (maleno+femaleno),
        'ddno' : ddno,
        'onlinepaid' : onlinepaid,

    }


    return render(request, 'regsoft/controlz_bill_details.html', context)




def controlz_bill_print(request):
    if request.POST:
        bill_id = int(request.POST['bill_id'])
        gl_id = int(request.POST['gl_id'])
        bill_ob = Bill.objects.get(id=bill_id)
        gl = gleader.objects.get(id=bill_ob.gleader)
        college =gl.details.college
        grpcode = gl.groupcode
        receiptno = bill_ob.id
        total = bill_ob.amount
        maleno = Participant.objects.filter(bill_id = bill_id, gender= 'M').count()
        femaleno = Participant.objects.filter(bill_id = bill_id, gender= 'F').count()

        if bill_ob.draft_number:
            ddno = bill_ob.draft_number
        else:
            ddno = '-'

        context = {
        'college': college,
        'receiptno' : bill_id,
        'amount' : total,
        'grpcode' : grpcode,
        'maleno' : maleno,
        'femaleno' : femaleno,
        'given' : bill_ob.given,
        'balance' : bill_ob.balance,
        'ddno' : ddno,

        }

        return render_to_response('regsoft/receipt.html', context)




def controlz_delete_bill(request):
    if request.POST:
        bill_idlist = request.POST.getlist('bill_id') 
        for bill_id in bill_idlist:
            bill_id = int(bill_id)
            bill_ob = Bill.objects.get(id = bill_id)
            plist = Participant.objects.filter(bill_id = bill_id)
            for part in plist:
                part.bill_id = 0
                part.controlz = False
                part.save()
            bill_ob.delete()

        return HttpResponseRedirect('../bill_delete')
 

    bills = Bill.objects.all()
    details = []
    for bill in bills:
        try:
            gl = gleader.objects.get(id = bill.gleader)
        except:
            gl = None
            # bill.save()
            # return HttpResponse(" Contact Satwik : 9928823099")
        partno = Participant.objects.filter(bill_id= bill.id).count()
        details.append( (bill,gl,partno) )

    context ={
    'details' : details,
    }
    return render(request, 'regsoft/controlz_bill_delete.html', context)

def controlz_view_bill(request, billid):
    bill = Bill.objects.get(id=billid)
    gleaderid = bill.gleader
    leader = gleader.objects.get(id=gleaderid)
    participants = Participant.objects.filter(bill_id=billid)

    context = {
        'participants' : participants,
        'bill' : bill,
        'gleader' : leader,
    }

    return render(request, 'regsoft/controlz_bill_view.html', context)
































# @csrf_exempt
# def controlz_home(request):
#   if request.POST:
#       try:
#           encoded = str( request.POST['code'] )
#           decoded = int(encoded[-4:]) #taking alternative character because alphabets were random and had no meaning

#       except:
#           return render(request, 'regsoft/controlz_home.html', {'status' : 0})
#       return HttpResponseRedirect("../home/" + str(decoded) )

#   return render(request, "regsoft/controlz_home.html")



# def controlz_dashboard(request,part_id):
#     part_ob = Participant.objects.filter(id = part_id)
#     if part_ob:
#         part_ob = part_ob[0]
#         if part_ob.controlz == True:
#             bill = Bill.objects.filter(participant=part_ob)[0]
#             bill_id = bill.id
#             context= {'part': part_ob, 'bill_id':bill_id}
#         else:
#             context = {'part':part_ob}
#         return render(request, 'regsoft/controlz_dashboard.html', context)
#     else:
#         return render(request, 'regsoft/controlz_home.html', {'status' : 0})





# # def controlz_edit_part(request, part_id):
# #   if request.POST:
# #       init_ob = InitialRegistration.objects.get(id = part_id)
# #       init_ob.name = str(request.POST['name'])
# #       init_ob.email_id = str(request.POST['email'])
# #       init_ob.phone_one = int(request.POST['phone'])
# #       init_ob.gender = str(request.POST['gender'])

# #       init_ob.events.clear()
# #       if request.POST.get('events', False):
# #           for k in request.POST.getlist('events'):                                    
# #               event = Event.objects.get(pk=k)
# #               init_ob.events.add(event)
# #       init_ob.save()

# #       gl = init_ob.grpleader
# #       return HttpResponseRedirect('../home/' + str(gl.id) )


# #   init_ob = InitialRegistration.objects.get(id= part_id)
# #   elist = Event.objects.all()
# #   gl = init_ob.grpleader
# #   return render(request, 'regsoft/controlz_edit.html' , {'part' : init_ob, 'events' : elist, 'gl' : gl})



# def controlz_bill_select(request, part_id):
#     if request.POST:
#         part_ob = Participant.objects.get(id=part_id)
# #       pidlist = request.POST.getlist('part')
# #       plist= []
# #       is_faculty= 0
# #       onlinepaid=0
# #       for k in pidlist:
# #           k= int(k)
# #           part = InitialRegistration.objects.get(id=k)
# #           plist.append(part)
# #           if part.is_faculty == True:
# #               is_faculty+=1
# #           if part.reg_paid == True:
# #               onlinepaid+=1

# #       totalamt= onlinepaid*500
#         if part_ob.fee_paid == True:
#             check = 1
#         elif part_ob.fee_paid == False:
#             check = 2

# #       gl = plist[0].grpleader
# #       total = len(plist) 
# #       totalamt += (total- is_faculty - onlinepaid) * 750
# #       pcount = (total - is_faculty - onlinepaid)
#         context ={
#             'part_ob' : part_ob, 
#             'check' : check,
# #       'plist' : plist,
# #       'facultyno' : is_faculty,
# #       'total' : total,
# #       'totalamt' : totalamt,
# #       'onlinepaid' : onlinepaid,
# #       'pcount' : pcount,
#         }

#         return render(request, 'regsoft/controlz_bill_amt.html', context)


# ###### SATWIK MAKE MIGRATIONS AND UNCOMMEN THE BELOW CODE ONCE also UNCOMMENT THE URLS
# def controlz_bill_details(request,part_id):
#     if request.POST:
# #       pidlist= str(request.POST['pidlist'])
# #       gl_id = gl_id
#         part_ob = Participant.objects.get(id=part_id)
# #       college = gl.details.college
# #       femaleno =0
# #       maleno  =0
# #       pidlistx = pidlist.split(',')
# #       pidlist = pidlist.split(',')
# #       onlinepaid = 0
# #       is_faculty=0
# #       for k in pidlist:
# #           if k != '' :
# #               k=int(k)
# #               part = InitialRegistration.objects.get(id =k)
# #               part.controlz = True
# #               if part.gender == 'M':
# #                   maleno+=1
# #               else:
# #                   femaleno+=1

# #               if part.is_faculty:
# #                   is_faculty+=1
# #               if part.reg_paid:
# #                   onlinepaid+=1
# #               part.save()
        
#         if part_ob.fee_paid == False:
#             ddno = request.POST.get('ddno' ,  False)
#             n1000 = int(request.POST.get('n_1000',0) )
#             n500 = int(request.POST.get('n_500',      0) )
#             n100 = int(request.POST.get('n_100',      0) )
#             n50 = int(request.POST.get('n_50',        0) )
#             n20 = int(request.POST.get('n_20',        0) )
#             n10 = int(request.POST.get('n_10' ,      0) )


# #       # totalamt = 1000*n1000 + 500*n500 + 100*n100 + 50*n50 + 20*n20 + 10*n10


#             balance = 0
#             given=0
#             if n1000 < 0:
#                 balance += -(n1000) * 1000
#             else:
#                 given+= n1000 * 1000


#             if n500 < 0:
#                 balance += -(n500) * 500
#             else:
#                 given+= n500 * 500


#             if n100 < 0:
#                 balance += -(n100) * 100
#             else:
#                 given+= n100 * 100


#             if n50 < 0:
#                 balance += -(n50) * 50
#             else:
#                 given+= n50 * 50


#             if n20 < 0:
#                 balance += -(n20) * 20 
#             else:
#                 given+= n20 * 20     

#             if n10 < 0:
#                 balance += -(n10) * 10 
#             else:
#                 given+= n10 * 10                                                     
                



#             total = request.POST.get('total', 0)
#             if total == '':
#                 total = 0   
#             if ddno:
#                 newbill = Bill(participant = part_ob, amount= total, given=given, balance=balance, draft_number= ddno)
#             else:
#                 newbill = Bill(participant = part_ob, amount= total, given=given, balance=balance)
#                 ddno= 'None'

#             newbill.save()
#             part_ob.controlz = True
#             part_ob.save()
# #         test = []
# #         for k in pidlistx:
# #             if k != '' :
# #                 k=int(k)
# #                 part = InitialRegistration.objects.get(id =k)
# #                 part.bill_id = int(newbill.id)
# #                 test.append({part.name, newbill.id})
# #                 part.save()

                
#             newbill.notes_1000 = int(n1000)
#             newbill.notes_500 = int(n500)
#             newbill.notes_100 = int(n100)
#             newbill.notes_50 = int(n50)
#             newbill.notes_20 = int(n20)
#             newbill.notes_10 = int(n10)
#             newbill.save()


# #       # return HttpResponse(test)
#             context={
#                 'part_ob' : part_ob,
#                 'given' : given,
#                 'balance' : balance, 
#                 'total' : total,
#                 'bill_id' : newbill.id,
#                 'ddno' : ddno,
#             }


#             return render(request, 'regsoft/controlz_bill_details.html', context)

#         elif part_ob.fee_paid == True:
#             newbill = Bill(participant = part_ob, amount= 800, given= 800, balance= 0, draft_number= 'None')
#             newbill.save()
#             part_ob.controlz = True
#             ddno='None'
#             context={
#                 'part_ob' : part_ob,
#                 'bill_id' : newbill.id,
#                 'ddno' : ddno,
#             }
#             return render(request, 'regsoft/controlz_bill_details.html', context)



# def controlz_bill_print(request):
#     if request.POST:
#         bill_id = int(request.POST['bill_id'])
#         bill_ob = Bill.objects.get(id=bill_id)
#         part_ob = bill_ob.participant
#         if part_ob.fee_paid == False:
#             college = part_ob.college
#             receiptno = bill_ob.id
#             total = bill_ob.amount

#             if bill_ob.draft_number:
#                 ddno = bill_ob.draft_number
#             else:
#                 ddno = '-'

#             context = {
#                 'college': college,
#                 'receiptno' : bill_id,
#                 'amount' : total,
#                 'given' : bill_ob.given,
#                 'balance' : bill_ob.balance,
#                 'ddno' : ddno,
#             }

#             return render_to_response('regsoft/receipt_offline.html', context)
#         elif part_ob.fee_paid == True:
#             total= '800'
#             context = {
#                 'college': part_ob.college,
#                 'receiptno' : bill_id,
#                 'amount' : total,
#             }

#             return render_to_response('regsoft/receipt_online.html', context)



# def controlz_delete_bill(request):
#     if request.POST:
#         bill_idlist = request.POST.getlist('bill_id') 
#         for bill_id in bill_idlist:
#             bill_id = int(bill_id)
#             bill_ob = Bill.objects.get(id = bill_id)
#             try:
#                 part= bill_ob.participant
#                 part.controlz = False
#                 part.save()
#             except:
#                 dumpvar=0
#             bill_ob.delete()
#         return HttpResponseRedirect('../bill_delete')
#     bills = Bill.objects.all()
#     details = []
#     for bill in bills:
#       try:
#           part = bill.participant
#       except:
#           part = None
#           # bill.save()
#           # return HttpResponse(" Contact Satwik : 9928823099")
#       details.append( (bill,part) )

#     context ={
#     'details' : details,
#     }
#     return render(request, 'regsoft/controlz_bill_delete.html', context)

# def controlz_view_bill(request, billid):
#     bill = Bill.objects.get(id=billid)
#     part = bill.participant 

#     context = {
#       'part' : part,
#       'bill' : bill,
#     }

#     return render(request, 'regsoft/controlz_bill_view.html', context)




# ##### Recnacc ###################



@csrf_exempt
def recnacc_home(request):
    if request.POST:
        try:
            encoded = str( request.POST['code'] )
            decoded = int(encoded[-4:]) #taking alternative character because alphabets were random and had no meaning

        except:
            return render(request, 'regsoft/recnacc_home.html', {'status' : 0})
        return HttpResponseRedirect("../home/" + str(decoded) )


    return render(request, "regsoft/recnacc_home.html")


def recnacc_notify(request):
    gl_list = gleader.objects.all()
    res = {}
    res['gauss'] =[]
    for gl in gl_list:
        temp = {}
        if gl.participant_set.filter(firewallzo= True, recnacc= False).count() or gl.participant_set.filter(firewallzo= True, controlz= False).count():
            temp['glname'] = gl.details.name
            temp['college'] = str(gl.details.college)
            temp['groupcode']  = gl.groupcode
            temp['phone'] = gl.details.phone_one
            partmalenolist = Participant.objects.filter(grpleader = gl, gender='M')
            partfemalenolist = Participant.objects.filter(grpleader = gl, gender='F')
            partmaleno = 0
            partfemaleno = 0
            facmaleno = 0
            facfemaleno = 0
            for x in partmalenolist:
                partmaleno += 1
            for x in partfemalenolist:
                partfemaleno += 1

            temp['partno'] = str(partmaleno)
            temp['facno'] = str(facmaleno)

            res['gauss'].append(temp)
            return HttpResponse(json.dumps(res), content_type="application/json")
    


def recnacc_dashboard(request,gl_id):
    gl_ob = gleader.objects.filter(id = gl_id)
    
    if gl_ob:
        gl_ob = gl_ob[0]
        plistfinal_two = []
        plistfinal_participant = []
        plist_participant = []
        plist_faculty = []
        plist_participant = gl_ob.participant_set.filter(firewallzo =True, recnacc=False)
        maleno_participant = 0
        maleno_two = 0
        femaleno_participant = 0
        femaleno_two = 0
        for x in plist_participant:
            plistfinal_participant.append(x)
            if x.gender == 'M':
                maleno_participant += 1
            else:
                femaleno_participant += 1
        
        plist_two = gl_ob.participant_set.filter(firewallzo =True, recnacc=True)
        for x in plist_two:
            if x.room.room != "Checkout":
                plistfinal_two.append(x)
                if x.gender == 'M':
                    maleno_two += 1
                else:
                    femaleno_two += 1
        # maleno = Ini.participanttion.objects.filter(grpleader = gl_ob, gender= 'M', firewallzo= True, recnacc=False).count()
        # femaleno = InitialRegistration.objects.filter(grpleader = gl_ob, gender= 'F', firewallzo= True, recnacc=False).count()
        # maleno_two = InitialRegistration.objects.filter(grpleader = gl_ob, gender= 'M', firewallzo= True, recnacc=True).count()
        # femaleno_two = InitialRegistration.objects.filter(grpleader = gl_ob, gender= 'F', firewallzo= True, recnacc=True).count()
        # for p in plist_two:
        #     p.bhavan = p.room+' '+p.room.bhavan.name
            
        
        context ={
        'gl' : gl_ob, 
        'plist_participant' : plistfinal_participant,
        'plist_two' : plistfinal_two,
        'maleno_participant' : maleno_participant,
        'femaleno_participant' : femaleno_participant,
        'maleno_two' : maleno_two,
        'femaleno_two' : femaleno_two,
        
        }

        return render(request, 'regsoft/recnacc_dashboard.html', context)

    else:
        return render(request, 'regsoft/recnacc_home.html', {'status' : 0})

@csrf_exempt
def recnacc_allot(request,gl_id):

  #list acco with availibilty
  #ability to select
    try:
        gleader.objects.get(id = gl_id)
    except:
        return HttpResponse('Please Check if firewallz has not unconfirmed this user. Check Notifications and if it still shows the group code then call Kunal.')
    bhavan_list= Bhavan.objects.all()
    initial_vacancy_display= []
    vacancy_display = []
    all_rooms = []
    for bhavan in bhavan_list:
        if bhavan.id != 1:
            bhavan_name = bhavan.name
            rooms = [x for x in bhavan.room_set.all()]
            all_rooms += rooms
            if len(rooms):
                vacancy_display.append((bhavan_name,rooms))
        gl = gleader.objects.filter(id = gl_id)[0]
    participant_list = gl.participant_set.all() 
    no_males=0
    no_females=0
    for p in participant_list:
        if p.gender[0].upper()=="M" and p.firewallzo ==True and p.recnacc!=True:
            no_males+=1
        elif p.gender[0].upper()=="F" and p.firewallzo ==True and p.recnacc!=True:
            no_females+=1
    if request.POST:
        try:
            request.POST.getlist('roomid')
        except:
            error="Invalid Room Selected"
            context = RequestContext(request)
            context_dict = {'error':error}
            return render_to_response('regsoft/recnacc_acco.html', context_dict, context)
        for roomid in request.POST.getlist('roomid'):
          # roomid=request.POST.getlist('roomid')
            
            x = roomid + 'alloted'
            noalloted=int(request.POST.get(x, False)) 
            # noa = 'a'+roomid
            # nob = 'b'+roomid
            # noc = 'c'+roomid
            # nod = 'd'+roomid
            # noe = 'e'+roomid
            # nof = 'f'+roomid

            roomid = int(roomid)
            no_males=0
            no_females=0
            
            # selectedroom = Room.objects.get(id=roomid)         
            # a_no=int(request.POST.get(noa, False))
            # if a_no == '':
            #     a_no =0 
            # b_no=int(request.POST.get(nob, False))
            # if b_no == '':
            #     b_no =0
            # c_no=int(request.POST.get(noc, False))
            # if c_no == '':
            #     c_no =0
            # d_no=int(request.POST.get(nod, False))
            # if d_no == '':
            #     d_no =0
            # e_no=int(request.POST.get(noe, False))
            # if e_no == '':
            #     e_no =0
            # f_no=int(request.POST.get(nof, False))
            # if f_no == '':
            #     f_no =0
            
            # selectedbhavan = Bhavan.objects.get(id = selectedroom.bhavan.id)
            # selectedbhavan.a_capacity -= a_no
            # selectedbhavan.b_capacity -= b_no
            # selectedbhavan.c_capacity -= c_no
            # selectedbhavan.d_capacity -= d_no
            # selectedbhavan.e_capacity -= e_no
            # selectedbhavan.f_capacity -= f_no
            # selectedbhavan.save()
            # # selectedroom.bhavan.a_capacity -= a_no
            # # selectedroom.bhavan.b_capacity -= b_no
            # # selectedroom.bhavan.c_capacity -= c_no
            # # selectedroom.bhavan.d_capacity -= d_no
            # # selectedroom.bhavan.e_capacity -= e_no
            # # selectedroom.bhavan.f_capacity -= f_no

            # # selectedroom.save()
            # if Inventory.objects.filter(room = selectedroom, gl_id = gl_id):
            #     inob = Inventory.objects.filter(room = selectedroom, gl_id = gl_id)[0]
            #     inob.a += a_no
            #     inob.b += b_no
            #     inob.c += c_no
            #     inob.d += d_no
            #     inob.e += e_no
            #     inob.f += f_no
            #     inob.save()

            # else:
            #     ilist = Inventory()
            #     ilist.a = a_no
            #     ilist.b = b_no
            #     ilist.c = c_no
            #     ilist.d = d_no
            #     ilist.e = e_no
            #     ilist.f = f_no
            #     ilist.room = selectedroom
            #     ilist.gl_id = gl_id
            #     ilist.save()        

            
            
            for p in participant_list:
                if p.gender[0].upper()=="M" and p.firewallzo ==True and p.recnacc!=True:
                    no_males+=1
                elif p.gender[0].upper()=="F" and p.firewallzo ==True and p.recnacc!=True:
                    no_females+=1
            selectedroom = Room.objects.get(id=roomid) 
            selectedroom_availibilty = selectedroom.vacancy
            unalloted_males = [x for x in participant_list if x.firewallzo == True and x.gender[0].upper() == 'M' and x.recnacc != True]
            unalloted_females = [x for x in participant_list if x.firewallzo == True and x.gender[0].upper() == 'F' and x.recnacc != True]
            if selectedroom.bhavan.name == 'MB' or selectedroom.bhavan.name == 'MB-1' or selectedroom.bhavan.name == 'MB-3' or selectedroom.bhavan.name == 'MB-4' or selectedroom.bhavan.name == 'MB 5' or selectedroom.bhavan.name == 'MB 6-1' or selectedroom.bhavan.name == 'MB 6-3' or selectedroom.bhavan.name == 'MB-7' or selectedroom.bhavan.name == 'MB-8' or selectedroom.bhavan.name == 'MB-9' : #use or for extra bhavanas
                if no_females<noalloted:
                    return HttpResponse('error: Alloted rooms are greater than the number of participants. <br /> <a href="http://www.bits-apoogee.org/2016/recnacc/allot/%s/">Back</a>' % gl_id)
                for y in range(noalloted):
                    unalloted_females[y].recnacc=True
                    unalloted_females[y].room = selectedroom
                    selectedroom.vacancy -= 1
                    selectedroom.save()
                    unalloted_females[y].save()
            
            else:
                if no_males<noalloted:
                    return HttpResponse('error: Alloted rooms are greater than the number of participants. <br /> <a href="http://www.bits-apogee.org/2016/recnacc/allot/%s/">Back</a>' % gl_id)
                for y in range(noalloted):
                    unalloted_males[y].recnacc=True
                    unalloted_males[y].room = selectedroom
                    selectedroom.vacancy -= 1
                    selectedroom.save()
                    unalloted_males[y].save()
        #return HttpResponse(selectedroom.vacancy)
            bal = noalloted*300
            gl.amount_taken += bal
            gl.save()
        no_males=0
        no_females=0
        participant_list = gl.participant_set.all()
        for p in participant_list:
            if p.gender[0].upper()=="M" and p.firewallzo ==True and p.recnacc!=True:
                no_males+=1
            elif p.gender[0].upper()=="F" and p.firewallzo ==True and p.recnacc!=True:
                no_females+=1
            bhavan_list= Bhavan.objects.all()
            all_rooms =[]
            blist = [ x for x in bhavan_list if x.id != 1]
            for bhavan in bhavan_list:
                if bhavan.id != 1:  
                    bhavan_name = bhavan.name
                    rooms = [x for x in bhavan.room_set.all() if x.vacancy != 0]
                    all_rooms += rooms
                    if len(rooms):
                        vacancy_display.append((bhavan_name,rooms))
        done_participants = [x for x in participant_list if x.firewallzo==True and x.recnacc==True]
        context = RequestContext(request)
        context_dict = {'done_participants':done_participants, 'blist':blist,'all_rooms':all_rooms,'no_males':no_males, 'no_females':no_females,"gl":gl, 'vacancy_display':vacancy_display}
        return render_to_response('regsoft/recnacc_acco.html', context_dict, context)

    else:
        bhavan_list = Bhavan.objects.all()
        blist = [x for x in bhavan_list if x.id != 1]
        done_participants = [x for x in participant_list if x.firewallzo==True and x.recnacc==True]
        context = RequestContext(request)
        context_dict = {'done_participants':done_participants, 'blist':blist, 'all_rooms':all_rooms,'vacancy_display':vacancy_display, 'no_males':no_males, 'no_females':no_females, "gl":gl}
        return render_to_response('regsoft/recnacc_acco.html', context_dict, context)

@csrf_exempt
def recnacc_deallocate(request,gl_id):
    gl = gleader.objects.get(id=gl_id)
    alloted_people = Participant.objects.filter(firewallzo= True, recnacc= True, grpleader= gl)
    alist=[]
    for x in alloted_people:
        if x.room.id != 1:
            alist.append(x)
    if request.POST:
        try:
            list_of_people_selected = request.POST.getlist('deallocate')
        except:
            return HttpResponse('No one was selected')
        selected_people_list = [int(x) for x in list_of_people_selected]
        done_people = []
        for x in selected_people_list:
            p= Participant.objects.get(id=x)
            p.recnacc = False
            if p.room:
                selected_room = p.room
                selected_room.vacancy += 1
                selected_room.save()
                p.room = None
                p.save()
                done_people.append(p)
                gl.amount_taken -= 300
                gl.save()
        alloted_people = Participant.objects.filter(firewallzo= True, recnacc= True, grpleader= gl)
        alist=[]
        for x in alloted_people:
            if x.room.id != 1:
                alist.append(x)
        context = RequestContext(request)
        context_dict = {'done_people':done_people, 'alloted_people':alist,"gl":gl}
        return render_to_response('regsoft/recnacc_deallocate.html', context_dict, context)
    else:
        done_people = []
        context = RequestContext(request)
        context_dict = {'done_people':done_people, 'alloted_people':alist,"gl":gl}
        return render_to_response('regsoft/recnacc_deallocate.html', context_dict, context)

@csrf_exempt
def recnacc_checkout(request,gl_id):
  #simple template to enter id
    postcheck = False
    if request.POST:
        postcheck = True
        try:
            list_of_people_selected = request.POST.getlist('checkout')
        except:
            return HttpResponse('error')
        selectedpeople_list = [int(x) for x in list_of_people_selected]
        display_table = []
        for x in selectedpeople_list:
            participant = Participant.objects.get(id=x)
            participant_room = participant.room
            participant_room.vacancy += 1
            participant_room.save()
            participant.room = Room.objects.get(id=1)
            croom = Room.objects.get(id=1)
            croom.vacancy -= 1
            croom.save()
            participant.save()
          # participant_name = str(participant.name) 
          # participant_gender = str(participant.gender)[0].upper()
          # if len(participant.events.all()): #checks if the participant has the event otherwise the lenth of the list will be zero
          #         participant_event = str(participant.events.all()[0].name)
          # else:
          #     participant_event = ''
            display_table.append(participant)
        gl = gleader.objects.get(id=gl_id)
        amt_ret = request.POST['amt_ret']
        amt_ret = int(amt_ret)
        gl.amount_deducted += amt_ret
        gl.save()
        participant_list = gl.participant_set.all() 
        final_participants = [x for x in participant_list if x.firewallzo==True and x.recnacc==True and x.room.bhavan.id != 1]
        context = RequestContext(request)
        context_dict = {'gl':gl,'display_table':display_table, 'postcheck':postcheck, 'final_participants':final_participants}
        return render_to_response('regsoft/recnacc_checkout.html', context_dict, context)


    else:
        gl = gleader.objects.get(id=gl_id)
        participant_list = gl.participant_set.all() 
      #college = str(gl.college)
      #gl_name = str(gl.firstname + ' ' + gl.lastname)
        final_participants = [x for x in participant_list if x.firewallzo==True and x.recnacc==True and x.room.bhavan.id != 1]
        context = RequestContext(request)
        context_dict = {'final_participants':final_participants, 'gl':gl}
        return render_to_response('regsoft/recnacc_checkout.html', context_dict, context)



















def encode_glid(gl_id):
    gl_ida = '0'*(4-len(str(gl_id)))+str(gl_id)
    mixed = string.ascii_uppercase + string.ascii_lowercase
    count = 51
    encoded = ''
    for x in gl_ida:
        encoded = encoded + x
        encoded = encoded + mixed[randint(0,51)]
    return encoded
def get_barcode(request):
    list_of_people_selected = Participant.objects.filter(pcr_approval=True).order_by('college__name')
    final_display = []
    for x in list_of_people_selected:
        name = x.name
        college = x.college.name
        pid= x.id
        encoded = encode_glid(pid)
        final_display.append((name,college,encoded, pid))
    context = RequestContext(request)
    context_dict = {'final_display':final_display}
    return render_to_response('regsoft/get_barcode.html', context_dict, context)





@csrf_exempt
def recnacc_room_list(request):
    rooms = Room.objects.all()
    plist = []
    for x in rooms:
        prtno = Participant.objects.filter(room = x).count()
        if x.id != 1:
            plist.append({"name":x.bhavan.name,"room":x.room,"participants":prtno,"id":x.id, "a":x.a,"b":x.b,"c":x.c,"d":x.d,"e":x.e,"f":x.f})

    context = RequestContext(request)
    context_dict = {'plist':plist}
    return render(request,'regsoft/recnacc_room_participants_list.html', context_dict)

@csrf_exempt
def recnacc_room_details(request, room_id):
    room = Room.objects.get(id = room_id)
    plist = Participant.objects.filter(room = room)
    # plist = []
    # for x in rooms:
    #   prtno = InitialRegistration.objects.filter(room = x).count()
    #   plist.append({x.bhavan.name,x.room,prtno})
    context = RequestContext(request)
    context_dict = {'plist':plist,'room':room}
    # return HttpResponse(plist)
    return render_to_response('regsoft/recnacc_room_participants_details.html', context_dict, context)

@csrf_exempt
def recnacc_checked_out_participants_in(request, gl_id):
    gl = gleader.objects.get(id = gl_id)
    if request.method == "POST":
        amtded = request.POST['amt_ded']
        gl.amount_deducted = amtded
        gl.save()
        prtlist = gl.participant_set.filter(room = 1)
        context_dict = {'prtlist':prtlist, 'gl':gl}
        context = RequestContext(request)
        return render_to_response('regsoft/recnacc_checked_out_participants_in.html', context_dict, context)
    else:
        prtlist = gl.participant_set.filter(room = 1)
        context_dict = {'prtlist':prtlist, 'gl':gl}
        context = RequestContext(request)
        return render_to_response('regsoft/recnacc_checked_out_participants_in.html', context_dict, context)


@csrf_exempt
def recnacc_bill_print(request, gl_id):
    gl = gleader.objects.get(id = gl_id)
    plist = gl.participant_set.filter(firewallzo=True, recnacc=True)
    prtlist = []
    for x in plist:
        if x.room.id != 1:
            prtlist.append(x)


    maleno = gl.participant_set.filter(gender= 'M', recnacc=True)
    femaleno = gl.participant_set.filter(gender= 'F', recnacc=True)
    malelist = 0
    femalelist = 0
    for x in maleno:
        if x.room.id != 1:
            malelist += 1
    for x in femaleno:
        if x.room.id != 1:
            femalelist += 1

    total_ppl = malelist + femalelist
    totalamt = total_ppl*300
    context = {
        'gl': gl,
        'prtlist' : prtlist,
        'maleno' : malelist,
        'femaleno' : femalelist,
        'totalamt' : totalamt,
        }

    return render_to_response('regsoft/receipt_recnacc.html', context)





def recnacc_bill_list(request):
    gl = gleader.objects.all()
    gllist = []
    for x in gl:
        if x.details.recnacc == True and Participant.objects.filter(grpleader= x).count():
            gllist.append(x)
    context = RequestContext(request)
    context_dict = {'gllist':gllist}
    return render_to_response('regsoft/controlz_recnacc_bill_print.html', context_dict, context)








# def certi_gen_txt(request):
#   # fopen =  open('/home/dvm/satwik_certitest/event_rap.txt', 'w')
#   # event_ob = Event.objects.get(name = 'Rap Wars')
#   # for tm in Team.objects.filter(event = event_ob,is_finalist=True):
#   # # for k in InitialRegistration.objects.filter(events = event_ob, controlz= True):
#   #   members_ob = tm.members.all()
#   #   # if tm.:
#   #   # if tm.is_winner:
#   #   for k in members_ob:
#   #       fopen.write(str(k.name.upper() ) + '$' + str(k.college) + '$Rap Wars$' + str(tm.position) + '\n'  )
#   # fopen.close()


#   fopen =  open('/home/dvm/satwik_certitest/event_winy.txt', 'w')
#   # event_ob = Event.objects.get(name = 'Street Dance')
#   winners= Team.objects.filter(is_winner=True)
#   for tm in winners:
#   # for k in InitialRegistration.objects.filter(events = event_ob, controlz= True):
#       members_ob = tm.members.all()
#       members_ob_bits = tm.bitsian_members.all()
#       for k in members_ob:
#           fopen.write(str(k.name.upper() ) + '$' + str(k.college) + '$' + str(tm.event) +'$' + str(tm.position)+'\n'  )

#       for k in members_ob_bits:
#           fopen.write(str(k.name.upper() ) + '$' + str(k.college) + '$' + str(tm.event) +'$' + str(tm.position)+'\n'  )
        
#       # if tm.:
#       # if tm.is_winner:
#   fopen.close()


#   fopen =  open('/home/dvm/satwik_certitest/event_finx.txt', 'w')
#   # event_ob = Event.objects.get(name = 'Street Dance')
#   finalists=Team.objects.filter(is_finalist=True)
#   for tm in finalists:
#   # for k in InitialRegistration.objects.filter(events = event_ob, controlz= True):
#       members_ob = tm.members.all()
#       members_ob_bits = tm.bitsian_members.all()
#       for k in members_ob:
#           fopen.write(str(k.name.upper() ) + '$' + str(k.college) + '$' + str(tm.event) +'$' + str(tm.position)+'\n'  )

#       for k in members_ob_bits:
#           fopen.write(str(k.name.upper() ) + '$' + str(k.college) + '$' + str(tm.event) +'$' + str(tm.position)+'\n'  )
        
#       # if tm.:
#       # if tm.is_winner:
#   fopen.close()


#   # fopen =  open('/home/dvm/satwik_certitest/event_fashP.txt', 'w')
#   # event_ob = Event.objects.get(name = 'FashP')

#   # # for tm in Team.objects.filter(is_winner=True):
#   # for k in InitialRegistration.objects.filter(events = event_ob, controlz= True):
#   #   fopen.write(str(k.name.upper() ) + '$' + str(k.college) + '$FashP' +'\n'  )
#   #   # members_ob = tm.members.all()
#   #   # if tm.:
#   #   # if tm.is_winner:
#   #   # for k in members_ob:
#   # fopen.close()




#   # fopen =  open('/home/dvm/satwik_certitest/event_tarang_pos.txt', 'w')
#   # event_ob = Event.objects.get(name = 'Tarang')
#   # # for k in Team.objects.filter(event = event_ob):
#   # for k in InitialRegistration.objects.filter(events = event_ob, controlz= True):
#   #   # members_ob = k.members.all()
#   #   # for init_ob in members_ob:
#   #   fopen.write(str(k.name.upper() ) + '$' + str(k.college) + '$Andholika\n'   )
#   # fopen.close()

#   # fopen =  open('/home/dvm/satwik_certitest/eventpart_splay.txt', 'w')
#   # event_ob1 = Event.objects.get(name = 'Stage Play')
#   # # for k in Team.objects.filter(event = event_ob):
#   # for k in InitialRegistration.objects.filter(events = event_ob1, controlz= True):
#   #   fopen.write(str(k.name.upper() ) + '$' + str(k.college) + '$Stage Play\n'   )
#   #   # members_ob = k.members.all()
#   #   # for init_ob in members_ob:
    
#   # fopen.close()


#   # fopen =  open('/home/dvm/satwik_certitest/eventpart_mime.txt', 'w')
#   # event_ob1 = Event.objects.get(name = 'Mime')
#   # # for k in Team.objects.filter(event = event_ob):
#   # for k in InitialRegistration.objects.filter(events = event_ob1, controlz= True):
#   #   # members_ob = k.members.all()
#   #   # for init_ob in members_ob:
#   #   fopen.write(str(k.name.upper() ) + '$' + str(k.college) + '$Mime\n'   )
#   # fopen.close()






#   # fopen =  open('/home/dvm/satwik_certitest/eventpartR.txt', 'w')
#   # event_ob2 = Event.objects.get(name = 'Razzmatazz')
#   # # for k in Team.objects.filter(event = event_ob):
#   # for k in InitialRegistration.objects.filter(events = event_ob2, controlz= True):
#   #   # members_ob = k.members.all()
#   #   # for init_ob in members_ob:
#   #   fopen.write(str(k.name.upper() ) + '$' + str(k.college) + '$Razzmatazz\n'   )
#   # fopen.close()

#   # fopen =  open('/home/dvm/satwik_certitest/eventpartD.txt', 'w')
#   # event_ob3 = Event.objects.get(name = 'Oasis Debate')
#   # # for k in Team.objects.filter(event = event_ob):
#   # for k in InitialRegistration.objects.filter(events = event_ob3, controlz= True):
#   #   # members_ob = k.members.all()
#   #   # for init_ob in members_ob:
#   #   fopen.write(str(k.name.upper() ) + '$' + str(k.college) + '$Oasis Debate\n'   )
#   # fopen.close()

#   return HttpResponse('Done : Gauss')















# #BOSM 2015 CODE

# # @csrf_exempt
# # def firewallzo_gl(request): #team details editable on first view
# #     #add gl_name to context dict
# #     if request.POST:
# #         if str(request.POST['formtype']) == 'finalform':
# #             list_of_people_selected = request.POST.getlist('left')
# #             selectedpeople_list = [int(x) for x in list_of_people_selected]
# #             display_table = []
# #             for x in selectedpeople_list:
# #                 participant = Participant.objects.get(id=x)
# #                 participant.firewallz = True
# #                 participant.save()
# #                 participant_name = str(participant.name)
# #                 participant_gender = str(participant.gender)[0].upper()
# #                 if len(participant.events.all()): #checks if the participant has the event otherwise the lenth of the list will be zero
# #                         participant_event_list = [x.name for x in participant.events.all()]
# #                         participant_event = ','.join(participant_event_list)
# #                 else:
# #                     participant_event = ''
# #                 display_table.append((participant_name,participant_gender,participant_event))
# #             context = RequestContext(request)
# #             context_dict = {'display_table':display_table}
# #             return render_to_response('firewallzo_checkout.html', context_dict, context)

# #         try:
# #             encoded=request.POST['code']
# #             decoded = encoded[0]+encoded[2]+encoded[4]+encoded[6] #taking alternative character because alphabets were random and had no meaning
# #             gl_id = int(decoded) #to remove preceding zeroes and get user profile
# #             gl = UserProfile.objects.get(id=gl_id)
# #         except:
# #             error="Invalid code entered " +encoded
# #             context = RequestContext(request)
# #             context_dict = {'error':error}
# #             return render_to_response('firewallzo_home.html', context_dict, context)

# #         participant_list = gl.user.participant_set.all() 
# #         college = str(gl.college)
# #         gl_name = str(gl.firstname) + ' ' + str(gl.lastname)
# #         display_participants = []
# #         done_participants = []
# #         for p in participant_list:
# #             participant_name = str(p.name) 
# #             participant_gender = str(p.gender)[0].upper()#for using just M or F instead of fulll to save space.
# #             participant_id = int(p.id)
# #             if len(p.events.all()): #checks if the participant has the event otherwise the lenth of the list will be zero
# #                 participant_event_list = [x.name for x in p.events.all()]
# #                 participant_event = ','.join(participant_event_list)
# #             else:
# #                 participant_event = '' #done because faculty is not assigned any event
# #             if p.firewallz != True: #list only particiants whose case is not finalized
# #                 display_participants.append((participant_name,participant_gender,participant_id,participant_event))
# #             else:
# #                 done_participants.append((participant_name,participant_gender,participant_id,participant_event))

# #         context = RequestContext(request)
# #         context_dict = {'display_participants': display_participants, 'college':college, 'gl_name':gl_name,'done_participants':done_participants,'gl':gl}
# #         return render_to_response('firewallzo_gl.html', context_dict, context)
# #     else:
# #         context = RequestContext(request)
# #         error = ''
# #         context_dict = {'error':error}
# #         return render_to_response('firewallzo_home.html', context_dict, context)

# # def encode_glid(gl_id):
# #     gl_ida = '0'*(4-len(str(gl_id)))+str(gl_id)
# #     mixed = string.ascii_uppercase + string.ascii_lowercase
# #     count = 51
# #     encoded = ''
# #     for x in gl_ida:
# #         encoded = encoded + x
# #         encoded = encoded + mixed[randint(0,51)]
# #     return encoded
# # def get_barcode(request):
# #     ''' list_of_people_selected = InitialRegistration.objects.all()
# #     # list_of_people_selected = [x for x in list_of_people_selected if x.user]'''
# #     list_of_people_selected = UserProfile.objects.all()
# #     list_of_people_selected = [x for x in list_of_people_selected]
# #     final_display = []
# #     for x in list_of_people_selected:
# #         gl_id = x.id
# #         name = x.firstname + ' ' + x.lastname
# #         college = x.college
# #         encoded = encode_glid(gl_id)
# #         final_display.append((name,college,encoded))
# #     context = RequestContext(request)
# #     context_dict = {'final_display':final_display}
# #     return render_to_response('get_barcode.html', context_dict, context)

# # def showteam(request,gl_id): #shows team members who have checked in from firewallz booth for teams
# #     gl = UserProfile.objects.get(id=gl_id)
# #     participant_list = gl.user.participant_set.all()
# #     final = [x for x in participant_list if x.firewallz==True]
# #     context = RequestContext(request)
# #     context_dict = {'final':final}
# #     return render_to_response('teamdetails.html', context_dict, context)
# # ####################################Firewallz outer booth code#######################################
# # #####################################################################################################


# # @csrf_exempt
# # @staff_member_required
# # def firewallzo_remove_people(request,gl_id):
# #     if request.POST:
# #         list_of_people_selected = request.POST.getlist('remove')
# #         selectedpeople_list = [int(x) for x in list_of_people_selected]
# #         removed_people = []
# #         for x in selectedpeople_list:
# #             participant = Participant.objects.get(id=x)
# #             participant.firewallz = False
# #             participant.save()
# #             participant_name = str(participant.name) 
# #             participant_gender = str(participant.gender[0].upper())
# #             if len(participant.events.all()): #checks if the participant has the event otherwise the lenth of the list will be zero
# #                 participant_event_list = [x.name for x in participant.events.all()]
# #                 participant_event = ','.join(participant_event_list)
# #             else:
# #                 participant_event = ''
# #             removed_people.append((participant_name,participant_gender,participant_event))
# #         gl = UserProfile.objects.get(id=gl_id)
# #         #participant_list = gl.user.participant_set.all()
# #         participant_list = gl.user.participant_set.all()
# #         approved_participant_list = [x for x in participant_list if x.firewallz == True]
# #         encoded = encode_glid(gl_id)
# #         context = RequestContext(request)
# #         context_dict = {'removed_people':removed_people,'approved_participant_list':approved_participant_list, 'gl_id':gl_id, 'encoded':encoded}
# #         return render_to_response('firewallzo_remove.html', context_dict, context)
# #     else:
# #         gl = UserProfile.objects.get(id=gl_id)
# #         participant_list = gl.user.participant_set.all()
# #         approved_participant_list = [x for x in participant_list if x.firewallz == True]
# #         encoded = encode_glid(gl_id)        
# #         context = RequestContext(request)
# #         context_dict = {'approved_participant_list':approved_participant_list, 'gl_id':gl_id,'encoded':encoded}
# #         return render_to_response('firewallzo_remove.html', context_dict, context)

# # @csrf_exempt
# # @staff_member_required
# # def firewallzo_add_participant(request,gl_id):
# #     event_list = EventNew.objects.all()
# #     c = Category.objects.get(name='other')
# #     category_list = [x for x in Category.objects.all() if x != c]
# #     category_event_list = []
# #     event_list = [x for x in event_list if x.category != category_list]
# #     category_name_list = [x.name for x in category_list]

# #     try:
# #         gl=UserProfile.objects.get(id=int(gl_id))
# #         message = ''
# #     except:
# #         return HttpResponse('try again')
# #     if request.POST:
# #         # try:
# #         #   gl=InitialRegistration.objects.get(id=int(gl_id))
# #         # except:
# #         #   return HttpResponse('Invalid Group Leader')
# #         participant_name=request.POST['name']
# #         participant_gender = request.POST['gender']
# #         participant_contact = request.POST['contact']
# #         participant_email = request.POST['email']
# #         par = request.POST.getlist('eventList')
# #         participant_event_list_final = [int(x) for x in par]
# #         participant_gl = gl.user
# #         participant_college = gl.college
# #         p = Participant(name=participant_name,phone=participant_contact,email_id=participant_email,gleader=gl.user,gender=participant_gender)
# #         p.save()
# #         #Now add events

# #         for event_id in participant_event_list_final:
# #             participant_event = EventNew.objects.get(id=event_id)
# #             p.events.add(participant_event)
# #         p.save()

# #         #save participant
# #         message="New Participant added successfully"

# #     encoded = encode_glid(gl_id)    
# #     context = RequestContext(request)
# #     context_dict = {'message':message, 'encoded':encoded,'gl_id':gl_id, 'event_list':event_list, 'category_name_list':category_name_list}
# #     return render_to_response('firewallzo_add.html', context_dict, context)
# # @csrf_exempt #currently allows only change of name and gender on firewalzz booth
# # @staff_member_required
# # def firewallzo_edit_participant(request,participant_id):
# #     try:
# #         participant=Participant.objects.get(id=int(participant_id))
# #         message = ''
# #     except:
# #         return HttpResponse('try again')
# #     if request.POST:
# #         participant.name=request.POST['name']
# #         participant.gender = request.POST['gender']
# #         participant.save()
# #         message="Participant Details changed successfully"
# #     u_id = int(participant.gleader.id)
# #     user_ob = User.objects.filter(id= u_id)[0]
# #     user_pr = UserProfile.objects.filter(user = user_ob)[0]
# #     gl_id = int(user_pr.id) 
# #     encoded = encode_glid(gl_id)
# #     context = RequestContext(request)
# #     context_dict = {'participant':participant,'message':message, 'encoded':encoded,'gl_id':gl_id}

# #     return render_to_response('firewallzo_edit.html', context_dict, context)

# # @csrf_exempt
# # @staff_member_required
# # def firewallzo_checkout(request):
# #     selectedpeople = request.session.get('selectedpeople')
# #     selectedpeople_list = selectedpeople.split()
# #     selectedpeople_list = [int(x) for x in selectedpeople_list]
# #     display_table = []
# #     for x in selectedpeople_list:
# #         participant = Participant.objects.get(id=x)
# #         participant.firewallz = True
# #         participant.save()
# #         participant_name = str(participant.name) 
# #         participant_gender = str(participant.gender)[0].upper()
# #         if len(participant.events.all()): #checks if the participant has the event otherwise the lenth of the list will be zero
# #                 participant_event = str(participant.events.all()[0].name)
# #         display_table.append((participant_name,participant_gender,participant_event))
# #     context = RequestContext(request)
# #     context_dict = {'display_table':display_table}
# #     return render_to_response('firewallzo_checkout.html', context_dict, context)

# # @csrf_exempt
# # @staff_member_required
# # def firewallzo_gl_reassign(request,gl_id):
# #     if request.POST:
# #         if str(request.POST['formtype']) == 'Finalform':
# #             newid= request.POST['newgl']
# #             newgl = Participant.objects.filter(id=newid)[0]
# #             puser = newgl.gleader
# #             glid = puser.id
# #             newuser= UserProfile.objects.filter(user=puser)[0]
# #             newuser.firstname = newgl.name
# #             newuser.lastname=''
# #             newuser.phone = int(request.POST['phone'])
# #             newuser.email_id= newgl.email_id
# #             newuser.save()
            
# #             context = RequestContext(request)
# #             context_dict = {'newgl' : newuser}
# #             return render_to_response('newglshow.html',context_dict, context)


# #         #   newglidlist = str(request.session.get('newglidlist')).split(' ')
# #         #   newglidlist = [int(x) for x in newglidlist]
# #         #   selected_participant_id=int(request.POST['newgl'])
# #         #   participant = Participant.objects.get(id= selected_participant_id)
# #         #   #creating user for participant
# #         #   final_member_list = [Participant.objects.get(id=x) for x in newglidlist]
# #         #   participant_username = str(participant.name).replace(' ','') + str(randint(100,9999))
# #         #   if participant.email_id:
# #         #       participant_email = participant.email_id
# #         #   else:
# #         #       participant_email = 'abc@abc.com'
# #         #   u = User(username=participant_username, email = participant_email)
# #         #   u.save()
# #         #   password = randint(1000,9999)
# #         #   u.set_password(password)
# #         #   #Creating InitialRegistration for participant
# #         #   participant_name = participant.name
# #         #   participant_college = participant.gleader.initialregistration_set.all()[0].college
# #         #   participant_gender = participant.gender
# #         #   participant_contact_no = participant.phone
# #         #   participant_city = participant.gleader.initialregistration_set.all()[0].city
# #         #   newgl = InitialRegistration(name=participant.name,user=u,college=participant_college,gender=participant.gender,phone=participant.phone,city =participant_city)
# #         #   newgl.save()
# #         #   #assigining the new gl to all selected people
# #         #   for x in newglidlist:
# #         #       part = Participant.objects.get(id=x)
# #         #       part.gleader = newgl.user
# #         #       part.save()
# #         #   #Generating uniquecode for new_gl
# #         #   new_gl_id = newgl.id
# #         #   gl_ida = '0'*(4-len(str(new_gl_id)))+str(new_gl_id)
# #         #   mixed = string.ascii_uppercase + string.ascii_lowercase
# #         #   count = 51
# #         #   new_encoded = ''
# #         #   for x in gl_ida:
# #         #       new_encoded = new_encoded + x
# #         #       new_encoded = new_encoded + mixed[randint(0,51)]
# #         #   #new_encoded is the unique id of the new_gl
# #         #   context = RequestContext(request)
# #         #   context_dict = {'newgl':newgl,'new_encoded':new_encoded,'password':password, 'participant_username':participant_username,'final_member_list':final_member_list}
# #         #   return render_to_response('newgl_checkout.html', context_dict, context)
# #         # else:#radio button form
# #         #   try:
# #         #       new_members_id = request.POST.getlist('newglmember')
# #         #       new_members_id = [str(x) for x in new_members_id]
# #         #       new_members_id_string = ' '.join(new_members_id)
# #         #       new_members_id = [int(x) for x in new_members_id]
# #         #   except:
# #         #       orignal_gl = UserProfile.objects.get(id=gl_id).user
# #         #       participant_list = orignal_gl.participant_set.all()
# #         #       not_approved_paticipants = [x for x in participant_list if x.firewallz != True]
# #         #       error = 'No selection made'
# #         #       context = RequestContext(request)
# #         #       context_dict = {'not_approved_participants':not_approved_participants,'error':error,'gl_id':gl_id}
# #         #       return render_to_response('newglcheckbox.html', context_dict, context)
            
# #             # request.session['newglidlist'] = new_members_id_string
# #             # new_members_list = [Participant.objects.get(id=y) for y in new_members_id]
# #             # context = RequestContext(request)
# #             # context_dict = {'new_members_list':new_members_list,'gl_id':gl_id}
# #             # return render_to_response(, context_dict, context)

# #     else:
# #         orignal_gl = UserProfile.objects.get(id=gl_id).user
# #         participant_list = orignal_gl.participant_set.all()
# #         not_approved_participants = [x for x in participant_list if x.firewallz != True]
# #         error = ''
# #         context = RequestContext(request)
# #         context_dict = {'not_approved_participants':not_approved_participants,'error':error,'gl_id':gl_id}
# #         return render_to_response('newglcheckbox.html', context_dict, context)



# # @csrf_exempt
# # @staff_member_required
# # def firewallz_fid(request):
# #     if request.POST:
# #         try:
# #             encoded=request.POST['code']
# #             decoded = encoded[0]+encoded[2]+encoded[4]+encoded[6] #taking alternative character because alphabets were random and had no meaning
# #             gl_id = int(decoded) #to remove preceding zeroes and get user profile
# #             gl = UserProfile.objects.get(id=gl_id)
# #             request.session['glidfire'] = str(gl_id)
# #         except:
# #             encoded=request.POST['code']
# #             decoded = encoded[0]+encoded[2]+encoded[4]+encoded[6] #taking alternative character because alphabets were random and had no meaning
# #             gl_id = int(decoded) #to remove preceding zeroes and get user profile
# #             gl = UserProfile.objects.get(id=gl_id)
# #             request.session['glidfire'] = str(gl_id)
# #             error="Invalid code entered " +encoded
# #             context = RequestContext(request)
# #             context_dict = {'encoded':encoded}
# #             return render_to_response('firewallzi_home.html', context_dict, context)
        
# #         if request.POST:
# #             if str(request.POST['formtype']) == 'finalform':
# #                 gl_id = int(request.session.get('glidfire'))
# #                 gl = UserProfile.objects.get(id=gl_id)
# #                 participant_list = gl.user.participant_set.all()
            
# #                 firewallz_controlz_approved = [x for x in participant_list if x.firewallz == True and x.fid != True and x.controlzpay == True]
# #                 for x in firewallz_controlz_approved:
# #                     if x.id in request.POST:
# #                         x.fid = True
# #                         x.save()
# #                 done_list = [x for x in participant_list if x.firewallz == True and x.fid == True and x.controlzpay == True]
# #                 participant_list = gl.user.participant_set.all()
# #                 firewallz_controlz_approved = [x for x in participant_list if x.firewallz == True and x.fid != True and x.controlzpay == True]
# #                 context = RequestContext(request)
# #                 context_dict = {'firewallz_controlz_approved':firewallz_controlz_approved,'done_list':done_list}
# #                 return render_to_response('firewallzi_checkout.html', context_dict, context)
        
# #             else:
# #                 gl_id = int(request.session.get('glidfire'))
# #                 gl = UserProfile.objects.get(id=gl_id)
# #                 participant_list = gl.user.participant_set.all()
# #                 firewallz_controlz_approved = [x for x in participant_list if x.firewallz == True and (x.fid)== False and x.controlzpay == True]
# #                 done_list = [x for x in participant_list if x.firewallz == True and (x.fid)== True]
# #                 context = RequestContext(request)
# #                 context_dict = {'firewallz_controlz_approved':firewallz_controlz_approved,'done_list':done_list}
# #                 return render_to_response('firewallzi_checkout.html', context_dict, context)
# #     else:
# #         context = RequestContext(request)
# #         error = ''
# #         context_dict = {'error':error}
# #         return render_to_response('firewallzi_home.html', context_dict, context)

# # @staff_member_required
# # def recnacc_dashboard(request, gl_id):
# #         gl = UserProfile.objects.get(id=gl_id)
# #         participant_list = gl.user.participant_set.all() 
# #         college = str(gl.college)
# #         gl_name = str(gl.firstname +' '+ gl.lastname)
# #         display_participants = []
# #         done_participants = []
# #         no_males=0
# #         no_females=0
# #         for p in participant_list:
# #             if p.gender[0].upper()=="M" and p.firewallz ==True and p.acco!=True:
# #                 no_males+=1
# #             elif p.gender[0].upper()=="F" and p.firewallz ==True and p.acco!=True:
# #                 no_females+=1       
# #             participant_name = str(p.name) 
# #             participant_gender = str(p.gender)[0].upper()#for using just M or F instead of fulll to save space.
# #             participant_id = int(p.id)
# #             if p.acco == True and p.room:
# #                 participant_room = str(p.room.room)+' '+p.room.bhavan.name
# #             else:
# #                 participant_room = ''
# #             # if len(p.events.all()): #checks if the participant has the event otherwise the lenth of the list will be zero
# #             #   participant_event = str(p.events.all()[0].name)
# #             # else:
# #             #   participant_event = '' #done because faculty is not assigned any event
# #             if p.firewallz == True: #list only particiants who have been approved by firewallz
# #                 display_participants.append((participant_name,participant_gender,participant_id,participant_room))
# #         done_participants = [x for x in participant_list if x.firewallz==True and x.acco==True]
# #         context = RequestContext(request)
# #         context_dict = {'done_participants':done_participants,'display_participants': display_participants, 'college':college, 'no_males':no_males, 'no_females':no_females,
# #         'gl_name':gl_name,'done_participants':done_participants, "gl_id":gl_id}
# #         return render_to_response('reconec_gl.html', context_dict, context)

# # @csrf_exempt
# # def reconec_home(request):
# #     #simple template to enter id
# #     if request.POST:
# #         try:
# #             encoded=request.POST['code']
# #             decoded = encoded[0]+encoded[2]+encoded[4]+encoded[6] #taking alternative character because alphabets were random and had no meaning
# #             gl_id = int(decoded) #to remove preceding zeroes and get user profile
# #             return redirect('regsoft:recnacc_dashboard', gl_id)
# #         except:
# #             error="Invalid code entered " +encoded
# #             context = RequestContext(request)
# #             context_dict = {'error':error}
# #             return render_to_response('reconec_home2.html', context_dict, context)

# #         # participant_list = gl.user.participant_set.all() 
# #         # college = str(gl.college)
# #         # gl_name = str(gl.firstname +' '+ gl.lastname)
# #         # display_participants = []
# #         # done_participants = []
# #         # no_males=0
# #         # no_females=0
# #         # for p in participant_list:
# #         #   if p.gender[0].upper()=="M" and p.firewallz ==True and p.acco!=True:
# #         #       no_males+=1
# #         #   elif p.gender[0].upper()=="F" and p.firewallz ==True and p.acco!=True:
# #         #       no_females+=1       
# #         #   participant_name = str(p.name) 
# #         #   participant_gender = str(p.gender)[0].upper()#for using just M or F instead of fulll to save space.
# #         #   participant_id = int(p.id)
# #         #   if p.acco == True and p.room:
# #         #       participant_room = str(p.room.room)+' '+p.room.bhavan.name
# #         #   else:
# #         #       participant_room = ''
# #         #   # if len(p.events.all()): #checks if the participant has the event otherwise the lenth of the list will be zero
# #         #   #   participant_event = str(p.events.all()[0].name)
# #         #   # else:
# #         #   #   participant_event = '' #done because faculty is not assigned any event
# #         #   if p.firewallz == True: #list only particiants who have been approved by firewallz
# #         #       display_participants.append((participant_name,participant_gender,participant_id,participant_room))
# #         # done_participants = [x for x in participant_list if x.firewallz==True and x.acco==True]
# #         # context = RequestContext(request)
# #         # context_dict = {'done_participants':done_participants,'display_participants': display_participants, 'college':college, 'no_males':no_males, 'no_females':no_females,
# #         # 'gl_name':gl_name,'done_participants':done_participants, "gl_id":gl_id}
# #         # return render_to_response('reconec_gl.html', context_dict, context)
# #     else:
# #         context = RequestContext(request)
# #         error = ''
# #         context_dict = {'error':error}
# #         return render_to_response('reconec_home2.html', context_dict, context)

# # @csrf_exempt
# # @staff_member_required
# # def acco_list(request,gl_id):

# #     #list acco with availibilty
# #     #ability to select
# #     bhavan_list= Bhavan.objects.all()
# #     initial_vacancy_display= []
# #     vacancy_display = []
# #     for bhavan in bhavan_list:
# #         if bhavan.id != 1:
# #             bhavan_name = bhavan.name
# #             rooms = bhavan.room_set.all()
# #             initial_vacancy_display.append((bhavan_name,rooms))
# #     all_rooms = []
# #     for bhavan in bhavan_list:
# #         if bhavan.id != 1:
# #             bhavan_name = bhavan.name
# #             rooms = [x for x in bhavan.room_set.all()]
# #             all_rooms += rooms
# #             if len(rooms):
# #                 vacancy_display.append((bhavan_name,rooms))
# #     gl = UserProfile.objects.get(id=gl_id)
# #     participant_list = gl.user.participant_set.all() 
# #     no_males=0
# #     no_females=0
# #     for p in participant_list:
# #         if p.gender[0].upper()=="M" and p.firewallz ==True and p.acco!=True:
# #             no_males+=1
# #         elif p.gender[0].upper()=="F" and p.firewallz ==True and p.acco!=True:
# #             no_females+=1
# #     if request.POST:
# #         try:
# #             request.POST.getlist('roomid')
# #         except:
# #             error="Invalid Room Selected"
# #             context = RequestContext(request)
# #             context_dict = {'error':error}
# #             return render_to_response('reconec_acco.html', context_dict, context)
# #         for roomid in request.POST.getlist('roomid'):
# #             # roomid=request.POST.getlist('roomid')
# #             x = roomid + 'alloted'
# #             noalloted=int(request.POST[x])
# #             roomid = int(roomid)
# #             no_males=0
# #             no_females=0
# #             for p in participant_list:
# #                 if p.gender[0].upper()=="M" and p.firewallz ==True and p.acco!=True:
# #                     no_males+=1
# #                 elif p.gender[0].upper()=="F" and p.firewallz ==True and p.acco!=True:
# #                     no_females+=1
# #             selectedroom = Room.objects.get(id=roomid)
# #             selectedroom_availibilty = selectedroom.vacancy
# #             unalloted_males = [x for x in participant_list if x.firewallz == True and x.gender[0].upper() == 'M' and x.acco != True]
# #             unalloted_females = [x for x in participant_list if x.firewallz == True and x.gender[0].upper() == 'F' and x.acco != True]
# #             if selectedroom.bhavan.name == 'MB' or selectedroom.bhavan.name == 'MB 1' or selectedroom.bhavan.name == 'MB 3' or selectedroom.bhavan.name == 'MB 4' or selectedroom.bhavan.name == 'MB 5' or selectedroom.bhavan.name == 'MB 6-1' or selectedroom.bhavan.name == 'MB 6-2'or selectedroom.bhavan.name == 'MB 9' or selectedroom.bhavan.name == 'SQ' or selectedroom.bhavan.name == 'CVR': #use or for extra bhavanas
# #                 if no_females<noalloted:
# #                     return HttpResponse('error: Alloted rooms are greater than the number of participants. <br /> <a href="http://www.bits-bosm.org/2015/regsoft/recnacc/allot/%s/">Back</a>' % gl_id)
# #                 for y in range(noalloted):
# #                     unalloted_females[y].acco=True
# #                     unalloted_females[y].room = selectedroom
# #                     selectedroom.vacancy -= 1
# #                     selectedroom.save()
# #                     unalloted_females[y].save()
            
# #             else:
# #                 if no_males<noalloted:
# #                     return HttpResponse('error: Alloted rooms are greater than the number of participants. <br /> <a href="http://www.bits-bosm.org/2015/regsoft/recnacc/allot/%s/">Back</a>' % gl_id)
# #                 for y in range(noalloted):
# #                     unalloted_males[y].acco=True
# #                     unalloted_males[y].room = selectedroom
# #                     selectedroom.vacancy -= 1
# #                     selectedroom.save()
# #                     unalloted_males[y].save()
# #         #return HttpResponse(selectedroom.vacancy)
# #         no_males=0
# #         no_females=0
# #         participant_list = gl.user.participant_set.all()
# #         for p in participant_list:
# #             if p.gender[0].upper()=="M" and p.firewallz ==True and p.acco!=True:
# #                 no_males+=1
# #             elif p.gender[0].upper()=="F" and p.firewallz ==True and p.acco!=True:
# #                 no_females+=1
# #         bhavan_list= Bhavan.objects.all()
# #         all_rooms =[]
# #         for bhavan in bhavan_list:
# #             if bhavan.id != 1:
# #                 bhavan_name = bhavan.name
# #                 rooms = [x for x in bhavan.room_set.all() if x.vacancy != 0]
# #                 all_rooms += rooms
# #                 if len(rooms):
# #                     vacancy_display.append((bhavan_name,rooms))
# #         done_participants = [x for x in participant_list if x.firewallz==True and x.acco==True]
# #         context = RequestContext(request)
# #         context_dict = {'done_participants':done_participants,'all_rooms':all_rooms,'no_males':no_males, 'no_females':no_females,"gl_id":gl_id, 'vacancy_display':vacancy_display}
# #         return render_to_response('reconec_acco.html', context_dict, context)

# #     else:
# #         done_participants = [x for x in participant_list if x.firewallz==True and x.acco==True]
# #         context = RequestContext(request)
# #         context_dict = {'done_participants':done_participants,'all_rooms':all_rooms,'vacancy_display':vacancy_display, 'no_males':no_males, 'no_females':no_females, "gl_id":gl_id}
# #         return render_to_response('reconec_acco.html', context_dict, context)
# # @staff_member_required
# # def all_bhawans(request):
# #     bhavan_list= Bhavan.objects.all()
# #     all_rooms = []
# #     for bhavan in bhavan_list:
# #         bhavan_name = bhavan.name
# #         rooms = [x for x in bhavan.room_set.all()]
# #         all_rooms += rooms
# #     context = RequestContext(request)
# #     context_dict = {'all_rooms':all_rooms}
# #     return render_to_response('all_bhavans.html', context_dict, context)

# # @csrf_exempt
# # @staff_member_required
# # def room_details(request):
# #     room_list= [x for x in Room.objects.all() if x.id != 1]
# #     room_list_mod = [(str(x.bhavan.name)+' '+str(x.room)+'#'+str(x.id),x) for x in room_list]
# #     if request.POST:
# #         roomid=str(request.POST['roomid'])
# #         roomid = int(roomid[roomid.find('#')+1:])
# #         selectedroom = Room.objects.get(id=roomid)
# #         room_participants = selectedroom.participant_set.all()
# #         gl_list = []
# #         gl_count = {}
# #         for p in room_participants:
# #             if p.gleader.initialregistration_set.all()[0] not in gl_list:
# #                 gl_list.append(p.gleader.initialregistration_set.all()[0])
# #                 gl_count[p.gleader.initialregistration_set.all()[0]] = 1
# #             else:
# #                 gl_count[p.gleader.initialregistration_set.all()[0]] += 1

# #         context = RequestContext(request)
# #         context_dict = {'gl_list':gl_list, 'room_list_mod':room_list_mod, 'gl_count':gl_count}
# #         return render_to_response('room_details.html', context_dict, context)

# #     context = RequestContext(request)
# #     context_dict = {'room_list_mod':room_list_mod}
# #     return render_to_response('room_details.html', context_dict, context)   

# # @csrf_exempt
# # @staff_member_required
# # def reconec_deallocate(request,gl_id):
# #     gl = UserProfile.objects.get(id=gl_id)
# #     alloted_people = [x for x in gl.user.participant_set.all() if x.firewallz == True and x.acco == True]
# #     if request.POST:
# #         try:
# #             list_of_people_selected = request.POST.getlist('deallocate')
# #         except:
# #             return HttpResponse('No one was selected')
# #         selected_people_list = [int(x) for x in list_of_people_selected]
# #         done_people = []
# #         for x in selected_people_list:
# #             p= Participant.objects.get(id=x)
# #             p.acco = False
# #             selected_room = p.room
# #             selected_room.vacancy += 1
# #             selected_room.save()
# #             p.room = None
# #             p.save()
# #             done_people.append(p)
# #         alloted_people = [x for x in gl.user.participant_set.all() if x.firewallz == True and x.acco == True]
# #         context = RequestContext(request)
# #         context_dict = {'done_people':done_people, 'alloted_people':alloted_people,"gl_id":gl_id}
# #         return render_to_response('reconec_deallocate.html', context_dict, context)
# #     else:
# #         done_people = []
# #         context = RequestContext(request)
# #         context_dict = {'done_people':done_people, 'alloted_people':alloted_people,"gl_id":gl_id}
# #         return render_to_response('reconec_deallocate.html', context_dict, context)
        
# # @csrf_exempt
# # @staff_member_required
# # def phonedetails(request,gl_id):
# #     gl = UserProfile.objects.get(id=gl_id)
# #     participant_list = gl.user.participant_set.all()
# #     context = RequestContext(request)
# #     context_dict = {'participant_list':participant_list}
# #     return render_to_response('reconec_phone.html', context_dict, context)


# # @csrf_exempt
# # @staff_member_required
# # def reconec_checkout(request,gl_id):
# #     #simple template to enter id
# #     postcheck = False
# #     if request.POST:
# #         postcheck = True
# #         try:
# #             list_of_people_selected = request.POST.getlist('checkout')
# #         except:
# #             return HttpResponse('error')

# #         selectedpeople_list = [int(x) for x in list_of_people_selected]
# #         display_table = []
# #         for x in selectedpeople_list:
# #             participant = Participant.objects.get(id=x)
# #             participant_room = participant.room
# #             participant_room.vacancy += 1
# #             participant_room.save()
# #             participant.room = Room.objects.get(id=1)
# #             croom = Room.objects.get(id=1)
# #             croom.vacancy -= 1
# #             croom.save()
# #             participant.save()
# #             participant_name = str(participant.name) 
# #             participant_gender = str(participant.gender)[0].upper()
# #             if len(participant.events.all()): #checks if the participant has the event otherwise the lenth of the list will be zero
# #                     participant_event = str(participant.events.all()[0].name)
# #             else:
# #                 participant_event = ''
# #             display_table.append((participant_name,participant_gender,participant_event))
# #         gl = UserProfile.objects.get(id=gl_id)
# #         participant_list = gl.user.participant_set.all() 
# #         college = str(gl.college)
# #         gl_name = str(gl.firstname + ' ' + gl.lastname)
# #         final_participants = [x for x in participant_list if x.firewallz==True and x.acco==True and x.room.bhavan.id != 1]
# #         context = RequestContext(request)
# #         context_dict = {'college':college,"gl_id":gl_id,'display_table':display_table, 'postcheck':postcheck}
# #         return render_to_response('reconec_checkout.html', context_dict, context)


# #     else:
# #         gl = UserProfile.objects.get(id=gl_id)
# #         participant_list = gl.user.participant_set.all() 
# #         college = str(gl.college)
# #         gl_name = str(gl.firstname + ' ' + gl.lastname)
# #         final_participants = [x for x in participant_list if x.firewallz==True and x.acco==True and x.room.bhavan.id != 1]
# #         context = RequestContext(request)
# #         context_dict = {'final_participants':final_participants, 'college':college,"gl_id":gl_id}
# #         return render_to_response('reconec_checkout.html', context_dict, context)
# # @staff_member_required
# # def college_in_bhavan(request):
# #     colleges = {}
# #     bhavan_list = Bhavan.objects.all()

# #     for bhavan in bhavan_list:
# #         colleges[bhavan.name] = []
# #         for room in bhavan.room_set.all():
# #             for participant in room.participant_set.all():
# #                 participant_college = participant.gleader.userprofile_set.all()[0].college
# #                 if participant_college not in colleges[bhavan.name]:
# #                     colleges[bhavan.name].append(participant_college)
# #     display = []
# #     for x in colleges:
# #         for y in colleges[x]:
# #             display.append((x,y))

# #     context = RequestContext(request)
# #     context_dict = {'display':display}
# #     return render_to_response('reconec_bhavanwise.html', context_dict, context)

# # @csrf_exempt
# # def receipt(request):
# #     if request.POST:
# #         try:
# #             encoded=request.POST['code']
# #             decoded = encoded[0]+encoded[2]+encoded[4]+encoded[6] #taking alternative character because alphabets were random and had no meaning
# #             gl_id = int(decoded) #to remove preceding zeroes and get user profile
# #             gl = UserProfile.objects.get(id=gl_id)
# #             if encoded == "":
# #                 college = request.POST['college']
# #                 gl = UserProfile.objects.get(college=college)           
# #         except:
# #             error="Invalid code entered " +encoded
# #             context = RequestContext(request)
# #             context_dict = {'error':error}
# #             return render_to_response('controlzhome.html', context_dict, context)
# #         college = gl.college
# #         uid = encoded
# #         people = [x for x in gl.user.participant_set.all() if x.firewallz == True and x.controlzpay != True]
# #         done_participants = [x for x in gl.user.participant_set.all() if x.firewallz == True and x.controlzpay == True]
# #         request.session['uid'] = encoded
# #         # count=0
# #         # for ppl in people:
# #         #   if ppl.controlzpay == True:
# #         #       count+=1
# #         #error = ''
# #         #if len(people)==0:
# #             #error="No receipt can be generated now."
# #             #context = RequestContext(request)
# #             #context_dict = {'error':error}
# #             #return render_to_response('controlzhome.html', context_dict, context)

# #         context = RequestContext(request)
# #         context_dict = {'people':people, 'done_participants':done_participants,'gl_id':gl.id,'encoded':encoded}
# #         return render_to_response('controlgl.html', context_dict, context)      


# #     else:
# #         context = RequestContext(request)
# #         colleges = UserProfile.objects.order_by('college')
# #         context_dict = {'users':colleges}
# #         return render_to_response('controlzhome.html', context_dict, context)

# # def controlz_lists(request):
# #     participants = None
# #     if request.POST:
# #         event = request.POST['sport']
# #         user = request.POST['college']
# #         all_participants = Participant.objects.all()
# #         if event == "":
# #             events = EventNew.objects.all()
# #             eventwise = all_participants
# #             if user == "":
# #                 participants = eventwise
# #             elif user != "":
# #                 userid = int(user.rsplit('| ', 1)[1])
# #                 participants = [x for x in eventwise if x.gleader.id == userid]

# #         elif event != "":
# #             eventid = int(event.rsplit('| ', 1)[1])
# #             event = EventNew.objects.get(id=eventid)
# #             eventwise = [x for x in all_participants if event in x.events.all()]
# #             if user == "":
# #                 participants = eventwise
# #                 participants.sort(key=lambda x: x.gleader.userprofile_set.last().college)
# #             elif user != "":
# #                 userid = int(user.rsplit('| ', 1)[1])
# #                 participants = [x for x in eventwise if x.gleader.id == userid]
# #         # eventwise = [x for x in all_participants if events in x.events.all()]
# #         # all_participants = Participant.objects.filter(controlzpay=True)
# #         # participants = [x for x in all_participants if x.gleader == college and event in x.event_set.all()]
        
# #     users = [x for x in UserProfile.objects.all()]
# #     sports = [x for x in EventNew.objects.all()]
# #     context = {
# #         'users':users,
# #         'sports':sports,
# #         'participants':participants,
# #     }
# #     return render(request, 'controlz_list.html', context)

# # @csrf_exempt
# # def enter_denominations(request,gl_id):
# #     if request.POST:
# #         gl = UserProfile.objects.get(id=gl_id)
# #         list_of_people_selected = request.POST.getlist('left')
# #         selectedpeople_list = [int(x) for x in list_of_people_selected]
# #         display_table = []
# #         for x in selectedpeople_list:
# #             participant = Participant.objects.get(id=x)
# #             display_table.append(participant)
    
# #     #people = [x for x in gl.user.participant_set.all() if x.firewallz == True and x.controlzpay != True and x.coach != True]
# #     #bill_no_raw = len(Bill.objects.all()) + 1
# #     #rec = '0'*(4-len(str(bill_no_raw)))+str(bill_no_raw)
# #     number_of_participants = len(selectedpeople_list)
# #     register=750
# #     amount=750*number_of_participants
# #     return render_to_response('bill_template.html',{'college':gl.college,'number_of_participants':number_of_participants,'register':register,'amount':amount,'gl_id':gl.id,'display_table':display_table})

# # # @csrf_exempt
# # # def generate_receipt(request,gl_id):  
# #     # gl=UserProfile.objects.get(id=gl_id)
# #     # if request.POST:
# #         # if str(request.POST['formtype']) == 'finalform':
# #             # bill_part = request.POST['left']
# #             # college = gl.college
# #             # participant = Participant.objects.filter(bill_id=bill_part)
            
                
# #     # encoded = encode_glid(gl_id)
# #     # #billno = request.POST['billid']
# #     # gl=UserProfile.objects.get(id=gl_id)
# #     # participant_list = gl.user.participant_set.all()
# #     # b_list=[]
# #     # for p in participant_list:    
# #         # if p.firewallz == True and p.controlzpay==True:
# #             # if str(p.bill_id) not in b_list:
# #                 # bid = str(p.bill_id)
# #                 # b_list.append(bid)
    
# #     # context = RequestContext(request)
# #     # context_dict = {'b_list':b_list}
# #     # # # p = Participant.objects.filter(gleader=gl)
# #         # # # for x in p:
# #             # # # x.controlzpay = False
# #             # # # x.bill_id = None
# #             # # # x.fid = False
        
# #         # # # a = Bill.objects.filter(number=billno)[0]
# #         # # # a.remove()
# #         # # #return render_to_response('revertbill.html',{'message':'This Bill has been cancelled'} )
# #     # return render_to_response('revertbill.html', context_dict, context)
    
# # @csrf_exempt
# # def generate_receipt(request,gl_id):
# #     if request.POST:
# #         # n1000 = request.POST['n_1000']
# #         # n500 = request.POST['n_500']
# #         # n100 = request.POST['n_100']
# #         # n50 = request.POST['n_50']
# #         # n20 = request.POST['n_20']
# #         # n10 = request.POST['n_10']
# #         gl = UserProfile.objects.get(id=gl_id)
# #         list_of_people_selected = request.POST.getlist('left')
# #         selectedpeople_list = [int(x) for x in list_of_people_selected]
# #         register=750
# #         number_of_participants = len(selectedpeople_list)
        
# #         amount=750*number_of_participants
# #         ddno = request.POST['dd']
        
# #     #calculationg amount
        
# #     #now make Bill
        
# #         a = Bill()
# #         # a.notes_1000= n1000
# #         # a.notes_500= n500
# #         # a.notes_100= n100
# #         # a.notes_50= n50
# #         # a.notes_20= n2
# #         # a.notes_10= n10
# #         a.draft_number = ddno
# #         a.gleader = gl.firstname + ' ' + gl.lastname
# #         a.college = gl.college
# #         #a.number = bill_no_raw 
# #         a.amount = amount
# #         a.save()
# #         rec = '0'*(4-len(str(a.id)))+str(a.id)
        
# #         display_table = []
# #         #bill_no_raw = len(Bill.objects.all()) + 1
# #         for x in selectedpeople_list:
# #             participant = Participant.objects.get(id=x)
# #             participant.controlzpay= True
# #             participant.bill_id = a.id
# #             participant.save()
        
# #         uid = request.session['uid']
        
# #         return render_to_response('controlz_gen_bill.html',{'college':gl.college,'uid':uid,'register':register,'amount':amount,'receiptno':rec,'gl_id':gl.id})


# # @csrf_exempt
# # def print_receipt(request,gl_id):
# #     if request.POST:
# #         college=request.POST['college']
# #         uid=request.POST['uid']
# #         register=request.POST['register']
# #         amount=request.POST['amount']
# #         rec=request.POST['receiptno']
# #         return render_to_response('receipt.html',{'college':college,'uid':uid,'register':register,'amount':amount,'receiptno':rec})
        
# # @csrf_exempt
# # def controlz_edit_participant(request,participant_id):
# #     try:
# #         participant=Participant.objects.get(id=int(participant_id))
# #         message = ''
# #     except:
# #         return HttpResponse('try again')
# #     #participant_selected_events = [event for event in participant.events.all()]
# #     p = participant
# #     event_list = EventNew.objects.all()
# #     #c = Category.objects.get(name='other')
# #     #category_list = [x for x in Category.objects.all() if x != c]
# #     #category_event_list = []
# #     ##event_list = [x for x in event_list if x.category != c]
# #     ##category_name_list = [x.name for x in category_list]
# #     participant_event_list = participant.events.all()
# #     event_add_list = [x for x in event_list if x not in participant_event_list]

# #     if request.POST:
# #         try:
# #             addorremove = request.POST['addorremove']
# #         except:
# #             return HttpResponse('error')
# #         if addorremove == 'add':
# #             selected_event_name = request.POST['eventselected']
# #             selected_event = EventNew.objects.get(name=selected_event_name)
# #             p.events.add(selected_event)
# #             p.save()
# #             message="Participant Details changed successfully"
# #         elif addorremove == 'remove':
# #             selected_event_name = request.POST['eventselected']
# #             selected_event = EventNew.objects.get(name=selected_event_name)
# #             p.events.remove(selected_event)
# #             p.save()
# #             message="Participant Details changed successfully"
# #     participant_event_list = participant.events.all()
# #     event_add_list = [x for x in event_list if x not in participant_event_list]
# #     gl_id = participant.gleader.id
# #     encoded = encode_glid(gl_id)
# #     context = RequestContext(request)
# #     context_dict = {'event_add_list':event_add_list,'participant':participant,'message':message, 'encoded':encoded,'gl_id':gl_id,'participant_event_list':participant_event_list}

# #     return render_to_response('controlz_edit.html', context_dict, context)

# # @csrf_exempt
# # def controlz_sport_leader(request,participant_id):
# #     try:
# #         participant=Participant.objects.get(id=int(participant_id))
# #         message = ''
# #     except:
# #         return HttpResponse('try again')
# #     #participant_selected_events = [event for event in participant.events.all()]
# #     p = participant
# #     event_list = EventNew.objects.all()
# #     #c = Category.objects.get(name='other')
# #     #category_list = [x for x in Category.objects.all() if x != c]
# #     #category_event_list = []
# #     #event_list = [x for x in event_list if x.category != c]
# #     #category_name_list = [x.name for x in category_list]
# #     participant_event_list = participant.events.all()
# #     participant_sport_leader = participant.sport_leader
# #     #event_add_list = [x for x in event_list if x not in participant_event_list]

# #     if request.POST:
# #         selected_event_name = request.POST['eventselected']
# #         phoneno = request.POST['phonen']
# #         selected_event = EventNew.objects.get(name=selected_event_name)
# #         p.sport_leader = selected_event_name
# #         p.phone = phoneno
# #         p.save()
# #         message="Successfully made sport leader."
# #         usr_ob = participant.gleader
# #         user_ob= UserProfile.objects.filter(user = usr_ob)[0]
# #         gl_id = user_ob.id
# #         encoded = encode_glid(gl_id)
# #         #participant_event_list = participant.events.all()
# #         #participant_sport_leader = participant.sport_leader
# #         context = RequestContext(request)
# #         context_dict = {'participant':participant,'message':message, 'encoded':encoded,'gl_id':gl_id,'participant_event_list':participant_event_list,'participant_sport_leader':participant_sport_leader}
# #         return render_to_response('make_sl.html', context_dict, context)
        
# #     #participant_event_list = participant.events.all()
# #     #event_add_list = [x for x in event_list if x not in participant_event_list]
    
# #     usr_ob = participant.gleader
# #     user_ob= UserProfile.objects.filter(user = usr_ob)[0]
# #     gl_id = user_ob.id
# #     encoded = encode_glid(gl_id)
# #     context = RequestContext(request)
# #     context_dict = {'participant':participant,'message':message, 'encoded':encoded,'gl_id':gl_id,'participant_event_list':participant_event_list,'participant_sport_leader':participant_sport_leader}

# #     return render_to_response('make_sl.html', context_dict, context)
    
# # @csrf_exempt
# # @staff_member_required
# # def controlz_event_details(request):
# #     #c = Category.objects.get(name='other')
# #     event_list= EventNew.objects.all()
# #     event_list_mod = [(str(x.name)+'#'+str(x.id),x) for x in event_list]
# #     if request.POST:
# #         eventid=str(request.POST['eventid'])
# #         eventid = int(eventid[eventid.find('#')+1:])
# #         selected_event = EventNew.objects.get(id=eventid)
# #         event_participants_temp = [x for x in selected_event.participant_set.all() if x.controlzpay == True]
# #         event_participants = [(x,x.gleader.college) for x in selected_event.participant_set.all() if x.controlzpay == True]
# #         no_males = len([x for x in event_participants_temp if x.gender[0].upper() == 'M'])
# #         no_females = len(event_participants)-no_males
# #         context = RequestContext(request)
# #         context_dict = {'event_participants':event_participants, 'event_list_mod':event_list_mod,'no_males':no_males,'no_females':no_females}
# #         return render_to_response('controlz_event_details.html', context_dict, context)

# #     context = RequestContext(request)
# #     context_dict = {'event_list_mod':event_list_mod}
# #     return render_to_response('controlz_event_details.html', context_dict, context) 

# # @csrf_exempt
# # def show_prev_bills(request):
# #     all_participants = Participant.objects.filter(controlzpay = True)
# #     bill_num = Bill.objects.all()
# #     all_bills = []
# #     #if not bill_num:
# #     for x in bill_num:
# #         bill_number = x.id
# #         part = Participant.objects.filter(bill_id = x.id)[0]
# #         # # for y in part:
# #             # # if y.bill_id == bill_number:
# #                 # # group_lead = y.gleader
# #                 # # break
# #         group_lead = part.gleader
# #         gl = UserProfile.objects.get(user = group_lead)
# #         college_nm = gl.college
# #         group_lead_name = gl.firstname + " " + gl.lastname
# #         all_bills.append((bill_number,college_nm,group_lead_name))
# #     context = RequestContext(request)
# #     context_dict = {'all_bills':all_bills}
# #     return render_to_response('show_bills.html',context_dict, context)
# #     #else:
# #     #   return render_to_response('show_bills.html',{'message':'No bills are created yet'})
# # @csrf_exempt    
# # def bill_details(request, bid):
# #     all_participants = Participant.objects.all()
# #     all_parts = []
# #     for x in all_participants:
# #         if str(x.bill_id) == str(bid):
# #             part_name = x.name
# #             part_gender = x.gender
# #             part_phone = x.phone
# #             all_parts.append((part_name, part_gender, part_phone))
# #     return render_to_response('bill_details.html',{'all_parts':all_parts})  


# # @csrf_exempt
# # def controlz_cancel_bill(request, gl_id):
# #     participant_list_bill_ref=[]
# #     if request.POST:
# #         if str(request.POST['formtype']) == 'finalform':
# #             bill_part = request.POST['left']
# #             participant = Participant.objects.filter(bill_id=bill_part)
# #             for x in participant:
# #                 if x.firewallz== True and x.controlzpay == True:
# #                     x.controlzpay = False
# #                     x.bill_id = None
# #                     x.save()
# #             a = Bill.objects.filter(id=bill_part).delete()
        
# #         # if str(request.POST['formtype']) == 'partform':
# #             # bill_number = request.POST['bill_number']
# #             # participant_list_bill_ref = Participant.objects.filter(bill_id=bill_number)
                    
# #     encoded = encode_glid(gl_id)
# #     #billno = request.POST['billid']
# #     gl=UserProfile.objects.get(id=gl_id)
# #     participant_list = gl.user.participant_set.all()
# #     b_list=[]
# #     for p in participant_list:  
# #         if p.firewallz == True and p.controlzpay==True:
# #             if str(p.bill_id) not in b_list:
# #             #if p not in b_list:
# #                 bid = str(p.bill_id)
# #                 p_ref_name = str(p.name)
# #                 b_list.append((bid,p_ref_name))
    
# #     context = RequestContext(request)
# #     context_dict = {'b_list':b_list}
# #     # # p = Participant.objects.filter(gleader=gl)
# #         # # for x in p:
# #             # # x.controlzpay = False
# #             # # x.bill_id = None
# #             # # x.fid = False
        
# #         # # a = Bill.objects.filter(number=billno)[0]
# #         # # a.remove()
# #         # #return render_to_response('revertbill.html',{'message':'This Bill has been cancelled'} )
# #     return render_to_response('revertbill.html', context_dict, context)
