from django.shortcuts import render
from django.http import HttpResponse
from blog.models import post


def blog_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    context = {'title':'coffe is great!','content':'for having good day drink coffe','author':'kiarash payervand'}
    return render(request, 'blog/blog-single.html',context)

def test(request):
    posts = post.objects.all()
    context = {'posts': posts}
    return render (request, 'test.html',context)