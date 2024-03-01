from django.db import models
from django.contrib.auth.models import User



class category(models.Model):
    name = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name
    
    
    

class post(models.Model):
    Image = models.ImageField(upload_to="blog/",default='blog/NaNN.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)   
    title = models.CharField(max_length= 255)
    content = models.TextField()
    # tag
    counted_veiws = models.IntegerField(default=0)
    category = models.ManyToManyField(category)
    status = models.BooleanField(default=False) 
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['created_date']
        
        
        
        
    def __str__(self):
        return self.title
    
    
    
