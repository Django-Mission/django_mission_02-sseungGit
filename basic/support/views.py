from django.shortcuts import render
from .models import Faq

# Create your views here.
def index(request):
    return render(request, 'index.html')

def support_list_view(request):
    faq_list = Faq.objects.all().order_by('id')
    return render(request, 'support/support_list.html', {'faq_list' : faq_list} )
    
def support_detail_view(request,id):
    faq_detail = Faq.objects.get(id=id)
    print(faq_detail)
    return render(request, 'support/support_detail.html', {'faq_detail' : faq_detail})
