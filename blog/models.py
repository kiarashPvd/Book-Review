from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class category(models.Model):
    name = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name
    
    
    

class post(models.Model):
    Image = models.ImageField(upload_to="blog/",default='blog/NaNN_TraECc1.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)   
    title = models.CharField(max_length= 255)
    content = models.TextField()
    tags = TaggableManager()
    counted_veiws = models.IntegerField(default=0)
    category = models.ManyToManyField(category,default='none')
    status = models.BooleanField(default=False) 
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['created_date']
        
        
        
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse ('blog:single',kwargs={'pid':self.id})
    
    
class Comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    
    
    
    
