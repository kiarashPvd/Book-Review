from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import post


def blog_view(request,**kwargs):
    posts = post.objects.filter(status=1)
    if kwargs.get('cat_name')!=None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!=None:
        posts = posts.filter(author__username=kwargs['author_username'])
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = post.objects.filter(status=1).order_by('created_date')
    Post = get_object_or_404 (posts,pk=pid)
    next_post = posts.filter(created_date__lt=Post.created_date).last()
    previous_post = posts.filter(created_date__gt=Post.created_date).first()
    context = {'post': Post,'next_post': next_post,'previous_post': previous_post,}
    return render(request, 'blog/blog-single.html',context)

def blog_search(request):
    posts = post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def test(request):#,pid
    #Post = get_object_or_404 (post,pk=pid)
    #context = {'post': Post}
    return render (request, 'blog/test.html')#,context