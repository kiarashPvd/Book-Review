from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import post


def blog_view(request):
    posts = post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = post.objects.filter(status=1)
    Post = get_object_or_404 (posts,pk=pid)
    context = {'post': Post}
    return render(request, 'blog/blog-single.html',context)

#def test(request,pid):
    #Post = get_object_or_404 (post,pk=pid)
    #context = {'post': Post}
    # return render (request, 'test.html',context)