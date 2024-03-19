from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.forms import NameForm,ContactForm,NewsLetterForm
from django.contrib import messages


def index_view(request):
    return render(request, 'home/index.html')

def about_view(request):
    return render(request, 'home/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your informations submited successfully")
        else:
            messages.error(request,"An error occurred")
    else:
        form = ContactForm()
    return render(request, 'home/contact.html',{"form": form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your informations submited successfully")
        else:
            messages.error(request,"An error occurred")
    else:
        form = NewsLetterForm()
    return render(request, 'home/index.html',{"form": form})
    
    




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

