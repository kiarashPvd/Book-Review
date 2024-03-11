from django import template
from blog.models import post
register = template.Library()


@register.inclusion_tag('home/home-latest-post.html')
def latestpost():
    posts = post.objects.filter(status=1).order_by('published_date')[:6]
    return {'posts':posts  }