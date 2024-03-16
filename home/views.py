from django.shortcuts import render
from django.http import HttpResponse
from home.forms import NameForm,ContactForm


def index_view(request):
    return render(request, 'home/index.html')

def about_view(request):
    return render(request, 'home/about.html')

def contact_view(request):
    return render(request, 'home/contact.html')

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message= form.cleaned_data['message']
            print(name, subject, email, message)
            return HttpResponse('success')
            
        else:
            return HttpResponse('failure')
        
        
    
    form = ContactForm()    
    return render(request, 'test.html',{"form": form})

