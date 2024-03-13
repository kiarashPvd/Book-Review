from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return render(request, 'home/index.html')

def about_view(request):
    return render(request, 'home/about.html')

def contact_view(request):
    return render(request, 'home/contact.html')

def test_view(request):
    if request.method == 'POST':
       print( request.POST.GET('name'))
        
    return render(request, 'test.html',{})

