from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return HttpResponse(' <h1>سلام به کیا توپیا خوش امدید </h1>(ورود ارمین و کسانی که ویزا ندارن ممنوع (به جز کوروش))') 

def about_view(request):
    return HttpResponse('در این مکان همه چیز ازاد است به جز اسلام و مواد مخدر و خلاف') 

def contact_view(request):
    return HttpResponse(' برای ورود مستقیما با پادشاه کیارش تماس بگیرید') 
# Create your views here.
