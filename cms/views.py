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

    workbook.close()
    filename = 'ExcelReport.xlsx'
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/ms-excel")  
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response