from django import template
from blog.models import post
register = template.Library()

@register.simple_tag(name="totalposts")
def function():
    posts = post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name="posts")
def function():
    posts = post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg = 70):
    return value[:arg] + '...'

@register.inclusion_tag('blog/blog-popularposts.html')
def popularposts():
    posts = post.objects.filter(status=1).order_by('-counted_veiws')[:4]
    return {'posts':posts  }