from django.shortcuts import render
from django.http import HttpResponse


def blog_view(request):
    return render(request, 'blog/blog-home.html')

def single_view(request):
    context = {'title':'coffe is great!','content':'for having good day drink coffe','author':'kiarash payervand'}
    return render(request, 'blog/blog-single.html',context)