from django import template
from blog.models import post
from blog.models import category
register = template.Library()


@register.inclusion_tag('home/home-lastest-post.html')
def lastestpost():
    posts = post.objects.filter(status=1).order_by('published_date')[:6]
    return {'posts':posts  }