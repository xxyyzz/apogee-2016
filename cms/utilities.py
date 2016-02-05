from django.shortcuts import render

# Create your views here.
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

def paper_stats_xlsx(request):
    from django.http import HttpResponse, HttpResponseRedirect
    import xlsxwriter

    try:
        import cStringIO as StringIO
    except ImportError:
        import StringIO
    a_list = []

    from registrations.models import Paper
    papers = Paper.objects.all()

    for p in papers:
        a_list.append({'obj': p})
    data = sorted(a_list, key=lambda k: k['obj'].category)
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('new-spreadsheet')
    date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

    worksheet.write(0, 0, "Paper ID")
    worksheet.write(0, 1, "Paper Name")
    worksheet.write(0, 2, "Category")
    worksheet.write(0, 3, "Reference Code")
    worksheet.write(0, 4, "Address")
    worksheet.write(0, 5, "Author Name")
    worksheet.write(0, 6, "Author Phone")
    worksheet.write(0, 7, "Author Email")
    worksheet.write(0, 8, "Author College")
    worksheet.write(0, 9, "Co-Author Name")
    worksheet.write(0, 10, "Co-Author Phone")
    worksheet.write(0, 11, "Co-Author Email")
    worksheet.write(0, 12, "Co-Author College")
    worksheet.write(0, 13, "Paper Submitted?")

    for i, row in enumerate(data):
        """for each object in the date list, attribute1 & attribute2
        are written to the first & second column respectively,
        for the relevant row. The 3rd arg is a failure message if
        there is no data available"""

        worksheet.write(i+1, 0, deepgetattr(row['obj'], 'id', 'NA'))
        worksheet.write(i+1, 1, deepgetattr(row['obj'], 'name', 'NA'))
        worksheet.write(i+1, 2, deepgetattr(row['obj'] , 'category.name', 'NA'))
        worksheet.write(i+1, 3, deepgetattr(row['obj'], 'stub', 'NA'))
        worksheet.write(i+1, 4, deepgetattr(row['obj'], 'address', 'NA'))
        worksheet.write(i+1, 5, deepgetattr(row['obj'] , 'author.name', 'NA'))
        worksheet.write(i+1, 6, deepgetattr(row['obj'] , 'author.phone', 'NA'))
        worksheet.write(i+1, 7, deepgetattr(row['obj'] , 'author.email', 'NA'))
        worksheet.write(i+1, 8, deepgetattr(row['obj'] , 'author.college.name', 'NA'))
        worksheet.write(i+1, 9, deepgetattr(row['obj'] , 'co_author.name', 'NA'))
        worksheet.write(i+1, 10, deepgetattr(row['obj'] , 'co_author.phone', 'NA'))
        worksheet.write(i+1, 11, deepgetattr(row['obj'] , 'co_author.email', 'NA'))
        worksheet.write(i+1, 12, deepgetattr(row['obj'] , 'co_author.college.name', 'NA'))
        worksheet.write(i+1, 13, "Yes" if row['obj'].paper else "No")

    workbook.close()
    filename = 'ExcelReport.xlsx'
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

def project_stats_xlsx(request):
    from django.http import HttpResponse, HttpResponseRedirect
    import xlsxwriter

    try:
        import cStringIO as StringIO
    except ImportError:
        import StringIO
    a_list = []

    from registrations.models import Project
    papers = Project.objects.all()

    for p in papers:
        a_list.append({'obj': p})
    data = sorted(a_list, key=lambda k: k['obj'].assoc)
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('new-spreadsheet')
    date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

    worksheet.write(0, 0, "Project ID")
    worksheet.write(0, 1, "Project Name")
    worksheet.write(0, 2, "Category")
    worksheet.write(0, 3, "Assoc")
    worksheet.write(0, 4, "Reference Code")
    worksheet.write(0, 5, "Leader Name")
    worksheet.write(0, 6, "Leader Phone")
    worksheet.write(0, 7, "Leader Email")
    worksheet.write(0, 8, "Leader College")
    for i in range(5):
        worksheet.write(0, 9+4*i, "Member "+str(i+1)+" Names")
        worksheet.write(0, 10+4*i, "Member "+str(i+1)+" Phone")
        worksheet.write(0, 11+4*i, "Member "+str(i+1)+" Email")
        worksheet.write(0, 12+4*i, "Member "+str(i+1)+" College")

    for i, row in enumerate(data):
        """for each object in the date list, attribute1 & attribute2
        are written to the first & second column respectively,
        for the relevant row. The 3rd arg is a failure message if
        there is no data available"""

        worksheet.write(i+1, 0, deepgetattr(row['obj'], 'id', 'NA'))
        worksheet.write(i+1, 1, deepgetattr(row['obj'], 'name', 'NA'))
        worksheet.write(i+1, 2, deepgetattr(row['obj'], 'category.name', 'NA'))
        worksheet.write(i+1, 3, deepgetattr(row['obj'], 'assoc.name', 'NA'))
        worksheet.write(i+1, 4, deepgetattr(row['obj'], 'stub', 'NA'))
        worksheet.write(i+1, 5, deepgetattr(row['obj'], 'leader.name', 'NA'))
        worksheet.write(i+1, 6, deepgetattr(row['obj'], 'leader.phone', 'NA'))
        worksheet.write(i+1, 7, deepgetattr(row['obj'], 'leader.email', 'NA'))
        worksheet.write(i+1, 8, deepgetattr(row['obj'], 'leader.college.name', 'NA'))
        for n, member in enumerate(row['obj'].members.all()):
            worksheet.write(i+1, 9+4*n, deepgetattr(member, 'name', 'NA'))
            worksheet.write(i+1, 10+4*n, deepgetattr(member, 'phone', 'NA'))
            worksheet.write(i+1, 11+4*n, deepgetattr(member, 'email', 'NA'))
            worksheet.write(i+1, 12+4*n, deepgetattr(member, 'college.name', 'NA'))

    workbook.close()
    filename = 'ExcelReport.xlsx'
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

def aic_stats_xlsx(request):
    from django.http import HttpResponse, HttpResponseRedirect
    import xlsxwriter

    try:
        import cStringIO as StringIO
    except ImportError:
        import StringIO
    a_list = []

    from aic2016.models import AicSubmission
    entries = AicSubmission.objects.all()

    for p in entries:
        a_list.append({'obj': p})
    data = sorted(a_list, key=lambda k: k['obj'].id)
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('new-spreadsheet')
    date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

    worksheet.write(0, 0, "Solution ID")
    worksheet.write(0, 1, "Problem Statement")
    worksheet.write(0, 2, "Solution URL")
    worksheet.write(0, 3, "Leader Name")
    worksheet.write(0, 4, "Leader Phone")
    worksheet.write(0, 5, "Leader Email")
    worksheet.write(0, 6, "Leader YOS")
    worksheet.write(0, 7, "Leader College")
    for i in range(3):
        worksheet.write(0, 8+5*i, "Member "+str(i+1)+" Names")
        worksheet.write(0, 9+5*i, "Member "+str(i+1)+" Phone")
        worksheet.write(0, 10+5*i, "Member "+str(i+1)+" Email")
        worksheet.write(0, 11+5*i, "Member "+str(i+1)+" YOS")
        worksheet.write(0, 12+5*i, "Member "+str(i+1)+" College")

    for i, row in enumerate(data):
        """for each object in the date list, attribute1 & attribute2
        are written to the first & second column respectively,
        for the relevant row. The 3rd arg is a failure message if
        there is no data available"""

        worksheet.write(i+1, 0, deepgetattr(row['obj'], 'id', 'NA'))
        worksheet.write(i+1, 1, deepgetattr(row['obj'], 'get_problem_statement_display()', 'NA'))
        worksheet.write(i+1, 2, deepgetattr(row['obj'], 'solution.url', 'NA'))
        worksheet.write(i+1, 3, deepgetattr(row['obj'], 'leader.name', 'NA'))
        worksheet.write(i+1, 4, deepgetattr(row['obj'], 'leader.phone', 'NA'))
        worksheet.write(i+1, 5, deepgetattr(row['obj'], 'leader.email', 'NA'))
        worksheet.write(i+1, 6, deepgetattr(row['obj'], 'leader.yos', 'NA'))
        worksheet.write(i+1, 7, deepgetattr(row['obj'], 'leader.college.name', 'NA'))
        for n, member in enumerate(row['obj'].members.all()):
            worksheet.write(i+1, 8+5*n, deepgetattr(member, 'name', 'NA'))
            worksheet.write(i+1, 9+5*n, deepgetattr(member, 'phone', 'NA'))
            worksheet.write(i+1, 10+5*n, deepgetattr(member, 'email', 'NA'))
            worksheet.write(i+1, 11+5*n, deepgetattr(member, 'yos', 'NA'))
            worksheet.write(i+1, 12+5*n, deepgetattr(member, 'college.name', 'NA'))

    workbook.close()
    filename = 'ExcelReport.xlsx'
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

def ambassador_stats_xlsx(request):
    from django.http import HttpResponse, HttpResponseRedirect
    import xlsxwriter

    try:
        import cStringIO as StringIO
    except ImportError:
        import StringIO
    a_list = []

    from registrations.models import CampusAmbassador
    entries = CampusAmbassador.objects.all()

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

def participant_stats_xlsx(request):
    from django.http import HttpResponse, HttpResponseRedirect
    import xlsxwriter

    try:
        import cStringIO as StringIO
    except ImportError:
        import StringIO
    a_list = []

    from backend.models import Participant
    entries = Participant.objects.all()

    for entry in entries:
        a_list.append({'obj': entry})
    data = sorted(a_list, key=lambda k: k['obj'].id)
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('new-spreadsheet')
    date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

    worksheet.write(0, 0, "User ID")
    worksheet.write(0, 1, "Name")
    worksheet.write(0, 2, "Gender")
    worksheet.write(0, 3, "College")
    worksheet.write(0, 4, "City")
    worksheet.write(0, 5, "Email ID")
    worksheet.write(0, 6, "Phone")
    worksheet.write(0, 7, "Alternate Phone")
    worksheet.write(0, 8, "Email Verified?")
    worksheet.write(0, 9, "PCR Approval?")
    worksheet.write(0, 10, "Fee Paid?")

    for i, row in enumerate(data):
        """for each object in the date list, attribute1 & attribute2
        are written to the first & second column respectively,
        for the relevant row. The 3rd arg is a failure message if
        there is no data available"""

        worksheet.write(i+1, 0, deepgetattr(row['obj'], 'id', 'NA'))
        worksheet.write(i+1, 1, deepgetattr(row['obj'], 'name', 'NA'))
        worksheet.write(i+1, 2, deepgetattr(row['obj'], 'gender', 'NA'))
        worksheet.write(i+1, 3, deepgetattr(row['obj'], 'college.name', 'NA'))
        worksheet.write(i+1, 4, deepgetattr(row['obj'], 'city', 'NA'))
        worksheet.write(i+1, 5, deepgetattr(row['obj'], 'email_id', 'NA'))
        worksheet.write(i+1, 6, deepgetattr(row['obj'], 'phone_one', 'NA'))
        worksheet.write(i+1, 7, deepgetattr(row['obj'], 'phone_two', 'NA'))
        worksheet.write(i+1, 8, deepgetattr(row['obj'], 'email_verified', 'NA'))
        worksheet.write(i+1, 9, deepgetattr(row['obj'], 'pcr_approval', 'NA'))
        worksheet.write(i+1, 10, deepgetattr(row['obj'], 'fee_paid', 'NA'))

    workbook.close()
    filename = 'ExcelReport.xlsx'
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response
