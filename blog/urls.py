from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('', blog_view, name= 'blog'),
    path('<int:pid>', blog_single, name= 'single'),
    path('category/<str:cat_name>', blog_view, name= 'category'),
    path('test',test, name= 'test')
]
