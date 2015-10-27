from django.shortcuts import render

# Create your views here.
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
    worksheet.write(0, 4, "Author")
    worksheet.write(0, 5, "Co-Author")
        
    for i, row in enumerate(data):
        """for each object in the date list, attribute1 & attribute2
        are written to the first & second column respectively,
        for the relevant row. The 3rd arg is a failure message if
        there is no data available"""

        worksheet.write(i+1, 0, getattr(row['obj'], 'id', 'NA'))
        worksheet.write(i+1, 1, getattr(row['obj'], 'name', 'NA'))
        worksheet.write(i+1, 2, getattr(row['obj'].category , 'name', 'NA'))
        worksheet.write(i+1, 3, getattr(row['obj'], 'stub', 'NA'))
        worksheet.write(i+1, 4, getattr(row['obj'].author , 'name', 'NA'))
        worksheet.write(i+1, 5, getattr(row['obj'].co_author , 'name', 'NA'))

    workbook.close()
    filename = 'ExcelReport.xlsx'
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/ms-excel")  
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response