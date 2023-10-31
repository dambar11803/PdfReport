from django.shortcuts import render 
from django.http import HttpResponse 
from django.template.loader import get_template 
from xhtml2pdf import pisa 

# Create your views here.

def Homepage(request):
    return render(request, 'homepage.html')

def Document(request):
    return render(request, 'doc.html')

def pdfreport_create(request):
    
    template_path = 'pdfreport.html'
    context = {'myvar': 'this is your template context'}
   
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    
def viewreport(request):
    return render(request, 'pdfreport.html')    
