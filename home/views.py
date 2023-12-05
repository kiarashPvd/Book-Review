from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return render(request, 'index.html')
def about_view(request):
    return HttpResponse('در این مکان همه چیز ازاد است به جز اسلام و مواد مخدر و خلاف') 

def contact_view(request):
    return HttpResponse(' برای ورود مستقیما با پادشاه کیارش تماس بگیرید') 
# Create your views here.
